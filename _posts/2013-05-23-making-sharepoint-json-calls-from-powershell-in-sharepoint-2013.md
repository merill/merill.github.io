---
id: 809
title: Making SharePoint JSon calls from PowerShell in SharePoint 2013
date: 2013-05-23T09:01:41+00:00


guid: http://merill.net/?p=809
permalink: /2013/05/making-sharepoint-json-calls-from-powershell-in-sharepoint-2013/
dsq_thread_id:
  - "1308126763"
categories:
  - SharePoint
tags:
  - json
  - powershell
  - sharepoint 2013
---
The `Invoke-RestMethod` in PowerShell 3 doesn't send the appropriate header required by SharePoint 2013 to return JSon results. It took me a while to figure out this workaround.

    $parameter = "my search text"
    $encParam = [System.Web.HttpUtility]::UrlEncode("'$parameter'")  
    $url = "http://mysp2013site/_api/search/query?querytext=$encParam"  
    $wc = new-object System.Net.WebClient  
    $wc.UseDefaultCredentials = $true  
    $wc.Headers.Add("Accept", "application/json; odata=verbose")  
    $res = $wc.DownloadString($url)  
    $res