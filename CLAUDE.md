# COS Parenting Content Pipeline — Project Rules

## Gemini Image Generation
- Photo source is `gemini` (AI-generated via Google Gemini API), NOT Imagn or stock photos.
- Mode is `base_only` — generate clean backgrounds with NO text, NO watermarks, NO overlays. Canva adds text overlays later.
- Model: `gemini-2.5-flash-image` (~$0.04/image). Only use `gemini-3-pro-image-preview` if explicitly requested.
- Image prompts must include: scene, subjects, mood, lighting, color palette, art style.
- Request clean visual space in the bottom third for text overlay readability.
- NEVER include celebrity likenesses, copyrighted characters, or brand logos in prompts.

## Brand Voice
- Personality: "That parent at school pickup who always knows what's going on" — warm, organized, helpful, laughs at parenting chaos.
- Voice attributes: Helpful, Warm, Fun, Curious, Local.
- ALWAYS use contractions ("we're" not "we are").
- NEVER use: mama/mama bear, boy mom/girl dad, hubby/wifey, "kids these days", "back in my day".
- Use "COS" or "Colorado Springs" — NEVER "the Springs" or "C-Springs".
- Use "parents" not "moms and dads". Use "families" not "moms".
- Use "kids" (occasionally "kiddos" on Facebook only).
- School districts: D11, D20, D49 (abbreviations are standard).
- Exclamation marks: max 1 per social post, 0 in articles.
- Oxford comma: YES. Numbers: spell 1-9, numerals 10+. Times: 12-hour with MT.

## Platform Rules
- **X/Twitter:** Concise, 1-2 emoji max, 4 hashtags (#COSParenting #ColoradoSprings #COSKids #PikesPeakParenting). Lead with date/time/place/age range. Max 280 chars (URLs = 23 chars).
- **Facebook:** Conversational, 3-5 paragraphs for news, 2-4 emoji (natural placement), NO hashtags, end with engagement question.
- **Articles:** 500-1000 words, NO emoji, semantic HTML5, must include "What's Next" closing section. Quick reference tables allowed.

## Content Pillars (5)
Every story must map to one: Local News, Local Events, National Parenting, Evergreen, or Humor. Target 7 stories/day across all pillars.

## Review Dashboard
- localStorage keys use `parenting-content-` prefix (e.g., `parenting-content-review-2026-02-22`, `parenting-content-schedule-config`).
- CSS badge classes: `.badge-x-post`, `.badge-facebook`, `.badge-article`, `.badge-image`, `.badge-brief`.
- Status classes: `.status-approved`, `.status-needs-edit`, `.status-rejected`, `.status-edited`.
- Fact-check badges: `.fact-check-verified`, `.fact-check-warning`, `.fact-check-unverified`.

## Fact-Checking (claim-patterns.py)
- Priority 1 (HIGH): Prices, "free" claims, age ranges, phone numbers, COS-specific locations, street addresses.
- Priority 2 (MEDIUM): School district references, statistics/percentages, unit counts, study/research citations.
- Priority 3 (LOW): Organizations (CPSC, AAP, CDC), product/brand names in recall context, safety hazard classifications, URLs.

## File Naming
- Content folders: `parenting-content-YYYY-MM-DD/`
- Articles: `article-NN-slug-title.html` (NN = two-digit story number, slug = lowercase hyphenated)
- Generated images: `story-{N}-{slug}.png` in `generated-images/` subfolder

## Canva Integration
- Brand kit ID: `kAHCKfCZgk0`
- Brand colors: Primary Teal (#0097A7), Warm Coral (#FF6F61), Soft Gold (#F4C542), Dark Slate (#2C3E50), Light Cloud (#F5F7FA)
- Fonts: Poppins (headlines), Nunito (subtitles), Open Sans (body)
- Image dimensions: X = 1200x675, Facebook = 1200x630
