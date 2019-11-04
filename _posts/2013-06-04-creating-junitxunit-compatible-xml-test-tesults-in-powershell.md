---
id: 854
title: Creating jUnit/xUnit compatible xml test tesults in PowerShell
date: 2013-06-04T11:08:50+00:00


guid: http://merill.net/?p=854
permalink: /2013/06/creating-junitxunit-compatible-xml-test-tesults-in-powershell/
dsq_thread_id:
  - "1357814456"
categories:
  - Tips
tags:
  - powershell
---
I originally wrote this function when I needed to create jUnit/xUnit compatible test results. The resulting xml file was then fed into the jUnit plugin in Jenkins to show the results PowerShell/[PSUnit](http://psunit.codeplex.com/) based tests.
 
	Function Write-JunitXml([System.Collections.ArrayList] $Results, [System.Collections.HashTable] $HeaderData, [System.Collections.HashTable] $Statistics, $ResultFilePath)
	{
	$template = @'
	<testsuite name="" file="">
	<testcase classname="" name="" time="">
		<failure type=""></failure>
	</testcase>
	</testsuite>
	'@
		
		$guid = [System.Guid]::NewGuid().ToString("N")
		$templatePath = [System.IO.Path]::Combine([System.IO.Path]::GetTempPath(), $guid + ".txt");
		
		$template | Out-File $templatePath -encoding UTF8
		# load template into XML object
		$xml = New-Object xml
		$xml.Load($templatePath)
		# grab template user
		$newTestCaseTemplate = (@($xml.testsuite.testcase)[0]).Clone()	
		
		$className = [System.IO.Path]::GetFileNameWithoutExtension($HeaderData.TestFileName)
		$xml.testsuite.name = $className
		$xml.testsuite.file = $HeaderData.TestFileName
		
		foreach($result in $Results) 
		{   
			$newTestCase = $newTestCaseTemplate.clone()
			$newTestCase.classname = $className
			$newTestCase.name = $result.Test.ToString()
			$newTestCase.time = $result.Time.ToString()
			if($result.Result -eq "PASS")
			{	#Remove the failure node
				$newTestCase.RemoveChild($newTestCase.ChildNodes[0]) | Out-Null
			}
			else
			{
				$newTestCase.failure.InnerText = Format-ErrorRecord $result.Reason
			}
			$xml.testsuite.AppendChild($newTestCase) > $null
		}   

		# remove users with undefined name (remove template)
		$xml.testsuite.testcase | Where-Object { $_.Name -eq "" } | ForEach-Object  { [void]$xml.testsuite.RemoveChild($_) }
		# save xml to file
		Write-Host "Path" $ResultFilePath
		
		$xml.Save($ResultFilePath)
		
		Remove-Item $templatePath #clean up
	}
