---
title: PowerShell script to generate a report on all Power BI workspaces and
  groups in your Microsoft 365 tenant
category: tips
tags:
  - powershell
  - report
  - powerbi
---

Here's a useful script I wrote the other day. This uses a few PowerShell modules to pull together information about all the Power BI workspaces in your Microsoft 365 tenant. This also includes the names of the Workspace/Group owners.

```powershell
#Install-Module AzureAD
#Install-Module MicrosoftPowerBIMgmt
#Connect-PowerBIServiceAccount
#Connect-AzureAD

$workspaces = Get-PowerBIWorkspace -Scope Organization -All
$wslist = @()
foreach ($ws in $workspaces) {
    $ws
    $owners = $null
    if ($ws.State -eq 'Active') { 
        if ($ws.Type -eq 'Workspace') {
            $u = $ws.Users | Where-Object AccessRight -eq 'Admin' | Select-Object UserPrincipalName
            Write-Host $u
            $owners = $u.UserPrincipalName -join ","
        }
        elseif ($ws.Type -eq 'Group') {
            $go = Get-AzureADGroupOwner -ObjectId $ws.ID 
            $owners = $go.UserPrincipalName -join "," 
        }
    } 
    $item = [ordered] @{
        Id                    = $ws.ID
        Name                  = $ws.Name
        Type                  = $ws.Type
        State                 = $ws.State
        IsReadOnly            = $ws.IsReadOnly
        IsOrphaned            = $ws.IsOrphaned
        IsOnDedicatedCapacity = $ws.IsOnDedicatedCapacity
        CapacityId            = $ws.CapacityId
        Owners                = $owners
    }
    $u = new-object PSObject -Property $item
    $wslist += $u
}
$wslist | Export-Csv .\PowerBI-Workspaces.csv -NoTypeInformation
```
Update: Brent Pearce reached out to me with this note. "However I did have to tweak it a bit. Seems the Workspaces of type ‘Workspace’ the .User.UserPrincipalName is blank but the User.Identifier is populated."
