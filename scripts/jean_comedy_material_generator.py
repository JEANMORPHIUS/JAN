"""
JEAN MORPHIUS - COMEDY MATERIAL GENERATOR
Bilingual Stand-Up Comedy Material System

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

PURPOSE:
Generate comedy material for Jean Morphius incorporating:
- Peter Kay style: Observational family comedy ("Peter Kay my mum, bilingually")
- Hasan Can Kaya: Observational conversational comedy (Turkish)
- Bill Bailey: Musical/intellectual comedy
- Eddie Izzard: Surreal stream-of-consciousness
- Sean Lock (RIP): Deadpan absurdism
- Milton Jones: One-liner master
- Gary Delaney: One-liner specialist

All delivered bilingually (French/English/Turkish).
"""

import json
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any, Optional
from dataclasses import dataclass, field
from enum import Enum


class ComedyStyle(Enum):
    """Comedy style influences"""
    PETER_KAY = "peter_kay"  # Observational family comedy
    HASAN_CAN_KAYA = "hasan_can_kaya"  # Observational conversational comedy (Turkish)
    BILL_BAILEY = "bill_bailey"  # Musical/intellectual
    EDDIE_IZZARD = "eddie_izzard"  # Surreal stream-of-consciousness
    SEAN_LOCK = "sean_lock"  # Deadpan absurdism
    MILTON_JONES = "milton_jones"  # One-liner master
    GARY_DELANEY = "gary_delaney"  # One-liner specialist


@dataclass
class ComedyMaterial:
    """Comedy material structure"""
    style: ComedyStyle
    category: str
    setup: str
    observation: str = ""
    wordplay: str = ""
    punchline: str = ""
    bilingual_delivery: str = ""
    delivery_notes: str = ""
    tags: List[str] = field(default_factory=list)


# Comedy Material Templates
COMEDY_TEMPLATES = {
    ComedyStyle.PETER_KAY: {
        "structure": ["setup", "observation", "bilingual_twist", "punchline"],
        "delivery": "Warm, relatable, nostalgic",
        "example": {
            "setup": "Ma mère, elle... she does this thing where...",
            "observation": "Every time I call, she answers the phone like she's been waiting for hours",
            "bilingual_twist": "C'est ma mère... she's like 'Allo? Allo? C'est toi?'",
            "punchline": "Like I'm calling from 1995 and she's been holding the phone since then"
        }
    },
    ComedyStyle.MILTON_JONES: {
        "structure": ["setup", "wordplay", "punchline"],
        "delivery": "Rapid, punchy",
        "example": {
            "setup": "Ma mère dit... my mum says...",
            "wordplay": "I'm not old, I'm vintage. Like a bottle of wine that's been open too long.",
            "punchline": "She's not vintage, she's vinegar."
        }
    },
    ComedyStyle.GARY_DELANEY: {
        "structure": ["setup", "wordplay", "punchline"],
        "delivery": "Rapid, dark",
        "example": {
            "setup": "My mum's cooking...",
            "wordplay": "She says it's organic. It's been organic for three weeks.",
            "punchline": "It's not organic, it's archaeology."
        }
    },
    ComedyStyle.EDDIE_IZZARD: {
        "structure": ["starting_point", "tangential_flow", "bilingual_switching", "surreal_conclusion"],
        "delivery": "Flowing, tangential",
        "example": {
            "starting_point": "C'est comme... it's like... imagine if...",
            "tangential_flow": "Your mum is a phone. No, wait. Your phone is a mum. No...",
            "bilingual_switching": "Ma mère, elle... she's like a phone that never stops ringing...",
            "surreal_conclusion": "But the phone is also a bird. And the bird is also a mum. Logic."
        }
    },
    ComedyStyle.BILL_BAILEY: {
        "structure": ["setup", "musical_element", "bilingual_delivery", "punchline"],
        "delivery": "Musical, rhythmic",
        "example": {
            "setup": "Ma mère chante... my mum sings...",
            "musical_element": "[Beat] She sings like... [rhythm] ...a bird that's been to music school",
            "bilingual_delivery": "Elle chante... she sings... [beat] ...in two languages at once",
            "punchline": "She's not bilingual, she's bi-musical."
        }
    },
    ComedyStyle.SEAN_LOCK: {
        "structure": ["setup", "absurd_twist", "deadpan_delivery"],
        "delivery": "Deadpan, straight-faced",
        "example": {
            "setup": "C'est normal, non? It's normal, right?",
            "absurd_twist": "My mum puts salt in everything. Even salt.",
            "deadpan_delivery": "She's not seasoning food, she's preserving it for future generations."
        }
    },
    ComedyStyle.HASAN_CAN_KAYA: {
        "structure": ["conversational_setup", "observational_flow", "bilingual_conversation", "relatable_punchline"],
        "delivery": "Conversational, observational, natural flow",
        "example": {
            "conversational_setup": "Bak, şimdi... look, now... ma mère, elle...",
            "observational_flow": "We're talking, right? Normal conversation. But then she says...",
            "bilingual_conversation": "O diyor ki... she says... 'Sen ne yapıyorsun?' What are you doing?",
            "relatable_punchline": "Like I'm not doing anything. I'm just existing. But that's apparently suspicious."
        }
    }
}


