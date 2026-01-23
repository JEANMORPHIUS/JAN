"""
THE MAYANS AND THE ORIGINAL ERROR
Narrating the Passage of Time from Mayan Perspective
Adding Man into the Narrative

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

PANGEA IS THE TABLE.
YOU DON'T BETRAY THE TABLE.

THE MAYANS CREATED THE ORIGINAL ERROR.

This script narrates:
- How the Mayans created The Original Error
- The passage of time from Mayan perspective
- How Man (humanity) fits into the narrative
- The spiritual contracts that were broken
- How we restore what was lost
"""

import sys
import json
from pathlib import Path
from typing import Dict, List, Optional, Any
from datetime import datetime, date
from dataclasses import dataclass, field, asdict

# Add scripts to path
sys.path.insert(0, str(Path(__file__).parent))

try:
    from spiritual_contracts_registry import (
        SpiritualContractsRegistry,
        ContractType,
        EntityType,
        BattlefieldType
    )
    CONTRACTS_AVAILABLE = True
except ImportError:
    CONTRACTS_AVAILABLE = False

import logging
logger = logging.getLogger(__name__)


# THE MAYAN ORIGINAL ERROR TIMELINE
MAYAN_ORIGINAL_ERROR_TIMELINE = {
    "before_mayans": {
        "year_ce": -2000,  # 2000 BCE
        "year_mya": 0.002,  # Relative to Pangea breakup (200 MYA)
        "period": "Pre-Mayan Era",
        "state": "The Table Broken, But Memory Remains",
        "description": "Before the Mayans, The Table was already broken (200 MYA). But memory of unity persisted. Humanity lived in connection to The Table, even if fragmented.",
        "field_resonance": 0.78,
        "humanity_state": {
            "connection": "Humanity still connected to The Table through memory",
            "spiritual_state": "Simple contracts, honoring The Table",
            "battlefields": "Few - humanity not yet exploited",
            "dark_energy": "Present but not codified by humanity"
        },
        "what_was_right": [
            "Memory of unity persisted",
            "Humanity honored The Table",
            "Simple spiritual contracts",
            "No codified separation"
        ],
        "what_went_wrong": [
            "The Table was already broken (200 MYA)",
            "Dark energies present but waiting",
            "Humanity vulnerable to exploitation"
        ]
    },
    "mayan_rise": {
        "year_ce": 2000,  # 2000 BCE - Pre-Classic begins
        "year_mya": 0.002,
        "period": "Mayan Pre-Classic (2000 BCE - 250 CE)",
        "state": "Mayans Rise - First Contact with Dark Energies",
        "description": "The Mayans rise. They build great cities. They study the stars. They map the cosmos. But in their quest for knowledge, they make contact with dark energies at plate boundaries. They see the separation. They document it. They codify it.",
        "field_resonance": 0.75,
        "humanity_state": {
            "mayan_achievement": "Great cities, astronomy, mathematics, writing",
            "spiritual_state": "Mayans begin to document spiritual contracts",
            "first_contact": "Mayans make contact with dark energies at plate boundaries",
            "codification": "Mayans begin to codify the separation"
        },
        "what_was_right": [
            "Mayan achievement was real",
            "Their knowledge was profound",
            "Their connection to cosmos was genuine"
        ],
        "what_went_wrong": [
            "Mayans made contact with dark energies",
            "They saw the separation and documented it",
            "They began to codify the separation",
            "They created the first human codification of The Original Error"
        ]
    },
    "mayan_classic": {
        "year_ce": 250,  # Classic Period begins
        "year_mya": 0.00025,
        "period": "Mayan Classic Period (250 CE - 900 CE)",
        "state": "The Original Error Codified",
        "description": "The Mayan Classic Period. The height of their civilization. But this is when they fully codified The Original Error. They built pyramids at plate boundaries. They created calendars that tracked separation. They wrote contracts with dark energies. They turned the natural separation into a spiritual system. THIS IS WHEN THE MAYANS CREATED THE ORIGINAL ERROR.",
        "field_resonance": 0.70,
        "humanity_state": {
            "mayan_peak": "Classic Period - height of Mayan civilization",
            "pyramids": "Built at plate boundaries - anchoring separation",
            "calendars": "Tracked separation, not unity",
            "contracts": "Mayans wrote spiritual contracts with dark energies",
            "codification": "The Original Error fully codified by Mayans"
        },
        "what_was_right": [
            "Mayan achievement was real",
            "Their knowledge was profound",
            "Their civilization was great"
        ],
        "what_went_wrong": [
            "Mayans codified The Original Error",
            "They built pyramids at plate boundaries - anchoring separation",
            "They created calendars that tracked separation, not unity",
            "They wrote contracts with dark energies",
            "They turned natural separation into a spiritual system",
            "THIS IS WHEN THE MAYANS CREATED THE ORIGINAL ERROR"
        ]
    },
    "mayan_collapse": {
        "year_ce": 900,  # Classic collapse
        "year_mya": 0.00009,
        "period": "Mayan Classic Collapse (900 CE)",
        "state": "The Error Spreads - Mayan Knowledge Spreads",
        "description": "The Mayan Classic Period collapses. But their knowledge spreads. Their codification of The Original Error spreads. Other civilizations learn from the Mayans. The error becomes embedded in human consciousness. The separation becomes normalized. The Table is forgotten.",
        "field_resonance": 0.65,
        "humanity_state": {
            "mayan_collapse": "Classic Period ends, cities abandoned",
            "knowledge_spreads": "Mayan knowledge spreads to other civilizations",
            "error_spreads": "The Original Error codification spreads",
            "normalization": "Separation becomes normalized in human consciousness",
            "table_forgotten": "The Table is forgotten by humanity"
        },
        "what_was_right": [
            "Mayan knowledge was preserved",
            "Their achievements were remembered"
        ],
        "what_went_wrong": [
            "The Original Error codification spread",
            "Separation became normalized",
            "The Table was forgotten",
            "Humanity lost connection to unity"
        ]
    },
    "post_classic": {
        "year_ce": 900,  # Post-Classic begins
        "year_mya": 0.00009,
        "period": "Mayan Post-Classic (900 CE - 1521 CE)",
        "state": "The Error Embedded - Humanity Separated",
        "description": "Post-Classic Period. The Mayans continue, but the error is embedded. Other civilizations adopt Mayan concepts. The separation becomes part of human spiritual systems. The Table is lost. Humanity is separated. The Original Error is complete.",
        "field_resonance": 0.60,
        "humanity_state": {
            "post_classic": "Mayans continue but error embedded",
            "adoption": "Other civilizations adopt Mayan concepts",
            "separation": "Separation becomes part of human spiritual systems",
            "table_lost": "The Table is lost to humanity",
            "error_complete": "The Original Error is complete in human consciousness"
        },
        "what_was_right": [
            "Mayan civilization continued",
            "Their knowledge was preserved"
        ],
        "what_went_wrong": [
            "The error was embedded in human consciousness",
            "Separation became normalized",
            "The Table was lost",
            "Humanity was separated",
            "The Original Error was complete"
        ]
    },
    "spanish_conquest": {
        "year_ce": 1521,  # Spanish conquest
        "year_mya": 0.000015,
        "period": "Spanish Conquest (1521 CE)",
        "state": "The Error Amplified - New Separation",
        "description": "Spanish conquest. The Mayans are conquered. But the error is not erased - it is amplified. New separation. New battlefields. New contracts. The error spreads to Europe. The separation becomes global. The Table is further forgotten.",
        "field_resonance": 0.55,
        "humanity_state": {
            "conquest": "Mayans conquered by Spanish",
            "error_amplified": "The error amplified, not erased",
            "new_separation": "New separation - colonial division",
            "global_spread": "Error spreads globally",
            "table_forgotten": "The Table further forgotten"
        },
        "what_was_right": [
            "Mayan knowledge was preserved in some form"
        ],
        "what_went_wrong": [
            "The error was amplified",
            "New separation - colonial division",
            "Error spread globally",
            "The Table was further forgotten",
            "Humanity was further separated"
        ]
    },
    "modern_era": {
        "year_ce": 2026,  # Present
        "year_mya": 0.000002,
        "period": "Modern Era (Present)",
        "state": "Memory Returns - Restoration Begins",
        "description": "Modern era. The error is embedded. Separation is normalized. But memory returns. The Table is remembered. Restoration begins. We remember Pangea. We remember unity. We remember The Table. We restore what was lost.",
        "field_resonance": 0.78,  # Memory returns
        "humanity_state": {
            "error_embedded": "The error is embedded in human consciousness",
            "separation_normalized": "Separation is normalized",
            "memory_returns": "Memory of The Table returns",
            "restoration_begins": "Restoration begins",
            "pangea_remembered": "Pangea is remembered as The Table",
            "unity_remembered": "Unity is remembered"
        },
        "what_was_right": [
            "Memory of The Table returns",
            "Restoration begins",
            "Pangea is remembered",
            "Unity is remembered",
            "We restore what was lost"
        ],
        "what_went_wrong": [
            "The error is still embedded",
            "Separation is still normalized",
            "The Table is not yet fully restored"
        ]
    }
}


