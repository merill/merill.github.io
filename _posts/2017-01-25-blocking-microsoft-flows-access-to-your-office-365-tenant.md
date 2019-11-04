---
id: 1074
title: 'Blocking Microsoft Flow&#8217;s access to your Office 365 tenant'
date: 2017-01-25T14:33:26+00:00
author: Merill Fernando

guid: http://merill.net/?p=1074
permalink: /2017/01/blocking-microsoft-flows-access-to-your-office-365-tenant/
medium_post:
  - 'O:11:"Medium_Post":11:{s:16:"author_image_url";s:69:"https://cdn-images-1.medium.com/fit/c/200/200/0*nOSMyIhdQJ9325FH.jpeg";s:10:"author_url";s:26:"https://medium.com/@merill";s:11:"byline_name";N;s:12:"byline_email";N;s:10:"cross_link";s:2:"no";s:2:"id";s:12:"227bcec7bee9";s:21:"follower_notification";s:3:"yes";s:7:"license";s:19:"all-rights-reserved";s:14:"publication_id";s:12:"99858869fb3c";s:6:"status";s:6:"public";s:3:"url";s:97:"https://medium.com/@merill/blocking-microsoft-flows-access-to-your-office-365-tenant-227bcec7bee9";}'
snap_isAutoPosted:
  - "1"
snap_MYURL:
  - ""
snapEdIT:
  - "1"
snapFB:
  - 's:178:"a:1:{i:0;a:7:{s:9:"msgFormat";s:10:"%FULLTEXT%";s:8:"postType";s:1:"T";s:9:"isAutoImg";s:1:"A";s:8:"imgToUse";s:0:"";s:9:"isAutoURL";s:1:"A";s:8:"urlToUse";s:0:"";s:2:"do";i:0;}}";'
snapLI:
  - 's:213:"a:1:{i:0;a:7:{s:2:"do";s:1:"1";s:9:"msgFormat";s:41:"New post has been published on %SITENAME%";s:8:"postType";s:1:"A";s:9:"isAutoImg";s:1:"A";s:8:"imgToUse";s:0:"";s:9:"isAutoURL";s:1:"A";s:8:"urlToUse";s:0:"";}}";'
snapTW:
  - 's:361:"a:1:{i:0;a:11:{s:2:"do";s:1:"1";s:9:"msgFormat";s:15:"%TITLE% - %URL%";s:8:"attchImg";s:1:"1";s:9:"isAutoImg";s:1:"A";s:8:"imgToUse";s:0:"";s:9:"isAutoURL";s:1:"A";s:8:"urlToUse";s:0:"";s:8:"isPosted";s:1:"1";s:4:"pgID";s:18:"824112973987938305";s:7:"postURL";s:52:"https://twitter.com/merill/status/824112973987938305";s:5:"pDate";s:19:"2017-01-25 04:33:37";}}";'
dsq_thread_id:
  - "5491341388"
categories:
  - Office 365
---
Did you know that any user in your organisation can sign into Microsoft Flow with their personal account and create a flow that connects to your organisation's Office 365 tenant?
This means that an employee can (even accidentally) create a flow that monitors a SharePoint site (obviously they need to have access to the site) and posts the contents to Twitter, Dropbox or any other external service.
The bad news is that as the Office 365 tenant admin we have no way of blocking this in the UI. The good news is that Microsoft can. So raise a service request with them and ask them to disable 'Cross tenant Flow creation'. This will force all of your data to stay within your tenant and prevents data loss.