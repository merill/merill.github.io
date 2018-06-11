---
id: 628
title: Workflow does not start automatically when bulk inserting items
date: 2010-03-11T08:18:27+00:00
author: Merill Fernando
layout: post
guid: http://merill.net/2010/03/workflow-does-not-start-automatically-when-bulk-inserting-items/
permalink: /2010/03/workflow-does-not-start-automatically-when-bulk-inserting-items/
dsq_thread_id:
  - "77838167"
categories:
  - SharePoint
tags:
  - bulk insert
  - workflow
---
This had me tripped for a while. I was bulk inserting items (~800) to a list which had event receivers as well as a workflow attached.

The problem was that the workflow was not being triggered. Or if it did it just hung at In Progress.

After poking around for more than an hour I discovered that if I inserted a single item it worked. So to fix the issue I added a ten second sleep (Thread.Sleep) between the inserts and the workflows are triggering away happily.