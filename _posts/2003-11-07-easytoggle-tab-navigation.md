---
id: 478
title: EasyToggle (Tab Navigation)
date: 2003-11-07T14:17:32+00:00


guid: /post/2003/11/EasyToggle-(Tab-Navigation).aspx
permalink: /2003/11/easytoggle-tab-navigation/
dsq_thread_id:
  - "78637139"
categories:
  - CSS
---
<body xmlns="http://www.w3.org/1999/xhtml">
    <div class="Section1">
        <p>
            Simon Willison has created an easy way to enable tabs in web pages. There is no javascript
            coding involved. Just include the .js file and add the class to your links.
        </p>
        <blockquote style='margin-top:5.0pt;margin-bottom:5.0pt'> 
        <p>
            I've been working on a new inobtrusive <acronym>DHTML</acronym> effect: <a href="http://simon.incutio.com/code/js/easytoggle/example.html" title="easytoggle demo page">easytoggle</a>,
            which is an inobtrusive implementation of the common effect where links or tabs can
            be clicked to reveal part of a page while hiding the other parts. It's similar in
            some ways to the <a href="http://simon.incutio.com/archive/2003/08/12/multiPartForms" title="http://simon.incutio.com/archive/2003/08/12/multiPartForms">Multi
            part forms with Javascript</a> technique.
        </p>
        <p>
            The idea is pretty simple - all you need are a bunch of links and a bunch of elements
            that should be toggled by those links. When adding special behaviour to links it is
            always a good idea to ensure that they still link to something sensible, so that in
            user agents without Javascript support they still do something useful. In this case,
            it makes sense for them to act as anchor links that point to the elements with which
            they are associated. With easytoggle, all you need to do is define the links, point
            them at an element with an ID and assign them the class 'toggle'. The script does
            the rest of the work. For example, for a simple set with only two panels the markup
            would look something like this:
        </p>
        <pre>
<code>&lt;ul&gt;</code> </pre>
        <pre>
<code>&lt;li&gt;&lt;a href="#p1" class="toggle"&gt;Panel 1&lt;/a&gt;&lt;/li&gt;</code> </pre>
        <pre>
<code>&lt;li&gt;&lt;a href="#p2" class="toggle"&gt;Panel 2&lt;/a&gt;&lt;/li&gt;</code> </pre>
        <pre>
<code>&lt;/ul&gt;</code> </pre>
        <pre>
<code>&lt;p id="p1"&gt;This is panel 1&lt;/p&gt;</code> </pre>
        <pre>
<code>&lt;p id="p2"&gt;This is panel 2&lt;/p&gt;</code> </pre>
        <p>
            That's all it takes - the <a href="http://simon.incutio.com/code/js/easytoggle/example.html" title="easytoggle demo page">demo</a> has
            a very slightly more complicated example.
        </p>
        <p>
            I thought it was finished, until I tested it in Apple's Safari browser. In Safari,
            the worst possible thing happens. The initialisation code which hides all of the panels
            after the first one works fine. Unfortunately, the code that causes the links to change
            which panel is visible fails silently, leaving only the first panel accessible to
            users with that browser. That's a big problem.
        </p>
        <p>
            It was at this point that I discovered that Safari's support for debugging Javascript <em><i>sucks
            rocks</i></em>. Firstly, the browser gives no indication that a bug has been encountered.
            I'm sure this is a deliberate usability decision, but it also means users who encounter
            a bug won't even know that there is a problem with the site. A quick Google led me
            to <a href="http://www.macosxhints.com/article.php?story=20030906093300383" title="Safari and Javascript debugging">this
            page</a>, which told me how to enable Javascript error reporting:
        </p>
        <ol start="1" type="1">
            <li class="MsoNormal" style='mso-margin-top-alt:auto;mso-margin-bottom-alt:auto; mso-list:l0 level1 lfo1'>
                <span style=''>In a command line shell, execute</span> <code>defaults write com.apple.Safari
                IncludeDebugMenu 1</code> (apparently <a href="http://www.lordofthecows.com/safari_enhancer.php" title="http://www.lordofthecows.com/safari_enhancer.php">Safari
                Enhancer</a> lets you do this from a <acronym>GUI</acronym>).</li>
            <li class="MsoNormal" style='mso-margin-top-alt:auto;mso-margin-bottom-alt:auto; mso-list:l0 level1 lfo1'>
                <span style=''>Reload Safari and check the "Log Javascript Exceptions" option in the
                newly enabled Debug menu.</span>
            </li>
            <li class="MsoNormal" style='mso-margin-top-alt:auto;mso-margin-bottom-alt:auto; mso-list:l0 level1 lfo1'>
                <span style=''>Start Console.app, which lives in</span> 
                <samp>
                    /Application/Utilities</samp>. Note that this is <em><i>not the same thing</i></em> as
                the command line console. This took me a few moments to figure out. Macs remain a
                strange new realm of discovery.</li>
            <li class="MsoNormal" style='mso-margin-top-alt:auto;mso-margin-bottom-alt:auto; mso-list:l0 level1 lfo1'>
                <span style=''>Javascript exceptions will now appear in the Console.app window.</span>
            </li>
        </ol>
        <p>
            Excellent - just what I needed to know. The entire error message I got when I clicked
            a link? <code><span style=''>(event handler):Undefined value</span></code>. Gee, thanks
            a lot Safari. If anyone has any ideas how I can fix the script in Safari (or at the
            very least prevent it from being unusable) please leave me a note.
        </p>
        <p>
            <strong><b>Update:</b></strong> Thanks to <a href="http://simon.incutio.com/archive/2003/11/06/easytoggle#comment1">a
            tip</a> from David Lindquist, <a href="http://simon.incutio.com/code/js/easytoggle/example2.html" title="easytoggle demo page (updated version)">the
            updated version of the script</a> now works in Safari. It's a little bit uglier though.
        </p>
        <p class="MsoNormal">
            <br />
            [<a href="http://simon.incutio.com/archive/2003/11/06/easytoggle">Simon Willison's
            Weblog</a>]
        </p>
        </blockquote>
    </div>
</body>