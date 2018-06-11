---
id: 421
title: Minimize Outlook to notification area
date: 2004-01-09T00:10:18+00:00
author: Merill Fernando
layout: post
guid: /post/2004/01/Minimize-Outlook-to-notification-area.aspx
permalink: /2004/01/minimize-outlook-to-notification-area/
dsq_thread_id:
  - "79391061"
categories:
  - Tips
---
<body xmlns="http://www.w3.org/1999/xhtml">
    <div class="Section1">
        <blockquote style='margin-top:5.0pt;margin-bottom:5.0pt'> 
        <p class="answer" style='mso-margin-top-alt:6.0pt;margin-right:0in;margin-bottom: 6.0pt;margin-left:0in'>
            <span style=''>Outlook 2003 has an option that allows it's <strong><b>window to be
            minimized to the system notification area</b></strong>, near the clock.&#160; You
            can also have Outlook 2002 do the same thing, with some registry hacking.</span>
        </p>
        <p class="answer" style='mso-margin-top-alt:6.0pt;margin-right:0in;margin-bottom: 6.0pt;margin-left:0in'>
            <span style=''>For OL2003, the option can be found by right-clicking the Outlook icon
            in the notification area.&#160; Choose the &ldquo;Hide when minimized&ldquo; option
            on the menu.</span>
        </p>
        <p class="answer" style='mso-margin-top-alt:6.0pt;margin-right:0in;margin-bottom: 6.0pt;margin-left:0in'>
            <span style=''>For OL2002, there is no user interface available to turn on the option.&#160;
            By modifying the registry, you can control the behavor.</span>
        </p>
        <p class="answer" style='mso-margin-top-alt:6.0pt;margin-right:0in;margin-bottom: 6.0pt;margin-left:0in'>
            <span style=''>The registry path is:</span>
        </p>
        <blockquote style='margin-top:5.0pt;margin-right:0in;margin-bottom:5.0pt'> 
        <p class="answer" style='mso-margin-top-alt:6.0pt;margin-right:0in;margin-bottom: 6.0pt;margin-left:0in'>
            <font color="red"><span style=';font-family:"Courier New";color:red'>HKEY_CURRENT_USER\Software\Microsoft\Office\10.0\Outlook\Preferences</span></font>
        </p>
        </blockquote> 
        <p class="answer" style='mso-margin-top-alt:6.0pt;margin-right:0in;margin-bottom: 6.0pt;margin-left:0in'>
            <span style=''>The registry key is called &ldquo;MinToTray&ldquo; and is a DWORD value.&#160;
            If the key doesn't exist, use RegEdit to create it.&#160; When set to a non-zero value,
            typically 1, the feature is turned on.&#160; Setting it to zero turns the feature
            off.</span>
        </p>
        <p class="answer" style='mso-margin-top-alt:6.0pt;margin-right:0in;margin-bottom: 6.0pt;margin-left:0in'>
            <span style=''>If you have Windows XP or later, copy the following command and paste
            it into Run dialog:</span>
        </p>
        <blockquote style='margin-top:5.0pt;margin-right:0in;margin-bottom:5.0pt'> 
        <p class="answer" style='mso-margin-top-alt:6.0pt;margin-right:0in;margin-bottom: 6.0pt;margin-left:0in'>
            <font color="red"><span style=';font-family:"Courier New";color:red'>reg add HKCU\Software\Microsoft\Office\10.0\Outlook\Preferences
            /v MinToTray /t REG_DWORD /d 0x01</span></font>
        </p>
        </blockquote> 
        <p class="answer" style='mso-margin-top-alt:6.0pt;margin-right:0in;margin-bottom: 6.0pt;margin-left:0in'>
            <span style=''>The REG.EXE program is included with Windows XP, and I believe was
            available for earlier versions as part of the Resource Kit.&#160; It's a very handy
            program.</span>
        </p>
        <p class="answer" style='mso-margin-top-alt:6.0pt;margin-right:0in;margin-bottom: 6.0pt;margin-left:0in'>
            <span style=''>After making the change, you'll need to restart Outlook 2002 for it
            to take effect.</span>
        </p>
        <p class="answer" style='mso-margin-top-alt:6.0pt;margin-right:0in;margin-bottom: 6.0pt;margin-left:0in'>
            <strong><b><font color="purple"><span style=';color:purple'>FYI</span></font></b></strong>,
            in case you're wondering, OL2003 uses the same key name for it's option, so you can
            use the registry to turn it on or off as well.&#160; However, change the registry
            path to reflect &ldquo;11.0&rdquo; instead of &ldquo;10.0&rdquo;.
        </p>
        <p class="answer" style='mso-margin-top-alt:6.0pt;margin-right:0in;margin-bottom: 6.0pt;margin-left:0in'>
            <span style=''>Can anyone try this on OL2000 and let me know if it works there as
            well?&#160; The path for that would be &ldquo;9.0&rdquo;.&#160; Thus:</span>
        </p>
        <p class="answer" style='mso-margin-top-alt:6.0pt;margin-right:0in;margin-bottom: 6.0pt;margin-left:0in'>
            <span style=''>Outlook 2000 (unverified):</span>
        </p>
        <p class="answer" style='mso-margin-top-alt:6.0pt;margin-right:0in;margin-bottom: 6.0pt;margin-left:0in'>
            <font color="red"><span style=';font-family:"Courier New";color:red'>reg add HKCU\Software\Microsoft\Office\9.0\Outlook\Preferences
            /v MinToTray /t REG_DWORD /d 0x01</span></font>
        </p>
        <p class="answer" style='mso-margin-top-alt:6.0pt;margin-right:0in;margin-bottom: 6.0pt;margin-left:0in'>
            <span style=''>Outlook 2002:</span>
        </p>
        <p class="answer" style='mso-margin-top-alt:6.0pt;margin-right:0in;margin-bottom: 6.0pt;margin-left:0in'>
            <font color="red"><span style=';font-family:"Courier New";color:red'>reg add HKCU\Software\Microsoft\Office\10.0\Outlook\Preferences
            /v MinToTray /t REG_DWORD /d 0x01</span></font>
        </p>
        <p class="answer" style='mso-margin-top-alt:6.0pt;margin-right:0in;margin-bottom: 6.0pt;margin-left:0in'>
            <span style=''>Outlook 2003:</span>
        </p>
        <p class="answer" style='mso-margin-top-alt:6.0pt;margin-right:0in;margin-bottom: 6.0pt;margin-left:0in'>
            <font color="red"><span style=';font-family:"Courier New";color:red'>reg add HKCU\Software\Microsoft\Office\11.0\Outlook\Preferences
            /v MinToTray /t REG_DWORD /d 0x01</span></font>
        </p>
        <p class="MsoNormal">
            <img width="1" height="1" id="_x0000_i1025" src="http://weblogs.asp.net/ChuckOp/aggbug/48416.aspx" />
            <br />
            [<a href="http://weblogs.asp.net/ChuckOp/archive/2004/01/07/48416.aspx">Weblogs @
            ASP.NET</a>]
        </p>
        </blockquote>
    </div>
</body>