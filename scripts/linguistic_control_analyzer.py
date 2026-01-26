"""LINGUISTIC CONTROL ANALYZER
Deep Analysis of Control Entity Language Architecture

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
Decode the linguistic architecture used by Control-Based Entities (CBEs) to:
- Detect semantic compression and plastic words
- Identify passive voice and hidden actors
- Analyze frequency paradoxes (high-frequency words, low-frequency actions)
- Uncover esoteric etymology in entity names
- Measure Duygu (emotional authenticity) vs hollow language
- Generate Antidote Language that cannot be "uninstalled"

LAYERS OF ANALYSIS:
1. Plastic Word Protocol (Semantic Compression)
2. Tower of Babel Reverse Engineering (Globish Detection)
3. Occult Branding (Esoteric Etymology)
4. Frequency Paradox Detection
5. Duygu Debugger (Emotional Content Analysis)
6. Antidote Language Generation

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity


PANGEA IS THE TABLE.
YOU DON'T BETRAY THE TABLE.

THE TRUTH:
WE MUST DEBUG AND BE 100% FOR WHAT COMES AT US.
THE REST IS UP TO BABA X."""

import sys
import re
import json
import logging
from pathlib import Path
from typing import Dict, List, Optional, Any, Tuple, Set
from dataclasses import dataclass, asdict, field
from datetime import datetime
from collections import Counter, defaultdict
from enum import Enum

# Add utils to path
sys.path.insert(0, str(Path(__file__).parent))

from utils import (
    Path, json, load_json, save_json,
    setup_logging, standard_main
)

logger = logging.getLogger(__name__)


class LinguisticControlType(Enum):
    """Types of linguistic control detected."""
    PLASTIC_WORD = "plastic_word"
    PASSIVE_VOICE = "passive_voice"
    ACRONYM_OVERLOAD = "acronym_overload"
    VERBIFICATION = "verbification"
    FREQUENCY_PARADOX = "frequency_paradox"
    GLOBISH = "globish"
    SEMANTIC_COMPRESSION = "semantic_compression"
    DUYGU_DEPLETION = "duygu_depletion"
    HIDDEN_ACTOR = "hidden_actor"
    ESOTERIC_ETYMOLOGY = "esoteric_etymology"


@dataclass
class LinguisticDetection:
    """Single detection of linguistic control pattern."""
    detection_type: str
    pattern_found: str
    context: str
    severity: float  # 0.0 to 1.0
    explanation: str
    location: Tuple[int, int]  # (start, end) character positions


@dataclass
class FrequencyAnalysis:
    """Analysis of frequency patterns in text."""
    high_frequency_words: List[str]
    low_frequency_actions: List[str]
    paradox_score: float  # 0.0 to 1.0
    semantic_distance: float
    frequency_gap: float


@dataclass
class DuyguAnalysis:
    """Analysis of emotional authenticity (Duygu = emotion in Turkish)."""
    authentic_emotion_count: int
    hollow_language_count: int
    emotional_density: float  # 0.0 to 1.0
    frequency_authenticity: float
    cultural_anchoring: bool
    duygu_score: float  # Higher = more authentic


@dataclass
class PassiveVoiceDetection:
    """Detection of passive voice patterns."""
    passive_phrases: List[str]
    hidden_actors: List[str]
    accountability_removal_score: float
    actor_clarity_score: float  # Lower = more hidden


@dataclass
class EsotericEtymology:
    """Esoteric etymology analysis."""
    entity_name: str
    phonetic_analysis: str
    etymological_roots: List[str]
    esoteric_meaning: str
    frequency_implications: str
    sigil_function: bool  # Does it function as a sigil?


@dataclass
class LinguisticAnalysis:
    """Complete linguistic analysis result."""
    text: str
    timestamp: datetime
    detections: List[LinguisticDetection]
    plastic_words_found: List[str]
    passive_voice: PassiveVoiceDetection
    frequency_analysis: FrequencyAnalysis
    duygu_analysis: DuyguAnalysis
    esoteric_etymology: List[EsotericEtymology]
    control_entity_indicators: List[str]
    overall_control_score: float  # 0.0 to 1.0
    authenticity_score: float  # 0.0 to 1.0
    antidote_suggestions: List[str]


