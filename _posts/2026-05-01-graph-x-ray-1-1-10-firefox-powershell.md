---
title: "Graph X-Ray 1.1.10: Firefox support, better PowerShell generation, and a sharper DevTools experience"
description: "Graph X-Ray 1.1.10 adds Firefox support, Invoke-MgGraphRequest PowerShell generation, REST mode, filtering, batch improvements, and broader admin portal coverage."
date: 2026-05-01T08:00:00.000Z
preview: ""
tags: []
categories: []
---

Graph X-Ray has always had one simple goal: make Microsoft Graph easier to learn, inspect, and automate. Open the Microsoft admin portal, perform the action you care about, and Graph X-Ray shows you the Graph calls happening behind the scenes so you can turn those clicks into code.

With the 1.1.10 release, Graph X-Ray takes a big step forward. The headline feature is Firefox support, which means Graph X-Ray is now available across Microsoft Edge, Google Chrome, and Mozilla Firefox. This release also adds a new PowerShell generation path based on `Invoke-MgGraphRequest`, improves reliability when the upstream snippet service has issues, adds filtering and request counts to the DevTools panel, expands portal coverage, and formally moves the project under the AGPL-3.0 license.

Install Graph X-Ray from [graphxray.merill.net](https://graphxray.merill.net/) or head straight to the browser stores:

- [Microsoft Edge Add-ons](https://microsoftedge.microsoft.com/addons/detail/graph-xray/oplgganppgjhpihgciiifejplnnpodak)
- [Chrome Web Store](https://chrome.google.com/webstore/detail/graph-x-ray/gdhbldfajbedclijgcmmmobdbnjhnpdh)
- [Firefox Add-ons](https://addons.mozilla.org/en-US/firefox/addon/graph-xray/)

## Graph X-Ray now supports Firefox

The biggest update in this release is full Firefox support, contributed in large part by [Jorge Suarez (@jorgeasaurus)](https://github.com/jorgeasaurus) in [PR #4](https://github.com/merill/graphxray/pull/4).

This was more than a checkbox change. Firefox and Chromium-based browsers have meaningful differences in extension APIs, manifest support, background scripts, DevTools integration, and packaging requirements. Graph X-Ray now handles those differences cleanly with a Firefox-specific build and compatibility layer.

The result is simple for users: Graph X-Ray now works in Firefox. If Firefox is your daily browser, you no longer need to switch to Edge or Chrome just to inspect Microsoft Graph calls.

## PowerShell generation now has an `Invoke-MgGraphRequest` path

The second major improvement is PowerShell reliability.

Graph X-Ray has traditionally used Microsoft's DevX snippet API to generate language-specific snippets. That works well for many languages, but the PowerShell endpoint began returning failures, which meant PowerShell snippets could disappear even though Graph X-Ray had captured the request correctly. This was tracked in [issue #8](https://github.com/merill/graphxray/issues/8) and fixed through [PR #11](https://github.com/merill/graphxray/pull/11), again thanks to [@jorgeasaurus](https://github.com/jorgeasaurus).

Graph X-Ray now includes a local PowerShell snippet generator that uses `Invoke-MgGraphRequest` from the Microsoft Graph PowerShell SDK. That gives users a reliable fallback when the external snippet API is unavailable and also adds a dedicated PowerShell option for people who prefer the direct request style.

For example, a captured request can now become:

```powershell
Invoke-MgGraphRequest -Method GET -Uri "https://graph.microsoft.com/v1.0/me"
```

For requests with JSON bodies, Graph X-Ray builds a PowerShell hashtable and sends it as JSON:

```powershell
$params = @{
	"displayName" = "Test User"
	"accountEnabled" = $true
}

Invoke-MgGraphRequest -Method POST -Uri "https://graph.microsoft.com/v1.0/users" -Body ($params | ConvertTo-Json -Depth 10) -ContentType "application/json"
```

The generator handles nested objects, arrays, booleans, numbers, `$null`, string escaping, request bodies, and `ConsistencyLevel: eventual` for advanced query scenarios. PowerShell snippets also render immediately while Graph X-Ray attempts to upgrade to a server-generated snippet in the background when appropriate.

The new path makes Graph X-Ray less dependent on an external service and gives admins a snippet that is easy to understand, edit, and run.

## New REST mode for people who want the raw request

This release also adds a `REST` language option in the DevTools panel.

Sometimes you do not want a generated SDK sample. You just want the clean request URL so you can paste it into Graph Explorer, an HTTP file, a script, or your own tooling. REST mode returns the raw URL directly and gives batch sub-requests their own copyable REST entries.

That makes Graph X-Ray more useful as an inspection tool, not just a script generator.

## Filtering, counts, and a cleaner request view

As Graph X-Ray captures more traffic, especially in Microsoft admin portals that make several calls for a single UI action, the DevTools panel can fill up quickly. Version 1.1.10 adds a much better way to navigate that stream.

The request view now includes:

- A filter box for narrowing by URL.
- Method filters such as `GET`, `POST`, `PATCH`, and `DELETE`.
- Resource filters that group related Graph resources.
- Domain filters when Ultra X-Ray mode is enabled and multiple domains are present.
- Request counts showing the total captured requests and the filtered subset.
- Better handling for batch requests, including per-request filtering inside a batch.
- A collapsible batch execution snippet so individual request snippets stay easier to scan.
- Color-coded URL rendering for hosts, paths, query keys, and query values.

These changes make Graph X-Ray easier to use during real admin workflows. You can perform an action in Entra, Intune, Power Platform admin center, or another supported portal, then quickly narrow the captured requests to the exact call you need.

## Better batch request handling

Microsoft admin portals often use Graph batch requests. Those are efficient for the portal, but they can be harder for humans to inspect because several logical requests are wrapped in a single network call.

Graph X-Ray now does more work to make batch requests useful:

- Individual batch requests get their own generated snippets.
- Batch item URLs are normalized more reliably.
- Filtering works against the sub-requests inside a batch.
- REST mode can show each individual batch URL.
- The batch execution snippet is still available, but collapsed by default so it does not dominate the view.

That means a single captured batch can now be unpacked into the specific Microsoft Graph operations that matter for your automation.

## Expanded portal and cloud coverage

Graph X-Ray continues to support Microsoft Graph endpoints across Microsoft cloud environments:

- `graph.microsoft.com`
- `graph.microsoft.us`
- `dod-graph.microsoft.us`
- `microsoftgraph.chinacloudapi.cn`

This release also expands Ultra X-Ray coverage with additional admin portal domains, including:

- `admin.powerplatform.microsoft.com`
- `admin.cloud.microsoft`

These additions close community-reported gaps from [issue #7](https://github.com/merill/graphxray/issues/7) and [issue #9](https://github.com/merill/graphxray/issues/9), where users reported missing capture support for Microsoft 365 admin center Edge settings and Power Platform admin center activity.

Ultra X-Ray remains the place for non-Graph or internal admin API visibility, while the standard Graph X-Ray experience focuses on Microsoft Graph calls.

## Graph X-Ray is now AGPL-3.0 licensed

This release also formalizes the project license as [GNU Affero General Public License v3.0](https://github.com/merill/graphxray/blob/main/LICENSE), with package metadata set to `AGPL-3.0-only`. The licensing update was handled in [PR #12](https://github.com/merill/graphxray/pull/12).

Graph X-Ray remains free and open source, and the license now makes that explicit in the repository and package metadata.

## Thank you to the contributors

This release had several important contributions and community reports.

Special thanks to:

- [Jorge Suarez (@jorgeasaurus)](https://github.com/jorgeasaurus), who contributed the Firefox support work and the PowerShell reliability improvements.

And thank you to the community members who reported issues that shaped this release:

- [@WigF1](https://github.com/WigF1), who reported that PowerShell snippets were not appearing.
- [@tlourey](https://github.com/tlourey), who reported missing capture support for Edge settings in the Microsoft 365 admin center.
- [@askaresh](https://github.com/askaresh), who requested Power Platform admin center support.

## Try the new release

If you work with Microsoft 365, Entra, Intune, Power Platform, or Microsoft Graph automation, install the latest version of Graph X-Ray and try it in your browser of choice.

Open an admin portal, open DevTools, switch to the Graph X-Ray panel, perform the action you want to automate, and copy the generated request or script.

Graph X-Ray is here to help you answer the question every Microsoft 365 admin eventually asks:

What did that button actually do?

Install Graph X-Ray at [graphxray.merill.net](https://graphxray.merill.net/) or view the source on [GitHub](https://github.com/merill/graphxray).
