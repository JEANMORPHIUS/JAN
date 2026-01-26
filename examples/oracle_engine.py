"""CREATIVE ORACLE ENGINE - Example Implementation
Flipping the Gambling Algorithm for Creative Liberation

This is a complete example implementation of the Creative Oracle system,
demonstrating how to use the oracle API and integrate it into applications.

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

import requests
import json
from typing import Dict, Optional, Any
from datetime import datetime


class OracleClient:
    """
    Client for interacting with the Creative Oracle API.
    
    Example usage:
        client = OracleClient(base_url="http://localhost:8000")
        result = client.cast_oracle(
            user_intent="I'm stuck on my novel's third act",
            creative_context="Science fiction, character development"
        )
        print(result["creative_prompt"])
    """
    
    def __init__(self, base_url: str = "http://localhost:8000", user_id: str = "public"):
        self.base_url = base_url.rstrip("/")
        self.user_id = user_id
    
    def cast_oracle(
        self,
        user_intent: str,
        creative_context: Optional[str] = None,
        transparency_level: str = "full"
    ) -> Dict[str, Any]:
        """
        Cast the Creative Oracle.
        
        Args:
            user_intent: User's creative question or challenge
            creative_context: Current project context, genre, medium, etc.
            transparency_level: Level of transparency (full, minimal)
        
        Returns:
            Oracle cast result with interpretation and creative prompt
        """
        response = requests.post(
            f"{self.base_url}/api/oracle/cast",
            json={
                "user_intent": user_intent,
                "creative_context": creative_context,
                "user_id": self.user_id,
                "transparency_level": transparency_level
            }
        )
        response.raise_for_status()
        return response.json()
    
    def get_session(self) -> Dict[str, Any]:
        """Get current user session information."""
        response = requests.get(
            f"{self.base_url}/api/oracle/session",
            params={"user_id": self.user_id}
        )
        response.raise_for_status()
        return response.json()
    
    def record_break(self) -> Dict[str, Any]:
        """Record a break in the creative session."""
        response = requests.post(
            f"{self.base_url}/api/oracle/break",
            params={"user_id": self.user_id}
        )
        response.raise_for_status()
        return response.json()
    
    def get_history(self, limit: int = 10) -> Dict[str, Any]:
        """Get user's oracle cast history."""
        response = requests.get(
            f"{self.base_url}/api/oracle/history",
            params={"user_id": self.user_id, "limit": limit}
        )
        response.raise_for_status()
        return response.json()


def example_usage():
    """
    Example usage of the Creative Oracle.
    
    This demonstrates:
    1. Casting an oracle for creative guidance
    2. Checking session status
    3. Recording breaks
    4. Viewing history
    """
    # Initialize client
    client = OracleClient(base_url="http://localhost:8000", user_id="example_user")
    
    print("=" * 60)
    print("CREATIVE ORACLE - Example Usage")
    print("=" * 60)
    print()
    
    # Example 1: Writer's Block
    print("Example 1: Writer's Block")
    print("-" * 60)
    result = client.cast_oracle(
        user_intent="I can't figure out my character's motivation in Act 3",
        creative_context="Science fiction novel, character development challenge"
    )
    
    print(f"Law Invoked: {result['transparency']['law_title']}")
    print(f"Hexagram: {result['transparency']['hexagram_number']} ({result['transparency']['hexagram_binary']})")
    print(f"Seed: {result['transparency']['seed'][:16]}...")
    print()
    print("Creative Prompt:")
    print(result['creative_prompt'])
    print()
    print(f"Session: {result['session']['cast_count']}/10 casts today")
    if result['ethical_guardrails']['message']:
        print(f"Guardrail: {result['ethical_guardrails']['message']}")
    print()
    
    # Example 2: Check Session
    print("Example 2: Check Session")
    print("-" * 60)
    session = client.get_session()
    print(f"Casts today: {session['cast_count']}")
    print(f"Time creating: {session['time_creating']} minutes")
    print(f"Last cast: {session['last_cast_at']}")
    print()
    
    # Example 3: Record Break
    print("Example 3: Record Break")
    print("-" * 60)
    break_result = client.record_break()
    print(break_result['message'])
    print()
    
    # Example 4: View History
    print("Example 4: View History")
    print("-" * 60)
    history = client.get_history(limit=5)
    print(f"Total casts: {history['total']}")
    for i, cast in enumerate(history['casts'][:3], 1):
        print(f"{i}. Law {cast['law_number']}: {cast['law_title']} - {cast['cast_timestamp']}")
    print()


def example_integration_with_ai():
    """
    Example of integrating Oracle with AI for enhanced interpretation.
    
    In production, you would use AI (Claude, GPT, etc.) to:
    1. Interpret the Law for the specific creative context
    2. Generate context-specific creative prompts
    3. Provide deeper insights based on user's project
    """
    client = OracleClient()
    
    # Cast oracle
    result = client.cast_oracle(
        user_intent="I'm stuck on my sci-fi novel's third act",
        creative_context="Science fiction, character development, plot resolution"
    )
    
    # In production, you would send this to AI for enhanced interpretation
    # For now, we use the basic interpretation from the oracle
    
    law_number = result['transparency']['law_number']
    law_title = result['transparency']['law_title']
    user_intent = result['user_intent']
    creative_context = result['creative_context']
    
    # Example AI prompt (you would use actual AI API here)
    ai_prompt = f"""
    Law {law_number}: {law_title}
    User Intent: {user_intent}
    Creative Context: {creative_context}
    
    Interpret this Law for the user's specific creative challenge.
    Generate an actionable creative prompt that helps them break through
    their creative block.
    """
    
    print("AI Integration Example:")
    print("-" * 60)
    print("Oracle Result:")
    print(f"  Law: {law_number} - {law_title}")
    print(f"  Hexagram: {result['transparency']['hexagram_number']}")
    print()
    print("AI Prompt (for enhanced interpretation):")
    print(ai_prompt)
    print()
    print("In production, this would be sent to Claude/GPT for:")
    print("  - Context-specific Law interpretation")
    print("  - Enhanced creative prompt generation")
    print("  - Deeper insights based on user's project")
    print()


if __name__ == "__main__":
    print("Creative Oracle Engine - Example Implementation")
    print("=" * 60)
    print()
    print("This example demonstrates how to use the Creative Oracle API.")
    print("Make sure the API server is running on http://localhost:8000")
    print()
    
    try:
        example_usage()
        example_integration_with_ai()
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to API server.")
        print("Make sure the server is running on http://localhost:8000")
    except Exception as e:
        print(f"Error: {e}")