# Family Comedy Topics (Peter Kay style)
FAMILY_COMEDY_TOPICS = [
    "Mum's phone calls",
    "Mum's cooking",
    "Mum's advice",
    "Mum's reactions",
    "Mum's sayings",
    "Family gatherings",
    "Mum's habits",
    "Mum's stories",
    "Mum's shopping",
    "Mum's TV watching",
    "Mum's cleaning",
    "Mum's worrying",
    "Mum's cooking disasters",
    "Mum's sayings in two languages",
    "Mum's reactions to technology",
    "Mum's stories about the past",
    "Mum's advice that makes no sense",
    "Mum's habits that drive you crazy",
    "Mum's love language",
    "Mum's way of saying things"
]


def generate_peter_kay_style_material(topic: str) -> ComedyMaterial:
    """Generate Peter Kay style observational family comedy"""
    
    material = ComedyMaterial(
        style=ComedyStyle.PETER_KAY,
        category="Observational Family Comedy",
        setup=f"Ma mère, elle... she does this thing where...",
        observation=f"Every time {topic.lower()}, she...",
        bilingual_delivery=f"C'est ma mère... she's like...",
        punchline="Like she's been doing this since before I was born",
        delivery_notes="Warm, relatable, nostalgic. Bilingual code-switching mid-observation.",
        tags=["family", "mum", "observational", "bilingual", "peter_kay"]
    )
    
    return material


def generate_one_liner_material(style: ComedyStyle) -> ComedyMaterial:
    """Generate one-liner material (Milton Jones or Gary Delaney style)"""
    
    if style == ComedyStyle.MILTON_JONES:
        material = ComedyMaterial(
            style=ComedyStyle.MILTON_JONES,
            category="One-Liner",
            setup="Ma mère dit... my mum says...",
            wordplay="I'm not old, I'm vintage. Like a bottle of wine that's been open too long.",
            punchline="She's not vintage, she's vinegar.",
            delivery_notes="Rapid, punchy. Bilingual wordplay.",
            tags=["one_liner", "wordplay", "mum", "bilingual", "milton_jones"]
        )
    else:  # GARY_DELANEY
        material = ComedyMaterial(
            style=ComedyStyle.GARY_DELANEY,
            category="One-Liner (Dark)",
            setup="My mum's cooking...",
            wordplay="She says it's organic. It's been organic for three weeks.",
            punchline="It's not organic, it's archaeology.",
            delivery_notes="Rapid, dark. Bilingual dark humor.",
            tags=["one_liner", "dark", "mum", "bilingual", "gary_delaney"]
        )
    
    return material


def generate_surreal_material() -> ComedyMaterial:
    """Generate surreal stream-of-consciousness material (Eddie Izzard style)"""
    
    material = ComedyMaterial(
        style=ComedyStyle.EDDIE_IZZARD,
        category="Surreal Stream-of-Consciousness",
        setup="C'est comme... it's like... imagine if...",
        observation="Your mum is a phone. No, wait. Your phone is a mum. No...",
        bilingual_delivery="Ma mère, elle... she's like a phone that never stops ringing...",
        punchline="But the phone is also a bird. And the bird is also a mum. Logic.",
        delivery_notes="Flowing, tangential. Seamless bilingual switching.",
        tags=["surreal", "stream_of_consciousness", "mum", "bilingual", "eddie_izzard"]
    )
    
    return material


def generate_musical_comedy_material() -> ComedyMaterial:
    """Generate musical comedy material (Bill Bailey style)"""
    
    material = ComedyMaterial(
        style=ComedyStyle.BILL_BAILEY,
        category="Musical Comedy",
        setup="Ma mère chante... my mum sings...",
        observation="[Beat] She sings like... [rhythm] ...a bird that's been to music school",
        bilingual_delivery="Elle chante... she sings... [beat] ...in two languages at once",
        punchline="She's not bilingual, she's bi-musical.",
        delivery_notes="Musical, rhythmic. Bilingual musical comedy.",
        tags=["musical", "comedy", "mum", "bilingual", "bill_bailey"]
    )
    
    return material


