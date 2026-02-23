#!/usr/bin/env python3
"""
Generate all 7 base images at 4:5 vertical (1080x1350) for COS Parenting 2026-02-23.
One image per story, used for both X and Facebook social posts.

These prompts are adapted from 05-image-concepts.md for portrait composition.
"""
import os
import sys
import importlib.util

# Import the Gemini generator
ENGINE_SCRIPTS = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..", "..", "_engine", "scripts"
)
spec = importlib.util.spec_from_file_location(
    "gemini_gen",
    os.path.join(os.path.abspath(ENGINE_SCRIPTS), "generate-gemini-image.py")
)
gemini_gen = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gemini_gen)
generate_image = gemini_gen.generate_image

IMAGES_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "images")
os.makedirs(IMAGES_DIR, exist_ok=True)

# All 7 stories with 4:5 vertical prompts (portrait composition, subject in upper 2/3)
STORIES = [
    # Story 1 — Childcare Crisis
    {
        "number": 1,
        "filename": "COS-Parenting-Story1-social-20260223.png",
        "prompt": (
            "Photorealistic editorial photograph in 4:5 vertical portrait orientation. "
            "A tired but determined mother in her early 30s wearing professional work clothes "
            "stands on the front porch of a modest Colorado Springs home, holding her toddler "
            "on her hip. She looks at the front door of a home-based daycare where two toddlers "
            "of different ethnicities are visible through the window playing with wooden blocks "
            "on a colorful rug, with a female caregiver sitting nearby. A small white picket "
            "fence lines the front yard with bare winter trees. Late morning winter sunlight "
            "illuminates the scene with warm golden tones. The faint silhouette of Pikes Peak "
            "is visible above the roofline. The mother's expression is concerned but not "
            "panicked — empathetic and relatable. The subject fills the upper two-thirds of "
            "the vertical frame, with the porch and yard details in the lower portion. "
            "No text, no words, no logos, no signs. Warm editorial photography style. "
            "Shot at 1080x1350 pixels, 4:5 vertical aspect ratio."
        ),
    },
    # Story 2 — Safety Alert (Recall)
    {
        "number": 2,
        "filename": "COS-Parenting-Story2-social-20260223.png",
        "prompt": (
            "Photorealistic editorial photograph in 4:5 vertical portrait orientation. "
            "A young Black father in his early 30s stands in a bright, modern nursery, "
            "carefully inspecting a white baby bath seat by holding it up and examining "
            "the suction cups on its underside. He wears a casual gray henley shirt and "
            "has a focused, protective expression. The nursery has pale walls and soft "
            "natural light streaming through sheer white curtains. A wooden changing table "
            "to the right has a small baby walker and a baby lounger pillow on it. In the "
            "background, a baby is safely lying in a white crib, reaching for a soft plush "
            "toy. The father is positioned prominently in the upper two-thirds of the "
            "vertical frame, with the changing table and nursery details filling the scene. "
            "The lighting is warm and natural, creating a safe domestic atmosphere. "
            "No text, no words, no logos, no labels. Warm, authentic candid style. "
            "Shot at 1080x1350 pixels, 4:5 vertical aspect ratio."
        ),
    },
    # Story 3 — Spring Break
    {
        "number": 3,
        "filename": "COS-Parenting-Story3-social-20260223.png",
        "prompt": (
            "Photorealistic editorial photograph in 4:5 vertical portrait orientation. "
            "A Latina mother in her mid-30s stands at a large wall-mounted calendar in a "
            "bright, modern kitchen. She holds a colorful marker in one hand and has a "
            "slightly amused, slightly overwhelmed expression as she looks at the calendar, "
            "which has multiple blocks of dates highlighted in different colors including "
            "teal, coral, and gold. On the kitchen counter below the calendar, two printed "
            "school schedules are laid out side by side. A white coffee mug sits on the "
            "counter. Warm winter morning sunlight streams through a kitchen window to the "
            "right, with a distant view of snow-capped Pikes Peak visible through the glass. "
            "In the background near the kitchen door, three kids' backpacks in different "
            "colors hang on wall hooks. The mother and calendar fill the upper two-thirds "
            "of the vertical frame. The overall mood is warm, relatable, and lightly humorous. "
            "No text, no words, no logos, no readable writing on the calendar or schedules. "
            "Warm and inviting editorial photography style. "
            "Shot at 1080x1350 pixels, 4:5 vertical aspect ratio."
        ),
    },
    # Story 4 — Teen Sleep
    {
        "number": 4,
        "filename": "COS-Parenting-Story4-social-20260223.png",
        "prompt": (
            "Photorealistic editorial photograph in 4:5 vertical portrait orientation. "
            "A teenage girl, approximately 16 years old, of mixed race, sleeping peacefully "
            "in a cozy bed on a weekend morning. She is curled on her side with soft rumpled "
            "white and light blue blankets pulled up to her shoulder, her face relaxed and "
            "serene against a fluffy pillow. Warm, golden late-morning sunlight streams "
            "through partially open light gray curtains on the right side of the frame, "
            "casting soft light across the bed and wall. The bedroom is authentic and "
            "lived-in: a wooden nightstand holds a small stack of books and a phone plugged "
            "into a charger, a navy blue hoodie is draped over a desk chair in the background, "
            "and a few small photos are tacked to a corkboard on the wall. The sleeping teen "
            "fills the upper two-thirds of the vertical frame, with the cozy bed and bedroom "
            "details filling the scene. The overall mood is peaceful, warm, and reassuring. "
            "No text, no words, no logos. Warm and inviting editorial photography style with "
            "soft focus on the background. "
            "Shot at 1080x1350 pixels, 4:5 vertical aspect ratio."
        ),
    },
    # Story 5 — D20 Job Fair + D11 STEM
    {
        "number": 5,
        "filename": "COS-Parenting-Story5-social-20260223.png",
        "prompt": (
            "Photorealistic editorial photograph in 4:5 vertical portrait orientation. "
            "A Colorado Springs high school campus on a bright, clear late-winter morning. "
            "In the upper portion, the main entrance of a modern suburban high school "
            "building with tan brick and large windows has its front doors open, with three "
            "adults of diverse backgrounds walking toward the entrance dressed in smart "
            "casual professional attire, carrying folders. In the foreground below, at an "
            "outdoor folding table, four middle school students of diverse ethnicities are "
            "excitedly working on a small robotics project, with a young female teacher in "
            "a teal cardigan leaning in to help them. The table has colorful STEM materials "
            "including circuit boards, small wheels, and craft supplies. The sky is brilliant "
            "clear Colorado blue, with snow-capped Pikes Peak visible in the background above "
            "the school roofline. Late morning winter sunlight casts crisp shadows. "
            "The vertical composition stacks the school entrance above and STEM table below. "
            "No text, no words, no logos, no banners, no signs. "
            "Warm and inviting editorial photography style. "
            "Shot at 1080x1350 pixels, 4:5 vertical aspect ratio."
        ),
    },
    # Story 6 — Starsmore + Plunge
    {
        "number": 6,
        "filename": "COS-Parenting-Story6-social-20260223.png",
        "prompt": (
            "Photorealistic editorial photograph in 4:5 vertical portrait orientation. "
            "A family of three exploring a nature trail at the base of North Cheyenne Canon "
            "in Colorado Springs. A white father in his late 30s wearing a light jacket and "
            "small backpack walks on a dirt trail alongside his two children: a boy around "
            "age 8 and a girl around age 6, both in colorful winter jackets. The girl is "
            "pointing excitedly up into the tall Ponderosa pine trees along the trail. "
            "Dramatic red and orange rock formations rise on both sides of the trail, "
            "framing the family. The forest floor has patches of winter-brown grass and a "
            "few small rocks. Dappled winter sunlight filters through the pine canopy above, "
            "casting warm spots of light on the trail and family. The vertical composition "
            "shows the towering canyon walls and pine canopy above, with the family walking "
            "toward the viewer in the center of the frame. The mood is adventurous, joyful, "
            "and full of natural wonder. "
            "No text, no words, no logos. Warm and inviting editorial photography style "
            "with rich natural colors. "
            "Shot at 1080x1350 pixels, 4:5 vertical aspect ratio."
        ),
    },
    # Story 7 — Humor: 5 Stages
    {
        "number": 7,
        "filename": "COS-Parenting-Story7-social-20260223.png",
        "prompt": (
            "Photorealistic editorial photograph with a warm, humorous tone in 4:5 vertical "
            "portrait orientation. A white mother in her late 30s sits at a bright kitchen "
            "island looking comically overwhelmed. She has one hand on her forehead and wide "
            "eyes with a half-smile, looking at several colorful printed school calendars "
            "spread across the counter in front of her. Pink, yellow, green, and blue sticky "
            "notes are stuck to the calendars and counter. A silver laptop is open nearby. "
            "Behind her on the kitchen wall, a large white wall calendar is visible, covered "
            "in overlapping colored sticky notes and multiple dates circled in different "
            "colored markers. A white coffee mug sits on the counter with crumpled sticky "
            "notes nearby. The kitchen is bright and modern with white cabinets and warm "
            "wood countertops. Morning sunlight streams through a window to the left. "
            "The mother and kitchen scene fill the full vertical frame — her expressive face "
            "prominent in the upper portion, the calendar chaos on the counter below. "
            "The mood is genuinely funny and relatable, not truly stressed. "
            "No text, no words, no logos, no readable writing on calendars or sticky notes. "
            "Warm and inviting editorial photography style with a humorous, lighthearted quality. "
            "Shot at 1080x1350 pixels, 4:5 vertical aspect ratio."
        ),
    },
]


def main():
    print(f"Generating {len(STORIES)} base images at 4:5 vertical (1080x1350)")
    print(f"Output: {IMAGES_DIR}")
    print("=" * 60)

    ok = 0
    for story in STORIES:
        num = story["number"]
        out_path = os.path.join(IMAGES_DIR, story["filename"])

        print(f"\n  Story {num} ... ", flush=True)

        result = generate_image(
            prompt=story["prompt"],
            width=1080,
            height=1350,
            mode="base_only",
            output_path=out_path,
            per_run_cap_override=20,
        )

        if result and result != "DRY_RUN":
            size_kb = os.path.getsize(out_path) / 1024
            print(f"  OK ({size_kb:.0f} KB)")
            ok += 1
        else:
            print(f"  FAILED")

    print(f"\n{'=' * 60}")
    print(f"Results: {ok}/{len(STORIES)} base images generated")
    return 0 if ok == len(STORIES) else 1


if __name__ == "__main__":
    sys.exit(main())
