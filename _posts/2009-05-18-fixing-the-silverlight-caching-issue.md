---
id: 579
title: Fixing the Silverlight caching issue
date: 2009-05-18T15:24:09+00:00


guid: https://merill.net/?p=579
permalink: /2009/05/fixing-the-silverlight-caching-issue/
dsq_thread_id:
  - "77713029"
categories:
  - Tips
tags:
  - silverlight
---
Fell into this trap today. I deployed an update of my silverlight project to the Sharepoint site but on some machines the browser continuously kept loading the older version.

I racked my brain trying to figure out how to add ETags to a xap file and yet keep the deployment simple. The answer though is unbelievably simple in this case. Update your AssemblyVersion when compiling. That's it. IIS takes care of sending the update through to all the browsers.

BTW the <a href="http://silverlight.net/forums/">silverlight.net forums</a> are a gem for figuring out answers to silverlight problems.