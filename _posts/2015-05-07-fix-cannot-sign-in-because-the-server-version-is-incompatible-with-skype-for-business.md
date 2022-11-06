---
id: 1003
title: 'Fix: Cannot sign in because the server version is incompatible with Skype for Business'
date: 2015-05-07T10:56:15+00:00


guid: https://merill.net/?p=1003
permalink: /2015/05/fix-cannot-sign-in-because-the-server-version-is-incompatible-with-skype-for-business/
snap_isAutoPosted:
  - "1"
dsq_thread_id:
  - "3742894619"
snap_MYURL:
  - ""
snapEdIT:
  - "1"
snapFB:
  - 's:208:"a:1:{i:0;a:8:{s:8:"postType";s:1:"T";s:10:"AttachPost";s:1:"2";s:10:"SNAPformat";s:10:"%FULLTEXT%";s:9:"isAutoImg";s:1:"A";s:8:"imgToUse";s:0:"";s:9:"isAutoURL";s:1:"A";s:8:"urlToUse";s:0:"";s:4:"doFB";i:0;}}";'
snapLI:
  - 's:280:"a:1:{i:0;a:9:{s:10:"AttachPost";s:1:"1";s:10:"SNAPformat";s:41:"New post has been published on %SITENAME%";s:11:"SNAPformatT";s:14:"{Blog} %TITLE%";s:9:"isAutoImg";s:1:"A";s:8:"imgToUse";s:0:"";s:9:"isAutoURL";s:1:"A";s:8:"urlToUse";s:0:"";s:4:"doLI";i:0;s:8:"postType";s:1:"A";}}";'
snapTW:
  - 's:141:"a:1:{i:0;a:5:{s:10:"SNAPformat";s:15:"%TITLE% - %URL%";s:8:"attchImg";s:1:"1";s:9:"isAutoImg";s:1:"A";s:8:"imgToUse";s:0:"";s:4:"doTW";i:0;}}";'
categories:
  - Tips
---
To get Skype for Business (Office 2016) working with an older OCS or Lync server create the following registry key and you are good to go.

HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Office\16.0\Lync
DisableServerCheck (DWORD 32-Bit Value): 1