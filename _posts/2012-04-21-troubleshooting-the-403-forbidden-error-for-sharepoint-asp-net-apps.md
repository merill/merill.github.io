---
id: 761
title: 'Troubleshooting the &#8216;403 Forbidden&#8217; error for SharePoint &#038; ASP.NET Apps'
date: 2012-04-21T07:31:01+00:00


guid: http://merill.net/?p=761
permalink: /2012/04/troubleshooting-the-403-forbidden-error-for-sharepoint-asp-net-apps/
dsq_thread_id:
  - "968818312"
categories:
  - Tips
tags:
  - SharePoint
  - Tips
---
If your site bombs out with 403 Forbidden error one quick way to identify the root cause is to run <a href="http://technet.microsoft.com/en-us/sysinternals/bb896645">ProcessMon</a> on the web server and filter it out to only show entries where

Process Name = w3wp.exe

Result = ACCESS DENIED