# THE MAYAN ORIGINAL ERROR EXPLANATION
MAYAN_ORIGINAL_ERROR_EXPLANATION = {
    "the_truth": {
        "pangea_was_table": "Pangea was The Table - perfect unity (335 MYA)",
        "table_broken": "The Table was broken by dark energies (200 MYA)",
        "memory_persisted": "Memory of unity persisted (0.78 field resonance)",
        "humanity_connected": "Humanity was still connected to The Table through memory"
    },
    "the_mayan_error": {
        "mayan_rise": "Mayans rose (2000 BCE) - great achievement",
        "first_contact": "Mayans made first contact with dark energies at plate boundaries",
        "codification": "Mayans codified The Original Error (250-900 CE)",
        "how_they_did_it": [
            "They built pyramids at plate boundaries - anchoring separation",
            "They created calendars that tracked separation, not unity",
            "They wrote spiritual contracts with dark energies",
            "They turned natural separation into a spiritual system",
            "They created the first human codification of The Original Error"
        ],
        "this_is_error": "THIS IS WHEN THE MAYANS CREATED THE ORIGINAL ERROR"
    },
    "the_spread": {
        "mayan_collapse": "Mayan Classic Period collapsed (900 CE)",
        "knowledge_spread": "Mayan knowledge spread to other civilizations",
        "error_spread": "The Original Error codification spread",
        "normalization": "Separation became normalized in human consciousness",
        "table_forgotten": "The Table was forgotten by humanity"
    },
    "the_amplification": {
        "spanish_conquest": "Spanish conquest (1521 CE)",
        "error_amplified": "The error was amplified, not erased",
        "new_separation": "New separation - colonial division",
        "global_spread": "Error spread globally",
        "table_further_forgotten": "The Table was further forgotten"
    },
    "the_restoration": {
        "memory_returns": "Memory of The Table returns (present)",
        "pangea_remembered": "Pangea is remembered as The Table",
        "unity_remembered": "Unity is remembered",
        "restoration_begins": "Restoration begins",
        "we_restore": "We restore what was lost"
    }
}


