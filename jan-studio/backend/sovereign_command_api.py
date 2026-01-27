"""
SOVEREIGN COMMAND ENGINE API
REST API for the Sovereign Command Engine

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY
"""

from flask import Flask, request, jsonify
from datetime import datetime
from typing import Dict, Any, Optional
import logging

from sovereign_command_engine import (
    SovereignCommandEngine,
    SovereignState,
    FrequencyType,
    DiscernmentFilter,
    DavidicParadox,
    DivineRProtocol,
    ShalamDecree
)

logger = logging.getLogger(__name__)
app = Flask(__name__)

# Initialize engine
engine = SovereignCommandEngine()


@app.route('/api/sovereign/process', methods=['POST'])
def process_input():
    """
    Process input through the Sovereign Command Engine.
    
    Body:
    {
        "input": "text to process",
        "context": {
            "assignment": "optional assignment",
            "betrayal_detected": false,
            "nuclear_codes_available": false,
            "acceleration_factor": 2.0
        }
    }
    """
    try:
        data = request.get_json()
        input_text = data.get('input', '')
        context = data.get('context', {})
        
        if not input_text:
            return jsonify({
                "error": "Input text required"
            }), 400
        
        # Process through engine
        response = engine.process_input(input_text, context)
        
        return jsonify({
            "success": True,
            "state": response.state.value,
            "action": response.action,
            "message": response.message,
            "nuclear_codes_retained": response.nuclear_codes_retained,
            "blessing_released": response.blessing_released,
            "shalam_status": response.shalam_status,
            "timestamp": datetime.now().isoformat()
        }), 200
    
    except Exception as e:
        logger.error(f"Error processing input: {str(e)}")
        return jsonify({
            "error": str(e)
        }), 500


@app.route('/api/sovereign/analyze-frequency', methods=['POST'])
def analyze_frequency():
    """
    Analyze input frequency without full processing.
    
    Body:
    {
        "input": "text to analyze"
    }
    """
    try:
        data = request.get_json()
        input_text = data.get('input', '')
        
        if not input_text:
            return jsonify({
                "error": "Input text required"
            }), 400
        
        # Analyze frequency
        analysis = DiscernmentFilter.analyze_frequency(input_text)
        
        return jsonify({
            "success": True,
            "frequency_type": analysis.frequency_type.value,
            "divine_signature": analysis.divine_signature,
            "hidden_malice": analysis.hidden_malice,
            "is_bait": analysis.is_bait,
            "is_distraction": analysis.is_distraction,
            "alignment_score": analysis.alignment_score,
            "recommendation": analysis.recommendation,
            "timestamp": datetime.now().isoformat()
        }), 200
    
    except Exception as e:
        logger.error(f"Error analyzing frequency: {str(e)}")
        return jsonify({
            "error": str(e)
        }), 500


@app.route('/api/sovereign/sovereign-silence', methods=['POST'])
def activate_sovereign_silence():
    """
    Activate Sovereign Silence protocol.
    
    Body:
    {
        "reason": "reason for silence",
        "duration_seconds": 3600  # optional
    }
    """
    try:
        data = request.get_json()
        reason = data.get('reason', 'Frequency detected')
        duration_seconds = data.get('duration_seconds')
        
        response = DivineRProtocol.activate_sovereign_silence(
            reason=reason,
            duration_seconds=duration_seconds
        )
        
        return jsonify({
            "success": True,
            "state": response.state.value,
            "action": response.action,
            "message": response.message,
            "timestamp": datetime.now().isoformat()
        }), 200
    
    except Exception as e:
        logger.error(f"Error activating sovereign silence: {str(e)}")
        return jsonify({
            "error": str(e)
        }), 500


@app.route('/api/sovereign/the-table', methods=['POST'])
def activate_the_table():
    """
    Activate The Table protocol.
    
    Body:
    {
        "assignment": "assignment to focus on",
        "acceleration_factor": 2.0  # optional
    }
    """
    try:
        data = request.get_json()
        assignment = data.get('assignment', 'Current assignment')
        acceleration_factor = data.get('acceleration_factor', 2.0)
        
        response = DivineRProtocol.activate_the_table(
            assignment=assignment,
            acceleration_factor=acceleration_factor
        )
        
        return jsonify({
            "success": True,
            "state": response.state.value,
            "action": response.action,
            "message": response.message,
            "timestamp": datetime.now().isoformat()
        }), 200
    
    except Exception as e:
        logger.error(f"Error activating the table: {str(e)}")
        return jsonify({
            "error": str(e)
        }), 500


