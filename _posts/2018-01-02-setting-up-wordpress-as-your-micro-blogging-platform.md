---
id: 1142
title: Setting up WordPress as your micro blogging platform
date: 2018-01-02T13:32:50+00:00
author: Merill Fernando

guid: http://merill.net/?p=1142
permalink: /2018/01/setting-up-wordpress-as-your-micro-blogging-platform/
medium_post:
  - 'O:11:"Medium_Post":11:{s:16:"author_image_url";s:69:"https://cdn-images-1.medium.com/fit/c/200/200/0*nOSMyIhdQJ9325FH.jpeg";s:10:"author_url";s:26:"https://medium.com/@merill";s:11:"byline_name";N;s:12:"byline_email";N;s:10:"cross_link";s:2:"no";s:2:"id";s:12:"a818448367ee";s:21:"follower_notification";s:3:"yes";s:7:"license";s:19:"all-rights-reserved";s:14:"publication_id";s:12:"99858869fb3c";s:6:"status";s:6:"public";s:3:"url";s:92:"https://medium.com/@merill/setting-up-wordpress-as-your-micro-blogging-platform-a818448367ee";}'
dsq_thread_id:
  - "6385694468"
categories:
  - Tips
tags:
  - Tips
---
Deciding on WordPress as your source of truth for your micro blog is all good but how do you avoid spamming your RSS readers with your status updates meant for micro.blog, twitter, linked in et al?

The simplest way to target WordPress posts for micro blogs is to use a specific category (I call mine <strong>status</strong>). You can then configure WordPress to not include posts from this category in the default feed.

One way to exclude a category from the default feed is using a re-write rule in your .htaccess file as shared by Manton in this gist <a href="https://gist.github.com/manton/f8b6f8b391a2f3d9b419">https://gist.github.com/manton/f8b6f8b391a2f3d9b419</a>

I wanted something a bit more robust that wouldn't break when the url format changed. Instead I wrote a custom filter that would hide the category from the default feed. To get this set up you can use the excellent 'My Custom Functions' plug in <a href="https://wordpress.org/plugins/my-custom-functions/">https://wordpress.org/plugins/my-custom-functions/</a>

https://gist.github.com/merill/92c71ffc980a1741ba1c4cc6900a3e5c

Once you have this set up you can now use the url to your feed as the feed source at <a href="https://micro.blog">https://micro.blog</a> using the following format http://&lt;&lt;domain&gt;&gt;/category/&lt;&lt;category name&gt;&gt;/feed/

In my case this is my feed url <a href="http://merill.net/category/status/feed/">http://merill.net/category/status/feed/</a>