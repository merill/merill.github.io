---
id: 518
title: Creating a Virtual Directory
date: 2003-08-19T22:58:01+00:00


guid: /post/2003/08/Creating-a-Virtual-Directory.aspx
permalink: /2003/08/creating-a-virtual-directory/
dsq_thread_id:
  - "78981277"
categories:
  - ASP.NET
  - Microsoft
---
<body xmlns="http://www.w3.org/1999/xhtml">
    <p>
        I always wondered what the differences were between creating virtual directory using
        the IIS and through Windows Explorer (Web Sharing).
    </p>
    <p>
        I found out today after spending over an hour trying to figure out why I was getting
        this error when calling my web service from a windows client: <em>WebException: The
        request failed with HTTP status 401: Unauthorized</em>
    </p>
    <p>
        The reason is that when you create a Virtual Directory through IIS the default permission
        for the directory is Anonymous but when using Windows Explorer the default permission
        is set to Integrated Window Authentication.
    </p>
</body>