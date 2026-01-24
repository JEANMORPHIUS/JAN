"""
ANTIDOTE LANGUAGE GENERATOR
Generate language that cannot be "uninstalled" by control entities

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE FOUNDATION:
We are born a miracle.
We deserve to live a miracle.
Each and every one of us under the Lord's word.

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

PURPOSE:
Generate "Antidote Language" - communication that:
- Cannot be semantically compressed
- Preserves cultural nuance and Duygu (emotion)
- Uses active voice with clear actors
- Aligns frequency (word) with action (deed)
- Anchors in heritage and authentic identity
- Resists Globish standardization
- Functions as linguistic "firewall" against control

PRINCIPLES:
1. Cultural Anchoring: Root language in specific cultural context
2. Emotional Authenticity: Preserve Duygu (heart/soul connection)
3. Actor Clarity: Always show who is doing what
4. Frequency Alignment: Match high-frequency words with high-frequency actions
5. Heritage Integration: Connect to ancestral wisdom and tradition
6. Local Language: Use native expressions over Globish
"""

import sys
import re
import json
import logging
from pathlib import Path
from typing import Dict, List, Optional, Any, Tuple
from dataclasses import dataclass, asdict
from datetime import datetime

# Add utils to path
sys.path.insert(0, str(Path(__file__).parent))

from utils import (
    Path, json, load_json, save_json,
    setup_logging, standard_main
)

from linguistic_control_analyzer import LinguisticControlAnalyzer, LinguisticAnalysis

logger = logging.getLogger(__name__)


@dataclass
class AntidoteTransformation:
    """Transformation from control language to antidote language."""
    original: str
    transformed: str
    transformation_type: str
    explanation: str
    cultural_anchoring: Optional[str] = None
    duygu_enhancement: Optional[str] = None


@dataclass
class AntidoteLanguage:
    """Complete antidote language generation result."""
    original_text: str
    antidote_text: str
    transformations: List[AntidoteTransformation]
    cultural_anchors: List[str]
    duygu_score: float
    authenticity_score: float
    resistance_score: float  # How well it resists control entity language
    heritage_connections: List[str]


