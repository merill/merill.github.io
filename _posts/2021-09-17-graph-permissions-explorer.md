---
title: Graph Permissions Explorer
category: tip
tags:
- permissions
- azuread
- graph
date: 2021-09-17 20:27:52 +0000
---
If you are a developer in the Microsoft 365 ecosystem you will be well versed with the [Microsoft Graph API reference docs](https://docs.microsoft.com/en-us/graph/api/overview?view=graph-rest-1.0) and most probably know about permission scopes (eg. User.Read).

The docs are an awesome resource geared towards developers and lets you navigate by APIs and view the permissions required and includes code samples.

What is missing in the docs however is a view that shows the APIs and resources that are exposed by a permission.

Let's say you are the Azure AD administrator or a security/compliance officer in your organisation and a developer asks for the Files.Read.All permission. 

Until today it's not been very easy to find this out. You would need to search by permission and then click through to each API. 

To solve this created the Graph Permissions Explorer. This site lets you navigate by a permission scope and view all the Graph APIs and resources for a given permission.

For example here is the view for [Files.Read.All](https://graphpermissions.merill.net/permission/Files.Read.All.html).  

Hopefully you find this site useful when working with apps in Azure Active Directory and Microsoft 365. In my next post I will show how I built the solution and set up the automation to update the site everyday as the Microsoft Graph docs are updated.

Give it a try at [https://graphpermissions.merill.net](https://graphpermissions.merill.net).