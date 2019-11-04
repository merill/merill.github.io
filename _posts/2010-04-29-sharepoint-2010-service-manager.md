---
id: 660
title: SharePoint 2010 Service Manager
date: 2010-04-29T22:43:38+00:00
author: Merill Fernando

guid: http://merill.net/?p=660
permalink: /2010/04/sharepoint-2010-service-manager/
dsq_thread_id:
  - "90834105"
categories:
  - Service Manager
tags:
  - "2010"
  - Service Manager
  - SharePoint
---
With the final release of SharePoint 2010, I finally had time to brush-up and release the Service Manager that I wrote sometime back when the 2010 betas was released.

This utility is basically akin to the SQL Server Service Manager of yore.

If you have SharePoint 2010 installed on your local Windows 7 workstation then you will definitely come across instances where your workstation suddenly freezes up and everything starts moving in slow motion. The most likely culprit is usually one of the SharePoint services. At other times the SharePoint services simply eat away at your RAM.

That's where the SharePoint 2010 Service Manager comes into play. It lets you start and stop all the SharePoint Services running on your workstation with a single-click.

This release handles both the full version of SQL Server as well as SQL Express Edition (the SharePoint instance). There is also an option to permanently disable the SharePoint services from starting up when Windows starts up, hopefully leading to faster boot times.

Here are a couple of screenshots. Get the setup file from CodePlex at <a href="http://sharepointserviceman.codeplex.com/">http://sharepointserviceman.codeplex.com/</a>.

<a href="https://merill.net/wp-content/uploads/2010/04/SharePoint-2010-Service-Manager.png"><img class="alignnone size-full wp-image-661" title="SharePoint 2010 Service Manager" src="https://merill.net/wp-content/uploads/2010/04/SharePoint-2010-Service-Manager.png" alt="" width="564" height="531" /></a>

<a href="https://merill.net/wp-content/uploads/2010/04/SharePoint-2010-Service-Manager-In-Action.png"><img class="alignnone size-full wp-image-662" title="SharePoint-2010-Service-Manager-In-Action" src="https://merill.net/wp-content/uploads/2010/04/SharePoint-2010-Service-Manager-In-Action.png" alt="" width="577" height="540" /></a>

I'd like to thank my colleagues at <a href="http://www.uniqueworld.net/">UniqueWorld</a> including <a href="http://www.neilphillips.com/">Neil</a>, <a href="http://rehmangul.wordpress.com/">Rehman</a> and <a href="http://sharepointsix.blogspot.com/">Dougie</a> who tested the first version and gave valuable feedback.

Please do report any issues you find to merill at merill.net