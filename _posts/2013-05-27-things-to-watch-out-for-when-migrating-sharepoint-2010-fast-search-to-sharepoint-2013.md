---
id: 813
title: Things to watch out for when migrating SharePoint 2010 FAST Search to SharePoint 2013
date: 2013-05-27T14:08:12+00:00


guid: http://merill.net/?p=813
permalink: /2013/05/things-to-watch-out-for-when-migrating-sharepoint-2010-fast-search-to-sharepoint-2013/
dsq_thread_id:
  - "1324417246"
categories:
  - SharePoint
tags:
  - search
  - SharePoint
  - Tips
---
I'm currently working on a <a href="http://technet.microsoft.com/en-us/library/dn130132(v=office.15)">Search First migration </a>to SharePoint 2013. This post is a placeholder to document the gotchas and workarounds.

<strong>Search Centre Keywords</strong>

Our initial plan was for a search-first migration where we would swap out the FAST search service application for an SP2013 search service application. The idea was that we would make no changes to the existing search centres but they would get a better/fast search engine with all the improvements that come in 2013.

Issue: Keywords defined in the SP 2010 Search Centre are ignored by SP2013 Search. The only way this functionality can work is when you use a SP2013 search centre. This is not a problem if you have only one search centre since you can manage the keywords at a farm level but we had a number of search centres with site collection admins needing the ability to manage the keywords for the site they manage.

Workaround: We were forced to create Search Centres in SP 2013 and have the SP 2010 sites use the new search centres.

<strong>XSLT to Display Templates</strong>

Given that we were on the path to using SP2013 search centres any customisations that were made to the SP2010/FAST search XSL now needs to be re-written as Display Templates. In a way this is better than having to mess with XSL, but this is still something that you need to take into account.

&nbsp;