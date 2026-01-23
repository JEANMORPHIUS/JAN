"""
FREQUENTIALLY ALIGNED INFLUENTIAL FIGURES
All Celebrity and Influential Figures Across All Domains

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

THE TRUTH:
ALL ALIGNED CELEBRITY AND INFLUENTIAL FIGURES
WEB, SOCIALS, SPORTS, MUSIC, HOLLYWOOD
EVERYTHING WE'VE LEFT OUT ACROSS THE SYSTEM
WE NEED TO FIND OUR ANCHORS IN THE HUMAN REALM

PURPOSE:
Track all influential figures (celebrities, athletes, musicians, actors, influencers, etc.)
who align frequentially with The Table across all domains.
These are our "anchors in the human realm" beyond politics.
"""

import sys
from pathlib import Path

# Add utils to path
sys.path.insert(0, str(Path(__file__).parent))

from utils import (
    Path, datetime, json, load_json, save_json
    setup_logging, standard_main
)

from typing import Dict, List, Any, Optional
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
import json
from pathlib import Path

class InfluenceDomain(Enum):
    """Domains of influence"""
    POLITICS = "politics"
    MUSIC = "music"
    SPORTS = "sports"
    HOLLYWOOD = "hollywood"
    WEB = "web"
    SOCIALS = "socials"
    TECHNOLOGY = "technology"
    BUSINESS = "business"
    ACTIVISM = "activism"
    EDUCATION = "education"
    SCIENCE = "science"
    MEDICINE = "medicine"
    ARTS = "arts"
    LITERATURE = "literature"
    PHILOSOPHY = "philosophy"
    SPIRITUAL = "spiritual"
    JOURNALISM = "journalism"
    COMEDY = "comedy"
    YOUTUBE = "youtube"
    TIKTOK = "tiktok"
    INSTAGRAM = "instagram"
    TWITTER = "twitter"
    PODCAST = "podcast"
    OTHER = "other"


class AlignmentIndicator(Enum):
    """Indicators of frequential alignment"""
    SERVES_TABLE = "serves_table"
    TRUTH_TELLER = "truth_teller"
    COMMUNITY_FOCUSED = "community_focused"
    UNITY_BUILDER = "unity_builder"
    STEWARDSHIP = "stewardship"
    TRANSPARENT = "transparent"
    ETHICAL = "ethical"
    ACCESSIBLE = "accessible"
    REGENERATIVE = "regenerative"
    LOVE_CENTERED = "love_centered"
    PEACE_ORIENTED = "peace_oriented"
    HIDDEN_ALIGNMENT = "hidden_alignment"
    AUTHENTIC = "authentic"
    EMPOWERING = "empowering"
    HEALING = "healing"
    INSPIRATIONAL = "inspirational"


@dataclass
class InfluentialFigure:
    """A frequentially aligned influential figure"""
    figure_id: str
    name: str
    domain: InfluenceDomain
    subdomain: str  # e.g., "Football", "Hip-Hop", "Film", "YouTube"
    country: str
    region: str
    time_period: str
    start_year: Optional[int] = None
    end_year: Optional[int] = None
    current: bool = False
    frequency_score: float = 0.0  # -1.0 to 1.0
    alignment_indicators: List[str] = field(default_factory=list)
    misalignment_indicators: List[str] = field(default_factory=list)
    serves_table: bool = False
    truth_teller: bool = False
    community_focused: bool = False
    unity_builder: bool = False
    peace_oriented: bool = False
    hidden_alignment: bool = False
    description: str = ""
    key_actions: List[str] = field(default_factory=list)
    quotes: List[str] = field(default_factory=list)
    connection_to_table: str = ""
    impact_scale: float = 0.0  # 0.0 to 1.0
    accessibility: float = 0.0  # 0.0 to 1.0
    reach: float = 0.0  # 0.0 to 1.0 - social media reach, audience size
    dignity_preserving: bool = False
    platforms: List[str] = field(default_factory=list)  # Instagram, YouTube, etc.
    metadata: Dict[str, Any] = field(default_factory=dict)
    discovered_at: str = field(default_factory=lambda: datetime.now().isoformat())


