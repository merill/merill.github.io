---
id: 1039
title: Allowing third party applications in your Office 365 tenant
date: 2016-08-11T23:09:13+00:00


guid: http://merill.net/?p=1039
permalink: /2016/08/allowing-third-party-applications-in-your-office-365-tenant/
medium_post:
  - 'O:11:"Medium_Post":11:{s:16:"author_image_url";s:69:"https://cdn-images-1.medium.com/fit/c/200/200/0*nOSMyIhdQJ9325FH.jpeg";s:10:"author_url";s:26:"https://medium.com/@merill";s:11:"byline_name";N;s:12:"byline_email";N;s:10:"cross_link";s:2:"no";s:2:"id";s:12:"67bee350e10f";s:21:"follower_notification";s:3:"yes";s:7:"license";s:19:"all-rights-reserved";s:14:"publication_id";s:12:"99858869fb3c";s:6:"status";s:6:"public";s:3:"url";s:99:"https://medium.com/@merill/allowing-third-party-applications-in-your-office-365-tenant-67bee350e10f";}'
snap_isAutoPosted:
  - "1"
dsq_thread_id:
  - "5059431574"
snap_MYURL:
  - ""
snapEdIT:
  - "1"
snapFB:
  - 's:240:"a:1:{i:0;a:9:{s:2:"do";i:0;s:8:"postType";s:1:"T";s:10:"AttachPost";s:1:"2";s:10:"SNAPformat";s:10:"%FULLTEXT%";s:9:"isAutoImg";s:1:"A";s:8:"imgToUse";s:0:"";s:9:"isAutoURL";s:1:"A";s:8:"urlToUse";s:0:"";s:9:"msgFormat";s:10:"%FULLTEXT%";}}";'
snapLI:
  - 's:350:"a:1:{i:0;a:10:{s:2:"do";s:1:"1";s:8:"postType";s:1:"A";s:10:"SNAPformat";s:41:"New post has been published on %SITENAME%";s:12:"liMsgFormatT";s:14:"{Blog} %TITLE%";s:9:"isAutoImg";s:1:"A";s:8:"imgToUse";s:0:"";s:9:"isAutoURL";s:1:"A";s:8:"urlToUse";s:0:"";s:11:"isPrePosted";s:1:"1";s:9:"msgFormat";s:41:"New post has been published on %SITENAME%";}}";'
snapTW:
  - 's:355:"a:1:{i:0;a:12:{s:2:"do";s:1:"1";s:10:"SNAPformat";s:15:"%TITLE% - %URL%";s:8:"attchImg";s:1:"1";s:9:"isAutoImg";s:1:"A";s:8:"imgToUse";s:0:"";s:11:"isPrePosted";s:1:"1";s:8:"isPosted";s:1:"1";s:4:"pgID";s:18:"763724039084838913";s:5:"pDate";s:19:"2016-08-11 13:09:34";s:9:"msgFormat";s:15:"%TITLE% - %URL%";s:9:"isAutoURL";s:1:"A";s:8:"urlToUse";s:0:"";}}";'
categories:
  - Office 365
tags:
  - azure
  - office 365
---
When managing Office 365 (and it's related Azure Active Directory) in a large enterprise your security team is wary about allowing third party applications to access enterprise data.

Take for example the list of options that you have available in the 'configure' tab in Azure AD under the 'integrated applications' section. If you turn on the 'Users may add integrated applications' you will start seeing a number of applications showing up in Azure AD under the applications section. What this means is that users are accessing third party applications and using their work account as the identity.

<img class="alignnone size-full wp-image-1040" src="https://merill.net/wp-content/uploads/2016/08/integrated-applications-azure.png" alt="integrated-applications-azure" width="930" height="648" />

Where this gets a little scary is with the option that says 'Users may give applications permission to access their data'. Depending on the type of permission requested by the application the user consents to in the consent page of the app (shown during the sign on process), they can potentially give third party applications access to their email, content in SharePoint Online etc. <a href="https://bestforthekids.com">as shown by Roger</a> from BestForTheKids.

Where I come from this is a big fat no from security. We typically require the security team vetting every SaaS application where the checks include performing vendor assessments, finding out what information is stored and how secure it is, whether the content is stored in Australia (data sovereignty).

Fine, let's say we disable all this to prevent end users willy nilly giving third party applications access to corporate data. You will be faced with a dilemma when you have an application that has been approved (eg Microsoft's own Fast Track portal <a href="http://fasttrack.microsoft.com">http://fasttrack.microsoft.com</a>) by your security team your users will still not be able to sign in to the third party app because of the above settings where we disabled users adding apps.

When a user tries to sign into the portal they will be shown an error message saying 'Sorry but we're having trouble signing you in. We received a bad request'.

So how do you go about whitelisting only certain apps on your Office 365 / Azure Active Directory tenant? I reached out to my friends at Microsoft and this time they had an answer that made me happy.
<blockquote>Today the only way for an admin to consent to an application for his entire tenant is to send an interactive sign-in request with the query parameter ?prompt=admin_consent. We usually ask the app developer to invoke this request in their app somehow. But you can actually craft the request as a link yourself and have an admin click on it. There's documentation on http://aka.ms/aaddev on how to craft a sign in request. We are working on adding this capability to our portal directly so you dont have to do this.</blockquote>
So the trick is to open a browser session in private/incognito mode and navigate to the target application (e.g. Fast Track) and try to sign in. This will redirect you to Microsoft's login page. When you are at this page insert the ?prompt=admin_consent parameter to the query string in the the address bar and hit enter to reload the sign in page. Now sign in as a global administrator for the tenant and you will be taken to the admin consent page. Review the settings that you are approving and click on Accept. Viola you've now approved the app in your tenant. Now any user in your organisation can sign into the third party app without login errors and won't even see the consent screen.

<img class="alignnone size-full wp-image-1042" src="https://merill.net/wp-content/uploads/2016/08/05_thumb.png" alt="05_thumb" width="640" height="350" />

&nbsp;