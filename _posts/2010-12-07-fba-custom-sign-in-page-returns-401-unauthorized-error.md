---
id: 720
title: FBA Custom Sign In Page returns 401 Unauthorized error
date: 2010-12-07T11:14:56+00:00


guid: http://merill.net/?p=720
permalink: /2010/12/fba-custom-sign-in-page-returns-401-unauthorized-error/
dsq_thread_id:
  - "186086429"
categories:
  - SharePoint 2010
tags:
  - claims
  - fba
  - sso
---
If you've built a custom sign in page in SharePoint 2010 but keep getting a 401 Unauthorized error instead of the sign in page then you've most probably deployed the solution package to a single web application.

To resolve the issue the solution needs to be deployed to all applications and not restricted to a single web application.

i.e. When calling Install-SPSolution don't include the -WebApplication parameter.

Edit: Another instance when you will see the 401 Unauthorized error is when your not inheriting from the correct base page. It should not be the layoutsbasepage.

Another tip if you see the following error in your ULS log:
<code>Request for security token failed with exception: System.ServiceModel.FaultException`1[System.ServiceModel.ExceptionDetail]: Object reference not set to an instance of an object. (Fault Detail is equal to An ExceptionDetail, likely created by IncludeExceptionDetailInFaults=true, whose value is: System.NullReferenceException: Object reference not set to an instance of an object.   
 at Microsoft.SharePoint.IdentityModel.SPSecurityTokenService.SPRequestInfo.ValidateFormsAuthProviderNames(Uri context, String membershipProvider, String roleProvider)    
 at Microsoft.SharePoint.IdentityModel.SPSecurityTokenService.SPRequestInfo.SetProviderNames(RequestSecurityToken request)    
 at Microsoft.SharePoint.IdentityModel.SPSecurityTokenService.SPRequestInfo..ctor(IClaimsIdentity identity, RequestSecurityToken request, Boolean initializeForActor)    
 at Microsoft.SharePoint.IdentityModel.SPSecurityTokenService.SPRequestInfo..ctor(IClaimsPrincipal principal, RequestSecurityToken request)    
 at Microsoft.SharePoint.IdentityModel.SPSecurityTokenService.GetTokenLifetime(Lifetime requestLifetime)    
 at Microsoft.IdentityModel.SecurityTokenService.SecurityTokenService.Issue(IClaimsPrincipal principal, RequestSecurityToken r...).
</code>

That means your using a name that has not been setup as an AAM. I was using http://localhost and it always kept failing. Changing the request url to the actual name of the server (in my case http://mosswfe1) fixed it.

Note to myself: References for creating a Custom Sign In Page
<a href="http://blogs.msdn.com/b/chunliu/archive/2010/08/21/creating-a-custom-login-page-for-fba-in-sharepoint-2010.aspx">Creating a Custom Login Page for FBA in SharePoint 2010</a>
<a href="http://blogs.msdn.com/b/kaevans/archive/2010/07/09/creating-a-custom-login-page-for-sharepoint-2010.aspx">Creating a Custom Login Page for SharePoint 2010</a>
<a href="http://blogs.msdn.com/b/pranab/archive/2010/07/26/how-to-create-custom-login-form-for-sharepoint-2010-form-based-authentication.aspx">How to create custom login page for SharePoint 2010 form based authentication (FBA)</a>