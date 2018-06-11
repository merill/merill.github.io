---
id: 238
title: Dataset performance in .NET Framework 2.0
date: 2005-02-19T01:58:50+00:00
author: Merill Fernando
layout: post
guid: /post/2005/02/Dataset-performance-in-NET-Framework-20.aspx
permalink: /2005/02/dataset-performance-in-net-framework-20/
dsq_thread_id:
  - "78846220"
categories:
  - .NET
---
<p>Andrew Conrad writes about <a href="http://blogs.msdn.com/aconrad/archive/2005/02/16/374757.aspx">Dataset performance improvements in .NET 2.0</a>. For me these improvements are really, really good reasons to switch to .NET 2.0 as soon as it ships (or even earlier when a &lsquo;Go Live&rsquo; license is available). </p>
<p>System.Data.DataSet contains some very significant performance improvements over prior versions &ndash; particularly for large result set scenarios.</p>
<p>In particular,</p>
<ul>
<li>Highly efficient Binary Remoting --&nbsp; For large Dataset, orders of magnitude better than v1.x </li>
<li>Row Insert, Delete and Modify operations &ndash; For large Dataset, orders of magnitude better than v1.x. For instance, for a DataTable with PrimaryKey constraint, inserting million rows in random order takes around 45 seconds. Everett took 30 Minutes.</li>
<li>Maintaining DataViews in sync with underlying DataTable was very expensive in v1.x, In Whidbey it&rsquo;s extremely fast &ndash; orders of magnitude better.</li>
<li>WebServices/Remoting for TypedDataset: It can be send across to other end without having to send its schema, significantly reducing the serialized payload and giving approx 4x+ improvement in end-end latency. </li></ul>
<p>The following <a href="http://msdn.microsoft.com/data/default.aspx?pull=/library/en-us/dnadonet/html/datasetenhance.asp">article</a> (in addition to highlighting some new V2 features) also details the performance improvements.</p>