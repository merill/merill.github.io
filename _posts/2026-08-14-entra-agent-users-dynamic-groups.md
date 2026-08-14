---
title: "Microsoft Entra agent users can join your dynamic groups. Here is what to check"
description: "Microsoft has clarified that agent user accounts are evaluated by Entra dynamic user group rules. Here is what that means for access, licensing, and the exclusion rule Microsoft has not documented clearly."
date: 2026-08-14T06:00:00.000Z
preview: ""
tags:
- entraid
- agentid
- dynamicgroups
- licensing
categories: []
---

Microsoft has clarified how agent user accounts are handled by dynamic membership groups in Entra ID.

An agent's user account is evaluated by user-based dynamic membership rules. If the account satisfies a rule, it can be added to the dynamic group just like another user.

That means an agent user could inherit anything connected to that group, including group-based licenses, application access, Microsoft 365 group resources, or other permissions.

I would change one part before reposting the warning:

> Agent users are not automatically added to every dynamic group. They are evaluated by the same user rules and are added when they satisfy those rules.

Broad membership rules are the problem. An agent user can already match one without the group owner realizing it.

![Microsoft Learn documentation explaining how agent user accounts are evaluated by dynamic membership rules](/images/uploads/2026/entra-agent-users-dynamic-groups.png)

The documentation change was [committed on 13 August 2026](https://github.com/MicrosoftDocs/entra-docs/commit/af37138d7608db0579438118337d71a3ea3f27c3). It reads as a clarification of existing behavior, not an announcement that the product behavior has changed.

## Why agent users look like users to dynamic group rules

There are two identities to keep straight in Microsoft Entra Agent ID.

The primary agent identity is a service principal. It is not supported as a member of a dynamic membership group.

An agent can also have an optional agent user account for systems that require a user identity. Microsoft describes this as a subtype of the user resource. It receives tokens with `idtyp=user`, can be added to groups and administrative units, and can be assigned licenses.

Microsoft Graph exposes the account as an [`agentUser` resource](https://learn.microsoft.com/graph/api/resources/agentuser?view=graph-rest-1.0). It inherits many normal user properties, including:

- `userPrincipalName`
- `userType`
- `department`
- `companyName`
- `employeeId`
- `assignedLicenses`
- `assignedPlans`

Because `agentUser` inherits these properties, a rule written before agent users arrived in the tenant can still match one.

Consider a common "all member users" rule:

```text
(user.objectId -ne null) -and (user.userType -eq "Member")
```

`userType` separates `Member` from `Guest`. An agent user can also have `userType` set to `Member`, so the property says nothing about whether the identity belongs to a person.

The same issue can appear in rules based on country, department, company name, usage location, UPN, or another supported user property. If the agent user has the value, it can satisfy the rule.

## How an agent user can consume a license

Microsoft explicitly documents that an agent user can be assigned licenses and that its `assignedLicenses` collection includes licenses inherited through group-based licensing.

If a dynamic group is used for licensing, an agent user that joins the group can consume one of the available product licenses. If the tenant runs out, newly added users will not receive that product license until another license becomes available.

There are two licensing checks to make:

1. The product assigned to the group could be assigned to an agent that does not need it.
2. Dynamic group licensing requires enough Entra ID P1 licenses to cover each unique user in one or more dynamic groups. Because an agent user is a user subtype, organizations should confirm how their agent population affects this requirement with their Microsoft licensing contact.

Licenses are only one consequence. Check whether each affected group is also used for:

- Enterprise application assignments
- Microsoft 365 groups and Teams
- SharePoint permissions
- Conditional Access targeting
- Access packages and other governance workflows
- Azure and application-specific role assignments that use the group

An agent user cannot be added to a role-assignable group. That blocks one privilege path, but ordinary security groups can still carry broad access.

## The documentation does not show the rule you need

Microsoft's guidance stops short of giving admins a usable rule.

Microsoft says administrators can add a condition to exclude agent user accounts, include only agent user accounts, or target accounts associated with a specific agent identity blueprint.

However, the same dynamic membership article does not list an agent-specific discriminator in its table of supported user properties. I also could not find a Microsoft example showing the syntax for targeting a blueprint.

I wouldn't put an undocumented agent exclusion into production unless Microsoft publishes the supported condition or the rule validator confirms it in your tenant.

On 14 August 2026, admins are being told to add a condition that Microsoft has not shown them how to write. Microsoft needs to publish the supported syntax.

## How I would check a tenant

### 1. Check what each matching group actually grants

Membership tells you where an agent user has landed. The group's consumers tell you what the account received.

Prioritize groups that:

- Have product licenses assigned
- Are assigned to enterprise applications
- Back a Team or Microsoft 365 group
- Are included in Conditional Access policies
- Grant access to SharePoint sites or other resources
- Feed entitlement management or automated provisioning

For licensing groups, also check group-based licensing errors and the remaining license count for each assigned SKU.

### 2. Prefer a positive marker for human identities

I prefer a positive rule that includes identities known to be human. Otherwise, the exclusion list grows every time a new nonhuman identity type appears.

For example, if every workforce identity receives an HR-controlled `employeeId` and agent users never do, you could require it:

```text
(user.userType -eq "Member") -and (user.employeeId -ne null)
```

Only use this if your HR process owns `employeeId` and assigns it consistently. Agent users support the property, so an agent could match later if someone populates the value.

A directory extension targeted at `User` may also work. Dynamic membership rules support directory extension properties, and the agent user creation API supports extensions. You could tag workforce users with `identityKind = Human` and require that value in licensing rules.

```text
user.extension_<appIdWithoutHyphens>_identityKind -eq "Human"
```

Microsoft's documentation does not show a dynamic group evaluating a directory extension on an `agentUser`. Test the provisioning and rule evaluation path with an agent user in a test tenant before relying on this design.

Do not assume the older `extensionAttribute1` to `extensionAttribute15` fields will solve this for agent users. Microsoft Graph currently shows `onPremisesExtensionAttributes` as not applicable to the `agentUser` subtype.

I'm glad the warning is now in the documentation. But Microsoft still needs to publish the rule syntax admins are supposed to use.

You can see this and the rest of the Microsoft Entra documentation changes for the day at [Daily.Entra.News](https://daily.entra.news/day/2026-08-14/).

## References

- [Manage rules for dynamic membership groups in Microsoft Entra ID](https://learn.microsoft.com/entra/identity/users/groups-dynamic-membership)
- [The agent's user account in Microsoft Entra Agent ID](https://learn.microsoft.com/entra/agent-id/agent-users)
- [Microsoft Graph agentUser resource](https://learn.microsoft.com/graph/api/resources/agentuser?view=graph-rest-1.0)
- [Validate rules for dynamic membership groups](https://learn.microsoft.com/entra/identity/users/groups-dynamic-rule-validation)
- [Assign Microsoft 365 licenses to user accounts](https://learn.microsoft.com/microsoft-365/enterprise/assign-licenses-to-user-accounts)
