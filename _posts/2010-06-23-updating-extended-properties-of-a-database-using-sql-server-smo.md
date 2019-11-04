---
id: 710
title: Updating Extended Properties of a Database using SQL Server SMO
date: 2010-06-23T11:28:01+00:00
author: Merill Fernando

guid: http://merill.net/?p=710
permalink: /2010/06/updating-extended-properties-of-a-database-using-sql-server-smo/
dsq_thread_id:
  - "110433721"
categories:
  - .NET
tags:
  - smo
  - SQL
---
Updating the extended properties on a database using SQL Server's excellent <a href="http://msdn.microsoft.com/en-us/library/ms162169.aspx">Server Management Objects</a> API is not as straightforward as setting the value and calling update.

The database.Alter() method needs to be called both before and after updating the value. I had to lookup the code of <a href="http://blog.elpluto.com/">El Pluto</a>'s awesome <a href="http://xqued.codeplex.com/">SQL Server Extended Properties Quick Editor</a> project on CodePlex to figure this out.

<div style="color: black; background: white; font-family: Consolas; font-size: 10pt;">
<pre style="margin: 0px;"><span style="color: blue;">using</span> Microsoft.SqlServer.Management.Smo;</pre>
<pre style="margin: 0px;">&nbsp;</pre>
<pre style="margin: 0px;"><span style="color: gray;">///</span><span style="color: green;"> </span><span style="color: gray;">&lt;summary&gt;</span></pre>
<pre style="margin: 0px;"><span style="color: gray;">///</span><span style="color: green;"> Set's the extended property of a database.</span></pre>
<pre style="margin: 0px;"><span style="color: gray;">///</span><span style="color: green;"> </span><span style="color: gray;">&lt;/summary&gt;</span></pre>
<pre style="margin: 0px;"><span style="color: gray;">///</span><span style="color: green;"> </span><span style="color: gray;">&lt;param name=&quot;serverName&quot;&gt;</span><span style="color: green;">The name of the SQL Server.</span><span style="color: gray;">&lt;/param&gt;</span></pre>
<pre style="margin: 0px;"><span style="color: gray;">///</span><span style="color: green;"> </span><span style="color: gray;">&lt;param name=&quot;databaseName&quot;&gt;</span><span style="color: green;">The name of the database.</span><span style="color: gray;">&lt;/param&gt;</span></pre>
<pre style="margin: 0px;"><span style="color: gray;">///</span><span style="color: green;"> </span><span style="color: gray;">&lt;param name=&quot;propertyName&quot;&gt;</span><span style="color: green;">The name of the extended property.</span><span style="color: gray;">&lt;/param&gt;</span></pre>
<pre style="margin: 0px;"><span style="color: gray;">///</span><span style="color: green;"> </span><span style="color: gray;">&lt;param name=&quot;value&quot;&gt;</span><span style="color: green;">The value of the extended property.</span><span style="color: gray;">&lt;/param&gt;</span></pre>
<pre style="margin: 0px;"><span style="color: blue;">private</span> <span style="color: blue;">void</span> SetExtendedProperty(<span style="color: blue;">string</span> serverName, <span style="color: blue;">string</span> </pre>
<pre style="margin: 0px;">&nbsp;&nbsp;&nbsp; databaseName, <span style="color: blue;">string</span> propertyName, <span style="color: blue;">string</span> value)</pre>
<pre style="margin: 0px;">{</pre>
<pre style="margin: 0px;">&nbsp;&nbsp;&nbsp; <span style="color: blue;">var</span> server = <span style="color: blue;">new</span> <span style="color: #2b91af;">Server</span>(serverName);</pre>
<pre style="margin: 0px;">&nbsp;&nbsp;&nbsp; <span style="color: blue;">var</span> database = server.Databases[databaseName];</pre>
<pre style="margin: 0px;">&nbsp;</pre>
<pre style="margin: 0px;">&nbsp;&nbsp;&nbsp; database.Alter();</pre>
<pre style="margin: 0px;">&nbsp;&nbsp;&nbsp; <span style="color: blue;">if</span> (!database.ExtendedProperties.Contains(propertyName))</pre>
<pre style="margin: 0px;">&nbsp;&nbsp;&nbsp; {</pre>
<pre style="margin: 0px;">&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; database.ExtendedProperties.Add(</pre>
<pre style="margin: 0px;">&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; <span style="color: blue;">new</span> <span style="color: #2b91af;">ExtendedProperty</span>(database, propertyName, value));</pre>
<pre style="margin: 0px;">&nbsp;&nbsp;&nbsp; }</pre>
<pre style="margin: 0px;">&nbsp;&nbsp;&nbsp; <span style="color: blue;">else</span></pre>
<pre style="margin: 0px;">&nbsp;&nbsp;&nbsp; {</pre>
<pre style="margin: 0px;">&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; database.ExtendedProperties[propertyName].Value = value;</pre>
<pre style="margin: 0px;">&nbsp;&nbsp;&nbsp; }</pre>
<pre style="margin: 0px;">&nbsp;&nbsp;&nbsp; database.Alter();</pre>
<pre style="margin: 0px;">}</pre>
<pre style="margin: 0px;">&nbsp;</pre>
</div>