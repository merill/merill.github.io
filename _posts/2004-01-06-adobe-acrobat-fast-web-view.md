---
id: 427
title: 'Adobe Acrobat &#8211; Fast Web View'
date: 2004-01-06T14:18:55+00:00
author: Merill Fernando

guid: /post/2004/01/Adobe-Acrobat---Fast-Web-View.aspx
permalink: /2004/01/adobe-acrobat-fast-web-view/
dsq_thread_id:
  - "77712956"
categories:
  - Tips
---
<body xmlns="http://www.w3.org/1999/xhtml">
    <div class="Section1">
        <p class="MsoNormal">
            Finding information on Adobe Acrobat PDF, especially version 6 related issues, is
            extremely hard to come by. We recently had two problems relating to Fast Web View
            (Byte Serving) and embedded thumbnails. Scouring the net for possible solutions turned
            up blank. Madura was finally able to get hold of a mail address of Robert McDaniels
            a System&rsquo;s Engineer at Adobe who kindly replied to our mail with some very insightful
            information. I&rsquo;m posting this here for anyone who has the same problems.
        </p>
        <p class="MsoNormal">
            &#160;
        </p>
        <p class="MsoNormal">
            Our question&rsquo;s and Robert&rsquo;s answers:
        </p>
        <p class="MsoNormal">
            <b><span style=';font-weight:bold'>Embedded Thumbnails</span></b>
        </p>
        <p class="MsoNormal">
            <i><span style=';font-style:italic'>Question:</span></i> I need to embed thumbnails
            in pdf&rsquo;s, since large pdf files (created by a third party tool I use <a href="http://www.activepdf.com/">Active
            PDF Toolkit</a>) shows blank thumbnails when viewed on Adobe Reader 6.0. Is there
            a way of doing it using a tool or using the Adobe&rsquo;s APIs?
        </p>
        <p class="MsoNormal">
            <i><span style=';font-style:italic'>Answer:</span></i>
        </p>
        <p class="MsoNormal">
            Using Adobe Acrobat 6 (Standard or Professional version) you can add thumbnail page
            previews using the options menu on the "Pages" tab. This can be automated using JavaScript
            Commands and batch processing files. For the complete Acrobat JavaScript Guide: <a href="http://partners.adobe.com/asn/acrobat/sdk/public/docs/AcroJS.pdf">http://partners.adobe.com/asn/acrobat/sdk/public/docs/AcroJS.pdf</a>.
            Just do a search for "thumbnail" and it will show you the commands you need. The user
            guide has all of the info you need on making batch processes.
        </p>
        <p class="MsoNormal">
            We also offer Adobe Document Server that can accessed via several API's and run as
            a web service to automated this process on a more Enterprise level. You could also
            replace the Active PDF toolkit with Adobe's new Adobe Acrobat Elements Server that
            will create Adobe PDFs that support byte-serving and have thumbnails embedded.
        </p>
        <p class="MsoNormal">
            &#160;
        </p>
        <p class="MsoNormal">
            <b><span style=';font-weight:bold'>Byte Serving</span></b>
        </p>
        <p class="MsoNormal">
            <i><span style=';font-style:italic'>Question:</span></i> Also the pdfs that we created
            using Active PDF Toolkit supported bytes serving in Reader 4 &amp; 5 but the same
            pdfs in Reader 6 are not byte served. Would you know of any differences that caused
            this change? We were not able to find much information relating to this issue with
            Reader 6.
        </p>
        <p class="MsoNormal">
            <i><span style=';font-style:italic'>Answer:</span></i>
        </p>
        <p class="MsoNormal">
            Adobe Reader 6 more strictly adheres to the PDF specification than previous versions
            of the Reader, as a result some non-Adobe PDF tools that got away with "shortcuts"
            in making PDFs may not produce fully compatible PDF files. This may be your issue.
        </p>
        <p class="MsoNormal">
            &#160;
        </p>
        <p class="MsoNormal">
            Open a PDF in question in Reader 6 and select FILE -&gt; DOCUMENT PROPERTIES. Select
            "Description" from the properties menu on the left, and look under the blue "PDF Information"
            heading. in the bottom right it will show if the PDF has been enabled for Fast Web
            View (aka supports byte-serving). If it says yes, then check to ensure your server
            supports byte serving. If it says no;
        </p>
        <p class="MsoNormal">
            a. Contact Active PDF for support
        </p>
        <p class="MsoNormal">
            b. Replace Active PDF with Adobe Acrobat Elements Server
        </p>
        <p class="MsoNormal">
            c. You can reprocess these files through Acrobat 6 Professional/Standard to create
            Adobe compatible PDFs - Save as PostScript and run through Distiller with Fast Web
            View turned on. This process can be automated as well using Batch processing and Distiller's
            watched folders.
        </p>
    </div>
</body>