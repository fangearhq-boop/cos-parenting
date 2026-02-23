#!/usr/bin/env python3
"""
COS Parenting — Gemini Image Generation (base_only mode)
=========================================================
Generates clean background images for all 7 stories.
Text overlays will be added in Canva afterward.

USAGE:
  1. Install the SDK:     pip install google-genai
  2. Run all stories:     python generate_images.py
  3. Run one story:       python generate_images.py 7
  4. Run specific ones:   python generate_images.py 1 2 5

Images are saved to ./generated-images/
Each takes ~15-30 seconds to generate.

REQUIREMENTS:
  - Python 3.10+
  - google-genai package
  - GEMINI_API_KEY env var OR edit API_KEY below
"""

import os
import sys
import time
from pathlib import Path

try:
    from google import genai
    from google.genai import types
except ImportError:
    print("ERROR: google-genai not installed. Run: pip install google-genai")
    sys.exit(1)

# ──────────────────────────────────────────────
# CONFIGURATION
# ──────────────────────────────────────────────
API_KEY = os.environ.get("GEMINI_API_KEY", "AIzaSyAPy3DXFExm9HWfF-GG1x2tTK-5IlxHIwg")
MODEL = "gemini-2.0-flash-exp"
OUTPUT_DIR = Path(__file__).parent / "generated-images"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# ──────────────────────────────────────────────
# STYLE ANCHOR (applied to every prompt)
# ──────────────────────────────────────────────
# This ensures visual consistency across all 7 images
STYLE_ANCHOR = (
    "Photorealistic editorial photography style. Shot on a professional camera with "
    "natural lighting and shallow depth of field. Authentic, candid feel — not posed "
    "or overly styled. Warm color temperature. "
    "IMPORTANT: The bottom third of the image must be visually simpler — "
    "use darker tones, natural shadow, or softly blurred background in the lower "
    "portion of the frame. This area will have a semi-transparent text overlay bar "
    "placed on top of it later. "
    "Do NOT include any text, words, logos, watermarks, or typographic elements "
    "anywhere in the image. "
    "Image should be landscape orientation suitable for 1200x675 pixels (16:9 aspect ratio)."
)

# ──────────────────────────────────────────────
# STORY PROMPTS
# ──────────────────────────────────────────────
# Each prompt describes only the visual scene.
# Brand text overlays are added later in Canva.

