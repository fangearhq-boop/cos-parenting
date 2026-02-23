---
name: cos-parenting-content
description: >
  **COS Parenting Daily Content Pipeline**: Runs the FanGear HQ shared content engine
  for the COS Parenting brand. Generates daily social media and editorial content
  for Colorado Springs parents including local news, events, national parenting stories,
  evergreen guides, and humor content.

  MANDATORY TRIGGERS: Use this skill whenever the user asks to "run the parenting content task",
  "generate today's parenting content", "run the COS Parenting pipeline", "create today's posts",
  or any variation involving daily content production for the COS Parenting brand.
---

# COS Parenting — Daily Content Pipeline

This skill runs the FanGear HQ shared content engine for the **COS Parenting** brand.

## Setup

Before executing the pipeline, read these files in order:

1. **Shared Engine**: `../../_engine/SKILL.md` — the universal 15-step pipeline
2. **Niche Config**: `../../niche-config.yaml` — brand name, content prefix, photo source, pillars
3. **Brand Guide**: `../../brand-guide.md` — colors, fonts, composition rules
4. **Brand Voice**: `../../brand-voice.md` — detailed voice attributes, tone spectrum, terminology
5. **API Reference**: `../../api-reference.md` — primary news sources for COS parenting
6. **Seasonal Calendar**: `../../seasonal-calendar.md` — seasonal events in Colorado Springs (if exists)

Then execute the 15-step pipeline as documented in the engine SKILL.md, using the
niche config values wherever `{CONFIG.*}` placeholders appear.

## Key Brand Rules

- **Photo source**: Gemini AI-generated images (`photo_source: "gemini"` in niche-config.yaml)
- **Gemini mode**: `base_only` — Gemini generates clean background images (no text), then Canva adds branded text overlays
- **Gemini model**: `gemini-2.5-flash-image` (fast, ~$0.04/image)
- **Image prompt guidelines**: Photorealistic, diverse families, warm tones, Colorado Springs settings, leave clean space for text overlays
- **Content pillars**: Local News, Local Events, National Parenting, Evergreen, Humor
- **Voice**: Warm, helpful, fun — like that parent at school pickup who always knows what's going on
- **Hashtags (X)**: #COSParenting #ColoradoSprings #COSKids #PikesPeakParenting
- **Hashtags (Facebook)**: None
- **Emoji (X)**: 1-2 max
- **Emoji (Facebook)**: 2-4 per post

## Script Paths

- Fact-check: `python ../../_engine/scripts/verify-facts.py --niche Parenting YYYY-MM-DD`
- Dashboard: `python ../../_engine/scripts/generate-review-dashboard.py --niche Parenting YYYY-MM-DD`
- Publish: `python ../../_engine/scripts/publish-dashboard.py --niche Parenting YYYY-MM-DD`
- Gemini images: `python ../../_engine/scripts/generate-gemini-image.py` (see README-gemini.md for full usage)
- Gemini budget: `python ../../_engine/scripts/generate-gemini-image.py --budget`
