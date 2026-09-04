---
title: About Merill Fernando
permalink: /about/
excerpt: "Founder of Jozra, creator of Maester, ex-Microsoft Entra PM and the #1 Entra fan. Here is who I am and what I build."
hide: true
---

<style>
.page__content .about-page {
  max-width: none;
}
.page__inner-wrap > header {
  display: none;
}
</style>

<div class="about-page">

<section class="about-hero">
  <div class="about-hero-copy">
    <p class="about-eyebrow">Founder · Builder · #1 Entra fan</p>
    <h1>I make Microsoft security practical.</h1>
    <p class="about-lede">I’m Merill Fernando. I spent years inside Microsoft as a Product Manager on Entra, helping the world’s largest organisations secure identity. In 2026 I left to found <a href="https://jozra.com">Jozra</a> and work full time on <a href="https://maester.dev">Maester</a>, the open source project tens of thousands of tenants rely on to keep Microsoft 365 secure.</p>
    <ul class="about-facts" aria-label="Quick facts">
      <li><i class="fas fa-fw fa-map-marker-alt" aria-hidden="true"></i>Melbourne, Australia</li>
      <li><i class="fas fa-fw fa-briefcase" aria-hidden="true"></i>Ex-Microsoft Entra PM</li>
      <li><i class="fas fa-fw fa-rocket" aria-hidden="true"></i>Founder, Jozra</li>
      <li><i class="fas fa-fw fa-pen-nib" aria-hidden="true"></i>Blogging since 2003</li>
    </ul>
    <p class="about-links"><a href="https://www.linkedin.com/in/merill"><i class="fab fa-fw fa-linkedin" aria-hidden="true"></i> LinkedIn</a><a href="https://x.com/merill"><i class="fab fa-fw fa-x-twitter" aria-hidden="true"></i> X</a><a href="https://www.youtube.com/@merillx"><i class="fab fa-fw fa-youtube" aria-hidden="true"></i> YouTube</a><a href="https://github.com/merill"><i class="fab fa-fw fa-github" aria-hidden="true"></i> GitHub</a></p>
  </div>
  <img class="about-portrait" src="/assets/images/merill-profile.png" alt="Merill Fernando">
</section>

<section class="about-stats" aria-label="Reach">
  <div><strong>53K</strong><span>LinkedIn followers</span></div>
  <div><strong>21K</strong><span>X followers</span></div>
  <div><strong>19K</strong><span>Entra.News subscribers</span></div>
  <div><strong>8K</strong><span>Entra.Chat listeners</span></div>
  <div><strong>60K+</strong><span>tenants running Maester</span></div>
</section>

<section class="about-story">
  <div class="about-story-copy">
    <p class="about-eyebrow">The short version</p>
    <h2>Twenty years of building things for the Microsoft community</h2>
    <p>I grew up in Sri Lanka, where the best tools were usually priced for someone else. I started this blog in 2003, was awarded Microsoft MVP in 2004, and built the Sri Lanka .NET User Group into one of the largest in the country. The habit of building things and giving them away never left.</p>
    <p>At Microsoft I was a Principal Product Manager in the Entra product group. I worked directly with some of Microsoft’s biggest customers on identity strategy and deployment, then carried what I learned back to the engineering teams. Along the way I shipped Entra External Authentication Methods and Entra PowerShell, and co-created the <a href="https://learn.microsoft.com/en-us/security/zero-trust/assessment/overview">Zero Trust Assessment</a> and the <a href="https://aka.ms/entra/security">Entra Security Hardening guide</a>.</p>
    <p>In 2026 I left to start Jozra, an independent Australian company that builds tools for the people who keep Microsoft 365 secure. Our first product is <a href="https://maester.cloud">Maester Cloud</a>, the evidence layer that sits on top of the open source framework. The deal is simple: the framework and its core tests stay free and open forever, and the paid services fund the work.</p>
  </div>
  <blockquote class="about-quote">
    <p>Security testing should be open, reusable, and available to everyone. Not just the teams with the biggest budgets.</p>
    <cite>From the <a href="https://maester.dev/manifesto/">Maester Manifesto</a></cite>
  </blockquote>
</section>