PROMPTS = {
    1: {
        "title": "COS Childcare Crisis: Federal Cuts Meet Local Shortage",
        "filename": "story-1-childcare-crisis",
        "prompt": (
            "A tired but determined parent — a mixed-race woman in her early 30s — "
            "sitting at a cluttered home office desk with a laptop open. A toddler "
            "plays with colorful wooden blocks on the floor nearby. The parent has "
            "one hand on the keyboard and is glancing toward the child with a "
            "concerned but loving expression. Through a window behind the desk, "
            "a Colorado winter landscape is visible: bare aspen trees, light snow "
            "on the ground, overcast sky with the faint outline of Pikes Peak in "
            "the distance. The room feels warm and lived-in — a half-empty coffee "
            "mug, scattered papers, a children's board book on the desk edge. "
            "Soft natural window light fills the room. The mood is relatable and "
            "slightly stressful but grounded in love. "
            + STYLE_ANCHOR
        ),
    },
    2: {
        "title": "Free Ice Carving Competitions Today in COS",
        "filename": "story-2-ice-carving",
        "prompt": (
            "A group of diverse families gathered outdoors watching an ice carving "
            "demonstration on a bright, crisp Colorado winter day. An artist in a "
            "heavy coat is mid-carve on a large block of crystal-clear ice, with "
            "ice chips catching golden sunlight and sparkling like diamonds. "
            "Children in colorful winter coats — reds, yellows, bright blues — "
            "lean forward with wide-eyed wonder and excitement, mouths slightly "
            "open in amazement. Parents stand behind them, smiling warmly. Two "
            "finished ice sculptures gleam in the background, catching light "
            "beautifully. Clear vivid blue Colorado sky with bright winter "
            "afternoon sun. The atmosphere is joyful, energetic, and magical. "
            "Pine trees and a glimpse of mountain foothills in the far background. "
            + STYLE_ANCHOR
        ),
    },
    3: {
        "title": "Colorado Child Support Changes Hit March 1",
        "filename": "story-3-child-support",
        "prompt": (
            "A thoughtful Black father in his late 30s sitting at a clean kitchen "
            "table reviewing paper documents spread out before him, using a "
            "calculator. A warm pendant light illuminates the table from above. "
            "A framed family photo — him with two young children — is visible "
            "on a shelf in the soft background. His expression is focused and "
            "serious but not distressed — he is being responsible and thorough. "
            "The kitchen is modern but lived-in, with a child's colorful crayon "
            "drawing attached to the refrigerator in soft focus behind him. "
            "Morning light streams gently through a side window. The mood is "
            "calm, grown-up, and purposeful. "
            + STYLE_ANCHOR
        ),
    },
    4: {
        "title": "D20 School Choice Window Open Through March 13",
        "filename": "story-4-school-choice",
        "prompt": (
            "A Latina mother and her elementary-age daughter (about 8 years old) "
            "sitting together on a comfortable couch, both looking at a laptop "
            "screen with engaged expressions. The daughter points at the screen "
            "with excitement while the mother smiles warmly and leans in. "
            "A colorful school backpack and a few notebooks sit on the couch "
            "beside them. Through a nearby window, a snow-dusted Colorado "
            "Springs neighborhood is visible with foothills and clear blue sky. "
            "The living room is bright, warm, and inviting with family photos "
            "on the wall and a bookshelf. Natural afternoon light floods the "
            "room. The mood is hopeful, collaborative, and optimistic. "
            + STYLE_ANCHOR
        ),
    },
    5: {
        "title": "CPSC Recalls: Children's Sleepwear and Baby Swings",
        "filename": "story-5-product-recalls",
        "prompt": (
            "A caring parent — a white woman with auburn hair in her early 30s — "
            "standing in a well-lit nursery, carefully holding up and examining "
            "the tag on a piece of children's sleepwear. Her expression is "
            "focused, protective, and attentive — a parent being diligent about "
            "safety. Behind her in soft focus: a wooden baby crib, organized "
            "shelves with neatly folded children's clothes, and a few stuffed "
            "animals. A happy toddler sits safely on a soft area rug in the "
            "background, contentedly playing with soft toys. The nursery is "
            "warm, clean, and organized with soft pastel yellow and sage green "
            "accents. Gentle natural light pours in from a curtained window. "
            "The mood is protective and responsible without being fearful. "
            + STYLE_ANCHOR
        ),
    },
    6: {
        "title": "2026 Parenting Trend: Boundaries With Empathy",
        "filename": "story-6-boundaries-empathy",
        "prompt": (
            "An Asian father in his mid-30s kneeling down to eye level with "
            "his 5-year-old daughter in a cozy living room. He gently holds "
            "her small hands in his while they have a calm, connected "
            "conversation. Both have gentle, peaceful expressions — the father "
            "is patient and present, the daughter feels safe and heard. "
            "The living room has a warm reading nook with soft cushions, "
            "a low bookshelf full of children's books, and a knit blanket "
            "draped over a nearby armchair. Golden late-afternoon light "
            "filters through sheer curtains, creating a warm glow. A few "
            "wooden toys are on the floor nearby. The scene radiates warmth, "
            "patience, emotional connection, and mutual respect. "
            + STYLE_ANCHOR
        ),
    },
    7: {
        "title": "COS Weather Whiplash: 23°F Today, 63°F Tomorrow",
        "filename": "story-7-weather-whiplash",
        "prompt": (
            "A joyful biracial family — a mother and two children (ages 4 and 7) — "
            "walking on a sunny Colorado Springs trail with patchy snow on the "
            "ground. All three are bundled in warm winter coats, knit hats, and "
            "mittens. The kids are laughing and the mom has a big smile. "
            "Despite the cold temperatures evident from their breath and gear, "
            "brilliant dazzling Colorado sunshine floods the scene under a vivid "
            "deep blue sky. Pikes Peak is clearly visible in the background, "
            "snow-capped and majestic against the blue. Frost-covered prairie "
            "grass and bare cottonwood trees line the trail. The sunshine makes "
            "everything glow warmly, hinting that warmer weather could arrive "
            "at any moment — classic Colorado Springs winter conditions. "
            "The mood is energetic, fun, and uniquely Colorado. "
            + STYLE_ANCHOR
        ),
    },
}


