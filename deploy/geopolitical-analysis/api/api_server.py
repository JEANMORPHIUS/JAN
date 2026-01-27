"""
GEOPOLITICAL ANALYSIS API SERVER
Public REST API for Geopolitical Analysis Engine

STATUS: PUBLIC DEPLOYMENT
SEPARATE FROM: Oracle System
"""

from flask import Flask, request, jsonify
from datetime import datetime
from typing import Dict, Any, Optional
import logging

from geopolitical_analysis_engine import (
    GeopoliticalAnalysisEngine,
    analyze_region
)

logger = logging.getLogger(__name__)

app = Flask(__name__)

# Initialize engine
engine = GeopoliticalAnalysisEngine()


@app.route('/api/geopolitical/analyze/<region>', methods=['GET'])
def analyze_region_endpoint(region: str):
    """
    Analyze a region comprehensively.
    
    Returns comprehensive analysis including:
    - Border dynamics
    - Hostile mappings
    - Help-seeking paradoxes
    - Strategic loyalty
    - Overall risk assessment
    - Recommendations
    """
    try:
        analysis = engine.generate_comprehensive_analysis(region)
        return jsonify(analysis), 200
    except Exception as e:
        logger.error(f"Error analyzing region {region}: {e}")
        return jsonify({"error": str(e)}), 500


@app.route('/api/geopolitical/border-dynamics/<region>', methods=['GET'])
def get_border_dynamics(region: str):
    """
    Get border dynamics analysis for a region.
    
    Query params:
    - timeframe_days: Number of days to analyze (default: 30)
    """
    try:
        timeframe_days = int(request.args.get('timeframe_days', 30))
        analysis = engine.analyze_border_dynamics(region, timeframe_days)
        return jsonify(analysis), 200
    except Exception as e:
        logger.error(f"Error analyzing border dynamics for {region}: {e}")
        return jsonify({"error": str(e)}), 500


@app.route('/api/geopolitical/hostile-mapping/<territory>', methods=['GET'])
def get_hostile_mappings(territory: str):
    """
    Get hostile mapping incidents for a territory.
    """
    try:
        mappings = engine.detect_hostile_mapping(territory)
        return jsonify(mappings), 200
    except Exception as e:
        logger.error(f"Error detecting hostile mappings for {territory}: {e}")
        return jsonify({"error": str(e)}), 500


@app.route('/api/geopolitical/help-seeking-paradox/<region>', methods=['GET'])
def get_help_seeking_paradoxes(region: str):
    """
    Get help-seeking paradox analysis for a region.
    """
    try:
        paradoxes = engine.analyze_help_seeking_paradox(region)
        return jsonify(paradoxes), 200
    except Exception as e:
        logger.error(f"Error analyzing help-seeking paradoxes for {region}: {e}")
        return jsonify({"error": str(e)}), 500


@app.route('/api/geopolitical/strategic-loyalty/<entity>', methods=['GET'])
def get_strategic_loyalty(entity: str):
    """
    Get strategic loyalty assessment for an entity.
    """
    try:
        loyalty = engine.assess_strategic_loyalty(entity)
        return jsonify(loyalty), 200
    except Exception as e:
        logger.error(f"Error assessing strategic loyalty for {entity}: {e}")
        return jsonify({"error": str(e)}), 500


@app.route('/api/geopolitical/record/border-event', methods=['POST'])
def record_border_event():
    """
    Record a border event.
    
    Request body:
    {
        "region": "Gaza",
        "border_point": "Rafah",
        "event_type": "control_shift",
        "description": "Border control changed hands",
        "control_status": "new_control",
        "shift_speed": "rapid"
    }
    """
    try:
        data = request.json
        required_fields = ["region", "border_point", "event_type", "description"]
        
        if not all(field in data for field in required_fields):
            return jsonify({"error": f"Missing required fields: {required_fields}"}), 400
        
        engine.record_border_event(
            region=data["region"],
            border_point=data["border_point"],
            event_type=data["event_type"],
            description=data["description"],
            control_status=data.get("control_status"),
            shift_speed=data.get("shift_speed")
        )
        
        return jsonify({"message": "Border event recorded", "status": "success"}), 200
    except Exception as e:
        logger.error(f"Error recording border event: {e}")
        return jsonify({"error": str(e)}), 500