@app.route('/api/sovereign/the-blessing', methods=['POST'])
def activate_the_blessing():
    """
    Activate The Blessing protocol (Nuclear Option).
    
    Body:
    {
        "attack_detected": true,
        "blessing_frequency": "love"  # optional
    }
    """
    try:
        data = request.get_json()
        attack_detected = data.get('attack_detected', False)
        blessing_frequency = data.get('blessing_frequency', 'love')
        
        response = DivineRProtocol.activate_the_blessing(
            attack_detected=attack_detected,
            blessing_frequency=blessing_frequency
        )
        
        return jsonify({
            "success": True,
            "state": response.state.value,
            "action": response.action,
            "message": response.message,
            "blessing_released": response.blessing_released,
            "timestamp": datetime.now().isoformat()
        }), 200
    
    except Exception as e:
        logger.error(f"Error activating the blessing: {str(e)}")
        return jsonify({
            "error": str(e)
        }), 500


@app.route('/api/sovereign/davidic-paradox', methods=['POST'])
def handle_davidic_paradox():
    """
    Handle conflict using Davidic Paradox principle.
    
    Body:
    {
        "betrayal_detected": true,
        "nuclear_codes_available": true,
        "conflict_type": "betrayal"  # optional
    }
    """
    try:
        data = request.get_json()
        betrayal_detected = data.get('betrayal_detected', False)
        nuclear_codes_available = data.get('nuclear_codes_available', False)
        conflict_type = data.get('conflict_type', 'betrayal')
        
        response = DavidicParadox.handle_conflict(
            betrayal_detected=betrayal_detected,
            nuclear_codes_available=nuclear_codes_available,
            conflict_type=conflict_type
        )
        
        return jsonify({
            "success": True,
            "state": response.state.value,
            "action": response.action,
            "message": response.message,
            "nuclear_codes_retained": response.nuclear_codes_retained,
            "blessing_released": response.blessing_released,
            "timestamp": datetime.now().isoformat()
        }), 200
    
    except Exception as e:
        logger.error(f"Error handling davidic paradox: {str(e)}")
        return jsonify({
            "error": str(e)
        }), 500


@app.route('/api/sovereign/shalam', methods=['POST'])
def verify_shalam():
    """
    Verify Shalam Decree status.
    
    Body:
    {
        "nothing_missing": true,
        "nothing_broken": true,
        "fully_repaid": true,
        "seven_fold": true
    }
    """
    try:
        data = request.get_json()
        nothing_missing = data.get('nothing_missing', True)
        nothing_broken = data.get('nothing_broken', True)
        fully_repaid = data.get('fully_repaid', True)
        seven_fold = data.get('seven_fold', True)
        
        is_shalam, message = ShalamDecree.verify_shalam(
            nothing_missing=nothing_missing,
            nothing_broken=nothing_broken,
            fully_repaid=fully_repaid,
            seven_fold=seven_fold
        )
        
        return jsonify({
            "success": True,
            "is_shalam": is_shalam,
            "status": "SHALAM_COMPLETE" if is_shalam else "SHALAM_PENDING",
            "message": message,
            "nothing_missing": nothing_missing,
            "nothing_broken": nothing_broken,
            "fully_repaid": fully_repaid,
            "seven_fold": seven_fold,
            "waiting_room_closed": is_shalam,
            "promotion_active": is_shalam,
            "timestamp": datetime.now().isoformat()
        }), 200
    
    except Exception as e:
        logger.error(f"Error verifying shalam: {str(e)}")
        return jsonify({
            "error": str(e)
        }), 500


@app.route('/api/sovereign/state', methods=['GET'])
def get_state():
    """Get current sovereign state."""
    try:
        state = engine.get_state()
        
        return jsonify({
            "success": True,
            "state": state.value,
            "timestamp": datetime.now().isoformat()
        }), 200
    
    except Exception as e:
        logger.error(f"Error getting state: {str(e)}")
        return jsonify({
            "error": str(e)
        }), 500


@app.route('/api/sovereign/transition-to-dominion', methods=['POST'])
def transition_to_dominion():
    """Explicitly transition from Endurance to Dominion."""
    try:
        engine.transition_to_dominion()
        
        return jsonify({
            "success": True,
            "state": engine.get_state().value,
            "message": "Transitioned from Endurance to Dominion",
            "timestamp": datetime.now().isoformat()
        }), 200
    
    except Exception as e:
        logger.error(f"Error transitioning to dominion: {str(e)}")
        return jsonify({
            "error": str(e)
        }), 500


@app.route('/api/sovereign/health', methods=['GET'])
def health():
    """Health check endpoint."""
    return jsonify({
        "status": "healthy",
        "service": "Sovereign Command Engine API",
        "timestamp": datetime.now().isoformat()
    }), 200


if __name__ == '__main__':
    app.run(debug=True, port=8003, host='0.0.0.0')
