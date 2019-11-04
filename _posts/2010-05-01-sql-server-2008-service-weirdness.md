---
id: 668
title: SQL Server 2008 Service Weirdness
date: 2010-05-01T15:59:17+00:00
author: Merill Fernando

guid: http://merill.net/?p=668
permalink: /2010/05/sql-server-2008-service-weirdness/
dsq_thread_id:
  - "91393932"
categories:
  - Service Manager
tags:
  - SQL
---
Two weird things I learnt about SQL Server while building the SharePoint 2010 Service Manager.

<strong>1. SQL Server Agent service for SQL Express is bogus</strong>

Whenever Service Manager started, the SQL Server Agent service for the SharePoint (SQL Express) instance  would immediately stop with either of the following errors logged in the Windows Event Log.
<ul>
	<li><em>The service cannot be started, either because it is disabled or because it has no enabled devices associated with it. [0x80070422]</em></li>
	<li><em>SQLServerAgent could not be started (reason: Error creating a new session).</em></li>
</ul>
The self explanatory title of the bug filed on Connect says it all '<a href="https://connect.microsoft.com/SQLServer/feedback/details/351806/sql-express-rc0-installs-sql-agent-service-for-no-apparent-reason">SQL Express installs SQL Agent Service for no apparent reason</a>'. Apparently the team cutting down features for the Express edition forgot to tell the Agent team that they weren't needed in Express.

<strong>2. SQL Server VSS Writer Service : Startup Type get's reset to 'Manual'</strong>

The Service Manager has a feature that let's you set the startup type of all the SharePoint and related services to Manual. This way they wouldn't automatically startup when Windows starts hence leaving the workstation to boot faster.

The Service Manager only shows the 'Stop Automatic Startup' button if the Startup Type of any of SharePoint services are set to Automatic. While testing the feature I released that after sometime the button automatically showed up even after I had set all the services to start manually.

That was when I figured out that even if I manually change the service (through Control Panel) to start manually, something would change the startup to Automatic after a while. I haven't figured out what changes it's startup type to automatic but I'm guessing that's by design. My workaround for the Service Manager was to ignore the startup type of the VSS Writer service when checking if all the services were set to manual.