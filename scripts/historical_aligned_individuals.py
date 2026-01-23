"""
HISTORICAL ALIGNED INDIVIDUALS
Great People Throughout Time Who Lived as Miracles in a Broken World

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

PANGEA IS THE TABLE.
YOU DON'T BETRAY THE TABLE.

HISTORICAL ALIGNED INDIVIDUALS:
Great people throughout time who went on their own journeys.
"Only to get so far" - limited by the broken world.
They lived as miracles in a broken world.
We must acknowledge and utilise everything.
"""

import sys
from pathlib import Path

# Add utils to path
sys.path.insert(0, str(Path(__file__).parent))

from utils import (
    Path, datetime, json, load_json, save_json
    setup_logging, standard_main
)

import sys
import json
from pathlib import Path
from typing import Dict, List, Optional, Any
from datetime import datetime
from dataclasses import dataclass, field, asdict
from enum import Enum
import logging

# Add scripts to path
sys.path.insert(0, str(Path(__file__).parent))

logger = logging.getLogger(__name__)


class IndividualCategory(Enum):
    """Category of historical aligned individual."""
    SCIENCE = "science"
    MEDICINE = "medicine"
    ARTS = "arts"
    PHILOSOPHY = "philosophy"
    SPIRITUAL = "spiritual"
    TECHNOLOGY = "technology"
    EDUCATION = "education"
    SOCIAL_REFORM = "social_reform"
    SPORTS = "sports"
    EMPIRE = "empire"
    NATION = "nation"
    DYNASTY = "dynasty"
    CIVILIZATION = "civilization"


@dataclass
class HistoricalAlignedIndividual:
    """Historical aligned individual who lived as a miracle in a broken world."""
    individual_id: str
    name: str
    category: str
    era: str
    birth_year: Optional[int] = None
    death_year: Optional[int] = None
    alignment_score: float = 0.85  # How aligned they were with The Table
    journey_description: str = ""  # Their journey, "only to get so far"
    contributions: List[str] = field(default_factory=list)
    limitations: List[str] = field(default_factory=list)  # How the broken world limited them
    connection_to_table: str = ""
    frequency_contribution: float = 0.0
    legacy: str = ""
    notes: str = ""
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())


