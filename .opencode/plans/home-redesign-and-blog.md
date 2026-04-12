# Plan: Restore Blog & Redesign Home Page

## Overview
1. Restore the blog in the site navigation
2. Enable pagination on the blog page
3. Redesign the home page with a visual card grid showcasing all projects

## Changes

### 1. `_data/navigation.yaml` — Add Blog to nav
Add a "Blog" entry to the `main:` section:
```yaml
main:
  - title: "Home"
    url: /
  - title: "Blog"
    url: /blog/
```

### 2. `_config.yml` — Enable pagination
Change `paginate:` (line 197) from blank to `10`:
```yaml
paginate: 10
paginate_path: /blog/page:num/
```

### 3. `_pages/blog.md` — Update for pagination
Replace the current blog page with a paginator-aware layout. Use `layout: home` from Minimal Mistakes (which supports jekyll-paginate) or implement manual pagination with `paginator` object.

Note: jekyll-paginate requires the paginated page to be `index.html` at the root or at the `paginate_path`. Since the blog is at `/blog/`, we need to move blog.md to `blog/index.html` or use a different approach.

**Approach**: Convert `_pages/blog.md` into a proper paginated blog listing using the Liquid `paginator` object. Since `jekyll-paginate` only works with `index.html` files, we'll update `paginate_path` to `/blog/page:num/` and create `/blog/index.html`.

### 4. Download project logos to `assets/images/projects/`
Download logos from their respective sites for projects that have them:
- Maester: `https://raw.githubusercontent.com/maester365/maester/main/website/static/img/logo.svg`
- Graph X-Ray: `https://graphxray.merill.net/logo.svg`
- Graph Permissions Explorer: `https://graphpermissions.merill.net/images/logo.svg`
- Lokka: `https://lokka.dev/img/logo.svg`
- Zero Trust Workshop: `https://microsoft.github.io/zerotrustassessment/img/logo.svg`
- Entra.News: `https://substack-post-media.s3.amazonaws.com/public/images/7b3b3378-703b-4f6a-ab4d-10470336b06f_1280x1280.png`
- idPowerToys: `https://idpowertoys.merill.net/logo192.png`
- Inclusiveness Analyzer: `https://inclusivenessanalyzer.com/images/logo.png`

Use existing splash images from `assets/images/splash/` for:
- cmd.ms → `cmd.png`
- Entra Exporter → `aadexporter.png`
- Graph PS Converter → `graphconverter.png`
- MSIdentityTools → `msid.png`
- Azure AD Assessment → `assessment.png`
- M365 Gender Pronoun Kit → `m365gender.png`
- Inclusiveness Analyzer → `inclusivenessanalyzer.png`

For projects without logos, use Font Awesome icons as fallback in the card HTML.

### 5. `_pages/home.md` — Redesign with card grid
Replace the current plain markdown with HTML card grid. Each section has a heading and a responsive grid of project cards. Each card contains:
- Project logo/icon (image or Font Awesome fallback)
- Project name (linked to the project URL)
- Short description

Custom CSS embedded in the page for the card grid layout.

## Files Modified
- `_data/navigation.yaml`
- `_config.yml`
- `_pages/blog.md` (or moved to `blog/index.html`)
- `_pages/home.md`

## Files Created
- `assets/images/projects/` (directory with downloaded logos)

## Files NOT Modified
- All existing blog posts remain at their current URLs
- No layout or theme files modified
