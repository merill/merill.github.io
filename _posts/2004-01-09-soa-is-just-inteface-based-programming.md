---
id: 418
title: SOA is Just Inteface Based Programming?
date: 2004-01-09T00:17:30+00:00
author: Merill Fernando
layout: post
guid: /post/2004/01/SOA-is-Just-Inteface-Based-Programming.aspx
permalink: /2004/01/soa-is-just-inteface-based-programming/
dsq_thread_id:
  - "78834078"
categories:
  - .NET
---
<body xmlns="http://www.w3.org/1999/xhtml">
    <div class="Section1">
        <blockquote style='margin-top:5.0pt;margin-bottom:5.0pt'> 
        <p>
            Steve Eichert&#160;suggests that&#160;<a href="http://dotnetjunkies.com/WebLog/seichert/posts/5268.aspx#comment" title="http://dotnetjunkies.com/WebLog/seichert/posts/5268.aspx#comment">SOA
            is&#160;just hyped up interface based programming</a>:
        </p>
        <blockquote style='margin-top:5.0pt;margin-right:0in;margin-bottom:5.0pt'> 
        <p>
            &ldquo;In OO systems we often declare interfaces that define the behavior of our objects.&#160;
            These interfaces allow us to plug in new&#160;implementations quickly and easily.&#160;&#160;By&#160;coupling
            our objects to&#160;interface contracts&#160;rather then concrete objects, we&#160;reduce
            the coupling between our objects.&#160;Is this different then SOA?&#160; Do Xml web
            services make SOA&#160;better or more interesting then normal old interface based
            programming in an OO world?&ldquo;[1]
        </p>
        </blockquote> 
        <p>
            While it may be safe to say that SOA is interfaced based (or contract based) programming,
            saying that it is nothing more is a huge generalization, especially if you are talking
            about SOA driven by web services. A few differences:
        </p>
        <ul type="disc">
            <li class="MsoNormal" style='mso-margin-top-alt:auto;mso-margin-bottom-alt:auto; mso-list:l0 level1 lfo1'>
                <span style=''>Interface programming doesn't play nearly as well AOP as SOA (especially
                web service based SOA).</span>
            </li>
            <li class="MsoNormal" style='mso-margin-top-alt:auto;mso-margin-bottom-alt:auto; mso-list:l0 level1 lfo1'>
                <span style=''>Use of interfaces generally doesn't give you cross-platform support.</span>
            </li>
            <li class="MsoNormal" style='mso-margin-top-alt:auto;mso-margin-bottom-alt:auto; mso-list:l0 level1 lfo1'>
                <span style=''>Use of interfaces says nothing about remote procedures.</span>
            </li>
            <li class="MsoNormal" style='mso-margin-top-alt:auto;mso-margin-bottom-alt:auto; mso-list:l0 level1 lfo1'>
                <span style=''>SOA is message based (HUGE difference). Web Services are not RMI, you
                aren't dealing with objects, you are dealing with messages (hell, SOAP's acronym&#160;status
                has been officially revoked, probably to do away with that very idea).</span>
            </li>
            <li class="MsoNormal" style='mso-margin-top-alt:auto;mso-margin-bottom-alt:auto; mso-list:l0 level1 lfo1'>
                <span style=''>The &ldquo;plug-and-play&ldquo; aspects of web services are a non-factor
                in most of today's SOA implementations. People today are worried far more about providing
                accessable behavior than swappable behavior. There are definately some very cool applications
                that for swappable services, but this type of thing is out on the fringe (stuff like
                WS-Transaction implementations fall into this category).</span>
            </li>
        </ul>
        <p>
            I'm sure there are plenty more reasons why SOA isn't just interfaced based programming,
            but the bottom line is that SOA provides for a ton of scenarios that interfaced based
            programming doesn't even begin to address. If interface programming alone was good
            enough, we wouldn't need SOA.
        </p>
        <p>
            <span lang="NL-BE" style=''>[1] Steve Eichert.</span> <a href="http://dotnetjunkies.com/WebLog/seichert/posts/5268.aspx#comment" title="http://dotnetjunkies.com/WebLog/seichert/posts/5268.aspx#comment"><span lang="NL-BE">http://dotnetjunkies.com/WebLog/seichert/posts/5268.aspx#comment</span></a>
        </p>
        <p class="MsoNormal">
            <img border="0" width="1" height="1" id="_x0000_i1025" src="http://weblogs.asp.net/jezell/aggbug/48169.aspx" />
            <br />
            [<a href="http://weblogs.asp.net/jezell/archive/2004/01/07/48169.aspx">Weblogs @ ASP.NET</a>]
        </p>
        </blockquote>
    </div>
</body>