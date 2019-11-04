---
id: 477
title: Sortable Table
date: 2003-11-07T14:22:20+00:00


guid: /post/2003/11/Sortable-Table.aspx
permalink: /2003/11/sortable-table/
dsq_thread_id:
  - "78098491"
categories:
  - CSS
---
<body xmlns="http://www.w3.org/1999/xhtml">
    <div class="Section1">
        <p>
            If you thought the Tab navigation was good, check out the Sort-able grid script. By
            simply setting a class on any table you can make the headers sortable. The script
            takes care of numbers, dates and text automatically.
        </p>
        <blockquote style='margin-top:5.0pt;margin-bottom:5.0pt'> 
        <p>
            Stuart Langridge has released a couple of <em><i>very</i></em> neat new Javascript
            experiments. <a href="http://www.kryogenix.org/code/browser/sorttable/" title="Sortable Tables">sorttable</a> makes
            any data table on a page "sortable" by clicking the table headers. I've seen this
            effect <a href="http://msdn.microsoft.com/library/en-us/dndude/html/dude07232001.asp" title="Fun with Tables">used</a> to
            demonstrate Microsoft's proprietary "behaviors" technology but Stuart's solution has
            the advantage of being standards compliant and working across different browsers.
            Best of all, it follows the principles of inobtrusive <acronym>DHTML</acronym> and
            hooks in to the markup using only a class attribute.
        </p>
        <p>
            Stuart's second experiment, <a href="http://www.kryogenix.org/code/browser/jses/">JavaScript
            Event Sheets</a>, is even more interesting. It tackles the problem of attaching events
            to page elements. The most common way of doing this is with inline attributes, but
            these require adding behavioural (rather than structural) code to your markup and
            can lead to additional maintenance costs further down the road. A better alternative
            is to use the <acronym>DOM</acronym> to dynamically add events, which works fine but
            means tightly coupling the structure of the document to the Javascript that sets up
            the events. Stuart's solution is to abstract the logic that attaches events to elements
            out to a separate file, called a Javascript Event Sheet. This uses <acronym>CSS</acronym> style
            syntax (partially handled by my <a href="http://simon.incutio.com/archive/2003/03/25/getElementsBySelector">getElementsBySelector
            function</a>) to specify how events attached to different elements should be handled.
            Stuart demonstrates the idea with a common image rollover:
        </p>
        <pre>
<code>img.rollover {</code> </pre>
        <pre>
<code> mouseover: rollover_handler;</code> </pre>
        <pre>
<code> mouseout: rollout_handler;</code> </pre>
        <pre>
<code>}</code> </pre>
        <p>
            Stuart's blog entries concerning the two new experiments are <a href="http://www.kryogenix.org/days/565.html" title="Sortable tables">here</a> and <a href="http://www.kryogenix.org/days/566.html" title="http://www.kryogenix.org/days/566.html">JavaScript
            Event Sheets</a>.
        </p>
        <p class="MsoNormal">
            <br />
            [<a href="http://simon.incutio.com/archive/2003/11/05/mojo">Simon Willison's Weblog</a>]
        </p>
        </blockquote>
    </div>
</body>