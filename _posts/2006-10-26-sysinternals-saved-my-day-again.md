---
id: 100
title: Sysinternals saved my day. Again!
date: 2006-10-26T10:20:18+00:00


guid: /post/2006/10/Sysinternals-saved-my-day-Again!.aspx
permalink: /2006/10/sysinternals-saved-my-day-again/
dsq_thread_id:
  - "78584991"
categories:
  - Utilities
---
<p>So I got into office early today and was greeted with this error when I fired out Outlook: <em>Cannot start Microsoft Office Outlook. Cannot open the Outlook window. The set of folders cannot be opened. The file D:\Merill\Mail\Personal Folders.pst cannot be opened.</em></p>
<p>The only promising link from searching (hmm.. I wanted to write googled, but since I used Live Search what should I say &lsquo;lived&rsquo;) around on the internet was <a href="http://www.techspot.com/vb/all/windows/t-20367-Cannot-open-Outlook.html">this</a>. But trying to start up in safe mode didn&rsquo;t work.</p>
<p>I then fired up <a href="http://www.sysinternals.com/Utilities/Filemon.html">FileMon</a>, made a filter to show only &lsquo;outlook&rsquo; and then&nbsp;ran Outlook as expected the error occured again. I then went into FileMon to figure out what exactly was happening and there it was an Open request to D:\Merill\Mail\~Personal Folders.pst was returning a &lsquo;Sharing Violation&rsquo;.</p>
<p>Now having to figure out which process was holding on to this file I started up <a href="http://www.sysinternals.com/Utilities/ProcessExplorer.html">Process Explorer</a> and did a search for the processes holding a handle to &lsquo;personal folders&rsquo; and there it was, a rogue Outlook.exe (must have crashed earlier). So I killed of the outlook.exe process and got my Outlook running back again.</p>
<p>So what does this all prove. If you have any problems with files not being accessible first try restarting Windows.</p>