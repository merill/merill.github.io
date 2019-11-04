---
id: 222
title: Installing Visual Studio .NET on a Domain Controller
date: 2005-03-14T20:23:22+00:00
author: Merill Fernando

guid: /post/2005/03/Installing-Visual-Studio-NET-on-a-Domain-Controller.aspx
permalink: /2005/03/installing-visual-studio-net-on-a-domain-controller/
dsq_thread_id:
  - "79769797"
categories:
  - Microsoft
---
<p>As part of setting up the <a href="http://www.testdriven.com/">TDD</a> environment for the next project that I&rsquo;m going to be working on, I started by trying to setup <a href="http://cruisecontrol.sourceforge.net/">CruiseControl.NET</a> on my VSS server when I released that it didn&rsquo;t have Visual Studio .NET. </p>
<p>But trying to install Visual Studio .NET over Terminal Services on a domain controller&nbsp;started throwing up a multitude of error messages and finally&nbsp;failed installing the FrontPage Web Extensions. </p>
<p>So what did I do? I figured it was something to do with Terminal Services, so instead I setup <a href="http://www.realvnc.com/">RealVNC</a> (they&rsquo;ve recently release Version 4) on the box and then ran the setup. Would you believe it, not a single error message.</p>