---
id: 453
title: Javascript Trick
date: 2003-12-12T01:00:19+00:00


guid: /post/2003/12/Javascript-Trick.aspx
permalink: /2003/12/javascript-trick/
dsq_thread_id:
  - "79127701"
categories:
  - HTML
---
<body xmlns="http://www.w3.org/1999/xhtml">
    <div class="Section1">
        <p>
            Did you know that you can execute javascript statements against a web page, just like
            using the Immediate window in Visual Basic 6? I just learnt this today.
        </p>
        <p>
            Browse to a web page that has a disabled textbox and type this (replace the form and
            textbox names) in the address bar and hit enter.
        </p>
        <p>
            <font color="black"><span style='; font-family:"Courier New";color:black'>javascript:void(document.Form1.txtBox1.disabled
            = false)</span></font>
        </p>
        <p>
            Presto you have an enabled textbox! Think of all the fun you can have on web sites
            that only have client side validation?
        </p>
    </div>
</body>