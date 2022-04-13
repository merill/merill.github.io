---
title: Parsing the Azure AD federationmetadata.xml in PowerShell
category: Tips
tags:
- powershell
- azuread

---
If you try to parse Azure AD's federation metadata xml in PowerShell using a script like the one below you most probably end up with the error "The specified node cannot be inserted as the valid child of this node, because the specified node is the wrong
type."

```powershell
$tenantId = "49dfc6a3-5fb7-49f4-adea-c54e725bb854"
$fedMetadataURI = "https://login.microsoftonline.com/$tenantId/federationmetadata/2007-06/federationmetadata.xml"
$xml = [xml] (Invoke-WebRequest -URI $fedMetadataURI).Content
```
I didn't have time to figure out the root cause but I was able to hack my way around the issue by writing the content to disk and then reading it.

```powershell
$tenantId = "49dfc6a3-5fb7-49f4-adea-c54e725bb854"
$fedMetadataURI = "https://login.microsoftonline.com/$tenantId/federationmetadata/2007-06/federationmetadata.xml"
$tempFile = "./fed.xml"
(Invoke-WebRequest -URI $fedMetadataURI).Content | Set-Content $tempFile
$xml = [xml] (Get-Content $tempFile)
Remove-Item $tempFile
```

I'm pretty sure it's related to encoding, if you figure it out let me know.