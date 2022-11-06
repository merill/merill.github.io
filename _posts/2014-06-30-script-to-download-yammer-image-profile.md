---
id: 868
title: Script to Download Yammer Image Profile
date: 2014-06-30T14:37:01+00:00


guid: https://merill.net/?p=868
permalink: /2014/06/script-to-download-yammer-image-profile/
dsq_thread_id:
  - "2806524283"
categories:
  - Tips
tags:
  - api
  - powershell
  - yammer
---
Here's a neat script I wrote the other day to download the urls of all the user's in your Yammer network. This comes in handy when you want to re-use the profile images that users have uploaded to Yammer.

The advantage with this script is that you don't need the app to be approved by your Yammer admin. Just create a user created app on Yammer, create a token and approve it for your profile. That's it. The token can be re-used as long as necessary.

Here's the PowerShell script that will get you there.

	<#
	.SYNOPSIS
		This script downloads the profile image urls of all the users from Yammer, creates a csv file and uploads it to the YammerProfile document library.
		Example> 	.\Download-YammerProfile.ps1 -YammerToken 05fdIb1pNwIFEBg9k34EWw -SiteUrl http://mysharepoint/site
	#>
	param(
		[Parameter(Mandatory = $True, HelpMessage='Yammer Access Token - Refer to https://developer.yammer.com/authentication/ for how to generate an access token. Eg. 05fdIb1pNwIFEBg9k34EWw')]
		[string]$YammerToken,
		[Parameter(Mandatory = $True, HelpMessage='The url of the site that will store the Yammer user profile list. E.g. http://mysharepoint/site')]
		[string]$SiteUrl
	)

	Function Main() {
		$documentLibrary = "YammerProfiles"
		$csvFile = "YammerProfiles.csv"
		
		CreateEventLogSource "MePage"
		Log "Starting Download-YammerProfile.ps1"
		try {
			$spWeb = Get-SPWeb -Identity $SiteUrl
			CreateSharePointLibrary $spWeb $documentLibrary  "Downloaded cache of Yammer profile image urls" "DocumentLibrary"
			CreateYammerProfileCsv $YammerToken $csvFile
			$spWeb = Get-SPWeb -Identity $SiteUrl #Refresh reference to avoid timeout issue when it takes a long time to download from Yammer
			UploadToSharePoint $csvFile $spWeb $documentLibrary
			
			Log "Download-YammerProfile.ps1 completed succesfully"
		}
		catch {
			[string]$errDetail = $_.ToString()
			LogError "Error occured: $errDetail"
			Write-Error $_
		}
	}

	Function CreateYammerProfileCsv($token, $csvFile){
		$page = 0
		$userCount = 0
		if (Test-Path $csvFile){ Remove-Item $csvFile }
		do {
			$page++		
			$users = GetYammerUsers $token $page
			$userCount = $users.Length
			Log "Downloading Yammer Profiles Page: $page Users: $userCount"
			for($i = 1; $i -lt $users.Length; $i++) {
				$user = $users[$i];			
				if($user.mugshot_url_template.EndsWith("no_photo.png")) { continue } #Only store valid photos			
				for($e = 0; $e -lt $user.contact.email_addresses.Length; $e++) {				
					$email = $user.contact.email_addresses[$e];
					if($email.type -eq "primary"){ #We're only interested in the telstra.com email addresses	
						$output = $email.address.ToLowerInvariant() + "," + $user.mugshot_url_template
						Write-Host $user.mugshot_url_template $email.address
						Add-Content $csvFile $output
					}
				}
			}
			Start-Sleep -s 2 #Sleep for two seconds so we don't go over Yammer's rate count of 10 req / 10 sec
		}
		while ($userCount -gt 0) # -and $page -eq 1)
	}

	Function UploadToSharePoint($fileName, $spWeb, $documentLibraryName) {
		Log "Uploading $fileName to $spWeb/$documentLibraryName"
		#Read the contents into a memory stream to prevent the file getting locked
		[byte[]]$byteArray = Get-Content -encoding byte -path $fileName	
		[void][reflection.assembly]::LoadWithPartialName("System.IO")
		$stream = [System.IO.MemoryStream]$byteArray

		$spDoc = $spWeb.GetFolder($documentLibraryName)
		$spFile = $spDoc.Files.Add($fileName, $stream, $true)
	}

	Function CreateSharePointLibrary ($Web, $LibraryName, $Description, $LibraryTemplate) {  
		$spListCollection = $spWeb.Lists   
		$spLibrary=$spWeb.Lists.TryGetList($LibraryName)
		if($spLibrary -eq $null) {
			Log -f Yellow "$LibraryName document library does not exist. Creating..."
			$spListCollection.Add($LibraryName, $Description, $LibraryTemplate)
		}
	}

	Function LoadPSSnapIn {
		$snapin = Get-PSSnapin | Where-Object {$_.Name -eq 'Microsoft.SharePoint.Powershell'}
		if ($snapin -eq $null) {
			Write-Host "Loading SharePoint Powershell Snapin"
			Add-PSSnapin "Microsoft.SharePoint.Powershell"
		}
	}

	Function ConvertToJson($jsonString) {
		[System.Reflection.Assembly]::LoadWithPartialName("System.Web.Extensions")
		$ser = New-Object System.Web.Script.Serialization.JavaScriptSerializer
		return $ser.DeserializeObject($jsonString)
	}

	Function GetYammerUsers($token, $pageNumber) {
		$users = InvokeYammerGetRequest $token "users.json?page=$pageNumber"
		return $users
	}

	Function InvokeYammerGetRequest($token, $target) { 
		# Setup the request
		$yammerApiUrl = "https://www.yammer.com/api/v1/"
		$requestUrl = $yammerApiUrl + $target
		$webRequest = [System.Net.WebRequest]::Create($requestUrl)
		$webRequest.Method = "GET"
		$webRequest.Headers.Add("Authorization", "Bearer $token")

		# Execute the request
		[System.Net.WebResponse]$resp = $webRequest.GetResponse()
		$reqstream = $resp.GetResponseStream()
		$sr = new-object System.IO.StreamReader $reqstream
		$obj = ConvertToJson $sr.ReadToEnd()
		return $obj
	}

	Function CreateEventLogSource($sourceName) {			
		try {
			if(![System.Diagnostics.Eventlog]::SourceExists($sourceName))
			{
				Write-Host "Creating event log source $sourceName"
				New-Eventlog -LogName "Application" -Source $sourceName
			}
		}
		catch {
			Write-Host "Error creating event log source $sourceName"			
			Write-Host $_
		}
	}

	Function Log($message) {
		Write-Host $message
		WriteEventLog $message $false
	}

	Function LogError($message) {	
		WriteEventLog $message $true    
	}

	Function WriteEventLog($message, $isError) {
		try {
			if($isError) {
				Write-EventLog -logname Application -source MePage -eventid 4002 -EntryType Error -Message $message
			}
			else {
				Write-EventLog -logname Application -source MePage -eventid 4001 -EntryType Information -Message $message
			}
		}
		catch { #We don't want the script to error out because it couldn't write to event log		
			Write-Host "Error writing message to eventlog. Message = $message"
			Write-Host $_
		}
	}

	$ErrorActionPreference = "stop"
	LoadPSSnapIn
	return Main