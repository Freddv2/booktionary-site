# Story-first Website Implementation Plan

> Execute directly in this session, as requested by the user. No subagents.

**Goal:** Publish the approved homepage mockup, approved realistic phone/book image, and tracked App Store URL across the existing localized website.

**Architecture:** Keep the dependency-free static Python generator, existing page URLs, support sections, and locale relationships. Port the approved mockup's scoped CSS and semantic sections into render_home; localized copy belongs in home_ui.py and home_refresh.py. Keep article SEO expansion outside this change.

**Tech Stack:** Python standard library, static HTML/CSS, GitHub Pages.

**Spec:** Approved mockup at /Users/Frederic.Vincent/Documents/perso/projects/booktionary/output/mockups/website-refresh-2026-10-11/booktionary-story-first.html and the current conversation.

## Global constraints

- Stay in the story → point at an unfamiliar word → get the meaning → keep reading.
- Capabilities follow the reading flow: 24 book languages, contextual definitions, offline after setup, one-time purchase.
- Track every App Store link with pt=129235559, ct=booktionary_website_ios, mt=8.
- Preserve real support content, email, seven locales, French compatibility redirect, canonical URLs and hreflang.
- Current release is 1.0.10; 1.0.11 full-definition translation remains upcoming.
- No changes to downloadable dictionaries, catalogs, privacy documents or app code.

## Review focus

- Long translated headings and 320px screens remain readable.
- Download links preserve complete query parameters in anchors and JSON-LD.
- Disclosure controls retain all 24 book languages and remain keyboard-accessible.
- Full-definition availability and contextual-definition device requirements are explicit.
- Rebuilding is deterministic and support URLs remain intact.

## Task 1: Implement approved home refresh

- [x] Update validator and add focused contracts for reading/proof order, real image, tracked URLs, support preservation and release availability; observe failures on old generator.
- [x] Update localized copy, renderer, scoped CSS and image asset; remove obsolete screenshot frames and top language carousel.
- [x] Build all pages; run validate.py and unittest discovery. Inspect English/French and narrow layouts in Zen.
- [ ] Review complete diff and deterministic rebuild; commit, publish through the repository's GitHub Pages main branch, and verify live HTML and asset.

## Progress

- Baseline: 28 pages, 0 failing; 4 unit tests passed. Working branch codex/story-first-website-20261011 in existing isolated worktree.
- Apple lookup: 1.0.10 released 2026-10-10, iOS 17+, $1.99 USD.
- User explicitly approved mockup and requested site update; proceed directly through publishing without a redundant approval request.

- Verification: 28 pages, zero failures; six unit tests pass, including 27-page campaign URL coverage. Checked English desktop and 320px, French 320px and desktop feature/photo section in Zen.
- Review: performed directly, respecting the user’s instruction against subagent delegation. Preserved support content and all resource/catalog bytes. Broader search-content corrections remain out of scope.
- Final source review and asset/link audit passed. No dictionary/catalog or privacy/license files changed.
