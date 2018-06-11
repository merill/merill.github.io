---
id: 777
title: Creating a BCS Content Source using PowerShell
date: 2012-12-12T17:44:30+00:00
author: Merill Fernando
layout: post
guid: http://merill.net/?p=777
permalink: /2012/12/creating-a-bcs-content-source-using-powershell/
dsq_thread_id:
  - "970298469"
categories:
  - SharePoint 2010
tags:
  - bcs
  - SharePoint
---
You can use the following command to create a content source to crawl a Business Data Connectivity Service (BDCS).
<pre><code>$lobSystems = @("LOBSystemName1","LOBSystemNameInstance1") 
New-SPEnterpriseSearchCrawlContentSource -name "My Content Source Name" -searchapplication "My Search Service Application Name" -Type Business -LOBSystemSet $lobSystems</code></pre>
If the LOBSystemName is not correct the content source gets created but the model you want to search is not checked.

To figure out the right values for the LOBSystemName and LOBSystemInstanceName look no further than the bdcm file in your solution. Open the .bdcm file in notepad and use the Name attributes of the LobSystem and LobSystemInstance nodes.

&nbsp;
<pre></pre>