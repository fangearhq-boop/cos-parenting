#!/usr/bin/env python3
"""
COS Parenting — Niche-Specific Claim Patterns

Loaded dynamically by verify-facts.py to extract parenting-niche claims
that go beyond the universal date/time extraction.

Claim types extracted:
  Priority 1 (HIGH):
    - Prices & costs ($34, $200-400, "free")
    - Age ranges (under 5, ages 16-24)
    - Phone numbers & hotlines
    - COS-specific locations (Starsmore, Liberty HS, Fort Carson, etc.)
    - Street addresses

  Priority 2 (MEDIUM):
    - School districts (D11, D20, D49, FFC8, etc.)
    - Statistics & percentages (26%, 41%)
    - Unit/population counts (9,000 units, 47,000 children)
    - Study/research references

  Priority 3 (LOW):
    - Organization references (CPSC, UCCS, AAP, etc.)
    - Product/brand names in recall context
    - Safety hazard classifications
"""

import re


def extract_niche_claims(text, claim_list, story_num):
    """
    Extract COS Parenting-specific claims from a text section.

    Called by verify-facts.py for each story section in each content file.
    Appends claim dicts to claim_list with keys:
        type, value, context, story, priority
    """

    def get_context(match, radius=50):
        ctx = text[max(0, match.start() - radius):match.end() + radius].strip()
        return re.sub(r'\s+', ' ', ctx)

    # =========================================================================
    # PRIORITY 1 (HIGH) — Most error-prone, verify first
    # =========================================================================

    # 1. PRICES & COSTS: "$34", "$200-$400", "$1,200"
    for match in re.finditer(
        r'\$[\d,]+(?:\.\d{2})?(?:\s*[-–—to]+\s*\$[\d,]+(?:\.\d{2})?)?',
        text
    ):
        claim_list.append({
            'type': 'Price',
            'value': match.group().strip(),
            'context': get_context(match, 40),
            'story': story_num,
            'priority': 1
        })

    # "Free" when associated with events/programs
    for match in re.finditer(
        r'\b[Ff]ree\b',
        text
    ):
        surrounding = text[max(0, match.start() - 40):match.end() + 40]
        if re.search(
            r'(?:admission|entry|event|parking|registration|program|class|'
            r'session|families|kids|children|parents|attend|open\s+to)',
            surrounding, re.IGNORECASE
        ):
            claim_list.append({
                'type': 'Price',
                'value': 'Free',
                'context': get_context(match, 40),
                'story': story_num,
                'priority': 1
            })

    # 2. AGE RANGES: "under 5", "ages 16-24", "kids under 5", "infant"
    for match in re.finditer(
        r'(?:(?:kids?|children|teens?|infants?|toddlers?|babies)\s+)?'
        r'(?:under|over|aged?|ages?)\s+\d{1,2}(?:\s*[-–to]+\s*\d{1,2})?|'
        r'ages?\s+\d{1,2}\+|'
        r'\d{1,2}\s*[-–]\s*\d{1,2}\s*(?:year|month|week)s?\s*(?:old)?',
        text, re.IGNORECASE
    ):
        claim_list.append({
            'type': 'Age Range',
            'value': match.group().strip(),
            'context': get_context(match, 40),
            'story': story_num,
            'priority': 1
        })

    # 3. PHONE NUMBERS & HOTLINES
    for match in re.finditer(
        r'\b\d{3}[-.\s]\d{3}[-.\s]\d{4}\b|'
        r'\b800[-.\s]\d{3}[-.\s]\d{4}\b|'
        r'\b\d{3}[-.\s]\d{4}\b',
        text
    ):
        claim_list.append({
            'type': 'Phone',
            'value': match.group().strip(),
            'context': get_context(match, 40),
            'story': story_num,
            'priority': 1
        })

    # 4. COS-SPECIFIC LOCATIONS & VENUES
    for match in re.finditer(
        r'(?:Liberty\s+High\s+School|Starsmore(?:\s+Discovery\s+Center)?|'
        r'North\s+Cheyenne\s+Ca[nñ]on|Palmer\s+High(?:\s+School)?|'
        r'Rockrimmon|Fort\s+Carson|Peterson\s+(?:SFB|Space\s+Force\s+Base)|'
        r'Garden\s+of\s+the\s+Gods|Manitou\s+Springs|Memorial\s+Park|'
        r'Penrose\s+Stadium|World\s+Arena|Broadmoor|'
        r'UCCS|Pikes?\s+Peak|Cheyenne\s+Mountain|'
        r'Bear\s+Creek\s+(?:Park|Nature\s+Center)|'
        r'Olympic\s+Training\s+Center|'
        r'El\s+Pomar\s+Youth\s+Sports\s+Park|'
        r'Rock\s+Ledge\s+Ranch)\b',
        text, re.IGNORECASE
    ):
        claim_list.append({
            'type': 'Location',
            'value': match.group().strip(),
            'context': get_context(match, 40),
            'story': story_num,
            'priority': 1
        })

    # 5. STREET ADDRESSES: "1234 N Academy Blvd"
    for match in re.finditer(
        r'\d+\s+(?:[NSEW]\.?\s+)?[A-Z][a-zA-Z]+(?:\s+[A-Z][a-zA-Z]+)*'
        r'\s+(?:St|Ave|Blvd|Dr|Rd|Way|Pkwy|Ln|Ct|Pl|Circle|Trail)\.?',
        text
    ):
        claim_list.append({
            'type': 'Address',
            'value': match.group().strip()[:60],
            'context': get_context(match, 40),
            'story': story_num,
            'priority': 1
        })

    # =========================================================================
    # PRIORITY 2 (MEDIUM) — Important but less error-prone
    # =========================================================================

    # 6. SCHOOL DISTRICTS: D11, D20, D49, D8, FFC8, District 20, etc.
    for match in re.finditer(
        r'\bD\d{1,2}\b|'
        r'\bFFC\s*\d{1,2}\b|'
        r'\b(?:Academy\s+)?District\s+\d{1,2}\b|'
        r'\bFountain[-\s]Fort\s+Carson\b|'
        r'\bHarrison\s+(?:School\s+)?District\b|'
        r'\bWidefield\s+(?:School\s+)?District\b|'
        r'\bCheyenne\s+Mountain\s+(?:School\s+)?District\b|'
        r'\bManitou\s+Springs\s+(?:School\s+)?District\b|'
        r'\bLewis[-\s]Palmer\s+(?:School\s+)?District\b|'
        r'\bFalcon\s+(?:School\s+)?District\b',
        text, re.IGNORECASE
    ):
        claim_list.append({
            'type': 'School District',
            'value': match.group().strip(),
            'context': get_context(match, 40),
            'story': story_num,
            'priority': 2
        })

    # 7. STATISTICS & PERCENTAGES
    for match in re.finditer(
        r'\d{1,3}(?:\.\d+)?%|'
        r'\b(?:one|two|three|four|five)\s+in\s+(?:four|five|three|ten|two|six|seven|eight|nine)',
        text, re.IGNORECASE
    ):
        claim_list.append({
            'type': 'Statistic',
            'value': match.group().strip(),
            'context': get_context(match, 40),
            'story': story_num,
            'priority': 2
        })

    # 8. UNIT/POPULATION COUNTS: "9,000 units", "47,000 children", "~1,100 young people"
    for match in re.finditer(
        r'(?:approximately\s+|about\s+|roughly\s+|~\s*|nearly\s+|more\s+than\s+|over\s+)?'
        r'[\d,]+(?:\.\d+)?\s+'
        r'(?:units?|children|kids|families|parents|spots?|seats?|'
        r'providers?|facilities|slots?|students?|people|residents|'
        r'service\s+members?|young\s+people)',
        text, re.IGNORECASE
    ):
        claim_list.append({
            'type': 'Count',
            'value': match.group().strip(),
            'context': get_context(match, 40),
            'story': story_num,
            'priority': 2
        })

    # 9. STUDY/RESEARCH REFERENCES
    for match in re.finditer(
        r'(?:study|research|report|survey|analysis)\s+'
        r'(?:found|shows?|suggests?|indicates?|reveals?|published|released|conducted)|'
        r'(?:according\s+to\s+(?:a|the)\s+(?:new\s+)?(?:study|report|survey))|'
        r'(?:University\s+of\s+\w+(?:\s+\w+)?)\s+(?:study|report|research)',
        text, re.IGNORECASE
    ):
        claim_list.append({
            'type': 'Study Finding',
            'value': match.group().strip(),
            'context': get_context(match, 60),
            'story': story_num,
            'priority': 2
        })

    # =========================================================================
    # PRIORITY 3 (LOW) — General claims, still worth logging
    # =========================================================================

    # 10. ORGANIZATION REFERENCES
    for match in re.finditer(
        r'\b(?:CPSC|Consumer\s+Product\s+Safety\s+Commission|'
        r'AAP|American\s+Academy\s+of\s+Pediatrics|'
        r'CDC|FDA|USDA|HHS|NIH|WHO|'
        r'El\s+Paso\s+County|'
        r'Colorado\s+Springs\s+(?:Chamber|City\s+Council|Planning\s+Commission'
        r'|Economic\s+Development\s+Corporation|Fire\s+Department|Police)|'
        r'Special\s+Olympics(?:\s+Colorado)?|'
        r'Colorado\s+Department\s+of\s+(?:Education|Human\s+Services))\b',
        text, re.IGNORECASE
    ):
        claim_list.append({
            'type': 'Organization',
            'value': match.group().strip(),
            'context': get_context(match, 40),
            'story': story_num,
            'priority': 3
        })

    # 11. PRODUCT/BRAND NAMES in recall context
    #     Only flagged when near recall/safety keywords to avoid false positives
    for match in re.finditer(
        r'\b(?:YCXXKJ|Uuoeebb|AiTuiTui|Joyful\s+Journeys)\b',
        text, re.IGNORECASE
    ):
        claim_list.append({
            'type': 'Product/Brand',
            'value': match.group().strip(),
            'context': get_context(match, 40),
            'story': story_num,
            'priority': 3
        })

    # 12. SAFETY HAZARD CLASSIFICATIONS
    for match in re.finditer(
        r'(?:drowning|choking|suffocation|entrapment|fall|strangulation|'
        r'respiratory\s+distress|burn|poisoning|laceration)\s+'
        r'(?:risk|hazard|danger|warning)',
        text, re.IGNORECASE
    ):
        claim_list.append({
            'type': 'Safety Claim',
            'value': match.group().strip(),
            'context': get_context(match, 40),
            'story': story_num,
            'priority': 3
        })

    # 13. WEBSITE/URL REFERENCES (for verifying links are correct)
    for match in re.finditer(
        r'(?:cpsc\.gov|amazon\.com|\w+\.colorado\.gov|'
        r'academydistrict20\.org|d11\.org|d49\.org)',
        text, re.IGNORECASE
    ):
        claim_list.append({
            'type': 'URL Reference',
            'value': match.group().strip(),
            'context': get_context(match, 40),
            'story': story_num,
            'priority': 3
        })