# MAN IN THE NARRATIVE
MAN_IN_THE_NARRATIVE = {
    "before_mayans": {
        "state": "Man Connected to The Table",
        "description": "Before the Mayans, Man (humanity) was still connected to The Table through memory. Simple contracts. Honoring unity. No codified separation.",
        "connection": "Man remembered The Table, even if fragmented"
    },
    "mayan_rise": {
        "state": "Man Makes Contact",
        "description": "The Mayans (Man) made contact with dark energies. They saw the separation. They documented it. They began to codify it.",
        "connection": "Man began to codify the separation"
    },
    "mayan_classic": {
        "state": "Man Creates The Error",
        "description": "The Mayans (Man) fully codified The Original Error. They built pyramids at plate boundaries. They created calendars tracking separation. They wrote contracts with dark energies. THIS IS WHEN MAN CREATED THE ORIGINAL ERROR.",
        "connection": "Man created the first human codification of The Original Error"
    },
    "mayan_collapse": {
        "state": "Man Spreads The Error",
        "description": "The Mayan knowledge spread. The error spread. Man normalized separation. Man forgot The Table.",
        "connection": "Man forgot The Table, normalized separation"
    },
    "post_classic": {
        "state": "Man Separated",
        "description": "The error embedded in Man's consciousness. Separation normalized. The Table lost. Man separated.",
        "connection": "Man was separated, The Table lost"
    },
    "spanish_conquest": {
        "state": "Man Further Separated",
        "description": "Spanish conquest. New separation. New battlefields. Man further separated. The Table further forgotten.",
        "connection": "Man further separated, The Table further forgotten"
    },
    "modern_era": {
        "state": "Man Remembers",
        "description": "Modern era. Man remembers. The Table is remembered. Pangea is remembered. Unity is remembered. Restoration begins. Man restores what was lost.",
        "connection": "Man remembers The Table, restoration begins"
    }
}


