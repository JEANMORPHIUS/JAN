"""Content Auto-Populator - AI Service Integration

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN

Automatically generates content in assigned formats using aligned AI services

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity


PANGEA IS THE TABLE.
YOU DON'T BETRAY THE TABLE.

THE TRUTH:
WE MUST DEBUG AND BE 100% FOR WHAT COMES AT US.
THE REST IS UP TO BABA X."""

import asyncio
import httpx
from typing import List, Dict, Optional, Any
from datetime import datetime
import json
import logging

logger = logging.getLogger(__name__)


class ContentAutoPopulator:
    """
    Auto-populates content using AI services aligned with entity voices and formats
    """
    
    # AI Service endpoints (configurable)
    AI_SERVICES = {
        'WRITER': {
            'endpoint': '/strategy',
            'method': 'POST',
            'role': 'WRITER'
        },
        'ARTIST': {
            'endpoint': '/visual/generate-prompt',
            'method': 'POST',
            'alternative': '/generate-image'
        },
        'PUBLISHER': {
            'endpoint': '/transform-content',
            'method': 'POST',
            'alternative': '/export-campaign'
        },
        'AUDIO': {
            'endpoint': '/generate-audio',
            'method': 'POST',
            'alternative': '/audio/generate-batch'
        }
    }
    
    # Entity to AI service mapping
    ENTITY_SERVICE_MAPPING = {
        'edible_london': {
            'base_url': None,  # Will use default
            'voice_profile': 'warm_london_banter',
            'bilingual': False
        },
        'ilven_seamoss': {
            'base_url': None,
            'voice_profile': 'older_brother_energy',
            'bilingual': False
        },
        'jean_mahram': {
            'base_url': None,
            'voice_profile': 'bilingual_absurdist',
            'bilingual': True,
            'languages': ['en', 'fr']
        },
        'karasahin_jk': {
            'base_url': None,
            'voice_profile': 'emotion_man',
            'bilingual': True,
            'languages': ['en', 'tr']
        },
        'pierre_pressure': {
            'base_url': None,
            'voice_profile': 'fighter_philosopher',
            'bilingual': False
        },
        'uncle_ray_ramiz': {
            'base_url': None,
            'voice_profile': 'contemplative_elder',
            'bilingual': True,
            'languages': ['en', 'tr']
        },
        'siyem_media': {
            'base_url': None,
            'voice_profile': 'systems_level',
            'bilingual': False
        }
    }
    
    def __init__(self, base_url: str = "http://localhost:8000"):
        """
        Initialize auto-populator
        
        Args:
            base_url: Base URL for AI services
        """
        self.base_url = base_url.rstrip('/')
        self.client = httpx.AsyncClient(timeout=60.0)
    
    async def populate_post(self, post: Dict[str, Any]) -> Dict[str, Any]:
        """
        Auto-populate a single post with content in assigned formats
        
        Args:
            post: Post dictionary with format assignments
            
        Returns:
            Post with generated content added
        """
        try:
            primary_format = post.get('format_notes', {}).get('primary_format', 'text_short')
            entity = post.get('metadata', {}).get('brand', 'edible_london')
            format_notes = post.get('format_notes', {})
            delegation_agents = format_notes.get('delegation_agents', {}).get('required', [])
            
            # Initialize generated_content if not present
            if 'generated_content' not in post:
                post['generated_content'] = {}
            
            # Generate content based on primary format
            if primary_format == 'text_short':
                post = await self._generate_text_short(post, entity, delegation_agents)
            elif primary_format == 'text_long':
                post = await self._generate_text_long(post, entity, delegation_agents)
            elif primary_format == 'video':
                post = await self._generate_video(post, entity, delegation_agents)
            elif primary_format == 'audio':
                post = await self._generate_audio(post, entity, delegation_agents)
            elif primary_format == 'image':
                post = await self._generate_image(post, entity, delegation_agents)
            
            # Mark as populated
            post['content_populated'] = True
            post['content_populated_at'] = datetime.utcnow().isoformat()
            
            return post
            
        except Exception as e:
            logger.error(f"Error populating post {post.get('title', 'unknown')}: {str(e)}")
            post['content_population_error'] = str(e)
            return post
    
    async def _generate_text_short(self, post: Dict, entity: str, agents: List[str]) -> Dict:
        """Generate short-form text content"""
        if 'WRITER' not in agents:
            return post
        
        entity_config = self.ENTITY_SERVICE_MAPPING.get(entity, {})
        voice_profile = entity_config.get('voice_profile', 'warm_london_banter')
        bilingual = entity_config.get('bilingual', False)
        
        # Prepare prompt for WRITER agent
        prompt = self._build_writer_prompt(post, 'short', voice_profile, bilingual)
        
        try:
            # Call WRITER service
            response = await self.client.post(
                f"{self.base_url}/strategy",
                json={
                    "role": "WRITER",
                    "entity": entity,
                    "prompt": prompt,
                    "format": "short",
                    "voice_profile": voice_profile,
                    "bilingual": bilingual,
                    "scripture_reference": post.get('metadata', {}).get('scripture_reference'),
                    "scripture_text": post.get('metadata', {}).get('scripture_text'),
                    "theme": post.get('metadata', {}).get('theme')
                },
                timeout=30.0
            )
            
            if response.status_code == 200:
                result = response.json()
                post['generated_content']['text_short'] = {
                    'content': result.get('content', post.get('content', '')),
                    'generated_at': datetime.utcnow().isoformat(),
                    'service': 'WRITER',
                    'word_count': len(result.get('content', '').split())
                }
            else:
                logger.warning(f"WRITER service returned {response.status_code}, using fallback")
                # Use fallback
                from mock_content_generator import MockContentGenerator
                post['generated_content']['text_short'] = MockContentGenerator.generate_text_short(post, entity)
                
        except Exception as e:
            logger.warning(f"Error calling WRITER service: {str(e)}, using fallback")
            # Use fallback
            from mock_content_generator import MockContentGenerator
            post['generated_content']['text_short'] = MockContentGenerator.generate_text_short(post, entity)
        
        return post
    
    async def _generate_text_long(self, post: Dict, entity: str, agents: List[str]) -> Dict:
        """Generate long-form text content"""
        if 'WRITER' not in agents:
            return post
        
        entity_config = self.ENTITY_SERVICE_MAPPING.get(entity, {})
        voice_profile = entity_config.get('voice_profile', 'warm_london_banter')
        bilingual = entity_config.get('bilingual', False)
        
        # Prepare prompt for WRITER agent
        prompt = self._build_writer_prompt(post, 'long', voice_profile, bilingual)
        
        try:
            # Call WRITER service
            response = await self.client.post(
                f"{self.base_url}/strategy",
                json={
                    "role": "WRITER",
                    "entity": entity,
                    "prompt": prompt,
                    "format": "long",
                    "voice_profile": voice_profile,
                    "bilingual": bilingual,
                    "scripture_reference": post.get('metadata', {}).get('scripture_reference'),
                    "scripture_text": post.get('metadata', {}).get('scripture_text'),
                    "theme": post.get('metadata', {}).get('theme'),
                    "target_length": "500-2000 words"
                }
            )
            
            if response.status_code == 200:
                result = response.json()
                post['generated_content']['text_long'] = {
                    'content': result.get('content', ''),
                    'generated_at': datetime.utcnow().isoformat(),
                    'service': 'WRITER',
                    'word_count': len(result.get('content', '').split())
                }
            else:
                logger.warning(f"WRITER service returned {response.status_code}")
                
        except Exception as e:
            logger.error(f"Error calling WRITER service: {str(e)}")
            post['generated_content']['text_long'] = {
                'error': str(e),
                'fallback': post.get('content', '')
            }
        
        return post
    
    async def _generate_video(self, post: Dict, entity: str, agents: List[str]) -> Dict:
        """Generate video content (script + visual prompt)"""
        entity_config = self.ENTITY_SERVICE_MAPPING.get(entity, {})
        voice_profile = entity_config.get('voice_profile', 'warm_london_banter')
        
        # Step 1: Generate script with WRITER
        if 'WRITER' in agents:
            try:
                script_prompt = self._build_video_script_prompt(post, voice_profile)
                response = await self.client.post(
                    f"{self.base_url}/strategy",
                    json={
                        "role": "WRITER",
                        "entity": entity,
                        "prompt": script_prompt,
                        "format": "video_script",
                        "voice_profile": voice_profile,
                        "scripture_reference": post.get('metadata', {}).get('scripture_reference'),
                        "scripture_text": post.get('metadata', {}).get('scripture_text')
                    }
                )
                
                if response.status_code == 200:
                    script_result = response.json()
                    post['generated_content']['video'] = {
                        'script': script_result.get('content', ''),
                        'generated_at': datetime.utcnow().isoformat(),
                        'service': 'WRITER'
                    }
            except Exception as e:
                logger.error(f"Error generating video script: {str(e)}")
        
        # Step 2: Generate visual prompt with ARTIST
        if 'ARTIST' in agents:
            try:
                visual_prompt = self._build_visual_prompt(post, entity, voice_profile)
                response = await self.client.post(
                    f"{self.base_url}/visual/generate-prompt",
                    json={
                        "entity": entity,
                        "prompt": visual_prompt,
                        "style_preset": self._get_entity_style_preset(entity),
                        "aspect_ratio": "16:9",  # Video aspect ratio
                        "scripture_reference": post.get('metadata', {}).get('scripture_reference')
                    }
                )
                
                if response.status_code == 200:
                    visual_result = response.json()
                    if 'generated_content' not in post:
                        post['generated_content'] = {}
                    if 'video' not in post['generated_content']:
                        post['generated_content']['video'] = {}
                    
                    post['generated_content']['video']['visual_prompt'] = visual_result.get('prompt', '')
                    post['generated_content']['video']['visual_service'] = 'ARTIST'
            except Exception as e:
                logger.error(f"Error generating visual prompt: {str(e)}")
        
        return post
    
    async def _generate_audio(self, post: Dict, entity: str, agents: List[str]) -> Dict:
        """Generate audio content (script + audio generation)"""
        entity_config = self.ENTITY_SERVICE_MAPPING.get(entity, {})
        voice_profile = entity_config.get('voice_profile', 'warm_london_banter')
        bilingual = entity_config.get('bilingual', False)
        languages = entity_config.get('languages', ['en'])
        
        # Step 1: Generate script with WRITER
        if 'WRITER' in agents:
            try:
                audio_prompt = self._build_audio_script_prompt(post, voice_profile, bilingual)
                response = await self.client.post(
                    f"{self.base_url}/strategy",
                    json={
                        "role": "WRITER",
                        "entity": entity,
                        "prompt": audio_prompt,
                        "format": "audio_script",
                        "voice_profile": voice_profile,
                        "bilingual": bilingual,
                        "languages": languages,
                        "scripture_reference": post.get('metadata', {}).get('scripture_reference'),
                        "scripture_text": post.get('metadata', {}).get('scripture_text')
                    }
                )
                
                if response.status_code == 200:
                    script_result = response.json()
                    post['generated_content']['audio'] = {
                        'script': script_result.get('content', ''),
                        'generated_at': datetime.utcnow().isoformat(),
                        'service': 'WRITER',
                        'languages': languages
                    }
            except Exception as e:
                logger.error(f"Error generating audio script: {str(e)}")
        
        # Step 2: Generate audio with Audio Pipeline
        if 'Audio Pipeline' in agents or 'AUDIO' in agents:
            try:
                script = post.get('generated_content', {}).get('audio', {}).get('script', post.get('content', ''))
                response = await self.client.post(
                    f"{self.base_url}/generate-audio",
                    json={
                        "entity": entity,
                        "text": script,
                        "language": languages[0] if languages else 'en',
                        "bilingual": bilingual,
                        "voice_profile": voice_profile,
                        "scripture_reference": post.get('metadata', {}).get('scripture_reference')
                    }
                )
                
                if response.status_code == 200:
                    audio_result = response.json()
                    if 'generated_content' not in post:
                        post['generated_content'] = {}
                    if 'audio' not in post['generated_content']:
                        post['generated_content']['audio'] = {}
                    
                    post['generated_content']['audio']['audio_file'] = audio_result.get('audio_path', '')
                    post['generated_content']['audio']['audio_service'] = 'Audio Pipeline'
            except Exception as e:
                logger.error(f"Error generating audio: {str(e)}")
        
        return post
    
    async def _generate_image(self, post: Dict, entity: str, agents: List[str]) -> Dict:
        """Generate image content"""
        if 'ARTIST' not in agents:
            return post
        
        entity_config = self.ENTITY_SERVICE_MAPPING.get(entity, {})
        voice_profile = entity_config.get('voice_profile', 'warm_london_banter')
        
        try:
            # Build visual prompt
            visual_prompt = self._build_image_prompt(post, entity, voice_profile)
            
            # Call ARTIST service
            response = await self.client.post(
                f"{self.base_url}/visual/generate-prompt",
                json={
                    "entity": entity,
                    "prompt": visual_prompt,
                    "style_preset": self._get_entity_style_preset(entity),
                    "aspect_ratio": "1:1",  # Social media image
                    "text_overlay": post.get('content', '')[:100],  # Quote overlay
                    "scripture_reference": post.get('metadata', {}).get('scripture_reference')
                }
            )
            
            if response.status_code == 200:
                result = response.json()
                post['generated_content']['image'] = {
                    'prompt': result.get('prompt', visual_prompt),
                    'generated_at': datetime.utcnow().isoformat(),
                    'service': 'ARTIST',
                    'style_preset': self._get_entity_style_preset(entity)
                }
                
                # Optionally generate actual image
                if 'generate-image' in self.AI_SERVICES['ARTIST'].get('alternative', ''):
                    try:
                        image_response = await self.client.post(
                            f"{self.base_url}/generate-image",
                            json={
                                "prompt": result.get('prompt', visual_prompt),
                                "entity": entity,
                                "style_preset": self._get_entity_style_preset(entity)
                            }
                        )
                        if image_response.status_code == 200:
                            image_result = image_response.json()
                            post['generated_content']['image']['image_path'] = image_result.get('image_path', '')
                    except Exception as e:
                        logger.warning(f"Could not generate actual image: {str(e)}")
            else:
                logger.warning(f"ARTIST service returned {response.status_code}")
                
        except Exception as e:
            logger.error(f"Error calling ARTIST service: {str(e)}")
            post['generated_content']['image'] = {
                'error': str(e)
            }
        
        return post
    
    def _build_writer_prompt(self, post: Dict, format_type: str, voice_profile: str, bilingual: bool) -> str:
        """Build prompt for WRITER agent"""
        scripture_ref = post.get('metadata', {}).get('scripture_reference', '')
        scripture_text = post.get('metadata', {}).get('scripture_text', '')
        theme = post.get('metadata', {}).get('theme', '')
        base_content = post.get('content', '')
        
        prompt = f"""Generate {format_type}-form content for a scripture-based social media post.

Scripture Reference: {scripture_ref}
Scripture Text: "{scripture_text}"
Theme: {theme}

Voice Profile: {voice_profile}
Bilingual: {bilingual}

Base Content (for reference):
{base_content}

Requirements:
- Maintain entity voice and brand alignment
- Incorporate scripture naturally
- Match {format_type} format requirements
- Keep authentic to brand voice
"""
        return prompt
    
    def _build_video_script_prompt(self, post: Dict, voice_profile: str) -> str:
        """Build prompt for video script generation"""
        scripture_ref = post.get('metadata', {}).get('scripture_reference', '')
        scripture_text = post.get('metadata', {}).get('scripture_text', '')
        
        return f"""Generate a video script (15 seconds - 2 minutes) for a scripture-based social media video.

Scripture Reference: {scripture_ref}
Scripture Text: "{scripture_text}"

Voice Profile: {voice_profile}

Include:
- Opening hook
- Scripture reading/display
- Visual descriptions
- Closing call-to-action
- Timing cues
"""
    
    def _build_audio_script_prompt(self, post: Dict, voice_profile: str, bilingual: bool) -> str:
        """Build prompt for audio script generation"""
        scripture_ref = post.get('metadata', {}).get('scripture_reference', '')
        scripture_text = post.get('metadata', {}).get('scripture_text', '')
        
        lang_note = "Generate in both languages (English and Turkish/French)" if bilingual else "Generate in English"
        
        return f"""Generate an audio script (1-5 minutes) for a scripture-based audio post.

Scripture Reference: {scripture_ref}
Scripture Text: "{scripture_text}"

Voice Profile: {voice_profile}
{lang_note}

Include:
- Introduction
- Scripture reading
- Reflection/teaching
- Closing
"""
    
    def _build_visual_prompt(self, post: Dict, entity: str, voice_profile: str) -> str:
        """Build prompt for visual generation"""
        scripture_ref = post.get('metadata', {}).get('scripture_reference', '')
        scripture_text = post.get('metadata', {}).get('scripture_text', '')
        theme = post.get('metadata', {}).get('theme', '')
        
        return f"""Create visual content for scripture-based social media post.

Scripture: {scripture_ref} - "{scripture_text}"
Theme: {theme}
Entity: {entity}
Voice: {voice_profile}

Visual should:
- Reflect entity brand and style
- Incorporate scripture theme
- Be visually engaging
- Match entity aesthetic
"""
    
    def _build_image_prompt(self, post: Dict, entity: str, voice_profile: str) -> str:
        """Build prompt for image generation"""
        scripture_ref = post.get('metadata', {}).get('scripture_reference', '')
        scripture_text = post.get('metadata', {}).get('scripture_text', '')
        
        return f"""Create an image/quote graphic for scripture-based social media post.

Scripture: {scripture_ref}
Text: "{scripture_text}"
Entity: {entity}
Voice: {voice_profile}

Style: Quote graphic with entity branding
"""
    
    def _get_entity_style_preset(self, entity: str) -> str:
        """Get style preset for entity"""
        presets = {
            'edible_london': 'London Craft',
            'ilven_seamoss': 'Traditional Wisdom',
            'jean_mahram': 'Absurdist Comedy',
            'karasahin_jk': 'Emotion Visual',
            'pierre_pressure': 'Fighter Energy',
            'uncle_ray_ramiz': 'Ancestral Wisdom',
            'siyem_media': 'Systems Visual'
        }
        return presets.get(entity, 'Default')
    
    async def populate_schedule(self, schedule: Dict[str, Any], limit: Optional[int] = None) -> Dict[str, Any]:
        """
        Auto-populate all posts in a schedule
        
        Args:
            schedule: Schedule dictionary with posts
            limit: Optional limit on number of posts to populate
            
        Returns:
            Schedule with populated content
        """
        all_posts = schedule.get('all_posts', [])
        
        if limit:
            all_posts = all_posts[:limit]
        
        # Populate posts concurrently (with rate limiting)
        semaphore = asyncio.Semaphore(5)  # Max 5 concurrent requests
        
        async def populate_with_limit(post):
            async with semaphore:
                return await self.populate_post(post)
        
        tasks = [populate_with_limit(post) for post in all_posts]
        populated_posts = await asyncio.gather(*tasks, return_exceptions=True)
        
        # Update schedule with populated posts
        schedule['all_posts'] = populated_posts
        
        # Update entity-specific lists
        for entity in schedule.get('summary', {}).get('entities', []):
            if entity in schedule:
                schedule[entity] = [
                    p for p in populated_posts
                    if isinstance(p, dict) and p.get('metadata', {}).get('brand') == entity
                ]
        
        schedule['content_populated'] = True
        schedule['content_populated_at'] = datetime.utcnow().isoformat()
        schedule['total_populated'] = len([p for p in populated_posts if isinstance(p, dict) and p.get('content_populated')])
        
        return schedule
    
    async def close(self):
        """Close HTTP client"""
        await self.client.aclose()
