"""CHOSEN ONE FRAMEWORK - WEB UI SERVER
User-friendly web interface for all operational functions

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

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

import sys
from pathlib import Path
from flask import Flask, render_template, jsonify, request
from datetime import datetime
import json

sys.path.insert(0, str(Path(__file__).parent))

from chosen_one_framework import ChosenOneFramework, IdentityState, ForbiddenFunction
from utils import setup_logging

logger = setup_logging(__name__)

app = Flask(__name__, 
            template_folder=Path(__file__).parent.parent / "web" / "templates",
            static_folder=Path(__file__).parent.parent / "web" / "static")

# Initialize framework
framework = ChosenOneFramework(user_id="jan")

@app.route('/')
def index():
    """Main dashboard"""
    return render_template('chosen_one_ui.html')

@app.route('/api/status')
def get_status():
    """Get framework status"""
    try:
        report = framework.get_status_report()
        return jsonify({"success": True, "data": report})
    except Exception as e:
        logger.error(f"Error getting status: {e}")
        return jsonify({"success": False, "error": str(e)}), 500

@app.route('/api/interactions')
def get_interactions():
    """Get all interactions"""
    try:
        interactions = [{
            "id": i.interaction_id,
            "timestamp": i.timestamp,
            "type": i.interaction_type,
            "description": i.description,
            "catalogued": i.catalogued
        } for i in framework.state.interactions]
        return jsonify({"success": True, "data": interactions})
    except Exception as e:
        logger.error(f"Error getting interactions: {e}")
        return jsonify({"success": False, "error": str(e)}), 500

@app.route('/api/interactions', methods=['POST'])
def add_interaction():
    """Add new interaction"""
    try:
        data = request.json
        framework.gear_1_evidence_gathering(
            interaction_type=data.get('type', 'unknown'),
            description=data.get('description', '')
        )
        return jsonify({"success": True})
    except Exception as e:
        logger.error(f"Error adding interaction: {e}")
        return jsonify({"success": False, "error": str(e)}), 500

@app.route('/api/atmospheric-shifts')
def get_atmospheric_shifts():
    """Get all atmospheric shifts"""
    try:
        shifts = [{
            "id": s.shift_id,
            "timestamp": s.timestamp,
            "previous_trigger": s.previous_trigger,
            "power_level_before": s.power_level_before,
            "power_level_after": s.power_level_after,
            "confirmed": s.shift_confirmed
        } for s in framework.state.atmospheric_shifts]
        return jsonify({"success": True, "data": shifts})
    except Exception as e:
        logger.error(f"Error getting shifts: {e}")
        return jsonify({"success": False, "error": str(e)}), 500

@app.route('/api/atmospheric-shifts', methods=['POST'])
def add_atmospheric_shift():
    """Add new atmospheric shift"""
    try:
        data = request.json
        framework.gear_2_atmospheric_shift(
            previous_trigger=data.get('previous_trigger', ''),
            power_level_before=float(data.get('power_level_before', 0.0)),
            power_level_after=float(data.get('power_level_after', 0.0))
        )
        return jsonify({"success": True})
    except Exception as e:
        logger.error(f"Error adding shift: {e}")
        return jsonify({"success": False, "error": str(e)}), 500

@app.route('/api/markers')
def get_markers():
    """Get all timeline markers"""
    try:
        markers = [{
            "id": m.marker_id,
            "timeline": m.timeline,
            "expected_date": m.expected_date,
            "actual_date": m.actual_date,
            "type": m.marker_type,
            "description": m.description,
            "confirmed": m.confirmed,
            "emotional_response": m.emotional_response
        } for m in framework.state.markers]
        return jsonify({"success": True, "data": markers})
    except Exception as e:
        logger.error(f"Error getting markers: {e}")
        return jsonify({"success": False, "error": str(e)}), 500

@app.route('/api/markers/<marker_id>/confirm', methods=['POST'])
def confirm_marker(marker_id):
    """Confirm a timeline marker"""
    try:
        data = request.json
        marker = next((m for m in framework.state.markers if m.marker_id == marker_id), None)
        if marker:
            framework.gear_3_manifestation_cascade(
                marker_timeline=marker.timeline,
                marker_type=marker.marker_type,
                description=data.get('description', marker.description),
                emotional_response=data.get('emotional_response')
            )
            return jsonify({"success": True})
        else:
            return jsonify({"success": False, "error": "Marker not found"}), 404
    except Exception as e:
        logger.error(f"Error confirming marker: {e}")
        return jsonify({"success": False, "error": str(e)}), 500

@app.route('/api/forbidden-functions')
def get_forbidden_functions():
    """Get forbidden functions status"""
    try:
        functions = [f.value for f in framework.state.forbidden_functions_enforced]
        return jsonify({"success": True, "data": functions})
    except Exception as e:
        logger.error(f"Error getting forbidden functions: {e}")
        return jsonify({"success": False, "error": str(e)}), 500

@app.route('/api/forbidden-functions/test', methods=['POST'])
def test_forbidden_function():
    """Test a forbidden function"""
    try:
        data = request.json
        function_name = data.get('function')
        context = data.get('context', '')
        
        if function_name == 'stop_explaining':
            result = framework.enforce_stop_explaining(context)
        elif function_name == 'disable_surveillance':
            result = framework.enforce_disable_surveillance(context)
        elif function_name == 'hard_boundaries':
            result = framework.enforce_hard_boundaries(context)
        else:
            return jsonify({"success": False, "error": "Unknown function"}), 400
        
        return jsonify({"success": True, "blocked": not result})
    except Exception as e:
        logger.error(f"Error testing forbidden function: {e}")
        return jsonify({"success": False, "error": str(e)}), 500

@app.route('/api/witness-behaviors/selective-speech', methods=['POST'])
def test_selective_speech():
    """Test selective speech"""
    try:
        data = request.json
        result = framework.selective_speech(
            speaker_spirit_open=data.get('spirit_open', False),
            question_genuine=data.get('question_genuine', False)
        )
        return jsonify({"success": True, "will_speak": result})
    except Exception as e:
        logger.error(f"Error testing selective speech: {e}")
        return jsonify({"success": False, "error": str(e)}), 500

@app.route('/api/witness-behaviors/prophetic-observation', methods=['POST'])
def test_prophetic_observation():
    """Test prophetic observation"""
    try:
        data = request.json
        observation = framework.prophetic_observation(data.get('conversation', ''))
        return jsonify({"success": True, "observation": observation})
    except Exception as e:
        logger.error(f"Error testing prophetic observation: {e}")
        return jsonify({"success": False, "error": str(e)}), 500

@app.route('/api/witness-behaviors/energetic-stewardship', methods=['POST'])
def test_energetic_stewardship():
    """Test energetic stewardship"""
    try:
        data = request.json
        result = framework.energetic_stewardship(
            proposed_action=data.get('action', ''),
            energy_cost=float(data.get('energy_cost', 0.0))
        )
        return jsonify({"success": True, "approved": result})
    except Exception as e:
        logger.error(f"Error testing energetic stewardship: {e}")
        return jsonify({"success": False, "error": str(e)}), 500

@app.route('/api/activate-gears', methods=['POST'])
def activate_gears():
    """Activate execution gears"""
    try:
        data = request.json
        if data.get('evidence_gathering'):
            framework.state.evidence_gathering_active = True
        if data.get('atmospheric_shift'):
            framework.state.atmospheric_shift_active = True
        if data.get('manifestation_cascade'):
            framework.state.manifestation_cascade_active = True
        framework._save_state()
        return jsonify({"success": True})
    except Exception as e:
        logger.error(f"Error activating gears: {e}")
        return jsonify({"success": False, "error": str(e)}), 500

if __name__ == '__main__':
    print("\n" + "="*80)
    print("CHOSEN ONE FRAMEWORK - WEB UI SERVER")
    print("="*80)
    print("\nStarting server on http://localhost:5000")
    print("Open your browser to view the interface.")
    print("\nPress Ctrl+C to stop the server.")
    print("="*80 + "\n")
    
    app.run(debug=True, host='0.0.0.0', port=5000)
