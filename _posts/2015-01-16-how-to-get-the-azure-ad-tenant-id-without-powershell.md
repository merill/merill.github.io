---
id: 995
title: How to get the Azure AD Tenant ID without PowerShell
date: 2015-01-16T08:24:00+00:00


guid: https://merill.net/?p=995
permalink: /2015/01/how-to-get-the-azure-ad-tenant-id-without-powershell/
snap_isAutoPosted:
  - "1"
snap_MYURL:
  - ""
snapEdIT:
  - "1"
snapFB:
  - 's:208:"a:1:{i:0;a:8:{s:8:"postType";s:1:"T";s:10:"AttachPost";s:1:"2";s:10:"SNAPformat";s:10:"%FULLTEXT%";s:9:"isAutoImg";s:1:"A";s:8:"imgToUse";s:0:"";s:9:"isAutoURL";s:1:"A";s:8:"urlToUse";s:0:"";s:4:"doFB";i:0;}}";'
snapLI:
  - 's:257:"a:1:{i:0;a:8:{s:10:"AttachPost";s:1:"1";s:10:"SNAPformat";s:41:"New post has been published on %SITENAME%";s:11:"SNAPformatT";s:14:"{Blog} %TITLE%";s:9:"isAutoImg";s:1:"A";s:8:"imgToUse";s:0:"";s:9:"isAutoURL";s:1:"A";s:8:"urlToUse";s:0:"";s:4:"doLI";i:0;}}";'
snapTW:
  - 's:141:"a:1:{i:0;a:5:{s:10:"SNAPformat";s:15:"%TITLE% - %URL%";s:8:"attchImg";s:1:"1";s:9:"isAutoImg";s:1:"A";s:8:"imgToUse";s:0:"";s:4:"doTW";i:0;}}";'
dsq_thread_id:
  - "3432222157"
categories:
  - Twitter
---
A quick way to get the Tenant Id for your Office 365 / Azure AD tenant is to login to the Azure AD Portal, drill down to the directory and copy the ID from the URL.

https://manage.windowsazure.com/teamtelstra.onmicrosoft.com#Workspaces/ActiveDirectoryExtension/Directory/<span style="color: #ff0000;">&lt;Tenant Id&gt;</span>/directoryQuickStart