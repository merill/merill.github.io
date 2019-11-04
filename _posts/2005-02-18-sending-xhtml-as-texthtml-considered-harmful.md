---
id: 242
title: Sending XHTML as text/html Considered Harmful
date: 2005-02-18T02:35:32+00:00
author: Merill Fernando

guid: /post/2005/02/Sending-XHTML-as-texthtml-Considered-Harmful.aspx
permalink: /2005/02/sending-xhtml-as-texthtml-considered-harmful/
dsq_thread_id:
  - "78497720"
categories:
  - Technology
---
<P><A href="http://ln.hixie.ch/">Ian Hickson</A> has an published an intruiging <A href="http://www.hixie.ch/advocacy/xhtml">paper</A> on the case for avoiding XHTML. </P>
<P>Here it is in a nutshell: </P>
<UL>
<LI>Browsers decide how to handle a file based on the MIME type that the server sends with it. 
<LI>HTML Web pages are identified with a MIME type of text/html. 
<LI>Pages written in XHTML that are sent with a MIME type of text/html don't benefit from any of the features of XHTML. 
<LI>To benefit from the features of XHTML, pages must be sent as application/xhtml+xml. 
<LI>The most popular Web browser (Internet Explorer 6) cannot view pages sent as application/xhtml+xml. </LI></UL>
<P>And all this time,&nbsp;I was ignorantly&nbsp;assuming that any well formed HTML page was XHTML.&nbsp;Well,&nbsp;you live and you learn.</P>
<P>UPDATE: I forgot to link to Ian Hickson's paper <A href="http://www.hixie.ch/advocacy/xhtml">http://www.hixie.ch/advocacy/xhtml</A>.</P>