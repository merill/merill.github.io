---
id: 569
title: Microsoft .NET Framework 3.5 SP1 breaks Microsoft CCF (Customer Care Framework)
date: 2009-02-26T12:27:32+00:00


guid: https://merill.net/2009/02/microsoft-net-framework-35-sp1-breaks-microsoft-ccf-customer-care-framework/
permalink: /2009/02/microsoft-net-framework-35-sp1-breaks-microsoft-ccf-customer-care-framework/
dsq_thread_id:
  - "77713025"
categories:
  - Tips
tags:
  - ccf
  - service pack
  - wcf
---
<p>So your seeing this exception in your WCF client application after installing SP1 on .NET Framework 3.5 </p>  <p><em>System.ServiceModel.Security.MessageSecurityException occurred Message=&quot;The HTTP request is unauthorized with client authentication scheme 'Negotiate'. The authentication header received from the server was 'Negotiate </em></p>  <p>As described in this <a href="https://connect.microsoft.com/VisualStudio/feedback/ViewFeedback.aspx?FeedbackID=364077">bug report</a> Microsoft classifies this as a known issue, with the bug being resolved as ‘By Design’.</p>  <p>Your fix is to add an identity element to the WCF endpoint like this.</p>  <div>   <pre style="border-bottom-style: none; padding-bottom: 0px; line-height: 12pt; border-right-style: none; background-color: #f4f4f4; margin: 0em; padding-left: 0px; width: 100%; padding-right: 0px; font-family: consolas, &#39;Courier New&#39;, courier, monospace; border-top-style: none; color: black; font-size: 8pt; border-left-style: none; overflow: visible; padding-top: 0px"><span style="color: #0000ff">&lt;</span><span style="color: #800000">identity</span><span style="color: #0000ff">&gt;</span>
    <span style="color: #0000ff">&lt;</span><span style="color: #800000">userPrincipalName</span> <span style="color: #ff0000">value</span><span style="color: #0000ff">=&quot;WcfServiceAccount@domain&quot;</span> <span style="color: #0000ff">/&gt;</span>
<span style="color: #0000ff">&lt;/</span><span style="color: #800000">identity</span><span style="color: #0000ff">&gt;</span></pre>
</div>

<p>But the problem with CCF is that the url for some of the endpoints are read through code from a database and set through the proxy class. Now when you do this the identity from the config file does not flow through resulting in the same exception you see above.</p>

<p>One option is to uninstall the service pack on the client. This is not as easy as it seems because the the 3.5 service pack also updates assemblies in the 2.0 and 3.0 frameworks to their SP2 levels.</p>

<p>To get back to pre 3.5 SP1 you need to uninstall all the frameworks and re-install them again avoiding the 3.5 SP1. The exact steps to do this is outlined <a href="http://blogs.msdn.com/astebner/archive/2008/08/01/8803442.aspx">here</a> by Microsoft engineer, Aaron Stebner. </p>

<p>But what if you don’t have the luxury of walking all your end-users through the uninstall? A suggested fix from Microsoft (targeting CCF) is as follows:</p>

<ol>
  <li>Set up a cNAME in DNS for the servername you are using in database urls.</li>

  <li>Use setspn -a HOST/CNAME domain\apppooluser</li>

  <li>Change all the database urls to this CNAME</li>

  <li>Do an iisreset</li>

  <li>Test</li>
</ol>

<p>For example if the database urls are <a href="http://ccfserver/">http://ccfserver/</a>.....</p>

<ol>
  <li>Create a&#160; CNAME CCFALIAS in DNS</li>

  <li>setspn -a HOST/CCFALIAS ccf\aspuser</li>

  <li>Change all database urls to ccfalias</li>

  <li>iisreset</li>

  <li>Test if you reach /urls with this alias from web servers and from clients</li>
</ol>

<p>Be careful not to set HOST/CCFSERVER spn for aspuser. Note we are setting HOST/CCFALIAS spn which is CNAME for ccfserver in DNS. If by mistake you set host/ccfserver it can wreak havoc&#160; for Kerberos.</p>