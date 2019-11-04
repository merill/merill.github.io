---
id: 337
title: A Quick Look At the Win2K Stolen Source
date: 2004-02-20T13:19:53+00:00


guid: /post/2004/02/A-Quick-Look-At-the-Win2K-Stolen-Source.aspx
permalink: /2004/02/a-quick-look-at-the-win2k-stolen-source/
dsq_thread_id:
  - "77807004"
categories:
  - News
---
<body xmlns="http://www.w3.org/1999/xhtml">
    <div class="Section1">
        <p class="MsoNormal">
            From the various articles that I read, the warning was not to go near any of the stolen
            source due to its IP. This <a href="http://www.kuro5hin.org/story/2004/2/15/71552/7795">article</a> on <a href="http://www.kuro5hin.org/">Kuro5hin</a> has
            a review of some of the files in the code.
        </p>
        <p class="MsoNormal">
            A quick, superficial look at the style and content of the leaked Windows 2000 source.
            I quote from the comments but not the code, so this should be safe for developers
            to read.
        </p>
        <p class="MsoNormal">
            <b><span style=';font-weight:bold'>Overview</span></b>
        </p>
        <p class="MsoNormal">
            Several days ago, two files containing Microsoft source code began circulating on
            the Internet. One contains a majority of the NT4 source code: this is not discussed
            here. The other contains a fraction of the Windows 2000 source code, reportedly about
            15% of the total. This includes some networking code including winsock and inet; as
            well as some shell code. Some other familiar items include the event log, and some
            of the default screensavers.
        </p>
        <p class="MsoNormal">
            The timestamps on the files generally say 25 July 2000. The source is contained in
            a Zip file of size 213,748,207 bytes, named windows_2000_source_code.zip, which has
            been widely circulated on P2P networks. Some dummy files of similar size, containing
            just strings of zeroes, have also circulated.
        </p>
        <p class="MsoNormal">
            There has been some speculation that while the bulk of the source is genuine, some
            of the comments have been tampered with to embarrass Microsoft. This is difficult
            to disprove, but I find it implausible. The embarrassing comments occur on thousands
            of lines, in realistic places. Furthermore, if someone had done that, it would have
            been easy to make the comments far more incriminating.
        </p>
        <p class="MsoNormal">
            &#160;
        </p>
        <p class="MsoNormal">
            <b><span style=';font-weight:bold'>Embarrassments</span></b>
        </p>
        <p class="MsoNormal">
            In the struggle to meet deadlines, I think pretty much all programmers have put in
            comments they might later regret, including swearwords and acerbic comments about
            other code or requirements. Also, any conscientious coder will put in prominent comments
            warning others about the trickier parts of the code. Comments like "UGLY TERRIBLE
            HACK" tend to indicate good code rather than bad: in bad code ugly terrible hacks
            are considered par for the course. It would therefore be both hypocritical and meaningless
            to go through the comments looking for embarrassments. But also fun, so let's go.
        </p>
        <p class="MsoNormal">
            Curse words: there are a dozen or so "fucks" and "shits", and hundreds of "craps".
            Some dissatisfaction with the compiler is expressed in private\shell\shell32\util.cpp:
        </p>
        <p class="MsoNormal">
            &#160;
        </p>
        <p class="MsoNormal">
            <span style='; font-family:"Courier New"'>// the fucking alpha cpp compiler seems
            to fuck up the goddam type "LPITEMIDLIST", so to work<br />
            // around the fucking peice of shit compiler we pass the last param as an void *instead
            of a LPITEMIDLIST</span>
        </p>
        <p class="MsoNormal">
            &#160;
        </p>
        <p class="MsoNormal">
            Some insight into Microsoft's famous daily build process is given in private\windows\media\avi\verinfo.16\verinfo.h:
        </p>
        <p class="MsoNormal">
            <span style='; font-family:"Courier New"'>&#160;*&#160;&#160;&#160;&#160;&#160;&#160;
            !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!<br />
            &#160;*&#160;&#160;&#160;&#160;&#160;&#160; !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!<br />
            &#160;* &#160;&#160;&#160;&#160;&#160;&#160;!!!!!!!IF YOU CHANGE TABS TO SPACES, YOU
            WILL BE KILLED!!!!!!!<br />
            &#160;*&#160;&#160;&#160;&#160;&#160;&#160; !!!!!!!!!!!!!!DOING SO FUCKS THE BUILD
            PROCESS!!!!!!!!!!!!!!!!<br />
            &#160;*&#160;&#160;&#160;&#160;&#160;&#160; !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!<br />
            &#160;*&#160;&#160;&#160;&#160;&#160;&#160; !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!<br />
            <br />
            </span>
        </p>
        <p class="MsoNormal">
            <b><span style=';font-weight:bold'>Quality</span></b>
        </p>
        <p class="MsoNormal">
            Despite the above, the quality of the code is generally excellent. Modules are small,
            and procedures generally fit on a single screen. The commenting is very detailed about
            intentions, but doesn't fall into "add one to i" redundancy.
        </p>
        <p class="MsoNormal">
            There is some variety in the commenting style. Sometimes blocks use a // at every
            line, sometimes the /* */ style. In some modules functions have a history, some do
            not. Some functions describe their variables in a comment block, some don't. Microsoft
            appears not to have fallen into the trap of enforcing over-rigid standards or universal
            use of over-complicated automatic tools. They seem to trust their developers to comment
            well, and they do.
        </p>
        <p class="MsoNormal">
            However, not everything is so rosy. Some of the modules are clearly suffering from
            the hacks upon hacks mentioned earlier. As someone who struggled immensely trying
            to get the MSInet control working not long after this code was released, it's a relief
            to see that the inet code is as bad as I thought.
        </p>
        <p class="MsoNormal">
            From the comments, it also appears that most of the uglier hacks are due to compatibility
            issues: either backward-compatibility, hardware compatibility or issues caused by
            particular software. Microsoft's vast compatibility strengths have clearly come at
            a cost, both in developer-sweat and the elegance (and hence stability and maintainability)
            of the code.
        </p>
        <p class="MsoNormal">
            &#160;
        </p>
        <p class="MsoNormal">
            <b><span style=';font-weight:bold'>Open Source</span></b>
        </p>
        <p class="MsoNormal">
            It's been widely rumored for a while that Microsoft relies on stolen open source code.
            The rumor has faced widespread skepticism too. Microsoft has hundreds of millions
            of lines of code, most of it highly specialized. Hardly any of that could benefit
            from stealing: it hardly seems worth the legal risk. It's true that early versions
            of the TCP-IP stack were (legally) taken from BSD: but that was a long time ago, when
            Microsoft was much smaller.
        </p>
        <p class="MsoNormal">
            Searching the code for "linux" and "GPL" finds no references. "BSD" finds only a couple
            of references to BSD-convention strings. "GNU" finds a lot of references to a GNUmakefile
            in private\genx\shell, which in turn mentions a "mode for Emacs." This is apparently
            legitimate: simply using a makefile does not apply the makefile's copyright to the
            resulting code.
        </p>
        <p class="MsoNormal">
            Therefore, a superficial look at the code finds no evidence that Microsoft has violated
            the GPL or stolen other open source code. Closer examination might turn something
            up.
        </p>
        <p class="MsoNormal">
            &#160;
        </p>
        <p class="MsoNormal">
            <b><span style=';font-weight:bold'>Favoritism</span></b>
        </p>
        <p class="MsoNormal">
            It's noticeable that a lot of the "hacks" refer to individual applications. In some
            cases they are non-Microsoft, such as this case: a Borland compiler came to depend
            on an existing bug, so their fix worked to preserve some of the bug's behaviour. But
            just as often these application-specific fixes are for Microsoft's own apps. There
            seems to be an informal hierarchy when it comes these: Microsoft apps take precedence,
            then major software companies like IBM and Borland.
        </p>
        <p class="MsoNormal">
            &#160;
        </p>
        <p class="MsoNormal">
            It's also interesting to finally see references to the notorious undocumented features,
            which Microsoft application developers have long been known to use.
        </p>
        <p class="MsoNormal">
            &#160;
        </p>
        <p class="MsoNormal">
            private\mvdm\wow32\wcntl32.c:
        </p>
        <p class="MsoNormal">
            <span style='; font-family:"Courier New"'>// These undocumented messages are used
            by Excel 5.0</span>
        </p>
        <p class="MsoNormal">
            private\mvdm\wow32\wgdi31.c:
        </p>
        <p class="MsoNormal">
            <span style='; font-family:"Courier New"'>// InquireVisRgn is an undocumented Win
            3.1 API. This code has been</span>
        </p>
        <p class="MsoNormal">
            <span style='; font-family:"Courier New"'>// suggested by ChuckWh. If this does not
            fix the s 2.0</span>
        </p>
        <p class="MsoNormal">
            <span style='; font-family:"Courier New"'>// problem, then ChuckWh would be providing
            us with an private entry</span>
        </p>
        <p class="MsoNormal">
            <span style='; font-family:"Courier New"'>// point.</span>
        </p>
        <p class="MsoNormal">
            &#160;
        </p>
        <p class="MsoNormal">
            private\mvdm\wow32\wgfont.c:
        </p>
        <p class="MsoNormal">
            <span style='; font-family:"Courier New"'>* This thunk implements the undocumented
            Win3.0 and Win3.1 API</span>
        </p>
        <p class="MsoNormal">
            <span style='; font-family:"Courier New"'>* GetCurLogFont (GDI.411). Symantec QA4.0
            uses it.</span>
        </p>
        <p class="MsoNormal">
            <span style='; font-family:"Courier New"'>* To implement this undocumented API we
            will use the NT undocumented API</span>
        </p>
        <p class="MsoNormal">
            &#160;
        </p>
        <p class="MsoNormal">
            In some cases, the programmers themselves appear to have been frustrated or surprised.
        </p>
        <p class="MsoNormal">
            private\ntos\w32\ntuser\kernel\mnpopup.c:
        </p>
        <p class="MsoNormal">
            <span style='; font-family:"Courier New"'>// Set the GlobalPopupMenu variable so that
            EndMenu works for popupmenus so</span>
        </p>
        <p class="MsoNormal">
            <span style='; font-family:"Courier New"'>// that WinWart II people can continue to
            abuse undocumented functions.</span>
        </p>
        <p class="MsoNormal">
            private\windows\shell\accesory\hypertrm\emu\minitel.c:
        </p>
        <p class="MsoNormal">
            <span style='; font-family:"Courier New"'>// Guess what? Latent background color is
            always adopted for mosaics.</span>
        </p>
        <p class="MsoNormal">
            <span style='; font-family:"Courier New"'>// This is a major undocumented find...</span>
        </p>
        <p class="MsoNormal">
            &#160;
        </p>
        <p class="MsoNormal">
            private\windows\shell\accesory\hypertrm\emu\minitelf.c:
        </p>
        <p class="MsoNormal">
            <span style='; font-family:"Courier New"'>// Ah, the life of the undocumented. The
            documentation says</span>
        </p>
        <p class="MsoNormal">
            <span style='; font-family:"Courier New"'>// that this guys does not validate, colors,
            act as a delimiter</span>
        </p>
        <p class="MsoNormal">
            <span style='; font-family:"Courier New"'>// and fills with spaces. Wrong. It does
            validate the color.</span>
        </p>
        <p class="MsoNormal">
            <span style='; font-family:"Courier New"'>// As such its a delimiter. If...</span>
        </p>
        <p class="MsoNormal">
            &#160;
        </p>
        <p class="MsoNormal">
            <b><span style=';font-weight:bold'>Conclusions</span></b>
        </p>
        <p class="MsoNormal">
            The security risks from this code appear to be low. Microsoft do appear to be checking
            for buffer overruns in the obvious places. The amount of networking code here is small
            enough for Microsoft to easily check for any vulnerabilities that might be revealed:
            it's the big applications that pose more of a risk. This code is also nearly four
            years old: any obvious problems should be patched by now.
        </p>
        <p class="MsoNormal">
            Microsoft's fears that this code will be pirated by its competitors also seem largely
            unfounded. With application code this would be a risk, but it's hard to see Microsoft's
            operating system competitors taking advantage of it. Neither Apple nor Linux are in
            a much of position to steal code and get away with it, even if it was useful to them.
        </p>
        <p class="MsoNormal">
            In short, there is nothing really surprising in this leak. Microsoft does not steal
            open-source code. Their older code is flaky, their modern code excellent. Their programmers
            are skilled and enthusiastic. Problems are generally due to a trade-off of current
            quality against vast hardware, software and backward compatibility.
        </p>
    </div>
</body>