class HistoricalAlignedIndividualsRegistry:
    """Registry for historical aligned individuals."""
    
    def __init__(self):
        """Initialize the registry."""
        self.individuals: Dict[str, HistoricalAlignedIndividual] = {}
        self._register_historical_individuals()
    
    def _register_historical_individuals(self):
        """Register historical aligned individuals."""
        
        # SCIENCE
        self._register_individual(
            individual_id="tesla",
            name="Nikola Tesla",
            category=IndividualCategory.SCIENCE.value,
            era="1856-1943",
            birth_year=1856,
            death_year=1943,
            alignment_score=0.92,
            journey_description="Visionary inventor who saw beyond the limitations of his time. 'Only to get so far' - his revolutionary ideas were suppressed, his funding cut, his work stolen. Lived as a miracle in a broken world that couldn't fully receive his gifts.",
            contributions=[
                "Alternating current (AC) power system",
                "Wireless energy transmission",
                "Radio technology",
                "Vision of free energy for all",
                "Connection to universal energy fields"
            ],
            limitations=[
                "Funding cut by J.P. Morgan (threatened monopoly)",
                "Ideas suppressed by established interests",
                "Work stolen and credited to others",
                "Died in poverty despite revolutionary contributions",
                "Free energy vision never realized in his lifetime"
            ],
            connection_to_table="Saw connection to universal energy fields. Vision aligned with Divine Frequency. Worked toward unity through energy.",
            frequency_contribution=0.15,
            legacy="His vision of free energy and universal connection lives on. His work continues to inspire. He saw The Table through the veil of separation."
        )
        
        self._register_individual(
            individual_id="einstein",
            name="Albert Einstein",
            category=IndividualCategory.SCIENCE.value,
            era="1879-1955",
            birth_year=1879,
            death_year=1955,
            alignment_score=0.90,
            journey_description="Revolutionary physicist who unified space and time. 'Only to get so far' - his unified field theory never completed, his pacifist ideals ignored, his vision of unity limited by the broken world.",
            contributions=[
                "Theory of Relativity (E=mc²)",
                "Unified field theory (attempted)",
                "Quantum mechanics foundations",
                "Vision of universal unity",
                "Pacifist ideals"
            ],
            limitations=[
                "Unified field theory never completed",
                "Pacifist ideals ignored during wars",
                "Nuclear weapons used despite his warnings",
                "Vision of unity limited by separation",
                "Could not fully bridge quantum and relativity"
            ],
            connection_to_table="Saw unity in the universe. Worked toward unified field theory. Vision aligned with restoring The Table.",
            frequency_contribution=0.12,
            legacy="His vision of unity continues. His work reveals the interconnectedness of all things. He saw The Table through physics."
        )
        
        self._register_individual(
            individual_id="curie",
            name="Marie Curie",
            category=IndividualCategory.SCIENCE.value,
            era="1867-1934",
            birth_year=1867,
            death_year=1934,
            alignment_score=0.88,
            journey_description="Pioneering scientist who broke barriers. 'Only to get so far' - faced discrimination, denied recognition, died from exposure to her own discoveries. Lived as a miracle in a broken world that limited women in science.",
            contributions=[
                "Radioactivity research",
                "Discovery of radium and polonium",
                "First woman to win Nobel Prize",
                "First person to win Nobel Prize twice",
                "Pioneered radiation therapy"
            ],
            limitations=[
                "Faced discrimination as a woman in science",
                "Denied membership in French Academy",
                "Died from radiation exposure",
                "Work limited by gender barriers",
                "Could not fully realize her potential"
            ],
            connection_to_table="Served truth through science. Broke barriers. Worked for healing. Aligned with The Table through service.",
            frequency_contribution=0.10,
            legacy="Her courage and dedication inspire. She broke barriers. She served truth. She lived as a miracle."
        )
        
        # MEDICINE
        self._register_individual(
            individual_id="semmelweis",
            name="Ignaz Semmelweis",
            category=IndividualCategory.MEDICINE.value,
            era="1818-1865",
            birth_year=1818,
            death_year=1865,
            alignment_score=0.89,
            journey_description="Pioneer of antiseptic procedures. 'Only to get so far' - his life-saving discovery was rejected, he was ridiculed, died in an asylum. Lived as a miracle in a broken world that couldn't see the truth.",
            contributions=[
                "Discovered handwashing prevents infection",
                "Pioneered antiseptic procedures",
                "Reduced maternal mortality by 90%",
                "Saved countless lives",
                "Truth-based medicine"
            ],
            limitations=[
                "Discovery rejected by medical establishment",
                "Ridiculed and ostracized",
                "Died in mental asylum",
                "Truth ignored for decades",
                "Could not save more lives due to rejection"
            ],
            connection_to_table="Served truth through medicine. Saved lives. Worked for healing. Aligned with The Table through service.",
            frequency_contribution=0.11,
            legacy="His truth eventually prevailed. His discovery saves millions. He lived as a miracle, serving truth despite rejection."
        )
        
        self._register_individual(
            individual_id="nightingale",
            name="Florence Nightingale",
            category=IndividualCategory.MEDICINE.value,
            era="1820-1910",
            birth_year=1820,
            death_year=1910,
            alignment_score=0.91,
            journey_description="Founder of modern nursing. 'Only to get so far' - revolutionized healthcare, but the broken world limited her vision of universal healthcare. Lived as a miracle serving healing.",
            contributions=[
                "Founded modern nursing",
                "Revolutionized hospital sanitation",
                "Pioneered healthcare statistics",
                "Vision of universal healthcare",
                "Service to all, regardless of status"
            ],
            limitations=[
                "Vision of universal healthcare not fully realized",
                "Limited by gender barriers of her time",
                "Could not fully transform healthcare system",
                "Healing limited by broken world",
                "Could not reach all who needed care"
            ],
            connection_to_table="Served healing. Served all. Worked for unity through health. Aligned with The Table through service.",
            frequency_contribution=0.13,
            legacy="Her vision of universal healthcare continues. Her service inspires. She lived as a miracle, serving healing."
        )
        
        # ARTS
        self._register_individual(
            individual_id="da_vinci",
            name="Leonardo da Vinci",
            category=IndividualCategory.ARTS.value,
            era="1452-1519",
            birth_year=1452,
            death_year=1519,
            alignment_score=0.93,
            journey_description="Renaissance master who saw unity in all things. 'Only to get so far' - his visionary inventions never built, his art limited by patrons, his vision of unity never fully expressed. Lived as a miracle in a broken world.",
            contributions=[
                "Mona Lisa, The Last Supper",
                "Visionary inventions (helicopter, tank, etc.)",
                "Anatomical studies",
                "Vision of unity in art and science",
                "Connection to universal principles"
            ],
            limitations=[
                "Many inventions never built in his lifetime",
                "Art limited by patron demands",
                "Vision of unity never fully expressed",
                "Could not fully bridge art and science",
                "Genius limited by the broken world"
            ],
            connection_to_table="Saw unity in all things. Connected art and science. Vision aligned with The Table. Encoded messages for future.",
            frequency_contribution=0.16,
            legacy="His vision of unity inspires. His encoded messages continue to reveal. He saw The Table through art and science."
        )
        
        self._register_individual(
            individual_id="van_gogh",
            name="Vincent van Gogh",
            category=IndividualCategory.ARTS.value,
            era="1853-1890",
            birth_year=1853,
            death_year=1890,
            alignment_score=0.87,
            journey_description="Visionary artist who saw the divine in nature. 'Only to get so far' - sold only one painting in his lifetime, died in poverty, his vision not recognized. Lived as a miracle in a broken world that couldn't see.",
            contributions=[
                "Starry Night, Sunflowers",
                "Vision of divine in nature",
                "Expression of spiritual truth",
                "Connection to universal beauty",
                "Art as spiritual practice"
            ],
            limitations=[
                "Sold only one painting in his lifetime",
                "Died in poverty",
                "Vision not recognized",
                "Mental health struggles",
                "Could not fully express his vision"
            ],
            connection_to_table="Saw the divine in nature. Expressed spiritual truth through art. Vision aligned with The Table.",
            frequency_contribution=0.12,
            legacy="His vision now recognized. His art reveals the divine. He lived as a miracle, expressing truth through beauty."
        )
        
        self._register_individual(
            individual_id="beethoven",
            name="Ludwig van Beethoven",
            category=IndividualCategory.ARTS.value,
            era="1770-1827",
            birth_year=1770,
            death_year=1827,
            alignment_score=0.90,
            journey_description="Revolutionary composer who transcended limitations. 'Only to get so far' - went deaf, but continued to compose. Lived as a miracle, creating beauty despite the broken world.",
            contributions=[
                "9th Symphony (Ode to Joy)",
                "Revolutionary compositions",
                "Transcended classical limitations",
                "Expressed unity through music",
                "Created despite deafness"
            ],
            limitations=[
                "Went deaf but continued composing",
                "Limited by physical constraints",
                "Could not fully hear his own work",
                "Vision limited by the broken world",
                "Could not fully express all he heard"
            ],
            connection_to_table="Expressed unity through music. Transcended limitations. Vision aligned with The Table. Ode to Joy = unity.",
            frequency_contribution=0.14,
            legacy="His music continues to inspire unity. His Ode to Joy expresses The Table. He lived as a miracle, creating despite limitations."
        )
        
        # PHILOSOPHY
        self._register_individual(
            individual_id="socrates",
            name="Socrates",
            category=IndividualCategory.PHILOSOPHY.value,
            era="470-399 BCE",
            birth_year=-470,
            death_year=-399,
            alignment_score=0.91,
            journey_description="Philosopher who sought truth. 'Only to get so far' - executed for asking questions, his truth too dangerous. Lived as a miracle in a broken world that feared truth.",
            contributions=[
                "Socratic method",
                "Questioned everything",
                "Sought truth above all",
                "Died for truth",
                "Inspired generations"
            ],
            limitations=[
                "Executed for asking questions",
                "Truth too dangerous for the broken world",
                "Could not fully spread his method",
                "Limited by fear of truth",
                "Could not complete his journey"
            ],
            connection_to_table="Sought truth. Questioned separation. Died for truth. Aligned with The Table through truth-seeking.",
            frequency_contribution=0.13,
            legacy="His method continues. His truth-seeking inspires. He lived as a miracle, seeking truth despite the cost."
        )
        
        # SPORTS
        self._register_individual(
            individual_id="jesse_owens",
            name="Jesse Owens",
            category=IndividualCategory.SPORTS.value,
            era="1913-1980",
            birth_year=1913,
            death_year=1980,
            alignment_score=0.90,
            journey_description="Olympic champion who broke barriers. 'Only to get so far' - won 4 gold medals in 1936 Berlin Olympics, but faced discrimination at home, struggled financially, his achievements limited by the broken world. Lived as a miracle, transcending barriers through sport.",
            contributions=[
                "4 gold medals at 1936 Berlin Olympics",
                "Broke racial barriers in sports",
                "Inspired generations of athletes",
                "Demonstrated unity through excellence",
                "Transcended separation through sport"
            ],
            limitations=[
                "Faced discrimination despite Olympic success",
                "Struggled financially after Olympics",
                "Achievements not fully recognized",
                "Limited by racial barriers",
                "Could not fully realize his potential"
            ],
            connection_to_table="Transcended separation through sport. Demonstrated unity through excellence. Broke barriers. Aligned with The Table through unity.",
            frequency_contribution=0.12,
            legacy="His courage and excellence inspire. He broke barriers. He demonstrated unity through sport. He lived as a miracle."
        )
        
        self._register_individual(
            individual_id="muhammad_ali",
            name="Muhammad Ali",
            category=IndividualCategory.SPORTS.value,
            era="1942-2016",
            birth_year=1942,
            death_year=2016,
            alignment_score=0.92,
            journey_description="Boxing champion and social activist. 'Only to get so far' - stood for truth, refused to fight in Vietnam, stripped of title, but his voice for justice limited by the broken world. Lived as a miracle, using sport as a platform for truth.",
            contributions=[
                "3-time heavyweight champion",
                "Stood for truth and justice",
                "Refused to fight in Vietnam",
                "Used platform for social change",
                "Inspired unity through sport"
            ],
            limitations=[
                "Stripped of title for standing for truth",
                "Banned from boxing in prime years",
                "Voice for justice limited by broken world",
                "Could not fully realize his vision",
                "Limited by the system"
            ],
            connection_to_table="Stood for truth. Used sport for justice. Demonstrated unity. Aligned with The Table through truth and service.",
            frequency_contribution=0.14,
            legacy="His courage and truth continue to inspire. He stood for justice. He used sport as a platform for truth. He lived as a miracle."
        )
        
        self._register_individual(
            individual_id="wilma_rudolph",
            name="Wilma Rudolph",
            category=IndividualCategory.SPORTS.value,
            era="1940-1994",
            birth_year=1940,
            death_year=1994,
            alignment_score=0.89,
            journey_description="Olympic champion who overcame polio. 'Only to get so far' - overcame childhood polio, won 3 gold medals, but faced discrimination, her achievements limited by the broken world. Lived as a miracle, transcending physical limitations.",
            contributions=[
                "3 gold medals at 1960 Olympics",
                "Overcame childhood polio",
                "Broke barriers for women and African Americans",
                "Inspired through perseverance",
                "Demonstrated unity through excellence"
            ],
            limitations=[
                "Faced discrimination despite achievements",
                "Limited by racial and gender barriers",
                "Could not fully realize her potential",
                "Achievements not fully recognized",
                "Limited by the broken world"
            ],
            connection_to_table="Transcended limitations. Demonstrated unity. Broke barriers. Aligned with The Table through perseverance and excellence.",
            frequency_contribution=0.11,
            legacy="Her perseverance and excellence inspire. She transcended limitations. She broke barriers. She lived as a miracle."
        )
        
        self._register_individual(
            individual_id="jim_thorpe",
            name="Jim Thorpe",
            category=IndividualCategory.SPORTS.value,
            era="1887-1953",
            birth_year=1887,
            death_year=1953,
            alignment_score=0.88,
            journey_description="Olympic champion and multi-sport athlete. 'Only to get so far' - won 2 gold medals, but stripped for playing semi-pro baseball, faced discrimination, died in poverty. Lived as a miracle, excelling despite the broken world.",
            contributions=[
                "2 gold medals at 1912 Olympics",
                "Multi-sport excellence",
                "Broke barriers for Native Americans",
                "Inspired through excellence",
                "Demonstrated unity through sport"
            ],
            limitations=[
                "Stripped of medals for playing semi-pro baseball",
                "Faced discrimination as Native American",
                "Died in poverty despite achievements",
                "Could not fully realize his potential",
                "Limited by the broken world"
            ],
            connection_to_table="Excelled despite limitations. Demonstrated unity. Broke barriers. Aligned with The Table through excellence.",
            frequency_contribution=0.10,
            legacy="His excellence continues to inspire. He broke barriers. He demonstrated unity through sport. He lived as a miracle."
        )
        
        self._register_individual(
            individual_id="arthur_ashe",
            name="Arthur Ashe",
            category=IndividualCategory.SPORTS.value,
            era="1943-1993",
            birth_year=1943,
            death_year=1993,
            alignment_score=0.91,
            journey_description="Tennis champion and activist. 'Only to get so far' - first African American to win Wimbledon, but faced discrimination, died from AIDS contracted from blood transfusion, his voice for justice limited. Lived as a miracle, using sport for truth.",
            contributions=[
                "First African American to win Wimbledon",
                "Used platform for social justice",
                "Advocated for AIDS awareness",
                "Broke barriers in tennis",
                "Demonstrated unity through excellence"
            ],
            limitations=[
                "Faced discrimination despite achievements",
                "Died from AIDS (blood transfusion)",
                "Voice for justice limited by broken world",
                "Could not fully realize his vision",
                "Limited by the system"
            ],
            connection_to_table="Used sport for truth. Demonstrated unity. Broke barriers. Aligned with The Table through service and justice.",
            frequency_contribution=0.13,
            legacy="His courage and truth continue to inspire. He used sport for justice. He broke barriers. He lived as a miracle."
        )
        
        # EMPIRES
        self._register_individual(
            individual_id="british_empire",
            name="British Empire",
            category=IndividualCategory.EMPIRE.value,
            era="1583-1997",
            birth_year=1583,
            death_year=1997,
            alignment_score=0.45,
            journey_description="Global empire that spanned continents. 'Only to get so far' - built on exploitation, colonization, separation. Lived as a broken system in a broken world. But within it, some aligned individuals emerged. We acknowledge and utilise everything - the good, the bad, the truth.",
            contributions=[
                "Global trade networks",
                "Technological innovations",
                "Legal systems",
                "Some aligned individuals emerged",
                "Infrastructure development"
            ],
            limitations=[
                "Built on exploitation and colonization",
                "Created separation and division",
                "Suppressed indigenous cultures",
                "Extracted resources without reciprocity",
                "Maintained separation from The Table"
            ],
            connection_to_table="Created separation. Maintained division. But within it, some aligned individuals emerged. We acknowledge and utilise everything - learn from the errors, honour the aligned, restore The Table.",
            frequency_contribution=-0.20,  # Negative - created separation
            legacy="Created separation. Maintained division. But we learn from the errors. We acknowledge and utilise everything. We restore The Table."
        )
        
        self._register_individual(
            individual_id="ottoman_empire",
            name="Ottoman Empire",
            category=IndividualCategory.EMPIRE.value,
            era="1299-1922",
            birth_year=1299,
            death_year=1922,
            alignment_score=0.50,
            journey_description="Multi-ethnic empire spanning three continents. 'Only to get so far' - maintained through conquest, but also preserved heritage, connected cultures. Lived as a complex system in a broken world. We acknowledge and utilise everything.",
            contributions=[
                "Preserved heritage sites",
                "Connected cultures",
                "Multi-ethnic administration",
                "Some aligned individuals emerged",
                "Cultural preservation"
            ],
            limitations=[
                "Maintained through conquest",
                "Created separation",
                "Suppressed some cultures",
                "Limited by the broken world",
                "Could not fully realize unity"
            ],
            connection_to_table="Maintained separation. But also preserved heritage. Some connection to The Table through heritage preservation. We acknowledge and utilise everything.",
            frequency_contribution=-0.15,  # Negative - created separation
            legacy="Maintained separation. But preserved heritage. We acknowledge and utilise everything. We restore The Table."
        )
        
        self._register_individual(
            individual_id="roman_empire",
            name="Roman Empire",
            category=IndividualCategory.EMPIRE.value,
            era="27 BCE - 476 CE",
            birth_year=-27,
            death_year=476,
            alignment_score=0.48,
            journey_description="Vast empire that unified much of the known world. 'Only to get so far' - built on conquest, but also created infrastructure, preserved knowledge. Lived as a complex system in a broken world. We acknowledge and utilise everything.",
            contributions=[
                "Infrastructure development",
                "Legal systems",
                "Preserved knowledge",
                "Connected regions",
                "Some aligned individuals emerged"
            ],
            limitations=[
                "Built on conquest",
                "Created separation",
                "Suppressed cultures",
                "Maintained through force",
                "Could not fully realize unity"
            ],
            connection_to_table="Created separation. But also connected regions. Some infrastructure remains. We acknowledge and utilise everything.",
            frequency_contribution=-0.18,  # Negative - created separation
            legacy="Created separation. But preserved knowledge. We acknowledge and utilise everything. We restore The Table."
        )
        
        self._register_individual(
            individual_id="mongol_empire",
            name="Mongol Empire",
            category=IndividualCategory.EMPIRE.value,
            era="1206-1368",
            birth_year=1206,
            death_year=1368,
            alignment_score=0.42,
            journey_description="Largest contiguous empire in history. 'Only to get so far' - built on conquest, but also connected East and West, facilitated trade. Lived as a complex system in a broken world. We acknowledge and utilise everything.",
            contributions=[
                "Connected East and West",
                "Facilitated trade",
                "Cultural exchange",
                "Some aligned individuals emerged",
                "Connected regions"
            ],
            limitations=[
                "Built on conquest",
                "Created separation",
                "Destroyed cultures",
                "Maintained through force",
                "Could not fully realize unity"
            ],
            connection_to_table="Created separation. But also connected regions. We acknowledge and utilise everything.",
            frequency_contribution=-0.22,  # Negative - created separation
            legacy="Created separation. But connected regions. We acknowledge and utilise everything. We restore The Table."
        )
        
        self._register_individual(
            individual_id="byzantine_empire",
            name="Byzantine Empire",
            category=IndividualCategory.EMPIRE.value,
            era="330-1453",
            birth_year=330,
            death_year=1453,
            alignment_score=0.52,
            journey_description="Continuation of Roman Empire in the East. 'Only to get so far' - preserved knowledge, heritage, but also maintained separation. Lived as a complex system in a broken world. We acknowledge and utilise everything.",
            contributions=[
                "Preserved knowledge",
                "Preserved heritage",
                "Cultural preservation",
                "Some aligned individuals emerged",
                "Maintained continuity"
            ],
            limitations=[
                "Maintained separation",
                "Limited by the broken world",
                "Could not fully realize unity",
                "Preserved but did not restore",
                "Limited connection to The Table"
            ],
            connection_to_table="Preserved heritage. But maintained separation. We acknowledge and utilise everything.",
            frequency_contribution=-0.12,  # Less negative - preserved heritage
            legacy="Preserved heritage. But maintained separation. We acknowledge and utilise everything. We restore The Table."
        )
        
        self._register_individual(
            individual_id="persian_empire",
            name="Persian Empire",
            category=IndividualCategory.EMPIRE.value,
            era="550 BCE - 330 BCE",
            birth_year=-550,
            death_year=-330,
            alignment_score=0.55,
            journey_description="Ancient empire that unified diverse peoples. 'Only to get so far' - built on tolerance, preserved cultures, but also maintained separation. Lived as a complex system in a broken world. We acknowledge and utilise everything.",
            contributions=[
                "Religious tolerance",
                "Preserved cultures",
                "Infrastructure development",
                "Some aligned individuals emerged",
                "Cultural preservation"
            ],
            limitations=[
                "Maintained separation",
                "Built on conquest",
                "Limited by the broken world",
                "Could not fully realize unity",
                "Limited connection to The Table"
            ],
            connection_to_table="Preserved cultures. But maintained separation. We acknowledge and utilise everything.",
            frequency_contribution=-0.10,  # Less negative - preserved cultures
            legacy="Preserved cultures. But maintained separation. We acknowledge and utilise everything. We restore The Table."
        )
        
        # NATIONS
        self._register_individual(
            individual_id="united_states",
            name="United States of America",
            category=IndividualCategory.NATION.value,
            era="1776-Present",
            birth_year=1776,
            death_year=None,
            alignment_score=0.55,
            journey_description="Nation founded on ideals of freedom and unity. 'Only to get so far' - built on ideals, but also on exploitation, separation. Lived as a complex system in a broken world. Within it, many aligned individuals emerged. We acknowledge and utilise everything.",
            contributions=[
                "Ideals of freedom and unity",
                "Technological innovations",
                "Many aligned individuals emerged",
                "Some progress toward unity",
                "Infrastructure development"
            ],
            limitations=[
                "Built on exploitation",
                "Created separation",
                "Maintained division",
                "Limited by the broken world",
                "Could not fully realize unity"
            ],
            connection_to_table="Built on ideals. But maintained separation. Many aligned individuals emerged. We acknowledge and utilise everything.",
            frequency_contribution=-0.15,  # Negative - created separation, but also produced aligned individuals
            legacy="Built on ideals. But maintained separation. Many aligned individuals emerged. We acknowledge and utilise everything. We restore The Table."
        )
        
        self._register_individual(
            individual_id="russia",
            name="Russia / Soviet Union",
            category=IndividualCategory.NATION.value,
            era="862-Present",
            birth_year=862,
            death_year=None,
            alignment_score=0.48,
            journey_description="Vast nation spanning continents. 'Only to get so far' - complex history of expansion, preservation, separation. Lived as a complex system in a broken world. Within it, some aligned individuals emerged. We acknowledge and utilise everything.",
            contributions=[
                "Preserved heritage",
                "Cultural preservation",
                "Some aligned individuals emerged",
                "Infrastructure development",
                "Knowledge preservation"
            ],
            limitations=[
                "Maintained separation",
                "Created division",
                "Suppressed some cultures",
                "Limited by the broken world",
                "Could not fully realize unity"
            ],
            connection_to_table="Preserved heritage. But maintained separation. Some aligned individuals emerged. We acknowledge and utilise everything.",
            frequency_contribution=-0.18,  # Negative - created separation
            legacy="Preserved heritage. But maintained separation. We acknowledge and utilise everything. We restore The Table."
        )
        
        self._register_individual(
            individual_id="china",
            name="China",
            category=IndividualCategory.NATION.value,
            era="221 BCE-Present",
            birth_year=-221,
            death_year=None,
            alignment_score=0.52,
            journey_description="Ancient civilization and modern nation. 'Only to get so far' - preserved heritage, knowledge, but also maintained separation. Lived as a complex system in a broken world. Within it, many aligned individuals emerged. We acknowledge and utilise everything.",
            contributions=[
                "Preserved heritage",
                "Preserved knowledge",
                "Many aligned individuals emerged",
                "Cultural preservation",
                "Technological innovations"
            ],
            limitations=[
                "Maintained separation",
                "Created division",
                "Limited by the broken world",
                "Could not fully realize unity",
                "Limited connection to The Table"
            ],
            connection_to_table="Preserved heritage and knowledge. But maintained separation. Many aligned individuals emerged. We acknowledge and utilise everything.",
            frequency_contribution=-0.12,  # Less negative - preserved heritage and knowledge
            legacy="Preserved heritage and knowledge. But maintained separation. We acknowledge and utilise everything. We restore The Table."
        )
        
        self._register_individual(
            individual_id="india",
            name="India",
            category=IndividualCategory.NATION.value,
            era="2500 BCE-Present",
            birth_year=-2500,
            death_year=None,
            alignment_score=0.58,
            journey_description="Ancient civilization and modern nation. 'Only to get so far' - preserved spiritual knowledge, heritage, but also maintained separation. Lived as a complex system in a broken world. Within it, many aligned individuals emerged. We acknowledge and utilise everything.",
            contributions=[
                "Preserved spiritual knowledge",
                "Preserved heritage",
                "Many aligned individuals emerged",
                "Cultural preservation",
                "Spiritual wisdom"
            ],
            limitations=[
                "Maintained separation",
                "Created division",
                "Limited by the broken world",
                "Could not fully realize unity",
                "Limited connection to The Table"
            ],
            connection_to_table="Preserved spiritual knowledge. But maintained separation. Many aligned individuals emerged. We acknowledge and utilise everything.",
            frequency_contribution=-0.08,  # Less negative - preserved spiritual knowledge
            legacy="Preserved spiritual knowledge. But maintained separation. We acknowledge and utilise everything. We restore The Table."
        )
        
        # DYNASTIES
        self._register_individual(
            individual_id="ming_dynasty",
            name="Ming Dynasty",
            category=IndividualCategory.DYNASTY.value,
            era="1368-1644",
            birth_year=1368,
            death_year=1644,
            alignment_score=0.54,
            journey_description="Chinese dynasty that restored Chinese rule. 'Only to get so far' - preserved heritage, knowledge, but also maintained separation. Lived as a complex system in a broken world. We acknowledge and utilise everything.",
            contributions=[
                "Preserved heritage",
                "Preserved knowledge",
                "Cultural preservation",
                "Some aligned individuals emerged",
                "Infrastructure development"
            ],
            limitations=[
                "Maintained separation",
                "Limited by the broken world",
                "Could not fully realize unity",
                "Limited connection to The Table",
                "Could not restore The Table"
            ],
            connection_to_table="Preserved heritage. But maintained separation. We acknowledge and utilise everything.",
            frequency_contribution=-0.10,  # Less negative - preserved heritage
            legacy="Preserved heritage. But maintained separation. We acknowledge and utilise everything. We restore The Table."
        )
        
        self._register_individual(
            individual_id="abbasid_caliphate",
            name="Abbasid Caliphate",
            category=IndividualCategory.DYNASTY.value,
            era="750-1258",
            birth_year=750,
            death_year=1258,
            alignment_score=0.56,
            journey_description="Islamic caliphate that preserved knowledge. 'Only to get so far' - preserved knowledge, heritage, but also maintained separation. Lived as a complex system in a broken world. Within it, many aligned individuals emerged. We acknowledge and utilise everything.",
            contributions=[
                "Preserved knowledge",
                "Preserved heritage",
                "Many aligned individuals emerged",
                "Cultural preservation",
                "Knowledge sharing"
            ],
            limitations=[
                "Maintained separation",
                "Limited by the broken world",
                "Could not fully realize unity",
                "Limited connection to The Table",
                "Could not restore The Table"
            ],
            connection_to_table="Preserved knowledge. But maintained separation. Many aligned individuals emerged. We acknowledge and utilise everything.",
            frequency_contribution=-0.08,  # Less negative - preserved knowledge
            legacy="Preserved knowledge. But maintained separation. We acknowledge and utilise everything. We restore The Table."
        )
        
        # CIVILIZATIONS
        self._register_individual(
            individual_id="ancient_egypt",
            name="Ancient Egypt",
            category=IndividualCategory.CIVILIZATION.value,
            era="3100 BCE - 30 BCE",
            birth_year=-3100,
            death_year=-30,
            alignment_score=0.60,
            journey_description="Ancient civilization that preserved knowledge and heritage. 'Only to get so far' - preserved knowledge, heritage, but also maintained separation. Lived as a complex system in a broken world. Within it, some aligned individuals emerged (Thoth prophecy). We acknowledge and utilise everything.",
            contributions=[
                "Preserved knowledge",
                "Preserved heritage",
                "Some aligned individuals emerged (Thoth)",
                "Cultural preservation",
                "Spiritual knowledge"
            ],
            limitations=[
                "Maintained separation",
                "Limited by the broken world",
                "Could not fully realize unity",
                "Limited connection to The Table",
                "Could not restore The Table"
            ],
            connection_to_table="Preserved knowledge. Thoth prophecy. But maintained separation. We acknowledge and utilise everything.",
            frequency_contribution=-0.05,  # Less negative - preserved knowledge, Thoth prophecy
            legacy="Preserved knowledge. Thoth prophecy. But maintained separation. We acknowledge and utilise everything. We restore The Table."
        )
        
        self._register_individual(
            individual_id="ancient_greece",
            name="Ancient Greece",
            category=IndividualCategory.CIVILIZATION.value,
            era="800 BCE - 146 BCE",
            birth_year=-800,
            death_year=-146,
            alignment_score=0.58,
            journey_description="Ancient civilization that preserved knowledge and philosophy. 'Only to get so far' - preserved knowledge, philosophy, but also maintained separation. Lived as a complex system in a broken world. Within it, many aligned individuals emerged (Socrates, etc.). We acknowledge and utilise everything.",
            contributions=[
                "Preserved knowledge",
                "Preserved philosophy",
                "Many aligned individuals emerged",
                "Cultural preservation",
                "Philosophical wisdom"
            ],
            limitations=[
                "Maintained separation",
                "Limited by the broken world",
                "Could not fully realize unity",
                "Limited connection to The Table",
                "Could not restore The Table"
            ],
            connection_to_table="Preserved knowledge and philosophy. Many aligned individuals emerged. But maintained separation. We acknowledge and utilise everything.",
            frequency_contribution=-0.06,  # Less negative - preserved knowledge, many aligned individuals
            legacy="Preserved knowledge and philosophy. But maintained separation. We acknowledge and utilise everything. We restore The Table."
        )
        
        self._register_individual(
            individual_id="mayan_civilization",
            name="Mayan Civilization",
            category=IndividualCategory.CIVILIZATION.value,
            era="2000 BCE - 1697 CE",
            birth_year=-2000,
            death_year=1697,
            alignment_score=0.35,
            journey_description="Ancient civilization that created The Original Error. 'Only to get so far' - codified separation, built pyramids to sabotage The Table. Lived as a broken system in a broken world. But we acknowledge and utilise everything - learn from the errors, honour what was aligned, restore The Table.",
            contributions=[
                "Preserved knowledge (some)",
                "Cultural preservation (some)",
                "Some aligned individuals may have emerged",
                "Astronomical knowledge",
                "Calendar systems"
            ],
            limitations=[
                "Created The Original Error",
                "Codified separation",
                "Built pyramids to sabotage The Table",
                "Maintained separation",
                "Limited connection to The Table"
            ],
            connection_to_table="Created The Original Error. Codified separation. But we learn from the errors. We acknowledge and utilise everything. We restore The Table.",
            frequency_contribution=-0.30,  # Highly negative - created The Original Error
            legacy="Created The Original Error. But we learn from the errors. We acknowledge and utilise everything. We restore The Table."
        )
        
        # Add more as needed...
    
    def _register_individual(
        self,
        individual_id: str,
        name: str,
        category: str,
        era: str,
        birth_year: Optional[int] = None,
        death_year: Optional[int] = None,
        alignment_score: float = 0.85,
        journey_description: str = "",
        contributions: List[str] = None,
        limitations: List[str] = None,
        connection_to_table: str = "",
        frequency_contribution: float = 0.0,
        legacy: str = "",
        notes: str = ""
    ):
        """Register a historical aligned individual."""
        if contributions is None:
            contributions = []
        if limitations is None:
            limitations = []
        
        individual = HistoricalAlignedIndividual(
            individual_id=individual_id,
            name=name,
            category=category,
            era=era,
            birth_year=birth_year,
            death_year=death_year,
            alignment_score=alignment_score,
            journey_description=journey_description,
            contributions=contributions,
            limitations=limitations,
            connection_to_table=connection_to_table,
            frequency_contribution=frequency_contribution,
            legacy=legacy,
            notes=notes
        )
        
        self.individuals[individual_id] = individual
        logger.info(f"Registered historical aligned individual: {name} ({category})")
    
    def get_all_individuals(self) -> Dict[str, HistoricalAlignedIndividual]:
        """Get all registered individuals."""
        return self.individuals
    
    def get_individuals_by_category(self, category: str) -> List[HistoricalAlignedIndividual]:
        """Get individuals by category."""
        return [ind for ind in self.individuals.values() if ind.category == category]
    
    def get_total_frequency_contribution(self) -> float:
        """Get total frequency contribution from all historical individuals."""
        return sum(ind.frequency_contribution for ind in self.individuals.values())
    
    def export_individuals_report(self) -> Dict[str, Any]:
        """Export complete report of historical aligned individuals."""
        from dataclasses import asdict
        
        return {
            "report_timestamp": datetime.now().isoformat(),
            "total_individuals": len(self.individuals),
            "total_frequency_contribution": self.get_total_frequency_contribution(),
            "by_category": {
                category.value: len(self.get_individuals_by_category(category.value))
                for category in IndividualCategory
            },
            "individuals": [asdict(ind) for ind in self.individuals.values()],
            "the_truth": "Great people throughout time who went on their own journeys. 'Only to get so far' - limited by the broken world. They lived as miracles in a broken world. Empires, nations, dynasties, civilizations - all of it. The British, the Ottomans, the Romans, the Mongols, the Byzantines, the Persians, the United States, Russia, China, India, Ming Dynasty, Abbasid Caliphate, Ancient Egypt, Ancient Greece, Mayan Civilization - all of it. We acknowledge and utilise everything - the good, the bad, the truth. We learn from the errors. We honour what was aligned. We restore The Table."
        }


