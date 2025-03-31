---
id: 626
title: Visual Studio Maintenance Mode
date: 2009-12-19T09:31:14+00:00


guid: https://merill.net/2009/12/visual-studio-maintenance-mode/
permalink: /2009/12/visual-studio-maintenance-mode/
dsq_thread_id:
  - "77736059"
categories:
  - Tips
tags:
  - command prompt
  - setup
  - visual studio 2010
---
<p>I started working my way through the hands on labs in the <a href="http://www.microsoft.com/downloads/details.aspx?FamilyID=cffb14e8-88a9-43bd-87aa-4792ab60d320&amp;displaylang=en">SharePoint 2010 Developer Evaluation Guide</a> and found that I was missing the Visual Studio 2010 Command Prompt in my installation.</p>  <p>Gabriel’s <a href="http://gabriel.lozano-moran.name/blog/post/Visual-Studio-2010-Command-Prompt-shortcut-missing.aspx">post</a> explained why. I typically don’t install VC++ on my dev boxes and apparently this is a known bug in VS 2010 where the command prompt doesn’t get installed if VC++ is not installed.</p>  <p>What really prompted me to post this is this nice feature new to 2010. I realized that I didn’t have the installation iso but gave it a try by going to Add/Remove programs and going through the Add/Remove features in VS 2010. The dreaded dialog to pick the installation path came up.</p>  <p>I was almost about to give up when I noticed the Download button. And viola the setup actually connects directly to the download servers at Microsoft and get’s only the items that have changed. It also went ahead and noticed updated Silverlight Tools and got them as well. </p>  <p>In the words of <a href="http://www.sharepointconfig.com/">@AriBakker</a>. Sweet. Sweet indeed. </p>  <p><a href="https://merill.net/wp-content/uploads/2009/12/VisualStudio2010MaintenanceMode.png"><img style="border-bottom: 0px; border-left: 0px; display: inline; border-top: 0px; border-right: 0px" title="Visual-Studio-2010-Maintenance-Mode" border="0" alt="Visual-Studio-2010-Maintenance-Mode" src="{{ site.url }}{{ site.baseurl }}/wp-content/uploads/2009/12/VisualStudio2010MaintenanceMode_thumb.png" width="624" height="480" /></a></p>