---
title: Azure AD Nudge (Authenticator registration campaign) failing to prompt users
category: Tips
tags: []
date: 2022-04-15 20:27:52 +0000
---
Getting users to go to the [aka.ms/mysecurityinfo]() page and set up the Authenticator app for MFA is not an easy task.

Azure AD's 'Nudge' feature allows you to run a [Microsoft Authenticator registration campaign](https://docs.microsoft.com/en-us/azure/active-directory/authentication/how-to-mfa-registration-campaign) that interrupts a user signing in with SMS and nudges them to set up the Authenticator app.

![](https://merill.net/images/uploads/improveyoursignin.png)

If you set this up but are not seeing users being nudged/prompted with the 'Improve your sign-ins' message its most probably because you have a conditional access policy for the 'Register security information' page.

![](https://merill.net/images/uploads/securityinfo.png)

The nudge screen will not be displayed if a user’s sign in is in scope of a conditional access policy that blocks access to the "Register security information" page.

Let's take for example you have a conditional access policy that blocks users from accessing the 'Register security information' page over the internet and limits access to your company's corporate (local area network).

When a user tries signing in over the internet and uses SMS they will not be shown the nudge (Improve your sign-ins) screen. 

Let's say for arguments sake if Azure AD were to send them to the page where they can set up security info. If we allowed the user to set up new auth methods it would bypass your conditional access policy defined above. Alternatively, it wouldn't be a pleasant experience if we redirected the user to the nudge screen and then showed them a CA policy error when they tried to set up a new auth method.

Instead, we simply avoid showing the nudge prompt if the current sign-in is not in scope for the 'Register security info' conditional access policy.

Hope that makes sense.