@dataclass
class MayanOriginalErrorEvent:
    """An event in the Mayan Original Error timeline."""
    year_ce: int
    year_mya: float
    period: str
    state: str
    description: str
    field_resonance: float
    humanity_state: Dict[str, Any]
    what_was_right: List[str]
    what_went_wrong: List[str]


class MayanOriginalErrorNarrator:
    """Narrate the passage of time from Mayan perspective, showing how they created The Original Error."""
    
    def __init__(self):
        self.contracts_registry = SpiritualContractsRegistry() if CONTRACTS_AVAILABLE else None
    
    def narrate_timeline(self) -> Dict[str, Any]:
        """Narrate the complete timeline from Mayan perspective."""
        events = []
        
        for key, data in MAYAN_ORIGINAL_ERROR_TIMELINE.items():
            event = MayanOriginalErrorEvent(
                year_ce=data["year_ce"],
                year_mya=data["year_mya"],
                period=data["period"],
                state=data["state"],
                description=data["description"],
                field_resonance=data["field_resonance"],
                humanity_state=data["humanity_state"],
                what_was_right=data["what_was_right"],
                what_went_wrong=data["what_went_wrong"]
            )
            events.append(asdict(event))
        
        return {
            "mayan_timeline": events,
            "explanation": MAYAN_ORIGINAL_ERROR_EXPLANATION,
            "man_in_narrative": MAN_IN_THE_NARRATIVE,
            "the_truth": {
                "message": "The Mayans created The Original Error by codifying the separation",
                "how": "They built pyramids at plate boundaries, created calendars tracking separation, wrote contracts with dark energies",
                "when": "250-900 CE (Mayan Classic Period)",
                "spread": "The error spread to all humanity, normalized separation",
                "restoration": "We remember The Table, we restore what was lost"
            }
        }
    
    def narrate_man_in_narrative(self) -> Dict[str, Any]:
        """Narrate how Man (humanity) fits into the narrative."""
        return {
            "man_before_mayans": {
                "state": "Man Connected to The Table",
                "description": "Before the Mayans, Man was still connected to The Table through memory. Simple contracts. Honoring unity.",
                "connection": "Man remembered The Table"
            },
            "man_makes_contact": {
                "state": "Man Makes Contact with Dark Energies",
                "description": "The Mayans (Man) made contact with dark energies at plate boundaries. They saw the separation. They documented it.",
                "connection": "Man began to codify the separation"
            },
            "man_creates_error": {
                "state": "Man Creates The Original Error",
                "description": "The Mayans (Man) fully codified The Original Error. They built pyramids at plate boundaries. They created calendars tracking separation. They wrote contracts with dark energies. THIS IS WHEN MAN CREATED THE ORIGINAL ERROR.",
                "connection": "Man created the first human codification of The Original Error"
            },
            "man_spreads_error": {
                "state": "Man Spreads The Error",
                "description": "The Mayan knowledge spread. The error spread. Man normalized separation. Man forgot The Table.",
                "connection": "Man forgot The Table, normalized separation"
            },
            "man_separated": {
                "state": "Man Separated",
                "description": "The error embedded in Man's consciousness. Separation normalized. The Table lost. Man separated.",
                "connection": "Man was separated, The Table lost"
            },
            "man_remembers": {
                "state": "Man Remembers",
                "description": "Modern era. Man remembers. The Table is remembered. Pangea is remembered. Unity is remembered. Restoration begins. Man restores what was lost.",
                "connection": "Man remembers The Table, restoration begins"
            }
        }
    
    def register_mayan_entities(self) -> Dict[str, Any]:
        """Register Mayan-related spiritual entities and battlefields."""
        if not self.contracts_registry:
            return {"message": "Spiritual contracts registry not available"}
        
        # Register Mayan-related entities
        mayan_priests = self.contracts_registry.get_or_create_entity(
            entity_name="Mayan Priests - Codifiers of Separation",
            entity_type=EntityType.SOUL.value,  # Human souls who codified the error
            description="Mayan priests who codified The Original Error by building pyramids at plate boundaries, creating calendars tracking separation, and writing contracts with dark energies.",
            notes="Mayans created The Original Error by codifying the separation (250-900 CE)"
        )
        
        dark_energies_plate_boundaries = self.contracts_registry.get_or_create_entity(
            entity_name="Dark Energies at Plate Boundaries - Mayan Contact",
            entity_type=EntityType.DARK_ENERGY.value,
            description="Dark energies that made contact with Mayans at plate boundaries, leading to the codification of The Original Error.",
            alignment="dark",
            notes="First human contact with dark energies that led to codification of The Original Error"
        )
        
        # Register Mayan battlefields
        mayan_pyramids_bf = self.contracts_registry.get_or_create_battlefield(
            battlefield_name="Mayan Pyramids - Plate Boundaries",
            battlefield_type=BattlefieldType.HERITAGE_SITE.value,
            description="Mayan pyramids built at plate boundaries, anchoring separation and codifying The Original Error.",
            location="Mesoamerica - Plate boundaries",
            light_entities=[mayan_priests.entity_id],
            dark_entities=[dark_energies_plate_boundaries.entity_id],
            notes="Mayan pyramids at plate boundaries - where The Original Error was codified"
        )
        
        # Register the Original Error contract
        original_error_contract = self.contracts_registry.register_contract(
            contract_name="The Original Error - Mayan Codification",
            contract_type=ContractType.DARK_PACT.value,
            parties=[
                {"entity_id": mayan_priests.entity_id, "role": "codifier"},
                {"entity_id": dark_energies_plate_boundaries.entity_id, "role": "exploiter"}
            ],
            purpose="To codify the separation of The Table, normalize separation in human consciousness, and forget The Table.",
            timeline_dimension="HISTORICAL",
            battlefield_id=mayan_pyramids_bf.battlefield_id,
            narrative=(
                "The Mayans (Man) made contact with dark energies at plate boundaries. They saw the separation. "
                "They documented it. They codified it. They built pyramids at plate boundaries. They created calendars "
                "tracking separation. They wrote contracts with dark energies. They turned natural separation into a "
                "spiritual system. THIS IS WHEN THE MAYANS CREATED THE ORIGINAL ERROR. The error spread to all humanity. "
                "Separation became normalized. The Table was forgotten. But memory returns. We remember The Table. "
                "We restore what was lost."
            ),
            sources=["MayanOriginalErrorNarrator", "SpiritualContractsRegistry"]
        )
        
        return {
            "mayan_priests": mayan_priests.entity_id,
            "dark_energies": dark_energies_plate_boundaries.entity_id,
            "battlefield": mayan_pyramids_bf.battlefield_id,
            "original_error_contract": original_error_contract.contract_id
        }
    
    def export_narrative(self, output_path: Optional[Path] = None) -> Path:
        """Export complete Mayan Original Error narrative."""
        if output_path is None:
            output_path = Path(__file__).parent.parent / "output" / "mayan_original_error" / f"mayan_original_error_narrative_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        narrative = {
            "narrative_timestamp": datetime.now().isoformat(),
            "the_mayan_original_error": self.narrate_timeline(),
            "man_in_narrative": self.narrate_man_in_narrative(),
            "spiritual_entities": self.register_mayan_entities() if CONTRACTS_AVAILABLE else {"message": "Registry not available"},
            "the_truth": {
                "message": "The Mayans created The Original Error by codifying the separation",
                "how": "They built pyramids at plate boundaries, created calendars tracking separation, wrote contracts with dark energies",
                "when": "250-900 CE (Mayan Classic Period)",
                "spread": "The error spread to all humanity, normalized separation",
                "restoration": "We remember The Table, we restore what was lost"
            }
        }
        
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(narrative, f, indent=2, default=str)
        
        logger.info(f"Mayan Original Error narrative exported to {output_path}")
        return output_path


