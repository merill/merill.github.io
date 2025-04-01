---
id: 610
title: 'Windows 7: WiFi slow to connect or Limited Connectivity'
date: 2009-11-18T21:50:53+00:00


guid: https://merill.net/2009/11/windows-7-wifi-slow-to-connect-or-limited-connectivity/
permalink: /2009/11/windows-7-wifi-slow-to-connect-or-limited-connectivity/
dsq_thread_id:
  - "77713072"
snap_MYURL:
  - ""
snapEdIT:
  - "1"
snapFB:
  - 's:182:"a:1:{i:0;a:7:{s:2:"do";s:1:"1";s:9:"msgFormat";s:10:"%FULLTEXT%";s:8:"postType";s:1:"T";s:9:"isAutoImg";s:1:"A";s:8:"imgToUse";s:0:"";s:9:"isAutoURL";s:1:"A";s:8:"urlToUse";s:0:"";}}";'
snapLI:
  - 's:213:"a:1:{i:0;a:7:{s:2:"do";s:1:"1";s:9:"msgFormat";s:41:"New post has been published on %SITENAME%";s:8:"postType";s:1:"A";s:9:"isAutoImg";s:1:"A";s:8:"imgToUse";s:0:"";s:9:"isAutoURL";s:1:"A";s:8:"urlToUse";s:0:"";}}";'
snapTW:
  - 's:187:"a:1:{i:0;a:7:{s:2:"do";s:1:"1";s:9:"msgFormat";s:15:"%TITLE% - %URL%";s:8:"attchImg";s:1:"1";s:9:"isAutoImg";s:1:"A";s:8:"imgToUse";s:0:"";s:9:"isAutoURL";s:1:"A";s:8:"urlToUse";s:0:"";}}";'
medium_post:
  - 'O:11:"Medium_Post":11:{s:16:"author_image_url";s:69:"https://cdn-images-1.medium.com/fit/c/200/200/0*nOSMyIhdQJ9325FH.jpeg";s:10:"author_url";s:26:"https://medium.com/@merill";s:11:"byline_name";N;s:12:"byline_email";N;s:10:"cross_link";s:2:"no";s:2:"id";s:12:"ef1c7ae94197";s:21:"follower_notification";s:3:"yes";s:7:"license";s:19:"all-rights-reserved";s:14:"publication_id";s:12:"99858869fb3c";s:6:"status";s:6:"public";s:3:"url";s:94:"https://medium.com/@merill/windows-7-wifi-slow-to-connect-or-limited-connectivity-ef1c7ae94197";}'
categories:
  - Tips
tags:
  - limited connectivity
  - slow to connect
  - wifi
  - windows 7
---
I’ve been having this frustrating issue for the last month where the laptop would take about 10 minutes before it was able to connect to the internet. This happened even when the machine came back from sleep/suspend mode.

The Wifi connection would be detected immediate but I would not get an IP from the DHCP server. I always had to fiddle around by disconnecting and connecting a few times. I was almost pulling my hair out by the end of my debug process, I even went out and bought the best wi-fi range extender I could find - thinking the signal was just weak.

Well today I got down the source. The problem was to do with the Virtual Machine Network Services that were installed when I added Virtual PC. Once I went into the WiFi Adapter properties and removed the Virtual Machine Network Services I was able to get my PC back to instant connectivity.