class LinguisticControlAnalyzer:
    """Main analyzer for linguistic control patterns."""
    
    def __init__(self, config_path: Optional[Path] = None):
        """Initialize analyzer with pattern configuration."""
        if config_path is None:
            config_path = Path(__file__).parent.parent / "config" / "linguistic_control_patterns.json"
        
        self.config = load_json(config_path)
        self.patterns = self._load_patterns()
        logger.info(f"Linguistic Control Analyzer initialized with {len(self.patterns)} pattern categories")
    
    def _load_patterns(self) -> Dict[str, Any]:
        """Load and structure pattern data."""
        return {
            "plastic_words": self.config.get("plastic_words", {}).get("patterns", []),
            "passive_voice": self.config.get("passive_voice_patterns", {}).get("patterns", []),
            "acronyms": self.config.get("acronym_overload", {}).get("patterns", []),
            "verbification": self.config.get("verbification", {}).get("patterns", []),
            "high_frequency": self.config.get("frequency_paradox", {}).get("high_frequency_words", []),
            "low_frequency": self.config.get("frequency_paradox", {}).get("low_frequency_actions", []),
            "globish": self.config.get("globish_indicators", {}).get("patterns", []),
            "authentic_emotion": self.config.get("duygu_indicators", {}).get("authentic_emotion", []),
            "hollow_language": self.config.get("duygu_indicators", {}).get("hollow_language", []),
            "control_entities": self._extract_control_entities(),
            "esoteric_etymology": self.config.get("esoteric_etymology", {}).get("patterns", {})
        }
    
    def _extract_control_entities(self) -> List[str]:
        """Extract all control entity names from config."""
        entities = []
        control_entities = self.config.get("control_entities", {})
        for category in control_entities.values():
            entities.extend(category.get("entities", []))
        return list(set(entities))
    
    def analyze(self, text: str) -> LinguisticAnalysis:
        """
        Perform complete linguistic analysis on text.
        
        Args:
            text: Text to analyze
            
        Returns:
            Complete linguistic analysis result
        """
        logger.info(f"Analyzing text ({len(text)} characters)")
        
        detections = []
        
        # Layer 1: Plastic Word Detection
        plastic_words = self._detect_plastic_words(text)
        detections.extend(plastic_words)
        
        # Layer 2: Passive Voice Detection
        passive_voice = self._detect_passive_voice(text)
        detections.extend(passive_voice["detections"])
        
        # Layer 3: Acronym Overload
        acronym_detections = self._detect_acronym_overload(text)
        detections.extend(acronym_detections)
        
        # Layer 4: Verbification
        verbification_detections = self._detect_verbification(text)
        detections.extend(verbification_detections)
        
        # Layer 5: Frequency Paradox
        frequency_analysis = self._analyze_frequency_paradox(text)
        
        # Layer 6: Duygu Analysis
        duygu_analysis = self._analyze_duygu(text)
        
        # Layer 7: Esoteric Etymology
        esoteric_etymology = self._analyze_esoteric_etymology(text)
        
        # Layer 8: Control Entity Indicators
        control_indicators = self._detect_control_entities(text)
        
        # Calculate overall scores
        control_score = self._calculate_control_score(detections, frequency_analysis, duygu_analysis)
        authenticity_score = 1.0 - control_score
        
        # Generate antidote suggestions
        antidote_suggestions = self._generate_antidote_suggestions(
            detections, frequency_analysis, duygu_analysis
        )
        
        return LinguisticAnalysis(
            text=text,
            timestamp=datetime.now(),
            detections=detections,
            plastic_words_found=[d.pattern_found for d in detections if d.detection_type == LinguisticControlType.PLASTIC_WORD.value],
            passive_voice=PassiveVoiceDetection(
                passive_phrases=passive_voice["phrases"],
                hidden_actors=passive_voice["hidden_actors"],
                accountability_removal_score=passive_voice["score"],
                actor_clarity_score=1.0 - passive_voice["score"]
            ),
            frequency_analysis=frequency_analysis,
            duygu_analysis=duygu_analysis,
            esoteric_etymology=esoteric_etymology,
            control_entity_indicators=control_indicators,
            overall_control_score=control_score,
            authenticity_score=authenticity_score,
            antidote_suggestions=antidote_suggestions
        )
    
    def _detect_plastic_words(self, text: str) -> List[LinguisticDetection]:
        """Detect plastic words (semantic compression)."""
        detections = []
        text_lower = text.lower()
        
        for word in self.patterns["plastic_words"]:
            pattern = r'\b' + re.escape(word) + r'\b'
            matches = list(re.finditer(pattern, text_lower, re.IGNORECASE))
            
            for match in matches:
                context_start = max(0, match.start() - 50)
                context_end = min(len(text), match.end() + 50)
                context = text[context_start:context_end]
                
                detections.append(LinguisticDetection(
                    detection_type=LinguisticControlType.PLASTIC_WORD.value,
                    pattern_found=word,
                    context=context,
                    severity=0.7,  # Plastic words are moderately severe
                    explanation=f"Plastic word detected: '{word}' - drained of specific meaning, can be installed into any language",
                    location=(match.start(), match.end())
                ))
        
        return detections
    
    def _detect_passive_voice(self, text: str) -> Dict[str, Any]:
        """Detect passive voice patterns and hidden actors."""
        detections = []
        passive_phrases = []
        hidden_actors = []
        
        # Check for known passive voice patterns
        for pattern in self.patterns["passive_voice"]:
            if pattern.lower() in text.lower():
                passive_phrases.append(pattern)
                detections.append(LinguisticDetection(
                    detection_type=LinguisticControlType.PASSIVE_VOICE.value,
                    pattern_found=pattern,
                    context=pattern,
                    severity=0.8,
                    explanation=f"Passive voice pattern detected: '{pattern}' - actor removed, accountability hidden",
                    location=(text.lower().find(pattern.lower()), text.lower().find(pattern.lower()) + len(pattern))
                ))
        
        # Detect passive voice using grammar patterns
        passive_indicators = ["were", "was", "been", "being", "is", "are", "will be"]
        sentences = re.split(r'[.!?]+', text)
        
        for sentence in sentences:
            sentence_lower = sentence.lower().strip()
            if any(indicator in sentence_lower for indicator in passive_indicators):
                # Check if sentence lacks clear subject performing action
                if not self._has_clear_actor(sentence):
                    passive_phrases.append(sentence.strip())
                    hidden_actors.append("Unknown")
                    detections.append(LinguisticDetection(
                        detection_type=LinguisticControlType.HIDDEN_ACTOR.value,
                        pattern_found=sentence.strip(),
                        context=sentence.strip(),
                        severity=0.6,
                        explanation=f"Hidden actor detected: sentence lacks clear subject performing action",
                        location=(text.find(sentence), text.find(sentence) + len(sentence))
                    ))
        
        score = min(len(passive_phrases) / max(len(sentences), 1), 1.0)
        
        return {
            "detections": detections,
            "phrases": passive_phrases,
            "hidden_actors": hidden_actors,
            "score": score
        }
    
    def _has_clear_actor(self, sentence: str) -> bool:
        """Check if sentence has a clear actor performing the action."""
        # Simple heuristic: check for personal pronouns or named entities before verb
        personal_pronouns = ["i", "you", "he", "she", "we", "they", "it"]
        words = sentence.lower().split()
        
        # Check for pronouns or capitalized words (likely names/entities)
        for i, word in enumerate(words[:5]):  # Check first 5 words
            if word in personal_pronouns or (word[0].isupper() if word else False):
                return True
        
        return False
    
    def _detect_acronym_overload(self, text: str) -> List[LinguisticDetection]:
        """Detect excessive use of acronyms."""
        detections = []
        words = text.split()
        total_words = len(words)
        
        if total_words == 0:
            return detections
        
        acronym_count = 0
        acronym_positions = []
        
        # Find acronyms (all caps, 2-5 letters, possibly with periods)
        acronym_pattern = r'\b[A-Z]{2,5}(?:\.[A-Z]{2,5})*\b'
        matches = list(re.finditer(acronym_pattern, text))
        
        for match in matches:
            acronym = match.group()
            # Check if it's a known control entity acronym
            if acronym in self.patterns["acronyms"]:
                acronym_count += 1
                acronym_positions.append((match.start(), match.end()))
        
        acronym_density = acronym_count / total_words
        
        # Threshold from config
        threshold = self.config.get("acronym_overload", {}).get("detection_rules", {}).get("density_threshold", 0.15)
        
        if acronym_density > threshold:
            for start, end in acronym_positions:
                context_start = max(0, start - 30)
                context_end = min(len(text), end + 30)
                context = text[context_start:context_end]
                
                detections.append(LinguisticDetection(
                    detection_type=LinguisticControlType.ACRONYM_OVERLOAD.value,
                    pattern_found=text[start:end],
                    context=context,
                    severity=min(acronym_density / threshold, 1.0),
                    explanation=f"Acronym overload detected: density {acronym_density:.2%} exceeds threshold {threshold:.2%} - creates barrier to understanding",
                    location=(start, end)
                ))
        
        return detections
    
    def _detect_verbification(self, text: str) -> List[LinguisticDetection]:
        """Detect verbification of brands/entities."""
        detections = []
        text_lower = text.lower()
        
        for pattern in self.patterns["verbification"]:
            if pattern in text_lower:
                matches = list(re.finditer(re.escape(pattern), text_lower))
                for match in matches:
                    context_start = max(0, match.start() - 30)
                    context_end = min(len(text), match.end() + 30)
                    context = text[context_start:context_end]
                    
                    detections.append(LinguisticDetection(
                        detection_type=LinguisticControlType.VERBIFICATION.value,
                        pattern_found=pattern,
                        context=context,
                        severity=0.7,
                        explanation=f"Verbification detected: '{pattern}' - brand used as verb, overwrites human agency",
                        location=(match.start(), match.end())
                    ))
        
        return detections
    
    def _analyze_frequency_paradox(self, text: str) -> FrequencyAnalysis:
        """Analyze frequency paradox (high-frequency words, low-frequency actions)."""
        text_lower = text.lower()
        words = re.findall(r'\b\w+\b', text_lower)
        word_counter = Counter(words)
        
        high_freq_found = []
        low_freq_found = []
        
        for word in self.patterns["high_frequency"]:
            if word in word_counter:
                high_freq_found.append(word)
        
        for word in self.patterns["low_frequency"]:
            if word in word_counter:
                low_freq_found.append(word)
        
        # Calculate paradox score
        high_freq_count = len(high_freq_found)
        low_freq_count = len(low_freq_found)
        total_unique_words = len(set(words))
        
        if total_unique_words == 0:
            return FrequencyAnalysis(
                high_frequency_words=[],
                low_frequency_actions=[],
                paradox_score=0.0,
                semantic_distance=0.0,
                frequency_gap=0.0
            )
        
        paradox_score = min((high_freq_count + low_freq_count) / max(total_unique_words, 1), 1.0)
        semantic_distance = abs(high_freq_count - low_freq_count) / max(total_unique_words, 1)
        frequency_gap = high_freq_count / max(total_unique_words, 1) if total_unique_words > 0 else 0.0
        
        return FrequencyAnalysis(
            high_frequency_words=high_freq_found,
            low_frequency_actions=low_freq_found,
            paradox_score=paradox_score,
            semantic_distance=semantic_distance,
            frequency_gap=frequency_gap
        )
    
    def _analyze_duygu(self, text: str) -> DuyguAnalysis:
        """Analyze emotional authenticity (Duygu = emotion in Turkish)."""
        text_lower = text.lower()
        words = re.findall(r'\b\w+\b', text_lower)
        
        authentic_count = sum(1 for word in words if word in self.patterns["authentic_emotion"])
        hollow_count = sum(1 for word in words if word in self.patterns["hollow_language"])
        
        total_words = len(words)
        if total_words == 0:
            return DuyguAnalysis(
                authentic_emotion_count=0,
                hollow_language_count=0,
                emotional_density=0.0,
                frequency_authenticity=0.0,
                cultural_anchoring=False,
                duygu_score=0.0
            )
        
        emotional_density = authentic_count / total_words
        frequency_authenticity = authentic_count / max(authentic_count + hollow_count, 1)
        
        # Check for cultural anchoring (Turkish words, heritage terms, etc.)
        cultural_indicators = ["duygu", "gönül", "söz", "namus", "şeref", "onur", "aile", "vatan"]
        cultural_anchoring = any(indicator in text_lower for indicator in cultural_indicators)
        
        # Duygu score: higher = more authentic
        duygu_score = (emotional_density * 0.5) + (frequency_authenticity * 0.3) + (0.2 if cultural_anchoring else 0.0)
        
        return DuyguAnalysis(
            authentic_emotion_count=authentic_count,
            hollow_language_count=hollow_count,
            emotional_density=emotional_density,
            frequency_authenticity=frequency_authenticity,
            cultural_anchoring=cultural_anchoring,
            duygu_score=min(duygu_score, 1.0)
        )
    
    def _analyze_esoteric_etymology(self, text: str) -> List[EsotericEtymology]:
        """Analyze esoteric etymology of entity names found in text."""
        etymologies = []
        text_upper = text.upper()
        
        esoteric_patterns = self.patterns.get("esoteric_etymology", {})
        
        for entity_name, analysis in esoteric_patterns.items():
            if entity_name in text_upper:
                etymologies.append(EsotericEtymology(
                    entity_name=entity_name,
                    phonetic_analysis=analysis.get("phonetic", ""),
                    etymological_roots=analysis.get("etymology", "").split() if isinstance(analysis.get("etymology"), str) else [],
                    esoteric_meaning=analysis.get("esoteric", ""),
                    frequency_implications=analysis.get("frequency", ""),
                    sigil_function=analysis.get("sigil_function", False)
                ))
        
        return etymologies
    
    def _detect_control_entities(self, text: str) -> List[str]:
        """Detect mentions of control entities."""
        found_entities = []
        text_upper = text.upper()
        
        for entity in self.patterns["control_entities"]:
            if entity.upper() in text_upper:
                found_entities.append(entity)
        
        return found_entities
    
    def _calculate_control_score(
        self,
        detections: List[LinguisticDetection],
        frequency_analysis: FrequencyAnalysis,
        duygu_analysis: DuyguAnalysis
    ) -> float:
        """Calculate overall control score (0.0 to 1.0)."""
        if not detections:
            return 0.0
        
        # Weight different factors
        detection_score = sum(d.severity for d in detections) / max(len(detections), 1)
        frequency_score = frequency_analysis.paradox_score
        duygu_score = 1.0 - duygu_analysis.duygu_score  # Invert: low duygu = high control
        
        # Weighted average
        control_score = (
            detection_score * 0.4 +
            frequency_score * 0.3 +
            duygu_score * 0.3
        )
        
        return min(control_score, 1.0)
    
    def _generate_antidote_suggestions(
        self,
        detections: List[LinguisticDetection],
        frequency_analysis: FrequencyAnalysis,
        duygu_analysis: DuyguAnalysis
    ) -> List[str]:
        """Generate antidote language suggestions."""
        suggestions = []
        
        # Suggest replacing plastic words
        plastic_detections = [d for d in detections if d.detection_type == LinguisticControlType.PLASTIC_WORD.value]
        if plastic_detections:
            suggestions.append("Replace plastic words with specific, culturally-anchored terms")
            suggestions.append("Use local language and cultural expressions instead of Globish")
        
        # Suggest adding actors to passive voice
        passive_detections = [d for d in detections if d.detection_type == LinguisticControlType.PASSIVE_VOICE.value]
        if passive_detections:
            suggestions.append("Add clear actors to passive voice constructions")
            suggestions.append("Use active voice: 'We decided' instead of 'It was decided'")
        
        # Suggest increasing Duygu
        if duygu_analysis.duygu_score < 0.5:
            suggestions.append("Increase emotional authenticity (Duygu)")
            suggestions.append("Use words that connect to heart, soul, and cultural heritage")
            suggestions.append("Replace corporate jargon with human language")
        
        # Suggest addressing frequency paradox
        if frequency_analysis.paradox_score > 0.3:
            suggestions.append("Align high-frequency words with actual actions")
            suggestions.append("If using 'peace', ensure peaceful actions follow")
            suggestions.append("Bridge the gap between word and deed")
        
        return suggestions


def main():
    """Main execution function."""
    setup_logging()
    
    analyzer = LinguisticControlAnalyzer()
    
    # Example analysis
    sample_text = """
    The United Nations has determined that sustainable development goals must be implemented.
    Decisions were made to facilitate inclusive growth and resilient communities.
    Stakeholders will be engaged to optimize outcomes and maximize impact.
    """
    
    result = analyzer.analyze(sample_text)
    
    print(f"\n{'='*60}")
    print("LINGUISTIC CONTROL ANALYSIS")
    print(f"{'='*60}\n")
    print(f"Control Score: {result.overall_control_score:.2%}")
    print(f"Authenticity Score: {result.authenticity_score:.2%}")
    print(f"Duygu Score: {result.duygu_analysis.duygu_score:.2%}\n")
    
    print(f"Detections: {len(result.detections)}")
    for detection in result.detections[:5]:  # Show first 5
        print(f"  - {detection.detection_type}: {detection.pattern_found}")
        print(f"    {detection.explanation}\n")
    
    print(f"\nAntidote Suggestions:")
    for suggestion in result.antidote_suggestions:
        print(f"  - {suggestion}")


if __name__ == "__main__":
    standard_main(main)