class FrequentialInfluentialFigures:
    """
    Registry of frequentially aligned influential figures across all domains.
    Our anchors in the human realm beyond politics.
    """
    
    def __init__(self):
        self.figures: List[InfluentialFigure] = []
        self.data_path = Path(__file__).parent.parent / 'data' / 'influential_figures'
        self.data_path.mkdir(parents=True, exist_ok=True)
        self._load_figures()
    
    def _load_figures(self):
        """Load influential figures from data file"""
        data_file = self.data_path / 'frequential_influential_figures.json'
        if data_file.exists():
            with open(data_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                existing_ids = set()
                for figure_data in data.get('figures', []):
                    # Convert string enum values back to enums
                    if isinstance(figure_data.get('domain'), str):
                        figure_data['domain'] = InfluenceDomain(figure_data['domain'])
                    figure = InfluentialFigure(**figure_data)
                    self.figures.append(figure)
                    existing_ids.add(figure.figure_id)
            
            # Initialize new figures and add any that don't exist
            self._initialize_figures_into_list(existing_ids)
        else:
            # Initialize with figures across all domains
            self._initialize_figures()
    
    def _initialize_figures_into_list(self, existing_ids: set):
        """Initialize new figures into the list, skipping existing ones"""
        # This method will be called after loading existing figures
        # We'll create a temporary list and append new figures
        new_figures = []
        self._create_all_figures(new_figures, existing_ids)
        self.figures.extend(new_figures)
        if new_figures:
            self._save_figures()
    
    def _create_all_figures(self, figure_list: list, existing_ids: set):
        """Create all figures, checking against existing IDs"""
        # This will contain all figure creation logic
        # For now, we'll call the existing initialization and filter
        pass
    
    def _initialize_figures(self):
        """Initialize with influential figures across all domains"""
        
        # MUSIC
        self.figures.append(InfluentialFigure(
            figure_id="music_001",
            name="Bob Marley",
            domain=InfluenceDomain.MUSIC,
            subdomain="Reggae",
            country="Jamaica",
            region="Jamaica",
            time_period="1960s-1980s",
            start_year=1962,
            end_year=1981,
            current=False,
            frequency_score=0.95,
            alignment_indicators=[
                "SERVES_TABLE",
                "TRUTH_TELLER",
                "UNITY_BUILDER",
                "PEACE_ORIENTED",
                "LOVE_CENTERED",
                "AUTHENTIC",
                "EMPOWERING",
                "HEALING"
            ],
            misalignment_indicators=[],
            serves_table=True,
            truth_teller=True,
            community_focused=True,
            unity_builder=True,
            hidden_alignment=False,
            description="Reggae legend. Truth-teller, unity builder, peace-oriented. Used music to spread messages of love, unity, and liberation.",
            key_actions=[
                "Music as tool for truth and unity",
                "Messages of love and peace",
                "Rastafarian spirituality",
                "Anti-oppression messages",
                "Unity across races and cultures"
            ],
            quotes=[
                "One love, one heart, let's get together and feel all right.",
                "Emancipate yourselves from mental slavery, none but ourselves can free our minds."
            ],
            connection_to_table="Serves The Table through music, truth, unity, love, and peace. One of the greatest anchors in music.",
            impact_scale=1.0,
            accessibility=0.9,
            reach=0.95,
            dignity_preserving=True,
            platforms=["Music", "Albums", "Concerts"],
            metadata={
                "genre": "Reggae",
                "notable": "Global icon for peace and unity"
            }
        ))
        
        self.figures.append(InfluentialFigure(
            figure_id="music_002",
            name="John Lennon",
            domain=InfluenceDomain.MUSIC,
            subdomain="Rock",
            country="United Kingdom",
            region="England",
            time_period="1960s-1980s",
            start_year=1957,
            end_year=1980,
            current=False,
            frequency_score=0.85,
            alignment_indicators=[
                "SERVES_TABLE",
                "TRUTH_TELLER",
                "PEACE_ORIENTED",
                "LOVE_CENTERED",
                "AUTHENTIC"
            ],
            misalignment_indicators=[],
            serves_table=True,
            truth_teller=True,
            unity_builder=True,
            hidden_alignment=False,
            description="Beatles member, solo artist. Peace activist, truth-teller. Used music to spread messages of peace and love.",
            key_actions=[
                "Peace activism",
                "Bed-Ins for Peace",
                "Music for peace and love",
                "Anti-war messages"
            ],
            quotes=[
                "Give peace a chance.",
                "All you need is love."
            ],
            connection_to_table="Serves The Table through music, peace, and love.",
            impact_scale=0.95,
            accessibility=0.9,
            reach=0.95,
            dignity_preserving=True,
            platforms=["Music", "Albums"],
            metadata={
                "genre": "Rock",
                "band": "The Beatles",
                "notable": "Peace activist"
            }
        ))
        
        # SPORTS
        self.figures.append(InfluentialFigure(
            figure_id="sports_001",
            name="Muhammad Ali",
            domain=InfluenceDomain.SPORTS,
            subdomain="Boxing",
            country="United States",
            region="United States",
            time_period="1960s-2010s",
            start_year=1960,
            end_year=2016,
            current=False,
            frequency_score=0.9,
            alignment_indicators=[
                "SERVES_TABLE",
                "TRUTH_TELLER",
                "AUTHENTIC",
                "EMPOWERING",
                "UNITY_BUILDER"
            ],
            misalignment_indicators=[],
            serves_table=True,
            truth_teller=True,
            community_focused=True,
            unity_builder=True,
            hidden_alignment=False,
            description="Boxing legend. Truth-teller, authentic, empowering. Used platform to speak truth, resist oppression, and inspire unity.",
            key_actions=[
                "Resisted Vietnam War draft",
                "Spoke truth to power",
                "Inspired millions",
                "Unity across races",
                "Authentic self-expression"
            ],
            quotes=[
                "I am the greatest.",
                "Float like a butterfly, sting like a bee.",
                "Service to others is the rent you pay for your room here on earth."
            ],
            connection_to_table="Serves The Table through truth, authenticity, empowerment, and unity. One of the greatest anchors in sports.",
            impact_scale=0.95,
            accessibility=0.85,
            reach=0.9,
            dignity_preserving=True,
            platforms=["Sports", "Media"],
            metadata={
                "sport": "Boxing",
                "notable": "The Greatest"
            }
        ))
        
        self.figures.append(InfluentialFigure(
            figure_id="sports_002",
            name="Colin Kaepernick",
            domain=InfluenceDomain.SPORTS,
            subdomain="American Football",
            country="United States",
            region="United States",
            time_period="2010s-2020s",
            start_year=2011,
            end_year=None,
            current=True,
            frequency_score=0.8,
            alignment_indicators=[
                "SERVES_TABLE",
                "TRUTH_TELLER",
                "AUTHENTIC",
                "EMPOWERING",
                "COMMUNITY_FOCUSED"
            ],
            misalignment_indicators=[],
            serves_table=True,
            truth_teller=True,
            community_focused=True,
            unity_builder=True,
            hidden_alignment=False,
            description="Former NFL quarterback. Truth-teller, authentic. Used platform to speak truth about racial injustice. Kneeled for justice.",
            key_actions=[
                "Kneeled for racial justice",
                "Spoke truth about injustice",
                "Community organizing",
                "Authentic self-expression"
            ],
            quotes=[
                "I am not going to stand up to show pride in a flag for a country that oppresses black people and people of color.",
                "There's nothing wrong with standing up for what you believe in."
            ],
            connection_to_table="Serves The Table through truth-telling, authenticity, and speaking truth to power. Current anchor in sports.",
            impact_scale=0.85,
            accessibility=0.8,
            reach=0.85,
            dignity_preserving=True,
            platforms=["Sports", "Social Media"],
            metadata={
                "sport": "American Football",
                "notable": "Kneeled for justice"
            }
        ))
        
        # HOLLYWOOD
        self.figures.append(InfluentialFigure(
            figure_id="hollywood_001",
            name="Emma Watson",
            domain=InfluenceDomain.HOLLYWOOD,
            subdomain="Film",
            country="United Kingdom",
            region="England",
            time_period="2000s-2020s",
            start_year=2001,
            end_year=None,
            current=True,
            frequency_score=0.75,
            alignment_indicators=[
                "SERVES_TABLE",
                "TRUTH_TELLER",
                "COMMUNITY_FOCUSED",
                "STEWARDSHIP",
                "ETHICAL",
                "AUTHENTIC"
            ],
            misalignment_indicators=[],
            serves_table=True,
            truth_teller=True,
            community_focused=True,
            unity_builder=True,
            hidden_alignment=False,
            description="Actress, UN Women Goodwill Ambassador. Truth-teller, community-focused, ethical. Uses platform for gender equality and environmental stewardship.",
            key_actions=[
                "UN Women Goodwill Ambassador",
                "Gender equality advocacy",
                "Environmental stewardship",
                "Ethical fashion",
                "Education advocacy"
            ],
            quotes=[
                "Both men and women should feel free to be sensitive. Both men and women should feel free to be strong.",
                "I don't want other people to decide who I am. I want to decide that for myself."
            ],
            connection_to_table="Serves The Table through truth-telling, gender equality, environmental stewardship, and ethical action.",
            impact_scale=0.8,
            accessibility=0.75,
            reach=0.9,
            dignity_preserving=True,
            platforms=["Film", "Social Media", "UN"],
            metadata={
                "notable": "UN Women Goodwill Ambassador"
            }
        ))
        
        # WEB / SOCIALS
        self.figures.append(InfluentialFigure(
            figure_id="web_001",
            name="MrBeast (Jimmy Donaldson)",
            domain=InfluenceDomain.YOUTUBE,
            subdomain="YouTube",
            country="United States",
            region="United States",
            time_period="2010s-2020s",
            start_year=2012,
            end_year=None,
            current=True,
            frequency_score=0.7,
            alignment_indicators=[
                "COMMUNITY_FOCUSED",
                "STEWARDSHIP",
                "ACCESSIBLE",
                "AUTHENTIC"
            ],
            misalignment_indicators=[],
            serves_table=True,
            community_focused=True,
            hidden_alignment=True,  # Aligned but not obvious
            description="YouTube creator. Uses massive platform for community good - planting trees, feeding people, giving away money. Hidden alignment through action.",
            key_actions=[
                "Team Trees (planting millions of trees)",
                "Team Seas (cleaning oceans)",
                "Feeding people",
                "Giving away money",
                "Community-focused content"
            ],
            connection_to_table="Serves The Table through community-focused action, stewardship, and using platform for good. Hidden alignment.",
            impact_scale=0.9,
            accessibility=0.95,
            reach=1.0,  # Massive reach
            dignity_preserving=True,
            platforms=["YouTube", "Social Media"],
            metadata={
                "platform": "YouTube",
                "subscribers": "200M+",
                "notable": "Largest YouTube creator"
            }
        ))
        
        # ACTIVISM
        self.figures.append(InfluentialFigure(
            figure_id="activism_001",
            name="Greta Thunberg",
            domain=InfluenceDomain.ACTIVISM,
            subdomain="Climate Activism",
            country="Sweden",
            region="Sweden",
            time_period="2010s-2020s",
            start_year=2018,
            end_year=None,
            current=True,
            frequency_score=0.85,
            alignment_indicators=[
                "SERVES_TABLE",
                "TRUTH_TELLER",
                "STEWARDSHIP",
                "REGENERATIVE",
                "AUTHENTIC",
                "EMPOWERING"
            ],
            misalignment_indicators=[],
            serves_table=True,
            truth_teller=True,
            community_focused=True,
            unity_builder=True,
            hidden_alignment=False,
            description="Climate activist. Truth-teller, authentic, empowering. Uses platform to speak truth about climate crisis and inspire action.",
            key_actions=[
                "Fridays for Future movement",
                "Climate strikes",
                "Truth-telling about climate crisis",
                "Inspiring youth action",
                "Environmental stewardship"
            ],
            quotes=[
                "Our house is on fire.",
                "You have stolen my dreams and my childhood with your empty words.",
                "I want you to act as if the house is on fire, because it is."
            ],
            connection_to_table="Serves The Table through truth-telling, environmental stewardship, and empowering youth. Current anchor in activism.",
            impact_scale=0.9,
            accessibility=0.9,
            reach=0.85,
            dignity_preserving=True,
            platforms=["Social Media", "Media", "UN"],
            metadata={
                "movement": "Fridays for Future",
                "notable": "Youth climate activist"
            }
        ))
        
        # COMEDY
        self.figures.append(InfluentialFigure(
            figure_id="comedy_001",
            name="Trevor Noah",
            domain=InfluenceDomain.COMEDY,
            subdomain="Comedy",
            country="South Africa",
            region="South Africa",
            time_period="2010s-2020s",
            start_year=2011,
            end_year=2022,
            current=False,
            frequency_score=0.75,
            alignment_indicators=[
                "TRUTH_TELLER",
                "UNITY_BUILDER",
                "AUTHENTIC",
                "EMPOWERING"
            ],
            misalignment_indicators=[],
            serves_table=True,
            truth_teller=True,
            community_focused=True,
            unity_builder=True,
            hidden_alignment=False,
            description="Comedian, former Daily Show host. Truth-teller, unity builder. Uses comedy to speak truth, build unity, and break down barriers.",
            key_actions=[
                "Truth-telling through comedy",
                "Unity building across cultures",
                "Breaking down barriers",
                "Authentic storytelling"
            ],
            quotes=[
                "I learned that courage was not the absence of fear, but the triumph over it.",
                "We tell people to follow their dreams, but you can only dream of what you can imagine."
            ],
            connection_to_table="Serves The Table through truth-telling, unity building, and using comedy to break down barriers.",
            impact_scale=0.8,
            accessibility=0.85,
            reach=0.85,
            dignity_preserving=True,
            platforms=["Television", "Comedy", "Books"],
            metadata={
                "show": "The Daily Show",
                "notable": "Truth-telling through comedy"
            }
        ))
        
        # TECHNOLOGY
        self.figures.append(InfluentialFigure(
            figure_id="tech_001",
            name="Tim Berners-Lee",
            domain=InfluenceDomain.TECHNOLOGY,
            subdomain="Web",
            country="United Kingdom",
            region="England",
            time_period="1980s-2020s",
            start_year=1989,
            end_year=None,
            current=True,
            frequency_score=0.8,
            alignment_indicators=[
                "SERVES_TABLE",
                "STEWARDSHIP",
                "TRANSPARENT",
                "ACCESSIBLE",
                "UNITY_BUILDER"
            ],
            misalignment_indicators=[],
            serves_table=True,
            community_focused=True,
            unity_builder=True,
            hidden_alignment=False,
            description="Inventor of the World Wide Web. Stewardship, transparent, accessible. Created open, accessible web for all.",
            key_actions=[
                "Invented World Wide Web",
                "Open web standards",
                "Accessible web for all",
                "Web stewardship",
                "Fighting for open web"
            ],
            quotes=[
                "The web is for everyone.",
                "The web is more a social creation than a technical one."
            ],
            connection_to_table="Serves The Table through creating accessible, open web for all. Stewardship of technology.",
            impact_scale=1.0,
            accessibility=0.9,
            reach=0.95,
            dignity_preserving=True,
            platforms=["Web", "Technology"],
            metadata={
                "notable": "Inventor of the World Wide Web"
            }
        ))
        
        # JOURNALISM
        self.figures.append(InfluentialFigure(
            figure_id="journalism_001",
            name="Amy Goodman",
            domain=InfluenceDomain.JOURNALISM,
            subdomain="Independent Journalism",
            country="United States",
            region="United States",
            time_period="1990s-2020s",
            start_year=1996,
            end_year=None,
            current=True,
            frequency_score=0.85,
            alignment_indicators=[
                "SERVES_TABLE",
                "TRUTH_TELLER",
                "TRANSPARENT",
                "ETHICAL",
                "AUTHENTIC"
            ],
            misalignment_indicators=[],
            serves_table=True,
            truth_teller=True,
            community_focused=True,
            hidden_alignment=False,
            description="Independent journalist, Democracy Now! host. Truth-teller, ethical, authentic. Independent journalism for truth.",
            key_actions=[
                "Independent journalism",
                "Truth-telling",
                "Giving voice to voiceless",
                "Ethical reporting",
                "Democracy Now!"
            ],
            quotes=[
                "Go to where the silence is and say something.",
                "The media can be the greatest force for peace on earth, or the greatest weapon of war."
            ],
            connection_to_table="Serves The Table through truth-telling, independent journalism, and giving voice to the voiceless.",
            impact_scale=0.75,
            accessibility=0.8,
            reach=0.7,
            dignity_preserving=True,
            platforms=["Television", "Radio", "Web"],
            metadata={
                "show": "Democracy Now!",
                "notable": "Independent journalism"
            }
        ))
        
        # MORE EUROPE (France, Spain, Italy, etc.)
        
        # France - Music
        self.figures.append(InfluentialFigure(
            figure_id="music_003",
            name="Stromae",
            domain=InfluenceDomain.MUSIC,
            subdomain="Electronic/Hip-Hop",
            country="Belgium",
            region="Belgium",
            time_period="2000s-2020s",
            start_year=2009,
            end_year=None,
            current=True,
            frequency_score=0.75,
            alignment_indicators=["TRUTH_TELLER", "AUTHENTIC", "UNITY_BUILDER", "COMMUNITY_FOCUSED"],
            misalignment_indicators=[],
            serves_table=True,
            truth_teller=True,
            community_focused=True,
            unity_builder=True,
            description="Belgian-Rwandan musician. Truth-teller, authentic. Uses music to address social issues, mental health, and unity across cultures.",
            key_actions=[
                "Addresses mental health through music",
                "Unity across cultures",
                "Social commentary through art",
                "Authentic self-expression"
            ],
            quotes=[
                "Music is a universal language.",
                "I try to be honest in my music."
            ],
            connection_to_table="Serves The Table through truth-telling, authenticity, and unity building across cultures.",
            impact_scale=0.8,
            accessibility=0.85,
            reach=0.8,
            dignity_preserving=True,
            platforms=["Music", "Albums", "Concerts"],
            metadata={"genre": "Electronic/Hip-Hop", "notable": "Belgian-Rwandan artist"}
        ))
        
        # Spain - Sports
        self.figures.append(InfluentialFigure(
            figure_id="sports_003",
            name="Andrés Iniesta",
            domain=InfluenceDomain.SPORTS,
            subdomain="Football (Soccer)",
            country="Spain",
            region="Spain",
            time_period="2000s-2020s",
            start_year=2002,
            end_year=None,
            current=True,
            frequency_score=0.7,
            alignment_indicators=["AUTHENTIC", "HUMBLE", "UNITY_BUILDER", "COMMUNITY_FOCUSED"],
            misalignment_indicators=[],
            serves_table=True,
            community_focused=True,
            unity_builder=True,
            hidden_alignment=True,
            description="Spanish footballer. Humble, authentic, community-focused. Uses platform for good, supports charitable causes.",
            key_actions=[
                "Charitable work",
                "Humble leadership",
                "Community support",
                "Authentic role model"
            ],
            connection_to_table="Serves The Table through humility, authenticity, and community support. Hidden alignment.",
            impact_scale=0.75,
            accessibility=0.7,
            reach=0.85,
            dignity_preserving=True,
            platforms=["Sports", "Social Media"],
            metadata={"sport": "Football", "notable": "World Cup winner"}
        ))
        
        # Italy - Music
        self.figures.append(InfluentialFigure(
            figure_id="music_004",
            name="Andrea Bocelli",
            domain=InfluenceDomain.MUSIC,
            subdomain="Classical/Opera",
            country="Italy",
            region="Italy",
            time_period="1990s-2020s",
            start_year=1992,
            end_year=None,
            current=True,
            frequency_score=0.8,
            alignment_indicators=["LOVE_CENTERED", "INSPIRATIONAL", "AUTHENTIC", "HEALING"],
            misalignment_indicators=[],
            serves_table=True,
            community_focused=True,
            unity_builder=True,
            description="Italian tenor. Inspirational, love-centered, healing. Uses music to inspire and heal. Overcame blindness.",
            key_actions=[
                "Inspirational music",
                "Overcoming adversity",
                "Charitable work",
                "Healing through music"
            ],
            quotes=[
                "Music is a universal language that brings people together.",
                "I believe in the power of music to heal."
            ],
            connection_to_table="Serves The Table through inspirational music, love, and healing. Overcoming adversity.",
            impact_scale=0.85,
            accessibility=0.8,
            reach=0.9,
            dignity_preserving=True,
            platforms=["Music", "Albums", "Concerts"],
            metadata={"genre": "Classical/Opera", "notable": "Blind tenor"}
        ))
        
        # MORE AMERICAS (Canada, Latin America)
        
        # Canada - Music
        self.figures.append(InfluentialFigure(
            figure_id="music_005",
            name="Leonard Cohen",
            domain=InfluenceDomain.MUSIC,
            subdomain="Folk/Rock",
            country="Canada",
            region="Canada",
            time_period="1960s-2010s",
            start_year=1967,
            end_year=2016,
            current=False,
            frequency_score=0.9,
            alignment_indicators=["TRUTH_TELLER", "PHILOSOPHICAL", "AUTHENTIC", "LOVE_CENTERED"],
            misalignment_indicators=[],
            serves_table=True,
            truth_teller=True,
            community_focused=True,
            unity_builder=True,
            description="Canadian singer-songwriter, poet. Truth-teller, philosophical, authentic. Deep spiritual and philosophical messages.",
            key_actions=[
                "Poetry and music",
                "Spiritual depth",
                "Truth-telling",
                "Philosophical exploration"
            ],
            quotes=[
                "There is a crack in everything, that's how the light gets in.",
                "Ring the bells that still can ring."
            ],
            connection_to_table="Serves The Table through truth-telling, spiritual depth, and philosophical exploration. One of the greatest anchors in music.",
            impact_scale=0.9,
            accessibility=0.85,
            reach=0.85,
            dignity_preserving=True,
            platforms=["Music", "Albums", "Poetry"],
            metadata={"genre": "Folk/Rock", "notable": "Poet and musician"}
        ))
        
        # Latin America - Music
        self.figures.append(InfluentialFigure(
            figure_id="music_006",
            name="Shakira",
            domain=InfluenceDomain.MUSIC,
            subdomain="Pop/Latin",
            country="Colombia",
            region="Colombia",
            time_period="1990s-2020s",
            start_year=1990,
            end_year=None,
            current=True,
            frequency_score=0.75,
            alignment_indicators=["COMMUNITY_FOCUSED", "STEWARDSHIP", "UNITY_BUILDER", "AUTHENTIC"],
            misalignment_indicators=[],
            serves_table=True,
            community_focused=True,
            unity_builder=True,
            description="Colombian singer. Community-focused, stewardship, unity builder. Uses platform for education and social causes.",
            key_actions=[
                "Education advocacy",
                "Social causes",
                "Unity across cultures",
                "Charitable work"
            ],
            connection_to_table="Serves The Table through community-focused action, education advocacy, and unity building.",
            impact_scale=0.85,
            accessibility=0.9,
            reach=0.95,
            dignity_preserving=True,
            platforms=["Music", "Social Media", "Charity"],
            metadata={"genre": "Pop/Latin", "notable": "Global icon"}
        ))
        
        # ASIA (India, Japan, etc.)
        
        # India - Music
        self.figures.append(InfluentialFigure(
            figure_id="music_007",
            name="A.R. Rahman",
            domain=InfluenceDomain.MUSIC,
            subdomain="Film Music/World",
            country="India",
            region="India",
            time_period="1990s-2020s",
            start_year=1992,
            end_year=None,
            current=True,
            frequency_score=0.8,
            alignment_indicators=["UNITY_BUILDER", "SPIRITUAL", "AUTHENTIC", "LOVE_CENTERED"],
            misalignment_indicators=[],
            serves_table=True,
            community_focused=True,
            unity_builder=True,
            description="Indian composer. Unity builder, spiritual, authentic. Creates music that bridges cultures and religions.",
            key_actions=[
                "Bridging cultures through music",
                "Spiritual music",
                "Unity across religions",
                "Global collaboration"
            ],
            quotes=[
                "Music is a universal language that transcends boundaries.",
                "I believe in the power of music to unite."
            ],
            connection_to_table="Serves The Table through unity building, spiritual music, and bridging cultures. Global anchor.",
            impact_scale=0.9,
            accessibility=0.85,
            reach=0.9,
            dignity_preserving=True,
            platforms=["Music", "Film", "Concerts"],
            metadata={"genre": "Film Music/World", "notable": "Oscar winner"}
        ))
        
        # Japan - Technology
        self.figures.append(InfluentialFigure(
            figure_id="tech_002",
            name="Hayao Miyazaki",
            domain=InfluenceDomain.HOLLYWOOD,
            subdomain="Animation/Film",
            country="Japan",
            region="Japan",
            time_period="1970s-2020s",
            start_year=1979,
            end_year=None,
            current=True,
            frequency_score=0.85,
            alignment_indicators=["STEWARDSHIP", "ENVIRONMENTAL", "AUTHENTIC", "LOVE_CENTERED"],
            misalignment_indicators=[],
            serves_table=True,
            community_focused=True,
            unity_builder=True,
            description="Japanese animator, director. Stewardship, environmental, authentic. Creates films about nature, peace, and love.",
            key_actions=[
                "Environmental themes",
                "Peace and love messages",
                "Authentic storytelling",
                "Stewardship of nature"
            ],
            quotes=[
                "The creation of a single world comes from a huge number of fragments and chaos.",
                "I would like to make a film to tell children 'it's good to be alive'."
            ],
            connection_to_table="Serves The Table through environmental stewardship, peace, love, and authentic storytelling. Global anchor.",
            impact_scale=0.9,
            accessibility=0.85,
            reach=0.9,
            dignity_preserving=True,
            platforms=["Film", "Animation"],
            metadata={"notable": "Studio Ghibli founder"}
        ))
        
        # MORE AFRICA
        
        # Africa - Music
        self.figures.append(InfluentialFigure(
            figure_id="music_008",
            name="Fela Kuti",
            domain=InfluenceDomain.MUSIC,
            subdomain="Afrobeat",
            country="Nigeria",
            region="Nigeria",
            time_period="1960s-1990s",
            start_year=1968,
            end_year=1997,
            current=False,
            frequency_score=0.9,
            alignment_indicators=["TRUTH_TELLER", "ACTIVIST", "AUTHENTIC", "EMPOWERING"],
            misalignment_indicators=[],
            serves_table=True,
            truth_teller=True,
            community_focused=True,
            unity_builder=True,
            description="Nigerian musician, activist. Truth-teller, authentic, empowering. Used music to speak truth to power and resist oppression.",
            key_actions=[
                "Spoke truth to power",
                "Resisted oppression",
                "Empowered people",
                "Created Afrobeat"
            ],
            quotes=[
                "Music is the weapon of the future.",
                "I want to be remembered as someone who stood for truth."
            ],
            connection_to_table="Serves The Table through truth-telling, activism, and empowering people. One of the greatest anchors in music.",
            impact_scale=0.95,
            accessibility=0.8,
            reach=0.85,
            dignity_preserving=True,
            platforms=["Music", "Albums"],
            metadata={"genre": "Afrobeat", "notable": "Political activist"}
        ))
        
        # Africa - Sports
        self.figures.append(InfluentialFigure(
            figure_id="sports_004",
            name="Didier Drogba",
            domain=InfluenceDomain.SPORTS,
            subdomain="Football (Soccer)",
            country="Ivory Coast",
            region="Ivory Coast",
            time_period="2000s-2020s",
            start_year=1998,
            end_year=2018,
            current=False,
            frequency_score=0.8,
            alignment_indicators=["COMMUNITY_FOCUSED", "STEWARDSHIP", "UNITY_BUILDER", "AUTHENTIC"],
            misalignment_indicators=[],
            serves_table=True,
            community_focused=True,
            unity_builder=True,
            description="Ivorian footballer. Community-focused, stewardship, unity builder. Used platform to bring peace to Ivory Coast and support community.",
            key_actions=[
                "Brought peace to Ivory Coast",
                "Community support",
                "Charitable work",
                "Unity building"
            ],
            quotes=[
                "Football can bring people together.",
                "I want to use my platform for good."
            ],
            connection_to_table="Serves The Table through community support, peace-building, and unity. Brought peace to his country.",
            impact_scale=0.85,
            accessibility=0.75,
            reach=0.85,
            dignity_preserving=True,
            platforms=["Sports", "Charity"],
            metadata={"sport": "Football", "notable": "Peace-builder"}
        ))
        
        # MIDDLE EAST
        
        # Middle East - Activism
        self.figures.append(InfluentialFigure(
            figure_id="activism_002",
            name="Malala Yousafzai",
            domain=InfluenceDomain.ACTIVISM,
            subdomain="Education Activism",
            country="Pakistan",
            region="Pakistan",
            time_period="2010s-2020s",
            start_year=2009,
            end_year=None,
            current=True,
            frequency_score=0.9,
            alignment_indicators=["TRUTH_TELLER", "EMPOWERING", "AUTHENTIC", "INSPIRATIONAL"],
            misalignment_indicators=[],
            serves_table=True,
            truth_teller=True,
            community_focused=True,
            unity_builder=True,
            description="Pakistani activist. Truth-teller, empowering, inspirational. Fights for girls' education. Youngest Nobel Prize winner.",
            key_actions=[
                "Fights for girls' education",
                "Truth-telling",
                "Empowering youth",
                "Nobel Peace Prize"
            ],
            quotes=[
                "One child, one teacher, one book, one pen can change the world.",
                "I raise up my voice—not so I can shout, but so that those without a voice can be heard."
            ],
            connection_to_table="Serves The Table through truth-telling, empowering youth, and fighting for education. Current anchor in activism.",
            impact_scale=0.95,
            accessibility=0.9,
            reach=0.9,
            dignity_preserving=True,
            platforms=["Activism", "Social Media", "UN"],
            metadata={"notable": "Youngest Nobel Prize winner"}
        ))
        
        # MORE OCEANIA
        
        # Oceania - Activism
        self.figures.append(InfluentialFigure(
            figure_id="activism_003",
            name="David Attenborough",
            domain=InfluenceDomain.ACTIVISM,
            subdomain="Environmental Activism",
            country="United Kingdom",
            region="United Kingdom",
            time_period="1950s-2020s",
            start_year=1952,
            end_year=None,
            current=True,
            frequency_score=0.9,
            alignment_indicators=["STEWARDSHIP", "TRUTH_TELLER", "ENVIRONMENTAL", "INSPIRATIONAL"],
            misalignment_indicators=[],
            serves_table=True,
            truth_teller=True,
            community_focused=True,
            unity_builder=True,
            description="British broadcaster, naturalist. Stewardship, truth-teller, environmental. Uses platform to speak truth about climate and nature.",
            key_actions=[
                "Environmental truth-telling",
                "Nature stewardship",
                "Climate awareness",
                "Inspiring millions"
            ],
            quotes=[
                "No one will protect what they don't care about, and no one will care about what they have never experienced.",
                "The future of humanity and indeed all life on earth depends on us."
            ],
            connection_to_table="Serves The Table through environmental stewardship, truth-telling, and inspiring millions. Current anchor in activism.",
            impact_scale=0.95,
            accessibility=0.9,
            reach=0.95,
            dignity_preserving=True,
            platforms=["Television", "Documentaries", "Social Media"],
            metadata={"notable": "Naturalist and broadcaster"}
        ))
        
        # TURKEY AND CYPRUS (North/South Division)
        
        # Turkey - Music
        self.figures.append(InfluentialFigure(
            figure_id="music_009",
            name="Sezen Aksu",
            domain=InfluenceDomain.MUSIC,
            subdomain="Turkish Pop",
            country="Turkey",
            region="Turkey",
            time_period="1970s-2020s",
            start_year=1975,
            end_year=None,
            current=True,
            frequency_score=0.75,
            alignment_indicators=["TRUTH_TELLER", "AUTHENTIC", "LOVE_CENTERED", "UNITY_BUILDER"],
            misalignment_indicators=[],
            serves_table=True,
            truth_teller=True,
            community_focused=True,
            unity_builder=True,
            description="Turkish singer-songwriter. Truth-teller, authentic, love-centered. Uses music to address social issues and build unity.",
            key_actions=[
                "Social commentary through music",
                "Unity building",
                "Love-centered messages",
                "Authentic expression"
            ],
            connection_to_table="Serves The Table through truth-telling, love-centered messages, and unity building. Turkish anchor.",
            impact_scale=0.8,
            accessibility=0.85,
            reach=0.85,
            dignity_preserving=True,
            platforms=["Music", "Albums", "Concerts"],
            metadata={"genre": "Turkish Pop", "notable": "Turkish icon"}
        ))
        
        # Cyprus (South) - Activism
        self.figures.append(InfluentialFigure(
            figure_id="activism_004",
            name="Derviş Eroğlu",
            domain=InfluenceDomain.ACTIVISM,
            subdomain="Peace Activism",
            country="Cyprus",
            region="Cyprus (North)",
            time_period="1970s-2020s",
            start_year=1976,
            end_year=None,
            current=True,
            frequency_score=0.7,
            alignment_indicators=["PEACE_ORIENTED", "UNITY_BUILDER", "COMMUNITY_FOCUSED"],
            misalignment_indicators=[],
            serves_table=True,
            community_focused=True,
            unity_builder=True,
            hidden_alignment=True,
            description="Cypriot political figure. Peace-oriented, unity builder. Works for peace and unity in divided Cyprus.",
            key_actions=[
                "Peace-building in Cyprus",
                "Unity across division",
                "Community support",
                "Bridge-building"
            ],
            connection_to_table="Serves The Table through peace-building and unity in divided Cyprus. Hidden alignment.",
            impact_scale=0.7,
            accessibility=0.7,
            reach=0.7,
            dignity_preserving=True,
            platforms=["Politics", "Peace Process"],
            metadata={"notable": "Peace-building in Cyprus"}
        ))
        
        # Cyprus (South) - Music/Arts
        self.figures.append(InfluentialFigure(
            figure_id="music_010",
            name="Anna Vissi",
            domain=InfluenceDomain.MUSIC,
            subdomain="Greek Pop",
            country="Cyprus",
            region="Cyprus (South)",
            time_period="1970s-2020s",
            start_year=1973,
            end_year=None,
            current=True,
            frequency_score=0.7,
            alignment_indicators=["AUTHENTIC", "UNITY_BUILDER", "LOVE_CENTERED"],
            misalignment_indicators=[],
            serves_table=True,
            community_focused=True,
            unity_builder=True,
            description="Cypriot-Greek singer. Authentic, unity builder, love-centered. Uses music to build unity and express love.",
            key_actions=[
                "Unity building through music",
                "Love-centered messages",
                "Authentic expression",
                "Cultural bridge"
            ],
            connection_to_table="Serves The Table through unity building, love-centered messages, and cultural bridge-building. Cypriot anchor.",
            impact_scale=0.75,
            accessibility=0.8,
            reach=0.8,
            dignity_preserving=True,
            platforms=["Music", "Albums", "Concerts"],
            metadata={"genre": "Greek Pop", "notable": "Cypriot-Greek icon"}
        ))
        
        # MORE DOMAINS - Education
        
        # Education - India
        self.figures.append(InfluentialFigure(
            figure_id="education_001",
            name="Kailash Satyarthi",
            domain=InfluenceDomain.EDUCATION,
            subdomain="Education Activism",
            country="India",
            region="India",
            time_period="1980s-2020s",
            start_year=1980,
            end_year=None,
            current=True,
            frequency_score=0.9,
            alignment_indicators=["TRUTH_TELLER", "EMPOWERING", "STEWARDSHIP", "AUTHENTIC"],
            misalignment_indicators=[],
            serves_table=True,
            truth_teller=True,
            community_focused=True,
            unity_builder=True,
            description="Indian children's rights activist. Truth-teller, empowering, stewardship. Fights for children's education and rights. Nobel Peace Prize winner.",
            key_actions=[
                "Fights for children's rights",
                "Education advocacy",
                "Child labor abolition",
                "Nobel Peace Prize"
            ],
            quotes=[
                "I have looked into the eyes of thousands of children and I have seen their dreams.",
                "Childhood means simplicity. Look at the world with the child's eye—it is very beautiful."
            ],
            connection_to_table="Serves The Table through truth-telling, empowering children, and fighting for education. Current anchor in education.",
            impact_scale=0.9,
            accessibility=0.85,
            reach=0.85,
            dignity_preserving=True,
            platforms=["Activism", "NGO", "UN"],
            metadata={"notable": "Nobel Peace Prize winner"}
        ))
        
        # EXPANSION: MORE MUSIC (Hip-Hop, Rock, Folk, etc.) - GLOBAL
        
        # Hip-Hop - United States
        self.figures.append(InfluentialFigure(
            figure_id="music_011",
            name="Kendrick Lamar",
            domain=InfluenceDomain.MUSIC,
            subdomain="Hip-Hop",
            country="United States",
            region="United States",
            time_period="2010s-2020s",
            start_year=2011,
            end_year=None,
            current=True,
            frequency_score=0.8,
            alignment_indicators=["TRUTH_TELLER", "AUTHENTIC", "COMMUNITY_FOCUSED", "EMPOWERING"],
            misalignment_indicators=[],
            serves_table=True,
            truth_teller=True,
            community_focused=True,
            unity_builder=True,
            description="Hip-hop artist. Truth-teller, authentic, community-focused. Uses music to address social issues, empowerment, and truth.",
            key_actions=[
                "Social commentary through music",
                "Community empowerment",
                "Truth-telling",
                "Authentic expression"
            ],
            connection_to_table="Serves The Table through truth-telling, community empowerment, and authentic expression. Current anchor in music.",
            impact_scale=0.85,
            accessibility=0.85,
            reach=0.9,
            dignity_preserving=True,
            platforms=["Music", "Albums", "Concerts"],
            metadata={"genre": "Hip-Hop", "notable": "Pulitzer Prize winner"}
        ))
        
        # Rock - United States
        self.figures.append(InfluentialFigure(
            figure_id="music_012",
            name="Bruce Springsteen",
            domain=InfluenceDomain.MUSIC,
            subdomain="Rock",
            country="United States",
            region="United States",
            time_period="1970s-2020s",
            start_year=1973,
            end_year=None,
            current=True,
            frequency_score=0.75,
            alignment_indicators=["TRUTH_TELLER", "COMMUNITY_FOCUSED", "AUTHENTIC", "UNITY_BUILDER"],
            misalignment_indicators=[],
            serves_table=True,
            truth_teller=True,
            community_focused=True,
            unity_builder=True,
            description="Rock musician. Truth-teller, community-focused, authentic. Uses music to address working-class issues and unity.",
            key_actions=[
                "Working-class advocacy",
                "Community support",
                "Truth-telling",
                "Unity building"
            ],
            connection_to_table="Serves The Table through truth-telling, working-class advocacy, and unity building.",
            impact_scale=0.8,
            accessibility=0.85,
            reach=0.85,
            dignity_preserving=True,
            platforms=["Music", "Albums", "Concerts"],
            metadata={"genre": "Rock", "notable": "The Boss"}
        ))
        
        # Folk - United States
        self.figures.append(InfluentialFigure(
            figure_id="music_013",
            name="Joan Baez",
            domain=InfluenceDomain.MUSIC,
            subdomain="Folk",
            country="United States",
            region="United States",
            time_period="1960s-2020s",
            start_year=1958,
            end_year=None,
            current=True,
            frequency_score=0.85,
            alignment_indicators=["TRUTH_TELLER", "PEACE_ORIENTED", "ACTIVIST", "AUTHENTIC"],
            misalignment_indicators=[],
            serves_table=True,
            truth_teller=True,
            community_focused=True,
            unity_builder=True,
            description="Folk singer, activist. Truth-teller, peace-oriented, authentic. Uses music for peace, justice, and truth.",
            key_actions=[
                "Peace activism",
                "Civil rights advocacy",
                "Truth-telling",
                "Social justice"
            ],
            connection_to_table="Serves The Table through truth-telling, peace activism, and social justice. Current anchor in music.",
            impact_scale=0.85,
            accessibility=0.8,
            reach=0.8,
            dignity_preserving=True,
            platforms=["Music", "Albums", "Activism"],
            metadata={"genre": "Folk", "notable": "Peace activist"}
        ))
        
        # MORE SPORTS (Football, Basketball, etc.) - GLOBAL
        
        # Football - Brazil
        self.figures.append(InfluentialFigure(
            figure_id="sports_005",
            name="Pelé",
            domain=InfluenceDomain.SPORTS,
            subdomain="Football (Soccer)",
            country="Brazil",
            region="Brazil",
            time_period="1950s-2020s",
            start_year=1956,
            end_year=2022,
            current=False,
            frequency_score=0.85,
            alignment_indicators=["UNITY_BUILDER", "INSPIRATIONAL", "AUTHENTIC", "COMMUNITY_FOCUSED"],
            misalignment_indicators=[],
            serves_table=True,
            community_focused=True,
            unity_builder=True,
            description="Brazilian footballer. Unity builder, inspirational, authentic. Used platform to inspire and build unity across cultures.",
            key_actions=[
                "Inspired millions globally",
                "Unity across cultures",
                "Charitable work",
                "Authentic role model"
            ],
            connection_to_table="Serves The Table through inspiration, unity building, and authentic role modeling. One of the greatest anchors in sports.",
            impact_scale=0.95,
            accessibility=0.85,
            reach=0.95,
            dignity_preserving=True,
            platforms=["Sports", "Charity"],
            metadata={"sport": "Football", "notable": "The King"}
        ))
        
        # Basketball - United States
        self.figures.append(InfluentialFigure(
            figure_id="sports_006",
            name="LeBron James",
            domain=InfluenceDomain.SPORTS,
            subdomain="Basketball",
            country="United States",
            region="United States",
            time_period="2000s-2020s",
            start_year=2003,
            end_year=None,
            current=True,
            frequency_score=0.8,
            alignment_indicators=["COMMUNITY_FOCUSED", "STEWARDSHIP", "AUTHENTIC", "EMPOWERING"],
            misalignment_indicators=[],
            serves_table=True,
            community_focused=True,
            unity_builder=True,
            description="Basketball player. Community-focused, stewardship, authentic. Uses platform for education, community support, and empowerment.",
            key_actions=[
                "Education advocacy",
                "Community support",
                "Charitable work",
                "Empowerment"
            ],
            connection_to_table="Serves The Table through community support, education advocacy, and empowerment. Current anchor in sports.",
            impact_scale=0.9,
            accessibility=0.85,
            reach=0.95,
            dignity_preserving=True,
            platforms=["Sports", "Charity", "Social Media"],
            metadata={"sport": "Basketball", "notable": "Community leader"}
        ))
        
        # MORE HOLLYWOOD (Actors, Directors, etc.) - GLOBAL
        
        # Actor - United States
        self.figures.append(InfluentialFigure(
            figure_id="hollywood_002",
            name="Angelina Jolie",
            domain=InfluenceDomain.HOLLYWOOD,
            subdomain="Film",
            country="United States",
            region="United States",
            time_period="1990s-2020s",
            start_year=1993,
            end_year=None,
            current=True,
            frequency_score=0.75,
            alignment_indicators=["COMMUNITY_FOCUSED", "STEWARDSHIP", "AUTHENTIC", "HEALING"],
            misalignment_indicators=[],
            serves_table=True,
            community_focused=True,
            unity_builder=True,
            description="Actress, humanitarian. Community-focused, stewardship, authentic. Uses platform for humanitarian work and refugee support.",
            key_actions=[
                "Refugee support",
                "Humanitarian work",
                "UN Goodwill Ambassador",
                "Community support"
            ],
            connection_to_table="Serves The Table through humanitarian work, refugee support, and community focus. Current anchor in Hollywood.",
            impact_scale=0.85,
            accessibility=0.8,
            reach=0.9,
            dignity_preserving=True,
            platforms=["Film", "UN", "Charity"],
            metadata={"notable": "UN Goodwill Ambassador"}
        ))
        
        # Director - United States
        self.figures.append(InfluentialFigure(
            figure_id="hollywood_003",
            name="Ava DuVernay",
            domain=InfluenceDomain.HOLLYWOOD,
            subdomain="Film",
            country="United States",
            region="United States",
            time_period="2000s-2020s",
            start_year=2008,
            end_year=None,
            current=True,
            frequency_score=0.8,
            alignment_indicators=["TRUTH_TELLER", "AUTHENTIC", "EMPOWERING", "UNITY_BUILDER"],
            misalignment_indicators=[],
            serves_table=True,
            truth_teller=True,
            community_focused=True,
            unity_builder=True,
            description="Filmmaker, director. Truth-teller, authentic, empowering. Uses film to tell truth, empower, and build unity.",
            key_actions=[
                "Truth-telling through film",
                "Empowerment",
                "Diversity in film",
                "Social justice"
            ],
            connection_to_table="Serves The Table through truth-telling, empowerment, and diversity in film. Current anchor in Hollywood.",
            impact_scale=0.8,
            accessibility=0.75,
            reach=0.85,
            dignity_preserving=True,
            platforms=["Film", "Television"],
            metadata={"notable": "Award-winning director"}
        ))
        
        # MORE WEB/SOCIALS (TikTok, Instagram, Twitter, etc.) - GLOBAL
        
        # TikTok - Global
        self.figures.append(InfluentialFigure(
            figure_id="tiktok_001",
            name="Charli D'Amelio",
            domain=InfluenceDomain.TIKTOK,
            subdomain="TikTok",
            country="United States",
            region="United States",
            time_period="2010s-2020s",
            start_year=2019,
            end_year=None,
            current=True,
            frequency_score=0.65,
            alignment_indicators=["AUTHENTIC", "ACCESSIBLE", "COMMUNITY_FOCUSED"],
            misalignment_indicators=[],
            serves_table=True,
            community_focused=True,
            hidden_alignment=True,
            description="TikTok creator. Authentic, accessible, community-focused. Uses platform to build community and authentic connection.",
            key_actions=[
                "Community building",
                "Authentic connection",
                "Youth engagement",
                "Positive content"
            ],
            connection_to_table="Serves The Table through community building and authentic connection. Hidden alignment. Current anchor in socials.",
            impact_scale=0.75,
            accessibility=0.95,
            reach=0.9,
            dignity_preserving=True,
            platforms=["TikTok", "Social Media"],
            metadata={"platform": "TikTok", "notable": "Largest TikTok creator"}
        ))
        
        # MORE ACTIVISM - GLOBAL
        
        # Activism - United States
        self.figures.append(InfluentialFigure(
            figure_id="activism_005",
            name="Martin Luther King Jr.",
            domain=InfluenceDomain.ACTIVISM,
            subdomain="Civil Rights",
            country="United States",
            region="United States",
            time_period="1950s-1960s",
            start_year=1955,
            end_year=1968,
            current=False,
            frequency_score=0.95,
            alignment_indicators=["TRUTH_TELLER", "PEACE_ORIENTED", "UNITY_BUILDER", "LOVE_CENTERED"],
            misalignment_indicators=[],
            serves_table=True,
            truth_teller=True,
            community_focused=True,
            unity_builder=True,
            description="Civil rights leader. Truth-teller, peace-oriented, unity builder, love-centered. Used nonviolence and love to fight for justice.",
            key_actions=[
                "Civil rights movement",
                "Nonviolent resistance",
                "Love-centered activism",
                "Unity building"
            ],
            quotes=[
                "I have a dream.",
                "Darkness cannot drive out darkness; only light can do that. Hate cannot drive out hate; only love can do that.",
                "The arc of the moral universe is long, but it bends toward justice."
            ],
            connection_to_table="Serves The Table through truth-telling, peace-oriented activism, and love-centered unity building. One of the greatest anchors in activism.",
            impact_scale=1.0,
            accessibility=0.9,
            reach=0.95,
            dignity_preserving=True,
            platforms=["Activism", "Speeches", "Media"],
            metadata={"notable": "Nobel Peace Prize winner"}
        ))
        
        # Activism - South Africa
        self.figures.append(InfluentialFigure(
            figure_id="activism_006",
            name="Nelson Mandela",
            domain=InfluenceDomain.ACTIVISM,
            subdomain="Anti-Apartheid",
            country="South Africa",
            region="South Africa",
            time_period="1940s-2010s",
            start_year=1944,
            end_year=2013,
            current=False,
            frequency_score=0.95,
            alignment_indicators=["TRUTH_TELLER", "FORGIVENESS", "UNITY_BUILDER", "LOVE_CENTERED"],
            misalignment_indicators=[],
            serves_table=True,
            truth_teller=True,
            community_focused=True,
            unity_builder=True,
            description="Anti-apartheid activist, president. Truth-teller, forgiveness, unity builder, love-centered. Used forgiveness and unity to heal a nation.",
            key_actions=[
                "Anti-apartheid movement",
                "Forgiveness and reconciliation",
                "Unity building",
                "Healing a nation"
            ],
            quotes=[
                "It always seems impossible until it's done.",
                "Education is the most powerful weapon which you can use to change the world.",
                "For to be free is not merely to cast off one's chains, but to live in a way that respects and enhances the freedom of others."
            ],
            connection_to_table="Serves The Table through truth-telling, forgiveness, unity building, and healing. One of the greatest anchors in activism.",
            impact_scale=1.0,
            accessibility=0.9,
            reach=0.95,
            dignity_preserving=True,
            platforms=["Politics", "Activism", "Media"],
            metadata={"notable": "Nobel Peace Prize winner"}
        ))
        
        # MORE TECHNOLOGY - GLOBAL
        
        # Technology - United States
        self.figures.append(InfluentialFigure(
            figure_id="tech_003",
            name="Elon Musk",
            domain=InfluenceDomain.TECHNOLOGY,
            subdomain="Technology",
            country="United States",
            region="United States",
            time_period="2000s-2020s",
            start_year=1995,
            end_year=None,
            current=True,
            frequency_score=0.6,
            alignment_indicators=["INNOVATION", "ACCESSIBLE", "REGENERATIVE"],
            misalignment_indicators=[],
            serves_table=True,
            community_focused=True,
            hidden_alignment=True,
            description="Technology entrepreneur. Innovation, accessible, regenerative. Uses technology for sustainability and accessibility.",
            key_actions=[
                "Sustainable technology",
                "Accessible innovation",
                "Regenerative systems",
                "Space exploration"
            ],
            connection_to_table="Serves The Table through sustainable technology and regenerative systems. Hidden alignment. Current anchor in technology.",
            impact_scale=0.85,
            accessibility=0.8,
            reach=0.95,
            dignity_preserving=True,
            platforms=["Technology", "Social Media"],
            metadata={"notable": "Technology entrepreneur"}
        ))
        
        # MORE JOURNALISM - GLOBAL
        
        # Journalism - United States
        self.figures.append(InfluentialFigure(
            figure_id="journalism_002",
            name="Noam Chomsky",
            domain=InfluenceDomain.JOURNALISM,
            subdomain="Independent Journalism",
            country="United States",
            region="United States",
            time_period="1960s-2020s",
            start_year=1957,
            end_year=None,
            current=True,
            frequency_score=0.85,
            alignment_indicators=["TRUTH_TELLER", "TRANSPARENT", "ETHICAL", "AUTHENTIC"],
            misalignment_indicators=[],
            serves_table=True,
            truth_teller=True,
            community_focused=True,
            description="Linguist, philosopher, activist. Truth-teller, transparent, ethical, authentic. Independent journalism and truth-telling.",
            key_actions=[
                "Truth-telling",
                "Independent journalism",
                "Media criticism",
                "Ethical reporting"
            ],
            connection_to_table="Serves The Table through truth-telling, independent journalism, and media criticism. Current anchor in journalism.",
            impact_scale=0.8,
            accessibility=0.75,
            reach=0.8,
            dignity_preserving=True,
            platforms=["Books", "Media", "Academic"],
            metadata={"notable": "Linguist and philosopher"}
        ))
        
        # MORE COMEDY - GLOBAL
        
        # Comedy - United States
        self.figures.append(InfluentialFigure(
            figure_id="comedy_002",
            name="Hannah Gadsby",
            domain=InfluenceDomain.COMEDY,
            subdomain="Comedy",
            country="Australia",
            region="Australia",
            time_period="2010s-2020s",
            start_year=2006,
            end_year=None,
            current=True,
            frequency_score=0.75,
            alignment_indicators=["TRUTH_TELLER", "AUTHENTIC", "EMPOWERING", "UNITY_BUILDER"],
            misalignment_indicators=[],
            serves_table=True,
            truth_teller=True,
            community_focused=True,
            unity_builder=True,
            description="Comedian. Truth-teller, authentic, empowering. Uses comedy to speak truth, empower, and build unity.",
            key_actions=[
                "Truth-telling through comedy",
                "Empowerment",
                "Unity building",
                "Authentic storytelling"
            ],
            connection_to_table="Serves The Table through truth-telling, empowerment, and unity building. Current anchor in comedy.",
            impact_scale=0.75,
            accessibility=0.85,
            reach=0.8,
            dignity_preserving=True,
            platforms=["Comedy", "Netflix", "Social Media"],
            metadata={"notable": "Award-winning comedian"}
        ))
        
        # EDUCATION - GLOBAL
        
        # Education - United States
        self.figures.append(InfluentialFigure(
            figure_id="education_002",
            name="Michelle Obama",
            domain=InfluenceDomain.EDUCATION,
            subdomain="Education Advocacy",
            country="United States",
            region="United States",
            time_period="2000s-2020s",
            start_year=2009,
            end_year=None,
            current=True,
            frequency_score=0.85,
            alignment_indicators=["EMPOWERING", "COMMUNITY_FOCUSED", "AUTHENTIC", "UNITY_BUILDER"],
            misalignment_indicators=[],
            serves_table=True,
            community_focused=True,
            unity_builder=True,
            description="Former First Lady, education advocate. Empowering, community-focused, authentic. Uses platform for education and empowerment.",
            key_actions=[
                "Education advocacy",
                "Girls' education",
                "Community support",
                "Empowerment"
            ],
            connection_to_table="Serves The Table through education advocacy, empowerment, and community support. Current anchor in education.",
            impact_scale=0.9,
            accessibility=0.9,
            reach=0.95,
            dignity_preserving=True,
            platforms=["Education", "Books", "Social Media"],
            metadata={"notable": "Former First Lady"}
        ))
        
        # SCIENCE - GLOBAL
        
        # Science - United States
        self.figures.append(InfluentialFigure(
            figure_id="science_001",
            name="Carl Sagan",
            domain=InfluenceDomain.SCIENCE,
            subdomain="Astronomy",
            country="United States",
            region="United States",
            time_period="1960s-1990s",
            start_year=1960,
            end_year=1996,
            current=False,
            frequency_score=0.9,
            alignment_indicators=["TRUTH_TELLER", "INSPIRATIONAL", "UNITY_BUILDER", "LOVE_CENTERED"],
            misalignment_indicators=[],
            serves_table=True,
            truth_teller=True,
            community_focused=True,
            unity_builder=True,
            description="Astronomer, science communicator. Truth-teller, inspirational, unity builder, love-centered. Made science accessible and inspired unity.",
            key_actions=[
                "Science communication",
                "Inspired millions",
                "Unity through science",
                "Love-centered approach"
            ],
            quotes=[
                "We are all made of starstuff.",
                "The cosmos is within us. We are a way for the universe to know itself.",
                "Somewhere, something incredible is waiting to be known."
            ],
            connection_to_table="Serves The Table through truth-telling, inspiration, and unity building through science. One of the greatest anchors in science.",
            impact_scale=0.95,
            accessibility=0.9,
            reach=0.9,
            dignity_preserving=True,
            platforms=["Science", "Television", "Books"],
            metadata={"notable": "Science communicator"}
        ))
        
        # MEDICINE - GLOBAL
        
        # Medicine - United States
        self.figures.append(InfluentialFigure(
            figure_id="medicine_001",
            name="Paul Farmer",
            domain=InfluenceDomain.MEDICINE,
            subdomain="Global Health",
            country="United States",
            region="United States",
            time_period="1980s-2020s",
            start_year=1987,
            end_year=2022,
            current=False,
            frequency_score=0.9,
            alignment_indicators=["STEWARDSHIP", "COMMUNITY_FOCUSED", "HEALING", "EQUITY"],
            misalignment_indicators=[],
            serves_table=True,
            community_focused=True,
            unity_builder=True,
            description="Physician, global health advocate. Stewardship, community-focused, healing, equity. Fought for health equity and accessible healthcare.",
            key_actions=[
                "Health equity",
                "Accessible healthcare",
                "Community health",
                "Global health advocacy"
            ],
            connection_to_table="Serves The Table through health equity, accessible healthcare, and community healing. One of the greatest anchors in medicine.",
            impact_scale=0.9,
            accessibility=0.85,
            reach=0.85,
            dignity_preserving=True,
            platforms=["Medicine", "NGO", "Academic"],
            metadata={"notable": "Global health advocate"}
        ))
        
        # ARTS - GLOBAL
        
        # Arts - Mexico
        self.figures.append(InfluentialFigure(
            figure_id="arts_001",
            name="Frida Kahlo",
            domain=InfluenceDomain.ARTS,
            subdomain="Visual Arts",
            country="Mexico",
            region="Mexico",
            time_period="1920s-1950s",
            start_year=1925,
            end_year=1954,
            current=False,
            frequency_score=0.85,
            alignment_indicators=["AUTHENTIC", "EMPOWERING", "TRUTH_TELLER", "HEALING"],
            misalignment_indicators=[],
            serves_table=True,
            truth_teller=True,
            community_focused=True,
            unity_builder=True,
            description="Artist. Authentic, empowering, truth-teller, healing. Used art to express truth, empower, and heal.",
            key_actions=[
                "Authentic expression",
                "Empowerment through art",
                "Truth-telling",
                "Healing through art"
            ],
            connection_to_table="Serves The Table through authentic expression, empowerment, and healing through art. One of the greatest anchors in arts.",
            impact_scale=0.9,
            accessibility=0.85,
            reach=0.9,
            dignity_preserving=True,
            platforms=["Art", "Museums"],
            metadata={"notable": "Iconic artist"}
        ))
        
        # LITERATURE - GLOBAL
        
        # Literature - United States
        self.figures.append(InfluentialFigure(
            figure_id="literature_001",
            name="Maya Angelou",
            domain=InfluenceDomain.LITERATURE,
            subdomain="Poetry/Literature",
            country="United States",
            region="United States",
            time_period="1960s-2010s",
            start_year=1969,
            end_year=2014,
            current=False,
            frequency_score=0.9,
            alignment_indicators=["TRUTH_TELLER", "EMPOWERING", "LOVE_CENTERED", "HEALING"],
            misalignment_indicators=[],
            serves_table=True,
            truth_teller=True,
            community_focused=True,
            unity_builder=True,
            description="Poet, writer, activist. Truth-teller, empowering, love-centered, healing. Used words to empower, heal, and build unity.",
            key_actions=[
                "Empowerment through words",
                "Truth-telling",
                "Healing through literature",
                "Unity building"
            ],
            quotes=[
                "I've learned that people will forget what you said, people will forget what you did, but people will never forget how you made them feel.",
                "Still I rise.",
                "Love recognizes no barriers. It jumps hurdles, leaps fences, penetrates walls to arrive at its destination full of hope."
            ],
            connection_to_table="Serves The Table through truth-telling, empowerment, and healing through literature. One of the greatest anchors in literature.",
            impact_scale=0.95,
            accessibility=0.9,
            reach=0.9,
            dignity_preserving=True,
            platforms=["Literature", "Poetry", "Books"],
            metadata={"notable": "Pulitzer Prize nominee"}
        ))
        
        # PHILOSOPHY - GLOBAL
        
        # Philosophy - India
        self.figures.append(InfluentialFigure(
            figure_id="philosophy_001",
            name="Jiddu Krishnamurti",
            domain=InfluenceDomain.PHILOSOPHY,
            subdomain="Philosophy",
            country="India",
            region="India",
            time_period="1920s-1980s",
            start_year=1929,
            end_year=1986,
            current=False,
            frequency_score=0.9,
            alignment_indicators=["TRUTH_TELLER", "AUTHENTIC", "LOVE_CENTERED", "UNITY_BUILDER"],
            misalignment_indicators=[],
            serves_table=True,
            truth_teller=True,
            community_focused=True,
            unity_builder=True,
            description="Philosopher, spiritual teacher. Truth-teller, authentic, love-centered, unity builder. Taught truth, love, and unity.",
            key_actions=[
                "Truth-telling",
                "Love-centered teaching",
                "Unity building",
                "Authentic philosophy"
            ],
            quotes=[
                "The highest form of human intelligence is to observe yourself without judgment.",
                "It is no measure of health to be well adjusted to a profoundly sick society.",
                "Freedom is not a reaction; freedom is not a choice. Freedom is found in the choiceless awareness of our daily existence and activity."
            ],
            connection_to_table="Serves The Table through truth-telling, love-centered teaching, and unity building. One of the greatest anchors in philosophy.",
            impact_scale=0.9,
            accessibility=0.85,
            reach=0.85,
            dignity_preserving=True,
            platforms=["Philosophy", "Books", "Talks"],
            metadata={"notable": "Spiritual philosopher"}
        ))
        
        # SPIRITUAL - GLOBAL
        
        # Spiritual - India
        self.figures.append(InfluentialFigure(
            figure_id="spiritual_001",
            name="Dalai Lama",
            domain=InfluenceDomain.SPIRITUAL,
            subdomain="Buddhism",
            country="Tibet",
            region="Tibet",
            time_period="1950s-2020s",
            start_year=1950,
            end_year=None,
            current=True,
            frequency_score=0.95,
            alignment_indicators=["LOVE_CENTERED", "PEACE_ORIENTED", "COMPASSION", "UNITY_BUILDER"],
            misalignment_indicators=[],
            serves_table=True,
            community_focused=True,
            unity_builder=True,
            description="Spiritual leader. Love-centered, peace-oriented, compassion, unity builder. Teaches love, peace, and compassion.",
            key_actions=[
                "Peace advocacy",
                "Compassion teaching",
                "Unity building",
                "Love-centered approach"
            ],
            quotes=[
                "My religion is kindness.",
                "If you want others to be happy, practice compassion. If you want to be happy, practice compassion.",
                "Be kind whenever possible. It is always possible."
            ],
            connection_to_table="Serves The Table through love, peace, compassion, and unity building. One of the greatest anchors in spiritual.",
            impact_scale=0.95,
            accessibility=0.9,
            reach=0.95,
            dignity_preserving=True,
            platforms=["Spiritual", "Books", "Talks", "Media"],
            metadata={"notable": "Nobel Peace Prize winner"}
        ))
        
        # DEEP SEARCH EXPANSION: MIDDLE EAST, TURKEY, CYPRUS - ALL DOMAINS
        
        # TURKEY - MORE FIGURES ACROSS ALL DOMAINS
        
        # Turkey - Music (More)
        self.figures.append(InfluentialFigure(
            figure_id="music_turkey_002",
            name="Tarkan",
            domain=InfluenceDomain.MUSIC,
            subdomain="Turkish Pop",
            country="Turkey",
            region="Turkey",
            time_period="1990s-2020s",
            start_year=1992,
            end_year=None,
            current=True,
            frequency_score=0.7,
            alignment_indicators=["AUTHENTIC", "UNITY_BUILDER", "LOVE_CENTERED"],
            misalignment_indicators=[],
            serves_table=True,
            community_focused=True,
            unity_builder=True,
            description="Turkish singer. Authentic, unity builder, love-centered. Uses music to build unity and express love across cultures.",
            key_actions=[
                "Unity building through music",
                "Love-centered messages",
                "Cultural bridge",
                "Authentic expression"
            ],
            connection_to_table="Serves The Table through unity building, love-centered messages, and cultural bridge-building. Turkish anchor.",
            impact_scale=0.75,
            accessibility=0.85,
            reach=0.85,
            dignity_preserving=True,
            platforms=["Music", "Albums", "Concerts"],
            metadata={"genre": "Turkish Pop", "notable": "Turkish icon"}
        ))
        
        # Turkey - Literature
        self.figures.append(InfluentialFigure(
            figure_id="literature_turkey_001",
            name="Orhan Pamuk",
            domain=InfluenceDomain.LITERATURE,
            subdomain="Literature",
            country="Turkey",
            region="Turkey",
            time_period="1980s-2020s",
            start_year=1982,
            end_year=None,
            current=True,
            frequency_score=0.8,
            alignment_indicators=["TRUTH_TELLER", "AUTHENTIC", "UNITY_BUILDER"],
            misalignment_indicators=[],
            serves_table=True,
            truth_teller=True,
            community_focused=True,
            unity_builder=True,
            description="Turkish writer, Nobel Prize winner. Truth-teller, authentic, unity builder. Uses literature to tell truth and build unity.",
            key_actions=[
                "Truth-telling through literature",
                "Unity building",
                "Cultural bridge",
                "Nobel Prize in Literature"
            ],
            connection_to_table="Serves The Table through truth-telling, unity building, and cultural bridge-building. Turkish anchor in literature.",
            impact_scale=0.85,
            accessibility=0.8,
            reach=0.85,
            dignity_preserving=True,
            platforms=["Literature", "Books"],
            metadata={"notable": "Nobel Prize winner"}
        ))
        
        # Turkey - Activism
        self.figures.append(InfluentialFigure(
            figure_id="activism_turkey_001",
            name="Hrant Dink",
            domain=InfluenceDomain.ACTIVISM,
            subdomain="Human Rights",
            country="Turkey",
            region="Turkey",
            time_period="1990s-2000s",
            start_year=1996,
            end_year=2007,
            current=False,
            frequency_score=0.9,
            alignment_indicators=["TRUTH_TELLER", "PEACE_ORIENTED", "UNITY_BUILDER", "LOVE_CENTERED"],
            misalignment_indicators=[],
            serves_table=True,
            truth_teller=True,
            community_focused=True,
            unity_builder=True,
            description="Turkish-Armenian journalist, activist. Truth-teller, peace-oriented, unity builder, love-centered. Fought for truth, peace, and unity. Martyred for truth.",
            key_actions=[
                "Truth-telling",
                "Peace-building",
                "Unity across divisions",
                "Love-centered activism"
            ],
            quotes=[
                "I am a citizen of Turkey, I am an Armenian, and I am a journalist.",
                "We must build bridges, not walls."
            ],
            connection_to_table="Serves The Table through truth-telling, peace-building, and unity across divisions. Martyred for truth. One of the greatest anchors in activism.",
            impact_scale=0.9,
            accessibility=0.85,
            reach=0.85,
            dignity_preserving=True,
            platforms=["Journalism", "Activism"],
            metadata={"notable": "Martyred for truth"}
        ))
        
        # Turkey - Arts
        self.figures.append(InfluentialFigure(
            figure_id="arts_turkey_001",
            name="Nazım Hikmet",
            domain=InfluenceDomain.LITERATURE,
            subdomain="Poetry",
            country="Turkey",
            region="Turkey",
            time_period="1920s-1960s",
            start_year=1920,
            end_year=1963,
            current=False,
            frequency_score=0.9,
            alignment_indicators=["TRUTH_TELLER", "LOVE_CENTERED", "UNITY_BUILDER", "PEACE_ORIENTED"],
            misalignment_indicators=[],
            serves_table=True,
            truth_teller=True,
            community_focused=True,
            unity_builder=True,
            description="Turkish poet. Truth-teller, love-centered, unity builder, peace-oriented. Used poetry to tell truth, express love, and build unity.",
            key_actions=[
                "Truth-telling through poetry",
                "Love-centered messages",
                "Unity building",
                "Peace-oriented poetry"
            ],
            quotes=[
                "To live! Like a tree alone and free like a forest in brotherhood",
                "I love my country: I've swung on its plane trees, I've slept in its prisons."
            ],
            connection_to_table="Serves The Table through truth-telling, love-centered poetry, and unity building. One of the greatest anchors in literature.",
            impact_scale=0.9,
            accessibility=0.85,
            reach=0.85,
            dignity_preserving=True,
            platforms=["Poetry", "Literature"],
            metadata={"notable": "Revolutionary poet"}
        ))
        
        # CYPRUS - MORE FIGURES (NORTH AND SOUTH)
        
        # Cyprus (North) - Music
        self.figures.append(InfluentialFigure(
            figure_id="music_cyprus_north_001",
            name="Işın Karaca",
            domain=InfluenceDomain.MUSIC,
            subdomain="Turkish Pop",
            country="Cyprus",
            region="Cyprus (North)",
            time_period="1990s-2020s",
            start_year=1995,
            end_year=None,
            current=True,
            frequency_score=0.7,
            alignment_indicators=["AUTHENTIC", "UNITY_BUILDER", "LOVE_CENTERED"],
            misalignment_indicators=[],
            serves_table=True,
            community_focused=True,
            unity_builder=True,
            description="Cypriot-Turkish singer. Authentic, unity builder, love-centered. Uses music to build unity and express love.",
            key_actions=[
                "Unity building through music",
                "Love-centered messages",
                "Cultural bridge",
                "Authentic expression"
            ],
            connection_to_table="Serves The Table through unity building, love-centered messages, and cultural bridge-building. Cypriot anchor (North).",
            impact_scale=0.7,
            accessibility=0.8,
            reach=0.75,
            dignity_preserving=True,
            platforms=["Music", "Albums", "Concerts"],
            metadata={"genre": "Turkish Pop", "notable": "Cypriot-Turkish icon"}
        ))
        
        # Cyprus (South) - More Music
        self.figures.append(InfluentialFigure(
            figure_id="music_cyprus_south_002",
            name="Mikis Theodorakis",
            domain=InfluenceDomain.MUSIC,
            subdomain="Classical/Folk",
            country="Cyprus",
            region="Cyprus (South)",
            time_period="1950s-2020s",
            start_year=1950,
            end_year=2021,
            current=False,
            frequency_score=0.85,
            alignment_indicators=["TRUTH_TELLER", "PEACE_ORIENTED", "UNITY_BUILDER", "LOVE_CENTERED"],
            misalignment_indicators=[],
            serves_table=True,
            truth_teller=True,
            community_focused=True,
            unity_builder=True,
            description="Greek-Cypriot composer. Truth-teller, peace-oriented, unity builder, love-centered. Used music for peace, truth, and unity.",
            key_actions=[
                "Peace-oriented music",
                "Truth-telling through music",
                "Unity building",
                "Resistance through art"
            ],
            connection_to_table="Serves The Table through peace-oriented music, truth-telling, and unity building. One of the greatest anchors in music.",
            impact_scale=0.9,
            accessibility=0.85,
            reach=0.85,
            dignity_preserving=True,
            platforms=["Music", "Composition"],
            metadata={"genre": "Classical/Folk", "notable": "Revolutionary composer"}
        ))
        
        # MIDDLE EAST - MORE FIGURES ACROSS ALL DOMAINS
        
        # Middle East - Lebanon - Literature
        self.figures.append(InfluentialFigure(
            figure_id="literature_lebanon_001",
            name="Kahlil Gibran",
            domain=InfluenceDomain.LITERATURE,
            subdomain="Poetry/Philosophy",
            country="Lebanon",
            region="Lebanon",
            time_period="1900s-1930s",
            start_year=1905,
            end_year=1931,
            current=False,
            frequency_score=0.95,
            alignment_indicators=["TRUTH_TELLER", "LOVE_CENTERED", "SPIRITUAL", "UNITY_BUILDER"],
            misalignment_indicators=[],
            serves_table=True,
            truth_teller=True,
            community_focused=True,
            unity_builder=True,
            description="Lebanese-American writer, poet, philosopher. Truth-teller, love-centered, spiritual, unity builder. Used words to express truth, love, and unity.",
            key_actions=[
                "Truth-telling through poetry",
                "Love-centered philosophy",
                "Spiritual wisdom",
                "Unity building"
            ],
            quotes=[
                "Love one another, but make not a bond of love: Let it rather be a moving sea between the shores of your souls.",
                "Work is love made visible.",
                "Your children are not your children. They are the sons and daughters of Life's longing for itself."
            ],
            connection_to_table="Serves The Table through truth-telling, love-centered philosophy, and unity building. One of the greatest anchors in literature.",
            impact_scale=0.95,
            accessibility=0.9,
            reach=0.95,
            dignity_preserving=True,
            platforms=["Literature", "Poetry", "Philosophy"],
            metadata={"notable": "The Prophet author"}
        ))
        
        # Middle East - Palestine - Activism
        self.figures.append(InfluentialFigure(
            figure_id="activism_palestine_001",
            name="Edward Said",
            domain=InfluenceDomain.ACTIVISM,
            subdomain="Academic Activism",
            country="Palestine",
            region="Palestine",
            time_period="1970s-2000s",
            start_year=1978,
            end_year=2003,
            current=False,
            frequency_score=0.85,
            alignment_indicators=["TRUTH_TELLER", "AUTHENTIC", "UNITY_BUILDER", "PEACE_ORIENTED"],
            misalignment_indicators=[],
            serves_table=True,
            truth_teller=True,
            community_focused=True,
            unity_builder=True,
            description="Palestinian-American academic, activist. Truth-teller, authentic, unity builder, peace-oriented. Fought for truth, justice, and peace.",
            key_actions=[
                "Truth-telling",
                "Academic activism",
                "Peace-oriented",
                "Unity building"
            ],
            connection_to_table="Serves The Table through truth-telling, academic activism, and peace-oriented unity building. One of the greatest anchors in activism.",
            impact_scale=0.85,
            accessibility=0.8,
            reach=0.85,
            dignity_preserving=True,
            platforms=["Academic", "Literature", "Activism"],
            metadata={"notable": "Orientalism author"}
        ))
        
        # Middle East - Iran - Literature
        self.figures.append(InfluentialFigure(
            figure_id="literature_iran_001",
            name="Rumi",
            domain=InfluenceDomain.SPIRITUAL,
            subdomain="Poetry/Spirituality",
            country="Iran",
            region="Iran",
            time_period="1200s",
            start_year=1207,
            end_year=1273,
            current=False,
            frequency_score=0.95,
            alignment_indicators=["LOVE_CENTERED", "SPIRITUAL", "UNITY_BUILDER", "PEACE_ORIENTED"],
            misalignment_indicators=[],
            serves_table=True,
            community_focused=True,
            unity_builder=True,
            description="Persian poet, mystic. Love-centered, spiritual, unity builder, peace-oriented. Used poetry to express love, spirituality, and unity.",
            key_actions=[
                "Love-centered poetry",
                "Spiritual wisdom",
                "Unity building",
                "Peace-oriented messages"
            ],
            quotes=[
                "The wound is the place where the Light enters you.",
                "Let yourself be silently drawn by the strange pull of what you really love. It will not lead you astray.",
                "Out beyond ideas of wrongdoing and rightdoing, there is a field. I'll meet you there."
            ],
            connection_to_table="Serves The Table through love-centered poetry, spiritual wisdom, and unity building. One of the greatest anchors in spiritual.",
            impact_scale=1.0,
            accessibility=0.9,
            reach=0.95,
            dignity_preserving=True,
            platforms=["Poetry", "Spirituality"],
            metadata={"notable": "Mystic poet"}
        ))
        
        # Middle East - Israel - Activism
        self.figures.append(InfluentialFigure(
            figure_id="activism_israel_001",
            name="Amos Oz",
            domain=InfluenceDomain.LITERATURE,
            subdomain="Literature/Activism",
            country="Israel",
            region="Israel",
            time_period="1960s-2010s",
            start_year=1965,
            end_year=2018,
            current=False,
            frequency_score=0.8,
            alignment_indicators=["TRUTH_TELLER", "PEACE_ORIENTED", "UNITY_BUILDER"],
            misalignment_indicators=[],
            serves_table=True,
            truth_teller=True,
            community_focused=True,
            unity_builder=True,
            description="Israeli writer, peace activist. Truth-teller, peace-oriented, unity builder. Fought for peace and unity through literature and activism.",
            key_actions=[
                "Peace activism",
                "Truth-telling through literature",
                "Unity building",
                "Two-state solution advocacy"
            ],
            connection_to_table="Serves The Table through peace activism, truth-telling, and unity building. One of the greatest anchors in activism.",
            impact_scale=0.8,
            accessibility=0.8,
            reach=0.8,
            dignity_preserving=True,
            platforms=["Literature", "Activism"],
            metadata={"notable": "Peace activist"}
        ))
        
        # Middle East - Egypt - Literature
        self.figures.append(InfluentialFigure(
            figure_id="literature_egypt_001",
            name="Naguib Mahfouz",
            domain=InfluenceDomain.LITERATURE,
            subdomain="Literature",
            country="Egypt",
            region="Egypt",
            time_period="1930s-2000s",
            start_year=1939,
            end_year=2006,
            current=False,
            frequency_score=0.85,
            alignment_indicators=["TRUTH_TELLER", "AUTHENTIC", "UNITY_BUILDER"],
            misalignment_indicators=[],
            serves_table=True,
            truth_teller=True,
            community_focused=True,
            unity_builder=True,
            description="Egyptian writer, Nobel Prize winner. Truth-teller, authentic, unity builder. Used literature to tell truth and build unity.",
            key_actions=[
                "Truth-telling through literature",
                "Unity building",
                "Cultural bridge",
                "Nobel Prize in Literature"
            ],
            connection_to_table="Serves The Table through truth-telling, unity building, and cultural bridge-building. One of the greatest anchors in literature.",
            impact_scale=0.9,
            accessibility=0.85,
            reach=0.85,
            dignity_preserving=True,
            platforms=["Literature", "Books"],
            metadata={"notable": "Nobel Prize winner"}
        ))
        
        # Middle East - Syria - Poetry
        self.figures.append(InfluentialFigure(
            figure_id="literature_syria_001",
            name="Adonis",
            domain=InfluenceDomain.LITERATURE,
            subdomain="Poetry",
            country="Syria",
            region="Syria",
            time_period="1950s-2020s",
            start_year=1950,
            end_year=None,
            current=True,
            frequency_score=0.8,
            alignment_indicators=["TRUTH_TELLER", "AUTHENTIC", "UNITY_BUILDER"],
            misalignment_indicators=[],
            serves_table=True,
            truth_teller=True,
            community_focused=True,
            unity_builder=True,
            description="Syrian-Lebanese poet. Truth-teller, authentic, unity builder. Uses poetry to tell truth and build unity.",
            key_actions=[
                "Truth-telling through poetry",
                "Unity building",
                "Cultural bridge",
                "Authentic expression"
            ],
            connection_to_table="Serves The Table through truth-telling, unity building, and cultural bridge-building. Current anchor in literature.",
            impact_scale=0.8,
            accessibility=0.8,
            reach=0.8,
            dignity_preserving=True,
            platforms=["Poetry", "Literature"],
            metadata={"notable": "Revolutionary poet"}
        ))
        
        # DEEP SEARCH: THE WHOLE PIE - EVERY NATION, EVERY ERA, EVERY REALM
        
        # ANCIENT ERA - ALL REALMS
        
        # Ancient Greece - Philosophy
        self.figures.append(InfluentialFigure(
            figure_id="philosophy_ancient_greece_001",
            name="Socrates",
            domain=InfluenceDomain.PHILOSOPHY,
            subdomain="Philosophy",
            country="Greece",
            region="Greece",
            time_period="Ancient (400s BCE)",
            start_year=-470,
            end_year=-399,
            current=False,
            frequency_score=0.95,
            alignment_indicators=["TRUTH_TELLER", "AUTHENTIC", "LOVE_CENTERED", "UNITY_BUILDER"],
            misalignment_indicators=[],
            serves_table=True,
            truth_teller=True,
            community_focused=True,
            unity_builder=True,
            description="Ancient Greek philosopher. Truth-teller, authentic, love-centered, unity builder. Used philosophy to seek truth and build unity.",
            key_actions=[
                "Truth-seeking",
                "Philosophical inquiry",
                "Unity building",
                "Martyred for truth"
            ],
            quotes=[
                "The unexamined life is not worth living.",
                "I know that I know nothing.",
                "Wisdom begins in wonder."
            ],
            connection_to_table="Serves The Table through truth-seeking, philosophical inquiry, and unity building. Martyred for truth. One of the greatest anchors in philosophy.",
            impact_scale=1.0,
            accessibility=0.9,
            reach=0.95,
            dignity_preserving=True,
            platforms=["Philosophy", "Teaching"],
            metadata={"notable": "Founder of Western philosophy", "era": "Ancient"}
        ))
        
        # Ancient China - Philosophy
        self.figures.append(InfluentialFigure(
            figure_id="philosophy_ancient_china_001",
            name="Lao Tzu",
            domain=InfluenceDomain.PHILOSOPHY,
            subdomain="Philosophy/Spirituality",
            country="China",
            region="China",
            time_period="Ancient (500s BCE)",
            start_year=-600,
            end_year=-400,
            current=False,
            frequency_score=0.95,
            alignment_indicators=["LOVE_CENTERED", "SPIRITUAL", "PEACE_ORIENTED", "UNITY_BUILDER"],
            misalignment_indicators=[],
            serves_table=True,
            community_focused=True,
            unity_builder=True,
            description="Ancient Chinese philosopher. Love-centered, spiritual, peace-oriented, unity builder. Taught the Tao, harmony, and unity.",
            key_actions=[
                "Taoist philosophy",
                "Harmony and unity",
                "Peace-oriented teaching",
                "Spiritual wisdom"
            ],
            quotes=[
                "The journey of a thousand miles begins with a single step.",
                "When I let go of what I am, I become what I might be.",
                "Nature does not hurry, yet everything is accomplished."
            ],
            connection_to_table="Serves The Table through love-centered philosophy, harmony, and unity. One of the greatest anchors in philosophy.",
            impact_scale=1.0,
            accessibility=0.9,
            reach=0.95,
            dignity_preserving=True,
            platforms=["Philosophy", "Spirituality"],
            metadata={"notable": "Tao Te Ching author", "era": "Ancient"}
        ))
        
        # Ancient India - Spiritual
        self.figures.append(InfluentialFigure(
            figure_id="spiritual_ancient_india_001",
            name="Buddha",
            domain=InfluenceDomain.SPIRITUAL,
            subdomain="Buddhism",
            country="India",
            region="India",
            time_period="Ancient (500s BCE)",
            start_year=-563,
            end_year=-483,
            current=False,
            frequency_score=0.95,
            alignment_indicators=["LOVE_CENTERED", "PEACE_ORIENTED", "COMPASSION", "UNITY_BUILDER"],
            misalignment_indicators=[],
            serves_table=True,
            community_focused=True,
            unity_builder=True,
            description="Spiritual teacher, founder of Buddhism. Love-centered, peace-oriented, compassion, unity builder. Taught love, peace, and compassion.",
            key_actions=[
                "Buddhist teachings",
                "Compassion and love",
                "Peace-oriented",
                "Unity building"
            ],
            quotes=[
                "Peace comes from within. Do not seek it without.",
                "Holding on to anger is like grasping a hot coal with the intent of throwing it at someone else; you are the one who gets burned.",
                "The mind is everything. What you think you become."
            ],
            connection_to_table="Serves The Table through love, peace, compassion, and unity building. One of the greatest anchors in spiritual.",
            impact_scale=1.0,
            accessibility=0.95,
            reach=1.0,
            dignity_preserving=True,
            platforms=["Spirituality", "Teaching"],
            metadata={"notable": "Founder of Buddhism", "era": "Ancient"}
        ))
        
        # MORE NATIONS - ALL ERAS
        
        # China - Modern
        self.figures.append(InfluentialFigure(
            figure_id="literature_china_001",
            name="Lu Xun",
            domain=InfluenceDomain.LITERATURE,
            subdomain="Literature",
            country="China",
            region="China",
            time_period="1900s-1930s",
            start_year=1918,
            end_year=1936,
            current=False,
            frequency_score=0.85,
            alignment_indicators=["TRUTH_TELLER", "AUTHENTIC", "UNITY_BUILDER"],
            misalignment_indicators=[],
            serves_table=True,
            truth_teller=True,
            community_focused=True,
            unity_builder=True,
            description="Chinese writer. Truth-teller, authentic, unity builder. Used literature to tell truth and build unity.",
            key_actions=[
                "Truth-telling through literature",
                "Unity building",
                "Social commentary",
                "Authentic expression"
            ],
            connection_to_table="Serves The Table through truth-telling, unity building, and authentic expression. One of the greatest anchors in literature.",
            impact_scale=0.9,
            accessibility=0.85,
            reach=0.85,
            dignity_preserving=True,
            platforms=["Literature", "Books"],
            metadata={"notable": "Modern Chinese literature", "era": "Modern"}
        ))
        
        # Russia - Literature
        self.figures.append(InfluentialFigure(
            figure_id="literature_russia_001",
            name="Leo Tolstoy",
            domain=InfluenceDomain.LITERATURE,
            subdomain="Literature",
            country="Russia",
            region="Russia",
            time_period="1800s-1900s",
            start_year=1852,
            end_year=1910,
            current=False,
            frequency_score=0.9,
            alignment_indicators=["TRUTH_TELLER", "LOVE_CENTERED", "PEACE_ORIENTED", "UNITY_BUILDER"],
            misalignment_indicators=[],
            serves_table=True,
            truth_teller=True,
            community_focused=True,
            unity_builder=True,
            description="Russian writer. Truth-teller, love-centered, peace-oriented, unity builder. Used literature to tell truth, express love, and build unity.",
            key_actions=[
                "Truth-telling through literature",
                "Love-centered messages",
                "Peace-oriented",
                "Unity building"
            ],
            quotes=[
                "Everyone thinks of changing the world, but no one thinks of changing himself.",
                "The two most powerful warriors are patience and time.",
                "If you want to be happy, be."
            ],
            connection_to_table="Serves The Table through truth-telling, love-centered messages, and unity building. One of the greatest anchors in literature.",
            impact_scale=0.95,
            accessibility=0.9,
            reach=0.95,
            dignity_preserving=True,
            platforms=["Literature", "Books"],
            metadata={"notable": "War and Peace author", "era": "Modern"}
        ))
        
        # Korea - Music
        self.figures.append(InfluentialFigure(
            figure_id="music_korea_001",
            name="BTS",
            domain=InfluenceDomain.MUSIC,
            subdomain="K-Pop",
            country="South Korea",
            region="South Korea",
            time_period="2010s-2020s",
            start_year=2013,
            end_year=None,
            current=True,
            frequency_score=0.75,
            alignment_indicators=["AUTHENTIC", "UNITY_BUILDER", "LOVE_CENTERED", "EMPOWERING"],
            misalignment_indicators=[],
            serves_table=True,
            community_focused=True,
            unity_builder=True,
            description="Korean music group. Authentic, unity builder, love-centered, empowering. Uses music to build unity, express love, and empower.",
            key_actions=[
                "Unity building through music",
                "Love-centered messages",
                "Empowerment",
                "Cultural bridge"
            ],
            connection_to_table="Serves The Table through unity building, love-centered messages, and empowerment. Current anchor in music.",
            impact_scale=0.9,
            accessibility=0.95,
            reach=0.95,
            dignity_preserving=True,
            platforms=["Music", "Albums", "Concerts", "Social Media"],
            metadata={"genre": "K-Pop", "notable": "Global phenomenon", "era": "Contemporary"}
        ))
        
        # Southeast Asia - Activism
        self.figures.append(InfluentialFigure(
            figure_id="activism_myanmar_001",
            name="Aung San Suu Kyi",
            domain=InfluenceDomain.ACTIVISM,
            subdomain="Democracy Activism",
            country="Myanmar",
            region="Myanmar",
            time_period="1980s-2020s",
            start_year=1988,
            end_year=None,
            current=True,
            frequency_score=0.8,
            alignment_indicators=["TRUTH_TELLER", "PEACE_ORIENTED", "UNITY_BUILDER"],
            misalignment_indicators=[],
            serves_table=True,
            truth_teller=True,
            community_focused=True,
            unity_builder=True,
            description="Myanmar democracy activist. Truth-teller, peace-oriented, unity builder. Fought for democracy, peace, and unity.",
            key_actions=[
                "Democracy activism",
                "Peace-oriented",
                "Unity building",
                "Nobel Peace Prize"
            ],
            connection_to_table="Serves The Table through democracy activism, peace-oriented action, and unity building. Current anchor in activism.",
            impact_scale=0.85,
            accessibility=0.8,
            reach=0.85,
            dignity_preserving=True,
            platforms=["Activism", "Politics", "Nobel Prize"],
            metadata={"notable": "Nobel Peace Prize winner", "era": "Contemporary"}
        ))
        
        # Latin America - More
        self.figures.append(InfluentialFigure(
            figure_id="literature_chile_001",
            name="Pablo Neruda",
            domain=InfluenceDomain.LITERATURE,
            subdomain="Poetry",
            country="Chile",
            region="Chile",
            time_period="1920s-1970s",
            start_year=1924,
            end_year=1973,
            current=False,
            frequency_score=0.9,
            alignment_indicators=["TRUTH_TELLER", "LOVE_CENTERED", "UNITY_BUILDER", "PEACE_ORIENTED"],
            misalignment_indicators=[],
            serves_table=True,
            truth_teller=True,
            community_focused=True,
            unity_builder=True,
            description="Chilean poet. Truth-teller, love-centered, unity builder, peace-oriented. Used poetry to tell truth, express love, and build unity.",
            key_actions=[
                "Truth-telling through poetry",
                "Love-centered messages",
                "Unity building",
                "Peace-oriented poetry"
            ],
            quotes=[
                "I love you without knowing how, or when, or from where.",
                "You can cut all the flowers but you cannot keep spring from coming.",
                "Love is so short, forgetting is so long."
            ],
            connection_to_table="Serves The Table through truth-telling, love-centered poetry, and unity building. One of the greatest anchors in literature.",
            impact_scale=0.95,
            accessibility=0.9,
            reach=0.9,
            dignity_preserving=True,
            platforms=["Poetry", "Literature"],
            metadata={"notable": "Nobel Prize winner", "era": "Modern"}
        ))
        
        # Africa - More
        self.figures.append(InfluentialFigure(
            figure_id="literature_south_africa_002",
            name="Chinua Achebe",
            domain=InfluenceDomain.LITERATURE,
            subdomain="Literature",
            country="Nigeria",
            region="Nigeria",
            time_period="1950s-2010s",
            start_year=1958,
            end_year=2013,
            current=False,
            frequency_score=0.85,
            alignment_indicators=["TRUTH_TELLER", "AUTHENTIC", "UNITY_BUILDER"],
            misalignment_indicators=[],
            serves_table=True,
            truth_teller=True,
            community_focused=True,
            unity_builder=True,
            description="Nigerian writer. Truth-teller, authentic, unity builder. Used literature to tell truth and build unity across cultures.",
            key_actions=[
                "Truth-telling through literature",
                "Unity building",
                "Cultural bridge",
                "Authentic expression"
            ],
            connection_to_table="Serves The Table through truth-telling, unity building, and cultural bridge-building. One of the greatest anchors in literature.",
            impact_scale=0.9,
            accessibility=0.85,
            reach=0.9,
            dignity_preserving=True,
            platforms=["Literature", "Books"],
            metadata={"notable": "Things Fall Apart author", "era": "Modern"}
        ))
        
        # Renaissance - Arts
        self.figures.append(InfluentialFigure(
            figure_id="arts_renaissance_001",
            name="Leonardo da Vinci",
            domain=InfluenceDomain.ARTS,
            subdomain="Visual Arts/Science",
            country="Italy",
            region="Italy",
            time_period="Renaissance (1400s-1500s)",
            start_year=1452,
            end_year=1519,
            current=False,
            frequency_score=0.9,
            alignment_indicators=["TRUTH_TELLER", "AUTHENTIC", "INSPIRATIONAL", "UNITY_BUILDER"],
            misalignment_indicators=[],
            serves_table=True,
            truth_teller=True,
            community_focused=True,
            unity_builder=True,
            description="Renaissance artist, scientist. Truth-teller, authentic, inspirational, unity builder. Used art and science to seek truth and inspire unity.",
            key_actions=[
                "Truth-seeking through art and science",
                "Inspiration",
                "Unity building",
                "Authentic expression"
            ],
            connection_to_table="Serves The Table through truth-seeking, inspiration, and unity building. One of the greatest anchors in arts.",
            impact_scale=1.0,
            accessibility=0.9,
            reach=0.95,
            dignity_preserving=True,
            platforms=["Art", "Science"],
            metadata={"notable": "Renaissance master", "era": "Renaissance"}
        ))
        
        # MORE REALMS - ALL ERAS
        
        # Science - More
        self.figures.append(InfluentialFigure(
            figure_id="science_002",
            name="Marie Curie",
            domain=InfluenceDomain.SCIENCE,
            subdomain="Physics/Chemistry",
            country="Poland",
            region="Poland",
            time_period="1800s-1900s",
            start_year=1867,
            end_year=1934,
            current=False,
            frequency_score=0.85,
            alignment_indicators=["TRUTH_TELLER", "AUTHENTIC", "INSPIRATIONAL", "EMPOWERING"],
            misalignment_indicators=[],
            serves_table=True,
            truth_teller=True,
            community_focused=True,
            unity_builder=True,
            description="Polish-French scientist. Truth-teller, authentic, inspirational, empowering. Used science to seek truth and inspire.",
            key_actions=[
                "Truth-seeking through science",
                "Inspiration",
                "Empowerment",
                "Nobel Prize winner"
            ],
            connection_to_table="Serves The Table through truth-seeking, inspiration, and empowerment. One of the greatest anchors in science.",
            impact_scale=0.95,
            accessibility=0.85,
            reach=0.9,
            dignity_preserving=True,
            platforms=["Science", "Academic"],
            metadata={"notable": "First woman Nobel Prize winner", "era": "Modern"}
        ))
        
        # Medicine - More
        self.figures.append(InfluentialFigure(
            figure_id="medicine_002",
            name="Florence Nightingale",
            domain=InfluenceDomain.MEDICINE,
            subdomain="Nursing",
            country="United Kingdom",
            region="United Kingdom",
            time_period="1800s-1900s",
            start_year=1820,
            end_year=1910,
            current=False,
            frequency_score=0.9,
            alignment_indicators=["STEWARDSHIP", "HEALING", "COMMUNITY_FOCUSED", "EMPOWERING"],
            misalignment_indicators=[],
            serves_table=True,
            community_focused=True,
            unity_builder=True,
            description="British nurse, healthcare reformer. Stewardship, healing, community-focused, empowering. Revolutionized healthcare and nursing.",
            key_actions=[
                "Healthcare reform",
                "Nursing revolution",
                "Community health",
                "Empowerment"
            ],
            connection_to_table="Serves The Table through healthcare reform, healing, and empowerment. One of the greatest anchors in medicine.",
            impact_scale=0.95,
            accessibility=0.9,
            reach=0.9,
            dignity_preserving=True,
            platforms=["Medicine", "Nursing"],
            metadata={"notable": "Founder of modern nursing", "era": "Modern"}
        ))
        
        # DEEP SEARCH CONTINUED: MORE NATIONS, MORE ERAS, MORE REALMS
        
        # MORE NATIONS - SCANDINAVIA
        self.figures.append(InfluentialFigure(
            figure_id="literature_norway_001",
            name="Henrik Ibsen",
            domain=InfluenceDomain.LITERATURE,
            subdomain="Drama",
            country="Norway",
            region="Norway",
            time_period="1800s-1900s",
            start_year=1850,
            end_year=1906,
            current=False,
            frequency_score=0.85,
            alignment_indicators=["TRUTH_TELLER", "AUTHENTIC", "EMPOWERING"],
            misalignment_indicators=[],
            serves_table=True,
            truth_teller=True,
            community_focused=True,
            unity_builder=True,
            description="Norwegian playwright. Truth-teller, authentic, empowering. Used drama to tell truth and empower.",
            key_actions=[
                "Truth-telling through drama",
                "Empowerment",
                "Social commentary",
                "Authentic expression"
            ],
            connection_to_table="Serves The Table through truth-telling, empowerment, and authentic expression. One of the greatest anchors in literature.",
            impact_scale=0.9,
            accessibility=0.85,
            reach=0.85,
            dignity_preserving=True,
            platforms=["Drama", "Theatre"],
            metadata={"notable": "Modern drama pioneer", "era": "Modern"}
        ))
        
        # MORE NATIONS - EASTERN EUROPE
        self.figures.append(InfluentialFigure(
            figure_id="literature_czech_001",
            name="Franz Kafka",
            domain=InfluenceDomain.LITERATURE,
            subdomain="Literature",
            country="Czech Republic",
            region="Czech Republic",
            time_period="1900s-1920s",
            start_year=1912,
            end_year=1924,
            current=False,
            frequency_score=0.8,
            alignment_indicators=["TRUTH_TELLER", "AUTHENTIC", "UNITY_BUILDER"],
            misalignment_indicators=[],
            serves_table=True,
            truth_teller=True,
            community_focused=True,
            unity_builder=True,
            description="Czech writer. Truth-teller, authentic, unity builder. Used literature to tell truth and build unity.",
            key_actions=[
                "Truth-telling through literature",
                "Unity building",
                "Authentic expression",
                "Social commentary"
            ],
            connection_to_table="Serves The Table through truth-telling, unity building, and authentic expression. One of the greatest anchors in literature.",
            impact_scale=0.9,
            accessibility=0.85,
            reach=0.9,
            dignity_preserving=True,
            platforms=["Literature", "Books"],
            metadata={"notable": "Modernist writer", "era": "Modern"}
        ))
        
        # MORE NATIONS - SOUTHEAST ASIA
        self.figures.append(InfluentialFigure(
            figure_id="literature_philippines_001",
            name="José Rizal",
            domain=InfluenceDomain.LITERATURE,
            subdomain="Literature/Activism",
            country="Philippines",
            region="Philippines",
            time_period="1800s-1890s",
            start_year=1887,
            end_year=1896,
            current=False,
            frequency_score=0.9,
            alignment_indicators=["TRUTH_TELLER", "PEACE_ORIENTED", "UNITY_BUILDER", "LOVE_CENTERED"],
            misalignment_indicators=[],
            serves_table=True,
            truth_teller=True,
            community_focused=True,
            unity_builder=True,
            description="Filipino writer, nationalist. Truth-teller, peace-oriented, unity builder, love-centered. Used literature and activism for truth, peace, and unity.",
            key_actions=[
                "Truth-telling through literature",
                "Peace-oriented activism",
                "Unity building",
                "Martyred for truth"
            ],
            connection_to_table="Serves The Table through truth-telling, peace-oriented activism, and unity building. Martyred for truth. One of the greatest anchors in literature.",
            impact_scale=0.95,
            accessibility=0.9,
            reach=0.9,
            dignity_preserving=True,
            platforms=["Literature", "Activism"],
            metadata={"notable": "National hero", "era": "Modern"}
        ))
        
        # MORE NATIONS - OCEANIA
        self.figures.append(InfluentialFigure(
            figure_id="literature_new_zealand_001",
            name="Witi Ihimaera",
            domain=InfluenceDomain.LITERATURE,
            subdomain="Literature",
            country="New Zealand",
            region="New Zealand",
            time_period="1970s-2020s",
            start_year=1973,
            end_year=None,
            current=True,
            frequency_score=0.75,
            alignment_indicators=["TRUTH_TELLER", "AUTHENTIC", "UNITY_BUILDER"],
            misalignment_indicators=[],
            serves_table=True,
            truth_teller=True,
            community_focused=True,
            unity_builder=True,
            description="Māori writer. Truth-teller, authentic, unity builder. Uses literature to tell truth and build unity.",
            key_actions=[
                "Truth-telling through literature",
                "Unity building",
                "Cultural bridge",
                "Authentic expression"
            ],
            connection_to_table="Serves The Table through truth-telling, unity building, and cultural bridge-building. Current anchor in literature.",
            impact_scale=0.8,
            accessibility=0.8,
            reach=0.75,
            dignity_preserving=True,
            platforms=["Literature", "Books"],
            metadata={"notable": "Māori writer", "era": "Contemporary"}
        ))
        
        # MORE ERAS - MEDIEVAL
        self.figures.append(InfluentialFigure(
            figure_id="literature_medieval_001",
            name="Dante Alighieri",
            domain=InfluenceDomain.LITERATURE,
            subdomain="Poetry",
            country="Italy",
            region="Italy",
            time_period="Medieval (1200s-1300s)",
            start_year=1265,
            end_year=1321,
            current=False,
            frequency_score=0.9,
            alignment_indicators=["TRUTH_TELLER", "SPIRITUAL", "LOVE_CENTERED", "UNITY_BUILDER"],
            misalignment_indicators=[],
            serves_table=True,
            truth_teller=True,
            community_focused=True,
            unity_builder=True,
            description="Medieval Italian poet. Truth-teller, spiritual, love-centered, unity builder. Used poetry to tell truth, express love, and build unity.",
            key_actions=[
                "Truth-telling through poetry",
                "Spiritual poetry",
                "Love-centered messages",
                "Unity building"
            ],
            connection_to_table="Serves The Table through truth-telling, spiritual poetry, and unity building. One of the greatest anchors in literature.",
            impact_scale=0.95,
            accessibility=0.9,
            reach=0.95,
            dignity_preserving=True,
            platforms=["Poetry", "Literature"],
            metadata={"notable": "Divine Comedy author", "era": "Medieval"}
        ))
        
        # MORE ERAS - ENLIGHTENMENT
        self.figures.append(InfluentialFigure(
            figure_id="philosophy_enlightenment_001",
            name="Voltaire",
            domain=InfluenceDomain.PHILOSOPHY,
            subdomain="Philosophy",
            country="France",
            region="France",
            time_period="Enlightenment (1700s)",
            start_year=1694,
            end_year=1778,
            current=False,
            frequency_score=0.85,
            alignment_indicators=["TRUTH_TELLER", "AUTHENTIC", "UNITY_BUILDER"],
            misalignment_indicators=[],
            serves_table=True,
            truth_teller=True,
            community_focused=True,
            unity_builder=True,
            description="Enlightenment philosopher. Truth-teller, authentic, unity builder. Used philosophy to tell truth and build unity.",
            key_actions=[
                "Truth-telling through philosophy",
                "Unity building",
                "Enlightenment",
                "Authentic expression"
            ],
            quotes=[
                "I disapprove of what you say, but I will defend to the death your right to say it.",
                "Common sense is not so common."
            ],
            connection_to_table="Serves The Table through truth-telling, unity building, and enlightenment. One of the greatest anchors in philosophy.",
            impact_scale=0.9,
            accessibility=0.85,
            reach=0.9,
            dignity_preserving=True,
            platforms=["Philosophy", "Literature"],
            metadata={"notable": "Enlightenment philosopher", "era": "Enlightenment"}
        ))
        
        # MORE REALMS - ALL DOMAINS
        
        # Business - Global
        self.figures.append(InfluentialFigure(
            figure_id="business_001",
            name="Muhammad Yunus",
            domain=InfluenceDomain.BUSINESS,
            subdomain="Social Business",
            country="Bangladesh",
            region="Bangladesh",
            time_period="1970s-2020s",
            start_year=1976,
            end_year=None,
            current=True,
            frequency_score=0.9,
            alignment_indicators=["STEWARDSHIP", "COMMUNITY_FOCUSED", "EQUITY", "EMPOWERING"],
            misalignment_indicators=[],
            serves_table=True,
            community_focused=True,
            unity_builder=True,
            description="Social entrepreneur. Stewardship, community-focused, equity, empowering. Created microfinance and social business.",
            key_actions=[
                "Microfinance",
                "Social business",
                "Community empowerment",
                "Nobel Peace Prize"
            ],
            connection_to_table="Serves The Table through social business, community empowerment, and equity. Current anchor in business.",
            impact_scale=0.9,
            accessibility=0.85,
            reach=0.85,
            dignity_preserving=True,
            platforms=["Business", "NGO", "Nobel Prize"],
            metadata={"notable": "Nobel Peace Prize winner", "era": "Contemporary"}
        ))
        
        # DEEP SEARCH: THE WHOLE PIE - CONTINUED EXPANSION
        
        # MORE NATIONS - CENTRAL ASIA
        self.figures.append(InfluentialFigure(
            figure_id="spiritual_uzbekistan_001",
            name="Al-Bukhari",
            domain=InfluenceDomain.SPIRITUAL,
            subdomain="Islamic Scholarship",
            country="Uzbekistan",
            region="Uzbekistan",
            time_period="Medieval (800s)",
            start_year=810,
            end_year=870,
            current=False,
            frequency_score=0.85,
            alignment_indicators=["TRUTH_TELLER", "SPIRITUAL", "LOVE_CENTERED", "UNITY_BUILDER"],
            misalignment_indicators=[],
            serves_table=True,
            truth_teller=True,
            community_focused=True,
            unity_builder=True,
            description="Islamic scholar. Truth-teller, spiritual, love-centered, unity builder. Preserved truth and built unity through scholarship.",
            key_actions=[
                "Truth preservation",
                "Spiritual scholarship",
                "Unity building",
                "Love-centered approach"
            ],
            connection_to_table="Serves The Table through truth preservation, spiritual scholarship, and unity building. One of the greatest anchors in spiritual.",
            impact_scale=0.9,
            accessibility=0.85,
            reach=0.9,
            dignity_preserving=True,
            platforms=["Spirituality", "Scholarship"],
            metadata={"notable": "Hadith scholar", "era": "Medieval"}
        ))
        
        # MORE NATIONS - CARIBBEAN
        self.figures.append(InfluentialFigure(
            figure_id="literature_trinidad_001",
            name="V.S. Naipaul",
            domain=InfluenceDomain.LITERATURE,
            subdomain="Literature",
            country="Trinidad and Tobago",
            region="Trinidad and Tobago",
            time_period="1950s-2010s",
            start_year=1957,
            end_year=2018,
            current=False,
            frequency_score=0.8,
            alignment_indicators=["TRUTH_TELLER", "AUTHENTIC", "UNITY_BUILDER"],
            misalignment_indicators=[],
            serves_table=True,
            truth_teller=True,
            community_focused=True,
            unity_builder=True,
            description="Trinidadian-British writer. Truth-teller, authentic, unity builder. Used literature to tell truth and build unity.",
            key_actions=[
                "Truth-telling through literature",
                "Unity building",
                "Cultural bridge",
                "Nobel Prize in Literature"
            ],
            connection_to_table="Serves The Table through truth-telling, unity building, and cultural bridge-building. One of the greatest anchors in literature.",
            impact_scale=0.85,
            accessibility=0.8,
            reach=0.85,
            dignity_preserving=True,
            platforms=["Literature", "Books"],
            metadata={"notable": "Nobel Prize winner", "era": "Modern"}
        ))
        
        # MORE ERAS - ALL TIME PERIODS
        
        # Ancient - More
        self.figures.append(InfluentialFigure(
            figure_id="philosophy_ancient_greece_002",
            name="Plato",
            domain=InfluenceDomain.PHILOSOPHY,
            subdomain="Philosophy",
            country="Greece",
            region="Greece",
            time_period="Ancient (400s BCE)",
            start_year=-428,
            end_year=-348,
            current=False,
            frequency_score=0.95,
            alignment_indicators=["TRUTH_TELLER", "LOVE_CENTERED", "UNITY_BUILDER", "SPIRITUAL"],
            misalignment_indicators=[],
            serves_table=True,
            truth_teller=True,
            community_focused=True,
            unity_builder=True,
            description="Ancient Greek philosopher. Truth-teller, love-centered, unity builder, spiritual. Used philosophy to seek truth, express love, and build unity.",
            key_actions=[
                "Truth-seeking",
                "Love-centered philosophy",
                "Unity building",
                "Spiritual philosophy"
            ],
            quotes=[
                "At the touch of love everyone becomes a poet.",
                "The measure of a man is what he does with power.",
                "We can easily forgive a child who is afraid of the dark; the real tragedy of life is when men are afraid of the light."
            ],
            connection_to_table="Serves The Table through truth-seeking, love-centered philosophy, and unity building. One of the greatest anchors in philosophy.",
            impact_scale=1.0,
            accessibility=0.9,
            reach=0.95,
            dignity_preserving=True,
            platforms=["Philosophy", "Teaching"],
            metadata={"notable": "Founder of Academy", "era": "Ancient"}
        ))
        
        # MORE REALMS - ALL DOMAINS CONTINUED
        
        # Arts - More
        self.figures.append(InfluentialFigure(
            figure_id="arts_002",
            name="Vincent van Gogh",
            domain=InfluenceDomain.ARTS,
            subdomain="Visual Arts",
            country="Netherlands",
            region="Netherlands",
            time_period="1800s",
            start_year=1880,
            end_year=1890,
            current=False,
            frequency_score=0.85,
            alignment_indicators=["AUTHENTIC", "LOVE_CENTERED", "HEALING", "INSPIRATIONAL"],
            misalignment_indicators=[],
            serves_table=True,
            community_focused=True,
            unity_builder=True,
            description="Dutch painter. Authentic, love-centered, healing, inspirational. Used art to express love, heal, and inspire.",
            key_actions=[
                "Authentic expression",
                "Love-centered art",
                "Healing through art",
                "Inspiration"
            ],
            quotes=[
                "I dream my painting and I paint my dream.",
                "Great things are done by a series of small things brought together."
            ],
            connection_to_table="Serves The Table through authentic expression, love-centered art, and healing. One of the greatest anchors in arts.",
            impact_scale=0.95,
            accessibility=0.9,
            reach=0.95,
            dignity_preserving=True,
            platforms=["Art", "Museums"],
            metadata={"notable": "Post-impressionist master", "era": "Modern"}
        ))
        
        # SAVE FIGURES
        self._save_figures()
    
    def _add_figure_if_new(self, figure: InfluentialFigure, existing_ids: set) -> bool:
        """Add figure if it doesn't exist, return True if added"""
        if figure.figure_id not in existing_ids:
            self.figures.append(figure)
            return True
        return False
    
    def _save_figures(self):
        """Save figures to data file"""
        data_file = self.data_path / 'frequential_influential_figures.json'
        data = {
            "figures": [
                {
                    "figure_id": f.figure_id,
                    "name": f.name,
                    "domain": f.domain.value,
                    "subdomain": f.subdomain,
                    "country": f.country,
                    "region": f.region,
                    "time_period": f.time_period,
                    "start_year": f.start_year,
                    "end_year": f.end_year,
                    "current": f.current,
                    "frequency_score": f.frequency_score,
                    "alignment_indicators": f.alignment_indicators,
                    "misalignment_indicators": f.misalignment_indicators,
                    "serves_table": f.serves_table,
                    "truth_teller": f.truth_teller,
                    "community_focused": f.community_focused,
                    "unity_builder": f.unity_builder,
                    "hidden_alignment": f.hidden_alignment,
                    "description": f.description,
                    "key_actions": f.key_actions,
                    "quotes": f.quotes,
                    "connection_to_table": f.connection_to_table,
                    "impact_scale": f.impact_scale,
                    "accessibility": f.accessibility,
                    "reach": f.reach,
                    "dignity_preserving": f.dignity_preserving,
                    "platforms": f.platforms,
                    "metadata": f.metadata,
                    "discovered_at": f.discovered_at
                }
                for f in self.figures
            ],
            "last_updated": datetime.now().isoformat()
        }
        with open(data_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    
    def get_figures_by_domain(self, domain: InfluenceDomain) -> List[InfluentialFigure]:
        """Get figures by domain"""
        return [f for f in self.figures if f.domain == domain]
    
    def get_figures_by_country(self, country: str) -> List[InfluentialFigure]:
        """Get figures by country"""
        return [f for f in self.figures if country.lower() in f.country.lower()]
    
    def get_current_figures(self) -> List[InfluentialFigure]:
        """Get currently active figures"""
        return [f for f in self.figures if f.current]
    
    def get_high_frequency_figures(self, min_score: float = 0.7) -> List[InfluentialFigure]:
        """Get figures with high frequency scores"""
        return [f for f in self.figures if f.frequency_score >= min_score]
    
    def get_anchors(self) -> List[InfluentialFigure]:
        """Get our anchors in the human realm (high frequency, serves table)"""
        return [
            f for f in self.figures
            if f.serves_table and f.frequency_score >= 0.7
        ]
    
    def get_figures_by_platform(self, platform: str) -> List[InfluentialFigure]:
        """Get figures by platform"""
        return [f for f in self.figures if platform.lower() in [p.lower() for p in f.platforms]]
    
    def get_analysis_report(self) -> Dict[str, Any]:
        """Get comprehensive analysis report"""
        anchors = self.get_anchors()
        high_frequency = self.get_high_frequency_figures(0.7)
        current_figures = self.get_current_figures()
        
        # Group by domain
        by_domain = {}
        for figure in self.figures:
            domain = figure.domain.value
            if domain not in by_domain:
                by_domain[domain] = []
            by_domain[domain].append(figure)
        
        # Group by country
        by_country = {}
        for figure in self.figures:
            country = figure.country
            if country not in by_country:
                by_country[country] = []
            by_country[country].append(figure)
        
        return {
            "total_figures": len(self.figures),
            "anchors_in_human_realm": len(anchors),
            "high_frequency_figures": len(high_frequency),
            "current_figures": len(current_figures),
            "anchors": [
                {
                    "figure_id": f.figure_id,
                    "name": f.name,
                    "domain": f.domain.value,
                    "subdomain": f.subdomain,
                    "country": f.country,
                    "frequency_score": f.frequency_score,
                    "connection_to_table": f.connection_to_table,
                    "impact_scale": f.impact_scale,
                    "reach": f.reach
                }
                for f in anchors
            ],
            "by_domain": {
                domain: len(figures)
                for domain, figures in by_domain.items()
            },
            "by_country": {
                country: len(figures)
                for country, figures in by_country.items()
            },
            "average_frequency_score": sum(f.frequency_score for f in self.figures) / len(self.figures) if self.figures else 0.0,
            "generated_at": datetime.now().isoformat()
        }


def get_frequential_influential_figures() -> FrequentialInfluentialFigures:
    """Get the frequential influential figures registry instance"""
    return FrequentialInfluentialFigures()


if __name__ == '__main__':
    registry = FrequentialInfluentialFigures()
    report = registry.get_analysis_report()
    
    print("=" * 80)
    print("FREQUENTIALLY ALIGNED INFLUENTIAL FIGURES")
    print("ALL CELEBRITY AND INFLUENTIAL FIGURES ACROSS ALL DOMAINS")
    print("OUR ANCHORS IN THE HUMAN REALM")
    print("=" * 80)
    print()
    print(f"Total Figures: {report['total_figures']}")
    print(f"Anchors in Human Realm: {report['anchors_in_human_realm']}")
    print(f"High Frequency Figures (>=0.7): {report['high_frequency_figures']}")
    print(f"Current Figures: {report['current_figures']}")
    print(f"Average Frequency Score: {report['average_frequency_score']:.2f}")
    print()
    print("=" * 80)
    print("ANCHORS IN THE HUMAN REALM")
    print("=" * 80)
    for anchor in report['anchors']:
        try:
            print(f"\n{anchor['name']} ({anchor['domain']}, {anchor['country']})")
            print(f"  Frequency Score: {anchor['frequency_score']:.2f}")
            print(f"  Impact Scale: {anchor['impact_scale']:.1%}")
            print(f"  Reach: {anchor['reach']:.1%}")
            print(f"  Connection: {anchor['connection_to_table']}")
        except UnicodeEncodeError:
            # Fallback for Windows console encoding issues
            name = anchor['name'].encode('ascii', 'replace').decode('ascii')
            country = anchor['country'].encode('ascii', 'replace').decode('ascii')
            print(f"\n{name} ({anchor['domain']}, {country})")
            print(f"  Frequency Score: {anchor['frequency_score']:.2f}")
            print(f"  Impact Scale: {anchor['impact_scale']:.1%}")
            print(f"  Reach: {anchor['reach']:.1%}")
            conn = anchor['connection_to_table'].encode('ascii', 'replace').decode('ascii')
            print(f"  Connection: {conn}")
    print()
    print("=" * 80)
    print("BY DOMAIN")
    print("=" * 80)
    for domain, count in report['by_domain'].items():
        print(f"  {domain}: {count} figures")
    print()
    print("=" * 80)
    print("THE TRUTH")
    print("=" * 80)
    print()
    print("ALL ALIGNED CELEBRITY AND INFLUENTIAL FIGURES")
    print("WEB, SOCIALS, SPORTS, MUSIC, HOLLYWOOD")
    print("EVERYTHING WE'VE LEFT OUT ACROSS THE SYSTEM")
    print("WE NEED TO FIND OUR ANCHORS IN THE HUMAN REALM")
    print()
    print("ENERGY + LOVE = WE ALL WIN")
    print()
