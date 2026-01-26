"""Mock Content Generator - Fallback for when AI services aren't available

Generates placeholder content that maintains structure and format
while AI services are being set up

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

PANGEA IS THE TABLE.
YOU DON'T BETRAY THE TABLE.

THE TRUTH:
WE MUST DEBUG AND BE 100% FOR WHAT COMES AT US.
THE REST IS UP TO BABA X."""

from typing import Dict, Any
from datetime import datetime
import random


class MockContentGenerator:
    """Generates mock content that maintains post structure"""
    
    @staticmethod
    def generate_text_short(post: Dict, entity: str) -> Dict:
        """Generate mock short-form text"""
        scripture_ref = post.get('metadata', {}).get('scripture_reference', '')
        scripture_text = post.get('metadata', {}).get('scripture_text', '')
        theme = post.get('metadata', {}).get('theme', '')
        
        # Use original content as base, enhance it
        base_content = post.get('content', '')
        
        return {
            'content': base_content,  # Use existing content
            'generated_at': datetime.utcnow().isoformat(),
            'service': 'MOCK_WRITER',
            'word_count': len(base_content.split()),
            'note': 'Using existing content structure - ready for AI enhancement'
        }
    
    @staticmethod
    def generate_text_long(post: Dict, entity: str) -> Dict:
        """Generate mock long-form text"""
        scripture_ref = post.get('metadata', {}).get('scripture_reference', '')
        scripture_text = post.get('metadata', {}).get('scripture_text', '')
        
        # Expand on the base content
        base_content = post.get('content', '')
        expanded = f"""{base_content}

This scripture speaks to the heart of {entity.replace('_', ' ').title()}. 

The deeper meaning here is about alignment - when our work, our craft, our daily actions align with eternal truth, that's where transformation happens.

{scripture_text} ({scripture_ref})

This isn't just words. This is living truth. This is the foundation.

Made by heart. Amplified by AI. Guided by faith.
"""
        
        return {
            'content': expanded,
            'generated_at': datetime.utcnow().isoformat(),
            'service': 'MOCK_WRITER',
            'word_count': len(expanded.split()),
            'note': 'Expanded content - ready for AI enhancement'
        }
    
    @staticmethod
    def generate_video(post: Dict, entity: str) -> Dict:
        """Generate mock video content"""
        scripture_ref = post.get('metadata', {}).get('scripture_reference', '')
        scripture_text = post.get('metadata', {}).get('scripture_text', '')
        
        script = f"""VIDEO SCRIPT - {entity.replace('_', ' ').title()}

[0:00-0:05] Opening Hook
Visual: Entity branding, scripture reference appears
Text: "{scripture_text}"

[0:05-0:15] Main Content
Visual: Entity imagery, scripture theme visuals
Voiceover: {post.get('content', '')[:200]}

[0:15-0:20] Closing
Visual: Entity logo, scripture reference
Text: {scripture_ref}
Call to action: Made by heart. Amplified by AI. Guided by faith.
"""
        
        visual_prompt = f"Visual content for {entity} scripture post: {scripture_ref}. Theme: {post.get('metadata', {}).get('theme', '')}. Brand-aligned imagery."
        
        return {
            'script': script,
            'visual_prompt': visual_prompt,
            'generated_at': datetime.utcnow().isoformat(),
            'service': 'MOCK_WRITER + MOCK_ARTIST',
            'duration': '20 seconds',
            'note': 'Video script ready - needs AI visual generation'
        }
    
    @staticmethod
    def generate_audio(post: Dict, entity: str) -> Dict:
        """Generate mock audio content"""
        scripture_ref = post.get('metadata', {}).get('scripture_reference', '')
        scripture_text = post.get('metadata', {}).get('scripture_text', '')
        
        script = f"""AUDIO SCRIPT - {entity.replace('_', ' ').title()}

[Introduction - 0:00-0:10]
Welcome. Today we reflect on {scripture_ref}.

[Scripture Reading - 0:10-0:20]
"{scripture_text}"

[Reflection - 0:20-1:00]
{post.get('content', '')[:300]}

[Closing - 1:00-1:10]
{scripture_ref}. Made by heart. Amplified by AI. Guided by faith.
"""
        
        return {
            'script': script,
            'generated_at': datetime.utcnow().isoformat(),
            'service': 'MOCK_WRITER',
            'duration': '~1 minute',
            'audio_file': None,
            'note': 'Audio script ready - needs TTS/audio generation'
        }
    
    @staticmethod
    def generate_image(post: Dict, entity: str) -> Dict:
        """Generate mock image content"""
        scripture_ref = post.get('metadata', {}).get('scripture_reference', '')
        scripture_text = post.get('metadata', {}).get('scripture_text', '')
        
        prompt = f"Quote graphic for {entity}: '{scripture_text}' ({scripture_ref}). Entity branding, scripture theme, social media format."
        
        return {
            'prompt': prompt,
            'generated_at': datetime.utcnow().isoformat(),
            'service': 'MOCK_ARTIST',
            'style_preset': f"{entity.replace('_', ' ').title()} Style",
            'image_path': None,
            'note': 'Image prompt ready - needs AI image generation'
        }