def main():
    """Main function to demonstrate historical aligned individuals registry."""
    print("=" * 80)
    print("HISTORICAL ALIGNED INDIVIDUALS")
    print("Great People Throughout Time Who Lived as Miracles in a Broken World")
    print("=" * 80)
    print()
    
    registry = HistoricalAlignedIndividualsRegistry()
    
    print(f"Registered individuals: {len(registry.individuals)}")
    print()
    
    print("By Category:")
    for category in IndividualCategory:
        individuals = registry.get_individuals_by_category(category.value)
        if individuals:
            contribution = sum(ind.frequency_contribution for ind in individuals)
            print(f"  {category.value}: {len(individuals)} (contribution: {contribution:+.2f})")
    print()
    
    total_contribution = registry.get_total_frequency_contribution()
    print(f"Total Frequency Contribution: {total_contribution:+.2f}")
    if total_contribution < 0:
        print("  (Net negative - empires/nations created separation, but individuals contributed positively)")
    print()
    
    # Export report
    import os
    os.makedirs("output/historical_aligned_individuals", exist_ok=True)
    report = registry.export_individuals_report()
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_path = f"output/historical_aligned_individuals/individuals_report_{timestamp}.json"
    
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False, default=str)
    
    print(f"Exporting report...")
    print(f"  [OK] Exported to: {report_path}")
    print()
    
    print("=" * 80)
    print("THE TRUTH: HISTORICAL ALIGNED INDIVIDUALS")
    print("=" * 80)
    print()
    print("GREAT PEOPLE THROUGHOUT TIME:")
    print("  - Went on their own journeys")
    print("  - 'Only to get so far' - limited by the broken world")
    print("  - Lived as miracles in a broken world")
    print("  - We must acknowledge and utilise everything")
    print()
    print("THEY:")
    print("  - Served truth, beauty, healing, unity")
    print("  - Were limited by the broken world")
    print("  - Contributed to Divine Frequency")
    print("  - Are connected to The Table")
    print()
    print("WE:")
    print("  - Acknowledge their contributions")
    print("  - Honour their journeys")
    print("  - Utilise their wisdom")
    print("  - Continue their work")
    print()
    print("=" * 80)
    print("PEACE, LOVE, UNITY")
    print("ENERGY + LOVE = WE ALL WIN")
    print("PANGEA IS THE TABLE")
    print("WE RESTORE THE TABLE")
    print("WE ACKNOWLEDGE AND UTILISE EVERYTHING")
    print("=" * 80)


if __name__ == "__main__":
    main()
