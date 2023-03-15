---
title: Azure AD and Microsoft Graph Extensions and Attributes
category: tips
tags:
- azuread
- graph
excerpt: A comparison of the five different types of Azure AD extensions and attributes.
date: 2023-02-09 22:39:52 +0000
---

A comparison of the five different types of Microsoft Azure AD + Graph extensions and attributes.

||[Extension Attributes](https://learn.microsoft.com/graph/extensibility-overview?tabs=http) 1-15 (aka onPremisesExtensionAttributes)|[Directory extensions / Custom extension properties](https://learn.microsoft.com/graph/api/resources/extensionProperty?view=graph-rest-1.0) (aka AAD extensions)|[Schema extensions](https://learn.microsoft.com/graph/api/resources/schemaextension)|[Open extensions](https://learn.microsoft.com/graph/api/resources/opentypeextension)|[Custom security attributes](https://learn.microsoft.com/azure/active-directory/fundamentals/custom-security-attributes-overview)|
|----|:-:|:-:|:-:|:-:|:-:|
|Audience|IT Admins • Devs|IT Admins • Devs|Devs|Devs|IT Admins • Devs|
|[Dynamic group membership rule](https://learn.microsoft.com/azure/active-directory/enterprise-users/groups-dynamic-membership)|✅|✅|❌|❌|❌|
|[Conditional Access - App Filter](https://learn.microsoft.com/azure/active-directory/conditional-access/concept-filter-for-applications)|❌|❌|❌|❌|✅|
|[Conditional Access - Device Filter](https://learn.microsoft.com/azure/active-directory/conditional-access/concept-condition-filters-for-devices)|✅|❌|❌|❌|❌|
|Admin user interface|✅|❌|❌|❌|✅|
|[Cross-Tenant synchronization](https://learn.microsoft.com/en-us/azure/active-directory/multi-tenant-organizations/cross-tenant-synchronization-overview)|✅|✅|❌|❌|❌|
|[App user provisioning](https://learn.microsoft.com/en-us/azure/active-directory/multi-tenant-organizations/cross-tenant-synchronization-overview)|✅|✅|❌|❌|❌|
|[Entitlement Management automatic assignment](https://learn.microsoft.com/en-us/azure/active-directory/governance/how-to-lifecycle-workflow-sync-attributes)|✅|✅|❌|❌|❌|
|[Lifecycle Workflows execution conditions scope](https://learn.microsoft.com/en-us/azure/active-directory/governance/how-to-lifecycle-workflow-sync-attributes)|✅|✅|❌|❌|❌|
|Filterable|✅|✅|✅|❌|✅|
|[External identities - Self-service sign up flow](https://learn.microsoft.com/en-us/azure/active-directory/external-identities/self-service-sign-up-user-flow)|✅|✅|❌|❌|❌|
|[Usable for customizing token claims](https://learn.microsoft.com/azure/active-directory/develop/active-directory-optional-claims)|✅|✅|❌|❌|❌|
|Requires AAD P1/P2 license|❌|❌|❌|❌|✅|
|[Azure ABAC](https://learn.microsoft.com/azure/role-based-access-control/conditions-overview)|❌|❌|❌|❌|✅|
|[Block read access](https://learn.microsoft.com/azure/active-directory/fundamentals/custom-security-attributes-overview#why-use-custom-security-attributes)|❌|❌|❌|❌|✅|
|Strongly typed|❌|✅|✅|❌|✅|
|Support multi-valued attributes|✅|✅<sup>1<sup>|❌|❌|✅|
|Azure AD Connect and Cloud Sync|✅|✅|❌|❌|❌|
|Supported resources|user • device|user • group • administrativeUnit • application • device • organization|user • group • administrativeUnit • application • contact • device • event • message • organization • post|user • group • contact • device • event • message • organization • post • todoTask • todoTaskList|user • servicePrincipal|
|Data types|String|Binary • Boolean • DateTime • Integer • LargeInteger • String (256 char)|Binary • Boolean • DateTime • Integer • String|String|Boolean • Integer • String|
|Max limits|15 per object|100 extensions across all types and all applications|100 per resource|2 per creator app per resource|50 per object • 500 attributes per tenant • More info|
|When to use|• Simpler way to leverage on-prem data or Exchange data<br/>• Wanting a simple string attribute on a user/device which can be used in multiple applications as a claim|• Extending AAD resources with more attributes<br/>• Need more strongly-typed attributes than extension attributes 1-15<br/>• With AAD Connect Sync, can also sync on-prem or SharePoint data|• To extend Graph resources<br/>• Don’t require attributes as part of user authentication and as a claim|Directly add attributes to single Graph object, rather than through an extension schema|Store confidential data
|Key notes|• Can only sync for users with onPremisesSyncEnabled<br/>• Cannot be updated by Microsoft Graph unless users/devices are cloud only (not synced from on-prem)|• Extension is created on an app object, then target resource(s) are manually updated with value<br/>• AAD Connect Sync uses directory extensions|Extension is created as stand-alone resource, then applied to object|Simple setup and usage|Built with security and least privilege|

<sup>1</sup> Multi-value support in directory extensions is limited to attributes synchronized from on-prem. It is not possible to create new multi-valued directory extensions in Azure AD.
