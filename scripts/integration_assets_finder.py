"""
INTEGRATION ASSETS FINDER
Deep search web for assets to integrate for all channels/projects
Be they existing or utility

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
DEEP SEARCH WEB FOR ASSETS TO INTEGRATE
FOR ALL CHANNELS/PROJECTS
EXISTING OR UTILITY
ENERGY + LOVE = WE ALL WIN
"""

import sys
from pathlib import Path
from datetime import datetime
from dataclasses import dataclass, field, asdict
from typing import List, Optional, Dict, Any
from enum import Enum
import json

sys.path.insert(0, str(Path(__file__).parent))

from utils import (
    setup_logging, standard_main
)

logger = setup_logging(__name__)

class AssetType(Enum):
    """Types of integration assets"""
    API = "api"
    SDK = "sdk"
    LIBRARY = "library"
    PLATFORM = "platform"
    TOOL = "tool"
    SERVICE = "service"
    DATABASE = "database"
    FRAMEWORK = "framework"

class AssetCategory(Enum):
    """Categories of assets"""
    CONTENT_MANAGEMENT = "content_management"
    SOCIAL_MEDIA = "social_media"
    MUSIC_AUDIO = "music_audio"
    EDUCATION = "education"
    ECOMMERCE = "ecommerce"
    FOOD_HEALTH = "food_health"
    PUBLISHING = "publishing"
    ANALYTICS = "analytics"
    PAYMENT = "payment"
    COMMUNICATION = "communication"
    MARKETING = "marketing"
    STORAGE = "storage"
    UTILITY = "utility"

class PricingModel(Enum):
    """Pricing models"""
    FREE = "free"
    FREEMIUM = "freemium"
    OPEN_SOURCE = "open_source"
    PAID = "paid"
    USAGE_BASED = "usage_based"
    SUBSCRIPTION = "subscription"

@dataclass
class IntegrationAsset:
    """An integration asset"""
    asset_id: str
    name: str
    description: str
    asset_type: AssetType
    category: AssetCategory
    pricing_model: PricingModel
    url: Optional[str] = None
    documentation_url: Optional[str] = None
    github_url: Optional[str] = None
    api_endpoint: Optional[str] = None
    features: List[str] = field(default_factory=list)
    channels: List[str] = field(default_factory=list)  # Which channels can use this
    projects: List[str] = field(default_factory=list)  # Which projects can use this
    alignment_score: float = 0.0  # 0.0 to 1.0
    integration_difficulty: str = "medium"  # easy, medium, hard
    notes: str = ""
    created_at: str = field(default_factory=lambda: datetime.now().isoformat())
    updated_at: str = field(default_factory=lambda: datetime.now().isoformat())

