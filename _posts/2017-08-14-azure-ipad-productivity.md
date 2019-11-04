---
id: 1099
title: Azure + iPad = Productivity
date: 2017-08-14T09:01:02+00:00


guid: http://merill.net/?p=1099
permalink: /2017/08/azure-ipad-productivity/
medium_post:
  - 'O:11:"Medium_Post":11:{s:16:"author_image_url";s:69:"https://cdn-images-1.medium.com/fit/c/200/200/0*nOSMyIhdQJ9325FH.jpeg";s:10:"author_url";s:26:"https://medium.com/@merill";s:11:"byline_name";N;s:12:"byline_email";N;s:10:"cross_link";s:2:"no";s:2:"id";s:12:"817f6762dc8c";s:21:"follower_notification";s:3:"yes";s:7:"license";s:19:"all-rights-reserved";s:14:"publication_id";s:12:"99858869fb3c";s:6:"status";s:6:"public";s:3:"url";s:63:"https://medium.com/@merill/azure-ipad-productivity-817f6762dc8c";}'
snap_isAutoPosted:
  - "1"
snap_MYURL:
  - ""
snapEdIT:
  - "1"
snapFB:
  - 's:178:"a:1:{i:0;a:7:{s:9:"msgFormat";s:10:"%FULLTEXT%";s:8:"postType";s:1:"T";s:9:"isAutoImg";s:1:"A";s:8:"imgToUse";s:0:"";s:9:"isAutoURL";s:1:"A";s:8:"urlToUse";s:0:"";s:2:"do";i:0;}}";'
snapLI:
  - 's:209:"a:1:{i:0;a:7:{s:9:"msgFormat";s:41:"New post has been published on %SITENAME%";s:8:"postType";s:1:"A";s:9:"isAutoImg";s:1:"A";s:8:"imgToUse";s:0:"";s:9:"isAutoURL";s:1:"A";s:8:"urlToUse";s:0:"";s:2:"do";i:0;}}";'
snapTW:
  - 's:361:"a:1:{i:0;a:11:{s:2:"do";s:1:"1";s:9:"msgFormat";s:15:"%TITLE% - %URL%";s:8:"attchImg";s:1:"1";s:9:"isAutoImg";s:1:"A";s:8:"imgToUse";s:0:"";s:9:"isAutoURL";s:1:"A";s:8:"urlToUse";s:0:"";s:8:"isPosted";s:1:"1";s:4:"pgID";s:18:"896869270897926146";s:7:"postURL";s:52:"https://twitter.com/merill/status/896869270897926146";s:5:"pDate";s:19:"2017-08-13 23:01:11";}}";'
dsq_thread_id:
  - "6064366471"
categories:
  - Tips
---
I don’t spend much timing writing code these days but when I do I want it to be productive as possible. Whether it is at my desk, in a meeting room or in bed in the middle of the night.

So this weekend I went about setting up a workflow that would let me access a powerful machine in the cloud with the latest version of Visual Studio and get access to it in a secure manner. Here is what I used to get it all going.

<strong>Azure DevTest Labs</strong>

The DevTest Labs is a neat Azure service that gives you a virtual machine running the greatest and latest version of Visual Studio. You can save yourself a ton of time by not having to deal with downloading and waiting through a Visual Studio install.

<strong>IFTT</strong>

The dollars can add up quickly when you leave a high end virtual machine running on Azure. Using a combo of Azure Runbooks, web hooks and IFTT buttons, I was able to set up a nice widget that would let me quickly start up and shut down my VM. Using iOS widgets and IFTT, it was just a swipe away from the home screen on my iPad/iPhone to start up my VM.
<img src="https://merill.net/wp-content/uploads/2017/08/IMG_0316-300x225.png" alt="" width="300" height="225" class="alignnone size-medium wp-image-1100" />

<strong>Jump Desktop Connect</strong>

The last piece of the puzzle was to get into my VM. When you are working in a corporate environment behind firewalls and proxies that only allow http traffic to flow through, RDP is simply not going to cut it. Plus you open up your surface area by exposing your VM to the public internet. Jump Desktop to the rescue to solve both the issues. The <a href="https://jumpdesktop.com/">Jump Desktop Connect</a> is a free app that you install on the PC/Mac that you need remote access to. You can then use the awesome Jump Desktop apps on iOS, Android, Mac or Windows and punch through any firewall to get to your remote machine.

Oh and by the way did I tell you that Jump Desktop is one of the few RDP apps that will let you use a mouse on your remote machine? Productivity FTW!