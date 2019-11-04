---
id: 25
title: 'Making use of the &#8216;??&#8217; operator in C#'
date: 2008-02-18T04:40:00+00:00
author: Merill Fernando

guid: /post/2008/02/Making-use-of-the--operator-in-C.aspx
permalink: /2008/02/making-use-of-the-operator-in-c/
dsq_thread_id:
  - "77862557"
categories:
  - .NET
---
<p>
The <a href="http://msdn2.microsoft.com/en-us/library/ms173224(VS.80).aspx">?? operator</a> was introduced to C# in 2.0 and I made a mental note to myself to use it when possible.
</p>
  
<p>
Recently I had to do some tinkering with good ole Request.Form and Request.QueryString and I kept trying get the neurons to connect and figure out the shorter way of doing it. I knew there was another way to do it than write all this.
</p>
  
<div>
   
<div style="border-style: none; padding: 0px; overflow: visible; font-size: 8pt; width: 100%; color: black; line-height: 12pt; font-family: consolas,'Courier New',courier,monospace; background-color: #f4f4f4">
     
<pre style="border-style: none; margin: 0em; padding: 0px; overflow: visible; font-size: 8pt; width: 100%; color: black; line-height: 12pt; font-family: consolas,'Courier New',courier,monospace; background-color: white">
<span style="color: #606060">   1:</span> <span style="color: #0000ff">string</span> filter = Request.QueryString[<span style="color: #006080">&quot;Filter&quot;</span>];
</pre>
<pre style="border-style: none; margin: 0em; padding: 0px; overflow: visible; font-size: 8pt; width: 100%; color: black; line-height: 12pt; font-family: consolas,'Courier New',courier,monospace; background-color: #f4f4f4">
<span style="color: #606060">   2:</span> <span style="color: #0000ff">if</span> (filter == <span style="color: #0000ff">null</span>)
</pre>
<pre style="border-style: none; margin: 0em; padding: 0px; overflow: visible; font-size: 8pt; width: 100%; color: black; line-height: 12pt; font-family: consolas,'Courier New',courier,monospace; background-color: white">
<span style="color: #606060">   3:</span> {
</pre>
<pre style="border-style: none; margin: 0em; padding: 0px; overflow: visible; font-size: 8pt; width: 100%; color: black; line-height: 12pt; font-family: consolas,'Courier New',courier,monospace; background-color: #f4f4f4">
<span style="color: #606060">   4:</span>     filter = <span style="color: #006080">&quot;&quot;</span>;
</pre>
<pre style="border-style: none; margin: 0em; padding: 0px; overflow: visible; font-size: 8pt; width: 100%; color: black; line-height: 12pt; font-family: consolas,'Courier New',courier,monospace; background-color: white">
<span style="color: #606060">   5:</span> }
</pre>
</div>
</div>
<p>
And Google is no help when you have no keyword to search. This is when <a href="http://www.jetbrains.com/resharper">ReSharper</a> came in handy and prompted to replace the above code with this succinct version.
</p>
<div>
<div style="border-style: none; padding: 0px; overflow: visible; font-size: 8pt; width: 100%; color: black; line-height: 12pt; font-family: consolas,'Courier New',courier,monospace; background-color: #f4f4f4">
<pre style="border-style: none; margin: 0em; padding: 0px; overflow: visible; font-size: 8pt; width: 100%; color: black; line-height: 12pt; font-family: consolas,'Courier New',courier,monospace; background-color: white">
<span style="color: #606060">   1:</span> filter = Request.QueryString[<span style="color: #006080">&quot;Filter&quot;</span>] ?? <span style="color: #006080">&quot;&quot;</span>;
</pre>
</div>
</div>
<p>
BTW: If you are coding in VS 2008 check out the <a href="http://www.jetbrains.net/confluence/display/ReSharper/ReSharper+4.0+EAP+Notes">ReSharper 4.0 nightly builds</a>, it&#39;s awesome.
</p>
