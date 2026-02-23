#!/usr/bin/env python3
"""
Generate all 14 final composite images for COS Parenting 2026-02-23.
Uses the FanGear HQ compositor script with brand fonts and colors.

Now uses single 4:5 vertical base images per story (generated natively at 1080x1350).
Both X and Facebook composites use the same base image.
"""
import os
import sys

# Add engine scripts to path
import importlib.util

ENGINE_SCRIPTS = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..", "..", "_engine", "scripts"
)
spec = importlib.util.spec_from_file_location(
    "compositor",
    os.path.join(os.path.abspath(ENGINE_SCRIPTS), "composite-social-image.py")
)
compositor = importlib.util.module_from_spec(spec)
spec.loader.exec_module(compositor)
composite_image = compositor.composite_image

IMAGES_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "images")
FINAL_DIR = os.path.join(IMAGES_DIR, "final")
os.makedirs(FINAL_DIR, exist_ok=True)

# Brand colors
GOLD = "#F4C542"
CORAL = "#FF6F61"

# All 14 images: (story, platform, base_filename, headline, subtitle, subtitle_color)
# Both X and FB now use the same 4:5 vertical base image per story
COMPOSITES = [
    # Story 1 — Childcare Crisis
    (1, "x", "COS-Parenting-Story1-social-20260223.png",
     "Childcare Crisis: Zoning Fast-Track Hits Neighborhoods",
     "47K kids, 18K spots. City Council moves on zoning changes.",
     GOLD),
    (1, "facebook", "COS-Parenting-Story1-social-20260223.png",
     "Childcare Crisis: Zoning Fast-Track Hits Neighborhoods",
     "47K kids, 18K spots. City Council moves on zoning changes.",
     GOLD),

    # Story 2 — Safety Alert (coral subtitle for urgency)
    (2, "x", "COS-Parenting-Story2-social-20260223.png",
     "Safety Alert: Baby Products Recalled NOW",
     "Bath seats, walkers, loungers. Check your home today.",
     CORAL),
    (2, "facebook", "COS-Parenting-Story2-social-20260223.png",
     "Safety Alert: Baby Products Recalled NOW",
     "Bath seats, walkers, loungers. Check your home today.",
     CORAL),

    # Story 3 — Spring Break
    (3, "x", "COS-Parenting-Story3-social-20260223.png",
     "Spring Break 2026: Every District, Different Dates",
     "D49, D20, D11, FFC — your complete planning guide.",
     GOLD),
    (3, "facebook", "COS-Parenting-Story3-social-20260223.png",
     "Spring Break 2026: Every District, Different Dates",
     "D49, D20, D11, FFC — your complete planning guide.",
     GOLD),

    # Story 4 — Teen Sleep
    (4, "x", "COS-Parenting-Story4-social-20260223.png",
     "Let Them Sleep: Weekend Rest Cuts Teen Depression 41%",
     "New study says sleeping in on weekends protects mental health.",
     GOLD),
    (4, "facebook", "COS-Parenting-Story4-social-20260223.png",
     "Let Them Sleep: Weekend Rest Cuts Teen Depression 41%",
     "New study says sleeping in on weekends protects mental health.",
     GOLD),

    # Story 5 — D20 Job Fair + D11 STEM
    (5, "x", "COS-Parenting-Story5-social-20260223.png",
     "D20 Job Fair Saturday + D11 STEM Challenge",
     "Feb 28 at Liberty HS, 9 AM. STEM runs through April.",
     GOLD),
    (5, "facebook", "COS-Parenting-Story5-social-20260223.png",
     "D20 Job Fair Saturday + D11 STEM Challenge",
     "Feb 28 at Liberty HS, 9 AM. STEM runs through April.",
     GOLD),

    # Story 6 — Starsmore + Plunge
    (6, "x", "COS-Parenting-Story6-social-20260223.png",
     "Family Day at Starsmore + Plunge Coming Up",
     "Free nature fun Feb 28. Special Olympics 5K March 7.",
     GOLD),
    (6, "facebook", "COS-Parenting-Story6-social-20260223.png",
     "Family Day at Starsmore + Plunge Coming Up",
     "Free nature fun Feb 28. Special Olympics 5K March 7.",
     GOLD),

    # Story 7 — Humor: 5 Stages
    (7, "x", "COS-Parenting-Story7-social-20260223.png",
     "The 5 Stages of Planning COS Spring Break",
     "When every district has different dates...",
     GOLD),
    (7, "facebook", "COS-Parenting-Story7-social-20260223.png",
     "The 5 Stages of Planning COS Spring Break",
     "When every district has different dates...",
     GOLD),
]


def main():
    print(f"Generating {len(COMPOSITES)} final composite images")
    print(f"Output: {FINAL_DIR}")
    print("=" * 60)

    ok = 0
    for story, platform, base_file, headline, subtitle, sub_color in COMPOSITES:
        base_path = os.path.join(IMAGES_DIR, base_file)
        plat_label = "X" if platform == "x" else "FB"
        out_name = f"COS-Parenting-Story{story}-{plat_label}-final-20260223.png"
        out_path = os.path.join(FINAL_DIR, out_name)

        print(f"  Story {story} {plat_label:2s} ... ", end="", flush=True)

        if not os.path.exists(base_path):
            print(f"SKIP (base not found: {base_file})")
            continue

        try:
            composite_image(
                base_image_path=base_path,
                output_path=out_path,
                headline=headline,
                subtitle=subtitle,
                platform=platform,
                subtitle_color=sub_color,
            )
            size_kb = os.path.getsize(out_path) / 1024
            print(f"OK ({size_kb:.0f} KB)")
            ok += 1
        except Exception as e:
            print(f"FAIL: {e}")

    print(f"\n{'=' * 60}")
    print(f"Results: {ok}/{len(COMPOSITES)} composites generated")
    return 0 if ok == len(COMPOSITES) else 1


if __name__ == "__main__":
    sys.exit(main())
