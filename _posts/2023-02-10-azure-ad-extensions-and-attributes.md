---
title: Azure AD Extensions and Attributes
category: tips
tags: []
excerpt: A comparison of the five different types of Azure AD extensions and attributes.
date: 2023-02-09 22:39:52 +0000
---

A comparison of the five different types of Azure AD extensions and attributes.

||Extension Attributes 1-15 (aka onPremisesExtensionAttributes)|Directory extensions (aka AAD extensions)|Schema extensions|Open extensions|Custom security attributes|
|----|----|----|----|----|----|
|Supported resources|user<br/>device|user<br/>group<br/>administrativeUnit<br/>application<br/>device<br/>organization|user<br/>group<br/>administrativeUnit<br/>application<br/>contact<br/>device<br/>event<br/>message<br/>organization<br/>post|user<br/>group<br/>contact<br/>device<br/>event<br/>message<br/>organization<br/>post<br/>todoTask<br/>todoTaskList|user<br/>servicePrincipal|
|Data types|String|Binary<br/>Boolean<br/>DateTime<br/>Integer<br/>LargeInteger<br/>String (256 char)|Binary<br/>Boolean<br/>DateTime<br/>Integer<br/>String|String|Boolean<br/>Integer<br/>String|
|Strongly typed|N|Y|Y|N|Y|
|Targeted audience|IT Admins|IT Admins|Devs|Devs|IT Admins|
|Dynamic groups|Y|Y|N|N|N|
|CA – App Filter|N|N|N|N|Y|
|CA – Device Filter|Y|Y|N|N|N|
|Admin user interface|Y|N|N|N|Y|
|Filterable|Y|Y|Y|N|Y|
|Use in claims?|Y|Y|N|N|N|
|Azure ABAC|N|N|N|N|Y|
|Use in custom token claims|Y|Y|N|N|N|
|Apply read security|N|N|N|N|Y|
|Supports multi-valued attributes|Y|Y||N|Y|
|Max limits|15 per object|100 extensions across all types and all applications|100 per resource|2 per creator app per resource|50 per object<br/>500 attributes per tenant<br/>More info|
