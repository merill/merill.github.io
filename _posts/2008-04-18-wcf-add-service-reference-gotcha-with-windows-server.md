---
id: 14
title: WCF Add Service Reference gotcha with Windows Server
date: 2008-04-18T09:11:00+00:00


guid: /post/2008/04/WCF-Add-Service-Reference-gotcha-with-Windows-Server.aspx
permalink: /2008/04/wcf-add-service-reference-gotcha-with-windows-server/
dsq_thread_id:
  - "77716141"
categories:
  - .NET
---
<p>
We recently switched from developing in Vista to Windows Server 2003. Someone had the bright idea that we should develop in the same environment the application is going to be hosted on. Go figure.
</p>
<p>
What that meant is that you run into wierd issues like this one. When trying to add a Service Reference to a WCF service hosted under IIS you keep getting this &#39;Add Service Reference&nbsp;Error&#39;:
</p>
<p>
<font face="courier new,courier">Metadata contains a reference that cannot be resolved: &#39;http://merill/Services.Host/ClientProfile.svc?wsdl&#39;.<br />
The WSDL document contains links that could not be resolved.<br />
There was an error downloading &#39;http://merill/Services.Host/ClientProfile.svc?xsd=xsd0&#39;.<br />
The underlying connection was closed: An unexpected error occurred on a receive.<br />
Unable to read data from the transport connection: An existing connection was forcibly closed by the remote host.<br />
An existing connection was forcibly closed by the remote host<br />
Metadata contains a reference that cannot be resolved: &#39;http://localhost/Services.Host/ClientProfile.svc&#39;.<br />
Metadata contains a reference that cannot be resolved: &#39;http://localhost/Services.Host/ClientProfile.svc&#39;.<br />
If the service is defined in the current solution, try building the solution and adding the service reference again.</font>
</p>
<p>
The key part of this message is the reference to the downloading of the xsd. When I tried accessing the .svc url in a browser it worked fine, but trying to access the .svc?xsd=xsd0 brings up the generic &#39;cannot display webpage&#39; message.
</p>
<p>
When you unleash your&nbsp;weapon (<a href="http://www.microsoft.com/technet/sysinternals/fileanddisk/processmonitor.mspx">Process Monitor</a>) on the csc.exe process (this is the compiler generating the xsd) you&#39;ll realise that the IIS&nbsp;identity IIS_WPG does not have access to the Windows\Temp folder. Give enough rights to the folder and viola problemo solved.
</p>
<p>
Happy WCF programming on Windows Server!
</p>
