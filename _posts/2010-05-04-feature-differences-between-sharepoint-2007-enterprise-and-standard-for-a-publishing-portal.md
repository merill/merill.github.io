---
id: 673
title: Feature differences between SharePoint 2007 Enterprise and Standard for a Publishing Portal
date: 2010-05-04T09:26:51+00:00


guid: https://merill.net/?p=673
permalink: /2010/05/feature-differences-between-sharepoint-2007-enterprise-and-standard-for-a-publishing-portal/
dsq_thread_id:
  - "92122147"
categories:
  - SharePoint
tags:
  - SharePoint
  - site template
---
I recently had to deploy a site template that was built using SharePoint Enterprise Edition 2007 on an instance of SharePoint Standard Edition 2007.

Obviously given that some features were not available in the Standard Edition I received the 'The template you have chosen is invalid or cannot be found'. Unlike a <a href="http://www.sharepointconfig.com/2007/05/moss-site-templates-not-compatible-with-wss/">MOSS to WSS conversion</a> the problem here is that the features do exist on the server but are simply not available for the standard edition.

I basically resorted to manually comparing the differences between a site template created in the Standard edition vs one created in the Enterprise edition.

Here's the list if anyone ever needs this.

<a href="https://merill.net/wp-content/uploads/2010/05/Publishing-Features-Standard-vs-Enterpise.png"><img class="alignnone size-medium wp-image-674" title="Publishing-Features-Standard-vs-Enterpise" src="{{ site.url }}{{ site.baseurl }}/wp-content/uploads/2010/05/Publishing-Features-Standard-vs-Enterpise-300x222.png" alt="" width="300" height="222" /></a>

Remove these features from a template created in the Enterprise edition if you want to deploy it on a Standard edition. Obviously you need to test to ensure that your template is not actually using any of the Enterprise features.
<code>
&lt;Feature ID="065c78be-5231-477e-a972-14177cc5b3c7" /&gt;
&lt;Feature ID="0806d127-06e6-447a-980e-2e90b03101b8" /&gt;
&lt;Feature ID="2510d73f-7109-4ccc-8a1c-314894deeb3a" /&gt;
&lt;Feature ID="e8734bb6-be8e-48a1-b036-5a40ff0b8a81" /&gt;
&lt;Feature ID="00bfea71-dbd7-4f72-b8cb-da7ac0440130" /&gt;
</code>