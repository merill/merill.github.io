---
title: 'Get-MgUser_List1: Expect simple name=value query, but observe property ''assignedLicenses''
  of complex type ''AssignedLicense''.'
category: azuread
tags:
- powershell
- graph

---
You are trying to run PowerShell You get this error

    ❯ Get-MgUser -Filter 'assignedLicenses/$count eq 0'
    Get-MgUser_List1: Expect simple name=value query, but observe property 'assignedLicenses' of complex type 'AssignedLicense'.

The fix is quite simple.

    ❯ Get-MgUser -Filter 'assignedLicenses/$count eq 0' -ConsistencyLevel eventual -CountVariable licensedUserCount -All
    
    Id                                   DisplayName     Mail                           UserPrincipalName
    --                                   -----------     ----                           -----------------
    1468b68b-8536-4bc5-ab1f-6014175b836d merill-fdo      merill-fdo@yopmail.net         merill-fdo_yopmail.net#E…
    160f8064-a20c-4236-bdf4-3393003e916b Ez              ezra@fdo.net                   ezra_fdo.net#EXT#@pora.n…
    37e5a3d1-f92b-4a12-bb35-91bf80969810 user2 fake      user2@fakedomain.com           user2_fakedomain.com#EXT…
    5c8537e4-7d7f-4920-a921-382d91fa53fd Fake Domain     user@fakedomain.com            user_fakedomain.com#EXT#…
    640885de-9652-4fb2-8a87-963cc2f599a0 Chris Green     chris.green@yopmail.net        chris.green_yopmail.net#…