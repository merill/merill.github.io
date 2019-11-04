---
id: 465
title: Session State
date: 2003-11-28T12:49:13+00:00
author: Merill Fernando

guid: /post/2003/11/Session-State.aspx
permalink: /2003/11/session-state/
dsq_thread_id:
  - "78022465"
categories:
  - .NET
---
<body xmlns="http://www.w3.org/1999/xhtml">
    <div class="Section1">
        <p>
            Steve <a href="http://hyperthink.net/blog/PermaLink.aspx?guid=6d6c9a73-42a1-4fec-86a1-e0e58a410eb4">talks</a> about
            how we can make more efficient use of the Session state in ASP.NET.
        </p>
        <p>
            It&rsquo;s something that we as developers should try to follow as a guideline. The
            idea is to use a private <span class="SpellE">SessionState</span> object (<span class="SpellE">struct</span>)
            which has fields for each property you need to store in the session. This way you
            don&rsquo;t need to use ugly strings when setting/accessing session variables and
            you get the advantage of the compiler doing early-bound checks for you.
        </p>
    </div>
</body>