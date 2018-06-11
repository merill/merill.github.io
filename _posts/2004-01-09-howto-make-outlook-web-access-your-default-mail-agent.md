---
id: 412
title: 'HOWTO: Make Outlook Web Access Your Default Mail Agent'
date: 2004-01-09T12:07:19+00:00
author: Merill Fernando
layout: post
guid: /post/2004/01/HOWTO-Make-Outlook-Web-Access-Your-Default-Mail-Agent.aspx
permalink: /2004/01/howto-make-outlook-web-access-your-default-mail-agent/
dsq_thread_id:
  - "80092096"
categories:
  - Tips
---
<body xmlns="http://www.w3.org/1999/xhtml">
    <div class="Section1">
        <blockquote style='margin-top:5.0pt;margin-bottom:5.0pt'> 
        <p>
            <span style=';font-family:Arial'>Here's a little off-topic post for you all.&#160;
            HOWTO: Make OWA your default mailer.</span>
        </p>
        <p>
            <span style=';font-family:Arial'>1.&#160; Add the following&#160;to&#160;a .reg file</span>
        </p>
        <blockquote style='margin-top:5.0pt;margin-right:0in;margin-bottom:5.0pt'> 
        <p>
            <em><i><span style=';font-family: Arial'>Windows Registry Editor Version 5.00</span></i></em>
        </p>
        <p>
            <em><i><span style=';font-family: Arial'>[HKEY_LOCAL_MACHINE\SOFTWARE\Clients\Mail\OWA]</span></i></em><i><span style=';font-family:Arial;font-style: italic'>
            <br />
            <em><i><span style='font-family:Arial'>@="Outlook Web Access"</span></i></em></span></i>
        </p>
        <p>
            <em><i><span style=';font-family: Arial'>[HKEY_LOCAL_MACHINE\SOFTWARE\Clients\Mail\OWA\shell\open\command]</span></i></em><i><span style=';font-family:Arial;font-style: italic'>
            <br />
            <em><i><span style='font-family:Arial'>@="\"C:\\Program Files\\Internet Explorer\\iexplore.exe\"
            http://server/exchange/alias/"</span></i></em></span></i>
        </p>
        </blockquote> 
        <p>
            <span style=';font-family:Arial'>2.&#160; Import it into the registry by double-clicking
            the .reg file&#160; (Please know that mucking with the registry is potentially dangerous
            and can make your system unstable).</span>
        </p>
        <p>
            <span style=';font-family:Arial'>3.&#160; Boot IE</span>
        </p>
        <p>
            <span style=';font-family:Arial'>4.&#160; Go to IE's Tools / Options...&#160; Programs
            tab</span>
        </p>
        <p>
            <span style=';font-family:Arial'>5.&#160; Choose &ldquo;Outlook Web Access&rdquo;
            from the E-mail dropdown.</span>
        </p>
        <p>
            <span style=';font-family:Arial'>6.&#160; Hit OK.</span>
        </p>
        <p>
            <span style=';font-family:Arial'>Now when you hit the &ldquo;Mail&rdquo; button on
            your MS keyboard you get OWA coming up automatically.&#160; You can also add OWA to
            the Start Menu now, just right+click on it and choose Properties, then click the Customize
            start menu and choose &ldquo;Outlook Web Access&rdquo;&#160;from the E-mail dropdown.</span>
        </p>
        <p>
            &#160;
        </p>
        <p class="MsoNormal">
            <img width="1" height="1" id="_x0000_i1025" src="http://weblogs.asp.net/tmeston/aggbug/48837.aspx" />
            <br />
            [<a href="http://weblogs.asp.net/tmeston/archive/2004/01/08/48837.aspx">Weblogs @
            ASP.NET</a>]
        </p>
        </blockquote>
    </div>
</body>