<section class="about-built">
  <div class="about-built-head">
    <div>
      <p class="about-eyebrow">What I’ve built</p>
      <h2>Ten things people actually use</h2>
    </div>
    <p>Free, practical tools for admins, developers, and security teams. Most are open source. All of them started as something I needed myself.</p>
  </div>

  <div class="about-built-grid">

    <a class="about-built-card" href="https://maester.dev">
      <img src="/assets/images/projects/maester.svg" alt="">
      <div>
        <h3>Maester</h3>
        <p>Open source test automation framework and security analyzer for Microsoft 365. Turns best practices into tests you can run every day.</p>
        <div class="about-built-stats">
          {%- assign s = site.data.stats.psgallery.Maester -%}
          {%- if s.display -%}<span>{{ s.display }} installs</span>{%- endif -%}
          {%- assign cf = site.data.stats.cloudflare["maester.dev"] -%}
          {%- if cf.display -%}<span>{{ cf.display }} monthly visits</span>{%- endif -%}
        </div>
      </div>
    </a>

    <a class="about-built-card" href="https://entra.news">
      <img src="/assets/images/projects/entranews.png" alt="">
      <div>
        <h3>Entra.News</h3>
        <p>The weekly briefing on Microsoft Entra for admins and security folks. Everything worth knowing, from Microsoft and the community, in one email.</p>
        <div class="about-built-stats"><span>19k subscribers</span><span>Free · Weekly</span></div>
      </div>
    </a>

    <a class="about-built-card" href="https://entra.chat">
      <img src="/assets/images/projects/entrachat.png" alt="">
      <div>
        <h3>Entra.Chat</h3>
        <p>My weekly podcast with the people who build and run Entra: Microsoft product managers and practitioners from IKEA, General Motors, McDonald’s and more.</p>
        <div class="about-built-stats"><span>8k listeners</span><span>New episode weekly</span></div>
      </div>
    </a>

    <a class="about-built-card" href="https://lokka.dev">
      <img src="/assets/images/projects/lokka.svg" alt="">
      <div>
        <h3>Lokka</h3>
        <p>The MCP server for Microsoft 365. Lets AI agents like Claude and GitHub Copilot query and manage your tenant through Microsoft Graph in plain language.</p>
        <div class="about-built-stats">
          {%- assign cf = site.data.stats.cloudflare["lokka.dev"] -%}
          {%- if cf.display -%}<span>{{ cf.display }} monthly visits</span>{%- endif -%}
          <span>Open source</span>
        </div>
      </div>
    </a>

    <a class="about-built-card" href="https://graphxray.merill.net">
      <img src="/assets/images/projects/graphxray.svg" alt="">
      <div>
        <h3>Graph X-Ray</h3>
        <p>Fiddler for Microsoft 365. A browser extension that watches what the admin portals do and hands you the Graph PowerShell to do it yourself.</p>
        <div class="about-built-stats"><span>19k monthly active users</span><span>Chrome · Edge · Firefox</span></div>
      </div>
    </a>

    <a class="about-built-card" href="https://graphpermissions.merill.net">
      <img src="/assets/images/projects/graphpermissions.svg" alt="">
      <div>
        <h3>Graph Permissions Explorer</h3>
        <p>Browse every Microsoft Graph API and see exactly what data each permission exposes before you grant it.</p>
        <div class="about-built-stats">
          {%- assign cf = site.data.stats.cloudflare["graphpermissions.merill.net"] -%}
          {%- if cf.display -%}<span>{{ cf.display }} monthly visits</span>{%- endif -%}
        </div>
      </div>
    </a>

    <a class="about-built-card" href="https://cmd.ms">
      <img src="/assets/images/projects/cmdms.svg" alt="">
      <div>
        <h3>cmd.ms</h3>
        <p>Your Microsoft Cloud command line. Type a shortcut, land on the right admin portal or docs page. No more bookmarks.</p>
        <div class="about-built-stats">
          {%- assign cf = site.data.stats.cloudflare["cmd.ms"] -%}
          {%- if cf.display -%}<span>{{ cf.display }} monthly visits</span>{%- endif -%}
        </div>
      </div>
    </a>

    <a class="about-built-card" href="https://aka.ms/msid">
      <img src="/assets/images/projects/msidentitytools.ico" alt="">
      <div>
        <h3>MSIdentityTools</h3>
        <p>PowerShell cmdlets for the everyday Entra tasks that Graph makes harder than they should be. Built at Microsoft, used everywhere.</p>
        <div class="about-built-stats">
          {%- assign s = site.data.stats.psgallery.MSIdentityTools -%}
          {%- if s.display -%}<span>{{ s.display }} installs</span>{%- endif -%}
        </div>
      </div>
    </a>

    <a class="about-built-card" href="https://github.com/microsoft/EntraExporter">
      <img src="/assets/images/projects/github-favicon.svg" alt="">
      <div>
        <h3>Entra Exporter</h3>
        <p>Export the entire configuration of a Microsoft Entra tenant to JSON so you can version it, diff it, and know what changed.</p>
        <div class="about-built-stats">
          {%- assign s = site.data.stats.psgallery.EntraExporter -%}
          {%- if s.display -%}<span>{{ s.display }} installs</span>{%- endif -%}
        </div>
      </div>
    </a>

    <a class="about-built-card" href="https://github.com/microsoft/zerotrustassessment/">
      <img src="/assets/images/projects/zerotrust.svg" alt="">
      <div>
        <h3>Zero Trust Assessment</h3>
        <p>Microsoft’s PowerShell module that checks your tenant against Zero Trust guidance and tells you what to fix first.</p>
        <div class="about-built-stats">
          {%- assign s = site.data.stats.psgallery.ZeroTrustAssessment -%}
          {%- if s.display -%}<span>{{ s.display }} installs</span>{%- endif -%}
        </div>
      </div>
    </a>

  </div>
  <p class="about-built-more"><a href="/">See everything I’ve built →</a></p>
