---
id: 41
title: Visual Studio 2008 TFS breaking Unit Test Projects
date: 2007-12-13T16:02:42+00:00
author: Merill Fernando

guid: /post/2007/12/Visual-Studio-2008-TFS-breaking-Unit-Test-Projects.aspx
permalink: /2007/12/visual-studio-2008-tfs-breaking-unit-test-projects/
dsq_thread_id:
  - "78006260"
categories:
  - Microsoft
---
<p>On the next iteration of my current we'll be using Visual Studio 2008 and targeting .NET 3.5.</p> <p>As usual I jumped the gun and installed it before the rest of the team, so I had to keep VS 2005 running at the same time. Everything was hunky dory until I installed the TFS 2008 client. This somehow caused the unit test projects to be disconnected from the TFS server. You could check out and check in stuff from the Team Explorer but the projects were showing up as disconnected from the Solution Explorer.</p> <p>To get out of this mess I had to uninstall both 2005 and 2008 Team Explorer and then reinstall Team Explorer 2005.</p>