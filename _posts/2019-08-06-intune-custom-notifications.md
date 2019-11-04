---
title: Intune Custom Notifications
---
Google recently released the details of some [major iOS security flaws](https://www.theverge.com/2019/7/30/20746827/apple-ios-security-flaw-imessage-google-project-zero). The good thing is that Apple already released the patch for five of them in the iOS 12.4 update a few weeks ago. The bad thing is that more than 90% of our corporate user base did not have the update applied.

This is a brilliant opportunity to use Intune's new [Custom Notifications](https://docs.microsoft.com/en-us/intune/custom-notifications) feature to target and notify just the devices that haven't yet updated to the latest version.

To do this you start by creating a dynamic group in Azure AD using the 'Dynamic Devices' option.
The query for the group is fairly simple and goes like this

    (device.deviceOSType -in ["iOS","IPhone", "IPad", "IPod"]) -and (device.deviceOSVersion -ne "12.4")

![Dynamic membership rule]({{site.baseurl}}/assets/2019-08-06_22h04_08.png)

Wait for the group to be populated (might take anywhere from a few minutes to an hour or more depending on how many devices you have in your Azure AD).

Next go to Intune >  Devices > Send custom notifications to compose and send out the notifications to your users. You can keep sending this everyday and since this is just a dynamic group it will target the remaining devices that haven't been updated.

![Intune custom notifications]({{site.baseurl}}/assets/2019-08-06_22h09_49.png)
