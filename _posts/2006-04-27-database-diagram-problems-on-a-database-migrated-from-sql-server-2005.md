---
id: 138
title: Database diagram problems on a database migrated from SQL Server 2005
date: 2006-04-27T02:00:37+00:00
author: Merill Fernando

guid: /post/2006/04/Database-diagram-problems-on-a-database-migrated-from-SQL-Server-2005.aspx
permalink: /2006/04/database-diagram-problems-on-a-database-migrated-from-sql-server-2005/
dsq_thread_id:
  - "78098791"
categories:
  - SQL
---
<p>I ran into a wierd error message when trying to view the Diagrams on a database that was migrated to SQL Server 2005.&nbsp;Something about the user not being valid and to change the database owner. </p>
<p>A quick search brought up this quick fix:</p>
<p>Try running this command to&nbsp;change the compatibility level to SQL Server 2005.</p><font color="#0000ff" size="1">
<p><font face="Lucida Console" size="2">EXEC</font></font><font face="Lucida Console" size="2"> <font color="#800000">sp_dbcmptlevel</font> database_name<font color="#808080">,</font> 90 </font></p>
<p>Works like a charm! [<a href="http://msdn2.microsoft.com/en-us/library/ms186345.aspx">SQL BOL</a>]</p>