def generate_deadpan_material() -> ComedyMaterial:
    """Generate deadpan absurdism material (Sean Lock style)"""
    
    material = ComedyMaterial(
        style=ComedyStyle.SEAN_LOCK,
        category="Deadpan Absurdism",
        setup="C'est normal, non? It's normal, right?",
        observation="My mum puts salt in everything. Even salt.",
        punchline="She's not seasoning food, she's preserving it for future generations.",
        delivery_notes="Deadpan, straight-faced. Bilingual deadpan.",
        tags=["deadpan", "absurdism", "mum", "bilingual", "sean_lock"]
    )
    
    return material


def generate_hasan_can_kaya_material(topic: str) -> ComedyMaterial:
    """Generate Hasan Can Kaya style observational conversational comedy"""
    
    material = ComedyMaterial(
        style=ComedyStyle.HASAN_CAN_KAYA,
        category="Observational Conversational Comedy",
        setup=f"Bak, şimdi... look, now... ma mère, elle...",
        observation=f"We're talking, right? Normal conversation about {topic.lower()}. But then...",
        bilingual_delivery=f"O diyor ki... she says... 'Sen ne yapıyorsun?' What are you doing?",
        punchline="Like I'm not doing anything. I'm just existing. But that's apparently suspicious.",
        delivery_notes="Conversational, observational, natural flow. Bilingual conversational (Turkish/French/English).",
        tags=["conversational", "observational", "mum", "bilingual", "hasan_can_kaya", "turkish"]
    )
    
    return material


def generate_comedy_collection(count: int = 20) -> List[ComedyMaterial]:
    """Generate a collection of comedy material"""
    
    materials = []
    
    # Peter Kay style (30% - main focus)
    peter_kay_count = int(count * 0.3)
    for i in range(peter_kay_count):
        topic = FAMILY_COMEDY_TOPICS[i % len(FAMILY_COMEDY_TOPICS)]
        materials.append(generate_peter_kay_style_material(topic))
    
    # Hasan Can Kaya style (20% - conversational observational)
    hasan_count = int(count * 0.2)
    for i in range(hasan_count):
        topic = FAMILY_COMEDY_TOPICS[i % len(FAMILY_COMEDY_TOPICS)]
        materials.append(generate_hasan_can_kaya_material(topic))
    
    # One-liners (25% - Milton Jones + Gary Delaney)
    one_liner_count = int(count * 0.25)
    for i in range(one_liner_count):
        style = ComedyStyle.MILTON_JONES if i % 2 == 0 else ComedyStyle.GARY_DELANEY
        materials.append(generate_one_liner_material(style))
    
    # Surreal (8% - Eddie Izzard)
    surreal_count = int(count * 0.08)
    for i in range(surreal_count):
        materials.append(generate_surreal_material())
    
    # Musical (8% - Bill Bailey)
    musical_count = int(count * 0.08)
    for i in range(musical_count):
        materials.append(generate_musical_comedy_material())
    
    # Deadpan (9% - Sean Lock)
    deadpan_count = int(count * 0.09)
    for i in range(deadpan_count):
        materials.append(generate_deadpan_material())
    
    return materials


def save_comedy_collection(materials: List[ComedyMaterial], output_dir: Path):
    """Save comedy collection to JSON"""
    
    output_dir.mkdir(parents=True, exist_ok=True)
    
    collection = {
        "timestamp": datetime.now().isoformat(),
        "total_materials": len(materials),
        "styles": {
            style.value: sum(1 for m in materials if m.style == style)
            for style in ComedyStyle
        },
        "materials": [
            {
                "style": material.style.value,
                "category": material.category,
                "setup": material.setup,
                "observation": material.observation,
                "wordplay": material.wordplay,
                "punchline": material.punchline,
                "bilingual_delivery": material.bilingual_delivery,
                "delivery_notes": material.delivery_notes,
                "tags": material.tags
            }
            for material in materials
        ]
    }
    
    output_file = output_dir / f"jean_comedy_material_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(collection, f, indent=2, ensure_ascii=False)
    
    return output_file


if __name__ == "__main__":
    print("=== JEAN MORPHIUS - COMEDY MATERIAL GENERATOR ===")
    print("\nGenerating comedy material collection...")
    
    materials = generate_comedy_collection(count=50)
    
    output_dir = Path(__file__).parent.parent / "data" / "jean_comedy"
    output_file = save_comedy_collection(materials, output_dir)
    
    print(f"\nGenerated {len(materials)} comedy materials")
    print(f"\nStyle breakdown:")
    for style in ComedyStyle:
        count = sum(1 for m in materials if m.style == style)
        print(f"  {style.value}: {count}")
    
    print(f"\nCollection saved to: {output_file}")
    print("\nComedy material generation complete!")
