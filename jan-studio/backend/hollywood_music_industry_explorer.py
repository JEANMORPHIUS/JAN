"""
HOLLYWOOD & MUSIC INDUSTRY EXPLORER
Understanding the industries through mission lens

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

YIN-YANG PRINCIPLE:
"My love for song became pulled in my path, but we must respect 
the yin and yang that is the miracle of the universe."

Exploring Hollywood and music industry:
- How do they serve mission? (Yang - Practical)
- How does mission honor them? (Yin - Creative)
- What are the spiritual battles?
- How do we navigate with right spirits?
"""

from typing import Dict, List, Optional, Any
from dataclasses import dataclass, field
from enum import Enum
from datetime import datetime
import json
import logging

logger = logging.getLogger(__name__)


class IndustryType(Enum):
    """Types of industries"""
    HOLLYWOOD = "hollywood"  # Film, TV, entertainment
    MUSIC_INDUSTRY = "music_industry"  # Record labels, streaming, live
    LIVE_EVENTS = "live_events"  # Concerts, festivals, tours, venues
    SPORTS = "sports"  # Professional sports, leagues, broadcasting
    TV_PAY_PER_VIEW = "tv_pay_per_view"  # Cable, streaming, PPV events
    NEWS_MEDIA = "news_media"  # News organizations, journalism
    GLOBAL_ECONOMICS = "global_economics"  # Financial systems, banks, markets
    FINANCE = "finance"  # Banking, investment, currency
    SHADY_BUSINESS = "shady_business"  # Necessary but problematic industries
    ALL = "all"  # All industries


class IndustryStructure(Enum):
    """Industry power structures"""
    MAJOR_LABELS = "major_labels"  # Big 3: Universal, Sony, Warner
    INDEPENDENT = "independent"  # Indie labels, self-release
    HYBRID = "hybrid"  # Mix of major and indie
    DIY = "diy"  # Do-it-yourself, direct to fan


class SpiritualBattleType(Enum):
    """Spiritual battles in the industries"""
    GATEKEEPING = "gatekeeping"  # Industry gatekeepers blocking access
    EXPLOITATION = "exploitation"  # People exploited for profit
    SOUL_SELLING = "soul_selling"  # Compromising values for success
    CREATIVE_SUPPRESSION = "creative_suppression"  # Art/truth suppressed for profit
    COMMUNITY_DIVISION = "community_division"  # Industry divides community
    INFORMATION_CONTROL = "information_control"  # News/truth controlled
    FINANCIAL_OPPRESSION = "financial_oppression"  # Economic systems oppress
    SPORTS_EXPLOITATION = "sports_exploitation"  # Athletes exploited
    PAYWALL_DIVISION = "paywall_division"  # Content behind paywalls divides
    NARRATIVE_MANIPULATION = "narrative_manipulation"  # Stories manipulated for control
    VENUE_EXPLOITATION = "venue_exploitation"  # Venues exploit artists/fans
    TICKET_SCALPING = "ticket_scalping"  # Ticket resale exploits community
    PROMOTER_EXPLOITATION = "promoter_exploitation"  # Promoters exploit artists
    SHADY_NECESSARY = "shady_necessary"  # Shady but necessary for path


@dataclass
class IndustryAnalysis:
    """Analysis of an industry"""
    industry_type: IndustryType
    structure: IndustryStructure
    
    serves_mission: bool = False
    honors_song: bool = False
    
    spiritual_battles: List[SpiritualBattleType] = field(default_factory=list)
    right_spirits_present: bool = False
    
    gatekeepers: List[str] = field(default_factory=list)
    opportunities: List[str] = field(default_factory=list)
    
    mission_alignment_score: float = 0.0  # 0-100
    symbiosis_score: float = 0.0  # 0-100
    
    recommendations: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)


