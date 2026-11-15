---
title: Sponsor Merill
permalink: /sponsor/
layout: splash
author_profile: false
excerpt: "Maester, Lokka, idPowerToys, cmd.ms, Graph X-Ray and the rest are free and self-funded. Here are three ways to keep them going."
description: "Sponsor Merill Fernando's free, open source tools for the Microsoft community: GitHub Sponsors, Maester Cloud, or a company sponsorship of Maester."
---

<style>
/* Layout: dark Maester-ink hero with a mock Maester run, then a light page in the merill.net style. */
.sponsor-page {
  --sp-ink: #161617;
  --sp-ink-warm: #1f1012;
  --sp-ink-line: #3d2326;
  --sp-flame-1: #f6851f;
  --sp-flame-2: #ee3d3a;
  --sp-flame-3: #c8202b;
  --sp-red: #d22c31;
  --sp-navy: #0f2745;
  --sp-blue: #2563eb;
  --sp-text: #172033;
  --sp-muted: #5b677a;
  --sp-border: #e5eaf1;
  --sp-soft: #f7f9fc;
  --sp-pass: #4ade80;
  --sp-fail: #ff8a8d;
  --sp-flame: linear-gradient(160deg, var(--sp-flame-1) 0%, var(--sp-flame-2) 48%, var(--sp-flame-3) 100%);
  display: flex;
  flex-direction: column;
  gap: clamp(2.75rem, 6vw, 4.5rem);
  max-width: 1120px;
  margin: 0 auto 3.5rem;
  color: var(--sp-text);
}
.sponsor-page h1,
.sponsor-page h2,
.sponsor-page h3 {
  margin: 0;
  border: 0;
  padding: 0;
  text-wrap: balance;
}
.sponsor-page p,
.sponsor-page li {
  margin: 0;
}
.sponsor-page ul {
  margin: 0;
  padding: 0;
  list-style: none;
}
.sponsor-page a {
  text-decoration: none;
}
.sponsor-page .sp-eyebrow {
  font-size: 0.75rem;
  font-weight: 800;
  letter-spacing: 0.12em;
  line-height: 1.3;
  text-transform: uppercase;
  color: var(--sp-blue);
}
.sponsor-page .sp-h2 {
  margin-top: 0.5rem;
  font-size: clamp(1.55rem, 1.25rem + 1.3vw, 2.2rem);
  line-height: 1.12;
  letter-spacing: -0.035em;
  color: var(--sp-navy);
}
.sponsor-page .sp-sub {
  max-width: 62ch;
  margin-top: 0.75rem;
  font-size: 1.02rem;
  line-height: 1.6;
  color: var(--sp-muted);
}

/* Buttons */
.sponsor-page .sp-btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  min-height: 2.75rem;
  padding: 0.7rem 1.15rem;
  border: 1px solid transparent;
  border-radius: 12px;
  font-size: 0.94rem;
  font-weight: 700;
  line-height: 1.1;
  transition: transform 0.15s ease, box-shadow 0.15s ease, background-color 0.15s ease, border-color 0.15s ease;
}
.sponsor-page .sp-btn:hover {
  transform: translateY(-1px);
  text-decoration: none;
}
.sponsor-page .sp-btn:focus-visible {
  outline: 3px solid var(--sp-blue);
  outline-offset: 2px;
}
.sponsor-page .sp-btn-flame {
  background: var(--sp-flame);
  color: #fff;
  box-shadow: 0 10px 24px rgba(210, 44, 49, 0.32);
}
.sponsor-page .sp-btn-ghost {
  border-color: rgba(255, 255, 255, 0.28);
  color: #fff;
}
.sponsor-page .sp-btn-ghost:hover {
  border-color: #fff;
  background: rgba(255, 255, 255, 0.08);
}
.sponsor-page .sp-btn-ink {
  background: var(--sp-ink);
  color: #fff;
}
.sponsor-page .sp-btn-outline {
  border-color: var(--sp-border);
  background: #fff;
  color: var(--sp-text);
}
.sponsor-page .sp-btn-outline:hover {
  border-color: var(--sp-text);
}

