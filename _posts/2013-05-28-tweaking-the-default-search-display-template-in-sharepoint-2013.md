---
id: 821
title: Tweaking the default search display template in SharePoint 2013
date: 2013-05-28T12:51:32+00:00


guid: https://merill.net/?p=821
permalink: /2013/05/tweaking-the-default-search-display-template-in-sharepoint-2013/
dsq_thread_id:
  - "1328590718"
categories:
  - SharePoint
tags:
  - search
  - SharePoint
  - tip
---
Let's look at what it takes to make a minor tweak to the out of the box search result in SharePoint 2013. Say my requirement is to show the document id in the search result like the sample shown below.

<img class="alignnone size-full wp-image-822" alt="Search Result" src="https://merill.net/wp-content/uploads/2013/05/Search-Result.png" width="507" height="127" />

For the example above I'm going to create a custom display template for PowerPoint files.

Let's start by mapping the display templates folder as a local drive. Browse to /_layouts/15/DesignMapDrive.aspx and click on the /_catalogs/masterpage/ link to open the drive. You can then map that as a network drive.

Through explorer browser to the \_catalogs\masterpage\Display Templates\Search folder and copy these two files file to a local drive.
<ul>
	<li>Item_PowerPoint.html</li>
	<li>Item_CommonItem_Body.html</li>
</ul>
Rename Item_PowerPoint.html to make it your own.

Open up the file and change the &lt;title&gt; node. This is what get's displayed in SharePoint.

Make the changes highlighted below.

I'm basically updating the title in javascript to show the doc id. You would think this would be enough, unfortunately the render body method doesn't seem to pick up the updated value. Instead you need to copy the entire div from the Item_CommonItem_Body.html file. Copy the Item_CommonItem_Body div from that file into your customised PowerPoint file and overwrite the line that makes the call to ctx.RenderBody.

<img class="alignnone size-full wp-image-823" alt="DisplayTemplate" src="https://merill.net/wp-content/uploads/2013/05/DisplayTemplate.png" width="812" height="667" />

Upload your custom html file to Search display templates mapped folder.

Now browse to the Manage Result Types page from Site Collection Administration and make a copy of the Microsoft PowerPoint result type.

From the Actions drop down pick the display template that you just uploaded and your all set.