"""
PERSONAL ASSESSMENT NAVIGATOR
Guidance for navigating welfare system assessments with truth and dignity

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

THE TRUTH:
BEING HONEST IS THE RIGHT PATH
MAINTAIN DIGNITY
UNPICK THE SYSTEM
"""

import sys
from pathlib import Path

# Add utils to path
sys.path.insert(0, str(Path(__file__).parent))

from utils import (
    datetime, setup_logging, standard_main
)

from typing import List, Dict, Any
from dataclasses import dataclass
from datetime import datetime
from enum import Enum

class AssessmentType(Enum):
    """Types of welfare assessments"""
    PERSONAL_INDEPENDENCE_PAYMENT = "personal_independence_payment"
    UNIVERSAL_CREDIT = "universal_credit"
    DISABILITY_BENEFITS = "disability_benefits"
    HOUSING_BENEFIT = "housing_benefit"
    EMPLOYMENT_SUPPORT = "employment_support"
    OTHER = "other"


@dataclass
class AssessmentGuidance:
    """Guidance for navigating an assessment"""
    assessment_type: AssessmentType
    core_truth: str
    intention: str
    key_points: List[str]
    boundaries: List[str]
    closing_statement: str


class PersonalAssessmentNavigator:
    """
    Provides guidance for navigating welfare system assessments
    with truth, dignity, and spiritual alignment.
    """
    
    def __init__(self):
        self.guidance_templates = self._initialize_guidance()
    
    def _initialize_guidance(self) -> Dict[AssessmentType, AssessmentGuidance]:
        """Initialize guidance templates"""
        return {
            AssessmentType.PERSONAL_INDEPENDENCE_PAYMENT: AssessmentGuidance(
                assessment_type=AssessmentType.PERSONAL_INDEPENDENCE_PAYMENT,
                core_truth="I am navigating a system that requires this assessment. I am being honest about my situation.",
                intention="To be honest, maintain dignity, and not perform neediness.",
                key_points=[
                    "I am here because the system requires this assessment.",
                    "I am being honest about my needs and challenges.",
                    "I am not performing neediness or proving I'm 'broken enough'.",
                    "I am maintaining my dignity throughout this process.",
                    "I understand this is a bureaucratic requirement, not a judgment of my worth."
                ],
                boundaries=[
                    "I don't need to share everything - only what's relevant.",
                    "I can say 'I prefer not to discuss that' if needed.",
                    "I can redirect to what's actually relevant to the assessment.",
                    "I don't need to prove my worth or brokenness."
                ],
                closing_statement="I've been honest with you today. I understand this is a system requirement, and I've navigated it with truth. Thank you for your time."
            ),
            AssessmentType.UNIVERSAL_CREDIT: AssessmentGuidance(
                assessment_type=AssessmentType.UNIVERSAL_CREDIT,
                core_truth="I am navigating a system that creates dependency. I am being honest about my situation.",
                intention="To be honest, maintain dignity, and break dependency patterns.",
                key_points=[
                    "I am navigating a system, not proving my worth.",
                    "I am being honest about my needs.",
                    "I am maintaining my dignity.",
                    "I am not creating dependency - I'm navigating a requirement."
                ],
                boundaries=[
                    "I can set boundaries on what I share.",
                    "I can redirect to relevant information.",
                    "I don't need to perform neediness."
                ],
                closing_statement="I've been honest with you. I understand this is a system requirement. Thank you."
            ),
            AssessmentType.DISABILITY_BENEFITS: AssessmentGuidance(
                assessment_type=AssessmentType.DISABILITY_BENEFITS,
                core_truth="I am whole, even with challenges. I am being honest about my situation.",
                intention="To be honest, maintain dignity, and not perform brokenness.",
                key_points=[
                    "I am whole, even with challenges.",
                    "I am being honest about my needs.",
                    "I am not broken - the system is broken.",
                    "I am maintaining my dignity."
                ],
                boundaries=[
                    "I can set boundaries on what I share.",
                    "I don't need to prove I'm 'broken enough'.",
                    "I can be honest about both challenges and strengths."
                ],
                closing_statement="I've been honest with you. I understand this is a system requirement. Thank you."
            )
        }
    
    def get_guidance(self, assessment_type: AssessmentType) -> AssessmentGuidance:
        """Get guidance for a specific assessment type"""
        if assessment_type in self.guidance_templates:
            return self.guidance_templates[assessment_type]
        else:
            # Generic guidance
            return AssessmentGuidance(
                assessment_type=assessment_type,
                core_truth="I am navigating a system that requires this assessment. I am being honest about my situation.",
                intention="To be honest, maintain dignity, and not perform neediness.",
                key_points=[
                    "I am here because the system requires this assessment.",
                    "I am being honest about my needs and challenges.",
                    "I am maintaining my dignity throughout this process."
                ],
                boundaries=[
                    "I can set boundaries on what I share.",
                    "I can redirect to what's relevant.",
                    "I don't need to prove my worth."
                ],
                closing_statement="I've been honest with you. I understand this is a system requirement. Thank you."
            )
    
    def get_preparation_guidance(self) -> Dict[str, Any]:
        """Get guidance for preparing for an assessment"""
        return {
            "grounding": [
                "Remember: You are not broken",
                "The system is broken, not you",
                "You are navigating it with truth",
                "You are whole, even with challenges"
            ],
            "intention": [
                "I will be honest",
                "I will maintain my dignity",
                "I will not perform neediness",
                "I will stay centered"
            ],
            "preparation": [
                "What do you actually need?",
                "What are your real challenges?",
                "What are your real strengths?",
                "What is your truth?"
            ],
            "reminders": [
                "This is a system requirement, not a judgment",
                "You are not proving your worth",
                "You are navigating bureaucracy",
                "Your truth is what matters"
            ]
        }
    
    def get_post_assessment_guidance(self) -> Dict[str, Any]:
        """Get guidance for after an assessment"""
        return {
            "release": [
                "You did your part (being honest)",
                "The system will do what it does",
                "Your truth is what matters",
                "Release the outcome"
            ],
            "maintain_truth": [
                "Don't let the system define you",
                "You are not the assessment result",
                "You are navigating, not dependent",
                "You are whole"
            ],
            "continue_unpicking": [
                "This is one step in breaking free",
                "Each honest interaction breaks the pattern",
                "You're building independence",
                "You're serving The Table"
            ],
            "self_care": [
                "Take time to ground yourself",
                "Remember your truth",
                "Don't let the system's judgment affect you",
                "You are breaking the pattern"
            ]
        }