/* Hero */
.sponsor-page .sp-hero {
  display: grid;
  grid-template-columns: minmax(0, 1.05fr) minmax(0, 0.95fr);
  gap: clamp(1.5rem, 4vw, 3rem);
  align-items: center;
  padding: clamp(1.5rem, 4.5vw, 3.5rem);
  border-radius: 28px;
  background:
    radial-gradient(90% 120% at 100% 0%, rgba(246, 133, 31, 0.26), transparent 55%),
    radial-gradient(70% 90% at 0% 100%, rgba(210, 44, 49, 0.3), transparent 60%),
    linear-gradient(135deg, var(--sp-ink) 0%, var(--sp-ink-warm) 100%);
  color: #fff;
}
.sponsor-page .sp-hero > * {
  min-width: 0;
}
.sponsor-page .sp-hero .sp-eyebrow {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  color: #ffb27a;
}
.sponsor-page .sp-hero .sp-eyebrow img {
  width: 18px;
  height: 18px;
}
.sponsor-page .sp-hero h1 {
  margin-top: 0.9rem;
  font-size: clamp(2.1rem, 1.3rem + 3.4vw, 3.7rem);
  font-weight: 800;
  line-height: 1.03;
  letter-spacing: -0.05em;
  color: #fff;
}
.sponsor-page .sp-hero h1 em {
  font-style: normal;
  background: linear-gradient(100deg, #ffb057 0%, #ff6f61 100%);
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
}
.sponsor-page .sp-lede {
  max-width: 54ch;
  margin-top: 1.15rem;
  font-size: clamp(1rem, 0.95rem + 0.35vw, 1.14rem);
  line-height: 1.62;
  color: #d9d4d4;
}
.sponsor-page .sp-cta-row {
  display: flex;
  flex-wrap: wrap;
  gap: 0.65rem;
  margin-top: 1.6rem;
}

/* Mock Maester run */
.sponsor-page .sp-term {
  border: 1px solid var(--sp-ink-line);
  border-radius: 16px;
  background: rgba(10, 10, 11, 0.72);
  box-shadow: 0 24px 60px rgba(0, 0, 0, 0.45);
  font-family: var(--merill-font-mono);
  font-size: 0.8rem;
  line-height: 1.5;
  color: #e7e3e3;
  overflow: hidden;
}
.sponsor-page .sp-term-bar {
  display: flex;
  align-items: center;
  gap: 0.4rem;
  padding: 0.65rem 0.9rem;
  border-bottom: 1px solid var(--sp-ink-line);
  color: #a39a9a;
  font-size: 0.72rem;
}
.sponsor-page .sp-term-bar i {
  width: 9px;
  height: 9px;
  border-radius: 50%;
  background: #4a3134;
}
.sponsor-page .sp-term-bar span {
  margin-left: 0.4rem;
}
.sponsor-page .sp-term-body {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  padding: 1rem 0.95rem 1.1rem;
}
.sponsor-page .sp-term-cmd {
  margin-bottom: 0.35rem;
  color: #fff;
  overflow-wrap: anywhere;
}
.sponsor-page .sp-term-cmd b {
  font-weight: 500;
  color: #ffb27a;
}
.sponsor-page .sp-check {
  display: grid;
  grid-template-columns: 4.6rem 4.4rem minmax(0, 1fr);
  gap: 0.5rem;
  align-items: baseline;
}
.sponsor-page .sp-check .sp-id {
  color: #a39a9a;
}
.sponsor-page .sp-pass {
  color: var(--sp-pass);
}
.sponsor-page .sp-fail {
  color: var(--sp-fail);
}
.sponsor-page .sp-term-fix {
  margin-top: 0.35rem;
  padding: 0.65rem 0.75rem;
  border: 1px dashed rgba(255, 138, 141, 0.5);
  border-radius: 10px;
  color: #ffd9c2;
}
.sponsor-page .sp-term-fix a {
  color: #fff;
  font-weight: 600;
  text-decoration: underline;
  text-underline-offset: 3px;
}
.sponsor-page .sp-term-sum {
  margin-top: 0.2rem;
  color: #a39a9a;
}

/* Stats */
.sponsor-page .sp-stats {
  display: grid;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  margin-top: calc(clamp(2.75rem, 6vw, 4.5rem) * -1 + 1rem);
  border: 1px solid var(--sp-border);
  border-radius: 20px;
  background: #fff;
}
.sponsor-page .sp-stats > div {
  min-width: 0;
  padding: 1.15rem 1.1rem;
}
.sponsor-page .sp-stats > div + div {
  border-left: 1px solid var(--sp-border);
}
.sponsor-page .sp-stats strong,
.sponsor-page .sp-stats span {
  display: block;
}
.sponsor-page .sp-stats strong {
  font-size: 1.65rem;
  font-weight: 800;
  letter-spacing: -0.04em;
  line-height: 1.1;
  color: var(--sp-navy);
  font-variant-numeric: tabular-nums;
}
.sponsor-page .sp-stats span {
  margin-top: 0.26rem;
  font-size: 0.78rem;
  font-weight: 600;
  line-height: 1.35;
  color: var(--sp-muted);
}

/* Note from Merill */
.sponsor-page .sp-note {
  display: grid;
  grid-template-columns: minmax(0, 0.8fr) minmax(0, 1.6fr);
  gap: clamp(1.5rem, 4vw, 3.5rem);
  align-items: start;
}
.sponsor-page .sp-note-facts {
  display: flex;
  flex-direction: column;
  gap: 0.1rem;
  margin-top: 1.25rem;
  font-size: clamp(1.5rem, 1.1rem + 1.6vw, 2.15rem);
  font-weight: 800;
  line-height: 1.15;
  letter-spacing: -0.04em;
  color: var(--sp-navy);
}
.sponsor-page .sp-note-facts span:last-child {
  background: var(--sp-flame);
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
}
.sponsor-page .sp-note-mission {
  max-width: 30ch;
  margin-top: 0.9rem;
  font-size: 1.02rem;
  line-height: 1.55;
  color: var(--sp-muted);
}
.sponsor-page .sp-note-funds {
  margin-top: 1.5rem;
  padding-top: 1.1rem;
  border-top: 1px solid var(--sp-border);
}
.sponsor-page .sp-note-funds > p {
  font-size: 0.72rem;
  font-weight: 800;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--sp-muted);
}
.sponsor-page .sp-note-funds ul {
  display: flex;
  flex-direction: column;
  gap: 0.7rem;
  margin-top: 0.85rem;
}
.sponsor-page .sp-note-funds li {
  position: relative;
  padding-left: 1.35rem;
  line-height: 1.35;
}
.sponsor-page .sp-note-funds li::before {
  content: "";
  position: absolute;
  left: 0.1rem;
  top: 0.45em;
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: var(--sp-flame);
}
.sponsor-page .sp-note-funds strong,
.sponsor-page .sp-note-funds span {
  display: block;
}
.sponsor-page .sp-note-funds strong {
  font-size: 0.98rem;
  color: var(--sp-text);
}
.sponsor-page .sp-note-funds span {
  font-size: 0.84rem;
  color: var(--sp-muted);
}
.sponsor-page .sp-ads {
  margin: 1.25rem 0 0;
  padding: 0.9rem 1.1rem;
  border: 1px dashed var(--sp-border, #e5eaf1);
  border-radius: 12px;
  font-size: 0.95rem;
  color: var(--sp-muted);
}
.sponsor-page .sp-ads strong {
  color: var(--sp-text);
  margin-right: 0.35rem;
}
.sponsor-page .sp-ads a {
  font-weight: 600;
}
.sponsor-page .sp-letter {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  max-width: 64ch;
}
.sponsor-page .sp-letter p {
  font-size: 1.06rem;
  line-height: 1.7;
  color: #34405a;
}
.sponsor-page .sp-letter p a {
  color: var(--sp-blue);
  font-weight: 600;
}
.sponsor-page .sp-letter p strong {
  color: var(--sp-text);
}
.sponsor-page .sp-sign {
  display: flex;
  align-items: center;
  gap: 0.8rem;
  margin-top: 0.4rem;
}
.sponsor-page .sp-sign img {
  width: 52px;
  height: 52px;
  border-radius: 50%;
  box-shadow: 0 6px 16px rgba(15, 39, 69, 0.16);
}
.sponsor-page .sp-sign strong,
.sponsor-page .sp-sign span {
  display: block;
  line-height: 1.35;
}
.sponsor-page .sp-sign span {
  font-size: 0.84rem;
  color: var(--sp-muted);
}

/* Three ways */
.sponsor-page .sp-ways {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 1rem;
  margin-top: 1.75rem;
}
.sponsor-page .sp-way {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  min-width: 0;
  padding: 1.5rem;
  border: 1px solid var(--sp-border);
  border-radius: 20px;
  background: #fff;
}
.sponsor-page .sp-way-cloud {
  border-color: transparent;
  background:
    linear-gradient(#fff, #fff) padding-box,
    var(--sp-flame) border-box;
  border-width: 2px;
  box-shadow: 0 18px 40px rgba(210, 44, 49, 0.12);
}
.sponsor-page .sp-way-who {
  font-size: 0.72rem;
  font-weight: 800;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--sp-muted);
}
.sponsor-page .sp-way h3 {
  display: flex;
  align-items: center;
  gap: 0.55rem;
  font-size: 1.3rem;
  line-height: 1.2;
  letter-spacing: -0.03em;
  color: var(--sp-navy);
}
.sponsor-page .sp-way h3 img,
.sponsor-page .sp-way h3 svg {
  flex: 0 0 auto;
  width: 26px;
  height: 26px;
}
.sponsor-page .sp-price {
  display: flex;
  align-items: baseline;
  gap: 0.4rem;
  font-variant-numeric: tabular-nums;
}
.sponsor-page .sp-price strong {
  font-size: 2.3rem;
  font-weight: 800;
  line-height: 1;
  letter-spacing: -0.05em;
  color: var(--sp-text);
}
.sponsor-page .sp-price span {
  font-size: 0.86rem;
  font-weight: 600;
  color: var(--sp-muted);
}
.sponsor-page .sp-way-desc {
  font-size: 0.95rem;
  line-height: 1.55;
  color: var(--sp-muted);
}
.sponsor-page .sp-way ul {
  display: flex;
  flex-direction: column;
  gap: 0.55rem;
  padding-top: 1rem;
  border-top: 1px solid var(--sp-border);
}
.sponsor-page .sp-way li {
  position: relative;
  padding-left: 1.35rem;
  font-size: 0.9rem;
  line-height: 1.5;
  color: #34405a;
}
.sponsor-page .sp-way li::before {
  content: "";
  position: absolute;
  left: 0.1rem;
  top: 0.5em;
  width: 7px;
  height: 7px;
  border-radius: 50%;
  background: var(--sp-flame);
}
.sponsor-page .sp-way li a {
  color: var(--sp-blue);
  font-weight: 600;
}
.sponsor-page .sp-way li b {
  color: var(--sp-text);
  font-variant-numeric: tabular-nums;
}
.sponsor-page .sp-way .sp-btn {
  margin-top: auto;
}
.sponsor-page .sp-way-foot {
  font-size: 0.78rem;
  line-height: 1.45;
  color: var(--sp-muted);
}
.sponsor-page .sp-way-foot a {
  color: var(--sp-blue);
  font-weight: 600;
  overflow-wrap: anywhere;
}

/* Where it goes */
.sponsor-page .sp-funds {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 0;
  margin-top: 1.5rem;
  border-top: 1px solid var(--sp-border);
}
.sponsor-page .sp-funds > div {
  min-width: 0;
  padding: 1.25rem 1.25rem 0 0;
}
.sponsor-page .sp-funds h3 {
  font-size: 1rem;
  letter-spacing: -0.015em;
  color: var(--sp-text);
}
.sponsor-page .sp-funds p {
  margin-top: 0.35rem;
  font-size: 0.9rem;
  line-height: 1.55;
  color: var(--sp-muted);
}

/* Tools */
.sponsor-page .sp-tools {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(230px, 1fr));
  gap: 0.6rem;
  margin-top: 1.5rem;
}
.sponsor-page .sp-tool {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  min-width: 0;
  padding: 0.75rem 0.9rem;
  border: 1px solid var(--sp-border);
  border-radius: 14px;
  background: #fff;
  color: var(--sp-text);
  transition: background-color 0.15s ease, border-color 0.15s ease;
}
.sponsor-page .sp-tool:hover {
  border-color: #c9d5e6;
  background: var(--sp-soft);
  text-decoration: none;
}
.sponsor-page .sp-tool img {
  flex: 0 0 auto;
  width: 32px;
  height: 32px;
  border-radius: 7px;
  object-fit: contain;
}
.sponsor-page .sp-tool .sp-tool-icon {
  display: grid;
  place-items: center;
  flex: 0 0 auto;
  width: 32px;
  height: 32px;
  border-radius: 7px;
  background: #eef4ff;
  color: var(--sp-blue);
  font-size: 1rem;
}
.sponsor-page .sp-tool strong,
.sponsor-page .sp-tool div span {
  display: block;
  line-height: 1.3;
}
.sponsor-page .sp-tool strong {
  font-size: 0.94rem;
}
.sponsor-page .sp-tool div span {
  font-size: 0.78rem;
  color: var(--sp-muted);
}

