---
title: Setting up Azure AD B2B Direct Federation with Google GSuite
date: 2020-07-10T10:01:54.049Z
tags:
  - azuread
---
If you are looking to configure [Azure AD B2B Direct Federation](https://docs.microsoft.com/en-us/azure/active-directory/b2b/direct-federation) with Google's GSuite and running into issues here's a quick screenshot of how it needs to be set up on the GSuite end.

**Service provider details**
* ACS URL: https://login.microsoftonline.com/login.srf
* Entity ID: urn:federation:MicrosoftOnline
* Name ID format: PERSISTENT
* Name ID: Basic Information > Primary Email

**SAML Attribute Mapping**
* Primary email > http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress

![](https://merill.net/images/uploads/gsuite-saml-app-1.png)

![](https://merill.net/images/uploads/gsuite-saml-app-2.png)

Once this is setup your guest users coming in from the specified domain can use their GSuite identity to sign in/SSO instead of having to create a Microsoft Account and password.

![](https://merill.net/images/uploads/azure-ad-direct-federation-gsuite-demo.gif)