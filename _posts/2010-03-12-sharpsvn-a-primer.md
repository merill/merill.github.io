---
id: 629
title: 'SharpSvn: A Primer'
date: 2010-03-12T10:03:14+00:00
author: Merill Fernando

guid: http://merill.net/2010/03/sharpsvn-a-primer/
permalink: /2010/03/sharpsvn-a-primer/
dsq_thread_id:
  - "77802068"
categories:
  - .NET
tags:
  - sharpsvn
  - subversion
  - tortoisesvn
---
<p>The SharpSvn library basically gives you a .NET interface to all the operations that you would normally perform through a tool like TortoiseSVN.</p>  <p>I found myself needing this exact library while writing a tool that changes files that have been checked out from SVN. </p>  <p>The problem with manipulating files that are under SVN is that you need to be careful about renaming files (and sometimes even deleting). If you don’t do it through the SVN api then you will end up with duplicates files/folders in SVN since SVN thinks that it’s a new file.</p>  <p>To solve this I finally got a chance to crack open the SharpSVN library which is used by my favourite AnkhSVN.</p>  <p>1. Download the latest library from <a href="http://sharpsvn.open.collab.net/">http://sharpsvn.open.collab.net/</a>. You have to pick between either 1.5 or 1.6. I went with 1.6 and didn’t run into any issues. I think this is based on the version of the SVN server that your connecting to.</p>  <p>2. In your Visual Studio project add a reference to the following assemblies.    <br />- SharpSvn.dll     <br />- SharpSvn.UI.dll (Only needed if you need the UI to prompt for login)</p>  <p>3. If like me your building on a 64 bit OS and you want your app to run on a 32 bit OS, make sure the project that references the SharpSvn.dll is set to Build for the x86 Platform. (Build –&gt; Configuration Manager – Solution Platform)</p>  <p>4. Write your code using the SvnClient object. Here are some samples from the SharpSvn Wiki and some that I wrote.</p>  <p><strong>CheckOut</strong></p>  <pre class="csharpcode"><span class="kwrd">public</span> <span class="kwrd">void</span> CheckOut()
{
  <span class="kwrd">using</span> (SvnClient client = <span class="kwrd">new</span> SvnClient())
  {
     client.CheckOut(
       <span class="kwrd">new</span> Uri(<span class="str">&quot;http://svn.collab.net/repos/svn/trunk/contrib&quot;</span>),
       <span class="str">@&quot;c:\wc&quot;</span>);
  } 
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

<p>Add new files to the working copy</p>

<pre class="csharpcode"><span class="kwrd">using</span>(SvnClient client = <span class="kwrd">new</span> SvnClient())
{
  SvnAddArgs args = <span class="kwrd">new</span> SvnAddArgs();
  <span class="rem">// TODO: Set optional settings on args</span>

  client.Add(<span class="str">@&quot;C:\file\in\workingcopy&quot;</span>, args);
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

<p><strong>Check if a given path is a valid SVN working copy</strong></p>

<pre class="csharpcode"><span class="kwrd">public</span> <span class="kwrd">static</span> <span class="kwrd">bool</span> IsWorkingCopy(<span class="kwrd">string</span> path)
{
    <span class="kwrd">using</span> (var client = GetSvnClient())
    {
        var uri = client.GetUriFromWorkingCopy(path);

        <span class="kwrd">return</span> uri != <span class="kwrd">null</span>;
    }
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

<p><strong>Find out if a particular folder/file has been marked for deletion.</strong></p>

<pre class="csharpcode"><span class="kwrd">public</span> <span class="kwrd">static</span> <span class="kwrd">bool</span> IsDeleted(<span class="kwrd">string</span> path)
{
    <span class="kwrd">if</span>(!IsWorkingCopy(path)) <span class="kwrd">return</span> <span class="kwrd">false</span>;

    <span class="kwrd">bool</span> isDeleted;
    <span class="kwrd">using</span> (var client = GetSvnClient())
    {
        Collection&lt;SvnStatusEventArgs&gt; args;
        client.GetStatus(path, <span class="kwrd">out</span> args);
        isDeleted = args.Count &gt; 0 &amp;&amp; args[0].LocalContentStatus == SvnStatus.Deleted;
    }
    <span class="kwrd">return</span> isDeleted;
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

<div>&#160;</div>

<div>What’s even more awesome about the guys who wrote this library actively support it (even over twitter, thanks <a href="http://twitter.com/srijken">http://twitter.com/srijken</a>!).</div>

<div>&#160;</div>

<div>And that was even before I found out that they have a ready made .wxs file for integrating the .dlls into my WiX installer package. Awesome!</div>