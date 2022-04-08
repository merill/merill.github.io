---
title: AzureAD Restricted Access - Guest Permission Level
category: azuread
tags:
- external identities
- azuread

---
ICYMI We introduced a new guest permission level in Azure AD that restricts what guests can view about other directory objects in your tenant.

![Screenshot showing table of guest permission levels with new one from Restricted access (new) = Guests can't see membership of any groups](https://pbs.twimg.com/media/FOz_tpsaUAEjioZ?format=jpg&name=large)

When guest access is restricted, guests can view only their own user profile. Permission to view other users isn't allowed even if the guest is searching by UserPrincipalName or objectId. Restricted access also restricts guest users from seeing the membership of groups they're in

[  
](https://twitter.com/merill/status/1507895295455428617/photo/1)![Screenshot from Azure Portal showing the new guest user access restriction option. Including "Guest user access is restricted to properties and memberships of their own directory objects (most restrictive)"](https://pbs.twimg.com/media/FO0Bf8WaAAMQ0ZE?format=jpg&name=medium)

Here are some before/after experiences for Guests. This is from the My Groups page (accessed from [https://aka.ms/myapps](https://aka.ms/myapps "https://aka.ms/myapps") ). The guest goes from being able to see the names and email addresses of other guests in the group to the Groups view being disabled for them.

![Image](https://pbs.twimg.com/media/FO0PWIiaMAU3zjS?format=jpg&name=large)

Similarly, guests with restricted access are also blocked from being able to see a list of groups they are members of.

[  
](https://twitter.com/merill/status/1507895299221917696/photo/1)![Image](https://pbs.twimg.com/media/FO0XgyjaIAMmBoD?format=jpg&name=medium)

Finally, PowerShell. By default, guests with limited access will be able to get a list of group members and even traverse up the org chart by looking up managers.

![Screenshot of PowerShell commands showing what guests can see.](https://pbs.twimg.com/media/FO0aoLxagAUCTIb?format=jpg&name=large)

Restricted access blocks these commands from being run.

![Screenshot of PowerShell cmdlets to get-azureadgroupmember, get-azureaduser cmdlets returning Request denied error messages.](https://pbs.twimg.com/media/FO0evtVaIAEIdjN?format=jpg&name=large)

This doc has a neat table summarizing the different access levels. [Default user permissions - Azure Active Directory | Microsoft Docs](https://docs.microsoft.com/en-us/azure/active-directory/fundamentals/users-default-permissions)

To learn more about the restricted permission, supported apps and config details see [Restrict guest user access permissions - Azure Active Directory | Microsoft Docs](https://docs.microsoft.com/en-us/azure/active-directory/enterprise-users/users-restrict-guest-permissions)[](https://t.co/AlEacJkshV)

If you want to learn how to restrict PowerShell access for guests while staying with 'Limited access', that's a post for another day.

BTW In Teams: 

Limited Access = Guests can search any user in the tenant by UPN/email and chat with them. 

Restricted Access = Guests can only search and chat with users that are in the team/group(s) they have been invited to. They cannot lookup & chat with other users in the tenant