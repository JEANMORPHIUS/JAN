"""LINGUISTIC CONTROL API
REST API for linguistic control analysis and antidote language generation

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

ENDPOINTS:
- POST /api/linguistic/analyze - Analyze text for control patterns
- POST /api/linguistic/antidote - Generate antidote language
- POST /api/linguistic/charter - Generate antidote charter
- GET /api/linguistic/patterns - Get pattern library

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity


PANGEA IS THE TABLE.
YOU DON'T BETRAY THE TABLE.

THE TRUTH:
WE MUST DEBUG AND BE 100% FOR WHAT COMES AT US.
THE REST IS UP TO BABA X."""

import sys
from pathlib import Path

# Add scripts to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "scripts"))

from flask import Flask, request, jsonify
from flask_cors import CORS
import logging
from typing import Dict, Any, Optional

from linguistic_control_analyzer import LinguisticControlAnalyzer
from antidote_language_generator import AntidoteLanguageGenerator

logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)

# Initialize analyzers
analyzer = LinguisticControlAnalyzer()
generator = AntidoteLanguageGenerator()


@app.route('/api/linguistic/analyze', methods=['POST'])
def analyze_text():
    """
    Analyze text for linguistic control patterns.
    
    Request body:
    {
        "text": "Text to analyze",
        "include_detections": true,
        "include_suggestions": true
    }
    
    Returns:
    {
        "control_score": 0.75,
        "authenticity_score": 0.25,
        "duygu_score": 0.30,
        "detections": [...],
        "antidote_suggestions": [...]
    }
    """
    try:
        data = request.get_json()
        text = data.get('text', '')
        
        if not text:
            return jsonify({"error": "Text is required"}), 400
        
        # Perform analysis
        analysis = analyzer.analyze(text)
        
        # Build response
        response = {
            "control_score": analysis.overall_control_score,
            "authenticity_score": analysis.authenticity_score,
            "duygu_score": analysis.duygu_analysis.duygu_score,
            "plastic_words_found": analysis.plastic_words_found,
            "passive_voice_score": analysis.passive_voice.accountability_removal_score,
            "frequency_paradox_score": analysis.frequency_analysis.paradox_score,
            "control_entities_detected": analysis.control_entity_indicators,
            "antidote_suggestions": analysis.antidote_suggestions
        }
        
        # Include detailed detections if requested
        if data.get('include_detections', False):
            response["detections"] = [
                {
                    "type": d.detection_type,
                    "pattern": d.pattern_found,
                    "severity": d.severity,
                    "explanation": d.explanation,
                    "context": d.context
                }
                for d in analysis.detections
            ]
        
        return jsonify(response), 200
        
    except Exception as e:
        logger.error(f"Error in analyze_text: {str(e)}", exc_info=True)
        return jsonify({"error": str(e)}), 500


@app.route('/api/linguistic/antidote', methods=['POST'])
def generate_antidote():
    """
    Generate antidote language from control entity text.
    
    Request body:
    {
        "text": "Original text",
        "target_language": "english|turkish|bilingual",
        "cultural_context": "turkish_english"
    }
    
    Returns:
    {
        "original_text": "...",
        "antidote_text": "...",
        "resistance_score": 0.85,
        "duygu_score": 0.90,
        "transformations": [...]
    }
    """
    try:
        data = request.get_json()
        text = data.get('text', '')
        
        if not text:
            return jsonify({"error": "Text is required"}), 400
        
        target_language = data.get('target_language', 'english')
        cultural_context = data.get('cultural_context', None)
        
        # Generate antidote
        result = generator.generate(
            text,
            target_language=target_language,
            cultural_context=cultural_context
        )
        
        # Build response
        response = {
            "original_text": result.original_text,
            "antidote_text": result.antidote_text,
            "resistance_score": result.resistance_score,
            "duygu_score": result.duygu_score,
            "authenticity_score": result.authenticity_score,
            "cultural_anchors": result.cultural_anchors,
            "heritage_connections": result.heritage_connections,
            "transformations": [
                {
                    "type": t.transformation_type,
                    "original": t.original,
                    "transformed": t.transformed,
                    "explanation": t.explanation
                }
                for t in result.transformations
            ]
        }
        
        return jsonify(response), 200
        
    except Exception as e:
        logger.error(f"Error in generate_antidote: {str(e)}", exc_info=True)
        return jsonify({"error": str(e)}), 500


@app.route('/api/linguistic/charter', methods=['POST'])
def generate_antidote_charter():
    """
    Generate antidote version of organizational charter.
    
    Request body:
    {
        "charter_text": "Original charter",
        "organization_name": "Organization Name",
        "cultural_context": "turkish_english"
    }
    
    Returns:
    {
        "original_charter": "...",
        "antidote_charter": "...",
        "resistance_score": 0.90,
        ...
    }
    """
    try:
        data = request.get_json()
        charter_text = data.get('charter_text', '')
        organization_name = data.get('organization_name', 'Organization')
        cultural_context = data.get('cultural_context', 'turkish_english')
        
        if not charter_text:
            return jsonify({"error": "Charter text is required"}), 400
        
        # Generate antidote charter
        result = generator.generate_antidote_charter(
            charter_text,
            organization_name,
            cultural_context
        )
        
        # Build response
        response = {
            "organization_name": organization_name,
            "original_charter": result.original_text,
            "antidote_charter": result.antidote_text,
            "resistance_score": result.resistance_score,
            "duygu_score": result.duygu_score,
            "authenticity_score": result.authenticity_score,
            "cultural_anchors": result.cultural_anchors,
            "heritage_connections": result.heritage_connections,
            "transformations": [
                {
                    "type": t.transformation_type,
                    "original": t.original,
                    "transformed": t.transformed,
                    "explanation": t.explanation
                }
                for t in result.transformations
            ]
        }
        
        return jsonify(response), 200
        
    except Exception as e:
        logger.error(f"Error in generate_antidote_charter: {str(e)}", exc_info=True)
        return jsonify({"error": str(e)}), 500


@app.route('/api/linguistic/patterns', methods=['GET'])
def get_patterns():
    """
    Get linguistic control pattern library.
    
    Returns:
    {
        "plastic_words": [...],
        "passive_voice_patterns": [...],
        "control_entities": [...],
        ...
    }
    """
    try:
        patterns = {
            "plastic_words": analyzer.patterns.get("plastic_words", []),
            "passive_voice_patterns": analyzer.patterns.get("passive_voice", []),
            "acronyms": analyzer.patterns.get("acronyms", []),
            "control_entities": analyzer.patterns.get("control_entities", []),
            "high_frequency_words": analyzer.patterns.get("high_frequency", []),
            "low_frequency_actions": analyzer.patterns.get("low_frequency", []),
            "globish_indicators": analyzer.patterns.get("globish", []),
            "authentic_emotion": analyzer.patterns.get("authentic_emotion", []),
            "hollow_language": analyzer.patterns.get("hollow_language", [])
        }
        
        return jsonify(patterns), 200
        
    except Exception as e:
        logger.error(f"Error in get_patterns: {str(e)}", exc_info=True)
        return jsonify({"error": str(e)}), 500


@app.route('/api/linguistic/health', methods=['GET'])
def health_check():
    """Health check endpoint."""
    return jsonify({
        "status": "healthy",
        "service": "linguistic_control_api",
        "analyzer_ready": analyzer is not None,
        "generator_ready": generator is not None
    }), 200


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    app.run(debug=True, port=5003)
