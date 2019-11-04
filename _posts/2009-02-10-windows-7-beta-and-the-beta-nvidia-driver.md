---
id: 565
title: Windows 7 beta and the beta nVidia Driver
date: 2009-02-10T07:59:58+00:00
author: Merill Fernando

guid: http://merill.net/2009/02/windows-7-beta-and-the-beta-nvidia-driver/
permalink: /2009/02/windows-7-beta-and-the-beta-nvidia-driver/
dsq_thread_id:
  - "77713006"
categories:
  - Microsoft
tags:
  - nvidia
  - windows 7
---
<p>Two words: Don’t install</p>  <p>This is what <a href="http://www.nvidia.com/object/windows_7.html">nVidia says</a> and you typically get it through Windows Update. I suffered with the title bar going missing and ugly black blocks on my desktop for a week before I figured that the nVidia beta drivers were to blame. It looks like others too are having the <a href="http://stevencwong.spaces.live.com/Blog/cns!4320F28E64229E18!998.entry">same problem</a>.</p>  <p>It appears on Windows Update as: <em>NVIDIA driver update for NVIDIA GeForce 8400M GS (Prerelease – WDDM 1.1) Optional</em></p>  <p>If you already installed it you can either Rollback the Update:</p>  <ol>   <li>Start-&gt; type in ‘Device Manager’ and open it</li>    <li>Expand the Display adapters node</li>    <li>Double-click the NVIDIA node</li>    <li>On the Driver tab click ‘Roll Back Driver’</li> </ol>  <p>Or you could uninstall the driver</p>  <ol>   <li>Start –&gt; type in ‘Programs’ and launch ‘Add or remove programs’</li>    <li>In the search box (top right) type in ‘nvidia’</li>    <li>Right-click and uninstall the ‘NVIDIA Drivers’ </li> </ol>  <p>After one (sometimes two) re-boots you should be all set. </p>