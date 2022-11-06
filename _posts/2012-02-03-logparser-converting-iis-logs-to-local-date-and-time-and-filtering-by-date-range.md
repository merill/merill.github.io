---
id: 750
title: 'LogParser &#8211; Converting IIS logs to local date and time and filtering by date range'
date: 2012-02-03T07:02:26+00:00


guid: https://merill.net/?p=750
permalink: /2012/02/logparser-converting-iis-logs-to-local-date-and-time-and-filtering-by-date-range/
dsq_thread_id:
  - "968759250"
categories:
  - Uncategorized
tags:
  - date
  - iis
  - log
  - logparser
  - time
  - utc
---
This is a note to myself to remember how to convert the UTC date/time to the local timezone.

logparser "SELECT TO_TIMESTAMP(date, time) AS utc-timestamp, TO_LOCALTIME(utc-timestamp) AS local-timestamp,* FROM D:\Log\SearchServiceWrapperLogs\SearchServiceWrapperLogs\u_ex1202* WHERE local-timestamp between timestamp('2012/02/02 00:00:00', 'yyyy/MM/dd hh:mm:ss') and timestamp('2012/02/03 00:00:00', 'yyyy/MM/dd hh:mm:ss')" -recurse:-1 -o:csv >> fulllog.csv
