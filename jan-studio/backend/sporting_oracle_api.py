"""
SPORTING ORACLE API
REST API for the Sporting Oracle harm prevention tool

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity
"""

from flask import Flask, request, jsonify
from datetime import datetime
from typing import Dict, Any, Optional, List
import logging

from sporting_oracle import (
    SportingOracle,
    GameActivity,
    analyze_gambling_activity
)

logger = logging.getLogger(__name__)

app = Flask(__name__)

# Initialize Sporting Oracle
sporting_oracle = SportingOracle()


@app.route('/api/sporting-oracle/analyze', methods=['POST'])
def analyze_activity():
    """
    Analyze user gambling activity and detect house edge exposure.
    
    Request body:
    {
        "user_id": "user123",
        "activities": [
            {
                "game_type": "slots",
                "bet_amount": 10.0,
                "timestamp": "2026-01-27T12:00:00",
                "result": "loss",
                "payout": null
            }
        ]
    }
    """
    try:
        data = request.json
        user_id = data.get('user_id')
        
        if not user_id:
            return jsonify({"error": "user_id required"}), 400
        
        # Parse activities if provided
        activities = None
        if 'activities' in data:
            activities = [
                GameActivity(
                    game_type=activity['game_type'],
                    bet_amount=float(activity['bet_amount']),
                    timestamp=datetime.fromisoformat(activity['timestamp']),
                    result=activity.get('result'),
                    payout=float(activity['payout']) if activity.get('payout') else None
                )
                for activity in data['activities']
            ]
        
        # Analyze
        result = sporting_oracle.analyze_user_activity(user_id, activities)
        
        return jsonify(result), 200
        
    except Exception as e:
        logger.error(f"Error analyzing activity: {e}")
        return jsonify({"error": str(e)}), 500


@app.route('/api/sporting-oracle/record', methods=['POST'])
def record_activity():
    """
    Record a gambling activity.
    
    Request body:
    {
        "user_id": "user123",
        "game_type": "slots",
        "bet_amount": 10.0,
        "result": "loss",
        "payout": null
    }
    """
    try:
        data = request.json
        user_id = data.get('user_id')
        game_type = data.get('game_type')
        bet_amount = data.get('bet_amount')
        
        if not all([user_id, game_type, bet_amount]):
            return jsonify({"error": "user_id, game_type, and bet_amount required"}), 400
        
        # Record activity
        sporting_oracle.record_activity(
            user_id=user_id,
            game_type=game_type,
            bet_amount=float(bet_amount),
            result=data.get('result'),
            payout=float(data['payout']) if data.get('payout') else None
        )
        
        return jsonify({"message": "Activity recorded", "user_id": user_id}), 200
        
    except Exception as e:
        logger.error(f"Error recording activity: {e}")
        return jsonify({"error": str(e)}), 500


@app.route('/api/sporting-oracle/intervention/<user_id>', methods=['GET'])
def get_interventions(user_id: str):
    """
    Get intervention history for a user.
    """
    try:
        # Load interventions from database
        from sporting_oracle import get_sporting_oracle_db
        
        interventions = []
        with get_sporting_oracle_db() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT * FROM interventions
                WHERE user_id = ?
                ORDER BY intervention_timestamp DESC
                LIMIT 10
            """, (user_id,))
            
            for row in cursor.fetchall():
                interventions.append({
                    "id": row["id"],
                    "timestamp": row["intervention_timestamp"],
                    "type": row["intervention_type"],
                    "message": row["message"],
                    "oracle_alternative": row["oracle_alternative"],
                    "comparison": row["comparison"],
                    "action_items": row["action_items"].split("\n") if row["action_items"] else []
                })
        
        return jsonify({"interventions": interventions}), 200
        
    except Exception as e:
        logger.error(f"Error getting interventions: {e}")
        return jsonify({"error": str(e)}), 500


@app.route('/api/sporting-oracle/stats/<user_id>', methods=['GET'])
def get_stats(user_id: str):
    """
    Get statistics for a user.
    """
    try:
        from sporting_oracle import get_sporting_oracle_db
        
        stats = {}
        with get_sporting_oracle_db() as conn:
            cursor = conn.cursor()
            
            # Total activities
            cursor.execute("""
                SELECT COUNT(*) as count, SUM(bet_amount) as total_wagered
                FROM user_activities
                WHERE user_id = ?
            """, (user_id,))
            row = cursor.fetchone()
            stats["total_activities"] = row["count"] if row else 0
            stats["total_wagered"] = row["total_wagered"] if row and row["total_wagered"] else 0.0
            
            # Latest edge detection
            cursor.execute("""
                SELECT * FROM edge_detections
                WHERE user_id = ?
                ORDER BY detection_timestamp DESC
                LIMIT 1
            """, (user_id,))
            row = cursor.fetchone()
            if row:
                stats["latest_edge_detection"] = {
                    "house_edge": row["house_edge"],
                    "expected_loss": row["expected_loss"],
                    "risk_level": row["risk_level"],
                    "timestamp": row["detection_timestamp"]
                }
            
            # Intervention count
            cursor.execute("""
                SELECT COUNT(*) as count
                FROM interventions
                WHERE user_id = ?
            """, (user_id,))
            row = cursor.fetchone()
            stats["intervention_count"] = row["count"] if row else 0
        
        return jsonify(stats), 200
        
    except Exception as e:
        logger.error(f"Error getting stats: {e}")
        return jsonify({"error": str(e)}), 500


@app.route('/api/sporting-oracle/health', methods=['GET'])
def health_check():
    """Health check endpoint."""
    return jsonify({
        "status": "healthy",
        "service": "sporting_oracle",
        "version": "1.0.0"
    }), 200


if __name__ == '__main__':
    app.run(debug=True, port=8001)