/* Sponsor wall */
.sponsor-page .sp-wall-group {
  display: flex;
  align-items: baseline;
  gap: 0.6rem;
  margin-top: 2rem;
  padding-bottom: 0.6rem;
  border-bottom: 1px solid var(--sp-border);
  font-size: 1rem;
  letter-spacing: -0.015em;
  color: var(--sp-text);
}
.sponsor-page .sp-wall-group span {
  font-size: 0.78rem;
  font-weight: 600;
  letter-spacing: 0;
  color: var(--sp-muted);
  font-variant-numeric: tabular-nums;
}
.sponsor-page .sp-wall-logos {
  display: flex;
  flex-wrap: wrap;
  gap: 0.75rem;
  margin-top: 1rem;
}
.sponsor-page .sp-wall-logos a {
  display: grid;
  place-items: center;
  min-width: 0;
  padding: 1.1rem 1.75rem;
  border: 1px solid var(--sp-border);
  border-radius: 16px;
  background: #fff;
  transition: border-color 0.15s ease, box-shadow 0.15s ease;
}
.sponsor-page .sp-wall-logos a:hover {
  border-color: #c9d5e6;
  box-shadow: 0 10px 24px rgba(15, 39, 69, 0.08);
}
.sponsor-page .sp-wall-logos img {
  width: auto;
  max-width: 100%;
  height: 52px;
  object-fit: contain;
}
.sponsor-page .sp-wall-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(210px, 1fr));
  gap: 0.6rem;
  margin-top: 1rem;
}
.sponsor-page .sp-member {
  display: flex;
  align-items: center;
  gap: 0.7rem;
  min-width: 0;
  padding: 0.6rem 0.75rem;
  border: 1px solid var(--sp-border);
  border-radius: 14px;
  background: #fff;
  color: var(--sp-text);
  font-size: 0.88rem;
  font-weight: 600;
  line-height: 1.3;
}
.sponsor-page a.sp-member:hover {
  border-color: #c9d5e6;
  background: var(--sp-soft);
  text-decoration: none;
}
.sponsor-page .sp-member img,
.sponsor-page .sp-member .sp-initials {
  flex: 0 0 auto;
  width: 36px;
  height: 36px;
  border-radius: 9px;
}
.sponsor-page .sp-member img {
  object-fit: contain;
  background: #fff;
}
.sponsor-page .sp-member .sp-initials {
  display: grid;
  place-items: center;
  background: #fdece6;
  color: var(--sp-flame-3);
  font-size: 0.8rem;
  font-weight: 800;
}
.sponsor-page .sp-member .sp-name {
  min-width: 0;
  overflow-wrap: anywhere;
}
.sponsor-page .sp-member-lg {
  padding: 0.8rem 0.9rem;
  font-size: 1rem;
  font-weight: 700;
}
.sponsor-page .sp-member-lg img,
.sponsor-page .sp-member-lg .sp-initials {
  width: 48px;
  height: 48px;
}
.sponsor-page .sp-member-round img {
  border-radius: 50%;
  object-fit: cover;
}
.sponsor-page a.sp-member-you {
  border-style: dashed;
  color: var(--sp-flame-3);
}
.sponsor-page .sp-member-you .sp-initials {
  background: transparent;
  border: 1px dashed #f0b9ab;
}

