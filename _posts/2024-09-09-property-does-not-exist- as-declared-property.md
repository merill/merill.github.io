---
title: Filtering members in Entra groups and admin units
description: Fix for Property 'extensionAttribute10' does not exist as a declared property or extension property
date: 2024-07-22T07:03:08Z
preview: ""
tags: []
categories: []
---

Here's a recent Graph query-related issue I helped troubleshoot.

The request was to find all the members in an Administrative Unit with a specific value in the `extensionAttribute10` property.

However this query errored out as an unsupported query.

❌
```
/directory/administrativeUnits/<guid>/members?$filter=onPremisesExtensionAttributes/extensionAttribute10 eq 'ABC'&$count=true

code: "Request_UnsupportedQuery",
message: "Property 'extensionAttribute10' does not exist as a declared property or extension property."
```

The fix was fairly simple, just add `/microsoft.graph.user` at the end of the url path.

✅
```
/directory/administrativeUnits/<guid>/members/microsoft.graph.user?$filter=onPremisesExtensionAttributes/extensionAttribute10 eq 'ABC'&$count=true
```

So let's break down the fix.

Adding `/microsoft.graph.user` at the end of url path tells Graph API to only return members that are of type `user`. You can then apply all the available user object property filters including filtering by `extensionAttribute10`.

Why did the original query fail?

The `administrativeUnit` object like the `group` object can contain different types of directory objects.

Here's a visual representation of the directory object inheritance hierarchy.

![Illustration showing directory object inheritance hierarchy with the DirectoryObject base type and child types]({{ site.url }}{{ site.baseurl }}/images/uploads/graphdirectoryobjects.png)

When you create a group or an administrative unit, you can add users, devices, and other groups to it. Each of these objects will have their unique set of properties.

> Not all object types inheriting from `DirectoryObject` can be added to groups and administrative units.

When you query for members in a group or an administrative unit, you are querying against all the objects in the container.

![Screenshot of an Entra group that contains users, groups and devices]({{ site.url }}{{ site.baseurl }}/images/uploads/entra-group-list.png)

So while you can query against special properties like `id` and `displayName` you cannot directly query against any of the other properties.

This explains why a query for `displayName` will work without qualifying the query with the object type.

✅
```
/groups/<guid>/members?$filter=displayName eq 'John'&$count=true
```

In our original query, not all the member object types in the `administrativeUnit` object would have a declared property called `onPremisesExtensionAttributes`. Instead it is a declared property of the `user` object.

Once you qualify the query to filter by the `microsoft.graph.user` object, the query works as expected.

To close it off with another example, this query for `groups` will fail for the same reason.

❌
```
/groups/<guid>/members?$filter=onPremisesExtensionAttributes/extensionAttribute10 eq 'ABC'&$count=true
```

Which can be fixed by qualifying the query with the `microsoft.graph.user` object type.

✅
```
/groups/<guid>/members/microsoft.graph.user?$filter=onPremisesExtensionAttributes/extensionAttribute10 eq 'ABC'&$count=true
```

Here's the TLDR;

![alt text]({{ site.url }}{{ site.baseurl }}/images/uploads/GraphFilter.png)

Hope this helps!
