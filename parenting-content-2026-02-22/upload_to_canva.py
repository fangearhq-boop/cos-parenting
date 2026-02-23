#!/usr/bin/env python3
"""
COS Parenting — Upload Generated Images to Canva
=================================================
After running generate_images.py, use this script to upload
each image to Canva as an asset for design creation.

NOTE: This script is for reference. The actual Canva upload
can be done through Claude's Canva integration once the
generated images are accessible via a public URL.

For manual upload:
1. Open Canva.com
2. Go to Brand Kit or Uploads
3. Upload each image from ./generated-images/
4. Record the Canva Asset IDs back in 07-image-manifest.md
"""

# Story-to-file mapping for easy reference
STORIES = {
    1: {
        "title": "COS Childcare Crisis",
        "file": "generated-images/story-1-childcare-crisis.png",
        "x_overlay": {
            "headline": "1 in 4 COS Parents Can't Find Childcare",
            "subtitle": "Federal Cuts Meet Local Shortage",
        },
    },
    2: {
        "title": "Free Ice Carving Today",
        "file": "generated-images/story-2-ice-carving.png",
        "x_overlay": {
            "headline": "Free Ice Carving Today",
            "subtitle": "12 PM, 1:30 PM & 3 PM | $1K Prize",
        },
    },
    3: {
        "title": "Child Support Changes",
        "file": "generated-images/story-3-child-support.png",
        "x_overlay": {
            "headline": "Child Support Changes March 1",
            "subtitle": "What Colorado Families Need to Know",
        },
    },
    4: {
        "title": "D20 School Choice",
        "file": "generated-images/story-4-school-choice.png",
        "x_overlay": {
            "headline": "D20 School Choice Open Now",
            "subtitle": "Apply by March 13",
        },
    },
    5: {
        "title": "CPSC Recalls",
        "file": "generated-images/story-5-product-recalls.png",
        "x_overlay": {
            "headline": "Product Recall Alert",
            "subtitle": "Check Your Kids' Products Today",
        },
    },
    6: {
        "title": "Boundaries With Empathy",
        "file": "generated-images/story-6-boundaries-empathy.png",
        "x_overlay": {
            "headline": "Boundaries With Empathy",
            "subtitle": "The 2026 Parenting Shift",
        },
    },
    7: {
        "title": "Weather Whiplash",
        "file": "generated-images/story-7-weather-whiplash.png",
        "x_overlay": {
            "headline": "23°F Today. 63°F Tomorrow.",
            "subtitle": "Just Colorado Springs Things",
        },
    },
}

if __name__ == "__main__":
    print("COS Parenting — Canva Upload Reference")
    print("=" * 50)
    print()
    print("Upload these files to Canva, then record Asset IDs")
    print("back in 07-image-manifest.md:\n")
    for num, data in sorted(STORIES.items()):
        print(f"  Story {num}: {data['title']}")
        print(f"    File: {data['file']}")
        print(f"    X Headline: {data['x_overlay']['headline']}")
        print(f"    X Subtitle: {data['x_overlay']['subtitle']}")
        print()