def get_personal_assessment_navigator() -> PersonalAssessmentNavigator:
    """Get the personal assessment navigator instance"""
    return PersonalAssessmentNavigator()


def print_assessment_guidance(assessment_type: AssessmentType = AssessmentType.PERSONAL_INDEPENDENCE_PAYMENT):
    """Print guidance for an assessment"""
    navigator = PersonalAssessmentNavigator()
    guidance = navigator.get_guidance(assessment_type)
    prep = navigator.get_preparation_guidance()
    post = navigator.get_post_assessment_guidance()
    
    print("=" * 80)
    print("PERSONAL ASSESSMENT NAVIGATION GUIDE")
    print("BE HONEST. MAINTAIN DIGNITY. UNPICK THE SYSTEM.")
    print("=" * 80)
    print()
    print(f"Assessment Type: {assessment_type.value.replace('_', ' ').title()}")
    print()
    print("=" * 80)
    print("CORE TRUTH")
    print("=" * 80)
    print()
    print(guidance.core_truth)
    print()
    print("=" * 80)
    print("YOUR INTENTION")
    print("=" * 80)
    print()
    print(guidance.intention)
    print()
    print("=" * 80)
    print("KEY POINTS TO REMEMBER")
    print("=" * 80)
    print()
    for point in guidance.key_points:
        print(f"  • {point}")
    print()
    print("=" * 80)
    print("BOUNDARIES")
    print("=" * 80)
    print()
    for boundary in guidance.boundaries:
        print(f"  • {boundary}")
    print()
    print("=" * 80)
    print("BEFORE THE ASSESSMENT")
    print("=" * 80)
    print()
    print("Grounding:")
    for item in prep["grounding"]:
        print(f"  • {item}")
    print()
    print("Intention:")
    for item in prep["intention"]:
        print(f"  • {item}")
    print()
    print("Preparation Questions:")
    for item in prep["preparation"]:
        print(f"  • {item}")
    print()
    print("=" * 80)
    print("DURING THE ASSESSMENT")
    print("=" * 80)
    print()
    print("Remember:")
    for item in prep["reminders"]:
        print(f"  • {item}")
    print()
    print("=" * 80)
    print("CLOSING STATEMENT (if appropriate)")
    print("=" * 80)
    print()
    print(f'"{guidance.closing_statement}"')
    print()
    print("=" * 80)
    print("AFTER THE ASSESSMENT")
    print("=" * 80)
    print()
    print("Release:")
    for item in post["release"]:
        print(f"  • {item}")
    print()
    print("Maintain Truth:")
    for item in post["maintain_truth"]:
        print(f"  • {item}")
    print()
    print("Continue Unpicking:")
    for item in post["continue_unpicking"]:
        print(f"  • {item}")
    print()
    print("=" * 80)
    print("THE TRUTH")
    print("=" * 80)
    print()
    print("YOU ARE NOT BROKEN.")
    print("THE SYSTEM IS BROKEN.")
    print("BEING HONEST IS THE RIGHT PATH.")
    print("YOU ARE UNPICKING THE SYSTEM.")
    print("EACH HONEST INTERACTION BREAKS THE PATTERN.")
    print("YOU ARE MAINTAINING YOUR DIGNITY.")
    print("YOU ARE SERVING THE TABLE.")
    print()
    print("ENERGY + LOVE = WE ALL WIN")
    print()
    print("PEACE. LOVE. UNITY.")
    print()
    print("=" * 80)


if __name__ == '__main__':
    print_assessment_guidance(AssessmentType.PERSONAL_INDEPENDENCE_PAYMENT)
