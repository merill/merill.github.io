---
id: 123
title: XslCompiledTransform Performance
date: 2006-08-24T15:59:49+00:00


guid: /post/2006/08/XslCompiledTransform-Performance.aspx
permalink: /2006/08/xslcompiledtransform-performance/
dsq_thread_id:
  - "77984559"
categories:
  - .NET
---
<p>Have&nbsp;you&rsquo;ve ever written any code on .NET that does XSL transformations? Here&rsquo;s another strong reason why you might think of making the jump to .NET 2.0 and start taking advantage of the .NET 2.0&rsquo;s XslCompiledTransform class.</p>
<p><a class="headermaintitle" id="_ctl0____ctl0___bt___BlogTitle" href="http://blogs.msdn.com/antosha/default.aspx">Anton Lapounov</a>&nbsp;does a <a href="http://blogs.msdn.com/antosha/archive/2006/07/24/677560.aspx">comparison</a> of&nbsp;the major XSL transformers out there and the results are eye opening.</p>
<p><img alt="XslCompiledTransform" src="/wp-content/uploads/contentbinary/XslCompiledTransform.jpg" border="0" /></p>
<p>If you&rsquo;ve tried building any of your pre 2.0 applications in Visual Studio 2005, you would have already seen the warning which keeps pushing you to use the XslCompiledTransform class.</p>
<p>The major jump in performance is due to the fact that we&rsquo;re now using an XSL compiler as opposed to the rest which are all interpreters.</p>