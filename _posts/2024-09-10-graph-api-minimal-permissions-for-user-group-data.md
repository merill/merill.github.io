---
title: "Graph API: Minimal permissions to read user group membership"
description: ""
date: 2024-09-10T08:00:23.428Z
preview: ""
tags: []
categories: []
---

Here's an interesting question I received today.

> What are the minimal permissions required to read group membership for a user?

The ask was for an application so we need to grant Application permissions and the first attempt was with [`User.Read.All`](https://graphpermissions.merill.net/permission/User.Read.All) permission.

When you run this query you do get the groups the user is a member of but it is limited to just the group id. The permission is not enough to get the name of the group.

```powershell
Invoke-GraphRequest -Uri 'https://graph.microsoft.com/v1.0/users/merill@elapora.com/memberOf/microsoft.graph.group?$select=displayName' | ConvertTo-Json
```

![screenshot showing querying by group member with user.read permission](/images/uploads/ReadGroupMember.png)

Now this would be perfectly valid if your app needed just the ID of the group.

However if the app needs the name and other details of the group then you will need to grant additional permissions.

My immediate thought was to grant [Group.Read.All](https://graphpermissions.merill.net/permission/Group.Read.All) but this is a scary permissions, especially when it is an application permission. This will grant tenant wide access to read any information stored in a Group or Team. This includes files and messages in a channel.

So what's the least privilege permission that will grant access to just the display name?

As of today, the answer is [`GroupMember.Read.All`](https://graphpermissions.merill.net/permission/GroupMember.Read.All) permission. The reason I say "as of today" is because the permissions are constantly being updated and new permissions are being added, so it is always a good idea to check the docs for the least privilege permissions. Since I did this frequently I built a site to easily show the least privilege permissions [Microsoft Graph permissions reference](https://graphpermissions.merill.net/).

```powershell

![screenshot showing querying by group member with user.read permission](/images/uploads/GetGroupMember-UserReadAllAndGroupMemberReadAll.png)

