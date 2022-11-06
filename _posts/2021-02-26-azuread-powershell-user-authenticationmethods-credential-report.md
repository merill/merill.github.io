---
title: Azure AD PowerShell script to generate a report on authentication methods registered
  by your users
category: tips
tags:
- powershell
- report
- azuread
- graph
date: 2021-02-26 20:27:52 +0000
---
NOTE: This API has been deprecated. Please use [List userRegistrationDetails - Microsoft Graph beta](https://learn.microsoft.com/en-us/graph/api/authenticationmethodsroot-list-userregistrationdetails?view=graph-rest-beta&tabs=http) instead.

***

The new User Authentication Methods Activity report is great. Did you know it has an awesome API as well?

The [/reports/credentialUserRegistrationDetails](https://docs.microsoft.com/en-us/graph/api/resources/credentialuserregistrationdetails?view=graph-rest-beta&preserve-view=true) method let's you pull out this information quickly.

Here is a PowerShell script to extract this into a csv.

```powershell
Import-Module Microsoft.Graph.Authentication
Connect-MgGraph -Scopes 'Reports.Read.All'
$reportJson = Invoke-GraphRequest -Uri 'https://graph.microsoft.com/beta/reports/credentialUserRegistrationDetails?$top=1000' -Method GET

$summary = @()
do
{
    foreach($item in $reportJson.value)
    {
        Write-Host "Getting" $item.userPrincipalName
        $itemInfo = [pscustomobject]@{
            id = $item.id
            userPrincipalName = $item.userPrincipalName
            userDisplayName = $item.userDisplayName
            isSsprRegistered = $item.isRegistered
            isSsprEnabled = $item.isEnabled
            isSsprOrMfaCapable = $item.isCapable
            isMfaRegistered = $item.isMfaRegistered
            authMethods = $item.authMethods -join ','
            appNotification = $item.authMethods -contains "appNotification"
            appCode = $item.authMethods -contains "appCode"
            mobilePhone = $item.authMethods -contains "mobilePhone"
            alternateMobilePhone = $item.authMethods -contains "alternateMobilePhone"
            officePhone = $item.authMethods -contains "officePhone"
            email = $item.authMethods -contains "email"
            securityQuestion = $item.authMethods -contains "securityQuestion"
        }

        $summary += $itemInfo
    }
    if($null -ne $reportJson.'@odata.nextLink') { $reportJson = Invoke-GraphRequest -Uri $reportJson.'@odata.nextLink' }
} while ($null -ne $reportJson.'@odata.nextLink') 

Write-Host "Writing to CredentialUserRegistrationDetails.csv"
$summary | Export-Csv -Path .\CredentialUserRegistrationDetails.csv -NoTypeInformation
```