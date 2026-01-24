"""
JEAN MORPHIUS - COMEDY TEMPLATE LIBRARY
Comprehensive Template Library for All Comedy Styles

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

PURPOSE:
Comprehensive template library for all comedy styles
Faster material generation with better quality
"""

import json
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any
from enum import Enum


class ComedyStyle(Enum):
    """Comedy style influences"""
    PETER_KAY = "peter_kay"
    HASAN_CAN_KAYA = "hasan_can_kaya"
    BILL_BAILEY = "bill_bailey"
    EDDIE_IZZARD = "eddie_izzard"
    SEAN_LOCK = "sean_lock"
    MILTON_JONES = "milton_jones"
    GARY_DELANEY = "gary_delaney"


# Comprehensive Template Library
COMEDY_TEMPLATE_LIBRARY = {
    ComedyStyle.PETER_KAY: {
        "name": "Peter Kay - Observational Family Comedy",
        "description": "Warm, relatable, nostalgic family observations",
        "structure": {
            "setup": "Ma mère, elle... she does this thing where...",
            "observation": "[Mum's specific behavior or habit]",
            "bilingual_twist": "C'est ma mère... she's like...",
            "punchline": "[Relatable truth that everyone recognizes]"
        },
        "delivery_notes": {
            "tone": "Warm, relatable, nostalgic",
            "pace": "Conversational, not rushed",
            "bilingual_flow": "Seamless French/English switching",
            "emphasis": "On the relatable truth"
        },
        "example_topics": [
            "Mum's phone calls",
            "Mum's cooking",
            "Mum's advice",
            "Mum's reactions",
            "Mum's sayings"
        ],
        "example_material": {
            "setup": "Ma mère, elle... she does this thing where every time I call...",
            "observation": "She answers the phone like she's been waiting for hours",
            "bilingual_twist": "C'est ma mère... she's like 'Allo? Allo? C'est toi?'",
            "punchline": "Like I'm calling from 1995 and she's been holding the phone since then"
        }
    },
    ComedyStyle.HASAN_CAN_KAYA: {
        "name": "Hasan Can Kaya - Observational Conversational Comedy",
        "description": "Natural, flowing conversation with observational humor",
        "structure": {
            "conversational_setup": "Bak, şimdi... look, now... ma mère, elle...",
            "observational_flow": "We're talking, right? Normal conversation. But then...",
            "bilingual_conversation": "O diyor ki... she says... 'Sen ne yapıyorsun?' What are you doing?",
            "relatable_punchline": "[Observation that everyone recognizes from conversation]"
        },
        "delivery_notes": {
            "tone": "Conversational, natural, observational",
            "pace": "Natural conversation flow",
            "bilingual_flow": "Turkish/French/English seamless switching",
            "emphasis": "On the natural conversation observation"
        },
        "example_topics": [
            "Conversations with mum",
            "Everyday conversations",
            "Family conversations",
            "Cultural conversations"
        ],
        "example_material": {
            "conversational_setup": "Bak, şimdi... look, now... ma mère, elle...",
            "observational_flow": "We're talking, right? Normal conversation about nothing. But then...",
            "bilingual_conversation": "O diyor ki... she says... 'Sen ne yapıyorsun?' What are you doing?",
            "relatable_punchline": "Like I'm not doing anything. I'm just existing. But that's apparently suspicious."
        }
    },
    ComedyStyle.MILTON_JONES: {
        "name": "Milton Jones - One-Liner Master",
        "description": "Rapid-fire one-liners with wordplay",
        "structure": {
            "setup": "Ma mère dit... my mum says...",
            "wordplay": "[Clever wordplay or pun]",
            "punchline": "[Surreal twist on the wordplay]"
        },
        "delivery_notes": {
            "tone": "Rapid, punchy, surreal",
            "pace": "Quick delivery",
            "bilingual_flow": "Bilingual wordplay",
            "emphasis": "On the wordplay and twist"
        },
        "example_material": {
            "setup": "Ma mère dit... my mum says...",
            "wordplay": "I'm not old, I'm vintage. Like a bottle of wine that's been open too long.",
            "punchline": "She's not vintage, she's vinegar."
        }
    },
    ComedyStyle.GARY_DELANEY: {
        "name": "Gary Delaney - One-Liner Specialist (Dark)",
        "description": "Rapid-fire dark one-liners with wordplay",
        "structure": {
            "setup": "My mum's [topic]...",
            "wordplay": "[Dark wordplay or pun]",
            "punchline": "[Dark twist on the wordplay]"
        },
        "delivery_notes": {
            "tone": "Rapid, dark, punchy",
            "pace": "Quick delivery",
            "bilingual_flow": "Bilingual dark wordplay",
            "emphasis": "On the dark wordplay and twist"
        },
        "example_material": {
            "setup": "My mum's cooking...",
            "wordplay": "She says it's organic. It's been organic for three weeks.",
            "punchline": "It's not organic, it's archaeology."
        }
    },
    ComedyStyle.EDDIE_IZZARD: {
        "name": "Eddie Izzard - Surreal Stream-of-Consciousness",
        "description": "Surreal, flowing, tangential observations",
        "structure": {
            "starting_point": "C'est comme... it's like... imagine if...",
            "tangential_flow": "[Connected absurdity, flowing logic]",
            "bilingual_switching": "Ma mère, elle... she's like...",
            "surreal_conclusion": "[Logical illogic conclusion]"
        },
        "delivery_notes": {
            "tone": "Flowing, tangential, surreal",
            "pace": "Natural flow, not rushed",
            "bilingual_flow": "Seamless language switching",
            "emphasis": "On the surreal logic flow"
        },
        "example_material": {
            "starting_point": "C'est comme... it's like... imagine if...",
            "tangential_flow": "Your mum is a phone. No, wait. Your phone is a mum. No...",
            "bilingual_switching": "Ma mère, elle... she's like a phone that never stops ringing...",
            "surreal_conclusion": "But the phone is also a bird. And the bird is also a mum. Logic."
        }
    },
    ComedyStyle.BILL_BAILEY: {
        "name": "Bill Bailey - Musical Comedy",
        "description": "Comedy through music and rhythm",
        "structure": {
            "setup": "Ma mère chante... my mum sings...",
            "musical_element": "[Beat, rhythm, melody description]",
            "bilingual_delivery": "Elle chante... she sings... [beat] ...in two languages at once",
            "punchline": "[Musical/comedy fusion]"
        },
        "delivery_notes": {
            "tone": "Musical, rhythmic, intellectual",
            "pace": "Rhythm-based",
            "bilingual_flow": "Bilingual musical comedy",
            "emphasis": "On the musical element and comedy fusion"
        },
        "example_material": {
            "setup": "Ma mère chante... my mum sings...",
            "musical_element": "[Beat] She sings like... [rhythm] ...a bird that's been to music school",
            "bilingual_delivery": "Elle chante... she sings... [beat] ...in two languages at once",
            "punchline": "She's not bilingual, she's bi-musical."
        }
    },
    ComedyStyle.SEAN_LOCK: {
        "name": "Sean Lock - Deadpan Absurdism",
        "description": "Deadpan delivery of absurd observations",
        "structure": {
            "setup": "C'est normal, non? It's normal, right?",
            "absurd_twist": "[Surreal but logical observation]",
            "deadpan_delivery": "[Straight-faced absurd conclusion]"
        },
        "delivery_notes": {
            "tone": "Deadpan, straight-faced, absurd",
            "pace": "Deliberate, not rushed",
            "bilingual_flow": "Deadpan in French/English",
            "emphasis": "On the deadpan delivery of absurdity"
        },
        "example_material": {
            "setup": "C'est normal, non? It's normal, right?",
            "absurd_twist": "My mum puts salt in everything. Even salt.",
            "deadpan_delivery": "She's not seasoning food, she's preserving it for future generations."
        }
    }
}


