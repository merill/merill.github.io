---
title: Querying Graph directory containers with specific properties
description: Fix for Property 'extensionAttribute15' does not exist as a declared property or extension property
date: 2024-07-22T07:03:08Z
preview: ""
tags: []
categories: []
---

Here's a recent Graph query-related issue I helped troubleshoot.

The request was to find all the members in an Administrative Unit with a specific value in the `extensionAttribute15` property.

However this query errored out as unsupported:

```
https://graph.microsoft.com/beta/directory/administrativeUnits/d2a86fca-7fe6-4842-b42f-9b53ad2283ee/members?$filter=onPremisesExtensionAttributes/extensionAttribute15 eq 'ABC'&$count=true

code: "Request_UnsupportedQuery",
message: "Property 'extensionAttribute15' does not exist as a declared property or extension property."
```

The fix was fairly simple:

```
https://graph.microsoft.com/beta/directory/administrativeUnits/d2a86fca-7fe6-4842-b42f-9b53ad2283ee/members/microsoft.graph.user?$filter=onPremisesExtensionAttributes/extensionAttribute15 eq 'F'&$count=true
```

So let's break down the fix.

The key difference is the `/microsoft.graph.user` at the end of the query. This tells the Graph API to filter the members by the `extensionAttribute15` property of the `microsoft.graph.user` object.

Why did the original query fail?

The `administrativeUnit` object like the `group` object is a directory container in Microsoft Entra that can contain different types of objects.

Here's a visual representation of the directory object hierarchy:

![Graph directory object hierarchy](/images/uploads/graphdirectoryobjects.png)

So while you can query against properties that exist in all objects like `displayName`, `id`, etc., you cannot query against properties that are specific to a certain object type.

This explains why a query for `displayName` will work without qualifying the query with the object type.

```
https://graph.microsoft.com/beta/groups/1e4a97fb-4b10-495f-8dfe-daee0f473fbd/members?$filter=displayName eq 'John'&$count=true
```

In our original query not all the members in the `administrativeUnit` object have a declared property called `onPremisesExtensionAttributes`. Instead it is a declared property of the `user` object.

Once you qualify the query to filter by the `microsoft.graph.user` object, the query works as expected.

To close it off with another example, this query for `gropus` will fail for the same reason.

```
https://graph.microsoft.com/beta/groups/1e4a97fb-4b10-495f-8dfe-daee0f473fbd/members?$filter=onPremisesExtensionAttributes/extensionAttribute15 eq 'ABC'&$count=true
```

Which can be fixed by qualifying the query with the `microsoft.graph.user` object.

```
https://graph.microsoft.com/beta/groups/1e4a97fb-4b10-495f-8dfe-daee0f473fbd/members/microsoft.graph.user?$filter=onPremisesExtensionAttributes/extensionAttribute15 eq 'ABC'&$count=true
```


Hope this helps!
