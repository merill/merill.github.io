---
id: 713
title: FBA Configuration Manager for SharePoint 2010
date: 2010-12-02T14:54:18+00:00


guid: http://merill.net/?p=713
permalink: /2010/12/fba-configuration-manager-for-sharepoint-2010/
dsq_thread_id:
  - "183217666"
categories:
  - SharePoint 2010
tags:
  - fba
  - powershell
  - sharepoint 2010
  - utility
---
Setting up forms based authentication in SharePoint 2010 requires making changes in three web.config files.

This utility allows you to perform the update in a single click and was inspired by the configuration manager that Steve Peschka <a href="http://blogs.technet.com/b/speschka/archive/2010/07/28/sharepoint-2010-forms-based-authentication-configuration-manager.aspx">released</a><code>.</code>

I've taken a different approach to Steve's, instead of using a feature and a timer job I directly update the config files in the local machine. To update the other machines in the farm you can use the included PowerShell script.

The utility makes a back-up of all of the web.configs before updating them. I've also included the sample membership and role providers that Steve provided.

<a href="https://merill.net/wp-content/uploads/2010/12/ConfigureMembershipProvider1.png"><img class="alignnone size-full wp-image-715" title="ConfigureMembershipProvider" src="https://merill.net/wp-content/uploads/2010/12/ConfigureMembershipProvider1.png" alt="" width="695" /></a>

The PowerShell script to perform the update uses the same engine as the UI. 

<code>
function global:Get-ScriptDirectory()
{
   $Invocation = (Get-Variable MyInvocation -Scope 1).Value
   Split-Path $Invocation.MyCommand.Path
}

$webApp = Get-SPWebApplication http://localhost:9191
$settingsPath = Join-Path (Get-ScriptDirectory) "SqlMembershipConfig.xml"
$settings = Get-Content $settingsPath
$scriptDir = Get-ScriptDirectory
$assemblyPath = Join-Path $scriptDir "FBA.dll"
Add-Type -Path $assemblyPath
[FBA.ConfigureMembershipProvider]::Configure($webApp, "Default", $settings)
</code>

The source code and release packages are available in CodePlex: <a href="http://fbaconfigmanager.codeplex.com/">http://fbaconfigmanager.codeplex.com/</a>