/* Closing */
.sponsor-page .sp-close {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-between;
  gap: 1.5rem;
  padding: clamp(1.5rem, 4vw, 2.75rem);
  border-radius: 24px;
  background: var(--sp-navy);
  color: #fff;
}
.sponsor-page .sp-close > div {
  min-width: 0;
}
.sponsor-page .sp-close h2 {
  font-size: clamp(1.45rem, 1.2rem + 1.1vw, 2rem);
  line-height: 1.15;
  letter-spacing: -0.035em;
  color: #fff;
}
.sponsor-page .sp-close p {
  max-width: 56ch;
  margin-top: 0.6rem;
  font-size: 0.98rem;
  line-height: 1.6;
  color: #c7d8f2;
}
.sponsor-page .sp-close p:not(.sp-cta-row) a {
  color: #fff;
  font-weight: 600;
  text-decoration: underline;
  text-underline-offset: 3px;
}
.sponsor-page .sp-close .sp-cta-row {
  margin-top: 0;
}

@media (max-width: 62em) {
  .sponsor-page .sp-hero,
  .sponsor-page .sp-note {
    grid-template-columns: 1fr;
  }
  .sponsor-page .sp-ways {
    grid-template-columns: 1fr;
  }
  .sponsor-page .sp-way .sp-btn {
    margin-top: 0.25rem;
  }
}
@media (max-width: 40em) {
  .sponsor-page .sp-stats {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }
  .sponsor-page .sp-stats > div:nth-child(3) {
    border-left: 0;
  }
  .sponsor-page .sp-stats > div:nth-child(n + 3) {
    border-top: 1px solid var(--sp-border);
  }
  .sponsor-page .sp-funds {
    grid-template-columns: 1fr;
  }
  .sponsor-page .sp-check {
    grid-template-columns: 4.4rem minmax(0, 1fr);
  }
  .sponsor-page .sp-check .sp-id {
    display: none;
  }
  .sponsor-page .sp-cta-row .sp-btn {
    flex: 1 1 100%;
  }
}
@media (prefers-reduced-motion: reduce) {
  .sponsor-page .sp-btn,
  .sponsor-page .sp-tool {
    transition: none;
  }
  .sponsor-page .sp-btn:hover {
    transform: none;
  }
}
</style>

