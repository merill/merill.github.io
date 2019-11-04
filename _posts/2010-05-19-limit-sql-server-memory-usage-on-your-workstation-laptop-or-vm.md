---
id: 678
title: Limit SQL Server memory usage on your workstation, laptop or VM
date: 2010-05-19T10:51:30+00:00
author: Merill Fernando

guid: http://merill.net/?p=678
permalink: /2010/05/limit-sql-server-memory-usage-on-your-workstation-laptop-or-vm/
dsq_thread_id:
  - "96940227"
medium_post:
  - 'O:11:"Medium_Post":11:{s:16:"author_image_url";s:69:"https://cdn-images-1.medium.com/fit/c/200/200/0*nOSMyIhdQJ9325FH.jpeg";s:10:"author_url";s:26:"https://medium.com/@merill";s:11:"byline_name";N;s:12:"byline_email";N;s:10:"cross_link";s:2:"no";s:2:"id";s:12:"858150825d98";s:21:"follower_notification";s:3:"yes";s:7:"license";s:19:"all-rights-reserved";s:14:"publication_id";s:12:"99858869fb3c";s:6:"status";s:6:"public";s:3:"url";s:102:"https://medium.com/@merill/limit-sql-server-memory-usage-on-your-workstation-laptop-or-vm-858150825d98";}'
snap_MYURL:
  - ""
snapEdIT:
  - "1"
snapFB:
  - 's:229:"a:1:{i:0;a:9:{s:2:"do";s:1:"1";s:8:"postType";s:1:"T";s:10:"AttachPost";s:1:"2";s:10:"SNAPformat";s:10:"%FULLTEXT%";s:9:"isAutoImg";s:1:"A";s:8:"imgToUse";s:0:"";s:9:"isAutoURL";s:1:"A";s:8:"urlToUse";s:0:"";s:4:"doFB";s:1:"1";}}";'
snapLI:
  - 's:276:"a:1:{i:0;a:9:{s:2:"do";s:1:"1";s:8:"postType";s:1:"A";s:10:"SNAPformat";s:41:"New post has been published on %SITENAME%";s:12:"liMsgFormatT";s:14:"{Blog} %TITLE%";s:9:"isAutoImg";s:1:"A";s:8:"imgToUse";s:0:"";s:9:"isAutoURL";s:1:"A";s:8:"urlToUse";s:0:"";s:4:"doLI";s:1:"1";}}";'
snapTW:
  - 's:162:"a:1:{i:0;a:6:{s:2:"do";s:1:"1";s:10:"SNAPformat";s:15:"%TITLE% - %URL%";s:8:"attchImg";s:1:"1";s:9:"isAutoImg";s:1:"A";s:8:"imgToUse";s:0:"";s:4:"doTW";s:1:"1";}}";'
categories:
  - Service Manager
  - Tips
tags:
  - "2010"
  - Service Manager
  - SharePoint
  - SQL
---
Here's a neat tip I learnt over the weekend.

All SQL Server instances are by default set up to use all the memory available on your workstation.

This is ideal when you have SQL Server running on it's own <a style="text-decoration: none;" href="https://www.servermania.com/dedicated-servers-hosting.htm">dedicated server hosting</a>, not so ideal when you have SQL Server installed on your laptop, workstation or even on a SharePoint VM.

Here's what <a href="http://msdn.microsoft.com/en-us/library/ms180797.aspx">MSDN says</a>
<blockquote>if SQL Server is one of several server applications running on a single computer, the system administrators may need to control the amount of memory allocated to SQL Server. In these cases, you can use the min server memory and max server memory options to control how much memory SQL Server can use.</blockquote>
In the <a href="http://msdn.microsoft.com/en-us/library/ms178067.aspx">Server Memory Options</a> page they go on to say:
<blockquote>When you are running multiple instances of the Database Engine, there are three approaches you can use to manage memory
<ul>
	<li>Use max server memory to control memory usage.</li>
	<li>Use min server memory to control memory usage.</li>
	<li><strong>Do nothing (not recommended).</strong></li>
</ul>
</blockquote>
Which brings us to how we can set the maximum limit. Quite easy. Just connect to each SQL Server instance and set the maximum memory to a more palatable value.

Here's a visual walk through to limit the maximum memory usage to 512MB for your SharePoint 2010 instance (if you installed it on Windows 7).

1. Start SQL Server Management Studio (or SSMS Express) and connect to your SQL Server instance (SharePoint in this case): <em>localhost\SharePoint</em>

<em> </em> <a href="https://merill.net/wp-content/uploads/2010/05/SqlServerConnectSharePoint.png"><img class="alignnone size-medium wp-image-681" title="SqlServerConnectSharePoint" src="https://merill.net/wp-content/uploads/2010/05/SqlServerConnectSharePoint-300x229.png" alt="" width="300" height="229" /></a>

2. Right-click on the instance node and select Properties.

<a href="https://merill.net/wp-content/uploads/2010/05/SqlServer-Properties.png"><img class="alignnone size-medium wp-image-683" title="SqlServer-Properties" src="https://merill.net/wp-content/uploads/2010/05/SqlServer-Properties-300x251.png" alt="" width="300" height="251" /></a>

3. Click on the Memory node you'll notice that the Maximum Server Memory is set to 2,147,483,647MB change it to a lower limit like 256 or 512MB. Click OK and your all set.

<a href="https://merill.net/wp-content/uploads/2010/05/SqlServer-Memory.png"><img class="alignnone size-medium wp-image-682" title="SqlServer-Memory" src="https://merill.net/wp-content/uploads/2010/05/SqlServer-Memory-300x269.png" alt="" width="300" height="269" /></a>

If you prefer SQL the same can be done with the following commands.

<br/><em>Enable advanced options:</em>

<code>USE master </code>

<code>EXEC sp_configure 'show advanced options', 1 </code>

<code>RECONFIGURE WITH OVERRIDE</code>

<br/><em>Set the maximum amount of memory to 512 MB:</em>

<code>USE master </code>

<code>EXEC sp_configure 'max server memory (MB)', 512 </code>

<code>RECONFIGURE WITH OVERRIDE</code>

<br/><em>Display the newly set configuration:</em>

<code>USE master </code>

<code>EXEC sp_configure 'max server memory (MB)' </code>

<br/><em>Set 'show advanced options' back to default:</em>

<code>USE master </code>

<code>EXEC sp_configure 'show advanced options', 0 </code>

<code>RECONFIGURE WITH OVERRIDE</code>