@app.route('/api/geopolitical/record/hostile-mapping', methods=['POST'])
def record_hostile_mapping():
    """
    Record a hostile mapping incident.
    
    Request body:
    {
        "source": "Foreign Textbook",
        "target_territory": "Hatay",
        "claimed_by": "Foreign State",
        "document_type": "textbook",
        "description": "Hatay included in foreign borders",
        "barrier_level": "definitive"
    }
    """
    try:
        data = request.json
        required_fields = ["source", "target_territory", "claimed_by", "document_type", "description"]
        
        if not all(field in data for field in required_fields):
            return jsonify({"error": f"Missing required fields: {required_fields}"}), 400
        
        engine.record_hostile_mapping(
            source=data["source"],
            target_territory=data["target_territory"],
            claimed_by=data["claimed_by"],
            document_type=data["document_type"],
            description=data["description"],
            barrier_level=data.get("barrier_level", "definitive")
        )
        
        return jsonify({"message": "Hostile mapping recorded", "status": "success"}), 200
    except Exception as e:
        logger.error(f"Error recording hostile mapping: {e}")
        return jsonify({"error": str(e)}), 500


@app.route('/api/geopolitical/record/help-seeking-paradox', methods=['POST'])
def record_help_seeking_paradox():
    """
    Record a help-seeking paradox incident.
    
    Request body:
    {
        "entity": "Entity X",
        "region": "Gaza",
        "hostile_label": "enemy",
        "aid_requested": "humanitarian aid, border opening",
        "description": "Entity labels state as enemy while requesting aid",
        "paradox_level": "high"
    }
    """
    try:
        data = request.json
        required_fields = ["entity", "region", "hostile_label", "aid_requested", "description"]
        
        if not all(field in data for field in required_fields):
            return jsonify({"error": f"Missing required fields: {required_fields}"}), 400
        
        engine.record_help_seeking_paradox(
            entity=data["entity"],
            region=data["region"],
            hostile_label=data["hostile_label"],
            aid_requested=data["aid_requested"],
            description=data["description"],
            paradox_level=data.get("paradox_level", "high")
        )
        
        return jsonify({"message": "Help-seeking paradox recorded", "status": "success"}), 200
    except Exception as e:
        logger.error(f"Error recording help-seeking paradox: {e}")
        return jsonify({"error": str(e)}), 500


@app.route('/api/geopolitical/record/strategic-loyalty', methods=['POST'])
def record_strategic_loyalty():
    """
    Record a strategic loyalty assessment.
    
    Request body:
    {
        "entity": "Entity Y",
        "relationship_type": "loyal_friend",
        "shared_resources": ["resource1", "resource2"],
        "common_path": true,
        "assessment": "Entity walks common path"
    }
    """
    try:
        data = request.json
        required_fields = ["entity", "relationship_type", "shared_resources", "common_path", "assessment"]
        
        if not all(field in data for field in required_fields):
            return jsonify({"error": f"Missing required fields: {required_fields}"}), 400
        
        engine.record_strategic_loyalty(
            entity=data["entity"],
            relationship_type=data["relationship_type"],
            shared_resources=data["shared_resources"],
            common_path=bool(data["common_path"]),
            assessment=data["assessment"]
        )
        
        return jsonify({"message": "Strategic loyalty recorded", "status": "success"}), 200
    except Exception as e:
        logger.error(f"Error recording strategic loyalty: {e}")
        return jsonify({"error": str(e)}), 500


@app.route('/api/geopolitical/regions', methods=['GET'])
def get_monitored_regions():
    """Get list of monitored regions."""
    return jsonify({
        "regions": engine.MONITORED_REGIONS,
        "strategic_border_points": engine.STRATEGIC_BORDER_POINTS
    }), 200


@app.route('/api/geopolitical/health', methods=['GET'])
def health_check():
    """Health check endpoint."""
    return jsonify({
        "status": "healthy",
        "service": "geopolitical_analysis_engine",
        "version": "1.0.0",
        "deployment": "public",
        "separate_from": "oracle_system"
    }), 200


if __name__ == '__main__':
    app.run(debug=True, port=8002, host='0.0.0.0')
