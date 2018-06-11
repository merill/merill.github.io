---
id: 578
title: Changing the default schema in Oracle
date: 2009-04-28T13:14:01+00:00
author: Merill Fernando
layout: post
guid: http://merill.net/2009/04/changing-the-default-schema-in-oracle/
permalink: /2009/04/changing-the-default-schema-in-oracle/
dsq_thread_id:
  - "77837966"
categories:
  - Tips
tags:
  - oracle
  - schema
  - session
---
<p>The application I was working on assumed that the user would always be in the default schema. I ran into a snag when I had to connect to the staging environment where the read only user that I was provided with didn’t have all the objects in his schema.</p>  <p>The solution was to make a call to change the default schema using the ALTER SESSION call with this code.</p>  <div class="csharpcode">   <pre class="alt">        <span class="rem">/// &lt;summary&gt;</span></pre>

  <pre>        <span class="rem">/// Sets the schema to use if one is configured.</span></pre>

  <pre class="alt">        <span class="rem">/// &lt;/summary&gt;</span></pre>

  <pre>        <span class="kwrd">public</span> <span class="kwrd">static</span> <span class="kwrd">void</span> SetSchema()</pre>

  <pre class="alt">        {</pre>

  <pre>            var schema = ConfigurationManager.AppSettings[<span class="str">&quot;SchemaName&quot;</span>];</pre>

  <pre class="alt">            <span class="kwrd">if</span> (<span class="kwrd">string</span>.IsNullOrEmpty(schema)) <span class="kwrd">return</span>;</pre>

  <pre>&#160;</pre>

  <pre class="alt">&#160;</pre>

  <pre>            <span class="kwrd">using</span> (var connection = GetConnection())</pre>

  <pre class="alt">            {</pre>

  <pre>                <span class="kwrd">using</span> (var command = <span class="kwrd">new</span> OracleCommand(<span class="str">&quot;alter session set current_schema=&quot;</span> + schema))</pre>

  <pre class="alt">                {</pre>

  <pre>                    connection.Open();</pre>

  <pre class="alt">                    command.Connection = connection;</pre>

  <pre>                    command.ExecuteNonQuery();</pre>

  <pre class="alt">                }</pre>

  <pre>            }</pre>

  <pre class="alt">        }</pre>
</div>
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