---
title: Use a custom app for Graph PowerShell delegate access
category: tips
tags:
- azuread
- graph
- powershell
excerpt: Set up a custom application registration for using with Microsoft Graph PowerShell
date: 2023-03-02T10:39:52.000+00:00

---
If you want to follow the least privilege model for the applications in your Azure AD tenant, you might be concerned about consenting to many permissions scopes to the Microsoft Graph PowerShell app over time.

To avoid this, you can register your own app for use with Microsoft Graph PowerShell. This allows you to have more granular control.

Here are the steps to go about setting it up.

* Browse to **Entra** > **App registrations** [\[adappreg.cmd.ms\]](https://adappreg.cmd.ms) > **New Registration**
  * **Name:** Microsoft Graph PowerShell - High Privilege admin use only (<- Give a meaningful name)
  * **Account type:** Accounts in this organization directory
  * **Redirect URI:**
    * Select **Public client/native** from the drop down
    * **Uri:** http<nolink>://localhost
  * Click **Create**

That's it!

Now you can use this app instead of the default one by connecting with

```powershell
Connect-MgGraph -ClientId <Your new app clientid> -TenantId <your tenant id>
```

Here are a few screenshots to help guide you.

![Screenshot showing how the app should be created](/images/uploads/graphpowershellcustomappsigninconfig.png "Microsoft Graph PowerShell app configuration")

![Screenshot signing in with the new app in PowerShell](/images/uploads/graphpowershellcustomappsignin.png)

Quick note. The steps above will get you working with PowerShell 7, which is what you SHOULD be using. In the unfortunate event that you are stuck with Windows PowerShell 5.1 you need to do one more thing.

* Open the app you just created in **App registrations** [\[adappreg.cmd.ms\]](https://adappreg.cmd.ms)
* Select **Authentication**
  * Check **https://login.microsoftonline.com/common/oauth2/nativeclient**
  * Click **Save**