---
id: 447
title: The Uncanny Disappearing Window
date: 2003-12-16T12:41:48+00:00
author: Merill Fernando

guid: /post/2003/12/The-Uncanny-Disappearing-Window.aspx
permalink: /2003/12/the-uncanny-disappearing-window/
dsq_thread_id:
  - ""
categories:
  - HTML
---
<body xmlns="http://www.w3.org/1999/xhtml">
    <div class="Section1">
        <p>
            How do you programmatically close a browser window when you didn't open it? Of course,
            everybody knows you can't. If they don't know that, they're novice developers and
            some seasoned veteran will set them straight... gently or otherwise.
        </p>
        <p>
            Well, this week one of my clients -- whose intranet app opens in a specially formatted
            window -- told me they didn't want two windows just to start one application. I had
            very little success removing the toolbars from an existing window, and my vast web
            development experience told me that I had no other option. Rather, I didn't until
            a suggestion from a fellow member of the LaTech JavaScript list altered my perspective
            and resulted in the script I'm about to show you.
        </p>
        <p>
            All you need to start the magic is to assign a window to the opener property of the
            current window. If this attribute is not set, the browser will realize that the current
            window is not open to your manipulation and nothing will happen.
        </p>
        <p>
            <span style=';font-family: "Courier New"'>&#160;&#160;&#160;&#160;&#160; &lt;SCRIPT
            LANGUAGE="JavaScript"&gt;<br />
            &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; window.opener =
            top;<br />
            &#160;&#160;&#160;&#160;&#160; &lt;/SCRIPT&gt;</span>
        </p>
        <p>
            [<a href="http://aspalliance.com/333">Read more</a>]
        </p>
    </div>
</body>