</section>

<section class="about-two-column">
  <div>
    <p class="about-eyebrow">Writing &amp; conversations</p>
    <h2>Sharing what matters</h2>
    <p>Every week I publish <a href="https://entra.news">Entra.News</a> for 19,000 identity and security practitioners, and co-author <a href="https://msai.ms">MSAI Weekly</a>, a roundup of Microsoft AI news worth your time.</p>
    <p>On <a href="https://entra.chat">Entra.Chat</a> I talk with the people building and operating identity at scale, including <a href="https://entra.news/p/securing-a-global-giant-inside-ikeas">Martin Sandren from IKEA</a>, <a href="https://entra.news/p/how-general-motors-moved-200000-people">Andrew Cameron from General Motors</a>, and <a href="https://entra.news/p/entra-mcdonalds-managing-22-million">George Roberts from McDonald’s</a>.</p>
  </div>
  <div>
    <p class="about-eyebrow">Speaking</p>
    <h2>On stage, around the world</h2>
    <p>I speak at identity, security, and workplace conferences across the United States, Europe, and Australia. Recent stages include Workplace Ninjas, Experts Live Denmark, and the HIP Conference.</p>
    <p>My sessions are built to send people home with something they can do on Monday, whether they are new to Entra or running identity for hundreds of thousands of users. Want me at your event? <a href="https://sessionize.com/merill/">Find me on Sessionize</a>.</p>
  </div>
</section>

<section class="about-kudos">
  <div>
    <p class="about-eyebrow">From the community</p>
    <h2>Kind words I’m grateful for</h2>
    <p>“Many of us can learn from your impressive drive and always positive and welcoming attitude.”</p>
    <cite>Claus Jespersen, former Principal Consultant, Security at Microsoft</cite>
    <p>“Your content, insights, and especially your podcast have helped so many professionals better understand identity, Entra, and cybersecurity challenges in a practical and accessible way.”</p>
    <cite>Karl A., identity and security practitioner</cite>
  </div>
  <a class="about-kudos-link" href="https://kudos.merill.net/">
    <span>Explore the Kudos Wall</span>
    <strong>See more recommendations →</strong>
  </a>
</section>

<section class="about-connect">
  <p class="about-eyebrow">Let’s connect</p>
  <h2>Say hello</h2>
  <p>The fastest way to reach me is on <a href="https://www.linkedin.com/in/merill">LinkedIn</a> or <a href="https://x.com/merill">X</a>. Email works too: merill at merill.net.</p>
  <p class="about-signoff">Cheers,<br><a rel="me" href="https://infosec.exchange/@merill">Merill</a></p>
</section>

</div>