<div class="sponsor-page">

<section class="sp-hero">
  <div>
    <p class="sp-eyebrow"><img src="/assets/images/projects/maester.svg" alt=""> Sponsor my work</p>
    <h1>Free tools for the Microsoft community, <em>funded by the people who use them.</em></h1>
    <p class="sp-lede">I build Maester, Lokka, idPowerToys, cmd.ms, Graph X-Ray and more, and give them away. There is no company or investor behind them. If they save you time, you can help me keep building.</p>
    <p class="sp-cta-row">
      <a class="sp-btn sp-btn-flame" href="https://github.com/sponsors/merill">Sponsor on GitHub</a>
      <a class="sp-btn sp-btn-ghost" href="#ways">See all three ways</a>
    </p>
  </div>
  <div class="sp-term" role="img" aria-label="A mock Maester test run. Passed: tools are free and open source. Passed: mission is to keep building Maester. Passed: four kids to feed. Passed: mortgage is present. Failed: no investors or outside funding found. Remediation: become a sponsor.">
    <div class="sp-term-bar"><i></i><i></i><i></i><span>pwsh</span></div>
    <div class="sp-term-body">
      <div class="sp-term-cmd"><b>PS&gt;</b> Invoke-Maester -Path ./merill -Tag Funding</div>
      <div class="sp-check"><span class="sp-pass">✓ Passed</span><span class="sp-id">ME.1001</span><span>Tools are free and open source</span></div>
      <div class="sp-check"><span class="sp-pass">✓ Passed</span><span class="sp-id">ME.1002</span><span>Mission: keep building Maester</span></div>
      <div class="sp-check"><span class="sp-pass">✓ Passed</span><span class="sp-id">ME.1003</span><span>Kids to feed: 4</span></div>
      <div class="sp-check"><span class="sp-pass">✓ Passed</span><span class="sp-id">ME.1004</span><span>Mortgage: present</span></div>
      <div class="sp-check"><span class="sp-fail">✗ Failed</span><span class="sp-id">ME.1005</span><span>Investors or outside funding: none found</span></div>
      <div class="sp-term-fix">Remediation: <a href="#ways">become a sponsor</a></div>
      <div class="sp-term-sum">Tests: 5 · Passed: 4 · Failed: 1</div>
    </div>
  </div>
</section>

<section class="sp-stats" aria-label="How much the tools are used">
  <div><strong>{{ site.data.stats.psgallery.Maester.display | default: "625k" }}</strong><span>Maester installs</span></div>
  <div><strong>{{ site.data.stats.cloudflare["graphpermissions.merill.net"].display | default: "1.8m" }}+</strong><span>views across my sites</span></div>
  <div><strong>{{ site.data.stats.cloudflare["cmd.ms"].display | default: "155k" }}</strong><span>monthly visits to cmd.ms</span></div>
  <div><strong>20K</strong><span>weekly Entra.News subscribers</span></div>
</section>