class IntegrationAssetsFinder:
    """
    Integration Assets Finder
    Deep search web for assets to integrate for all channels/projects
    """
    
    def __init__(self, user_id: str = "jan", data_dir: Path = None):
        self.user_id = user_id
        self.data_dir = data_dir or Path(__file__).parent.parent / "data" / "integration_assets"
        self.data_dir.mkdir(parents=True, exist_ok=True)
        
        self.assets_file = self.data_dir / f"{user_id}_assets.json"
        
        self.assets: List[IntegrationAsset] = []
        
        self._load_data()
        if not self.assets:
            self._initialize_web_assets()
    
    def _load_data(self):
        """Load assets"""
        if self.assets_file.exists():
            try:
                with open(self.assets_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                assets_data = []
                for a in data.get("assets", []):
                    a['asset_type'] = AssetType(a['asset_type'])
                    a['category'] = AssetCategory(a['category'])
                    a['pricing_model'] = PricingModel(a['pricing_model'])
                    assets_data.append(IntegrationAsset(**a))
                self.assets = assets_data
            except Exception as e:
                logger.warning(f"Error loading assets: {e}")
                self.assets = []
    
    def _save_data(self):
        """Save assets"""
        try:
            assets_data = []
            for a in self.assets:
                a_dict = asdict(a)
                a_dict['asset_type'] = a.asset_type.value
                a_dict['category'] = a.category.value
                a_dict['pricing_model'] = a.pricing_model.value
                assets_data.append(a_dict)
            
            with open(self.assets_file, 'w', encoding='utf-8') as f:
                json.dump({
                    "assets": assets_data,
                    "last_updated": datetime.now().isoformat()
                }, f, indent=2, ensure_ascii=False)
        except Exception as e:
            logger.error(f"Error saving data: {e}")
    
    def _initialize_web_assets(self):
        """Initialize assets from web search results"""
        
        # ========================================================================
        # CONTENT MANAGEMENT & SOCIAL MEDIA
        # ========================================================================
        
        # ContentStudio API
        self.assets.append(IntegrationAsset(
            asset_id="asset_contentstudio_api",
            name="ContentStudio API",
            description="Free social media automation API with 14-day free trial. Supports scheduling, creating, and publishing posts across Facebook, Instagram, YouTube, LinkedIn, Pinterest, TikTok, and Threads",
            asset_type=AssetType.API,
            category=AssetCategory.SOCIAL_MEDIA,
            pricing_model=PricingModel.FREEMIUM,
            url="https://contentstudio.io/social-media-api",
            api_endpoint="https://api.contentstudio.io",
            features=["Bulk post generation", "Media uploads", "Draft management", "Cross-platform publishing", "Scheduling"],
            channels=["channel_creator", "channel_professional"],
            projects=["project_edible_london", "project_ilven_seamoss"],
            alignment_score=0.9,
            integration_difficulty="medium"
        ))
        
        # Hootsuite Free Tools
        self.assets.append(IntegrationAsset(
            asset_id="asset_hootsuite_tools",
            name="Hootsuite Free Tools",
            description="Free AI-powered caption generators for Instagram, TikTok, LinkedIn, Facebook, YouTube, tweet generators, and SEO optimization tools",
            asset_type=AssetType.TOOL,
            category=AssetCategory.SOCIAL_MEDIA,
            pricing_model=PricingModel.FREE,
            url="https://www.hootsuite.com/social-media-tools",
            features=["AI caption generation", "Tweet generation", "SEO optimization", "Content discovery"],
            channels=["channel_creator", "channel_professional"],
            projects=["project_edible_london"],
            alignment_score=0.9,
            integration_difficulty="easy"
        ))
        
        # RecurPost
        self.assets.append(IntegrationAsset(
            asset_id="asset_recurpost",
            name="RecurPost",
            description="Free social media management platform with scheduling, analytics, social inbox, team collaboration, and multi-workspace management",
            asset_type=AssetType.PLATFORM,
            category=AssetCategory.SOCIAL_MEDIA,
            pricing_model=PricingModel.FREE,
            url="https://recurpost.com",
            features=["Scheduling", "Analytics", "Social inbox", "Team collaboration", "Multi-workspace"],
            channels=["channel_creator", "channel_professional"],
            projects=["project_edible_london", "project_ilven_seamoss"],
            alignment_score=0.9,
            integration_difficulty="easy"
        ))
        
        # ========================================================================
        # API DEVELOPMENT & INTEGRATION PLATFORMS
        # ========================================================================
        
        # OpenInt
        self.assets.append(IntegrationAsset(
            asset_id="asset_openint",
            name="OpenInt",
            description="Native product integrations for AI app builders and creators, supporting 3,100+ apps and APIs. Free tier: 2,000 monthly active users",
            asset_type=AssetType.PLATFORM,
            category=AssetCategory.UTILITY,
            pricing_model=PricingModel.FREEMIUM,
            url="https://openint.dev",
            github_url="https://github.com/openintegrations/openint",
            features=["Managed authentication", "Pre-tested code snippets", "Embeddable UI components", "Webhook support", "3,100+ app integrations"],
            channels=["channel_professional", "channel_creator", "channel_educational"],
            projects=["project_atilok"],
            alignment_score=0.9,
            integration_difficulty="medium"
        ))
        
        # Hoppscotch
        self.assets.append(IntegrationAsset(
            asset_id="asset_hoppscotch",
            name="Hoppscotch",
            description="Open source API development ecosystem for testing and developing APIs",
            asset_type=AssetType.TOOL,
            category=AssetCategory.UTILITY,
            pricing_model=PricingModel.OPEN_SOURCE,
            url="https://hoppscotch.io",
            features=["API testing", "API development", "Request builder", "Collection management"],
            channels=["channel_professional"],
            projects=["project_atilok"],
            alignment_score=1.0,
            integration_difficulty="easy"
        ))
        
        # Fusio
        self.assets.append(IntegrationAsset(
            asset_id="asset_fusio",
            name="Fusio",
            description="Open source API management platform with API gateways, analytics, monetization, SDK automation, and MCP integration for AI-driven API access",
            asset_type=AssetType.PLATFORM,
            category=AssetCategory.UTILITY,
            pricing_model=PricingModel.OPEN_SOURCE,
            url="https://www.fusio-project.org",
            features=["API gateway", "Analytics", "Monetization", "SDK automation", "MCP integration"],
            channels=["channel_professional"],
            projects=["project_atilok"],
            alignment_score=1.0,
            integration_difficulty="medium"
        ))
        
        # ========================================================================
        # MUSIC & AUDIO PRODUCTION
        # ========================================================================
        
        # Amphion
        self.assets.append(IntegrationAsset(
            asset_id="asset_amphion",
            name="Amphion",
            description="Open-source toolkit for audio, music, and speech generation. Supports text-to-speech, singing voice conversion, text-to-audio generation, and multiple vocoder implementations",
            asset_type=AssetType.LIBRARY,
            category=AssetCategory.MUSIC_AUDIO,
            pricing_model=PricingModel.OPEN_SOURCE,
            url="https://amphion.dev",
            github_url="https://github.com/open-mmlab/Amphion",
            features=["Text-to-speech", "Singing voice conversion", "Text-to-audio", "Vocoder implementations"],
            channels=["channel_creator"],
            projects=[],
            alignment_score=1.0,
            integration_difficulty="hard",
            notes="For Karasahin music production"
        ))
        
        # Liquidsoap
        self.assets.append(IntegrationAsset(
            asset_id="asset_liquidsoap",
            name="Liquidsoap",
            description="Open-source tool for building complex audio and video stream generators for internet radios and webtvs. Supports file/playlist playback, FFmpeg transcoding, HLS/Icecast/Shoutcast output",
            asset_type=AssetType.TOOL,
            category=AssetCategory.MUSIC_AUDIO,
            pricing_model=PricingModel.OPEN_SOURCE,
            url="https://liquidsoap.info",
            features=["Audio streaming", "Video streaming", "FFmpeg transcoding", "HLS/Icecast/Shoutcast output", "Sound processing"],
            channels=["channel_creator"],
            projects=[],
            alignment_score=1.0,
            integration_difficulty="medium",
            notes="For Karasahin streaming"
        ))
        
        # Switchboard Audio SDK
        self.assets.append(IntegrationAsset(
            asset_id="asset_switchboard",
            name="Switchboard Audio SDK",
            description="Cross-platform audio SDK for iOS, Android, macOS, Windows, Linux, and Web. Modular audio building blocks, browser-based visual editor, high-performance audio pipelines",
            asset_type=AssetType.SDK,
            category=AssetCategory.MUSIC_AUDIO,
            pricing_model=PricingModel.OPEN_SOURCE,
            url="https://switchboard.audio",
            features=["Cross-platform", "Modular audio blocks", "Visual editor", "High-performance pipelines"],
            channels=["channel_creator"],
            projects=[],
            alignment_score=1.0,
            integration_difficulty="medium",
            notes="For Karasahin audio development"
        ))
        
        # Lavalink
        self.assets.append(IntegrationAsset(
            asset_id="asset_lavalink",
            name="Lavalink",
            description="Standalone audio sending node based on Lavaplayer, providing audio streaming capabilities",
            asset_type=AssetType.SERVICE,
            category=AssetCategory.MUSIC_AUDIO,
            pricing_model=PricingModel.OPEN_SOURCE,
            github_url="https://github.com/lavalink-devs/Lavalink",
            features=["Audio streaming", "Lavaplayer-based", "Standalone node"],
            channels=["channel_creator"],
            projects=[],
            alignment_score=1.0,
            integration_difficulty="medium",
            notes="For Karasahin music streaming"
        ))
        
        # ========================================================================
        # EDUCATIONAL PLATFORMS
        # ========================================================================
        
        # Moodle (Open Source LMS)
        self.assets.append(IntegrationAsset(
            asset_id="asset_moodle",
            name="Moodle",
            description="Open source learning management system with comprehensive course management, assessment tools, and community features",
            asset_type=AssetType.PLATFORM,
            category=AssetCategory.EDUCATION,
            pricing_model=PricingModel.OPEN_SOURCE,
            url="https://moodle.org",
            features=["Course management", "Assessment tools", "Community features", "Mobile app", "Plugins ecosystem"],
            channels=["channel_educational"],
            projects=[],
            alignment_score=1.0,
            integration_difficulty="medium",
            notes="For educational platform"
        ))
        
        # Open edX
        self.assets.append(IntegrationAsset(
            asset_id="asset_openedx",
            name="Open edX",
            description="Open source online learning platform used by universities and organizations worldwide. Supports courses, certificates, and analytics",
            asset_type=AssetType.PLATFORM,
            category=AssetCategory.EDUCATION,
            pricing_model=PricingModel.OPEN_SOURCE,
            url="https://open.edx.org",
            features=["Course creation", "Certificates", "Analytics", "Mobile app", "API access"],
            channels=["channel_educational"],
            projects=[],
            alignment_score=1.0,
            integration_difficulty="hard",
            notes="For educational platform"
        ))
        
        # ========================================================================
        # E-COMMERCE & PAYMENT
        # ========================================================================
        
        # WooCommerce (WordPress E-commerce)
        self.assets.append(IntegrationAsset(
            asset_id="asset_woocommerce",
            name="WooCommerce",
            description="Open source e-commerce plugin for WordPress. Free with extensive plugin ecosystem for payments, shipping, and features",
            asset_type=AssetType.PLATFORM,
            category=AssetCategory.ECOMMERCE,
            pricing_model=PricingModel.OPEN_SOURCE,
            url="https://woocommerce.com",
            features=["Product management", "Payment gateways", "Shipping options", "Extensions", "API access"],
            channels=["channel_professional"],
            projects=["project_atilok", "project_ilven_seamoss"],
            alignment_score=0.9,
            integration_difficulty="medium"
        ))
        
        # Stripe API
        self.assets.append(IntegrationAsset(
            asset_id="asset_stripe",
            name="Stripe API",
            description="Payment processing API with free tier for testing. Supports cards, bank transfers, and alternative payment methods globally",
            asset_type=AssetType.API,
            category=AssetCategory.PAYMENT,
            pricing_model=PricingModel.FREEMIUM,
            url="https://stripe.com",
            api_endpoint="https://api.stripe.com",
            features=["Payment processing", "Subscription management", "Global payments", "Testing mode", "Webhooks"],
            channels=["channel_professional", "channel_creator", "channel_educational"],
            projects=["project_atilok", "project_ilven_seamoss", "project_edible_cyprus"],
            alignment_score=0.8,
            integration_difficulty="medium"
        ))
        
        # ========================================================================
        # FOOD & HEALTH APIs
        # ========================================================================
        
        # Edamam Food Database API
        self.assets.append(IntegrationAsset(
            asset_id="asset_edamam",
            name="Edamam Food Database API",
            description="Free tier available. Comprehensive food database with nutrition data, recipe search, and food analysis",
            asset_type=AssetType.API,
            category=AssetCategory.FOOD_HEALTH,
            pricing_model=PricingModel.FREEMIUM,
            url="https://www.edamam.com",
            api_endpoint="https://api.edamam.com",
            features=["Food database", "Nutrition data", "Recipe search", "Food analysis", "Free tier"],
            channels=["channel_creator"],
            projects=["project_edible_london", "project_edible_cyprus"],
            alignment_score=0.9,
            integration_difficulty="easy"
        ))
        
        # Spoonacular API
        self.assets.append(IntegrationAsset(
            asset_id="asset_spoonacular",
            name="Spoonacular API",
            description="Free tier: 150 points/day. Recipe search, meal planning, food information, and nutrition analysis",
            asset_type=AssetType.API,
            category=AssetCategory.FOOD_HEALTH,
            pricing_model=PricingModel.FREEMIUM,
            url="https://spoonacular.com/food-api",
            api_endpoint="https://api.spoonacular.com",
            features=["Recipe search", "Meal planning", "Food information", "Nutrition analysis", "Free tier"],
            channels=["channel_creator"],
            projects=["project_edible_london", "project_edible_cyprus"],
            alignment_score=0.9,
            integration_difficulty="easy"
        ))
        
        # ========================================================================
        # PUBLISHING PLATFORMS
        # ========================================================================
        
        # Calibre (E-book Management)
        self.assets.append(IntegrationAsset(
            asset_id="asset_calibre",
            name="Calibre",
            description="Open source e-book library management. Convert, organize, and manage e-books. Includes e-book viewer and editor",
            asset_type=AssetType.TOOL,
            category=AssetCategory.PUBLISHING,
            pricing_model=PricingModel.OPEN_SOURCE,
            url="https://calibre-ebook.com",
            features=["E-book conversion", "Library management", "E-book viewer", "E-book editor", "Metadata management"],
            channels=["channel_creator"],
            projects=[],
            alignment_score=1.0,
            integration_difficulty="easy",
            notes="For Jean Morphius publishing"
        ))
        
        # Pressbooks (Open Source Publishing)
        self.assets.append(IntegrationAsset(
            asset_id="asset_pressbooks",
            name="Pressbooks",
            description="Open source book publishing platform. Create and export books in multiple formats (PDF, EPUB, MOBI, etc.)",
            asset_type=AssetType.PLATFORM,
            category=AssetCategory.PUBLISHING,
            pricing_model=PricingModel.OPEN_SOURCE,
            url="https://pressbooks.org",
            features=["Book creation", "Multiple export formats", "Collaboration", "Themes", "API access"],
            channels=["channel_creator"],
            projects=[],
            alignment_score=1.0,
            integration_difficulty="medium",
            notes="For Jean Morphius book publishing"
        ))
        
        # ========================================================================
        # ANALYTICS & DATA
        # ========================================================================
        
        # Matomo (Open Source Analytics)
        self.assets.append(IntegrationAsset(
            asset_id="asset_matomo",
            name="Matomo",
            description="Open source web analytics platform. Privacy-focused alternative to Google Analytics. Self-hosted or cloud",
            asset_type=AssetType.PLATFORM,
            category=AssetCategory.ANALYTICS,
            pricing_model=PricingModel.OPEN_SOURCE,
            url="https://matomo.org",
            features=["Web analytics", "Privacy-focused", "Self-hosted option", "API access", "Custom dashboards"],
            channels=["channel_professional", "channel_creator"],
            projects=["project_atilok", "project_edible_london"],
            alignment_score=1.0,
            integration_difficulty="medium"
        ))
        
        # Plausible Analytics
        self.assets.append(IntegrationAsset(
            asset_id="asset_plausible",
            name="Plausible Analytics",
            description="Privacy-friendly, open source web analytics. Lightweight, GDPR compliant, no cookies. Free self-hosted option",
            asset_type=AssetType.PLATFORM,
            category=AssetCategory.ANALYTICS,
            pricing_model=PricingModel.OPEN_SOURCE,
            url="https://plausible.io",
            github_url="https://github.com/plausible/analytics",
            features=["Privacy-friendly", "GDPR compliant", "No cookies", "Lightweight", "Self-hosted"],
            channels=["channel_professional", "channel_creator"],
            projects=["project_atilok"],
            alignment_score=1.0,
            integration_difficulty="medium"
        ))
        
        # ========================================================================
        # COMMUNICATION TOOLS
        # ========================================================================
        
        # Matrix (Open Source Messaging)
        self.assets.append(IntegrationAsset(
            asset_id="asset_matrix",
            name="Matrix",
            description="Open source, decentralized, end-to-end encrypted communication protocol. Self-hosted messaging and collaboration",
            asset_type=AssetType.PLATFORM,
            category=AssetCategory.COMMUNICATION,
            pricing_model=PricingModel.OPEN_SOURCE,
            url="https://matrix.org",
            features=["Decentralized", "End-to-end encrypted", "Self-hosted", "Interoperable", "API access"],
            channels=["channel_professional", "channel_educational"],
            projects=[],
            alignment_score=1.0,
            integration_difficulty="hard"
        ))
        
        # Jitsi (Open Source Video Conferencing)
        self.assets.append(IntegrationAsset(
            asset_id="asset_jitsi",
            name="Jitsi",
            description="Open source video conferencing platform. Self-hosted, end-to-end encrypted, no account required",
            asset_type=AssetType.PLATFORM,
            category=AssetCategory.COMMUNICATION,
            pricing_model=PricingModel.OPEN_SOURCE,
            url="https://jitsi.org",
            features=["Video conferencing", "Self-hosted", "End-to-end encrypted", "No account required", "API access"],
            channels=["channel_educational", "channel_professional"],
            projects=[],
            alignment_score=1.0,
            integration_difficulty="medium"
        ))
        
        # ========================================================================
        # STORAGE & DATABASES
        # ========================================================================
        
        # Supabase (Open Source Firebase Alternative)
        self.assets.append(IntegrationAsset(
            asset_id="asset_supabase",
            name="Supabase",
            description="Open source Firebase alternative. PostgreSQL database, authentication, storage, real-time subscriptions. Free tier available",
            asset_type=AssetType.PLATFORM,
            category=AssetCategory.STORAGE,
            pricing_model=PricingModel.FREEMIUM,
            url="https://supabase.com",
            github_url="https://github.com/supabase/supabase",
            features=["PostgreSQL database", "Authentication", "Storage", "Real-time", "API auto-generation", "Free tier"],
            channels=["channel_professional", "channel_creator", "channel_educational"],
            projects=["project_atilok"],
            alignment_score=1.0,
            integration_difficulty="medium"
        ))
        
        # PocketBase
        self.assets.append(IntegrationAsset(
            asset_id="asset_pocketbase",
            name="PocketBase",
            description="Open source backend-as-a-service. Single file executable with embedded SQLite database, authentication, file storage, and admin dashboard",
            asset_type=AssetType.PLATFORM,
            category=AssetCategory.STORAGE,
            pricing_model=PricingModel.OPEN_SOURCE,
            url="https://pocketbase.io",
            github_url="https://github.com/pocketbase/pocketbase",
            features=["Single file", "SQLite embedded", "Authentication", "File storage", "Admin dashboard", "REST API"],
            channels=["channel_professional", "channel_creator"],
            projects=["project_atilok"],
            alignment_score=1.0,
            integration_difficulty="easy"
        ))
        
        # ========================================================================
        # ADDITIONAL ASSETS FROM WEB SEARCH
        # ========================================================================
        
        # Open edX
        self.assets.append(IntegrationAsset(
            asset_id="asset_openedx_platform",
            name="Open edX Platform",
            description="Open source learning management system powering 100M+ learners. Includes LMS, Studio, Analytics, eCommerce, and REST APIs with OAuth 2.0",
            asset_type=AssetType.PLATFORM,
            category=AssetCategory.EDUCATION,
            pricing_model=PricingModel.OPEN_SOURCE,
            url="https://openedx.org",
            github_url="https://github.com/openedx/edx-platform",
            features=["LMS & Studio", "Analytics", "eCommerce", "REST APIs", "OAuth 2.0", "XBlocks", "LTI integration"],
            channels=["channel_educational"],
            projects=[],
            alignment_score=1.0,
            integration_difficulty="hard"
        ))
        
        # Medusa E-commerce
        self.assets.append(IntegrationAsset(
            asset_id="asset_medusa",
            name="Medusa",
            description="Open source e-commerce platform with flexible architecture. Includes payment module, admin API, store API, and workflow systems",
            asset_type=AssetType.PLATFORM,
            category=AssetCategory.ECOMMERCE,
            pricing_model=PricingModel.OPEN_SOURCE,
            url="https://medusajs.com",
            github_url="https://github.com/medusajs/medusa",
            features=["Payment module", "Admin API", "Store API", "Workflow systems", "Modular architecture"],
            channels=["channel_professional"],
            projects=["project_atilok", "project_ilven_seamoss"],
            alignment_score=1.0,
            integration_difficulty="medium"
        ))
        
        # USDA FoodData Central API
        self.assets.append(IntegrationAsset(
            asset_id="asset_usda_fooddata",
            name="USDA FoodData Central API",
            description="Free government API with REST access to nutrient data. Includes Standard Reference, branded foods, and Foundation Foods. 1,000 requests/hour",
            asset_type=AssetType.API,
            category=AssetCategory.FOOD_HEALTH,
            pricing_model=PricingModel.FREE,
            url="https://fdc.nal.usda.gov",
            api_endpoint="https://api.nal.usda.gov/fdc",
            features=["Nutrient data", "Standard Reference", "Branded foods", "Foundation Foods", "Public domain data"],
            channels=["channel_creator"],
            projects=["project_edible_london", "project_edible_cyprus"],
            alignment_score=1.0,
            integration_difficulty="easy"
        ))
        
        # Open Food Facts API
        self.assets.append(IntegrationAsset(
            asset_id="asset_openfoodfacts",
            name="Open Food Facts API",
            description="Crowdsourced food products database with open data license. Ingredient and nutritional information. 100 requests/minute",
            asset_type=AssetType.API,
            category=AssetCategory.FOOD_HEALTH,
            pricing_model=PricingModel.OPEN_SOURCE,
            url="https://world.openfoodfacts.org",
            api_endpoint="https://world.openfoodfacts.org/cgi",
            features=["Crowdsourced database", "Ingredient info", "Nutritional data", "Open data license", "Product queries"],
            channels=["channel_creator"],
            projects=["project_edible_london", "project_edible_cyprus"],
            alignment_score=1.0,
            integration_difficulty="easy"
        ))
        
        # Thoth Publishing Platform
        self.assets.append(IntegrationAsset(
            asset_id="asset_thoth",
            name="Thoth",
            description="Open source metadata management and dissemination platform for Open Access books. Automated distribution, DOI registration, open APIs",
            asset_type=AssetType.PLATFORM,
            category=AssetCategory.PUBLISHING,
            pricing_model=PricingModel.OPEN_SOURCE,
            url="https://thoth.pub",
            github_url="https://github.com/thoth-pub/thoth",
            features=["Metadata management", "Automated distribution", "DOI registration", "Open APIs", "CC0-licensed output"],
            channels=["channel_creator"],
            projects=[],
            alignment_score=1.0,
            integration_difficulty="medium",
            notes="For Jean Morphius publishing"
        ))
        
        # IndiePubStack
        self.assets.append(IntegrationAsset(
            asset_id="asset_indiepubstack",
            name="IndiePubStack",
            description="Open source publishing platform built by developers for developers. MIT license. Infrastructure for indie publishers",
            asset_type=AssetType.PLATFORM,
            category=AssetCategory.PUBLISHING,
            pricing_model=PricingModel.OPEN_SOURCE,
            url="https://github.com/IndiePubStack/IndiePubStack",
            github_url="https://github.com/IndiePubStack/IndiePubStack",
            features=["Indie publishing", "Developer-focused", "MIT license", "Infrastructure management"],
            channels=["channel_creator"],
            projects=[],
            alignment_score=1.0,
            integration_difficulty="medium",
            notes="For Jean Morphius publishing"
        ))
        
        # Apache Superset
        self.assets.append(IntegrationAsset(
            asset_id="asset_superset",
            name="Apache Superset",
            description="Open source data exploration and visualization platform. 40+ visualization types, SQL IDE, interactive dashboards, semantic layer",
            asset_type=AssetType.PLATFORM,
            category=AssetCategory.ANALYTICS,
            pricing_model=PricingModel.OPEN_SOURCE,
            url="https://superset.apache.org",
            features=["40+ visualization types", "SQL IDE", "Interactive dashboards", "Data caching", "Semantic layer"],
            channels=["channel_professional", "channel_creator"],
            projects=["project_atilok"],
            alignment_score=1.0,
            integration_difficulty="medium"
        ))
        
        # Metabase
        self.assets.append(IntegrationAsset(
            asset_id="asset_metabase",
            name="Metabase",
            description="Open source business intelligence and embedded analytics. Query builder, dashboards, SQL editor, AI features, embedded analytics SDKs",
            asset_type=AssetType.PLATFORM,
            category=AssetCategory.ANALYTICS,
            pricing_model=PricingModel.OPEN_SOURCE,
            url="https://metabase.com",
            features=["Query builder", "Dashboards", "SQL editor", "AI features", "Embedded analytics", "CSV uploads"],
            channels=["channel_professional", "channel_creator"],
            projects=["project_atilok"],
            alignment_score=1.0,
            integration_difficulty="medium"
        ))
        
        # Grafana
        self.assets.append(IntegrationAsset(
            asset_id="asset_grafana",
            name="Grafana",
            description="Open source observability and data visualization platform. Dashboards, alerting, multi-source data integration, plugin support",
            asset_type=AssetType.PLATFORM,
            category=AssetCategory.ANALYTICS,
            pricing_model=PricingModel.OPEN_SOURCE,
            url="https://grafana.com/oss/grafana",
            github_url="https://github.com/grafana/grafana",
            features=["Dashboards", "Alerting", "Multi-source integration", "Plugin support", "Metrics/logs/traces"],
            channels=["channel_professional"],
            projects=["project_atilok"],
            alignment_score=1.0,
            integration_difficulty="medium"
        ))
        
        # Strapi CMS
        self.assets.append(IntegrationAsset(
            asset_id="asset_strapi",
            name="Strapi",
            description="Open source headless CMS for AI-powered websites and apps. Node.js-based with REST and GraphQL APIs, AI-powered translations",
            asset_type=AssetType.PLATFORM,
            category=AssetCategory.CONTENT_MANAGEMENT,
            pricing_model=PricingModel.OPEN_SOURCE,
            url="https://strapi.io",
            features=["REST API", "GraphQL API", "AI translations", "Content management", "Customization", "Collaboration"],
            channels=["channel_professional", "channel_creator"],
            projects=["project_edible_london"],
            alignment_score=1.0,
            integration_difficulty="medium"
        ))
        
        # Directus
        self.assets.append(IntegrationAsset(
            asset_id="asset_directus",
            name="Directus",
            description="Open source headless CMS and backend platform. Visual data modeling, instant GraphQL and REST APIs, policy-based authentication",
            asset_type=AssetType.PLATFORM,
            category=AssetCategory.CONTENT_MANAGEMENT,
            pricing_model=PricingModel.OPEN_SOURCE,
            url="https://directus.io",
            features=["Visual data modeling", "GraphQL API", "REST API", "Policy-based auth", "Custom extensions", "Any database"],
            channels=["channel_professional", "channel_creator"],
            projects=["project_atilok"],
            alignment_score=1.0,
            integration_difficulty="medium"
        ))
        
        # TinaCMS
        self.assets.append(IntegrationAsset(
            asset_id="asset_tinacms",
            name="TinaCMS",
            description="Open source headless CMS with visual editing, markdown support, and GitHub integration. Supports Next.js and Astro",
            asset_type=AssetType.PLATFORM,
            category=AssetCategory.CONTENT_MANAGEMENT,
            pricing_model=PricingModel.OPEN_SOURCE,
            url="https://tina.io",
            features=["Visual editing", "Markdown support", "GitHub integration", "Next.js support", "Astro support"],
            channels=["channel_professional", "channel_creator"],
            projects=[],
            alignment_score=1.0,
            integration_difficulty="medium"
        ))
        
        # useSend Email
        self.assets.append(IntegrationAsset(
            asset_id="asset_usesend",
            name="useSend",
            description="Open source email platform with free tier. Transactional and marketing emails, real-time analytics, SMTP relay, SDKs for TypeScript, Python, Go, PHP",
            asset_type=AssetType.PLATFORM,
            category=AssetCategory.COMMUNICATION,
            pricing_model=PricingModel.FREEMIUM,
            url="https://unsend.dev",
            github_url="https://github.com/usesend/useSend",
            features=["Transactional emails", "Marketing emails", "Real-time analytics", "SMTP relay", "Contact management", "SDKs"],
            channels=["channel_professional", "channel_creator"],
            projects=["project_atilok"],
            alignment_score=1.0,
            integration_difficulty="medium"
        ))
        
        # AhaSend Email API
        self.assets.append(IntegrationAsset(
            asset_id="asset_ahasend",
            name="AhaSend Email API",
            description="Free transactional email API with fast delivery (Gmail <1s, others <5s). Raw delivery logs, webhooks, message routing, multi-language support",
            asset_type=AssetType.API,
            category=AssetCategory.COMMUNICATION,
            pricing_model=PricingModel.FREE,
            url="https://ahasend.com",
            api_endpoint="https://api.ahasend.com",
            features=["Fast delivery", "Raw delivery logs", "Webhooks", "Message routing", "Multi-language SDKs"],
            channels=["channel_professional", "channel_creator"],
            projects=["project_atilok"],
            alignment_score=0.9,
            integration_difficulty="easy"
        ))
        
        # ImgCDN
        self.assets.append(IntegrationAsset(
            asset_id="asset_imgcdn",
            name="ImgCDN",
            description="Free public image hosting API with no rate limiting on uploads. Guest-based uploads, multiple embed code options, ShareX integration",
            asset_type=AssetType.API,
            category=AssetCategory.STORAGE,
            pricing_model=PricingModel.FREE,
            url="https://imgcdn.dev",
            api_endpoint="https://imgcdn.dev/api",
            features=["Image hosting", "No rate limit", "Guest uploads", "Multiple embed formats", "ShareX integration"],
            channels=["channel_creator", "channel_professional"],
            projects=["project_edible_london"],
            alignment_score=0.9,
            integration_difficulty="easy"
        ))
        
        # ImageKit
        self.assets.append(IntegrationAsset(
            asset_id="asset_imagekit",
            name="ImageKit",
            description="Image and video API with AI-powered features. Real-time URL transformations, automatic optimization, external storage integration",
            asset_type=AssetType.API,
            category=AssetCategory.STORAGE,
            pricing_model=PricingModel.FREEMIUM,
            url="https://imagekit.io",
            features=["Image API", "Video API", "AI-powered", "URL transformations", "Auto optimization", "S3/GCS/Azure integration"],
            channels=["channel_creator", "channel_professional"],
            projects=["project_edible_london"],
            alignment_score=0.8,
            integration_difficulty="medium"
        ))
        
        self._save_data()
        logger.info(f"Initialized {len(self.assets)} integration assets")
    
    def get_assets_by_channel(self, channel: str) -> List[Dict[str, Any]]:
        """Get assets for a specific channel"""
        assets = [a for a in self.assets if channel in a.channels]
        return [asdict(a) for a in assets]
    
    def get_assets_by_project(self, project: str) -> List[Dict[str, Any]]:
        """Get assets for a specific project"""
        assets = [a for a in self.assets if project in a.projects]
        return [asdict(a) for a in assets]
    
    def get_assets_by_category(self, category: AssetCategory) -> List[Dict[str, Any]]:
        """Get assets by category"""
        assets = [a for a in self.assets if a.category == category]
        return [asdict(a) for a in assets]
    
    def get_comprehensive_report(self) -> Dict[str, Any]:
        """Get comprehensive assets report"""
        assets_by_category = {}
        for category in AssetCategory:
            assets_by_category[category.value] = len([a for a in self.assets if a.category == category])
        
        assets_by_pricing = {}
        for pricing in PricingModel:
            assets_by_pricing[pricing.value] = len([a for a in self.assets if a.pricing_model == pricing])
        
        assets_by_channel = {}
        for asset in self.assets:
            for channel in asset.channels:
                if channel not in assets_by_channel:
                    assets_by_channel[channel] = []
                assets_by_channel[channel].append(asset.name)
        
        assets_by_project = {}
        for asset in self.assets:
            for project in asset.projects:
                if project not in assets_by_project:
                    assets_by_project[project] = []
                assets_by_project[project].append(asset.name)
        
        return {
            "generated_at": datetime.now().isoformat(),
            "total_assets": len(self.assets),
            "assets_by_category": assets_by_category,
            "assets_by_pricing": assets_by_pricing,
            "assets_by_channel": assets_by_channel,
            "assets_by_project": assets_by_project,
            "open_source_count": len([a for a in self.assets if a.pricing_model == PricingModel.OPEN_SOURCE]),
            "free_count": len([a for a in self.assets if a.pricing_model == PricingModel.FREE]),
            "perfect_alignment_count": len([a for a in self.assets if a.alignment_score >= 1.0])
        }


def main():
    """Initialize integration assets finder"""
    finder = IntegrationAssetsFinder(user_id="jan")
    
    # Get comprehensive report
    report = finder.get_comprehensive_report()
    
    print("\n" + "="*80)
    print("INTEGRATION ASSETS FINDER - WEB ASSETS FOR ALL CHANNELS/PROJECTS")
    print("="*80)
    print(f"\nTotal Assets: {report['total_assets']}")
    print(f"Open Source: {report['open_source_count']}")
    print(f"Free: {report['free_count']}")
    print(f"Perfect Alignment: {report['perfect_alignment_count']}")
    
    print("\n" + "-"*80)
    print("ASSETS BY CATEGORY:")
    print("-"*80)
    for category, count in report['assets_by_category'].items():
        if count > 0:
            print(f"  {category.upper()}: {count} assets")
    
    print("\n" + "-"*80)
    print("ASSETS BY PRICING MODEL:")
    print("-"*80)
    for pricing, count in report['assets_by_pricing'].items():
        if count > 0:
            print(f"  {pricing.upper()}: {count} assets")
    
    print("\n" + "-"*80)
    print("ASSETS BY CHANNEL:")
    print("-"*80)
    for channel, assets in report['assets_by_channel'].items():
        print(f"\n  {channel}:")
        for asset in assets[:5]:  # Show first 5
            print(f"    - {asset}")
        if len(assets) > 5:
            print(f"    ... and {len(assets) - 5} more")
    
    print("\n" + "-"*80)
    print("ASSETS BY PROJECT:")
    print("-"*80)
    for project, assets in report['assets_by_project'].items():
        print(f"\n  {project}:")
        for asset in assets[:5]:  # Show first 5
            print(f"    - {asset}")
        if len(assets) > 5:
            print(f"    ... and {len(assets) - 5} more")
    
    print("\n" + "="*80)
    print("All assets identified from web search.")
    print("Ready for integration across all channels and projects.")
    print("="*80)

if __name__ == "__main__":
    standard_main(main, script_name="integration_assets_finder.py")