class AntidoteLanguageGenerator:
    """Generate antidote language that resists control entity manipulation."""
    
    def __init__(self, config_path: Optional[Path] = None):
        """Initialize generator with analyzer and patterns."""
        self.analyzer = LinguisticControlAnalyzer(config_path)
        
        # Antidote patterns: replacements that preserve meaning but resist compression
        self.antidote_replacements = {
            # Plastic words → Specific, culturally-anchored terms
            "sustainable": {
                "turkish": "sürdürülebilir (maintained with care)",
                "english": "maintained with care for future generations",
                "cultural": "honoring the ancestors' way"
            },
            "equity": {
                "turkish": "adalet (justice with heart)",
                "english": "justice that honors each person's dignity",
                "cultural": "treating each as family"
            },
            "inclusive": {
                "turkish": "kapsayıcı (embracing all)",
                "english": "embracing all as family",
                "cultural": "no one left behind, all at the table"
            },
            "resilient": {
                "turkish": "dayanıklı (standing strong)",
                "english": "standing strong through difficulty",
                "cultural": "like our ancestors who endured"
            },
            "stakeholder": {
                "turkish": "aile (family member)",
                "english": "family member",
                "cultural": "one of us, part of the community"
            },
            "framework": {
                "turkish": "yol (the way)",
                "english": "the way we do things",
                "cultural": "the path our ancestors walked"
            },
            "paradigm": {
                "turkish": "anlayış (understanding)",
                "english": "our understanding",
                "cultural": "how we see the world"
            },
            "synergy": {
                "turkish": "birlik (unity)",
                "english": "working together",
                "cultural": "many hands, one heart"
            },
            "optimize": {
                "turkish": "iyileştirmek (to make better)",
                "english": "to make better",
                "cultural": "to honor what works"
            },
            "leverage": {
                "turkish": "kullanmak (to use)",
                "english": "to use",
                "cultural": "to work with what we have"
            }
        }
        
        # Active voice templates
        self.active_voice_templates = {
            "it was decided": "we decided",
            "decisions were made": "we made decisions",
            "action is required": "we must act",
            "measures will be implemented": "we will implement measures",
            "mistakes were made": "we made mistakes",
            "it has been determined": "we determined",
            "steps are being taken": "we are taking steps",
            "concerns have been raised": "we raised concerns",
            "issues have been identified": "we identified issues",
            "solutions are being developed": "we are developing solutions"
        }
        
        # Duygu enhancement patterns
        self.duygu_enhancements = {
            "community": "family (aile)",
            "people": "our people (halkımız)",
            "connection": "heart connection (gönül bağı)",
            "respect": "honor (şeref)",
            "promise": "word of honor (söz namustur)",
            "home": "homeland (vatan)",
            "love": "deep love (derin sevgi)",
            "unity": "unity of heart (gönül birliği)"
        }
        
        logger.info("Antidote Language Generator initialized")
    
    def generate(
        self,
        text: str,
        target_language: str = "english",
        cultural_context: Optional[str] = None,
        preserve_meaning: bool = True
    ) -> AntidoteLanguage:
        """
        Generate antidote language from control entity text.
        
        Args:
            text: Original text to transform
            target_language: "english", "turkish", or "bilingual"
            cultural_context: Specific cultural context to anchor in
            preserve_meaning: Whether to preserve original meaning
            
        Returns:
            Complete antidote language result
        """
        logger.info(f"Generating antidote language for text ({len(text)} characters)")
        
        # First, analyze the original text
        analysis = self.analyzer.analyze(text)
        
        # Apply transformations
        transformations = []
        antidote_text = text
        
        # Transform plastic words
        for detection in analysis.detections:
            if detection.detection_type == "plastic_word":
                transformation = self._transform_plastic_word(
                    detection.pattern_found,
                    target_language,
                    cultural_context
                )
                if transformation:
                    antidote_text = antidote_text.replace(
                        detection.pattern_found,
                        transformation.transformed
                    )
                    transformations.append(transformation)
        
        # Transform passive voice
        for detection in analysis.detections:
            if detection.detection_type == "passive_voice":
                transformation = self._transform_passive_voice(detection.pattern_found)
                if transformation:
                    antidote_text = antidote_text.replace(
                        detection.pattern_found,
                        transformation.transformed
                    )
                    transformations.append(transformation)
        
        # Enhance Duygu
        duygu_enhanced = self._enhance_duygu(antidote_text, target_language)
        if duygu_enhanced != antidote_text:
            transformations.append(AntidoteTransformation(
                original=text,
                transformed=duygu_enhanced,
                transformation_type="duygu_enhancement",
                explanation="Enhanced emotional authenticity and cultural connection",
                duygu_enhancement="Added heart/soul language"
            ))
            antidote_text = duygu_enhanced
        
        # Add cultural anchors
        cultural_anchors = self._add_cultural_anchors(antidote_text, cultural_context)
        
        # Re-analyze to get new scores
        final_analysis = self.analyzer.analyze(antidote_text)
        
        # Calculate resistance score
        resistance_score = self._calculate_resistance_score(analysis, final_analysis)
        
        # Extract heritage connections
        heritage_connections = self._extract_heritage_connections(antidote_text)
        
        return AntidoteLanguage(
            original_text=text,
            antidote_text=antidote_text,
            transformations=transformations,
            cultural_anchors=cultural_anchors,
            duygu_score=final_analysis.duygu_analysis.duygu_score,
            authenticity_score=final_analysis.authenticity_score,
            resistance_score=resistance_score,
            heritage_connections=heritage_connections
        )
    
    def _transform_plastic_word(
        self,
        word: str,
        target_language: str,
        cultural_context: Optional[str]
    ) -> Optional[AntidoteTransformation]:
        """Transform a plastic word into antidote language."""
        word_lower = word.lower()
        
        if word_lower not in self.antidote_replacements:
            return None
        
        replacement = self.antidote_replacements[word_lower]
        
        if target_language == "turkish":
            transformed = replacement.get("turkish", word)
        elif target_language == "bilingual":
            transformed = f"{replacement.get('english', word)} ({replacement.get('turkish', '')})"
        else:
            transformed = replacement.get("cultural", replacement.get("english", word))
        
        return AntidoteTransformation(
            original=word,
            transformed=transformed,
            transformation_type="plastic_word_replacement",
            explanation=f"Replaced plastic word '{word}' with culturally-anchored term",
            cultural_anchoring=replacement.get("cultural", ""),
            duygu_enhancement=replacement.get("turkish", "")
        )
    
    def _transform_passive_voice(self, phrase: str) -> Optional[AntidoteTransformation]:
        """Transform passive voice to active voice."""
        phrase_lower = phrase.lower()
        
        if phrase_lower in self.active_voice_templates:
            transformed = self.active_voice_templates[phrase_lower]
            
            # Capitalize if original was capitalized
            if phrase[0].isupper():
                transformed = transformed.capitalize()
            
            return AntidoteTransformation(
                original=phrase,
                transformed=transformed,
                transformation_type="active_voice",
                explanation=f"Transformed passive voice to active: added clear actor",
                duygu_enhancement="Added human agency and accountability"
            )
        
        return None
    
    def _enhance_duygu(self, text: str, target_language: str) -> str:
        """Enhance emotional authenticity (Duygu) in text."""
        enhanced = text
        
        for english_term, enhancement in self.duygu_enhancements.items():
            pattern = r'\b' + re.escape(english_term) + r'\b'
            
            if target_language == "turkish":
                replacement = enhancement.split("(")[1].split(")")[0].strip() if "(" in enhancement else enhancement
            elif target_language == "bilingual":
                replacement = enhancement
            else:
                replacement = enhancement.split("(")[0].strip()
            
            enhanced = re.sub(pattern, replacement, enhanced, flags=re.IGNORECASE)
        
        return enhanced
    
    def _add_cultural_anchors(
        self,
        text: str,
        cultural_context: Optional[str]
    ) -> List[str]:
        """Add cultural anchoring phrases."""
        anchors = []
        
        # Turkish cultural anchors
        turkish_anchors = [
            "söz namustur",  # word is honor
            "gönül birliği",  # unity of heart
            "aile bağı",  # family bond
            "vatan sevgisi"  # love of homeland
        ]
        
        # Check if text already has cultural anchors
        text_lower = text.lower()
        for anchor in turkish_anchors:
            if anchor in text_lower:
                anchors.append(anchor)
        
        return anchors
    
    def _calculate_resistance_score(
        self,
        original_analysis: LinguisticAnalysis,
        final_analysis: LinguisticAnalysis
    ) -> float:
        """Calculate how well the antidote resists control entity language."""
        # Resistance = reduction in control score + increase in authenticity
        control_reduction = original_analysis.overall_control_score - final_analysis.overall_control_score
        authenticity_increase = final_analysis.authenticity_score - original_analysis.authenticity_score
        duygu_increase = final_analysis.duygu_analysis.duygu_score - original_analysis.duygu_analysis.duygu_score
        
        resistance_score = (
            control_reduction * 0.4 +
            authenticity_increase * 0.4 +
            duygu_increase * 0.2
        )
        
        return max(0.0, min(1.0, resistance_score))
    
    def _extract_heritage_connections(self, text: str) -> List[str]:
        """Extract heritage and ancestral connections from text."""
        heritage_terms = [
            "ancestors", "heritage", "tradition", "roots", "lineage",
            "atalar", "miras", "gelenek", "köken", "soy"
        ]
        
        connections = []
        text_lower = text.lower()
        
        for term in heritage_terms:
            if term in text_lower:
                connections.append(term)
        
        return connections
    
    def generate_antidote_charter(
        self,
        original_charter: str,
        organization_name: str,
        cultural_context: str = "turkish_english"
    ) -> AntidoteLanguage:
        """
        Generate antidote version of an organizational charter.
        
        Args:
            original_charter: Original charter text
            organization_name: Name of organization
            cultural_context: Cultural context for anchoring
            
        Returns:
            Complete antidote language result
        """
        logger.info(f"Generating antidote charter for {organization_name}")
        
        # Generate base antidote
        antidote = self.generate(
            original_charter,
            target_language="bilingual",
            cultural_context=cultural_context
        )
        
        # Add preamble with heritage connection
        heritage_preamble = f"""
        {organization_name} - Antidote Charter
        Rooted in the wisdom of our ancestors (atalarımızın bilgeliği)
        Honoring the word as honor (söz namustur)
        Serving with heart (gönül ile hizmet)
        
        """
        
        antidote.antidote_text = heritage_preamble + antidote.antidote_text
        
        return antidote