<section class="sp-note">
  <div>
    <p class="sp-eyebrow">Why I'm asking</p>
    <p class="sp-note-facts"><span>No investors.</span><span>One mission.</span></p>
    <p class="sp-note-mission">Keep building Maester and free tools for the Microsoft community.</p>
    <div class="sp-note-funds">
      <p>How the free work is paid for</p>
      <ul>
        <li><strong>Maester Cloud</strong></li>
        <li><strong>Ad sponsors</strong><span>on Entra.News and Entra.Chat</span></li>
        <li><strong>Sponsors like you</strong><span>on GitHub and through your company</span></li>
      </ul>
    </div>
  </div>
  <div class="sp-letter">
    <p>I spent years on the Microsoft Entra product team. In 2026 I left to build tools for this community full time.</p>
    <p>I give away most of what I build, and I want to keep it that way. <strong>None of the free work has outside funding.</strong> I pay for the hosting, the test tenants and the Microsoft licences myself.</p>
    <p>I support myself through paid work that sits alongside the free tools: <a href="https://maester.cloud">Maester Cloud</a> and <a href="https://sponsors.admin.news">ad sponsors</a> on the newsletters and podcast. Sponsorship is the part that pays for the time I spend on everything that stays free.</p>
    <p>It isn't only the tools. I write <a href="https://entra.news">Entra.News</a> every week, host the <a href="https://entra.chat">Entra.Chat</a> podcast, and post what I learn about Entra, security and Graph on <a href="https://www.linkedin.com/in/merill">LinkedIn</a> and <a href="https://x.com/merill">X</a>. If something I shared taught you something and you'd like to give back, this is how.</p>
    <p>I also have a mortgage and four kids, so this work has to pay its way if I'm going to keep doing it.</p>
    <p>My mission is to keep building Maester and keep helping the Microsoft community. If my tools save you or your team time, sponsoring is how you keep them coming.</p>
    <div class="sp-sign">
      <img src="/assets/images/merill-profile.png" alt="Merill Fernando">
      <div><strong>Merill Fernando</strong><span>Maintainer of Maester · ex-Microsoft Entra PM · Melbourne</span></div>
    </div>
  </div>
</section>

<section id="ways">
  <p class="sp-eyebrow">Three ways to sponsor</p>
  <h2 class="sp-h2">Pick the one that fits you.</h2>
  <p class="sp-sub">A coffee from one admin, a subscription for a team, or a company backing the project. All three keep the tools free for everyone else.</p>

  <div class="sp-ways">

    <div class="sp-way">
      <p class="sp-way-who">For individuals and teams</p>
      <h3><svg viewBox="0 0 16 16" aria-hidden="true"><path fill="#bf3989" d="m8 14.25.345.666a.75.75 0 0 1-.69 0l-.008-.004-.018-.01a7.152 7.152 0 0 1-.31-.17 22.055 22.055 0 0 1-3.434-2.414C2.045 10.731 0 8.35 0 5.5 0 2.836 2.086 1 4.25 1 5.797 1 7.153 1.802 8 3.02 8.847 1.802 10.203 1 11.75 1 13.914 1 16 2.836 16 5.5c0 2.85-2.045 5.231-3.885 6.818a22.066 22.066 0 0 1-3.744 2.584l-.018.01-.006.003h-.002ZM4.25 2.5c-1.336 0-2.75 1.164-2.75 3 0 2.15 1.58 4.144 3.365 5.682A20.58 20.58 0 0 0 8 13.393a20.58 20.58 0 0 0 3.135-2.211C12.92 9.644 14.5 7.65 14.5 5.5c0-1.836-1.414-3-2.75-3-1.373 0-2.609.986-3.029 2.456a.749.749 0 0 1-1.442 0C6.859 3.486 5.623 2.5 4.25 2.5Z"/></svg> GitHub Sponsors</h3>
      <p class="sp-price"><span>from</span><strong>$5</strong><span>/ month, or a one-off</span></p>
      <p class="sp-way-desc">Learned something from a post, the newsletter or the podcast? Shout me a coffee, or sponsor every month.</p>
      <ul>
        <li><b>$5</b> Coffee fuel. A sponsor badge and your avatar on the <a href="#wall">sponsor wall on merill.net</a>.</li>
        <li><b>$15</b> Admin's thank-you. A larger avatar on the sponsor wall.</li>
        <li><b>$100</b> Company sponsor. Your logo on the sponsor wall and the tool READMEs.</li>
        <li><b>$500</b> Lead sponsor. A large logo at the top of the sponsor wall.</li>
      </ul>
      <a class="sp-btn sp-btn-ink" href="https://github.com/sponsors/merill">Sponsor on GitHub</a>
      <p class="sp-way-foot">A donation to my open source work. It doesn't include Maester Cloud.</p>
    </div>

    <div class="sp-way sp-way-cloud">
      <p class="sp-way-who">For teams that run Maester</p>
      <h3><img src="/assets/images/projects/maester.svg" alt=""> Maester Cloud</h3>
      <p class="sp-price"><span>from</span><strong>$99</strong><span>/ month</span></p>
      <p class="sp-way-desc">Sponsor Maester and get a product in return. Maester Cloud runs Maester for you and keeps the history.</p>
      <ul>
        <li>Deploys into your own Azure subscription.</li>
        <li>Posture across all your tenants, with history for every check.</li>
        <li>Shows what drifted between runs and alerts you when it changes.</li>
        <li>Every subscription funds new checks, docs and fixes in open source Maester.</li>
      </ul>
      <a class="sp-btn sp-btn-flame" href="https://maester.cloud/pricing">Get Maester Cloud</a>
      <p class="sp-way-foot">Open to companies and individuals. <a href="https://maester.cloud">maester.cloud</a></p>
    </div>

    <div class="sp-way">
      <p class="sp-way-who">For companies that rely on Maester</p>
      <h3><img src="/assets/images/projects/maester.svg" alt=""> Company sponsor</h3>
      <p class="sp-price"><strong>Let's talk</strong></p>
      <p class="sp-way-desc">Sponsor my time on Maester directly. In return you get logo placement and a bigger say in what gets built.</p>
      <ul>
        <li>Pays for maintainer time on checks, releases and reviews.</li>
        <li>Your logo on the Maester home page, sponsor page and README.</li>
        <li>A bigger say in the Maester backlog and what I work on next.</li>
      </ul>
      <a class="sp-btn sp-btn-outline" href="mailto:merill@merill.net?subject=Sponsoring%20Maester">Email me</a>
      <p class="sp-way-foot">Write to <a href="mailto:merill@merill.net?subject=Sponsoring%20Maester">merill@merill.net</a> and tell me a little about your company.</p>
    </div>

  </div>
  <p class="sp-ads"><strong>Looking to advertise instead?</strong> <span>Newsletter ads across Admin.News, including Entra.News, are booked at <a href="https://sponsors.admin.news">sponsors.admin.news</a>.</span></p>
