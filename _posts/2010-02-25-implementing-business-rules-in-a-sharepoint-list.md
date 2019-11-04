---
id: 627
title: Implementing Business Rules in a SharePoint list
date: 2010-02-25T07:57:28+00:00
author: Merill Fernando

guid: http://merill.net/2010/02/implementing-business-rules-in-a-sharepoint-list/
permalink: /2010/02/implementing-business-rules-in-a-sharepoint-list/
dsq_thread_id:
  - "77728856"
categories:
  - SharePoint
tags:
  - sharepoint; business rule; form validation; sharepoint 2010
---
<p>On the project I am currently working on I had to implement a custom business rule for a list. The requirement was that only users in an Administrator group should be allowed to edit a particular field. All other users can edit that list but they are not allowed to touch that particular field.</p>  <p>Given that this was the first time I had to do this in SharePoint I did some research to figure out the best practice but came up empty. Most of suggestions were to customize the edit form and add the logic there. This clearly will not work since the business rule validation is in the UI and not in the actual list. Hence leaving it open for anyone to open in datasheet view or any of the other numerous ways (e.g. web services) to break the business rule. </p>  <p>[Note: While researching for this post I did come across the ‘<a href="http://msdn.microsoft.com/en-au/library/ee413933.aspx">Enforcing Custom List Item Data Validation</a>’ best practice by SharePoint patterns and practices group, which essentially makes the same recommendation as this blog post.]</p>  <p>SharePoint 2010 makes it a little easy with the <a href="http://www.sharemuch.com/2010/02/06/provisioning-validation-formula-to-sharepoint-2010-list-field/">Validation Formula</a> feature which lets you add business rules to any list directly from the UI. But with SharePoint 2007 you’ll need to use an <a href="http://blah.winsmarts.com/2006-7-Sharepoint_2007__List_Events_Practical_Example__Creating_a_rigged_survey.aspx">SPItemEventReceiver</a> to implement your business rule.</p>  <p>There is a good code sample on validating a list in the <a href="http://msdn.microsoft.com/en-au/library/ee413940.aspx">List Item Event Receivers</a> article on TechNet.</p>