class HollywoodMusicIndustryExplorer:
    """
    Explorer for ALL Industries - The Whole Cake
    
    Analyzes industries through mission lens:
    - Music Industry
    - Hollywood
    - Sports
    - TV/Pay-Per-View
    - News Media
    - Global Economics
    - Finance
    
    Questions for all:
    - Do they serve stewardship and community?
    - Do they honor creative expression?
    - What spiritual battles exist?
    - How do we navigate with right spirits?
    """
    
    def __init__(self):
        """Initialize explorer"""
        self.industry_structures = {
            IndustryType.MUSIC_INDUSTRY: {
                IndustryStructure.MAJOR_LABELS: {
                    "description": "Big 3: Universal Music Group, Sony Music, Warner Music Group",
                    "gatekeepers": ["Record label executives", "A&R departments", "Radio programmers", "Playlist curators"],
                    "power": "High - controls distribution, marketing, radio",
                    "mission_alignment": "Low - profit-driven, not community-driven",
                    "spiritual_battles": [
                        SpiritualBattleType.GATEKEEPING,
                        SpiritualBattleType.EXPLOITATION,
                        SpiritualBattleType.CREATIVE_SUPPRESSION
                    ]
                },
                IndustryStructure.INDEPENDENT: {
                    "description": "Indie labels, smaller distribution",
                    "gatekeepers": ["Indie label owners", "Music blogs", "Tastemakers"],
                    "power": "Medium - more accessible, still gatekeepers",
                    "mission_alignment": "Medium - more artist-friendly, still profit-driven",
                    "spiritual_battles": [
                        SpiritualBattleType.GATEKEEPING
                    ]
                },
                IndustryStructure.DIY: {
                    "description": "Self-release, direct to fan, streaming platforms",
                    "gatekeepers": ["Algorithm curators", "Social media algorithms"],
                    "power": "Low - artist has more control",
                    "mission_alignment": "High - artist controls message, serves community directly",
                    "spiritual_battles": [
                        SpiritualBattleType.CREATIVE_SUPPRESSION  # Algorithm suppression
                    ]
                }
            },
            IndustryType.HOLLYWOOD: {
                IndustryStructure.MAJOR_LABELS: {
                    "description": "Major studios: Disney, Warner Bros, Universal, Sony, Paramount",
                    "gatekeepers": ["Studio executives", "Producers", "Agents", "Casting directors"],
                    "power": "Very High - controls content, distribution, careers",
                    "mission_alignment": "Low - profit-driven, formulaic content",
                    "spiritual_battles": [
                        SpiritualBattleType.GATEKEEPING,
                        SpiritualBattleType.EXPLOITATION,
                        SpiritualBattleType.SOUL_SELLING,
                        SpiritualBattleType.CREATIVE_SUPPRESSION,
                        SpiritualBattleType.COMMUNITY_DIVISION
                    ]
                },
                IndustryStructure.INDEPENDENT: {
                    "description": "Independent films, festivals, streaming originals",
                    "gatekeepers": ["Film festival programmers", "Streaming executives", "Indie producers"],
                    "power": "Medium - more creative freedom, less distribution",
                    "mission_alignment": "Medium - more diverse stories, still profit-driven",
                    "spiritual_battles": [
                        SpiritualBattleType.GATEKEEPING,
                        SpiritualBattleType.CREATIVE_SUPPRESSION
                    ]
                },
                IndustryStructure.DIY: {
                    "description": "Self-produced, YouTube, streaming, crowdfunded",
                    "gatekeepers": ["Algorithm curators", "Social media algorithms"],
                    "power": "Low - creator has more control",
                    "mission_alignment": "High - creator controls message, serves community directly",
                    "spiritual_battles": [
                        SpiritualBattleType.CREATIVE_SUPPRESSION  # Algorithm suppression
                    ]
                }
            },
            IndustryType.SPORTS: {
                IndustryStructure.MAJOR_LABELS: {
                    "description": "Major leagues: NFL, NBA, MLB, FIFA, etc. - Corporate sports",
                    "gatekeepers": ["League commissioners", "Team owners", "Sports agents", "Broadcast executives"],
                    "power": "Very High - controls athletes, broadcasting, revenue",
                    "mission_alignment": "Low - profit-driven, exploits athletes, divides communities",
                    "spiritual_battles": [
                        SpiritualBattleType.GATEKEEPING,
                        SpiritualBattleType.SPORTS_EXPLOITATION,
                        SpiritualBattleType.COMMUNITY_DIVISION,
                        SpiritualBattleType.PAYWALL_DIVISION
                    ]
                },
                IndustryStructure.INDEPENDENT: {
                    "description": "Independent leagues, local sports, community teams",
                    "gatekeepers": ["Local organizers", "Community leaders"],
                    "power": "Low - community-controlled",
                    "mission_alignment": "High - community-driven, unites people",
                    "spiritual_battles": []
                },
                IndustryStructure.DIY: {
                    "description": "Pickup games, street sports, community-organized",
                    "gatekeepers": ["None - community self-organized"],
                    "power": "None - fully community-controlled",
                    "mission_alignment": "High - pure community, no profit motive",
                    "spiritual_battles": []
                }
            },
            IndustryType.TV_PAY_PER_VIEW: {
                IndustryStructure.MAJOR_LABELS: {
                    "description": "Cable networks, streaming giants, PPV platforms",
                    "gatekeepers": ["Network executives", "Streaming executives", "Content curators"],
                    "power": "Very High - controls content distribution, pricing",
                    "mission_alignment": "Low - profit-driven, paywalls divide community",
                    "spiritual_battles": [
                        SpiritualBattleType.GATEKEEPING,
                        SpiritualBattleType.PAYWALL_DIVISION,
                        SpiritualBattleType.INFORMATION_CONTROL,
                        SpiritualBattleType.COMMUNITY_DIVISION
                    ]
                },
                IndustryStructure.INDEPENDENT: {
                    "description": "Independent streaming, community platforms",
                    "gatekeepers": ["Platform owners", "Content moderators"],
                    "power": "Medium - more accessible, still gatekeepers",
                    "mission_alignment": "Medium - can serve community if aligned",
                    "spiritual_battles": [
                        SpiritualBattleType.PAYWALL_DIVISION
                    ]
                },
                IndustryStructure.DIY: {
                    "description": "Free streaming, community broadcasts, open platforms",
                    "gatekeepers": ["Algorithm curators (minimal)"],
                    "power": "Low - creator controls distribution",
                    "mission_alignment": "High - free access, serves community",
                    "spiritual_battles": [
                        SpiritualBattleType.CREATIVE_SUPPRESSION  # Algorithm suppression
                    ]
                }
            },
            IndustryType.NEWS_MEDIA: {
                IndustryStructure.MAJOR_LABELS: {
                    "description": "Major news networks, corporate media",
                    "gatekeepers": ["Media executives", "Editors", "Owners", "Advertisers"],
                    "power": "Very High - controls information, narratives",
                    "mission_alignment": "Low - profit-driven, narrative manipulation, divides community",
                    "spiritual_battles": [
                        SpiritualBattleType.INFORMATION_CONTROL,
                        SpiritualBattleType.NARRATIVE_MANIPULATION,
                        SpiritualBattleType.COMMUNITY_DIVISION,
                        SpiritualBattleType.GATEKEEPING
                    ]
                },
                IndustryStructure.INDEPENDENT: {
                    "description": "Independent journalism, alternative media",
                    "gatekeepers": ["Independent editors", "Platform moderators"],
                    "power": "Medium - more truth-focused, still gatekeepers",
                    "mission_alignment": "Medium - can serve truth if aligned",
                    "spiritual_battles": [
                        SpiritualBattleType.INFORMATION_CONTROL,
                        SpiritualBattleType.GATEKEEPING
                    ]
                },
                IndustryStructure.DIY: {
                    "description": "Citizen journalism, community news, open platforms",
                    "gatekeepers": ["Algorithm curators (minimal)"],
                    "power": "Low - truth-teller controls message",
                    "mission_alignment": "High - truth serves community directly",
                    "spiritual_battles": [
                        SpiritualBattleType.CREATIVE_SUPPRESSION  # Algorithm suppression
                    ]
                }
            },
            IndustryType.GLOBAL_ECONOMICS: {
                IndustryStructure.MAJOR_LABELS: {
                    "description": "Central banks, IMF, World Bank, multinational corporations",
                    "gatekeepers": ["Central bankers", "IMF/World Bank executives", "Corporate CEOs"],
                    "power": "Absolute - controls global money, resources, economies",
                    "mission_alignment": "Very Low - profit-driven, oppresses communities, divides world",
                    "spiritual_battles": [
                        SpiritualBattleType.FINANCIAL_OPPRESSION,
                        SpiritualBattleType.COMMUNITY_DIVISION,
                        SpiritualBattleType.EXPLOITATION,
                        SpiritualBattleType.GATEKEEPING
                    ]
                },
                IndustryStructure.INDEPENDENT: {
                    "description": "Local economies, community currencies, cooperatives",
                    "gatekeepers": ["Local leaders", "Cooperative boards"],
                    "power": "Low - community-controlled",
                    "mission_alignment": "High - serves community, stewardship-based",
                    "spiritual_battles": []
                },
                IndustryStructure.DIY: {
                    "description": "Gift economy, barter, resource-based, community exchange",
                    "gatekeepers": ["None - community self-organized"],
                    "power": "None - fully community-controlled",
                    "mission_alignment": "Very High - pure stewardship, community-first",
                    "spiritual_battles": []
                }
            },
            IndustryType.FINANCE: {
                IndustryStructure.MAJOR_LABELS: {
                    "description": "Big banks, Wall Street, investment firms",
                    "gatekeepers": ["Bank executives", "Investment bankers", "Regulators"],
                    "power": "Absolute - controls money, credit, access",
                    "mission_alignment": "Very Low - profit-driven, exploits communities, creates debt",
                    "spiritual_battles": [
                        SpiritualBattleType.FINANCIAL_OPPRESSION,
                        SpiritualBattleType.EXPLOITATION,
                        SpiritualBattleType.GATEKEEPING,
                        SpiritualBattleType.COMMUNITY_DIVISION
                    ]
                },
                IndustryStructure.INDEPENDENT: {
                    "description": "Credit unions, community banks, ethical investing",
                    "gatekeepers": ["Credit union boards", "Community leaders"],
                    "power": "Medium - more community-focused",
                    "mission_alignment": "Medium - can serve community if aligned",
                    "spiritual_battles": [
                        SpiritualBattleType.FINANCIAL_OPPRESSION  # Less severe
                    ]
                },
                IndustryStructure.DIY: {
                    "description": "Community lending, mutual aid, direct exchange",
                    "gatekeepers": ["None - community self-organized"],
                    "power": "None - fully community-controlled",
                    "mission_alignment": "Very High - serves community directly, no exploitation",
                    "spiritual_battles": []
                }
            },
            IndustryType.LIVE_EVENTS: {
                IndustryStructure.MAJOR_LABELS: {
                    "description": "Major venues, Live Nation, Ticketmaster, corporate promoters",
                    "gatekeepers": ["Venue owners", "Promoters", "Ticket companies", "Booking agents"],
                    "power": "Very High - controls venues, tickets, artist access",
                    "mission_alignment": "Very Low - exploits artists and fans, ticket scalping, venue fees",
                    "spiritual_battles": [
                        SpiritualBattleType.GATEKEEPING,
                        SpiritualBattleType.EXPLOITATION,
                        SpiritualBattleType.VENUE_EXPLOITATION,
                        SpiritualBattleType.TICKET_SCALPING,
                        SpiritualBattleType.PROMOTER_EXPLOITATION,
                        SpiritualBattleType.COMMUNITY_DIVISION
                    ]
                },
                IndustryStructure.INDEPENDENT: {
                    "description": "Independent venues, DIY promoters, community spaces",
                    "gatekeepers": ["Venue owners", "Promoters"],
                    "power": "Medium - more artist-friendly, still gatekeepers",
                    "mission_alignment": "Medium - can serve community if aligned",
                    "spiritual_battles": [
                        SpiritualBattleType.VENUE_EXPLOITATION,
                        SpiritualBattleType.GATEKEEPING
                    ]
                },
                IndustryStructure.DIY: {
                    "description": "House shows, community spaces, free events, direct-to-fan",
                    "gatekeepers": ["None - community self-organized"],
                    "power": "None - fully community-controlled",
                    "mission_alignment": "Very High - serves community directly, unites people",
                    "spiritual_battles": []
                }
            },
            IndustryType.SHADY_BUSINESS: {
                IndustryStructure.MAJOR_LABELS: {
                    "description": "Industries that seem shady but may be necessary: gambling, adult entertainment, certain financial instruments, etc.",
                    "gatekeepers": ["Industry regulators", "Corporate executives", "Lobbyists"],
                    "power": "Very High - controls access, often regulated",
                    "mission_alignment": "Very Low - but may be necessary for path",
                    "spiritual_battles": [
                        SpiritualBattleType.SHADY_NECESSARY,
                        SpiritualBattleType.EXPLOITATION,
                        SpiritualBattleType.GATEKEEPING,
                        SpiritualBattleType.COMMUNITY_DIVISION
                    ],
                    "note": "Shady but necessary - requires recycling strategy"
                },
                IndustryStructure.INDEPENDENT: {
                    "description": "Independent operators in necessary but problematic industries",
                    "gatekeepers": ["Independent operators", "Regulators"],
                    "power": "Medium - more control, still regulated",
                    "mission_alignment": "Low - but can be recycled if aligned",
                    "spiritual_battles": [
                        SpiritualBattleType.SHADY_NECESSARY,
                        SpiritualBattleType.EXPLOITATION
                    ],
                    "note": "Can be recycled with right spirits"
                },
                IndustryStructure.DIY: {
                    "description": "Community-controlled versions of necessary industries",
                    "gatekeepers": ["None - community self-regulated"],
                    "power": "None - fully community-controlled",
                    "mission_alignment": "High - recycled to serve mission",
                    "spiritual_battles": [],
                    "note": "Recycled - transformed to serve mission"
                }
            }
        }
        
        self.mission_keywords = [
            "stewardship", "community", "right spirits", "love",
            "peace", "unity", "we all win", "serve", "honor"
        ]
        
        self.anti_mission_patterns = [
            "exploitation", "gatekeeping", "soul selling", "suppression",
            "division", "profit over people", "formulaic", "manufactured",
            "oppression", "manipulation", "control", "paywall"
        ]
    
    def analyze_music_industry(
        self,
        structure: IndustryStructure = IndustryStructure.MAJOR_LABELS
    ) -> IndustryAnalysis:
        """
        Analyze music industry through mission lens.
        
        Questions:
        - Does it serve stewardship and community?
        - Does it honor song and creative expression?
        - What spiritual battles exist?
        - How do we navigate with right spirits?
        """
        analysis = IndustryAnalysis(
            industry_type=IndustryType.MUSIC_INDUSTRY,
            structure=structure
        )
        
        industry_info = self.industry_structures[IndustryType.MUSIC_INDUSTRY].get(structure, {})
        
        # Check mission alignment
        mission_alignment = industry_info.get("mission_alignment", "Low")
        if mission_alignment == "High" or mission_alignment == "Very High":
            analysis.serves_mission = True
            analysis.mission_alignment_score = 80.0 if mission_alignment == "High" else 90.0
        elif mission_alignment == "Medium":
            analysis.serves_mission = True
            analysis.mission_alignment_score = 50.0
        else:
            # Even low alignment can serve mission if artist controls message
            if structure == IndustryStructure.DIY:
                analysis.serves_mission = True  # DIY allows mission alignment
                analysis.mission_alignment_score = 70.0
            else:
                analysis.serves_mission = False
                analysis.mission_alignment_score = 20.0
        
        # Check if honors song
        if structure == IndustryStructure.DIY:
            analysis.honors_song = True
        elif structure == IndustryStructure.INDEPENDENT:
            analysis.honors_song = True  # More artist-friendly
        else:
            analysis.honors_song = False  # Major labels often suppress creative expression
        
        # Identify spiritual battles
        analysis.spiritual_battles = industry_info.get("spiritual_battles", [])
        
        # Check for right spirits
        if structure == IndustryStructure.DIY:
            analysis.right_spirits_present = True  # Artist controls message
        elif structure == IndustryStructure.INDEPENDENT:
            analysis.right_spirits_present = True  # More aligned with mission
        else:
            analysis.right_spirits_present = False  # Major labels often misaligned
        
        # Gatekeepers
        analysis.gatekeepers = industry_info.get("gatekeepers", [])
        
        # Opportunities
        if structure == IndustryStructure.DIY:
            analysis.opportunities = [
                "Direct connection to community",
                "Full creative control",
                "Songs serve mission directly",
                "No gatekeepers blocking message",
                "Can honor song and mission together"
            ]
        elif structure == IndustryStructure.INDEPENDENT:
            analysis.opportunities = [
                "More creative freedom than majors",
                "Better artist support",
                "Can maintain mission alignment",
                "Community-focused labels exist"
            ]
        else:
            analysis.opportunities = [
                "Wide distribution reach",
                "Marketing resources",
                "Industry connections",
                "But: Must navigate gatekeepers carefully"
            ]
        
        # Calculate symbiosis score
        # Symbiosis = mission alignment + honors song + right spirits
        symbiosis_factors = []
        if analysis.serves_mission:
            symbiosis_factors.append(analysis.mission_alignment_score)
        if analysis.honors_song:
            symbiosis_factors.append(80.0)
        if analysis.right_spirits_present:
            symbiosis_factors.append(80.0)
        
        if symbiosis_factors:
            analysis.symbiosis_score = sum(symbiosis_factors) / len(symbiosis_factors)
        else:
            analysis.symbiosis_score = 0.0
        
        # Recommendations
        if structure == IndustryStructure.MAJOR_LABELS:
            analysis.recommendations = [
                "Navigate carefully - gatekeepers may block mission-aligned content",
                "Maintain creative control in contracts",
                "Use major platform for distribution, but keep message independent",
                "Build community outside industry structure",
                "Remember: Song must serve mission, not industry profit"
            ]
            analysis.warnings = [
                "Major labels prioritize profit over mission",
                "Gatekeepers may suppress mission-aligned content",
                "Contracts may limit creative expression",
                "Industry may exploit for profit, not serve community"
            ]
        elif structure == IndustryStructure.INDEPENDENT:
            analysis.recommendations = [
                "Choose indie labels aligned with mission",
                "Maintain creative control",
                "Build community through music",
                "Use indie structure to serve mission"
            ]
        else:  # DIY
            analysis.recommendations = [
                "Perfect structure for mission alignment",
                "Full control over message and distribution",
                "Direct connection to community",
                "Song serves mission, mission honors song",
                "Right spirits flow freely"
            ]
        
        return analysis
    
    def analyze_hollywood(
        self,
        structure: IndustryStructure = IndustryStructure.MAJOR_LABELS
    ) -> IndustryAnalysis:
        """
        Analyze Hollywood through mission lens.
        
        Questions:
        - Does it serve stewardship and community?
        - Does it honor creative expression?
        - What spiritual battles exist?
        - How do we navigate with right spirits?
        """
        analysis = IndustryAnalysis(
            industry_type=IndustryType.HOLLYWOOD,
            structure=structure
        )
        
        industry_info = self.industry_structures[IndustryType.HOLLYWOOD].get(structure, {})
        
        # Check mission alignment
        mission_alignment = industry_info.get("mission_alignment", "Low")
        if mission_alignment == "High" or mission_alignment == "Very High":
            analysis.serves_mission = True
            analysis.mission_alignment_score = 80.0 if mission_alignment == "High" else 90.0
        elif mission_alignment == "Medium":
            analysis.serves_mission = True
            analysis.mission_alignment_score = 50.0
        else:
            # Even low alignment can serve mission if creator controls message
            if structure == IndustryStructure.DIY:
                analysis.serves_mission = True  # DIY allows mission alignment
                analysis.mission_alignment_score = 70.0
            else:
                analysis.serves_mission = False
                analysis.mission_alignment_score = 15.0  # Lower than music - more gatekeeping
        
        # Check if honors creative expression
        if structure == IndustryStructure.DIY:
            analysis.honors_song = True  # Honors all creative expression
        elif structure == IndustryStructure.INDEPENDENT:
            analysis.honors_song = True  # More creative freedom
        else:
            analysis.honors_song = False  # Major studios often formulaic
        
        # Identify spiritual battles
        analysis.spiritual_battles = industry_info.get("spiritual_battles", [])
        
        # Check for right spirits
        if structure == IndustryStructure.DIY:
            analysis.right_spirits_present = True
        elif structure == IndustryStructure.INDEPENDENT:
            analysis.right_spirits_present = True
        else:
            analysis.right_spirits_present = False  # Major studios often misaligned
        
        # Gatekeepers
        analysis.gatekeepers = industry_info.get("gatekeepers", [])
        
        # Opportunities
        if structure == IndustryStructure.DIY:
            analysis.opportunities = [
                "Direct connection to audience",
                "Full creative control",
                "Content serves mission directly",
                "No gatekeepers blocking message",
                "Can honor creative expression and mission together"
            ]
        elif structure == IndustryStructure.INDEPENDENT:
            analysis.opportunities = [
                "More creative freedom than majors",
                "Diverse stories possible",
                "Can maintain mission alignment",
                "Festival circuit for exposure"
            ]
        else:
            analysis.opportunities = [
                "Wide distribution reach",
                "Marketing resources",
                "Industry connections",
                "But: Must navigate gatekeepers very carefully"
            ]
        
        # Calculate symbiosis score
        symbiosis_factors = []
        if analysis.serves_mission:
            symbiosis_factors.append(analysis.mission_alignment_score)
        if analysis.honors_song:
            symbiosis_factors.append(80.0)
        if analysis.right_spirits_present:
            symbiosis_factors.append(80.0)
        
        if symbiosis_factors:
            analysis.symbiosis_score = sum(symbiosis_factors) / len(symbiosis_factors)
        else:
            analysis.symbiosis_score = 0.0
        
        # Recommendations
        if structure == IndustryStructure.MAJOR_LABELS:
            analysis.recommendations = [
                "Navigate very carefully - heavy gatekeeping",
                "Major studios prioritize profit over mission",
                "Formulaic content often suppresses mission",
                "Build community outside industry structure",
                "Use platform for distribution, keep message independent"
            ]
            analysis.warnings = [
                "Heavy gatekeeping may block mission-aligned content",
                "Industry may require soul-selling for access",
                "Creative expression often suppressed for profit",
                "Community may be divided by industry narratives",
                "Exploitation common - protect mission and values"
            ]
        elif structure == IndustryStructure.INDEPENDENT:
            analysis.recommendations = [
                "Choose indie projects aligned with mission",
                "Maintain creative control",
                "Use festivals to build community",
                "Independent structure can serve mission"
            ]
        else:  # DIY
            analysis.recommendations = [
                "Perfect structure for mission alignment",
                "Full control over content and message",
                "Direct connection to community",
                "Creative expression serves mission",
                "Right spirits flow freely"
            ]
        
        return analysis
    
    def analyze_sports(
        self,
        structure: IndustryStructure = IndustryStructure.MAJOR_LABELS
    ) -> IndustryAnalysis:
        """
        Analyze sports industry through mission lens.
        
        Questions:
        - Does it serve stewardship and community?
        - Does it unite or divide community?
        - What spiritual battles exist?
        - How do we navigate with right spirits?
        """
        analysis = IndustryAnalysis(
            industry_type=IndustryType.SPORTS,
            structure=structure
        )
        
        industry_info = self.industry_structures[IndustryType.SPORTS].get(structure, {})
        
        # Check mission alignment
        mission_alignment = industry_info.get("mission_alignment", "Low")
        if mission_alignment == "Very High":
            analysis.serves_mission = True
            analysis.mission_alignment_score = 90.0
        elif mission_alignment == "High":
            analysis.serves_mission = True
            analysis.mission_alignment_score = 80.0
        elif mission_alignment == "Medium":
            analysis.serves_mission = True
            analysis.mission_alignment_score = 50.0
        else:
            # DIY can serve mission even if marked "Low" in structure
            if structure == IndustryStructure.DIY:
                analysis.serves_mission = True  # DIY allows mission alignment
                analysis.mission_alignment_score = 80.0
            else:
                analysis.serves_mission = False
                analysis.mission_alignment_score = 10.0  # Very low - exploits athletes
        
        # Check if honors community
        if structure == IndustryStructure.DIY:
            analysis.honors_song = True  # Honors community expression
        elif structure == IndustryStructure.INDEPENDENT:
            analysis.honors_song = True
        else:
            analysis.honors_song = False  # Major leagues exploit athletes
        
        # Identify spiritual battles
        analysis.spiritual_battles = industry_info.get("spiritual_battles", [])
        
        # Check for right spirits
        if structure in [IndustryStructure.DIY, IndustryStructure.INDEPENDENT]:
            analysis.right_spirits_present = True
        else:
            analysis.right_spirits_present = False
        
        # Gatekeepers
        analysis.gatekeepers = industry_info.get("gatekeepers", [])
        
        # Opportunities
        if structure == IndustryStructure.DIY:
            analysis.opportunities = [
                "Pure community unity",
                "No profit motive",
                "Sports serve community directly",
                "Right spirits flow freely"
            ]
        elif structure == IndustryStructure.INDEPENDENT:
            analysis.opportunities = [
                "Community-controlled",
                "Unites people",
                "Can serve mission"
            ]
        else:
            analysis.opportunities = [
                "Wide reach",
                "But: Exploits athletes",
                "But: Divides communities",
                "But: Profit over people"
            ]
        
        # Calculate symbiosis
        symbiosis_factors = []
        if analysis.serves_mission:
            symbiosis_factors.append(analysis.mission_alignment_score)
        if analysis.honors_song:
            symbiosis_factors.append(80.0)
        if analysis.right_spirits_present:
            symbiosis_factors.append(80.0)
        
        analysis.symbiosis_score = sum(symbiosis_factors) / len(symbiosis_factors) if symbiosis_factors else 0.0
        
        # Recommendations
        if structure == IndustryStructure.MAJOR_LABELS:
            analysis.recommendations = [
                "Major leagues exploit athletes and divide communities",
                "Use platform carefully - don't let it control message",
                "Build community outside league structure",
                "Support independent/community sports"
            ]
            analysis.warnings = [
                "Athletes exploited for profit",
                "Sports used to divide communities",
                "Paywalls exclude community",
                "Profit over people, not mission"
            ]
        elif structure == IndustryStructure.INDEPENDENT:
            analysis.recommendations = [
                "Community sports unite people",
                "Can serve mission if aligned",
                "Build community through sports"
            ]
        else:  # DIY
            analysis.recommendations = [
                "Perfect for mission - pure community",
                "Sports unite, don't divide",
                "No exploitation, no profit motive",
                "Right spirits flow freely"
            ]
        
        return analysis
    
    def analyze_tv_pay_per_view(
        self,
        structure: IndustryStructure = IndustryStructure.MAJOR_LABELS
    ) -> IndustryAnalysis:
        """
        Analyze TV/Pay-Per-View through mission lens.
        
        Questions:
        - Does it serve stewardship and community?
        - Do paywalls divide or unite?
        - What spiritual battles exist?
        - How do we navigate with right spirits?
        """
        analysis = IndustryAnalysis(
            industry_type=IndustryType.TV_PAY_PER_VIEW,
            structure=structure
        )
        
        industry_info = self.industry_structures[IndustryType.TV_PAY_PER_VIEW].get(structure, {})
        
        # Check mission alignment
        mission_alignment = industry_info.get("mission_alignment", "Low")
        if mission_alignment == "High" or mission_alignment == "Very High":
            analysis.serves_mission = True
            analysis.mission_alignment_score = 80.0 if mission_alignment == "High" else 90.0
        elif mission_alignment == "Medium":
            analysis.serves_mission = True
            analysis.mission_alignment_score = 50.0
        else:
            # DIY can serve mission even if marked "Low" in structure
            if structure == IndustryStructure.DIY:
                analysis.serves_mission = True  # DIY allows mission alignment
                analysis.mission_alignment_score = 70.0
            else:
                analysis.serves_mission = False
                analysis.mission_alignment_score = 15.0  # Paywalls divide
        
        # Check if honors access
        if structure == IndustryStructure.DIY:
            analysis.honors_song = True  # Free access
        else:
            analysis.honors_song = False  # Paywalls block access
        
        # Identify spiritual battles
        analysis.spiritual_battles = industry_info.get("spiritual_battles", [])
        
        # Check for right spirits
        if structure == IndustryStructure.DIY:
            analysis.right_spirits_present = True
        else:
            analysis.right_spirits_present = False
        
        # Gatekeepers
        analysis.gatekeepers = industry_info.get("gatekeepers", [])
        
        # Opportunities
        if structure == IndustryStructure.DIY:
            analysis.opportunities = [
                "Free access for all",
                "Content serves community",
                "No paywalls divide",
                "Right spirits flow freely"
            ]
        else:
            analysis.opportunities = [
                "Wide distribution",
                "But: Paywalls divide community",
                "But: Content controlled by gatekeepers"
            ]
        
        # Calculate symbiosis
        symbiosis_factors = []
        if analysis.serves_mission:
            symbiosis_factors.append(analysis.mission_alignment_score)
        if analysis.honors_song:
            symbiosis_factors.append(80.0)
        if analysis.right_spirits_present:
            symbiosis_factors.append(80.0)
        
        analysis.symbiosis_score = sum(symbiosis_factors) / len(symbiosis_factors) if symbiosis_factors else 0.0
        
        # Recommendations
        if structure == IndustryStructure.MAJOR_LABELS:
            analysis.recommendations = [
                "Paywalls divide community - avoid if possible",
                "Use for distribution, keep message free",
                "Build community outside paywall structure"
            ]
            analysis.warnings = [
                "Paywalls exclude community",
                "Content controlled by gatekeepers",
                "Information controlled for profit",
                "Divides community by access"
            ]
        elif structure == IndustryStructure.INDEPENDENT:
            analysis.recommendations = [
                "Can serve community if free/low-cost",
                "Maintain access for all",
                "Use to unite, not divide"
            ]
        else:  # DIY
            analysis.recommendations = [
                "Perfect for mission - free access",
                "Content serves community directly",
                "No paywalls divide",
                "Right spirits flow freely"
            ]
        
        return analysis
    
    def analyze_news_media(
        self,
        structure: IndustryStructure = IndustryStructure.MAJOR_LABELS
    ) -> IndustryAnalysis:
        """
        Analyze news media through mission lens.
        
        Questions:
        - Does it serve truth and community?
        - Does it unite or divide?
        - What spiritual battles exist?
        - How do we navigate with right spirits?
        """
        analysis = IndustryAnalysis(
            industry_type=IndustryType.NEWS_MEDIA,
            structure=structure
        )
        
        industry_info = self.industry_structures[IndustryType.NEWS_MEDIA].get(structure, {})
        
        # Check mission alignment
        mission_alignment = industry_info.get("mission_alignment", "Low")
        if mission_alignment == "High" or mission_alignment == "Very High":
            analysis.serves_mission = True
            analysis.mission_alignment_score = 80.0 if mission_alignment == "High" else 90.0
        elif mission_alignment == "Medium":
            analysis.serves_mission = True
            analysis.mission_alignment_score = 50.0
        else:
            # DIY can serve mission even if marked "Low" in structure
            if structure == IndustryStructure.DIY:
                analysis.serves_mission = True  # DIY allows mission alignment
                analysis.mission_alignment_score = 70.0
            else:
                analysis.serves_mission = False
                analysis.mission_alignment_score = 10.0  # Very low - manipulates truth
        
        # Check if honors truth
        if structure == IndustryStructure.DIY:
            analysis.honors_song = True  # Honors truth
        else:
            analysis.honors_song = False  # Major media manipulates
        
        # Identify spiritual battles
        analysis.spiritual_battles = industry_info.get("spiritual_battles", [])
        
        # Check for right spirits
        if structure == IndustryStructure.DIY:
            analysis.right_spirits_present = True
        else:
            analysis.right_spirits_present = False
        
        # Gatekeepers
        analysis.gatekeepers = industry_info.get("gatekeepers", [])
        
        # Opportunities
        if structure == IndustryStructure.DIY:
            analysis.opportunities = [
                "Truth serves community directly",
                "No narrative manipulation",
                "Right spirits flow freely"
            ]
        else:
            analysis.opportunities = [
                "Wide reach",
                "But: Narrative manipulation",
                "But: Divides community",
                "But: Information controlled"
            ]
        
        # Calculate symbiosis
        symbiosis_factors = []
        if analysis.serves_mission:
            symbiosis_factors.append(analysis.mission_alignment_score)
        if analysis.honors_song:
            symbiosis_factors.append(80.0)
        if analysis.right_spirits_present:
            symbiosis_factors.append(80.0)
        
        analysis.symbiosis_score = sum(symbiosis_factors) / len(symbiosis_factors) if symbiosis_factors else 0.0
        
        # Recommendations
        if structure == IndustryStructure.MAJOR_LABELS:
            analysis.recommendations = [
                "Major media manipulates narratives - avoid",
                "Build truth-telling outside corporate structure",
                "Use platform carefully - don't let it control truth"
            ]
            analysis.warnings = [
                "Information controlled for profit",
                "Narratives manipulated to divide",
                "Truth suppressed for agenda",
                "Community divided by media narratives"
            ]
        elif structure == IndustryStructure.INDEPENDENT:
            analysis.recommendations = [
                "Independent journalism can serve truth",
                "Choose aligned outlets",
                "Support truth-telling"
            ]
        else:  # DIY
            analysis.recommendations = [
                "Perfect for mission - truth serves community",
                "No narrative manipulation",
                "Right spirits flow freely"
            ]
        
        return analysis
    
    def analyze_global_economics(
        self,
        structure: IndustryStructure = IndustryStructure.MAJOR_LABELS
    ) -> IndustryAnalysis:
        """
        Analyze global economics through mission lens.
        
        Questions:
        - Does it serve stewardship and community?
        - Does it oppress or liberate?
        - What spiritual battles exist?
        - How do we navigate with right spirits?
        """
        analysis = IndustryAnalysis(
            industry_type=IndustryType.GLOBAL_ECONOMICS,
            structure=structure
        )
        
        industry_info = self.industry_structures[IndustryType.GLOBAL_ECONOMICS].get(structure, {})
        
        # Check mission alignment (handle strings like "Very High - description")
        mission_alignment = industry_info.get("mission_alignment", "Low")
        mission_alignment_lower = mission_alignment.lower()
        
        if "very high" in mission_alignment_lower:
            analysis.serves_mission = True
            analysis.mission_alignment_score = 90.0
        elif "high" in mission_alignment_lower:
            analysis.serves_mission = True
            analysis.mission_alignment_score = 80.0
        elif "medium" in mission_alignment_lower:
            analysis.serves_mission = True
            analysis.mission_alignment_score = 50.0
        else:
            # DIY can serve mission even if marked "Low" in structure
            if structure == IndustryStructure.DIY:
                analysis.serves_mission = True  # DIY allows mission alignment
                analysis.mission_alignment_score = 80.0
            else:
                analysis.serves_mission = False
                analysis.mission_alignment_score = 5.0  # Very low - oppresses
        
        # Check if honors stewardship
        if structure == IndustryStructure.DIY:
            analysis.honors_song = True  # Honors stewardship
        elif structure == IndustryStructure.INDEPENDENT:
            analysis.honors_song = True
        else:
            analysis.honors_song = False  # Oppresses communities
        
        # Identify spiritual battles
        analysis.spiritual_battles = industry_info.get("spiritual_battles", [])
        
        # Check for right spirits
        if structure in [IndustryStructure.DIY, IndustryStructure.INDEPENDENT]:
            analysis.right_spirits_present = True
        else:
            analysis.right_spirits_present = False
        
        # Gatekeepers
        analysis.gatekeepers = industry_info.get("gatekeepers", [])
        
        # Opportunities
        if structure == IndustryStructure.DIY:
            analysis.opportunities = [
                "Pure stewardship economy",
                "Community-first",
                "No exploitation",
                "Right spirits flow freely"
            ]
        elif structure == IndustryStructure.INDEPENDENT:
            analysis.opportunities = [
                "Community-controlled",
                "Stewardship-based",
                "Can serve mission"
            ]
        else:
            analysis.opportunities = [
                "Global reach",
                "But: Oppresses communities",
                "But: Exploits for profit",
                "But: Divides world"
            ]
        
        # Calculate symbiosis
        symbiosis_factors = []
        if analysis.serves_mission:
            symbiosis_factors.append(analysis.mission_alignment_score)
        if analysis.honors_song:
            symbiosis_factors.append(80.0)
        if analysis.right_spirits_present:
            symbiosis_factors.append(80.0)
        
        analysis.symbiosis_score = sum(symbiosis_factors) / len(symbiosis_factors) if symbiosis_factors else 0.0
        
        # Recommendations
        if structure == IndustryStructure.MAJOR_LABELS:
            analysis.recommendations = [
                "Global economic systems oppress - navigate very carefully",
                "Build community economies outside global structure",
                "Use local/community exchange when possible",
                "Protect community from financial oppression"
            ]
            analysis.warnings = [
                "Financial oppression of communities",
                "Exploitation for profit",
                "Global systems divide world",
                "Very low mission alignment"
            ]
        elif structure == IndustryStructure.INDEPENDENT:
            analysis.recommendations = [
                "Community economies can serve mission",
                "Local exchange serves community",
                "Stewardship-based economics"
            ]
        else:  # DIY
            analysis.recommendations = [
                "Perfect for mission - pure stewardship",
                "Community-first economics",
                "No exploitation, no oppression",
                "Right spirits flow freely"
            ]
        
        return analysis
    
    def analyze_finance(
        self,
        structure: IndustryStructure = IndustryStructure.MAJOR_LABELS
    ) -> IndustryAnalysis:
        """
        Analyze finance industry through mission lens.
        
        Questions:
        - Does it serve stewardship and community?
        - Does it oppress or liberate?
        - What spiritual battles exist?
        - How do we navigate with right spirits?
        """
        analysis = IndustryAnalysis(
            industry_type=IndustryType.FINANCE,
            structure=structure
        )
        
        industry_info = self.industry_structures[IndustryType.FINANCE].get(structure, {})
        
        # Check mission alignment (handle strings like "Very High - description")
        mission_alignment = industry_info.get("mission_alignment", "Low")
        mission_alignment_lower = mission_alignment.lower()
        
        if "very high" in mission_alignment_lower:
            analysis.serves_mission = True
            analysis.mission_alignment_score = 90.0
        elif "high" in mission_alignment_lower:
            analysis.serves_mission = True
            analysis.mission_alignment_score = 80.0
        elif "medium" in mission_alignment_lower:
            analysis.serves_mission = True
            analysis.mission_alignment_score = 50.0
        else:
            # DIY can serve mission even if marked "Low" in structure
            if structure == IndustryStructure.DIY:
                analysis.serves_mission = True  # DIY allows mission alignment
                analysis.mission_alignment_score = 80.0
            else:
                analysis.serves_mission = False
                analysis.mission_alignment_score = 5.0  # Very low - oppresses
        
        # Check if honors stewardship
        if structure == IndustryStructure.DIY:
            analysis.honors_song = True  # Honors community
        elif structure == IndustryStructure.INDEPENDENT:
            analysis.honors_song = True
        else:
            analysis.honors_song = False  # Big banks oppress
        
        # Identify spiritual battles
        analysis.spiritual_battles = industry_info.get("spiritual_battles", [])
        
        # Check for right spirits
        if structure in [IndustryStructure.DIY, IndustryStructure.INDEPENDENT]:
            analysis.right_spirits_present = True
        else:
            analysis.right_spirits_present = False
        
        # Gatekeepers
        analysis.gatekeepers = industry_info.get("gatekeepers", [])
        
        # Opportunities
        if structure == IndustryStructure.DIY:
            analysis.opportunities = [
                "Community lending, mutual aid",
                "Direct exchange, no exploitation",
                "Serves community directly",
                "Right spirits flow freely"
            ]
        elif structure == IndustryStructure.INDEPENDENT:
            analysis.opportunities = [
                "Community-focused",
                "Can serve mission if aligned",
                "Less exploitation"
            ]
        else:
            analysis.opportunities = [
                "Access to capital",
                "But: Exploits through debt",
                "But: Oppresses communities",
                "But: Profit over people"
            ]
        
        # Calculate symbiosis
        symbiosis_factors = []
        if analysis.serves_mission:
            symbiosis_factors.append(analysis.mission_alignment_score)
        if analysis.honors_song:
            symbiosis_factors.append(80.0)
        if analysis.right_spirits_present:
            symbiosis_factors.append(80.0)
        
        analysis.symbiosis_score = sum(symbiosis_factors) / len(symbiosis_factors) if symbiosis_factors else 0.0
        
        # Recommendations
        if structure == IndustryStructure.MAJOR_LABELS:
            analysis.recommendations = [
                "Big banks oppress - avoid if possible",
                "Build community finance outside banking structure",
                "Use credit unions when needed",
                "Protect community from financial exploitation"
            ]
            analysis.warnings = [
                "Financial oppression through debt",
                "Exploitation of communities",
                "Gatekeeping access to resources",
                "Very low mission alignment"
            ]
        elif structure == IndustryStructure.INDEPENDENT:
            analysis.recommendations = [
                "Credit unions can serve community",
                "Choose aligned financial institutions",
                "Support community finance"
            ]
        else:  # DIY
            analysis.recommendations = [
                "Perfect for mission - community finance",
                "Mutual aid, direct exchange",
                "No exploitation, no oppression",
                "Right spirits flow freely"
            ]
        
        return analysis
    
    def analyze_live_events(
        self,
        structure: IndustryStructure = IndustryStructure.MAJOR_LABELS
    ) -> IndustryAnalysis:
        """
        Analyze live events industry through mission lens.
        
        Questions:
        - Does it serve stewardship and community?
        - Does it unite or divide community?
        - What spiritual battles exist (venue exploitation, ticket scalping)?
        - How do we navigate with right spirits?
        """
        analysis = IndustryAnalysis(
            industry_type=IndustryType.LIVE_EVENTS,
            structure=structure
        )
        
        industry_info = self.industry_structures[IndustryType.LIVE_EVENTS].get(structure, {})
        
        # Check mission alignment
        mission_alignment = industry_info.get("mission_alignment", "Low")
        mission_alignment_lower = mission_alignment.lower()
        
        if "very high" in mission_alignment_lower:
            analysis.serves_mission = True
            analysis.mission_alignment_score = 90.0
        elif "high" in mission_alignment_lower:
            analysis.serves_mission = True
            analysis.mission_alignment_score = 80.0
        elif "medium" in mission_alignment_lower:
            analysis.serves_mission = True
            analysis.mission_alignment_score = 50.0
        else:
            # DIY can serve mission even if marked "Low" in structure
            if structure == IndustryStructure.DIY:
                analysis.serves_mission = True  # DIY allows mission alignment
                analysis.mission_alignment_score = 80.0
            else:
                analysis.serves_mission = False
                analysis.mission_alignment_score = 10.0  # Very low - exploits artists/fans
        
        # Check if honors community
        if structure == IndustryStructure.DIY:
            analysis.honors_song = True  # Honors community gathering
        elif structure == IndustryStructure.INDEPENDENT:
            analysis.honors_song = True
        else:
            analysis.honors_song = False  # Major venues exploit
        
        # Identify spiritual battles
        analysis.spiritual_battles = industry_info.get("spiritual_battles", [])
        
        # Check for right spirits
        if structure == IndustryStructure.DIY:
            analysis.right_spirits_present = True
        elif structure == IndustryStructure.INDEPENDENT:
            analysis.right_spirits_present = True
        else:
            analysis.right_spirits_present = False
        
        # Gatekeepers
        analysis.gatekeepers = industry_info.get("gatekeepers", [])
        
        # Opportunities
        if structure == IndustryStructure.DIY:
            analysis.opportunities = [
                "House shows, community spaces",
                "Free events unite community",
                "Direct-to-fan connection",
                "Right spirits flow freely"
            ]
        elif structure == IndustryStructure.INDEPENDENT:
            analysis.opportunities = [
                "Independent venues can serve community",
                "More artist-friendly",
                "Can align with mission"
            ]
        else:
            analysis.opportunities = [
                "Wide reach",
                "But: Venue exploitation",
                "But: Ticket scalping",
                "But: Promoter exploitation"
            ]
        
        # Calculate symbiosis
        symbiosis_factors = []
        if analysis.serves_mission:
            symbiosis_factors.append(analysis.mission_alignment_score)
        if analysis.honors_song:
            symbiosis_factors.append(80.0)
        if analysis.right_spirits_present:
            symbiosis_factors.append(80.0)
        
        analysis.symbiosis_score = sum(symbiosis_factors) / len(symbiosis_factors) if symbiosis_factors else 0.0
        
        # Recommendations
        if structure == IndustryStructure.MAJOR_LABELS:
            analysis.recommendations = [
                "Major venues exploit artists and fans - navigate carefully",
                "Ticket scalping divides community - avoid if possible",
                "Use for reach, build community outside venue structure",
                "Protect mission - don't let promoters control message"
            ]
            analysis.warnings = [
                "Venue fees exploit artists",
                "Ticket scalping exploits fans",
                "Promoters may require soul-selling",
                "Heavy gatekeeping blocks mission-aligned artists"
            ]
        elif structure == IndustryStructure.INDEPENDENT:
            analysis.recommendations = [
                "Independent venues can serve community",
                "Choose aligned venues and promoters",
                "Maintain control over message",
                "Build community through events"
            ]
        else:  # DIY
            analysis.recommendations = [
                "Perfect for mission - community gatherings",
                "House shows unite community",
                "Free events serve all",
                "Right spirits flow freely"
            ]
        
        return analysis
    
    def analyze_shady_business(
        self,
        structure: IndustryStructure = IndustryStructure.MAJOR_LABELS,
        business_type: str = "general"
    ) -> IndustryAnalysis:
        """
        Analyze "shady business" - industries that seem problematic but may be necessary.
        
        Key concept: RECYCLING
        - Some industries are necessary for path but seem "shady"
        - We must RECYCLE them - transform them to serve mission
        - Navigate with right spirits, not wrong ones
        
        Questions:
        - Is this business necessary for our path?
        - How do we recycle it to serve mission?
        - How do we navigate with right spirits?
        - What spiritual battles exist?
        """
        analysis = IndustryAnalysis(
            industry_type=IndustryType.SHADY_BUSINESS,
            structure=structure
        )
        
        industry_info = self.industry_structures[IndustryType.SHADY_BUSINESS].get(structure, {})
        
        # Check mission alignment
        mission_alignment = industry_info.get("mission_alignment", "Low")
        mission_alignment_lower = mission_alignment.lower()
        
        if "very high" in mission_alignment_lower or "high" in mission_alignment_lower:
            analysis.serves_mission = True
            analysis.mission_alignment_score = 80.0 if "high" in mission_alignment_lower else 90.0
        elif "medium" in mission_alignment_lower:
            analysis.serves_mission = True
            analysis.mission_alignment_score = 50.0
        else:
            # Shady business can be recycled - DIY structure allows transformation
            if structure == IndustryStructure.DIY:
                analysis.serves_mission = True  # Recycled to serve mission
                analysis.mission_alignment_score = 75.0  # Recycled alignment
            else:
                analysis.serves_mission = False
                analysis.mission_alignment_score = 15.0  # Shady but necessary
        
        # Check if honors mission (recycled)
        if structure == IndustryStructure.DIY:
            analysis.honors_song = True  # Recycled to honor mission
        elif structure == IndustryStructure.INDEPENDENT:
            analysis.honors_song = True  # Can be recycled
        else:
            analysis.honors_song = False  # Shady, not recycled
        
        # Identify spiritual battles
        analysis.spiritual_battles = industry_info.get("spiritual_battles", [])
        
        # Check for right spirits (recycling requires right spirits)
        if structure == IndustryStructure.DIY:
            analysis.right_spirits_present = True  # Recycled with right spirits
        elif structure == IndustryStructure.INDEPENDENT:
            analysis.right_spirits_present = True  # Can recycle with right spirits
        else:
            analysis.right_spirits_present = False  # Wrong spirits, not recycled
        
        # Gatekeepers
        analysis.gatekeepers = industry_info.get("gatekeepers", [])
        
        # Opportunities (recycling opportunities)
        if structure == IndustryStructure.DIY:
            analysis.opportunities = [
                "RECYCLED - transformed to serve mission",
                "Community-controlled version",
                "Right spirits flow through recycling",
                "Necessary business serves mission"
            ]
        elif structure == IndustryStructure.INDEPENDENT:
            analysis.opportunities = [
                "Can be recycled with right spirits",
                "Transform to serve mission",
                "Navigate carefully"
            ]
        else:
            analysis.opportunities = [
                "Shady but necessary for path",
                "Requires recycling strategy",
                "Must transform to serve mission"
            ]
        
        # Calculate symbiosis (recycled symbiosis)
        symbiosis_factors = []
        if analysis.serves_mission:
            symbiosis_factors.append(analysis.mission_alignment_score)
        if analysis.honors_song:
            symbiosis_factors.append(80.0)
        if analysis.right_spirits_present:
            symbiosis_factors.append(80.0)
        
        analysis.symbiosis_score = sum(symbiosis_factors) / len(symbiosis_factors) if symbiosis_factors else 0.0
        
        # Recommendations (recycling strategy)
        if structure == IndustryStructure.MAJOR_LABELS:
            analysis.recommendations = [
                "RECYCLING STRATEGY REQUIRED:",
                "1. Identify why this business is necessary for path",
                "2. Transform it to serve mission, not profit",
                "3. Navigate with right spirits, not wrong ones",
                "4. Build community-controlled version when possible",
                "5. Use for path, recycle to serve mission",
                "6. Protect mission - don't let business control it"
            ]
            analysis.warnings = [
                "Shady business requires careful navigation",
                "Must recycle to serve mission",
                "Wrong spirits will corrupt mission",
                "Gatekeepers may block recycling",
                "Only use if truly necessary for path"
            ]
        elif structure == IndustryStructure.INDEPENDENT:
            analysis.recommendations = [
                "RECYCLING POSSIBLE:",
                "1. Transform with right spirits",
                "2. Align with mission",
                "3. Serve community, not profit",
                "4. Build recycling into structure"
            ]
        else:  # DIY
            analysis.recommendations = [
                "RECYCLED - transformed to serve mission",
                "Community-controlled version",
                "Right spirits flow through recycling",
                "Necessary business now serves mission",
                "Perfect symbiosis achieved through recycling"
            ]
        
        return analysis
    
    def get_recycling_strategy(
        self,
        industry_type: IndustryType,
        why_necessary: str = "Path requires it"
    ) -> Dict[str, Any]:
        """
        Get recycling strategy for necessary but problematic industry.
        
        RECYCLING = Transforming shady business to serve mission.
        
        Steps:
        1. Identify why necessary
        2. Identify what makes it "shady"
        3. Transform to serve mission
        4. Navigate with right spirits
        5. Build community-controlled version
        """
        return {
            "industry": industry_type.value,
            "why_necessary": why_necessary,
            "recycling_steps": [
                {
                    "step": 1,
                    "action": "Identify necessity",
                    "question": "Why is this business necessary for our path?",
                    "principle": "Only use if truly necessary - not convenience"
                },
                {
                    "step": 2,
                    "action": "Identify shadiness",
                    "question": "What makes this business 'shady'?",
                    "principle": "Understand the spiritual battles"
                },
                {
                    "step": 3,
                    "action": "Transform structure",
                    "question": "How do we transform it to serve mission?",
                    "principle": "DIY structure when possible - community control"
                },
                {
                    "step": 4,
                    "action": "Navigate with right spirits",
                    "question": "How do we navigate with right spirits?",
                    "principle": "Right spirits flow through recycling, wrong spirits corrupt"
                },
                {
                    "step": 5,
                    "action": "Build community version",
                    "question": "How do we build community-controlled version?",
                    "principle": "Community serves mission, not profit"
                },
                {
                    "step": 6,
                    "action": "Protect mission",
                    "question": "How do we protect mission from business?",
                    "principle": "Mission controls business, not business controls mission"
                }
            ],
            "recycling_principles": [
                "Mission controls business, not business controls mission",
                "Right spirits flow through recycling, wrong spirits corrupt",
                "Community serves mission, not profit",
                "DIY structure when possible - community control",
                "Only use if truly necessary - not convenience",
                "Transform to serve mission, not exploit"
            ],
            "examples": {
                "gambling": {
                    "why_necessary": "May be necessary for certain paths",
                    "recycled_as": "Community-controlled, mission-aligned version",
                    "transformation": "Serve community, not exploit"
                },
                "adult_entertainment": {
                    "why_necessary": "May be necessary for certain paths",
                    "recycled_as": "Community-controlled, mission-aligned version",
                    "transformation": "Honor expression, not exploit"
                },
                "certain_financial_instruments": {
                    "why_necessary": "May be necessary for path",
                    "recycled_as": "Community-controlled, mission-aligned version",
                    "transformation": "Serve stewardship, not oppression"
                }
            },
            "warning": "Recycling requires right spirits. Wrong spirits will corrupt mission."
        }
    
    def get_navigation_strategy(
        self,
        industry_type: IndustryType,
        structure: IndustryStructure,
        mission_aligned: bool = True
    ) -> Dict[str, Any]:
        """
        Get navigation strategy for industry.
        
        How to navigate with right spirits while serving mission.
        """
        if industry_type == IndustryType.MUSIC_INDUSTRY:
            analysis = self.analyze_music_industry(structure)
        elif industry_type == IndustryType.HOLLYWOOD:
            analysis = self.analyze_hollywood(structure)
        elif industry_type == IndustryType.SPORTS:
            analysis = self.analyze_sports(structure)
        elif industry_type == IndustryType.TV_PAY_PER_VIEW:
            analysis = self.analyze_tv_pay_per_view(structure)
        elif industry_type == IndustryType.NEWS_MEDIA:
            analysis = self.analyze_news_media(structure)
        elif industry_type == IndustryType.GLOBAL_ECONOMICS:
            analysis = self.analyze_global_economics(structure)
        elif industry_type == IndustryType.FINANCE:
            analysis = self.analyze_finance(structure)
        elif industry_type == IndustryType.LIVE_EVENTS:
            analysis = self.analyze_live_events(structure)
        elif industry_type == IndustryType.SHADY_BUSINESS:
            analysis = self.analyze_shady_business(structure)
        else:
            # Default to music industry
            analysis = self.analyze_music_industry(structure)
        
        strategy = {
            "industry": industry_type.value,
            "structure": structure.value,
            "mission_aligned": mission_aligned,
            "symbiosis_score": analysis.symbiosis_score,
            "navigate_with_right_spirits": analysis.right_spirits_present,
            "spiritual_battles_to_avoid": [battle.value for battle in analysis.spiritual_battles],
            "gatekeepers_to_navigate": analysis.gatekeepers,
            "opportunities": analysis.opportunities,
            "strategy": []
        }
        
        if structure == IndustryStructure.MAJOR_LABELS:
            strategy["strategy"] = [
                "Use industry for distribution, not for message control",
                "Build community outside industry structure",
                "Maintain creative control in all contracts",
                "Protect mission - don't let gatekeepers suppress it",
                "Remember: Song/message serves mission, not industry profit",
                "Right spirits flow through community, not industry"
            ]
        elif structure == IndustryStructure.INDEPENDENT:
            strategy["strategy"] = [
                "Choose partners aligned with mission",
                "Maintain creative control",
                "Build community through work",
                "Use structure to amplify mission",
                "Right spirits can flow through aligned partners"
            ]
        else:  # DIY
            strategy["strategy"] = [
                "Full control - song/message serves mission directly",
                "Direct connection to community",
                "No gatekeepers to navigate",
                "Right spirits flow freely",
                "Perfect symbiosis: creative serves practical, practical honors creative"
            ]
        
        return strategy
    
    def explore_all_industries(self) -> Dict[str, Any]:
        """Explore ALL industries - the whole cake"""
        results = {}
        
        # Music Industry
        results["music_industry"] = {
            "major": self.analyze_music_industry(IndustryStructure.MAJOR_LABELS),
            "independent": self.analyze_music_industry(IndustryStructure.INDEPENDENT),
            "diy": self.analyze_music_industry(IndustryStructure.DIY)
        }
        
        # Hollywood
        results["hollywood"] = {
            "major": self.analyze_hollywood(IndustryStructure.MAJOR_LABELS),
            "independent": self.analyze_hollywood(IndustryStructure.INDEPENDENT),
            "diy": self.analyze_hollywood(IndustryStructure.DIY)
        }
        
        # Sports
        results["sports"] = {
            "major": self.analyze_sports(IndustryStructure.MAJOR_LABELS),
            "independent": self.analyze_sports(IndustryStructure.INDEPENDENT),
            "diy": self.analyze_sports(IndustryStructure.DIY)
        }
        
        # Live Events
        results["live_events"] = {
            "major": self.analyze_live_events(IndustryStructure.MAJOR_LABELS),
            "independent": self.analyze_live_events(IndustryStructure.INDEPENDENT),
            "diy": self.analyze_live_events(IndustryStructure.DIY)
        }
        
        # Shady Business (necessary but problematic)
        results["shady_business"] = {
            "major": self.analyze_shady_business(IndustryStructure.MAJOR_LABELS),
            "independent": self.analyze_shady_business(IndustryStructure.INDEPENDENT),
            "diy": self.analyze_shady_business(IndustryStructure.DIY)
        }
        
        # TV/Pay-Per-View
        results["tv_pay_per_view"] = {
            "major": self.analyze_tv_pay_per_view(IndustryStructure.MAJOR_LABELS),
            "independent": self.analyze_tv_pay_per_view(IndustryStructure.INDEPENDENT),
            "diy": self.analyze_tv_pay_per_view(IndustryStructure.DIY)
        }
        
        # News Media
        results["news_media"] = {
            "major": self.analyze_news_media(IndustryStructure.MAJOR_LABELS),
            "independent": self.analyze_news_media(IndustryStructure.INDEPENDENT),
            "diy": self.analyze_news_media(IndustryStructure.DIY)
        }
        
        # Global Economics
        results["global_economics"] = {
            "major": self.analyze_global_economics(IndustryStructure.MAJOR_LABELS),
            "independent": self.analyze_global_economics(IndustryStructure.INDEPENDENT),
            "diy": self.analyze_global_economics(IndustryStructure.DIY)
        }
        
        # Finance
        results["finance"] = {
            "major": self.analyze_finance(IndustryStructure.MAJOR_LABELS),
            "independent": self.analyze_finance(IndustryStructure.INDEPENDENT),
            "diy": self.analyze_finance(IndustryStructure.DIY)
        }
        
        # Summary
        all_diy_scores = [
            results["music_industry"]["diy"].symbiosis_score,
            results["hollywood"]["diy"].symbiosis_score,
            results["sports"]["diy"].symbiosis_score,
            results["tv_pay_per_view"]["diy"].symbiosis_score,
            results["news_media"]["diy"].symbiosis_score,
            results["global_economics"]["diy"].symbiosis_score,
            results["finance"]["diy"].symbiosis_score,
            results["live_events"]["diy"].symbiosis_score,
            results["shady_business"]["diy"].symbiosis_score
        ]
        
        all_major_scores = [
            results["music_industry"]["major"].symbiosis_score,
            results["hollywood"]["major"].symbiosis_score,
            results["sports"]["major"].symbiosis_score,
            results["tv_pay_per_view"]["major"].symbiosis_score,
            results["news_media"]["major"].symbiosis_score,
            results["global_economics"]["major"].symbiosis_score,
            results["finance"]["major"].symbiosis_score,
            results["live_events"]["major"].symbiosis_score,
            results["shady_business"]["major"].symbiosis_score
        ]
        
        return {
            "industries": results,
            "summary": {
                "average_diy_symbiosis": sum(all_diy_scores) / len(all_diy_scores),
                "average_major_symbiosis": sum(all_major_scores) / len(all_major_scores),
                "best_structure": "DIY - Average symbiosis: {:.1f}/100".format(sum(all_diy_scores) / len(all_diy_scores)),
                "worst_structure": "Major - Average symbiosis: {:.1f}/100".format(sum(all_major_scores) / len(all_major_scores)),
                "recommendation": "DIY structure across all industries for mission alignment"
            }
        }
    
    def compare_industries(self) -> Dict[str, Any]:
        """Compare Hollywood and Music Industry through mission lens"""
        music_major = self.analyze_music_industry(IndustryStructure.MAJOR_LABELS)
        music_indie = self.analyze_music_industry(IndustryStructure.INDEPENDENT)
        music_diy = self.analyze_music_industry(IndustryStructure.DIY)
        
        hollywood_major = self.analyze_hollywood(IndustryStructure.MAJOR_LABELS)
        hollywood_indie = self.analyze_hollywood(IndustryStructure.INDEPENDENT)
        hollywood_diy = self.analyze_hollywood(IndustryStructure.DIY)
        
        return {
            "music_industry": {
                "major_labels": {
                    "symbiosis_score": music_major.symbiosis_score,
                    "serves_mission": music_major.serves_mission,
                    "honors_song": music_major.honors_song,
                    "right_spirits": music_major.right_spirits_present
                },
                "independent": {
                    "symbiosis_score": music_indie.symbiosis_score,
                    "serves_mission": music_indie.serves_mission,
                    "honors_song": music_indie.honors_song,
                    "right_spirits": music_indie.right_spirits_present
                },
                "diy": {
                    "symbiosis_score": music_diy.symbiosis_score,
                    "serves_mission": music_diy.serves_mission,
                    "honors_song": music_diy.honors_song,
                    "right_spirits": music_diy.right_spirits_present
                }
            },
            "hollywood": {
                "major_studios": {
                    "symbiosis_score": hollywood_major.symbiosis_score,
                    "serves_mission": hollywood_major.serves_mission,
                    "honors_creative": hollywood_major.honors_song,
                    "right_spirits": hollywood_major.right_spirits_present
                },
                "independent": {
                    "symbiosis_score": hollywood_indie.symbiosis_score,
                    "serves_mission": hollywood_indie.serves_mission,
                    "honors_creative": hollywood_indie.honors_song,
                    "right_spirits": hollywood_indie.right_spirits_present
                },
                "diy": {
                    "symbiosis_score": hollywood_diy.symbiosis_score,
                    "serves_mission": hollywood_diy.serves_mission,
                    "honors_creative": hollywood_diy.honors_song,
                    "right_spirits": hollywood_diy.right_spirits_present
                }
            },
            "recommendation": {
                "best_for_mission": "DIY structure in both industries",
                "reason": "Full control, direct community connection, right spirits flow freely",
                "principle": "Song/message serves mission. Mission honors song. They flow together."
            }
        }


# Singleton instance
_industry_explorer = None

def get_industry_explorer() -> HollywoodMusicIndustryExplorer:
    """Get singleton instance of HollywoodMusicIndustryExplorer"""
    global _industry_explorer
    if _industry_explorer is None:
        _industry_explorer = HollywoodMusicIndustryExplorer()
    return _industry_explorer


__all__ = [
    "HollywoodMusicIndustryExplorer",
    "IndustryType",
    "IndustryStructure",
    "SpiritualBattleType",
    "IndustryAnalysis",
    "get_industry_explorer"
]
