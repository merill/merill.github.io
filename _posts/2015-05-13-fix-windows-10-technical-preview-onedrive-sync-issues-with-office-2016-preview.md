---
id: 1005
title: 'Fix: Windows 10 (Technical Preview) OneDrive Sync Issues with Office 2016 Preview'
date: 2015-05-13T21:37:17+00:00
author: Merill Fernando

guid: http://merill.net/?p=1005
permalink: /2015/05/fix-windows-10-technical-preview-onedrive-sync-issues-with-office-2016-preview/
snap_isAutoPosted:
  - "1"
snap_MYURL:
  - ""
snapEdIT:
  - "1"
snapFB:
  - 's:208:"a:1:{i:0;a:8:{s:8:"postType";s:1:"T";s:10:"AttachPost";s:1:"2";s:10:"SNAPformat";s:10:"%FULLTEXT%";s:9:"isAutoImg";s:1:"A";s:8:"imgToUse";s:0:"";s:9:"isAutoURL";s:1:"A";s:8:"urlToUse";s:0:"";s:4:"doFB";i:0;}}";'
snapTW:
  - 's:271:"a:1:{i:0;a:9:{s:4:"doTW";s:1:"1";s:10:"SNAPformat";s:15:"%TITLE% - %URL%";s:8:"attchImg";s:1:"1";s:9:"isAutoImg";s:1:"A";s:8:"imgToUse";s:0:"";s:11:"isPrePosted";s:1:"1";s:8:"isPosted";s:1:"1";s:4:"pgID";s:18:"598451962758057984";s:5:"pDate";s:19:"2015-05-13 11:37:21";}}";'
snapLI:
  - 's:288:"a:1:{i:0;a:9:{s:4:"doLI";s:1:"1";s:10:"AttachPost";s:1:"1";s:10:"SNAPformat";s:41:"New post has been published on %SITENAME%";s:11:"SNAPformatT";s:14:"{Blog} %TITLE%";s:9:"isAutoImg";s:1:"A";s:8:"imgToUse";s:0:"";s:9:"isAutoURL";s:1:"A";s:8:"urlToUse";s:0:"";s:11:"isPrePosted";s:1:"1";}}";'
dsq_thread_id:
  - "3760151897"
categories:
  - Tips
---
After installing the Office 2016 Preview on build 10074 of the Windows 10 Technical Preview I came across a recurring sync issue with OneDrive. All the Office documents would show up with the following error 'Files can't be synced. Open the document in Office for more info.'
It didn't make any difference if you opened the document in Word, Excel and saved them back they would still show up with sync errors.

To fix the issue I turned off the 'Use Office to sync files faster and work on files with other people at the same time' from the Settings tab (right click the OneDrive icon on the status bar). An Exit and restart of OneDrive fixed the issue and everything comes up green again.

I'm guessing this is something to do with the Office 2016 preview since I've been running Windows 10 TP for a few months now and didn't have any sync issues.

This not only fixed the sync issue but also made Office use the local files instead of taking a few seconds connecting to OneDrive each time I saved.

<a href="https://merill.net/wp-content/uploads/2015/05/OneDriveSync.png"><img class="alignnone size-full wp-image-1006" src="https://merill.net/wp-content/uploads/2015/05/OneDriveSync.png" alt="OneDriveSync" width="454" height="510" /></a>

I know you can <a href="https://softwarekeep.ca/download-microsoft-office/office-for-mac.html">buy Microsoft Office for Mac</span></a> now, but after all these years, I'm going to stick to what I know.