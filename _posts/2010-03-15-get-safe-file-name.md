---
id: 631
title: Get Safe File Name
date: 2010-03-15T07:20:49+00:00


guid: http://merill.net/2010/03/get-safe-file-name/
permalink: /2010/03/get-safe-file-name/
dsq_thread_id:
  - "77712940"
categories:
  - Tips
tags:
  - code;
---
<p>Here’s a quick utility that might come in handy. More than once I’ve seen code where the invalid chars were hard coded. The <a href="http://msdn.microsoft.com/en-us/library/system.io.path.getinvalidfilenamechars.aspx">Path.GetInvalidFilenameChars</a> has been in the .NET Framework since 2.0.</p>  <p>The thing is you would expect something like this to be in the framework itself.</p>  <pre class="csharpcode">        <span class="rem">/// &lt;summary&gt;</span>
        <span class="rem">/// Removes invalid characters from the string that is passed in.</span>
        <span class="rem">/// &lt;/summary&gt;</span>
        <span class="rem">/// &lt;param name=&quot;name&quot;&gt;The name of the file.&lt;/param&gt;</span>
        <span class="rem">/// &lt;returns&gt;The safe name with invalid chars removed.&lt;/returns&gt;</span>
        <span class="kwrd">public</span> <span class="kwrd">static</span> <span class="kwrd">string</span> GetSafeFileName(<span class="kwrd">string</span> name)
        {
            var safeName = <span class="kwrd">new</span> StringBuilder();
            <span class="kwrd">foreach</span> (var c <span class="kwrd">in</span> name)
            {
                <span class="kwrd">if</span> ((from p <span class="kwrd">in</span> Path.GetInvalidFileNameChars() <span class="kwrd">where</span> p == c select p).Count() == 0)
                {
                    safeName.Append(c);
                }
            }
            <span class="kwrd">return</span> safeName.ToString();
        }</pre>
<style type="text/css">

.csharpcode, .csharpcode pre
{
	font-size: small;
	color: black;
	font-family: consolas, "Courier New", courier, monospace;
	background-color: #ffffff;
	/*white-space: pre;*/
}
.csharpcode pre { margin: 0em; }
.csharpcode .rem { color: #008000; }
.csharpcode .kwrd { color: #0000ff; }
.csharpcode .str { color: #006080; }
.csharpcode .op { color: #0000c0; }
.csharpcode .preproc { color: #cc6633; }
.csharpcode .asp { background-color: #ffff00; }
.csharpcode .html { color: #800000; }
.csharpcode .attr { color: #ff0000; }
.csharpcode .alt 
{
	background-color: #f4f4f4;
	width: 100%;
	margin: 0em;
}
.csharpcode .lnum { color: #606060; }</style>

<p>Chris Martin posted an even tighter version of this code in the comments below. Thanks Chris.</p>

<pre class="csharpcode">var invalid = Path.GetInvalidFileNameChars();

<span class="kwrd">return</span> <span class="kwrd">new</span> <span class="kwrd">string</span>((from p <span class="kwrd">in</span> name 
        <span class="kwrd">where</span> !invalid.Contains(p) select p).ToArray());</pre>
<style type="text/css">
.csharpcode, .csharpcode pre
{
	font-size: small;
	color: black;
	font-family: consolas, "Courier New", courier, monospace;
	background-color: #ffffff;
	/*white-space: pre;*/
}
.csharpcode pre { margin: 0em; }
.csharpcode .rem { color: #008000; }
.csharpcode .kwrd { color: #0000ff; }
.csharpcode .str { color: #006080; }
.csharpcode .op { color: #0000c0; }
.csharpcode .preproc { color: #cc6633; }
.csharpcode .asp { background-color: #ffff00; }
.csharpcode .html { color: #800000; }
.csharpcode .attr { color: #ff0000; }
.csharpcode .alt 
{
	background-color: #f4f4f4;
	width: 100%;
	margin: 0em;
}
.csharpcode .lnum { color: #606060; }</style>