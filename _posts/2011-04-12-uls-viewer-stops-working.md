---
id: 719
title: ULS Viewer stops working
date: 2011-04-12T12:38:42+00:00


guid: https://merill.net/?p=719
permalink: /2011/04/uls-viewer-stops-working/
dsq_thread_id:
  - "277425343"
categories:
  - SharePoint 2010
tags:
  - log
  - SharePoint
  - uls viewer
---
If ULS Viewer suddenly stops reading from the ULS log, the quick fix is to move all the log files to another folder. Except for the last log file which Explorer will anyway prevent you from moving.

The issue is most probably because one or more files in the folder are not in the right format and trip up ULS Viewer. 

Some have reported the *upgrade.log files as the culprit. Deleting them didn't fix it for me so I just deleted all the files.

PS: If your a SharePoint dev and your not using the ULS Viewer from Microsoft (no not the one from CodePlex). Do yourself a favour and give it a try.
<a href="http://archive.msdn.microsoft.com/ULSViewer">http://archive.msdn.microsoft.com/ULSViewer</a>