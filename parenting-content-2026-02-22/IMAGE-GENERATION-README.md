# Image Generation Guide — Feb 22, 2026

## Quick Start

```bash
# 1. Install the SDK (one time)
pip install google-genai

# 2. Generate all 7 images (~3 minutes total)
cd Niche_Launches/Parenting/parenting-content-2026-02-22
python generate_images.py

# 3. Generate a single story (for testing)
python generate_images.py 7

# 4. Retry specific failures
python generate_images.py 1 3
```

## What This Generates

7 clean background images (no text), one per story:

| Story | File | Scene |
|-------|------|-------|
| 1 | story-1-childcare-crisis.png | Parent working from home with toddler, Colorado winter window |
| 2 | story-2-ice-carving.png | Families watching ice carving outdoors, bright winter day |
| 3 | story-3-child-support.png | Father reviewing documents at kitchen table |
| 4 | story-4-school-choice.png | Mother and daughter on couch looking at laptop |
| 5 | story-5-product-recalls.png | Parent examining children's sleepwear tag in nursery |
| 6 | story-6-boundaries-empathy.png | Father kneeling at eye level with daughter, calm conversation |
| 7 | story-7-weather-whiplash.png | Family bundled up walking on sunny snowy Colorado trail |

## Next Steps After Generation

1. **Upload to Canva** — Upload each image as an asset
2. **Create designs** — Apply the COS Parenting brand template with text overlays from 07-image-manifest.md
3. **Export** — Export X (1200x675) and Facebook (1200x630) versions
4. **Update manifest** — Update 07-image-manifest.md with Canva asset/design IDs

## Design Specifications

All text overlays use:
- **Headline:** Poppins Bold, white (#FFFFFF) or teal (#0097A7)
- **Subtitle:** Nunito Semi-bold, gold (#F4C542) or coral (#FF6F61)
- **Overlay bar:** Dark Slate (#2C3E50) at 80% opacity, bottom third
- **Dimensions:** X = 1200x675, Facebook = 1200x630

## Prompt Strategy

- **Mode:** base_only (clean images, no text baked in)
- **Style:** Consistent photorealistic editorial photography across all 7
- **Diversity:** Varied family compositions across the set
- **Colorado context:** Stories 1, 2, 4, 7 include CO-specific scenery
- **Bottom third:** All prompts request simpler/darker lower area for overlay
