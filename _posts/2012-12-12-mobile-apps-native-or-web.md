---
id: 803
title: 'Mobile Apps: Native or Web?'
date: 2012-12-12T18:12:35+00:00
author: Merill Fernando
layout: post
guid: http://merill.net/?p=803
permalink: /2012/12/mobile-apps-native-or-web/
dsq_thread_id:
  - "970294894"
categories:
  - Opinion
tags:
  - app
  - dev
---
When building for mobile there isn't a silver bullet. Instead we have a myriad of compromises to make. If your an enterprise wanting to build apps here are four broad options.

<strong>Native code</strong> (Objective C for iOS, Java for Android, C#/Xaml for Windows)

Pros:
<ul>
	<li>Build the best experience in each platform (Native UI, Performance)</li>
	<li>Discoverable in app stor</li>
</ul>
Cons:
<ul>
	<li>Cost (3 codebases)</li>
	<li>Dev skills</li>
	<li>Publishing to each app store, wait for approvals etc</li>
</ul>
<strong>Native with re-usable code</strong> (C# for platforms -&gt; MonoTouch for iOS, Mono for Android, C#/Xaml for Windows) <a href="http://xamarin.com">http://xamarin.com</a>

Pros:
<ul>
	<li>Build the best experience in each platform (Native UI, Performance)</li>
	<li>Discover-able in app store</li>
	<li>Code reuse (except for the presentation layer in each platform the rest of the business logic, web service calls etc are reusable)</li>
</ul>
Cons:
<ul>
	<li>Cost (Cheaper than 100% native but will cost more than plain html)</li>
	<li>Dev skills (Devs still need to understand the UI APIs for each platform e.g. CocoaTouch, UIKit…</li>
	<li>Publishing to each app store, wait for approvals (e.g. you find a bug fix it and submit to app store, it will then take 5 business days before the bug fix is available for end users to download).</li>
</ul>
<strong>HTML but deployed natively</strong> (PhoneGap, Sencha, etc…)

Pros
<ul>
	<li>Javascript (Use frameworks /tools such as jQuery mobile, TypeScripts etc)</li>
	<li>Costs less to build (one code base across platforms)</li>
</ul>
Cons:
<ul>
	<li>Performance issues with iOS webkit (Only Apple apps and Safari browser can use the hardware accelerated Nitro JavaScript engine, everyone else is forced to use the slower js engine. This is why Facebook ditched HTML5 and wrote a native iOS app). If the apps we’re building are not going to be flashy and don’t rely on animations then this is a non-issue.</li>
	<li>UI is not native to each OS</li>
	<li>App updates need to go through approval process for each App Store</li>
</ul>
<strong>HTML only</strong>: Basically a web site (ASP.NET MVC or a SharePoint app / application page with responsive layout to adapt to a mobile browser)

Pros:
<ul>
	<li>Javascript (Use frameworks /tools such as jQuery mobile, TypeScripts etc)</li>
	<li>Costs less to build (one code base across platforms)</li>
	<li>Performance will be better (but not as good as native) since the site runs in Safari and can use hardware acceleration</li>
	<li>Updates to app is just a matter of pushing update to website (user doesn’t need to upload etc)</li>
	<li>Option #1 and #2 will anyway need a website to host the webservice</li>
</ul>
Cons:
<ul>
	<li>UI is not native to each OS</li>
	<li>Discover-ability: No app store. User needs to bookmark app url. Enterprises can work around this by having a single Web App Store that lists all their web apps (ala <a href="http://www.apple.com/webapps">http://www.apple.com/webapps</a>). Or build a shell native app that acts as a launcher for the web apps.</li>
</ul>
Need more options/tool choices? See <a href="http://en.wikipedia.org/wiki/Mobile_application_development">http://en.wikipedia.org/wiki/Mobile_application_development</a>

Another disadvantage with the native options. You need to build and publish a mobile and a tablet version of the app.

My view is that while native apps are the better choice for companies that build and sell services/products, the web option gives the best ROI for enterprises. Even when it comes to product/service companies a strong case can be made for going web only. <a href="http://37signals.com/svn/posts/2761-launch-basecamp-mobile">Ask the guys</a> who built Basecamp.