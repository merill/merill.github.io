---
title: "Uninstall-Graph PowerShell"
description: "Free and open source cmdlet to force remove all Microsoft Graph PowerShell modules from your system."
date: 2025-05-29T01:37:34.000Z
preview: ""
tags: []
categories: []
---

The Graph PowerShell module is a complicated beast. It has multiple modules and due to various reasons you might want to get back to a clean slate of no Graph PowerShell modules in your system.

To solve this I built a module that does just one thing

**Uninstall-Graph**

![Uninstall-Graph landing page](/images/uploads/2025/uninstall-graph-landing.jpeg)

You can get it at [uninstall-graph.merill.net](https://uninstall-graph.merill.net).

It basically runs through multiple times to uninstall all the modules and then finally cleans out the folders for the ones that are stubborn.

Remember to restart a fresh PowerShell session after running this.

## Why is the Graph PowerShell module so special?

For starters, some graph modules depend on other graph modules then you have various non-Microsoft modules (like [Maester](https://maester.dev)) that rely on Graph modules.

This means uninstalling them is not as simple as running

```
Uninstall-Module Microsoft.Graph
```

You would typically see something like this error.

```
PackageManagement\Uninstall-Package : The module 'Microsoft.Graph.Applications' of version '2.12.0' in module base folder 'C:\Program Files\WindowsPowerShell\Modules\Microsoft.Graph.Applications\2.12.0' cannot be uninstalled, because one or more other modules 'Microsoft.Graph' are dependent on this module. Uninstall the modules that depend on this module before uninstalling module 'Microsoft.Graph.Applications'.
```

## Why would you need to uninstall Microsoft Graph in the first place?

Well the most common reason is that you end up with different versions of the various Graph PowerShell modules and one day you will be hit errors like this

```
Could not load file or assembly 'Microsoft.Graph.Authentication, Version=2.8.0.0, Culture=neutral,PublicKeyToken=31bf3856ad364e35' or one of its dependencies. The system cannot find the file specified.
```

or

```
Import Graph module fails with Could not load file or assembly 'Azure.Core, Version=1.39.0.0, Culture=neutral, PublicKeyToken=92742159e12e44c8' or one of its dependencies. The system cannot find the file specified
```

or something similar.

So getting back to a clean slate and then installing the modules afresh is my preferred solution for this problem.

I'm keen on having this module address all the edge cases when it comes to uninstalling the Graph PS modules. So if you come across any issues please raise them on GitHub. Thanks!
