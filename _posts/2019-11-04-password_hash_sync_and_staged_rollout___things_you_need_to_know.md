---
layout: post
title: Password Hash Sync and Staged Rollout - Things you need to know

---
Now that Staged Rollout is out of NDA, I can finally talk about one of the projects I've been working on for the last twelve months.
 
**Why Staged Rollout?**

How do you migrate from an on-prem identity provider to using Azure AD as the authentication provider? Before Staged Rollout was available the only option was either big-bang where you switched the entire domain from federated to managed or you had to mess with the user's UPN and temporarily move them to a managed domain. Not very great options which basically meant it made the already difficult task an almost impossible one.

Thanks to Staged Rollout you can now migrate a few users at a time to native Azure AD authentication. The end result will be as simple as adding the users to an AAD group.

**Things to consider before doing a staged rollout with Password Hash Sync**

The documentation for [Password Hash Sync](https://docs.microsoft.com/en-us/azure/active-directory/hybrid/how-to-connect-password-hash-synchronization) and [Staged Rollout](https://docs.microsoft.com/en-us/azure/active-directory/hybrid/how-to-connect-staged-rollout) give a good overview of what you need to do as a bare minimum, however there are many things you need to consider or might run into when implementing this in the real world. I ran into most of these when turning on Password Hash Sync (PHS) but most of the guidance is equally applicable to Pass Through Authentication (PTA) as well.


## Tighten up your Conditional Access policies
Check your conditional access policies and make sure you've covered all the scenarios. At a minimum, make sure you have MFA as a requirement for any user access that comes in over the internet. 

## Block Legacy Authentication
You will also want to [block legacy authentication] (https://docs.microsoft.com/en-us/azure/active-directory/conditional-access/block-legacy-authentication). If not, you have opened the door for bad guys to run brute force attacks on your user passwords. A quick note that blocking legacy authentication will not break Exchange Active Sync sign ins (even though they use a form of basic auth). 
You might have issues blocking legacy authentication for users that are on the LAN/VPN, especially if you have robot accounts using EWS APIs, old Outlook clients, etc. At a minimum you should set up a CA policy to block legacy auth requests coming in over the internet.

![2019-11-01-437469.png](https://merill.net/assets/2019-11-01-437469.png)



## UPN Analysis
You should also do an analysis of the accounts that are being synced to Azure AD. What you might not be aware is that users having a UPN suffix (domain) that is not registered in Azure AD will end up with an @<tenantname>.onmicrosoft.com UPN in Azure AD.

In a federated world this might have been enough to block these users from signing into Azure AD but that's not true anymore once you sync the hashes. Users can type in their cloud UPN (e.g. name@mytenant.onmicrosoft.com)  and on-prem password and be signed into Azure AD.

There are a few ways you can go about address this, a combination of registering the domain in AAD, dynamic groups and conditional access will help you manage/block these accounts if they are not supposed to sign into Azure AD.

## Password Expiry
This is a big one and has an impact on user experience. By default the Azure AD password is set to 'Never Expire'. The result is that when a user's password has expired on-prem they will still be able to sign into Azure AD with the old password.
  
The issue stems from the fact that password expiry status is not a true/false flag that's stored against the user in Active Directory. Instead it's a calculated field based on the pwdLastSet attribute of the user + the password expiry policy that applied to the user. This is why there is no such attribute to configure in AAD Connect.
  
The good news is that the story is a lot better now (Nov 2019) than what is was a few months ago. What you need to do now is create a password policy in Azure AD that matches your on-prem policy (eg 90 day expiry). Then you need to do two things. 
  
The first is to turn on _EnforceCloudPasswordPolicyForPasswordSyncedUsers_ in AAD. This will ensure that going forward whenever a user resets the password, AAD Connect will set that user's password policy from _DisablePasswordExpiration_ to _None_.

```
Set-MsolDirSyncFeature -Feature EnforceCloudPasswordPolicyForPasswordSyncedUsers  $true
```

However this is not going to go and fix each user's account. To do that you need to set it for each individual user like this.

```
Set-AzureADUser -ObjectID <User Object ID> -PasswordPolicies "DisablePasswordExpiration"
```	

Now for the catch. If you try this on a federated user account, AAD will complain its a synced account and throw the error "Unable to update the specified properties for on-premises mastered Directory Sync objects or objects". Nothing that some simple PowerShell can't solve. All you have to do is switch the user's UPN to a managed domain, update the policy and switch the UPN back to the federated one. There is no impact to the user (they won't see any sign in prompts or weird behaviour). Remember to use the user's GUID as the ObjectId instead of the UPN since we are swapping the UPNs around. I also added the .x@ to the temporary managedUpn to avoid conflicts where some users 

```powershell
function SetPasswordPolicyNone($objectId, $upn)
{
    $upnSplit = $upn.Split("@")
    $tenantDomain = "<mytenantname>.onmicrosoft.com"
    
    $managedUpn = $upnSplit[0] + ".x@" + $tenantDomain
    # Change UPN to managed domain
    Write-Host "Update Policy: Updating " $upn " to " $managedUpn
    Set-AzureADUser -ObjectId $objectId -UserPrincipalName $managedUpn
    # Update the password policy
    Set-AzureADUser -ObjectId $objectId -PasswordPolicies DisablePasswordExpiration
    # Change UPN back to the federated domain
    Set-AzureADUser -ObjectId $objectId -UserPrincipalName $upn
}

$users = Import-Csv .\users.csv
foreach ($user in $users){
    Write-Host $user.userPrincipalName
    SetPasswordPolicyNone -upn $user.userPrincipalName -objectId $user.ObjectId
}
```
	
Now for some notes/warnings
- You should do some reporting to understand the current state of the user's password policies. This article has some helpful scripts to do this https://docs.microsoft.com/en-us/office365/admin/add-users/set-password-to-never-expire?view=o365-worldwide

- If you have some users or types of users on-prem that don't have a password expiry policy you will need to make sure you don't set their password policy to None. If you do it they will be prompted with the 'Change Password' flow in Azure AD even though their password has not expired on-prem. 

## CA Policy to Lockdown access to the Security info page
The [Security Info](https://docs.microsoft.com/en-us/azure/active-directory/user-help/security-info-setup-auth-app) page where your users can set up the MFA options is well protected by Microsoft once the user has set up an MFA option. Each time they access this page they will be prompted to perform an MFA.
  
However, the first time you add the user to the MFA group they will be able to access this page with just the username and password and sometimes this could be over the internet. My recommendation is to secure this page so that it is only accessible from a managed device (ie IsCompliant or Hybrid Joined) and to lock down un-managed devices to the LAN.
  
This way you can prevent intruders hijacking a user's account and setting up MFA between the window where you add them to PHS and the user first logging in. Steps to turn this on can be found here https://docs.microsoft.com/bs-latn-ba/azure/active-directory/authentication/howto-registration-mfa-sspr-combined#conditional-access-policies-for-combined-registration




![2019-11-01-842606.png](https://merill.net/assets/2019-11-01-842606.png)
![2019-11-01-718026.png](https://merill.net/assets/2019-11-01-718026.png)




## MFA configuration for end users
This is more about end user comms and planning. You need to figure out how you guide your users through the process of setting up MFA.

Microsoft has a good guide to set this up over https://docs.microsoft.com/en-us/azure/active-directory/authentication/howto-mfa-getstarted

You get the best end user experience if you are licenced for Identity Protection (currently AAD P2) since it guides the user through the MFA set up process as part of their initial sign in.

If you are not licenced you will need to roll your own and come up with a plan to migrate users. If you don't do anything then your users will be hit with the MFA set up process the first time a CA policy checks for it. Unfortunately for a vast majority of users this could be when they are signing in from a mobile device. Users are going to get stuck real fast on the mobile when it asks them to scan the QR code (displayed on the mobile phone) with the phone itself. To avoid this deadlock and very bad user experience you need to send out comms early to users and make sure they have set up their MFA.

Unfortunately, reporting on the MFA options set up by the user is still locked down to the old MSOL PowerShell module. 

This script will help create a report for you.

```	
Remove-Item $outputCsvPath
$result=@() 
$inputUserCsv | ForEach-Object {
    Write-Host $_.UserPrincipalName
    $user = Get-Msoluser -UserPrincipalName $_.UserPrincipalName
    $result = New-Object PSObject -property @{         
        UserPrincipalName = $user.UserPrincipalName
        UserName = $user.DisplayName
        MFADefault = ($user.StrongAuthenticationMethods | Where-Object IsDefault -eq True).MethodType
        MFAMethods = ($user.StrongAuthenticationMethods | ForEach-Object { $_.MethodType }) -join ", "
        ImmutableId = $user.ImmutableId
    }
    $result | Export-CSV $outputCsvPath -NoTypeInformation -Append
}
```


## Other titbits 
### Sites with domain hint 
Microsoft has a warning about sites with domain hint. Yes they will still redirect the user to the federated sign in page, however most users will rarely see this page. If they have a PRT token or they've signed in before it will take them to the cloud authentication flow. The rare occurrence where they might see this is if they are on a mobile device that doesn't have single sign on (eg. Safari).

### Do I need to implement Seamless SSO? 
If all the users you are migrating are on Windows 10 and AAD Hybrid Joined then Seamless Sign On does not add any benefit. You can skip it altogether. However if you are migrating Windows 7 users to PHS then yes you should set up Seamless SSO

### What should I set the Active Directory Service Connection Point to? 
It's better to have the SCP point to the <mytenant>.onmicrosoft.com domain instead of your custom domain to avoid DNS and proxy issues related to your tenant.
