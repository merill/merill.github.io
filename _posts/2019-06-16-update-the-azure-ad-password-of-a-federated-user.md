---

published: true
title: Update the Azure AD password of a federated user
---
There are times you need to update the Azure AD password of a user that's synced from Active Directory. However running either Set-AzureADUserPassword or Set-MsolUserPassword fails with one of the following errors.

- Set-MsolUserPassword : You cannot reset a password for a federated user.
- Set-AzureADUserPassword : Error occurred while executing SetUser Code: Request_BadRequest

There is a simple hack to workaround this limitation. All you need to do is temporarily change the user's UserPrincipalName to that of a managed domain, update the password and then change the UserPrincipalName back to the federated domain.

	# Change UPN to managed domain
    Set-AzureADUser -ObjectId xxxxx -UserPrincipalName user@domain.onmicrosoft.com
    
    # Update the password
    Set-AzureADUserPassword -ObjectId xxxxx
    
    # Change UPN back to the federated domain
    Set-AzureADUser -ObjectId xxxxx -UserPrincipalName user@domain.com

That's it. The user will eventually be signed out of the apps they are in and will have to re-sign in again. 

The new password will remain until the user changes their password on-prem in Active Directory which will then sync across to Azure Active Directory.
