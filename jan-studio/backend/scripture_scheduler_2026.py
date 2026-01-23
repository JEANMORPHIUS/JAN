"""
Scripture Scheduler for Edible London & ILVEN Sea Moss - 2026

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN

Generates scripture-based social media content scheduled throughout 2026
for both Edible London and ILVEN Sea Moss brands.
"""

import json
from datetime import datetime, timedelta, timezone
from typing import List, Dict, Optional
from dataclasses import dataclass, asdict
import random


@dataclass
class ScripturePost:
    """Scripture-based social media post with multi-format support"""
    title: str
    content: str
    scripture_reference: str
    scripture_text: str
    scheduled_time: datetime
    platform: str
    hashtags: List[str]
    brand: str  # All SIYEM entities
    metadata: Dict
    # Format support for delegation
    formats: Optional[List[str]] = None  # ['text_short', 'text_long', 'video', 'audio', 'image']
    primary_format: str = 'text_short'  # Default format
    format_notes: Optional[Dict] = None  # Format-specific instructions
    delegation_ready: bool = True  # Ready for format-specific generation
    
    def __post_init__(self):
        """Initialize default values for optional fields"""
        if self.formats is None:
            self.formats = ['text_short']
        if self.format_notes is None:
            self.format_notes = {}


class ScriptureScheduler:
    """Generates scripture-based content for 2026 scheduling - All SIYEM Entities"""
    
    # All supported entities
    ENTITIES = [
        'edible_london',
        'ilven_seamoss',
        'jean_mahram',
        'karasahin_jk',
        'pierre_pressure',
        'uncle_ray_ramiz',
        'siyem_media'
    ]
    
    # Scripture verses aligned with brand values
    SCRIPTURES = {
        'craft_work': [
            ("Proverbs 22:29", "Do you see a man skilled in his work? He will stand before kings; he will not stand before obscure men.", "Craft, excellence, skill"),
            ("Colossians 3:23", "Whatever you do, work heartily, as for the Lord and not for men.", "Work, heart, purpose"),
            ("Proverbs 14:23", "In all toil there is profit, but mere talk tends only to poverty.", "Graft, real work, action"),
            ("Ecclesiastes 9:10", "Whatever your hand finds to do, do it with your might.", "Diligence, effort, excellence"),
        ],
        'heart_purpose': [
            ("Proverbs 4:23", "Above all else, guard your heart, for everything you do flows from it.", "Heart first, purpose, intention"),
            ("Matthew 6:21", "For where your treasure is, there your heart will be also.", "Heart, values, priorities"),
            ("Jeremiah 29:11", "For I know the plans I have for you, declares the Lord, plans to prosper you and not to harm you, plans to give you hope and a future.", "Purpose, vision, hope"),
            ("Proverbs 16:3", "Commit to the Lord whatever you do, and he will establish your plans.", "Commitment, planning, faith"),
        ],
        'community_stewardship': [
            ("Galatians 6:2", "Carry each other's burdens, and in this way you will fulfill the law of Christ.", "Community, support, togetherness"),
            ("1 Peter 4:10", "Each of you should use whatever gift you have received to serve others, as faithful stewards of God's grace.", "Stewardship, service, gifts"),
            ("Hebrews 10:24-25", "And let us consider how we may spur one another on toward love and good deeds, not giving up meeting together.", "Community, encouragement, connection"),
            ("Proverbs 27:17", "As iron sharpens iron, so one person sharpens another.", "Community, growth, support"),
        ],
        'wisdom_tradition': [
            ("Proverbs 13:20", "Walk with the wise and become wise, for a companion of fools suffers harm.", "Wisdom, tradition, learning"),
            ("Proverbs 19:20", "Listen to advice and accept discipline, and at the end you will be counted among the wise.", "Wisdom, learning, humility"),
            ("Ecclesiastes 7:12", "Wisdom is a shelter as money is a shelter, but the advantage of knowledge is this: Wisdom preserves those who have it.", "Wisdom, protection, knowledge"),
            ("Proverbs 3:13-14", "Blessed are those who find wisdom, those who gain understanding, for she is more profitable than silver.", "Wisdom, value, understanding"),
        ],
        'faith_trust': [
            ("Proverbs 3:5-6", "Trust in the Lord with all your heart and lean not on your own understanding; in all your ways submit to him, and he will make your paths straight.", "Trust, faith, guidance"),
            ("Isaiah 41:10", "So do not fear, for I am with you; do not be dismayed, for I am your God. I will strengthen you and help you; I will uphold you with my righteous right hand.", "Faith, strength, support"),
            ("Matthew 17:20", "Truly I tell you, if you have faith as small as a mustard seed, you can say to this mountain, 'Move from here to there,' and it will move.", "Faith, possibility, transformation"),
            ("Philippians 4:13", "I can do all this through him who gives me strength.", "Strength, faith, capability"),
        ],
        'love_service': [
            ("1 Corinthians 16:14", "Do everything in love.", "Love, action, purpose"),
            ("John 13:35", "By this everyone will know that you are my disciples, if you love one another.", "Love, community, witness"),
            ("1 John 4:19", "We love because he first loved us.", "Love, origin, purpose"),
            ("Galatians 5:13", "Serve one another humbly in love.", "Service, love, humility"),
        ],
        'patience_process': [
            ("Ecclesiastes 3:1", "There is a time for everything, and a season for every activity under the heavens.", "Time, seasons, patience"),
            ("James 5:7", "Be patient, then, brothers and sisters, until the Lord's coming. See how the farmer waits for the land to yield its valuable crop, patiently waiting for the autumn and spring rains.", "Patience, process, waiting"),
            ("Proverbs 19:2", "Desire without knowledge is not good—how much more will hasty feet miss the way!", "Patience, wisdom, process"),
            ("Romans 8:25", "But if we hope for what we do not yet have, we wait for it patiently.", "Hope, patience, waiting"),
        ]
    }
    
    # Edible London brand voice adaptations
    EDIBLE_LONDON_HOOKS = [
        "Planning a global brand on the 329 bus? Scripture says...",
        "The graft comes first. The Word backs it up:",
        "Real hands. Real work. Scripture reminds us:",
        "Made by heart. The Bible puts it this way:",
        "Building something real? The Word says:",
        "From Wood Green to the world. Scripture teaches:",
    ]
    
    # ILVEN Sea Moss brand voice adaptations
    ILVEN_HOOKS = [
        "Hand-prepared. Heart-first. Scripture tells us:",
        "Sea moss made by hand, guided by heart. The Word says:",
        "Ancient wisdom meets modern craft. Scripture reminds:",
        "From hand to jar, from heart to community. The Bible says:",
        "Traditional craft, timeless wisdom. Scripture teaches:",
        "Real work. Real heart. The Word puts it like this:",
    ]
    
    # Jean Morphius brand voice adaptations (bilingual absurdist)
    JEAN_MAHRAM_HOOKS = [
        "Merde, c'est beautiful! Scripture says...",
        "Je reviens, baby! The Word backs it up:",
        "Bilingual chaos meets eternal truth. Scripture tells us:",
        "Absurd? Maybe. Profound? Always. The Bible says:",
        "French/English code-switching for the Word:",
        "Chaos meets craft, profane meets sacred. Scripture reminds:",
    ]
    
    # Karasahin/JK brand voice adaptations (Duygu Adamı - Emotion Man)
    KARASAHIN_HOOKS = [
        "Duygu Adamı. Emotion Man. The Word says:",
        "Feeling first. Sound follows. Scripture tells us:",
        "Emotion drives the beat. Scripture backs it up:",
        "Turkish heart. English soul. Scripture reminds:",
        "Music is emotion. Scripture is truth. The Bible says:",
        "Sound architecture built on feeling. Scripture teaches:",
    ]
    
    # Pierre Pressure brand voice adaptations (fighter philosopher)
    PIERRE_PRESSURE_HOOKS = [
        "Discipline is freedom. Scripture confirms:",
        "5 AM warrior energy. The Word backs it up:",
        "Fighter philosophy meets divine truth. Scripture says:",
        "No shortcuts. Real work. Scripture reminds:",
        "Ring strategy. Life application. The Bible says:",
        "Warrior mindset. Faith foundation. Scripture teaches:",
    ]
    
    # Uncle Ray Ramiz brand voice adaptations (contemplative elder, Dayı)
    UNCLE_RAY_RAMIZ_HOOKS = [
        "Yeğen, dinle... Child, listen. Scripture tells us:",
        "Contemplative wisdom meets eternal truth. The Word says:",
        "Nature teaches. Scripture confirms. The Bible reminds:",
        "Ancestral wisdom. Timeless Scripture. The Word says:",
        "Friday evening reflection. Scripture wisdom:",
        "Old wisdom meets eternal truth. Scripture teaches:",
    ]
    
    # Siyem Media brand voice adaptations (systems-level, meta-awareness)
    SIYEM_MEDIA_HOOKS = [
        "Systems-level thinking. Eternal truth. Scripture says:",
        "Infrastructure for artists. Foundation in faith. The Word says:",
        "Meta-awareness meets divine purpose. Scripture reminds:",
        "Seeing the whole picture. Scripture provides the frame:",
        "Infrastructure built on truth. The Bible says:",
        "Systems thinking. Faith foundation. Scripture teaches:",
    ]
    
    PLATFORMS = ['Instagram', 'Twitter', 'Facebook', 'LinkedIn']
    
    # Best posting times (UTC)
    POSTING_TIMES = {
        'Instagram': ['09:00', '12:00', '17:00', '20:00'],
        'Twitter': ['08:00', '13:00', '18:00'],
        'Facebook': ['09:00', '15:00', '19:00'],
        'LinkedIn': ['08:00', '12:00', '17:00'],
    }
    
    HASHTAGS = {
        'edible_london': [
            '#MadeByHeart', '#AmplifiedByAI', '#LondonCraft', '#RealWork',
            '#HeartFirst', '#TheGraft', '#LondonHustle', '#Scripture',
            '#FaithInAction', '#CraftAndScripture', '#LondonFaith'
        ],
        'ilven_seamoss': [
            '#MadeByHeart', '#AmplifiedByAI', '#SeaMoss', '#HandCrafted',
            '#HeartFirst', '#TraditionalCraft', '#Scripture', '#FaithInAction',
            '#WisdomAndCraft', '#SeaMossWisdom', '#HandMade'
        ],
        'jean_mahram': [
            '#JeanMorphius', '#Bilingual', '#Absurdist', '#Scripture',
            '#FaithInAction', '#ChaosAndCraft', '#FrenchEnglish', '#ComebackStories',
            '#ProfaneAndSacred', '#CreativeChaos', '#FaithInChaos'
        ],
        'karasahin_jk': [
            '#Karasahin', '#DuyguAdami', '#EmotionMan', '#Scripture',
            '#FaithInAction', '#MusicAndFaith', '#TurkishEnglish', '#SoundArchitecture',
            '#EmotionFirst', '#SonicStoryteller', '#VoiceOfGod'
        ],
        'pierre_pressure': [
            '#PierrePressure', '#FighterPhilosophy', '#Discipline', '#Scripture',
            '#FaithInAction', '#WarriorMindset', '#5AMWarrior', '#BoxingWisdom',
            '#DisciplineIsFreedom', '#FighterFaith', '#WarriorEnergy'
        ],
        'uncle_ray_ramiz': [
            '#UncleRayRamiz', '#Dayı', '#ContemplativeWisdom', '#Scripture',
            '#FaithInAction', '#AncestralWisdom', '#NatureAsTeacher', '#TurkishWisdom',
            '#ElderWisdom', '#ThresholdMoments', '#ContemplativeFaith'
        ],
        'siyem_media': [
            '#SiyemMedia', '#SystemsThinking', '#Infrastructure', '#Scripture',
            '#FaithInAction', '#MetaAwareness', '#CinematicOverseer', '#ProductionPhilosophy',
            '#SystemsFaith', '#InfrastructureWisdom', '#MediaFaith'
        ]
    }
    
    # Recommended posting frequencies per entity (posts per week)
    # Based on entity purpose, audience engagement, and Four Forms alignment
    DEFAULT_FREQUENCIES = {
        'edible_london': 2,      # Business entity - consistent but not overwhelming
        'ilven_seamoss': 2,      # Business entity - steady presence
        'jean_mahram': 4,        # Spiral (Active) - high-frequency creative content
        'karasahin_jk': 3,       # Music/emotion - regular but not daily
        'pierre_pressure': 3,    # Barred Spiral (Structured) - disciplined regularity
        'uncle_ray_ramiz': 2,    # Elliptical (Legacy) - contemplative, less frequent
        'siyem_media': 2,        # Systems-level - moderate, infrastructure-focused
    }
    
    # Four Forms alignment frequencies
    # Spiral = high frequency, Barred Spiral = regular, Elliptical = contemplative, Irregular = variable
    FOUR_FORMS_FREQUENCIES = {
        'spiral': 4,          # Active entities (Jean Morphius)
        'barred_spiral': 3,   # Structured entities (Pierre Pressure)
        'elliptical': 2,      # Legacy/contemplative (Uncle Ray Ramiz)
        'irregular': 3,       # Transformation entities (variable)
    }
    
    # Format preferences per entity (for delegation)
    # Each entity has preferred formats based on their purpose and audience
    ENTITY_FORMAT_PREFERENCES = {
        'edible_london': {
            'primary': ['text_short', 'image'],
            'secondary': ['video', 'text_long'],
            'distribution': {'text_short': 0.6, 'image': 0.3, 'video': 0.1},
            'notes': 'Business-focused: short text for quick engagement, images for product, occasional video for behind-the-scenes'
        },
        'ilven_seamoss': {
            'primary': ['text_short', 'image'],
            'secondary': ['video', 'text_long'],
            'distribution': {'text_short': 0.5, 'image': 0.3, 'video': 0.15, 'text_long': 0.05},
            'notes': 'Product-focused: short text, preparation images, video for traditional methods, occasional long-form for education'
        },
        'jean_mahram': {
            'primary': ['text_short', 'text_long', 'audio'],
            'secondary': ['video', 'image'],
            'distribution': {'text_short': 0.4, 'text_long': 0.3, 'audio': 0.2, 'video': 0.1},
            'notes': 'Creative/Spiral: bilingual text (short/long), audio for spoken word, video for absurdist content'
        },
        'karasahin_jk': {
            'primary': ['audio', 'video', 'text_short'],
            'secondary': ['image', 'text_long'],
            'distribution': {'audio': 0.4, 'video': 0.3, 'text_short': 0.2, 'image': 0.1},
            'notes': 'Music/Emotion: audio for sound architecture, video for performance, short text for emotion, images for visual art'
        },
        'pierre_pressure': {
            'primary': ['text_short', 'video', 'audio'],
            'secondary': ['image', 'text_long'],
            'distribution': {'text_short': 0.4, 'video': 0.3, 'audio': 0.2, 'image': 0.1},
            'notes': 'Motivational/Structured: short text for discipline drops, video for training, audio for motivational speeches'
        },
        'uncle_ray_ramiz': {
            'primary': ['audio', 'text_long', 'text_short'],
            'secondary': ['video', 'image'],
            'distribution': {'audio': 0.4, 'text_long': 0.3, 'text_short': 0.2, 'video': 0.1},
            'notes': 'Contemplative/Legacy: audio for wisdom teachings (bilingual), long-form text for depth, short for daily wisdom, video for teaching moments'
        },
        'siyem_media': {
            'primary': ['text_short', 'text_long', 'image'],
            'secondary': ['video', 'audio'],
            'distribution': {'text_short': 0.5, 'text_long': 0.2, 'image': 0.2, 'video': 0.1},
            'notes': 'Systems/Infrastructure: short text for updates, long-form for documentation, images for systems visualization, video for tutorials'
        }
    }
    
    # Format definitions for delegation
    FORMAT_DEFINITIONS = {
        'text_short': {
            'description': 'Short-form text content (social media posts, tweets)',
            'length': '50-300 words',
            'use_case': 'Quick engagement, daily posts, platform-native content',
            'delegation': 'WRITER agent (short-form), PUBLISHER agent (formatting)'
        },
        'text_long': {
            'description': 'Long-form text content (articles, essays, blog posts)',
            'length': '500-2000+ words',
            'use_case': 'Deep dives, educational content, wisdom teachings',
            'delegation': 'WRITER agent (long-form), PUBLISHER agent (formatting)'
        },
        'video': {
            'description': 'Video content (short-form, long-form, tutorials, performances)',
            'duration': '15 seconds - 10 minutes',
            'use_case': 'Visual storytelling, tutorials, performances, behind-the-scenes',
            'delegation': 'ARTIST agent (visual), WRITER agent (script), PUBLISHER agent (production)'
        },
        'audio': {
            'description': 'Audio content (podcasts, audiobooks, spoken word, music)',
            'duration': '1 minute - 60+ minutes',
            'use_case': 'Wisdom teachings, music, spoken word, audiobooks',
            'delegation': 'WRITER agent (script), Audio pipeline (TTS/recording), PUBLISHER agent (distribution)'
        },
        'image': {
            'description': 'Image content (graphics, quotes, product photos, art)',
            'formats': 'JPG, PNG, SVG',
            'use_case': 'Quote graphics, product images, visual art, infographics',
            'delegation': 'ARTIST agent (generation), WRITER agent (text overlay), PUBLISHER agent (formatting)'
        }
    }
    
    def __init__(self, year: int = 2026, entity_frequencies: Dict[str, int] = None):
        """
        Initialize scheduler
        
        Args:
            year: Year to schedule
            entity_frequencies: Optional dict to override default frequencies
                               Format: {'entity_name': posts_per_week}
        """
        self.year = year
        self.start_date = datetime(year, 1, 1, tzinfo=timezone.utc)
        
        # Use provided frequencies or defaults
        if entity_frequencies:
            self.frequencies = {**self.DEFAULT_FREQUENCIES, **entity_frequencies}
        else:
            self.frequencies = self.DEFAULT_FREQUENCIES.copy()
    
    def _assign_formats(self, brand: str) -> tuple:
        """
        Assign formats to a post based on entity preferences
        
        Returns:
            (formats_list, primary_format, format_notes)
        """
        prefs = self.ENTITY_FORMAT_PREFERENCES.get(brand, self.ENTITY_FORMAT_PREFERENCES['edible_london'])
        
        # Select primary format based on distribution
        dist = prefs['distribution']
        rand = random.random()
        cumulative = 0
        primary = 'text_short'  # Default
        
        for fmt, prob in dist.items():
            cumulative += prob
            if rand <= cumulative:
                primary = fmt
                break
        
        # Build formats list (primary + secondary options)
        formats = [primary]
        if primary in prefs['primary']:
            formats.extend([f for f in prefs['secondary'] if f != primary])
        else:
            formats.extend(prefs['primary'][:2])
        
        # Create format notes for delegation
        format_notes = {
            'primary_format': primary,
            'available_formats': formats,
            'entity_preferences': prefs['notes'],
            'delegation_agents': self._get_delegation_agents(primary),
            'format_requirements': self.FORMAT_DEFINITIONS.get(primary, {})
        }
        
        return formats, primary, format_notes
    
    def _get_delegation_agents(self, format_type: str) -> Dict[str, List[str]]:
        """Get which agents should handle this format"""
        agents = {
            'text_short': ['WRITER', 'PUBLISHER'],
            'text_long': ['WRITER', 'PUBLISHER'],
            'video': ['WRITER', 'ARTIST', 'PUBLISHER'],
            'audio': ['WRITER', 'Audio Pipeline', 'PUBLISHER'],
            'image': ['ARTIST', 'WRITER', 'PUBLISHER']
        }
        return {'required': agents.get(format_type, ['WRITER', 'PUBLISHER']), 'optional': []}
    
    def generate_edible_london_post(self, verse_ref: str, verse_text: str, theme: str, scheduled_time: datetime) -> ScripturePost:
        """Generate Edible London styled scripture post with format support"""
        hook = random.choice(self.EDIBLE_LONDON_HOOKS)
        
        # Brand voice: warm London banter, older-brother energy
        content = f"""{hook}

"{verse_text}" ({verse_ref})

This isn't about shortcuts. It's about the work—the real, hands-on, day-in-day-out graft. That's where the heart lives.

From planning on the 329 bus to building something that matters. The craft comes first. Scripture backs it up.

Made by heart. Amplified by AI. Guided by faith.

#MadeByHeart #AmplifiedByAI #LondonCraft #RealWork #HeartFirst #Scripture #FaithInAction"""
        
        # Assign formats for delegation
        formats, primary_format, format_notes = self._assign_formats('edible_london')
        
        return ScripturePost(
            title=f"Scripture: {verse_ref} - {theme}",
            content=content,
            scripture_reference=verse_ref,
            scripture_text=verse_text,
            scheduled_time=scheduled_time,
            platform=random.choice(self.PLATFORMS),
            hashtags=random.sample(self.HASHTAGS['edible_london'], 7),
            brand='edible_london',
            metadata={
                'theme': theme,
                'category': 'scripture',
                'voice': 'warm_london_banter'
            },
            formats=formats,
            primary_format=primary_format,
            format_notes=format_notes,
            delegation_ready=True
        )
    
    def generate_jean_mahram_post(self, verse_ref: str, verse_text: str, theme: str, scheduled_time: datetime) -> ScripturePost:
        """Generate Jean Morphius styled scripture post (bilingual absurdist)"""
        hook = random.choice(self.JEAN_MAHRAM_HOOKS)
        
        # Brand voice: bilingual absurdist, profane-yet-poetic, chaotic creativity
        # Sometimes include French phrases naturally
        french_intro = random.choice([
            "Merde, c'est vrai!",
            "Tu sais quoi?",
            "Écoute, mon frère:",
            "C'est ça, la vérité:",
            "",
        ])
        
        content = f"""{hook}

"{verse_text}" ({verse_ref})

{french_intro} This isn't about perfection. It's about authenticity—chaotic, messy, real. That's where the magic lives.

From absurdist comedy to profound truth. From French/English chaos to eternal Scripture. The craft comes first. Scripture backs it up.

Je reviens, baby! Made by heart. Amplified by AI. Guided by faith.

#JeanMorphius #Bilingual #Absurdist #Scripture #FaithInAction #ChaosAndCraft"""
        
        # Assign formats for delegation
        formats, primary_format, format_notes = self._assign_formats('jean_mahram')
        
        return ScripturePost(
            title=f"Scripture: {verse_ref} - {theme}",
            content=content,
            scripture_reference=verse_ref,
            scripture_text=verse_text,
            scheduled_time=scheduled_time,
            platform=random.choice(self.PLATFORMS),
            hashtags=random.sample(self.HASHTAGS['jean_mahram'], 7),
            brand='jean_mahram',
            metadata={
                'theme': theme,
                'category': 'scripture',
                'voice': 'bilingual_absurdist'
            },
            formats=formats,
            primary_format=primary_format,
            format_notes=format_notes,
            delegation_ready=True
        )
    
    def generate_karasahin_post(self, verse_ref: str, verse_text: str, theme: str, scheduled_time: datetime) -> ScripturePost:
        """Generate Karasahin/JK styled scripture post (Duygu Adamı - Emotion Man)"""
        hook = random.choice(self.KARASAHIN_HOOKS)
        
        # Brand voice: Emotion Man, feeling-first, Turkish/English bilingual, sound architecture
        # Sometimes include Turkish phrases naturally
        turkish_intro = random.choice([
            "Duygu Adamı diyorum. Emotion Man.",
            "His önce. Feeling first.",
            "Duygularla inşa ediyoruz. Building with emotion.",
            "Emotion drives everything.",
            "",
        ])
        
        content = f"""{hook}

"{verse_text}" ({verse_ref})

{turkish_intro} This is sound architecture. Built on feeling. Driven by emotion. That's where the truth lives.

From Turkish heart to English soul. From feeling to sound. From emotion to Scripture. Duygu Adamı. Emotion Man. The craft comes first. Scripture backs it up.

Made by heart. Amplified by AI. Guided by faith.

#Karasahin #DuyguAdami #EmotionMan #Scripture #FaithInAction #SoundArchitecture"""
        
        # Assign formats for delegation
        formats, primary_format, format_notes = self._assign_formats('karasahin_jk')
        
        return ScripturePost(
            title=f"Scripture: {verse_ref} - {theme}",
            content=content,
            scripture_reference=verse_ref,
            scripture_text=verse_text,
            scheduled_time=scheduled_time,
            platform=random.choice(self.PLATFORMS),
            hashtags=random.sample(self.HASHTAGS['karasahin_jk'], 7),
            brand='karasahin_jk',
            metadata={
                'theme': theme,
                'category': 'scripture',
                'voice': 'emotion_man'
            },
            formats=formats,
            primary_format=primary_format,
            format_notes=format_notes,
            delegation_ready=True
        )
    
    def generate_pierre_pressure_post(self, verse_ref: str, verse_text: str, theme: str, scheduled_time: datetime) -> ScripturePost:
        """Generate Pierre Pressure styled scripture post (fighter philosopher)"""
        hook = random.choice(self.PIERRE_PRESSURE_HOOKS)
        
        # Brand voice: direct, commanding, fighter philosophy, discipline, warrior energy
        content = f"""{hook}

"{verse_text}" ({verse_ref})

No shortcuts. No excuses. Discipline is freedom. That's where the strength lives.

From 5 AM training to life application. From ring strategy to faith foundation. The fighter's mindset. Scripture backs it up.

Warrior energy. Made by heart. Amplified by AI. Guided by faith.

#PierrePressure #FighterPhilosophy #Discipline #Scripture #FaithInAction #WarriorMindset"""
        
        # Assign formats for delegation
        formats, primary_format, format_notes = self._assign_formats('pierre_pressure')
        
        return ScripturePost(
            title=f"Scripture: {verse_ref} - {theme}",
            content=content,
            scripture_reference=verse_ref,
            scripture_text=verse_text,
            scheduled_time=scheduled_time,
            platform=random.choice(self.PLATFORMS),
            hashtags=random.sample(self.HASHTAGS['pierre_pressure'], 7),
            brand='pierre_pressure',
            metadata={
                'theme': theme,
                'category': 'scripture',
                'voice': 'fighter_philosopher'
            },
            formats=formats,
            primary_format=primary_format,
            format_notes=format_notes,
            delegation_ready=True
        )
    
    def generate_uncle_ray_ramiz_post(self, verse_ref: str, verse_text: str, theme: str, scheduled_time: datetime) -> ScripturePost:
        """Generate Uncle Ray Ramiz styled scripture post (contemplative elder, Dayı)"""
        hook = random.choice(self.UNCLE_RAY_RAMIZ_HOOKS)
        
        # Brand voice: contemplative, Dayı address, nature as teacher, ancestral wisdom, Turkish/English bilingual
        dayi_address = random.choice([
            "Yeğen, dinle... Child, listen...",
            "Evlat, dikkatle dinle... My child, listen carefully...",
            "Child, listen...",
            "Listen carefully...",
        ])
        
        content = f"""{dayi_address} {hook}

"{verse_text}" ({verse_ref})

Nature teaches. Scripture confirms. Ancestral wisdom meets eternal truth. That's where the wisdom lives.

From contemplative reflection to practical application. From Friday evening stillness to daily guidance. The elder's wisdom. Scripture backs it up.

Made by heart. Amplified by AI. Guided by faith.

#UncleRayRamiz #Dayı #ContemplativeWisdom #Scripture #FaithInAction #AncestralWisdom"""
        
        # Assign formats for delegation
        formats, primary_format, format_notes = self._assign_formats('uncle_ray_ramiz')
        
        return ScripturePost(
            title=f"Scripture: {verse_ref} - {theme}",
            content=content,
            scripture_reference=verse_ref,
            scripture_text=verse_text,
            scheduled_time=scheduled_time,
            platform=random.choice(self.PLATFORMS),
            hashtags=random.sample(self.HASHTAGS['uncle_ray_ramiz'], 7),
            brand='uncle_ray_ramiz',
            metadata={
                'theme': theme,
                'category': 'scripture',
                'voice': 'contemplative_elder'
            },
            formats=formats,
            primary_format=primary_format,
            format_notes=format_notes,
            delegation_ready=True
        )
    
    def generate_siyem_media_post(self, verse_ref: str, verse_text: str, theme: str, scheduled_time: datetime) -> ScripturePost:
        """Generate Siyem Media styled scripture post (systems-level, meta-awareness)"""
        hook = random.choice(self.SIYEM_MEDIA_HOOKS)
        
        # Brand voice: systems-level thinking, meta-awareness, infrastructure, cinematic overseer
        content = f"""{hook}

"{verse_text}" ({verse_ref})

Infrastructure for artists. Foundation in faith. Systems-level thinking meets eternal truth. That's where the structure lives.

From meta-awareness to practical systems. From cinematic vision to daily operations. The infrastructure. Scripture backs it up.

Made by heart. Amplified by AI. Guided by faith.

#SiyemMedia #SystemsThinking #Infrastructure #Scripture #FaithInAction #MetaAwareness"""
        
        # Assign formats for delegation
        formats, primary_format, format_notes = self._assign_formats('siyem_media')
        
        return ScripturePost(
            title=f"Scripture: {verse_ref} - {theme}",
            content=content,
            scripture_reference=verse_ref,
            scripture_text=verse_text,
            scheduled_time=scheduled_time,
            platform=random.choice(self.PLATFORMS),
            hashtags=random.sample(self.HASHTAGS['siyem_media'], 7),
            brand='siyem_media',
            metadata={
                'theme': theme,
                'category': 'scripture',
                'voice': 'systems_level'
            },
            formats=formats,
            primary_format=primary_format,
            format_notes=format_notes,
            delegation_ready=True
        )
    
    def generate_ilven_post(self, verse_ref: str, verse_text: str, theme: str, scheduled_time: datetime) -> ScripturePost:
        """Generate ILVEN Sea Moss styled scripture post"""
        hook = random.choice(self.ILVEN_HOOKS)
        
        # Brand voice: older-brother energy, warm, protective
        content = f"""{hook}

"{verse_text}" ({verse_ref})

This is sea moss. Hand-prepared. Every batch. Every jar. The way it's been done for generations.

But here's the deeper truth: when craft meets faith, when hands meet heart, that's where real work lives.

Traditional wisdom meets timeless Scripture. Ancient preparation meets eternal truth.

Made by heart. Amplified by AI. Guided by faith.

#MadeByHeart #AmplifiedByAI #SeaMoss #HandCrafted #HeartFirst #Scripture #FaithInAction"""
        
        # Assign formats for delegation
        formats, primary_format, format_notes = self._assign_formats('ilven_seamoss')
        
        return ScripturePost(
            title=f"Scripture: {verse_ref} - {theme}",
            content=content,
            scripture_reference=verse_ref,
            scripture_text=verse_text,
            scheduled_time=scheduled_time,
            platform=random.choice(self.PLATFORMS),
            hashtags=random.sample(self.HASHTAGS['ilven_seamoss'], 7),
            brand='ilven_seamoss',
            metadata={
                'theme': theme,
                'category': 'scripture',
                'voice': 'older_brother_energy'
            },
            formats=formats,
            primary_format=primary_format,
            format_notes=format_notes,
            delegation_ready=True
        )
    
    def generate_yearly_schedule(
        self, 
        posts_per_week: Optional[int] = None,
        brands: List[str] = None,
        entity_frequencies: Dict[str, int] = None
    ) -> List[ScripturePost]:
        """
        Generate scripture posts for entire year with entity-specific frequencies
        
        Args:
            posts_per_week: Optional override for all entities (if None, uses entity-specific frequencies)
            brands: List of entities to schedule. If None, uses all entities.
            entity_frequencies: Optional dict to override frequencies per entity
                               Format: {'entity_name': posts_per_week}
        """
        if brands is None:
            brands = self.ENTITIES
        
        # Use provided entity frequencies or merge with defaults
        if entity_frequencies:
            frequencies = {**self.frequencies, **entity_frequencies}
        else:
            frequencies = self.frequencies.copy()
        
        # If posts_per_week is provided, override all entities
        if posts_per_week is not None:
            frequencies = {entity: posts_per_week for entity in brands}
        
        posts = []
        current_date = self.start_date
        end_date = datetime(self.year, 12, 31, 23, 59, 59, tzinfo=timezone.utc)
        
        # Track which themes we've used
        theme_rotation = list(self.SCRIPTURES.keys())
        theme_index = 0
        
        # Generate posts for each entity with their specific frequency
        week_start = current_date
        
        while week_start <= end_date:
            for brand in brands:
                freq = frequencies.get(brand, 3)  # Default to 3 if not specified
                
                if freq <= 0:
                    continue  # Skip entities with 0 frequency
                
                # Calculate days between posts for this entity
                days_between = 7 / freq if freq > 0 else 7
                
                # Generate posts for this week for this entity
                for post_num in range(freq):
                    # Select theme
                    theme = theme_rotation[theme_index % len(theme_rotation)]
                    verse_ref, verse_text, _ = random.choice(self.SCRIPTURES[theme])
                    
                    # Calculate post time within the week
                    post_offset = post_num * days_between + random.uniform(0, days_between * 0.5)
                    scheduled_date = week_start + timedelta(days=post_offset)
                    
                    # Ensure we don't exceed the end date
                    if scheduled_date > end_date:
                        break
                    
                    # Select platform and time
                    platform = random.choice(self.PLATFORMS)
                    time_str = random.choice(self.POSTING_TIMES[platform])
                    hour, minute = map(int, time_str.split(':'))
                    
                    # Create scheduled time
                    scheduled_time = scheduled_date.replace(hour=hour, minute=minute)
                    # Add some randomness to minute (0-30 minutes)
                    scheduled_time += timedelta(minutes=random.randint(0, 30))
                    
                    # Generate post based on entity
                    if brand == 'edible_london':
                        post = self.generate_edible_london_post(verse_ref, verse_text, theme, scheduled_time)
                    elif brand == 'ilven_seamoss':
                        post = self.generate_ilven_post(verse_ref, verse_text, theme, scheduled_time)
                    elif brand == 'jean_mahram':
                        post = self.generate_jean_mahram_post(verse_ref, verse_text, theme, scheduled_time)
                    elif brand == 'karasahin_jk':
                        post = self.generate_karasahin_post(verse_ref, verse_text, theme, scheduled_time)
                    elif brand == 'pierre_pressure':
                        post = self.generate_pierre_pressure_post(verse_ref, verse_text, theme, scheduled_time)
                    elif brand == 'uncle_ray_ramiz':
                        post = self.generate_uncle_ray_ramiz_post(verse_ref, verse_text, theme, scheduled_time)
                    elif brand == 'siyem_media':
                        post = self.generate_siyem_media_post(verse_ref, verse_text, theme, scheduled_time)
                    else:
                        # Default to Edible London voice
                        post = self.generate_edible_london_post(verse_ref, verse_text, theme, scheduled_time)
                    
                    posts.append(post)
                    
                    theme_index += 1
            
            # Move to next week
            week_start += timedelta(days=7)
        
        # Sort by scheduled time
        posts.sort(key=lambda p: p.scheduled_time)
        
        return posts
    
    def export_to_calendar_format(self, posts: List[ScripturePost]) -> List[Dict]:
        """
        Convert ScripturePost objects to calendar export format
        Includes format information for delegation
        """
        return [
            {
                'title': post.title,
                'content': post.content,
                'scheduled_time': post.scheduled_time.isoformat(),
                'platform': post.platform,
                'hashtags': post.hashtags,
                'url': None,  # Can be added later
                'location': None,
                'metadata': {
                    **post.metadata,
                    'scripture_reference': post.scripture_reference,
                    'scripture_text': post.scripture_text,
                    'brand': post.brand,
                },
                # Format delegation fields
                'formats': post.formats or ['text_short'],
                'primary_format': post.primary_format,
                'format_notes': post.format_notes or {},
                'delegation_ready': post.delegation_ready
            }
            for post in posts
        ]


