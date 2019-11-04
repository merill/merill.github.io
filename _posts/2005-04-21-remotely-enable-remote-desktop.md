---
id: 204
title: Remotely Enable Remote Desktop
date: 2005-04-21T02:43:21+00:00


guid: /post/2005/04/Remotely-Enable-Remote-Desktop.aspx
permalink: /2005/04/remotely-enable-remote-desktop/
dsq_thread_id:
  - "78633530"
categories:
  - Tips
---
<p>I didn&rsquo;t know this was so easy.</p>
<ol>
<li>Connect to the remote registry of the machine</li>
<li>Browse to <font face="Courier New" size="2">HKLM\SYSTEM\CurrentControlSet\Control\Terminal Server</font></li>
<li>Change <font face="Courier New" size="2">fDenyTSConnection </font>from 1 to 0 </li>
<li>Restart the remote machine for the setting to take effect: <font face="Courier New" size="2">shutdown -m \\servername -r</font></li></ol>
<p>Remember that you need to have administrator rights on the remote machine.</p>