---
title: Azure AD multi-tenant app vs single tenant app
category: ''
tags: []

---
I've recently noticed that Azure AD admins are being asked to create multi-tenant apps in their corporate tenant.

In some instances, it was the devs in the org asking for this, in other instances it was the application vendor.

Here are some things to watch out for 👇

![](/images/uploads/azureadsingletenantappvsmultitenantapp.jpg)

Multi-tenant apps are meant for ISVs and SaaS vendors to create an instance of an app in 'their own tenant'. Examples of such apps are ServiceNow and SalesForce.

When an app is created as a multi-tenant app, ANY user from ANY Azure AD tenant can visit the app's url and sign in.

If you create a multi-tenant app in your corporate tenant and apply a conditional access policy. The policy only applies to users in your tenant.

⚠️ I'll repeat ➟ your CA policies do not apply to users signing into your multi-tenant app in their own tenant.

So, what is the general rule of thumb that Azure AD admins and cybersecurity teams should follow?

If the app is from a vendor/SaaS provider:

✅ Add the app to your tenant from the Azure AD Application Gallery

✅ If the app is not in the gallery, you as the customer can request the vendor to get their app listed on the Azure AD app gallery

✅ If app gallery is not an option, request the vendor to create the app in their own tenant. Use the admin consent model to add the app to your tenant.

✅ If the only option provided by the vendor is to create the app in your tenant, push for the vendor to allow you to create a single tenant app.

If the app is developed by devs in your org and is only meant for users in your own org.

✅ Ask why the dev needs this to be a multi-tenant app?

✅ Ask if the devs have implemented appropriate checks to prevent sign-ins from other tenants.

There are many valid scenarios for creating multi-tenant apps in your tenant, including

✅ You are a SaaS vendor or ISV and you create and publish apps that Azure AD customers can consume

✅ You manage multiple Azure AD tenants in your org and you need a single service principle (workload identity) to access the other tenants (e.g. automate DevOps tasks across your tenants)

Here are some further reading on the topic of multi-tenancy. These are meant for devs however its good reading for admins to appreciate what it takes to build a least-privilege multitenant app.

👉 [https://learn.microsoft.com/en-us/azure/architecture/multitenant-identity/](https://learn.microsoft.com/en-us/azure/architecture/multitenant-identity/ "https://learn.microsoft.com/en-us/azure/architecture/multitenant-identity/")

👉 [https://learn.microsoft.com/en-us/azure/active-directory/develop/howto-convert-app-to-be-multi-tenant](https://learn.microsoft.com/en-us/azure/architecture/multitenant-identity/ "https://learn.microsoft.com/en-us/azure/architecture/multitenant-identity/")

Note: This MSRC blog post provides additional guidance on how you can review the multi-tenant apps in your tenant and switch them to a single tenant app if multi-tenant is not a requirement.

[Guidance on Potential Misconfiguration of Authorization of Multi-Tenant Applications that use Azure AD | MSRC Blog | Microsoft Security Response Center](https://msrc.microsoft.com/blog/2023/03/guidance-on-potential-misconfiguration-of-authorization-of-multi-tenant-applications-that-use-azure-ad/)