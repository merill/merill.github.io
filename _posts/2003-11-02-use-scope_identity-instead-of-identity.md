---
id: 482
title: Use scope_identity() instead of @@identity
date: 2003-11-02T13:15:10+00:00
author: Merill Fernando

guid: /post/2003/11/Use-scope_identity()-instead-of-identity.aspx
permalink: /2003/11/use-scope_identity-instead-of-identity/
dsq_thread_id:
  - "77893695"
categories:
  - SQL
---
<body xmlns="http://www.w3.org/1999/xhtml">
    <p>
        <a href="http://weblogs.sqlteam.com/travisl/">TravisL</a> <a href="http://weblogs.sqlteam.com/travisl/posts/405.aspx">explains</a> why
        we should use scope_identity instead of @@identity when we want to get the ID of the
        last record that was added.
    </p>
    <p>
        The problem with @@identity is that it returns the ID of the last record that was
        in the current connection. In which case if the table that you adding to has triggers
        (which inserts records in other tables) then @@identity returns the ID of the last
        record that was added by code inside the trigger. This becomes a potentially very
        difficult bug to track down. 
    </p>
    <p>
        So what should you do? Use scope_identity() which returns the ID of the last record
        that was inserted in the current scope. See&#160;<a href="http://msdn.microsoft.com/library/default.asp?url=/library/en-us/tsqlref/ts_sa-ses_6n8p.asp">MSDN:scope_identity()</a>&#160;for
        detailed examples.&#160;
    </p>
</body>