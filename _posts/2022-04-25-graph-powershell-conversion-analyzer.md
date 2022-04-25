---
title: Graph PowerShell Conversion Analyzer
category: azuread
tags: []

---
![](/images/uploads/gps.png)

Hey folks, I took part in a hackathon last week and built the Graph PowerShell Conversion Analyzer. Hopefully, this will help a bit as you upgrade your AzureAD & MSOnline PowerShell scripts to Graph PowerShell.

It's very rough right now but I would love to hear your feedback.

Try it out at [**https://graphpowershell.merill.net**](https://graphpowershell.merill.net "https://graphpowershell.merill.net")

You start by pasting in one of your old scripts that you want to upgrade to Graph PowerShell and clicking the **Analyze** button.

This will generate a report of all the Azure AD PowerShell and MSOnline commands that were found along with a mapping to its corresponding Graph PowerShell command. The sample generated will try to map the parameters to the new command.

This is where I still need to do a lot more work to make it really useful.

![Screenshot of report generated when you click Analyze](https://media-exp1.licdn.com/dms/image/C5612AQEhF3NfXn-MIg/article-inline_image-shrink_1000_1488/0/1650874164692?e=2147483647&v=beta&t=sa5vS3USargkGv3Rt_5bSkZIuphUctcJbyqEuRhy4_I)

Where possible you also get direct links to both the Graph PowerShell command reference as well as the Graph API reference (which usually has more relevant info).

No more hunting around and searching the docs!

![Screenshot showing links to the Graph PowerShell and API docs](https://media-exp1.licdn.com/dms/image/C5612AQHcLRKuVJXhkA/article-inline_image-shrink_1500_2232/0/1650874247675?e=2147483647&v=beta&t=8VY0tZwNBLk3y5tApKFE3NiLnVkHOJp1cWl65Diu8w4)

The last bit is where you the community can really help us and each other out. We've started an open repository of sample Graph PowerShell scripts at [**https://aka.ms/graphsamples**](https://aka.ms/graphsamples "https://aka.ms/graphsamples")

We would love to make this the largest collection of Graph PowerShell sample scripts. It's open to everyone to contribute so please share your scripts (even one-liners).

![Screenshot of the Graph API samples library](https://media-exp1.licdn.com/dms/image/C5612AQH7yRTK3zG8zw/article-inline_image-shrink_1000_1488/0/1650874388214?e=2147483647&v=beta&t=paRa4qUyOBXM-46lZP39jvqJu1MN1Kl-1sJiugZpqzE)

Let me know what you think. If you have any ideas on how this can be improved I'm all ears!