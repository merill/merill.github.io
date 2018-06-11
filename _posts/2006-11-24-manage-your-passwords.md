---
id: 86
title: Manage your passwords
date: 2006-11-24T19:20:07+00:00
author: Merill Fernando
layout: post
guid: /post/2006/11/Manage-your-passwords.aspx
permalink: /2006/11/manage-your-passwords/
dsq_thread_id:
  - "79908496"
categories:
  - Utilities
---
<p>Another program from my &lsquo;Must Have&rsquo; folder. KeePass stores all my privata logins in a safe, secure encrypted file. It&rsquo;s open-source,&nbsp;so it&rsquo;s free as well. The features I love the most are the quick search text box as well as the macro play-back. For example I simply need to navigate to my VSS entry on KeePass&nbsp;and press Ctrl+V to have it run a macro that starts VSS Admin and logs me into the server. This is how the macro looks:</p><font size="1">
<p>Auto-Type:@r{DELAY 500}{APPACTIVATE Run}{URL}{ENTER}{DELAY 1000}{APPACTIVATE Log On To Visual SourceSafe Database}{PASSWORD}{ENTER}</p></font>
<p><img alt="KeePass" src="http://www.merill.net/KeePass_small1.jpg" border="0" /></p>
<p>KeePass is very secure, even when the data is loaded into memory it is kept encrypted. Read all about it and get it from <a href="http://keepass.sourceforge.net/">here</a>.</p>