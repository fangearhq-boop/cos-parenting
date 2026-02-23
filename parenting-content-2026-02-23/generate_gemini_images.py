#!/usr/bin/env python3
"""
Generate all 14 Gemini base images for COS Parenting 2026-02-23.
Reads API key from Windows registry (setx-stored), generates images,
saves to content folder with proper naming convention.
"""

import os
import sys
import json
import base64
import time
import urllib.request
import urllib.error

# Try reading API key from environment first, then Windows registry
API_KEY = os.environ.get('GEMINI_API_KEY')
if not API_KEY:
    try:
        import winreg
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Environment')
        API_KEY, _ = winreg.QueryValueEx(key, 'GEMINI_API_KEY')
        winreg.CloseKey(key)
    except Exception:
        print("ERROR: GEMINI_API_KEY not found in environment or registry")
        sys.exit(1)

MODEL = "gemini-2.5-flash-image"
OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGES_DIR = os.path.join(OUTPUT_DIR, "images")
os.makedirs(IMAGES_DIR, exist_ok=True)

# All 14 image prompts: (story_num, platform, filename, prompt)
IMAGES = [
    (1, "X", "COS-Parenting-Story1-X-20260223.png",
     "Photorealistic editorial photograph of a charming home-based daycare in a Colorado Springs residential neighborhood, shot from the sidewalk looking toward the front of a modest single-story house with a covered porch. Through the large front window, two toddlers of different ethnicities are visible sitting on a colorful rug playing with wooden blocks, with a female caregiver in her 30s sitting cross-legged nearby smiling at them. The front yard has a small white picket fence, a few bare winter trees, and a tidy sidewalk. Neighboring houses are visible on both sides. Late morning winter sunlight illuminates the scene with warm golden tones. The upper third of the frame is open blue Colorado sky with the faint silhouette of Pikes Peak on the horizon. No text, no words, no logos, no signs. Warm and inviting but with an authentic neighborhood feel. Shot at 1200x675 pixels, 16:9 aspect ratio. Leave the upper third as open sky for text overlay."),

    (1, "Facebook", "COS-Parenting-Story1-Facebook-20260223.png",
     "Photorealistic editorial photograph of a charming home-based daycare in a Colorado Springs residential neighborhood, shot from the sidewalk looking toward the front of a modest single-story house with a covered porch. Through the large front window, two toddlers of different ethnicities are visible sitting on a colorful rug playing with wooden blocks, with a female caregiver in her 30s sitting cross-legged nearby smiling at them. The front yard has a small white picket fence, a few bare winter trees, and a tidy sidewalk. Neighboring houses are visible on both sides. Late morning winter sunlight illuminates the scene with warm golden tones. The upper portion of the frame is open blue Colorado sky with the faint silhouette of Pikes Peak on the horizon. No text, no words, no logos, no signs. Warm and inviting but with an authentic neighborhood feel. Shot at 1200x630 pixels, 1.91:1 aspect ratio. Leave the upper portion as open sky for text overlay."),

    (2, "X", "COS-Parenting-Story2-X-20260223.png",
     "Photorealistic editorial photograph of a young Black father in his early 30s standing in a bright, modern nursery, carefully inspecting a white baby bath seat by holding it up and examining the suction cups on its underside. He wears a casual gray henley shirt and has a focused, protective expression. The nursery has pale walls, soft natural light streaming through sheer white curtains, and a wooden changing table to the right with a small baby walker and a baby lounger pillow neatly placed on it. In the far background, a baby is safely lying in a white crib, reaching for a soft plush toy. The lighting is warm and natural, creating a safe domestic atmosphere. The upper third of the frame shows the clean nursery wall and ceiling, providing open space for text overlay. No text, no words, no logos, no labels. Warm, authentic candid style. Shot at 1200x675 pixels, 16:9 aspect ratio."),

    (2, "Facebook", "COS-Parenting-Story2-Facebook-20260223.png",
     "Photorealistic editorial photograph of a young Black father in his early 30s standing in a bright, modern nursery, carefully inspecting a white baby bath seat by holding it up and examining the suction cups on its underside. He wears a casual gray henley shirt and has a focused, protective expression. The nursery has pale walls, soft natural light streaming through sheer white curtains, and a wooden changing table to the right with a small baby walker and a baby lounger pillow neatly placed on it. In the far background, a baby is safely lying in a white crib, reaching for a soft plush toy. The lighting is warm and natural, creating a safe domestic atmosphere. The upper portion of the frame shows the clean nursery wall, providing open space for text overlay. No text, no words, no logos, no labels. Warm, authentic candid style. Shot at 1200x630 pixels, 1.91:1 aspect ratio."),

    (3, "X", "COS-Parenting-Story3-X-20260223.png",
     "Photorealistic editorial photograph of a Latina mother in her mid-30s standing at a large wall-mounted calendar in a bright, modern kitchen. She holds a colorful marker in one hand and has a slightly amused, slightly overwhelmed expression as she looks at the calendar, which has multiple blocks of dates highlighted in different colors including teal, coral, and gold. On the kitchen counter below the calendar, two printed school schedules are laid out side by side. A white coffee mug sits on the counter. Warm winter morning sunlight streams through a kitchen window to the right, with a distant view of snow-capped Pikes Peak visible through the glass. In the background near the kitchen door, three kids' backpacks in different colors hang on wall hooks. The overall mood is warm, relatable, and lightly humorous. No text, no words, no logos, no readable writing on the calendar or schedules. Warm and inviting editorial photography style. Shot at 1200x675 pixels, 16:9 aspect ratio. Leave the upper third as open wall space and window light for text overlay."),

    (3, "Facebook", "COS-Parenting-Story3-Facebook-20260223.png",
     "Photorealistic editorial photograph of a Latina mother in her mid-30s standing at a large wall-mounted calendar in a bright, modern kitchen. She holds a colorful marker in one hand and has a slightly amused, slightly overwhelmed expression as she looks at the calendar, which has multiple blocks of dates highlighted in different colors including teal, coral, and gold. On the kitchen counter below the calendar, two printed school schedules are laid out side by side. A white coffee mug sits on the counter. Warm winter morning sunlight streams through a kitchen window to the right, with a distant view of snow-capped Pikes Peak visible through the glass. In the background near the kitchen door, three kids' backpacks in different colors hang on wall hooks. The overall mood is warm, relatable, and lightly humorous. No text, no words, no logos, no readable writing on the calendar or schedules. Warm and inviting editorial photography style. Shot at 1200x630 pixels, 1.91:1 aspect ratio. Leave the upper portion as open wall space for text overlay."),

    (4, "X", "COS-Parenting-Story4-X-20260223.png",
     "Photorealistic editorial photograph of a teenage girl, approximately 16 years old, of mixed race, sleeping peacefully in a cozy bed on a weekend morning. She is curled on her side with soft rumpled white and light blue blankets pulled up to her shoulder, her face relaxed and serene against a fluffy pillow. Warm, golden late-morning sunlight streams through partially open light gray curtains on the right side of the frame, casting soft light across the bed and wall. The bedroom is authentic and lived-in: a wooden nightstand holds a small stack of books and a phone plugged into a charger, a navy blue hoodie is draped over a desk chair in the background, and a few small photos are tacked to a corkboard on the wall. The overall mood is peaceful, warm, and reassuring. The upper third of the frame shows the light-colored bedroom wall above the headboard, bathed in soft window light. No text, no words, no logos. Warm and inviting editorial photography style with soft focus on the background. Shot at 1200x675 pixels, 16:9 aspect ratio. Leave the upper third as clean wall space for text overlay."),

    (4, "Facebook", "COS-Parenting-Story4-Facebook-20260223.png",
     "Photorealistic editorial photograph of a teenage girl, approximately 16 years old, of mixed race, sleeping peacefully in a cozy bed on a weekend morning. She is curled on her side with soft rumpled white and light blue blankets pulled up to her shoulder, her face relaxed and serene against a fluffy pillow. Warm, golden late-morning sunlight streams through partially open light gray curtains on the right side of the frame, casting soft light across the bed and wall. The bedroom is authentic and lived-in: a wooden nightstand holds a small stack of books and a phone plugged into a charger, a navy blue hoodie is draped over a desk chair in the background. The overall mood is peaceful, warm, and reassuring. The upper portion of the frame shows the light-colored bedroom wall above the headboard. No text, no words, no logos. Warm and inviting editorial photography style with soft focus on the background. Shot at 1200x630 pixels, 1.91:1 aspect ratio. Leave the upper portion as clean wall space for text overlay."),

    (5, "X", "COS-Parenting-Story5-X-20260223.png",
     "Photorealistic editorial photograph of a Colorado Springs high school campus on a bright, clear late-winter morning. The shot is taken from the parking lot looking toward the main entrance of a modern suburban high school building with tan brick and large windows. The front doors are open, and three adults of diverse backgrounds are walking toward the entrance dressed in smart casual professional attire, carrying folders and looking purposeful. To the right foreground, at an outdoor folding table, four middle school students of diverse ethnicities are excitedly working on a small robotics project, with a young female teacher in a teal cardigan leaning in to help them. The table has colorful STEM materials including circuit boards, small wheels, and craft supplies. The sky is brilliant clear Colorado blue, with snow-capped Pikes Peak visible in the background above the school roofline. Late morning winter sunlight casts crisp shadows. A few bare trees line the school perimeter. No text, no words, no logos, no banners, no signs. Warm and inviting editorial photography style. Shot at 1200x675 pixels, 16:9 aspect ratio. Leave the upper third as open blue sky and school roofline for text overlay."),

    (5, "Facebook", "COS-Parenting-Story5-Facebook-20260223.png",
     "Photorealistic editorial photograph of a Colorado Springs high school campus on a bright, clear late-winter morning. The shot is taken from the parking lot looking toward the main entrance of a modern suburban high school building with tan brick and large windows. The front doors are open, and three adults of diverse backgrounds are walking toward the entrance dressed in smart casual professional attire, carrying folders. To the right foreground, at an outdoor folding table, four middle school students of diverse ethnicities are excitedly working on a small robotics project, with a young female teacher in a teal cardigan leaning in to help them. The table has colorful STEM materials. The sky is brilliant clear Colorado blue, with snow-capped Pikes Peak visible above the school roofline. Late morning winter sunlight casts crisp shadows. No text, no words, no logos, no banners, no signs. Warm and inviting editorial photography style. Shot at 1200x630 pixels, 1.91:1 aspect ratio. Leave the upper portion as open sky for text overlay."),

    (6, "X", "COS-Parenting-Story6-X-20260223.png",
     "Photorealistic editorial photograph of a family of three exploring a nature trail at the base of North Cheyenne Canon in Colorado Springs. A white father in his late 30s wearing a light jacket and small backpack walks on a dirt trail alongside his two children: a boy around age 8 and a girl around age 6, both in colorful winter jackets. The girl is pointing excitedly up into the tall Ponderosa pine trees along the trail. Dramatic red and orange rock formations rise on the left side of the trail. The forest floor has patches of winter-brown grass and a few small rocks. Dappled winter sunlight filters through the pine canopy, casting warm spots of light on the trail and family. In the background, the rugged canyon walls are visible, rising toward a brilliant blue Colorado sky. The mood is adventurous, joyful, and full of natural wonder. No text, no words, no logos. Warm and inviting editorial photography style with rich natural colors. Shot at 1200x675 pixels, 16:9 aspect ratio. Leave the upper third as pine canopy and open sky for text overlay."),

    (6, "Facebook", "COS-Parenting-Story6-Facebook-20260223.png",
     "Photorealistic editorial photograph of a family of three exploring a nature trail at the base of North Cheyenne Canon in Colorado Springs. A white father in his late 30s wearing a light jacket and small backpack walks on a dirt trail alongside his two children: a boy around age 8 and a girl around age 6, both in colorful winter jackets. The girl is pointing excitedly up into the tall Ponderosa pine trees along the trail. Dramatic red and orange rock formations rise on the left side. Dappled winter sunlight filters through the pine canopy. In the background, rugged canyon walls rise toward a brilliant blue Colorado sky. The mood is adventurous, joyful, and full of natural wonder. No text, no words, no logos. Warm and inviting editorial photography style. Shot at 1200x630 pixels, 1.91:1 aspect ratio. Leave the upper portion as pine canopy and sky for text overlay."),

    (7, "X", "COS-Parenting-Story7-X-20260223.png",
     "Photorealistic editorial photograph with a warm, humorous tone of a white mother in her late 30s sitting at a bright kitchen island looking comically overwhelmed. She has one hand on her forehead and wide eyes with a half-smile, looking at several colorful printed school calendars spread across the counter in front of her. There are pink, yellow, green, and blue sticky notes stuck to the calendars and counter. A silver laptop is open nearby. Behind her on the kitchen wall, a large white wall calendar is visible, covered in overlapping colored sticky notes and multiple dates circled in different colored markers. A white coffee mug sits on the counter next to her, with a few crumpled sticky notes nearby. The kitchen is bright and modern with white cabinets and warm wood countertops. Morning sunlight streams through a window to the left, creating warm, cheerful lighting. The mood is genuinely funny and relatable, not truly stressed. She is the picture of a parent in affectionate chaos. No text, no words, no logos, no readable writing on calendars or sticky notes. Warm and inviting editorial photography style with a humorous, lighthearted quality. Shot at 1200x675 pixels, 16:9 aspect ratio. Leave the upper third as clean kitchen wall and bright window light for text overlay."),

    (7, "Facebook", "COS-Parenting-Story7-Facebook-20260223.png",
     "Photorealistic editorial photograph with a warm, humorous tone of a white mother in her late 30s sitting at a bright kitchen island looking comically overwhelmed. She has one hand on her forehead and wide eyes with a half-smile, looking at several colorful printed school calendars spread across the counter. Pink, yellow, green, and blue sticky notes are stuck to the calendars and counter. A silver laptop is open nearby. Behind her on the kitchen wall, a large white wall calendar is covered in overlapping colored sticky notes and circled dates. A white coffee mug sits on the counter. The kitchen is bright and modern with white cabinets and warm wood countertops. Morning sunlight streams through a window to the left. The mood is genuinely funny and relatable. No text, no words, no logos, no readable writing on calendars or sticky notes. Warm and inviting editorial photography style with a humorous quality. Shot at 1200x630 pixels, 1.91:1 aspect ratio. Leave the upper portion as clean kitchen wall for text overlay."),
]


