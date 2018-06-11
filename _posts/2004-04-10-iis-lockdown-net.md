---
id: 293
title: 'IIS Lockdown &#038; .NET'
date: 2004-04-10T08:31:13+00:00
author: Merill Fernando
layout: post
guid: /post/2004/04/IIS-Lockdown--NET.aspx
permalink: /2004/04/iis-lockdown-net/
dsq_thread_id:
  - "78553606"
categories:
  - .NET
  - ASP.NET
---
<P>I recently ran into quite a few problems when the <A href="http://www.microsoft.com/windows2000/downloads/recommended/iislockdown/default.asp">IIS Lockdown</A> tool was applied on one of our production servers. I'm listing it here so that&nbsp;I don't trip over it again and also end&nbsp;up helping anyone who comes across the same problem.</P>
<P>My scenario is that we have a classic asp application relying on .NET components which use MSMQ. After applying the lock down tool the asp application worked fine until it called one of the .NET components that sent a message through MSMQ which threw this exeception:</P>
<P align=left><FONT face="Courier New">Cannot execute a program. The command being executed was "c:\winnt\microsoft.net\framework\v1.1.4322\csc.exe".</FONT>&nbsp;</P>
<P>What I found out was that the XmlSerializer which was used by System.Messaging to send the message created&nbsp;a dynamic class and compiles it on the fly. The problem is that the lockdown tool denies access to all the .exe files in the Windows system folder (and subfolders). This prevents the csc.exe&nbsp;or vbc.exe&nbsp;which is in C:\WINNT\Microsoft.NET\Framework\v1.1.4322&nbsp;from being able to dynamically compile. To fix this I gave the Web Applications group Execute permissions for this file but this threw another exception. </P>
<P align=left><FONT face="Courier New">File or assembly name sk-fuua9.dll, or one of its dependencies, was not found.</MESSAGE><STACKTRACE> at System.Reflection.Assembly.nLoad(AssemblyName fileName...</FONT></P>
<P>After spending a couple of hours trying to figure this out, I finally got around to using the excellent <A href="http://www.sysinternals.com/ntw2k/source/filemon.shtml">FileMon</A> tool which highlighted that the cvtres.exe too was used by csc.exe when attempting to compile. So I ended up giving Execute permissions for the cvtres.exe file for the Web Applications group and wallah problem solved!</P>
<P>The Microsoft KB recommends creating an seperate user and impersonating it in the application. But I feel that going&nbsp;this route makes it more secure since the default groups created by the lock down tool revokes most of the rights, which is not the case when you create your own user.</P>