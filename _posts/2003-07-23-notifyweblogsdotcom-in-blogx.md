---
id: 540
title: NotifyWebLogsDotCom in BlogX
date: 2003-07-23T19:11:39+00:00
author: Merill Fernando
layout: post
guid: /post/2003/07/NotifyWebLogsDotCom-in-BlogX.aspx
permalink: /2003/07/notifyweblogsdotcom-in-blogx/
categories:
  - Technology
---
<body xmlns="http://www.w3.org/1999/xhtml">
    <font size="2"> 
    <p>
        The day before an ex-coworker&#160;friend (Nimalan) posted a comment to to one of
        my blogs but I only noticed it when I was browsing through the site. Most of the other
        blogging tools supported some type of notification server when comments were posted
        for a blog. 
    </p>
    <p>
        I browsed through the BlogX code but the addComment procedure doesn't seem to do any
        email notification. 
    </p>
    <p>
        But I <u>did</u> notice a NotifyWebLogsDotCom tag in SiteConfig, this does a very
        interesting thing, it calls a weblogUpdates web service on the <a href="http://www.weblogs.com">weblogs.com</a> site. 
    </p>
    <p>
        The weblogs.com site seems to keep an log of the most recently posted articles. I
        set this flag to true now, hope this brings some Google Juice my way ;)<font size="2"> </font>
    </p>
    </font>
</body>