---
title: Merill Fernando
permalink: /
hidden: true
---

<style>
.page__content .home-page {
  max-width: none;
}
.page__inner-wrap > header {
  display: none;
}
.project-section {
  margin-bottom: 3rem;
}
.project-section h2 {
  margin: 0 0 1rem;
  font-size: 1.15rem;
  font-weight: 750;
  letter-spacing: -0.025em;
  border: 0;
}
.project-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 1px;
  overflow: hidden;
  margin-bottom: 1rem;
  border: 1px solid var(--home-border, #e5eaf1);
  border-radius: 18px;
  background: var(--home-border, #e5eaf1);
}
@media (min-width: 640px) {
  .project-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}
@media (min-width: 1024px) {
  .project-grid {
    grid-template-columns: repeat(3, 1fr);
  }
}
.project-card {
  position: relative;
  display: flex;
  align-items: flex-start;
  gap: 0.9rem;
  min-height: 150px;
  padding: 1.15rem;
  border: 0;
  border-radius: 0;
  background: var(--home-card, #fff);
  transition: background-color 0.15s ease, transform 0.15s ease;
  text-decoration: none;
  color: inherit;
}
.project-card:hover {
  background: var(--home-card-hover, #f7f9fc);
  transform: translateY(-1px);
  text-decoration: none;
}
.project-card-logo {
  flex-shrink: 0;
  width: 42px;
  height: 42px;
  display: flex;
  align-items: center;
  justify-content: center;
}
.project-card-logo img {
  max-width: 42px;
  max-height: 42px;
  border-radius: 9px;
  object-fit: contain;
}
.project-card-logo .fa-icon-fallback {
  font-size: 1.25rem;
  color: #334155;
  width: 42px;
  height: 42px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #eef4ff;
  border-radius: 9px;
}
.project-card-body {
  flex: 1;
  min-width: 0;
}
.project-card-body h3 {
  margin: 0 0 0.35rem 0;
  font-size: 0.98rem;
  font-weight: 700;
  line-height: 1.25;
  letter-spacing: -0.015em;
}
.project-card-body h3 a {
  color: var(--home-text, #172033);
  text-decoration: none;
}
.project-card-body h3 a:hover {
  color: #2563eb;
  text-decoration: none;
}
.project-card-body h3 a::after {
  content: "";
  position: absolute;
  inset: 0;
}
.project-card-body p {
  margin: 0;
  font-size: 0.82rem;
  color: var(--home-muted, #5b677a);
  line-height: 1.5;
}
.project-card-stat {
  display: inline-block;
  font-size: 0.72rem;
  font-weight: 600;
  color: #1d4ed8;
  background: #eff6ff;
  padding: 0.18rem 0.45rem;
  border-radius: 999px;
  margin-top: 0.55rem;
}
.project-card-stat + .project-card-stat {
  margin-left: 0.35rem;
}
.home-hero {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 2rem;
}
.home-hero-copy {
  min-width: 0;
}
.home-hero-logo {
  flex: 0 0 auto;
  width: min(28vw, 210px);
  max-width: 210px;
  border-radius: 24px;
  filter: drop-shadow(0 18px 35px rgba(15, 23, 42, 0.16));
}
@media (max-width: 640px) {
  .home-hero {
    align-items: flex-start;
    flex-direction: column-reverse;
  }
  .home-hero-logo {
    width: 96px;
    border-radius: 18px;
  }
}
</style>

<div class="home-page">

<section class="home-hero">
  <div class="home-hero-copy">
    <p class="home-eyebrow">Microsoft AI, Security, Graph, and community tools</p>
    <h1 class="home-title">Hi, I'm Merill.</h1>
    <p class="home-intro">I build practical tools, share about Microsoft AI, Security, Entra and Graph, and share resources for admins, developers, and security teams.</p>
  </div>
  <img class="home-hero-logo" src="/assets/images/projects/msailogo.png" alt="Microsoft AI logo">
</section>

<div class="project-section">
<h2>Writing & Talks</h2>
<div class="project-grid">

  <div class="project-card">
    <div class="project-card-logo">
      <img src="/assets/images/projects/blog.svg" alt="My Personal Blog logo">
    </div>
    <div class="project-card-body">
      <h3><a href="/blog/">My Personal Blog</a></h3>
      <p>My random thoughts and an archive of everything I post on social media.</p>
    </div>
  </div>

  <div class="project-card">
    <div class="project-card-logo">
      <img src="/assets/images/projects/entranews.png" alt="Entra.News logo">
    </div>
    <div class="project-card-body">
      <h3><a href="https://entra.news">Entra.News</a></h3>
      <p>My weekly newsletter for Microsoft admins and cybersecurity folks on the latest in Microsoft Entra.</p>
      <span class="project-card-stat">18k readers</span>
    </div>
  </div>

  <div class="project-card">
    <div class="project-card-logo">
      <img src="/assets/images/projects/entrachat.png" alt="Entra.Chat logo">
    </div>
    <div class="project-card-body">
      <h3><a href="https://entra.chat">Entra.Chat</a></h3>
      <p>My weekly podcast on Microsoft Entra covering the latest news, features, and best practices.</p>
      <span class="project-card-stat">8k listeners</span>
    </div>
  </div>

</div>
</div>

<div class="project-section">
<h2>Community Tools</h2>
<div class="project-grid">

  <div class="project-card">
    <div class="project-card-logo">
      <img src="/assets/images/projects/maester.svg" alt="Maester logo">
    </div>
    <div class="project-card-body">
      <h3><a href="https://maester.dev">Maester</a></h3>
      <p>Open source Microsoft test automation framework and security analyzer for your tenant.</p>
      {%- assign s = site.data.stats.psgallery.Maester -%}
      {%- if s.display -%}<span class="project-card-stat">{{ s.display }} installs</span>{%- endif -%}
      {%- assign cf = site.data.stats.cloudflare["maester.dev"] -%}
      {%- if cf.display -%}<span class="project-card-stat">{{ cf.display }} monthly visits</span>{%- endif -%}
    </div>
  </div>

  <div class="project-card">
    <div class="project-card-logo">
      <img src="/assets/images/projects/cmdms.svg" alt="cmd.ms logo">
    </div>
    <div class="project-card-body">
      <h3><a href="https://cmd.ms">cmd.ms</a></h3>
      <p>Your Microsoft Cloud command line. Quick shortcuts to jump to any admin portal or documentation page.</p>
      {%- assign cf = site.data.stats.cloudflare["cmd.ms"] -%}
      {%- if cf.display -%}<span class="project-card-stat">{{ cf.display }} monthly visits</span>{%- endif -%}
    </div>
  </div>

  <div class="project-card">
    <div class="project-card-logo">
      <img src="/assets/images/projects/yako.png" alt="Yako logo">
    </div>
    <div class="project-card-body">
      <h3><a href="https://getyako.com">Yako</a></h3>
      <p>A beautiful browser start page for Microsoft users and admins. Instantly access 900+ Microsoft portals from your new tab.</p>
      {%- assign cf = site.data.stats.cloudflare["getyako.com"] -%}
      {%- if cf.display -%}<span class="project-card-stat">{{ cf.display }} monthly visits</span>{%- endif -%}
    </div>
  </div>

  <div class="project-card">
    <div class="project-card-logo">
      <img src="/assets/images/projects/mc-merill.ico" alt="M365 Message Center &amp; Roadmap Archive logo">
    </div>
    <div class="project-card-body">
      <h3><a href="https://mc.merill.net">M365 Message Center &amp; Roadmap Archive</a></h3>
      <p>Searchable archive of Microsoft 365 Message Center posts and Roadmap updates.</p>
    </div>
  </div>

  <div class="project-card">
    <div class="project-card-logo">
      <img src="/assets/images/projects/github-favicon.svg" alt="Refined Microsoft Learn logo">
    </div>
    <div class="project-card-body">
      <h3><a href="https://github.com/merill/refined-microsoft-learn">Refined Microsoft Learn</a></h3>
      <p>Browser extension to make Microsoft Learn distraction free and help you focus on the content.</p>
    </div>
  </div>

  <div class="project-card">
    <div class="project-card-logo">
      <img src="/assets/images/projects/bluesky-ms.ico" alt="bluesky.ms logo">
    </div>
    <div class="project-card-body">
      <h3><a href="https://bluesky.ms">bluesky.ms</a></h3>
      <p>Discover Microsoft folks on Bluesky. Find and connect with the Microsoft community.</p>
      {%- assign cf = site.data.stats.cloudflare["bluesky.ms"] -%}
      {%- if cf.display -%}<span class="project-card-stat">{{ cf.display }} monthly visits</span>{%- endif -%}
    </div>
  </div>

  <div class="project-card">
    <div class="project-card-logo">
      <img src="/assets/images/projects/cybersecpods.png" alt="CyberSecPods logo">
    </div>
    <div class="project-card-body">
      <h3><a href="https://cybersecpods.com">CyberSecPods</a></h3>
      <p>The home of cybersecurity podcasts. Curated shows on threat intel, identity, cloud security, red team, blue team, and more.</p>
      {%- assign cf = site.data.stats.cloudflare["cybersecpods.com"] -%}
      {%- if cf.display -%}<span class="project-card-stat">{{ cf.display }} monthly visits</span>{%- endif -%}
    </div>
  </div>

</div>
</div>

<div class="project-section">
<h2>AI Skills</h2>
<div class="project-grid">

  <div class="project-card">
    <div class="project-card-logo">
      <img src="/assets/images/projects/graphpm.svg" alt="Microsoft Graph skill logo">
    </div>
    <div class="project-card-body">
      <h3><a href="https://skills.sh/merill/msgraph/msgraph">Microsoft Graph</a></h3>
      <p>Agent skill to search, look up, and call any of the 27,700+ Microsoft Graph APIs locally with no network calls.</p>
    </div>
  </div>

  <div class="project-card">
    <div class="project-card-logo">
      <img src="/assets/images/projects/mc-merill.ico" alt="M365 Message Center skill logo">
    </div>
    <div class="project-card-body">
      <h3><a href="https://skills.sh/merill/mc/microsoft-365-message-center-archive">M365 Message Center</a></h3>
      <p>Agent skill to search, summarize, and cite Microsoft 365 Message Center messages and Microsoft 365 Roadmap posts.</p>
    </div>
  </div>

</div>
</div>

<div class="project-section">
<h2>Microsoft Graph Tools</h2>
<div class="project-grid">

  <div class="project-card">
    <div class="project-card-logo">
      <img src="/assets/images/projects/graphxray.svg" alt="Graph X-Ray logo">
    </div>
    <div class="project-card-body">
      <h3><a href="https://graphxray.merill.net">Graph X-Ray</a></h3>
      <p>Fiddler for Microsoft! Convert your actions in the Azure Portal to Graph PowerShell commands.</p>
      <span class="project-card-stat">19k monthly active users</span>
    </div>
  </div>

  <div class="project-card">
    <div class="project-card-logo">
      <img src="/assets/images/projects/lokka.svg" alt="Lokka logo">
    </div>
    <div class="project-card-body">
      <h3><a href="https://lokka.dev">lokka.dev</a></h3>
      <p>An AI agent tool that brings the power of Microsoft Graph to AI agents and LLMs.</p>
      {%- assign cf = site.data.stats.cloudflare["lokka.dev"] -%}
      {%- if cf.display -%}<span class="project-card-stat">{{ cf.display }} monthly visits</span>{%- endif -%}
    </div>
  </div>

  <div class="project-card">
    <div class="project-card-logo">
      <img src="/assets/images/projects/graphpm.svg" alt="graph.pm logo">
    </div>
    <div class="project-card-body">
      <h3><a href="https://graph.pm">graph.pm</a></h3>
      <p>Microsoft Graph Skill for AI agents. Search 27,700+ Graph APIs and curated samples locally, in milliseconds.</p>
      {%- assign cf = site.data.stats.cloudflare["graph.pm"] -%}
      {%- if cf.display -%}<span class="project-card-stat">{{ cf.display }} monthly visits</span>{%- endif -%}
    </div>
  </div>

  <div class="project-card">
    <div class="project-card-logo">
      <img src="/assets/images/projects/graphpermissions.svg" alt="Graph Permissions Explorer logo">
    </div>
    <div class="project-card-body">
      <h3><a href="https://graphpermissions.merill.net">Graph Permissions Explorer</a></h3>
      <p>Browse all Microsoft Graph APIs and see exactly what data is exposed for each Graph Permission.</p>
      {%- assign cf = site.data.stats.cloudflare["graphpermissions.merill.net"] -%}
      {%- if cf.display -%}<span class="project-card-stat">{{ cf.display }} monthly visits</span>{%- endif -%}
    </div>
  </div>

  <div class="project-card">
    <div class="project-card-logo">
      <img src="/assets/images/projects/uninstall-graph.png" alt="Uninstall-Graph logo">
    </div>
    <div class="project-card-body">
      <h3><a href="https://uninstall-graph.merill.net">Uninstall-Graph</a></h3>
      <p>PowerShell module that completely uninstalls and removes all Microsoft Graph PowerShell modules from your system.</p>
      {%- assign s = site.data.stats.psgallery["Uninstall-Graph"] -%}
      {%- if s.display -%}<span class="project-card-stat">{{ s.display }} installs</span>{%- endif -%}
    </div>
  </div>

  <div class="project-card">
    <div class="project-card-logo">
      <img src="/assets/images/projects/vscodemcp.svg" alt="VS Code MCP Install Button Generator logo">
    </div>
    <div class="project-card-body">
      <h3><a href="https://vscodemcp.com">VS Code MCP Install Button Generator</a></h3>
      <p>Create one-click VS Code install badges and links for Model Context Protocol servers.</p>
      {%- assign cf = site.data.stats.cloudflare["vscodemcp.com"] -%}
      {%- if cf.display -%}<span class="project-card-stat">{{ cf.display }} monthly visits</span>{%- endif -%}
    </div>
  </div>

</div>
</div>

<div class="project-section">
<h2>Microsoft Entra Tools</h2>
<div class="project-grid">

  <div class="project-card">
    <div class="project-card-logo">
      <img src="/assets/images/projects/idpowertoys.png" alt="idPowerToys logo">
    </div>
    <div class="project-card-body">
      <h3><a href="https://idPowerToys.merill.net">idPowerToys</a></h3>
      <p>Microsoft Entra Conditional Access visualizer. Understand and troubleshoot your CA policies.</p>
    </div>
  </div>

  <div class="project-card">
    <div class="project-card-logo">
      <img src="/assets/images/projects/signin-merill.svg" alt="Entra Sign-in URL Builder logo">
    </div>
    <div class="project-card-body">
      <h3><a href="https://signin.merill.net">Entra Sign-in URL Builder</a></h3>
      <p>Generate Microsoft Entra OAuth 2.0 authorization and admin consent URLs.</p>
    </div>
  </div>

  <div class="project-card">
    <div class="project-card-logo">
      <img src="/assets/images/projects/github-favicon.svg" alt="aka.ms/AppNames logo">
    </div>
    <div class="project-card-body">
      <h3><a href="https://aka.ms/AppNames">aka.ms/AppNames</a></h3>
      <p>Repository hosting a daily updated CSV/JSON of Microsoft first party app names and their GUIDs.</p>
    </div>
  </div>

</div>
</div>

<div class="project-section">
<h2>Microsoft Contributions</h2>
<div class="project-grid">

  <div class="project-card">
    <div class="project-card-logo">
      <img src="/assets/images/projects/zerotrust.svg" alt="Zero Trust Workshop logo">
    </div>
    <div class="project-card-body">
      <h3><a href="https://aka.ms/ztworkshop">Zero Trust Workshop</a></h3>
      <p>A workshop to help organizations understand and implement Zero Trust principles using Microsoft Security solutions.</p>
    </div>
  </div>

  <div class="project-card">
    <div class="project-card-logo">
      <img src="/assets/images/projects/zerotrustexplorer.svg" alt="Zero Trust Explorer logo">
    </div>
    <div class="project-card-body">
      <h3><a href="https://zerotrustexplorer.merill.net">Zero Trust Explorer</a></h3>
      <p>Interactive explorer for the Microsoft Zero Trust framework. Visualize and navigate Zero Trust architecture and controls.</p>
    </div>
  </div>

  <div class="project-card">
    <div class="project-card-logo">
      <img src="/assets/images/projects/github-favicon.svg" alt="Zero Trust Assessment logo">
    </div>
    <div class="project-card-body">
      <h3><a href="https://github.com/microsoft/zerotrustassessment/">Zero Trust Assessment</a></h3>
      <p>PowerShell module that checks your tenant configuration and recommends ways to improve the security configuration.</p>
      {%- assign s = site.data.stats.psgallery.ZeroTrustAssessment -%}
      {%- if s.display -%}<span class="project-card-stat">{{ s.display }} installs</span>{%- endif -%}
    </div>
  </div>

  <div class="project-card">
    <div class="project-card-logo">
      <img src="/assets/images/projects/github-favicon.svg" alt="Entra Exporter logo">
    </div>
    <div class="project-card-body">
      <h3><a href="https://github.com/microsoft/EntraExporter">Entra Exporter</a></h3>
      <p>PowerShell module that exports all the configuration and data of a Microsoft Entra tenant.</p>
      {%- assign s = site.data.stats.psgallery.EntraExporter -%}
      {%- if s.display -%}<span class="project-card-stat">{{ s.display }} installs</span>{%- endif -%}
    </div>
  </div>

  <div class="project-card">
    <div class="project-card-logo">
      <img src="/assets/images/projects/msidentitytools.ico" alt="MSIdentityTools logo">
    </div>
    <div class="project-card-body">
      <h3><a href="https://aka.ms/msid">MSIdentityTools</a></h3>
      <p>Collection of useful PowerShell cmdlets for common Azure AD and Microsoft Entra functionality.</p>
      {%- assign s = site.data.stats.psgallery.MSIdentityTools -%}
      {%- if s.display -%}<span class="project-card-stat">{{ s.display }} installs</span>{%- endif -%}
    </div>
  </div>

</div>
</div>

</div>
