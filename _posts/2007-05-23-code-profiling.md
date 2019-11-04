---
id: 51
title: Code Profiling
date: 2007-05-23T11:40:38+00:00


guid: /post/2007/05/Code-Profiling.aspx
permalink: /2007/05/code-profiling/
dsq_thread_id:
  - "77879296"
categories:
  - .NET
---
<p>Until yesterday, if anyone asked me about dynamic code profiling, I would have said that the only way to do it is to buy the Red Gate <a href="http://www.red-gate.com/products/ants_profiler/index.htm">ANTS Profiler</a> or the Jet Brains <a href="http://www.jetbrains.com/profiler">dotTrace Profiler</a>.</p> <p>Little did I know that I already had an excellent profiling tool installed right there on my machine for the last couple of years!</p> <p>So what am I talking about. It's the small menu option that you see under Tools called Performance. Aha so that's why I never knew about this all along. The VSTS most probably wanted this to be an easter egg!</p> <p><a href="http://www.merill.net/wp-content/uploads/binary/CodeProfiling_5DC8/VSTSCodeProfiler3.jpg" atomicselection="true"><img style="border-right: 0px; border-top: 0px; border-left: 0px; border-bottom: 0px" height="470" src="http://www.merill.net/wp-content/uploads/binary/CodeProfiling_5DC8/VSTSCodeProfiler_thumb1.jpg" width="517" border="0"></a> </p> <p>No worries though Orcas is going to fix this by renaming it to Profiler and moving it under the new Developer menu.</p> <p><a href="http://www.merill.net/wp-content/uploads/binary/CodeProfiling_5DC8/OrcaseDeveloperMenu6.jpg" atomicselection="true"><img style="border-right: 0px; border-top: 0px; border-left: 0px; border-bottom: 0px" height="377" src="http://www.merill.net/wp-content/uploads/binary/CodeProfiling_5DC8/OrcaseDeveloperMenu_thumb4.jpg" width="554" border="0"></a> </p> <p>No wonder that this rarely shows up on Live Search or Google. The keyword profiler is nowhere to be found even in the overview page of this feature on MSDN.</p> <p>So what can you do with the profiler today? Well you can use it to make your .NET applications super-duper fast. You'll find out things like which method gets called the most and which method takes most of the time to execute and a whole number of other things. </p>