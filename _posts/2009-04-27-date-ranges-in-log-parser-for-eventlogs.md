---
id: 577
title: Date Ranges in Log Parser for EventLogs
date: 2009-04-27T10:22:11+00:00


guid: http://merill.net/2009/04/date-ranges-in-log-parser-for-eventlogs/
permalink: /2009/04/date-ranges-in-log-parser-for-eventlogs/
dsq_thread_id:
  - "77852560"
categories:
  - Tips
tags:
  - date
  - logparser
  - range
  - timestamp
---
<p>If you need to trawl through your production server event logs. Here’s a quick tip for extracting just the entries for a given date range using LogParser. BTW <a href="http://www.codeplex.com/visuallogparser">Visual LogParser</a> is a must have, it even downloads and automatically installs the latest version of LogParer from MS.</p>  <p><font size="2" face="Courier New">SELECT&#160; TimeGenerated, SourceName, ComputerName, Message FROM C:\Downloads\May09-ErrorLog\AppLog\*.evt      <br />WHERE TimeGenerated BETWEEN timestamp('04/04/2009', 'dd/MM/yyyy') and timestamp('06/04/2009', 'dd/MM/yyyy')      <br />ORDER BY TimeGenerated desc </font></p>