def generate_2026_scripture_schedule(
    posts_per_week: Optional[int] = None,
    entities: List[str] = None,
    entity_frequencies: Dict[str, int] = None
) -> Dict:
    """
    Generate complete 2026 scripture schedule for all or specified SIYEM entities
    
    Uses optimized entity-specific frequencies based on purpose and Four Forms alignment.
    
    Args:
        posts_per_week: Optional override for all entities (if None, uses optimized frequencies)
        entities: List of entities to schedule. If None, schedules all entities.
                  Options: 'edible_london', 'ilven_seamoss', 'jean_mahram', 
                  'karasahin_jk', 'pierre_pressure', 'uncle_ray_ramiz', 'siyem_media'
        entity_frequencies: Optional dict to override frequencies per entity
                           Format: {'entity_name': posts_per_week}
    
    Default Frequencies (posts per week):
        - edible_london: 2 (Business - steady but not overwhelming)
        - ilven_seamoss: 2 (Business - consistent presence)
        - jean_mahram: 4 (Spiral/Active - high-frequency creative)
        - karasahin_jk: 3 (Music/Emotion - regular engagement)
        - pierre_pressure: 3 (Barred Spiral/Structured - disciplined regularity)
        - uncle_ray_ramiz: 2 (Elliptical/Legacy - contemplative, less frequent)
        - siyem_media: 2 (Systems-level - moderate infrastructure focus)
    
    Returns:
        Dictionary with post lists for each entity and summary
    """
    scheduler = ScriptureScheduler(year=2026, entity_frequencies=entity_frequencies)
    
    # Default to all entities if not specified
    if entities is None:
        entities = scheduler.ENTITIES
    
    # Validate entities
    valid_entities = [e for e in entities if e in scheduler.ENTITIES]
    if not valid_entities:
        raise ValueError(f"No valid entities found. Valid options: {scheduler.ENTITIES}")
    
    # Generate for all specified entities with their optimized frequencies
    all_posts = scheduler.generate_yearly_schedule(
        posts_per_week=posts_per_week,
        brands=valid_entities,
        entity_frequencies=entity_frequencies
    )
    
    # Separate by entity
    entity_posts = {}
    entity_counts = {}
    
    for entity in valid_entities:
        entity_post_list = [p for p in all_posts if p.brand == entity]
        entity_posts[entity] = scheduler.export_to_calendar_format(entity_post_list)
        entity_counts[f"{entity}_count"] = len(entity_post_list)
    
    # Calculate frequency summary
    frequency_summary = {}
    for entity in valid_entities:
        freq = scheduler.frequencies.get(entity, 3)
        if posts_per_week is not None:
            freq = posts_per_week
        elif entity_frequencies and entity in entity_frequencies:
            freq = entity_frequencies[entity]
        frequency_summary[f"{entity}_frequency"] = freq
    
    return {
        **entity_posts,  # Individual entity lists
        'all_posts': scheduler.export_to_calendar_format(all_posts),
        'summary': {
            'total_posts': len(all_posts),
            'year': 2026,
            'posts_per_week': posts_per_week if posts_per_week else 'entity-specific',
            'entities': valid_entities,
            **entity_counts,
            **frequency_summary,
            'frequency_breakdown': {
                entity: scheduler.frequencies.get(entity, 3) if posts_per_week is None else posts_per_week
                for entity in valid_entities
            }
        }
    }


if __name__ == "__main__":
    # Generate schedule for all entities with optimized frequencies
    schedule = generate_2026_scripture_schedule()  # Uses entity-specific frequencies
    
    # Save to JSON
    with open('scripture_schedule_2026.json', 'w', encoding='utf-8') as f:
        json.dump(schedule, f, indent=2, ensure_ascii=False, default=str)
    
    print(f"Generated {schedule['summary']['total_posts']} scripture posts for 2026")
    print(f"\nPosts per entity (optimized frequencies):")
    for entity in schedule['summary']['entities']:
        count_key = f"{entity}_count"
        freq_key = f"{entity}_frequency"
        count = schedule['summary'].get(count_key, 0)
        freq = schedule['summary'].get(freq_key, 'N/A')
        print(f"  - {entity}: {count} posts ({freq} posts/week)")
    print(f"\nFrequency breakdown:")
    for entity, freq in schedule['summary']['frequency_breakdown'].items():
        print(f"  - {entity}: {freq} posts/week")
    print(f"\nSaved to: scripture_schedule_2026.json")