</section>

<section>
  <p class="sp-eyebrow">Where it goes</p>
  <h2 class="sp-h2">What your sponsorship pays for.</h2>
  <div class="sp-funds">
    <div>
      <h3>My time</h3>
      <p>Writing checks, reviewing pull requests, shipping releases and answering the community.</p>
    </div>
    <div>
      <h3>Test tenants and licences</h3>
      <p>Maester checks are verified against real tenants, and those tenants need Microsoft licences.</p>
    </div>
    <div>
      <h3>Hosting</h3>
      <p>The servers and domains behind the free sites, so they stay fast and free of ads.</p>
    </div>
  </div>
</section>

<section>
  <p class="sp-eyebrow">What you're backing</p>
  <h2 class="sp-h2">Tools and teaching you may already rely on.</h2>
  <p class="sp-sub">Free tools, a weekly newsletter, a podcast, and the posts I share on LinkedIn and X to help you learn Entra, security and Graph.</p>
  <div class="sp-tools">
    <a class="sp-tool" href="https://maester.dev"><img src="/assets/images/projects/maester.svg" alt=""><div><strong>Maester</strong><span>Security testing for Microsoft 365</span></div></a>
    <a class="sp-tool" href="https://lokka.dev"><img src="/assets/images/projects/lokka.svg" alt=""><div><strong>Lokka</strong><span>MCP server for Microsoft Graph</span></div></a>
    <a class="sp-tool" href="https://idpowertoys.merill.net"><img src="/assets/images/projects/idpowertoys.png" alt=""><div><strong>idPowerToys</strong><span>Conditional Access visualizer</span></div></a>
    <a class="sp-tool" href="https://cmd.ms"><img src="/assets/images/projects/cmdms.svg" alt=""><div><strong>cmd.ms</strong><span>Your Microsoft Cloud command line</span></div></a>
    <a class="sp-tool" href="https://graphxray.merill.net"><img src="/assets/images/projects/graphxray.svg" alt=""><div><strong>Graph X-Ray</strong><span>Portal clicks to Graph scripts</span></div></a>
    <a class="sp-tool" href="https://graphpermissions.merill.net"><img src="/assets/images/projects/graphpermissions.svg" alt=""><div><strong>Graph Permissions Explorer</strong><span>What each Graph permission exposes</span></div></a>
    <a class="sp-tool" href="https://getyako.com"><img src="/assets/images/projects/yako.png" alt=""><div><strong>Yako</strong><span>Start page for Microsoft admins</span></div></a>
    <a class="sp-tool" href="https://aka.ms/msid"><img src="/assets/images/projects/msidentitytools.ico" alt=""><div><strong>MSIdentityTools</strong><span>PowerShell cmdlets for Entra</span></div></a>
    <a class="sp-tool" href="https://entra.news"><img src="/assets/images/projects/entranews.png" alt=""><div><strong>Entra.News</strong><span>Weekly newsletter, 20K subscribers</span></div></a>
    <a class="sp-tool" href="https://entra.chat"><img src="/assets/images/projects/entrachat.png" alt=""><div><strong>Entra.Chat</strong><span>Podcast with the people behind Entra</span></div></a>
    <a class="sp-tool" href="https://admin.news"><img src="/assets/images/projects/adminnews.png" alt=""><div><strong>Admin.News</strong><span>Weekly and daily newsletters, 34K+ subscribers</span></div></a>
    <a class="sp-tool" href="https://intune.admin.news"><img src="/assets/images/projects/intunenews.png" alt=""><div><strong>Intune News</strong><span>Weekly Intune roundup</span></div></a>
    <a class="sp-tool" href="https://defender.admin.news"><img src="/assets/images/projects/defendernews.png" alt=""><div><strong>Defender News</strong><span>Weekly Defender and Sentinel roundup</span></div></a>
    <a class="sp-tool" href="https://ad.admin.news"><img src="/assets/images/projects/adnews.png" alt=""><div><strong>AD News</strong><span>Weekly Active Directory roundup</span></div></a>
    <a class="sp-tool" href="https://purview.admin.news"><img src="/assets/images/projects/purviewnews.png" alt=""><div><strong>Purview News</strong><span>Weekly Purview roundup</span></div></a>
    <a class="sp-tool" href="https://msai.ms"><img src="/assets/images/projects/msailogo.png" alt=""><div><strong>Microsoft AI News</strong><span>Weekly Microsoft AI and Copilot roundup</span></div></a>
    <a class="sp-tool" href="https://www.linkedin.com/in/merill"><span class="sp-tool-icon"><i class="fab fa-linkedin-in" aria-hidden="true"></i></span><div><strong>Posts on LinkedIn</strong><span>Tips and explainers, 50K followers</span></div></a>
    <a class="sp-tool" href="https://x.com/merill"><span class="sp-tool-icon"><i class="fab fa-twitter" aria-hidden="true"></i></span><div><strong>Posts on X</strong><span>Tips and explainers, 21K followers</span></div></a>
    <a class="sp-tool" href="/"><img src="/assets/images/projects/blog.svg" alt=""><div><strong>And many more</strong><span>See everything on merill.net</span></div></a>
  </div>
