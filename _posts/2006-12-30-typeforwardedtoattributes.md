---
id: 80
title: TypeForwardedToAttributes
date: 2006-12-30T14:55:44+00:00


guid: /post/2006/12/TypeForwardedToAttributes.aspx
permalink: /2006/12/typeforwardedtoattributes/
dsq_thread_id:
  - "78096647"
categories:
  - Certification
---
<p>While preparing for the <a href="http://www.microsoft.com/learning/exams/70-551.mspx">70&ndash;551</a> exam I came across the new TypeForwardedToAttributes class. Searching for this on <a href="http://search.msdn.microsoft.com/search/default.aspx?__VIEWSTATE=&amp;query=typeforwardedtoattributes&amp;siteid=0&amp;tab=0">MSDN</a> brought up &ldquo;no search results&rdquo;. Hmm.. that sounded funny.</p>
<p>Searching on <a href="http://live.com/">Live</a>&nbsp;did bring up some results. The problem stems from the fact that the actual class name is <a href="http://msdn2.microsoft.com/en-us/library/system.runtime.compilerservices.typeforwardedtoattribute.aspx">TypeForwardedToAttribute</a> not TypeForwardedToAttributes as incorecctly stated in the exam preparation guide <a href="http://www.microsoft.com/learning/exams/70-551.mspx">page</a>.</p>
<p>A handy feature too which allows you to move classes from one assembly to another without breaking existing applications that have the earlier reference. Bill Bozeman&rsquo;s blog has a good overview on the <a href="http://www.bozemanblog.com/PermaLink,guid,2e6d7675-eb43-438f-8b93-9155ca1712fa.aspx">TypeForwardedToAttributes</a> class with examples.</p>