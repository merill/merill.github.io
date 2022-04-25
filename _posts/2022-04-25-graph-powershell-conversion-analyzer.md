---
title: Graph PowerShell Conversion Analyzer
category: azuread
tags: []

---
![Screenshot of Graph PowerShell Analyzer](/images/uploads/gps.png "https://graphpowershell.merill.net")

Hey folks, I took part in a hackathon last week and built the Graph PowerShell Conversion Analyzer. Hopefully, this will help a bit as you upgrade your AzureAD & MSOnline PowerShell scripts to Graph PowerShell.

It's very rough right now but I would love to hear your feedback.

Try it out at [**https://graphpowershell.merill.net**](https://graphpowershell.merill.net "https://graphpowershell.merill.net")

You start by pasting in one of your old scripts that you want to upgrade to Graph PowerShell and clicking the **Analyze** button.

This will generate a report of all the Azure AD PowerShell and MSOnline commands that were found along with a mapping to its corresponding Graph PowerShell command. The sample generated will try to map the parameters to the new command.

This is where I still need to do a lot more work to make it really useful.

![Screenshot of Analysis Report](/images/uploads/fq97krbaiaeof-i.jpeg)

Where possible you also get direct links to both the Graph PowerShell command reference as well as the Graph API reference (which usually has more relevant info).

No more hunting around and searching the docs!

![Screenshot showing links to the docs](/images/uploads/fq99di3auaas7g.jpeg)

The last bit is where you the community can really help us and each other out. We've started an open repository of sample Graph PowerShell scripts at [**https://aka.ms/graphsamples**](https://aka.ms/graphsamples "https://aka.ms/graphsamples")

We would love to make this the largest collection of Graph PowerShell sample scripts. It's open to everyone to contribute so please share your scripts (even one-liners).

![Screenshot of the Graph samples community](/images/uploads/fq99wh1aiairqhi.jpeg)

Let me know what you think. If you have any ideas on how this can be improved I'm all ears!