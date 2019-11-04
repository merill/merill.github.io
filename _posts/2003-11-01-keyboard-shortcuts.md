---
id: 483
title: Keyboard Shortcuts
date: 2003-11-01T16:25:15+00:00
author: Merill Fernando

guid: /post/2003/11/Keyboard-Shortcuts.aspx
permalink: /2003/11/keyboard-shortcuts/
dsq_thread_id:
  - "79915615"
categories:
  - Tips
---
<body xmlns="http://www.w3.org/1999/xhtml">
    <p>
        Are you a keyboard freak like me? Then you've got to know how to add shortcuts to
        your frequently used programs so that you can launch them from the keyboard.
    </p>
    <p>
        If you want to be a keyboard freak know the default shortcuts that come with the programs,
        the ones that I use most are given below. To try this press WinKey + R and then type
        in any of the following shortcuts and press enter. Presto, see ma no mouse!
    </p>
    <ul>
        <li>
            cmd - Command Window</li>
        <li>
            explorer - Windows Explorer</li>
        <li>
            iexplore - Internet Explorer</li>
        <li>
            notepad - Notepad</li>
        <li>
            winword - Word</li>
        <li>
            outlook - Outlook</li>
        <li>
            excel - Excel</li>
        <li>
            devenv - Visual Studio</li>
        <li>
            inetmgr - IIS</li>
        <li>
            iisreset - Restart IIS</li>
        <li>
            isqlw - SQL Query Analyser</li>
        <li>
            services.msc - Windows Services</li>
        <li>
            calc - Calculator</li>
        <li>
            compmgmt.msc - Computer Manager</li>
    </ul>
    <p>
        To add your own shortcuts to other programs that you use most often there are two
        ways. I like the more elegant second method which uses the.
    </p>
    <p>
        Shorten shortcuts: Instead of typing paths in the Run box or Address bar, create shortcuts
        in the folders Windows looks in by default. In Windows 9x and Me, try the Windows\Command
        folder. In Windows 2000 and XP, put the shortcuts in the Windows\System folder (not
        Windows\System32), since the System folder is relatively uncrowded. 
    </p>
    <p>
        To create the shortcuts, open Explorer and select the applications, folders, and files
        you use most often. Right-click and drag them to one of the aforementioned Windows
        folders, release the mouse button, and choose Create Shortcut(s) Here. (You can also
        create shortcuts to Web pages this way.) Give each a short name so you can launch
        it with little typing; you could name your word-processor shortcut wp, for example.
        Don't use the name of an existing folder, since doing so could confuse the Address
        bar or the Run box.
    </p>
    <p>
        When using this tip with the Address bar, include .lnk (the hidden extension for shortcuts)
        when you type the name of a non-Web shortcut--wp.lnk, say. And in both the Run box
        and the Address bar, add .url when launching Web shortcuts--for example, pcw.url.
        If you store batch files in one of these folders, omit the .bat extension when entering
        file names.
    </p>
    <p>
        Bypass paths: To cut down on typing even more, choose Start, Run, type regedit, and
        press Enter. Select this folder in the left pane: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\App
        Paths. Right-click App Paths in the right pane and choose New, Key. Type the shorthand
        name in the Address bar followed by .exe--regardless of whether you plan to launch
        an application or a file. For instance, type r.exe to launch a report file in a desktop
        publishing app. Press Enter to complete the naming. 
    </p>
    <p>
        Select your new shorthand key in the left pane and double-click (Default) in the right
        pane. In the 'Value data' box, type the path and name of the program, data file, or
        shortcut you want to launch. (Add .lnk to the name of shortcut paths, and .url to
        the end of Web shortcuts.) For example, type c:\My Documents\Quarterly Report.indd
        (see FIGURE 4). Click OK and exit the Registry Editor. Now when you enter your shorthand
        text (minus the .exe) in the Address bar or the Run box--such as r, to continue the
        example above--Windows will open the specified file.
    </p>
</body>