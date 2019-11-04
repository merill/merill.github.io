---
id: 772
title: Tips for working with BCS and FAST Search
date: 2012-11-29T11:03:37+00:00


guid: http://merill.net/?p=772
permalink: /2012/11/tips-for-working-with-bcs-and-fast-search/
dsq_thread_id:
  - "968835473"
categories:
  - SharePoint
tags:
  - bcs
  - fast
---
When building a FAST search solution to crawl external entities through BCS it can get very frustrating if you deploy a change and it doesn't get updated in all the right places.

After much trial and error I have come up with the following checklist to keep your sanity.

Rule #1: If you change the BCS model manually (i.e. using a text editor instead of Visual Studio) you need to change the Version attribute of the Entity node in the entity that you make the change in. If you don't do this any update you make will not be applied. This can lead to very confusing behaviour since the change you made will get reflected at some point down the line.

Apart from that here goes the checklist
<ol>
	<li>Delete the BCS content source</li>
	<li>Restart the SharePoint Server Search service</li>
	<li>Using Task Manager kill off any mssdmn.exe that are running</li>
	<li>Deploy your updated solution</li>
	<li>Recreate the content source and run a full crawl.</li>
</ol>
If your working in a multi-farm scenario where the Search service is in a different farm to that of the BCS service then you need to do steps #2 &amp; #3 in the server running the Search crawls. This is important because any assemblies that you have built for the entity are dynamically copied into that server and loaded into Server Search &amp; mssdmn.exe.

If you don't do steps #2 &amp; #3 Search will end up using the older version of your assembly and not the one that you just deployed.