</section>

<section id="wall">
  {%- assign wall = site.data.sponsor_wall -%}
  {%- assign wall_total = wall.company.size | plus: wall.cloud.size | plus: wall.github.size -%}
  <p class="sp-eyebrow">Sponsor wall</p>
  <h2 class="sp-h2">Thank you to the {{ wall_total }} sponsors backing this work.</h2>
  <p class="sp-sub">Everyone who sponsors Maester, subscribes to Maester Cloud or sponsors me on GitHub, and chose to be listed. Updated daily.</p>

  {%- if wall.company.size > 0 %}
  <h3 class="sp-wall-group">Company sponsors</h3>
  <div class="sp-wall-logos">
    {%- for s in wall.company %}
    <a href="{{ s.url | default: 'https://maester.dev/sponsor' | escape }}" rel="noopener" title="{{ s.name | escape }}"><img src="{{ s.logo | escape }}" alt="{{ s.name | escape }}" loading="lazy"></a>
    {%- endfor %}
  </div>
  {%- endif %}

  {%- if wall.cloud.size > 0 %}
  <h3 class="sp-wall-group">Maester Cloud supporters <span>{{ wall.cloud.size }}</span></h3>
  <div class="sp-wall-grid">
    {%- for s in wall.cloud %}
    {%- capture inner %}{% if s.image %}<img src="{{ s.image | escape }}" alt="" loading="lazy">{% else %}<span class="sp-initials" aria-hidden="true">{{ s.initials | escape }}</span>{% endif %}<span class="sp-name">{{ s.name | escape }}</span>{% endcapture %}
    {%- if s.url %}
    <a class="sp-member" href="{{ s.url | escape }}" rel="noopener nofollow">{{ inner }}</a>
    {%- else %}
    <div class="sp-member">{{ inner }}</div>
    {%- endif %}
    {%- endfor %}
    <a class="sp-member sp-member-you" href="https://maester.cloud/pricing"><span class="sp-initials" aria-hidden="true">+</span><span class="sp-name">Your name here</span></a>
  </div>
  {%- endif %}

  <h3 class="sp-wall-group">GitHub sponsors{% if wall.github.size > 0 %} <span>{{ wall.github.size }}</span>{% endif %}</h3>
  <div class="sp-wall-grid">
    {%- for s in wall.github %}
    {%- assign big = false -%}
    {%- if s.tier == "Lead Sponsors" or s.tier == "Company Sponsors" %}{% assign big = true %}{% endif %}
    <a class="sp-member{% if big %} sp-member-lg{% endif %}{% unless s.org %} sp-member-round{% endunless %}" href="{{ s.website | default: s.url | escape }}" rel="noopener nofollow"><img src="{{ s.avatar | escape }}" alt="" loading="lazy"><span class="sp-name">{{ s.name | escape }}</span></a>
    {%- endfor %}
    <a class="sp-member sp-member-you" href="https://github.com/sponsors/merill"><span class="sp-initials" aria-hidden="true">+</span><span class="sp-name">Your name here</span></a>
  </div>
</section>

<section class="sp-close">
  <div>
    <h2>Keep the tools free for everyone.</h2>
    <p>Can't sponsor right now? Starring <a href="https://github.com/maester365/maester">Maester on GitHub</a> or telling a colleague about a tool helps too.</p>
  </div>
  <p class="sp-cta-row">
    <a class="sp-btn sp-btn-flame" href="https://github.com/sponsors/merill">Sponsor on GitHub</a>
    <a class="sp-btn sp-btn-ghost" href="https://maester.cloud/pricing">Get Maester Cloud</a>
  </p>
</section>

</div>
