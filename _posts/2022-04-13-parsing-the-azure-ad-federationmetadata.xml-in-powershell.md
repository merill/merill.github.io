---
title: Parsing the Azure AD federationmetadata.xml in PowerShell
category: Tips
tags:
- powershell
- azuread

---

```powershell
$tenantId = "49dfc6a3-5fb7-49f4-adea-c54e725bb854"
$fedMetadataURI = "https://login.microsoftonline.com/$tenantId/federationmetadata/2007-06/federationmetadata.xml"
$xml = [xml] (Invoke-WebRequest -URI $fedMetadataURI).Content
```

If you try to parse the federation metadata xml in PowerShell using a script like the one above you most probably end up with the error "The specified node cannot be inserted as the valid child of this node, because the specified node is the wrong
type."

There seems to be an encoding issue and I really didn't have the time to investigate it.

A quick fix I found was to write to a file and then do the parse.

```powershell
$tenantId = "49dfc6a3-5fb7-49f4-adea-c54e725bb854"
$fedMetadataURI = "https://login.microsoftonline.com/$tenantId/federationmetadata/2007-06/federationmetadata.xml"
$tempFile = "./fed.xml"
(Invoke-WebRequest -URI $fedMetadataURI).Content | Set-Content $tempFile
$xml = [xml] (Get-Content $tempFile)
Remove-Item $tempFile
```