---
id: 611
title: Installing SharePoint Server 2010 on Windows 7
date: 2009-11-23T07:37:15+00:00


guid: http://merill.net/2009/11/installing-sharepoint-serve-2010-on-windows-7/
permalink: /2009/11/installing-sharepoint-serve-2010-on-windows-7/
dsq_thread_id:
  - "77723161"
categories:
  - SharePoint 2010
tags:
  - "2010"
  - install
  - SharePoint
  - windows 7
---
<p>Here’s a quick summary of how I installed the <a href="http://www.microsoft.com/2010/en/">public beta of SharePoint Server 2010</a>.</p>  <p><u>Minimum Requirements:     <br /></u>- Windows 7 64 bit: What this means is that your workstation needs to be 64 bit and you need to have the 64 bit version of Windows 7 installed.</p>  <p><u>Setup:     <br /></u>The key document that you need to follow for installing on Windows 7 is this article: <a href="http://msdn.microsoft.com/en-us/library/ee554869(office.14).aspx">Setting Up the Development Environment for SharePoint Server</a></p>  <p><u>Key Notes:      <br /></u>- This was installed on Windows 7 Build 7100    <br />- I had UAC turned off    <br />- I already had Visual Studio 2010 Beta before installing SharePoint    <br />- You need to manually download and install the pre-requisites for SharePoint 2010    <br />- You need to extract the setup (using /extract), change an xml file before being able to run setup on Windows 7. </p>  <p><u>Minor Deviation:     <br /></u>The only part of the guide that I was forced to skip was #5 of ‘Step 3: Install SharePoint’</p>  <p>The reason was that the install for the SQL Server patch kept asking for the other files in the multi-part zip. (Remember to unzip the file even though it has a .exe extension)</p>  <p><u>Summary:     <br /></u>Excluding the download times it took about 30 minutes to install SharePoint server on my Dell XPS laptop which has 4GB of RAM.</p>  <p>Although there is no guide published yet I was able to install Office Web Apps on my laptop as well, that guide will follow next.</p>