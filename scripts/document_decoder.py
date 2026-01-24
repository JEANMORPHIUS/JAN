"""
DOCUMENT DECODER
Deep decode specific documents/charters for linguistic control patterns

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

PURPOSE:
Decode specific documents (UN 2030 Agenda, WEF charters, etc.) to reveal:
- Linguistic architecture of control
- Hidden actors and accountability removal
- Frequency paradoxes
- Semantic compression
- Esoteric etymology
- Generate complete antidote versions
"""

import sys
import json
import logging
from pathlib import Path
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, asdict
from datetime import datetime

# Add utils to path
sys.path.insert(0, str(Path(__file__).parent))

from utils import (
    Path, json, load_json, save_json,
    setup_logging, standard_main
)

from linguistic_control_analyzer import LinguisticControlAnalyzer
from antidote_language_generator import AntidoteLanguageGenerator

logger = logging.getLogger(__name__)


@dataclass
class DocumentDecode:
    """Complete document decoding result."""
    document_name: str
    source: str
    original_text: str
    analysis: Any  # LinguisticAnalysis
    antidote: Any  # AntidoteLanguage
    key_findings: List[str]
    control_architecture: Dict[str, Any]
    timestamp: datetime


class DocumentDecoder:
    """Decode specific documents for linguistic control patterns."""
    
    def __init__(self):
        """Initialize decoder with analyzers."""
        self.analyzer = LinguisticControlAnalyzer()
        self.generator = AntidoteLanguageGenerator()
        logger.info("Document Decoder initialized")
    
    def decode_document(
        self,
        document_name: str,
        text: str,
        source: str = "unknown",
        generate_antidote: bool = True
    ) -> DocumentDecode:
        """
        Decode a complete document.
        
        Args:
            document_name: Name of document
            text: Full document text
            source: Source/origin of document
            generate_antidote: Whether to generate antidote version
            
        Returns:
            Complete document decode result
        """
        logger.info(f"Decoding document: {document_name}")
        
        # Analyze
        analysis = self.analyzer.analyze(text)
        
        # Generate antidote if requested
        antidote = None
        if generate_antidote:
            antidote = self.generator.generate(
                text,
                target_language="bilingual",
                cultural_context="turkish_english"
            )
        
        # Extract key findings
        key_findings = self._extract_key_findings(analysis)
        
        # Map control architecture
        control_architecture = self._map_control_architecture(analysis)
        
        return DocumentDecode(
            document_name=document_name,
            source=source,
            original_text=text,
            analysis=analysis,
            antidote=antidote,
            key_findings=key_findings,
            control_architecture=control_architecture,
            timestamp=datetime.now()
        )
    
    def decode_un_2030_agenda(self, text: str) -> DocumentDecode:
        """Decode UN 2030 Agenda specifically."""
        return self.decode_document(
            "UN 2030 Agenda for Sustainable Development",
            text,
            source="United Nations",
            generate_antidote=True
        )
    
    def decode_wef_charter(self, text: str) -> DocumentDecode:
        """Decode WEF charter specifically."""
        return self.decode_document(
            "World Economic Forum Charter",
            text,
            source="World Economic Forum",
            generate_antidote=True
        )
    
    def decode_who_constitution(self, text: str) -> DocumentDecode:
        """Decode WHO constitution specifically."""
        return self.decode_document(
            "WHO Constitution",
            text,
            source="World Health Organization",
            generate_antidote=True
        )
    
    def _extract_key_findings(self, analysis: Any) -> List[str]:
        """Extract key findings from analysis."""
        findings = []
        
        # Control score findings
        if analysis.overall_control_score > 0.7:
            findings.append(f"High control score ({analysis.overall_control_score:.1%}) - Strong linguistic manipulation detected")
        elif analysis.overall_control_score > 0.4:
            findings.append(f"Moderate control score ({analysis.overall_control_score:.1%}) - Some linguistic manipulation present")
        
        # Plastic words
        if len(analysis.plastic_words_found) > 5:
            findings.append(f"Excessive plastic words ({len(analysis.plastic_words_found)}) - Semantic compression detected")
        
        # Passive voice
        if analysis.passive_voice.accountability_removal_score > 0.6:
            findings.append(f"High passive voice usage ({analysis.passive_voice.accountability_removal_score:.1%}) - Hidden actors detected")
        
        # Frequency paradox
        if analysis.frequency_analysis.paradox_score > 0.4:
            findings.append(f"Frequency paradox detected ({analysis.frequency_analysis.paradox_score:.1%}) - Words don't match actions")
        
        # Duygu depletion
        if analysis.duygu_analysis.duygu_score < 0.3:
            findings.append(f"Low Duygu score ({analysis.duygu_analysis.duygu_score:.1%}) - Emotional authenticity depleted")
        
        # Control entities
        if analysis.control_entity_indicators:
            findings.append(f"Control entities detected: {', '.join(analysis.control_entity_indicators)}")
        
        # Esoteric etymology
        if analysis.esoteric_etymology:
            findings.append(f"Esoteric etymology patterns found in {len(analysis.esoteric_etymology)} entity names")
        
        return findings
    
    def _map_control_architecture(self, analysis: Any) -> Dict[str, Any]:
        """Map the linguistic control architecture."""
        return {
            "plastic_word_layer": {
                "count": len(analysis.plastic_words_found),
                "words": analysis.plastic_words_found,
                "purpose": "Semantic compression - drain meaning"
            },
            "passive_voice_layer": {
                "score": analysis.passive_voice.accountability_removal_score,
                "purpose": "Remove actors, hide accountability"
            },
            "frequency_paradox_layer": {
                "score": analysis.frequency_analysis.paradox_score,
                "high_frequency_words": analysis.frequency_analysis.high_frequency_words,
                "low_frequency_actions": analysis.frequency_analysis.low_frequency_actions,
                "purpose": "Mask low-frequency actions with high-frequency words"
            },
            "duygu_depletion_layer": {
                "score": 1.0 - analysis.duygu_analysis.duygu_score,
                "authentic_emotion_count": analysis.duygu_analysis.authentic_emotion_count,
                "hollow_language_count": analysis.duygu_analysis.hollow_language_count,
                "purpose": "Remove emotional authenticity, replace with hollow language"
            },
            "control_entity_layer": {
                "entities": analysis.control_entity_indicators,
                "purpose": "Establish authority through entity names"
            },
            "esoteric_etymology_layer": {
                "etymologies": [
                    {
                        "entity": e.entity_name,
                        "esoteric_meaning": e.esoteric_meaning,
                        "frequency_implications": e.frequency_implications
                    }
                    for e in analysis.esoteric_etymology
                ],
                "purpose": "Bypass conscious mind through sigil-like names"
            }
        }
    
    def generate_report(self, decode: DocumentDecode, output_path: Optional[Path] = None) -> str:
        """Generate comprehensive decode report."""
        report = f"""
{'='*80}
DOCUMENT DECODE REPORT
{'='*80}

Document: {decode.document_name}
Source: {decode.source}
Date: {decode.timestamp.strftime('%Y-%m-%d %H:%M:%S')}

{'='*80}
EXECUTIVE SUMMARY
{'='*80}

Control Score: {decode.analysis.overall_control_score:.1%}
Authenticity Score: {decode.analysis.authenticity_score:.1%}
Duygu Score: {decode.analysis.duygu_analysis.duygu_score:.1%}

KEY FINDINGS:
"""
        for finding in decode.key_findings:
            report += f"  • {finding}\n"
        
        report += f"""
{'='*80}
CONTROL ARCHITECTURE
{'='*80}

"""
        for layer_name, layer_data in decode.control_architecture.items():
            report += f"{layer_name.upper().replace('_', ' ')}:\n"
            if isinstance(layer_data, dict):
                for key, value in layer_data.items():
                    if key != "purpose":
                        report += f"  {key}: {value}\n"
                if "purpose" in layer_data:
                    report += f"  Purpose: {layer_data['purpose']}\n"
            report += "\n"
        
        if decode.antidote:
            report += f"""
{'='*80}
ANTIDOTE LANGUAGE
{'='*80}

Resistance Score: {decode.antidote.resistance_score:.1%}
Duygu Score: {decode.antidote.duygu_score:.1%}

ORIGINAL TEXT (excerpt):
{decode.original_text[:500]}...

ANTIDOTE TEXT (excerpt):
{decode.antidote.antidote_text[:500]}...

TRANSFORMATIONS:
"""
            for transformation in decode.antidote.transformations[:10]:  # First 10
                report += f"  • {transformation.transformation_type}: {transformation.original} → {transformation.transformed}\n"
                report += f"    {transformation.explanation}\n"
        
        report += f"""
{'='*80}
END OF REPORT
{'='*80}
"""
        
        if output_path:
            output_path.write_text(report, encoding='utf-8')
            logger.info(f"Report saved to {output_path}")
        
        return report


def main():
    """Main execution function."""
    setup_logging()
    
    decoder = DocumentDecoder()
    
    # Example: Decode a sample document
    sample_text = """
    The United Nations 2030 Agenda for Sustainable Development represents a transformative
    framework for global cooperation. Through inclusive participation and resilient
    implementation, stakeholders will optimize outcomes to maximize impact. Decisions
    have been made to facilitate equitable growth across all sectors. It has been
    determined that sustainable practices must be integrated into all development
    initiatives. Measures will be implemented to ensure inclusive engagement of all
    stakeholders in the governance framework.
    """
    
    decode = decoder.decode_document(
        "Sample UN 2030 Agenda Excerpt",
        sample_text,
        source="Example",
        generate_antidote=True
    )
    
    # Generate report
    report = decoder.generate_report(decode)
    print(report)
    
    # Save to file
    output_dir = Path(__file__).parent.parent / "output" / "linguistic_decodes"
    output_dir.mkdir(parents=True, exist_ok=True)
    
    output_path = output_dir / f"decode_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    decoder.generate_report(decode, output_path)


if __name__ == "__main__":
    standard_main(main)