def generate_template_library_report() -> Dict[str, Any]:
    """Generate comprehensive template library report"""
    
    return {
        "timestamp": datetime.now().isoformat(),
        "total_templates": len(COMEDY_TEMPLATE_LIBRARY),
        "templates": {
            style.value: {
                "name": template["name"],
                "description": template["description"],
                "structure": template["structure"],
                "delivery_notes": template["delivery_notes"],
                "example_material": template["example_material"]
            }
            for style, template in COMEDY_TEMPLATE_LIBRARY.items()
        },
        "usage": "Use templates to generate comedy material in specific styles",
        "status": "template_library_complete"
    }


def save_template_library(output_dir: Path):
    """Save template library to JSON"""
    
    output_dir.mkdir(parents=True, exist_ok=True)
    
    report = generate_template_library_report()
    output_file = output_dir / f"comedy_template_library_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    
    return output_file, report


if __name__ == "__main__":
    print("=== JEAN MORPHIUS - COMEDY TEMPLATE LIBRARY ===")
    print("\nGenerating template library...")
    
    output_dir = Path(__file__).parent.parent / "data" / "jean_comedy"
    output_file, report = save_template_library(output_dir)
    
    print(f"\nTotal Templates: {report['total_templates']}")
    print(f"\nTemplates:")
    for style, template in report['templates'].items():
        print(f"  - {template['name']}")
    
    print(f"\nTemplate library saved to: {output_file}")
    print("\nTemplate library complete!")
