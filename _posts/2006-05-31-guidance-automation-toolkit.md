---
id: 132
title: Guidance Automation Toolkit
date: 2006-05-31T17:22:00+00:00
author: Merill Fernando

guid: /post/2006/05/Guidance-Automation-Toolkit.aspx
permalink: /2006/05/guidance-automation-toolkit/
dsq_thread_id:
  - "77852174"
categories:
  - .NET
---
<p>There were a couple of recent posts in the <a href="http://dotnetforum.lk/">forum</a> asking what GAT was and how one gets started on using this, so I thought of writing a post to cover the answers.</p>
<p>Let's just take one aspect: Say for example architecting the data access in software solutions developed at your company.</p>
<p>You might define whether it be using CRUD operations or using an ORM. Once you decide on the architecture you want all your developers to follow that methodology along with the best practices.</p>
<p>One way that you give guidance to your developers is through writing a document with all the relevant guidelines. Another option that you could do is build a utility that let's the developer walk through a wizard which would then generate the skeleton or handle most of the mundane things like writing the insert, update sp's and related .NET code.</p>
<p>Now building a utility like this takes a lot of time and effort, this is exactly where GAT fits in. It let's you define the guidance to developers in an easier manner (than if you were to write your own) so that it becomes very easy for your developers to follow the guidance that you have defined. They don't need to read long documents but can instead use the toolkit that you provide.</p>
<p>The best way to learn GAT is to practice it. Try out this HOL (<a href="http://guidanceautomation.net/cs/library/view.aspx?tab=3&amp;id=40">Hands-On Lab: Data Client Application</a>)&nbsp;which walks you through creating a guidance package for generating the data access classes as well as connecting them to a simple smart client.</p>