def generate_image(prompt, output_path, story_num, platform):
    """Generate a single image via Gemini API."""
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent?key={API_KEY}"
    payload = json.dumps({
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {"responseModalities": ["TEXT", "IMAGE"]}
    }).encode()

    req = urllib.request.Request(url, data=payload, headers={"Content-Type": "application/json"})
    try:
        resp = urllib.request.urlopen(req, timeout=120)
        data = json.loads(resp.read())
        parts = data["candidates"][0]["content"]["parts"]

        for part in parts:
            if "inlineData" in part:
                img_data = base64.b64decode(part["inlineData"]["data"])
                with open(output_path, "wb") as f:
                    f.write(img_data)
                size_kb = len(img_data) / 1024
                return True, f"{size_kb:.0f} KB"

        return False, "No image in response"

    except urllib.error.HTTPError as e:
        body = e.read().decode()
        msg = json.loads(body).get("error", {}).get("message", "Unknown error")[:100]
        return False, f"HTTP {e.code}: {msg}"
    except Exception as e:
        return False, str(e)[:100]


def main():
    print(f"Generating {len(IMAGES)} images with {MODEL}")
    print(f"Output: {IMAGES_DIR}")
    print(f"{'='*60}")

    results = []
    for i, (story_num, platform, filename, prompt) in enumerate(IMAGES):
        output_path = os.path.join(IMAGES_DIR, filename)
        label = f"Story {story_num} {platform:8s}"
        print(f"\n[{i+1:2d}/14] {label} ... ", end="", flush=True)

        start = time.time()
        success, detail = generate_image(prompt, output_path, story_num, platform)
        elapsed = time.time() - start

        if success:
            print(f"OK  ({detail}, {elapsed:.1f}s)")
        else:
            print(f"FAIL ({detail})")

        results.append((story_num, platform, filename, success, detail))

        # Rate limit: small pause between requests
        if i < len(IMAGES) - 1:
            time.sleep(2)

    # Summary
    ok = sum(1 for r in results if r[3])
    print(f"\n{'='*60}")
    print(f"Results: {ok}/{len(IMAGES)} images generated")

    if ok < len(IMAGES):
        print("\nFailed:")
        for story, plat, fname, success, detail in results:
            if not success:
                print(f"  Story {story} {plat}: {detail}")

    return 0 if ok == len(IMAGES) else 1


if __name__ == "__main__":
    sys.exit(main())