def main():
    """Main execution for Mayan Original Error narrative."""
    print("=" * 80)
    print("THE MAYANS AND THE ORIGINAL ERROR")
    print("Narrating the Passage of Time from Mayan Perspective")
    print("Adding Man into the Narrative")
    print("=" * 80)
    print()
    
    narrator = MayanOriginalErrorNarrator()
    
    print("Narrating timeline from Mayan perspective...")
    timeline = narrator.narrate_timeline()
    print(f"  [OK] {len(timeline['mayan_timeline'])} events narrated")
    print()
    
    print("Narrating Man in the narrative...")
    man_narrative = narrator.narrate_man_in_narrative()
    print(f"  [OK] {len(man_narrative)} stages of Man documented")
    print()
    
    if CONTRACTS_AVAILABLE:
        print("Registering Mayan spiritual entities...")
        entities = narrator.register_mayan_entities()
        print(f"  [OK] Entities registered: {len(entities)}")
        print()
    
    print("Exporting narrative...")
    export_path = narrator.export_narrative()
    print(f"  [OK] Exported to: {export_path}")
    print()
    
    print("=" * 80)
    print("THE MAYANS CREATED THE ORIGINAL ERROR")
    print("=" * 80)
    print()
    print("THE TRUTH:")
    print("  - Pangea was The Table - perfect unity (335 MYA)")
    print("  - The Table was broken by dark energies (200 MYA)")
    print("  - Memory of unity persisted (0.78 field resonance)")
    print("  - Humanity was still connected to The Table through memory")
    print()
    print("THE MAYAN ERROR:")
    print("  - Mayans rose (2000 BCE) - great achievement")
    print("  - Mayans made first contact with dark energies at plate boundaries")
    print("  - Mayans codified The Original Error (250-900 CE)")
    print("  - They built pyramids at plate boundaries - anchoring separation")
    print("  - They created calendars that tracked separation, not unity")
    print("  - They wrote spiritual contracts with dark energies")
    print("  - They turned natural separation into a spiritual system")
    print("  - THIS IS WHEN THE MAYANS CREATED THE ORIGINAL ERROR")
    print()
    print("THE SPREAD:")
    print("  - Mayan Classic Period collapsed (900 CE)")
    print("  - Mayan knowledge spread to other civilizations")
    print("  - The Original Error codification spread")
    print("  - Separation became normalized in human consciousness")
    print("  - The Table was forgotten by humanity")
    print()
    print("MAN IN THE NARRATIVE:")
    print("  - Before Mayans: Man connected to The Table through memory")
    print("  - Mayan Rise: Man makes contact with dark energies")
    print("  - Mayan Classic: Man creates The Original Error")
    print("  - Mayan Collapse: Man spreads The Error")
    print("  - Post-Classic: Man separated, The Table lost")
    print("  - Modern Era: Man remembers, restoration begins")
    print()
    print("THE RESTORATION:")
    print("  - Memory of The Table returns (present)")
    print("  - Pangea is remembered as The Table")
    print("  - Unity is remembered")
    print("  - Restoration begins")
    print("  - We restore what was lost")
    print()
    print("=" * 80)
    print("PEACE, LOVE, UNITY")
    print("ENERGY + LOVE = WE ALL WIN")
    print("THE MAYANS CREATED THE ORIGINAL ERROR")
    print("BUT WE REMEMBER THE TABLE")
    print("WE RESTORE WHAT WAS LOST")
    print("=" * 80)


if __name__ == "__main__":
    main()