def generate_image(story_num: int, prompt_data: dict, client) -> str | None:
    """Generate a single image via Gemini and save it."""
    filename = f"{prompt_data['filename']}.png"
    filepath = OUTPUT_DIR / filename

    print(f"\n{'='*60}")
    print(f"Story {story_num}: {prompt_data['title']}")
    print(f"{'='*60}")
    print(f"Generating image...")
    start = time.time()

    try:
        response = client.models.generate_content(
            model=MODEL,
            contents=prompt_data["prompt"],
            config=types.GenerateContentConfig(
                response_modalities=["IMAGE", "TEXT"],
            ),
        )

        # Extract image from response
        if response.candidates and response.candidates[0].content.parts:
            for part in response.candidates[0].content.parts:
                if part.inline_data and part.inline_data.mime_type.startswith("image/"):
                    with open(filepath, "wb") as f:
                        f.write(part.inline_data.data)
                    elapsed = time.time() - start
                    size_kb = filepath.stat().st_size / 1024
                    print(f"  ✓ Saved: {filepath}")
                    print(f"  Size: {size_kb:.1f} KB | Time: {elapsed:.1f}s")
                    return str(filepath)
                elif part.text:
                    print(f"  Model text: {part.text[:200]}")

        print(f"  ✗ No image returned")
        if response.candidates:
            print(f"  Finish reason: {response.candidates[0].finish_reason}")
        return None

    except Exception as e:
        elapsed = time.time() - start
        print(f"  ✗ Error ({elapsed:.1f}s): {e}")
        return None


def main():
    print("=" * 60)
    print("COS Parenting — Gemini Image Generator (base_only)")
    print("=" * 60)

    # Parse args — optionally generate just specific stories
    stories_to_gen = sorted(PROMPTS.keys())
    if len(sys.argv) > 1:
        stories_to_gen = [int(x) for x in sys.argv[1:]]
    print(f"Stories to generate: {stories_to_gen}")
    print(f"Output directory: {OUTPUT_DIR}")
    print(f"Model: {MODEL}")
    print()

    # Initialize client
    print("Initializing Gemini client...")
    client = genai.Client(api_key=API_KEY)
    print("Client ready.\n")

    results = {}
    for i, story_num in enumerate(stories_to_gen):
        if story_num not in PROMPTS:
            print(f"Story {story_num} not found in prompts, skipping")
            continue
        result = generate_image(story_num, PROMPTS[story_num], client)
        results[story_num] = result

        # Rate limiting: pause between requests
        if i < len(stories_to_gen) - 1:
            wait = 5
            print(f"  Waiting {wait}s before next request...")
            time.sleep(wait)

    # Summary
    print(f"\n{'='*60}")
    print("GENERATION SUMMARY")
    print(f"{'='*60}")
    success = sum(1 for v in results.values() if v is not None)
    total = len(results)
    print(f"Generated: {success}/{total} images\n")

    for num in sorted(results.keys()):
        path = results[num]
        status = "✓" if path else "✗ FAILED"
        title = PROMPTS[num]["title"]
        print(f"  Story {num} ({title}): {status}")
        if path:
            print(f"           {path}")

    if success < total:
        failed = [str(n) for n, v in results.items() if v is None]
        print(f"\nTo retry failed stories: python {__file__} {' '.join(failed)}")

    return 0 if success == total else 1


if __name__ == "__main__":
    sys.exit(main())
