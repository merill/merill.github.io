---
id: 609
title: 'CKS: World Clock and Weather WebPart with Proxy Support'
date: 2009-11-18T17:47:49+00:00


guid: http://merill.net/2009/11/cks-world-clock-and-weather-webpart-with-proxy-support/
permalink: /2009/11/cks-world-clock-and-weather-webpart-with-proxy-support/
dsq_thread_id:
  - "77751917"
categories:
  - Utilities
tags:
  - SharePoint
  - weather
---
<p>I recently had to add proxy support to the <a href="http://www.codeplex.com/Release/ProjectReleases.aspx?ProjectName=CKS&amp;ReleaseId=7649">Community Kit for SharePoint: World Clock and Weather WebPart</a>.</p>  <p>IT Teams usually like to lock down the proxy server and are not happy when they need to allow anonymous access for outgoing requests.</p>  <p>Looking around none of the the free ones seem to support this. Not even the cool, free <a href="http://store.bamboosolutions.com/ps-55-5-world-clock-and-weather-web-part.aspx">Silverlight</a> one from Bamboo Solutions.</p>  <p>So I added proxy support to the CKS World Clock and Weather WebPart that was released on CodePlex (v1.0.15 to be exact). I looked at the licenses and I don’t think I’m breaking any of them by sharing the source code and the setup over at MSDN Code Gallery.</p>  <p>There were numerous posts on various forums wishing to enable <a style="text-decoration: none" href="http://incognitoline.com/anonymous-proxy-server/"><font color="#555555">proxy server</font></a> support. So here’s hoping someone might find it useful.</p>  <p><a href="https://merill.net/wp-content/uploads/2009/11/WorldClockAndWeatherWebPartWithProxySupport.png"><img style="border-bottom: 0px; border-left: 0px; display: inline; border-top: 0px; border-right: 0px" title="WorldClockAndWeatherWebPartWithProxySupport" border="0" alt="WorldClockAndWeatherWebPartWithProxySupport" src="https://merill.net/wp-content/uploads/2009/11/WorldClockAndWeatherWebPartWithProxySupport_thumb.png" width="327" height="276" /></a> </p>  <p><a href="http://code.msdn.microsoft.com/CKSWeatherWithProxy/">Download CKS: Weather WebPart with Poxy - Setup</a></p>