def main():
    """Main execution function."""
    setup_logging()
    
    generator = AntidoteLanguageGenerator()
    
    # Example: Transform control entity language
    sample_text = """
    The United Nations has determined that sustainable development goals must be implemented.
    Decisions were made to facilitate inclusive growth and resilient communities.
    Stakeholders will be engaged to optimize outcomes and maximize impact.
    """
    
    result = generator.generate(
        sample_text,
        target_language="bilingual",
        cultural_context="turkish_english"
    )
    
    print(f"\n{'='*60}")
    print("ANTIDOTE LANGUAGE GENERATION")
    print(f"{'='*60}\n")
    print(f"Original Control Score: {generator.analyzer.analyze(sample_text).overall_control_score:.2%}")
    print(f"Antidote Resistance Score: {result.resistance_score:.2%}")
    print(f"Duygu Score: {result.duygu_score:.2%}\n")
    
    print("ORIGINAL TEXT:")
    print(sample_text)
    print("\n" + "-"*60 + "\n")
    print("ANTIDOTE TEXT:")
    print(result.antidote_text)
    print("\n" + "-"*60 + "\n")
    
    print("TRANSFORMATIONS:")
    for transformation in result.transformations:
        print(f"  - {transformation.transformation_type}: {transformation.original} → {transformation.transformed}")
        print(f"    {transformation.explanation}\n")
    
    print(f"\nCultural Anchors: {', '.join(result.cultural_anchors) if result.cultural_anchors else 'None'}")
    print(f"Heritage Connections: {', '.join(result.heritage_connections) if result.heritage_connections else 'None'}")


if __name__ == "__main__":
    standard_main(main)
