"""
QUICK TEST - LINGUISTIC CONTROL SYSTEM
Test all components of the linguistic analysis system

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY
"""

import sys
import io
from pathlib import Path

# Set UTF-8 encoding for Windows console
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

# Add scripts to path
sys.path.insert(0, str(Path(__file__).parent))

from linguistic_control_analyzer import LinguisticControlAnalyzer
from antidote_language_generator import AntidoteLanguageGenerator
from document_decoder import DocumentDecoder

def test_basic_analysis():
    """Test basic linguistic analysis."""
    print("\n" + "="*80)
    print("TEST 1: BASIC LINGUISTIC ANALYSIS")
    print("="*80 + "\n")
    
    analyzer = LinguisticControlAnalyzer()
    
    sample_text = """
    The United Nations has determined that sustainable development goals must be implemented.
    Decisions were made to facilitate inclusive growth and resilient communities.
    Stakeholders will be engaged to optimize outcomes and maximize impact.
    """
    
    result = analyzer.analyze(sample_text)
    
    print(f"Control Score: {result.overall_control_score:.1%}")
    print(f"Authenticity Score: {result.authenticity_score:.1%}")
    print(f"Duygu Score: {result.duygu_analysis.duygu_score:.1%}\n")
    
    print(f"Plastic Words Found: {result.plastic_words_found}")
    print(f"Passive Voice Score: {result.passive_voice.accountability_removal_score:.1%}")
    print(f"Frequency Paradox Score: {result.frequency_analysis.paradox_score:.1%}")
    print(f"Control Entities: {result.control_entity_indicators}\n")
    
    print(f"Total Detections: {len(result.detections)}")
    for detection in result.detections[:5]:
        print(f"  - {detection.detection_type}: {detection.pattern_found}")
    
    print("\n[PASS] Basic analysis test passed!")


def test_antidote_generation():
    """Test antidote language generation."""
    print("\n" + "="*80)
    print("TEST 2: ANTIDOTE LANGUAGE GENERATION")
    print("="*80 + "\n")
    
    generator = AntidoteLanguageGenerator()
    
    original = "Decisions were made to facilitate sustainable development through inclusive stakeholder engagement."
    
    print("ORIGINAL TEXT:")
    print(original)
    print("\n" + "-"*80 + "\n")
    
    antidote = generator.generate(
        original,
        target_language="bilingual",
        cultural_context="turkish_english"
    )
    
    print("ANTIDOTE TEXT:")
    try:
        print(antidote.antidote_text)
    except UnicodeEncodeError:
        print(antidote.antidote_text.encode('ascii', 'ignore').decode('ascii'))
    print("\n" + "-"*80 + "\n")
    
    print(f"Resistance Score: {antidote.resistance_score:.1%}")
    print(f"Duygu Score: {antidote.duygu_score:.1%}")
    print(f"Authenticity Score: {antidote.authenticity_score:.1%}\n")
    
    print("TRANSFORMATIONS:")
    for transformation in antidote.transformations:
        print(f"  - {transformation.transformation_type}")
        print(f"    {transformation.original} -> {transformation.transformed}")
    
    print("\n[PASS] Antidote generation test passed!")


def test_document_decoding():
    """Test document decoding."""
    print("\n" + "="*80)
    print("TEST 3: DOCUMENT DECODING")
    print("="*80 + "\n")
    
    decoder = DocumentDecoder()
    
    sample_charter = """
    The World Economic Forum Charter
    
    We are committed to sustainable transformation through inclusive stakeholder engagement.
    Decisions have been made to facilitate resilient communities and optimize global outcomes.
    Our framework enables synergistic collaboration across all sectors.
    Measures will be implemented to ensure equitable distribution of resources.
    """
    
    decode = decoder.decode_document(
        "Sample WEF Charter",
        sample_charter,
        source="World Economic Forum",
        generate_antidote=True
    )
    
    print(f"Document: {decode.document_name}")
    print(f"Control Score: {decode.analysis.overall_control_score:.1%}")
    print(f"Duygu Score: {decode.analysis.duygu_analysis.duygu_score:.1%}\n")
    
    print("KEY FINDINGS:")
    for finding in decode.key_findings:
        print(f"  - {finding}")
    
    print("\nCONTROL ARCHITECTURE LAYERS:")
    for layer_name in decode.control_architecture.keys():
        print(f"  - {layer_name.replace('_', ' ').title()}")
    
    if decode.antidote:
        print(f"\nAntidote Resistance Score: {decode.antidote.resistance_score:.1%}")
    
    print("\n[PASS] Document decoding test passed!")


def main():
    """Run all tests."""
    print("\n" + "="*80)
    print("LINGUISTIC CONTROL SYSTEM - COMPREHENSIVE TEST")
    print("="*80)
    
    try:
        test_basic_analysis()
        test_antidote_generation()
        test_document_decoding()
        
        print("\n" + "="*80)
        print("[PASS] ALL TESTS PASSED - SYSTEM OPERATIONAL")
        print("="*80 + "\n")
        
    except Exception as e:
        print(f"\n[FAIL] TEST FAILED: {str(e)}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
