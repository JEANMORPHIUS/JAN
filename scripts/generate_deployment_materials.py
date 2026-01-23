"""
Generate Deployment Materials with AI Execution Engine
Uses Claude/Gemini with SIYEM Protocol enforcement
Generates Shell (public-facing) materials for North Cyprus deployment

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

This code honors that we are born a miracle.
This code creates space for miracles to live.
This code recognizes each person under the Lord's word.
"""

import sys
from pathlib import Path

# Add utils to path
sys.path.insert(0, str(Path(__file__).parent))

from utils import (
    Path, datetime, json, load_json, save_json
    setup_logging, standard_main
)

import sys
import os
import json
from pathlib import Path
from datetime import datetime

# Add AI Execution Engine to path
sys.path.insert(0, str(Path(__file__).parent))

try:
    from ai_execution_engine import AIExecutionEngine, execute_deployment_content
    AI_ENGINE_AVAILABLE = True
except ImportError:
    print("Warning: AI Execution Engine not available. Install dependencies.")
    AI_ENGINE_AVAILABLE = False

# Output directory
OUTPUT_DIR = Path(__file__).parent.parent / "output" / "deployment_materials"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def generate_school_presentation_slides(engine: AIExecutionEngine) -> dict:
    """Generate school presentation slides (Shell - public-facing)"""
    
    prompt = """
    Create a school presentation slide deck for our educational platform launch in North Cyprus.
    
    THE MISSION (Shell - Public Language):
    We are building an educational platform that transforms lives through values-based education, creating global impact through digital inclusion, honoring our mission to serve communities, and trusting in the process.
    
    Target Audience: School administrators, teachers, parents (North Cyprus)
    Context: Values-based education through story-based learning
    Market: North Cyprus (Turkish Cypriot community, bilingual Turkish/English)
    
    Content Requirements:
    - Slide 1: Title - "Values-Based Education for the Next Generation"
    - Slide 2: Mission - "Building an educational platform that transforms lives through values-based education"
    - Slide 3: Problem - "Modern education lacks character building, values education"
    - Slide 4: Solution - "Story-based learning teaching honor, truth, loyalty, respect"
    - Slide 5: The Book of Racon - "40 timeless laws found in all cultures (NOT religious scripture)"
    - Slide 6: Content - "376 lessons (40 Laws + 7 Keys), age-appropriate (5-16 years), bilingual (Turkish/English)"
    - Slide 7: Delivery - "Online platform + Raspberry Pi kit (offline option)"
    - Slide 8: Benefits - "Character building, values education, cultural preservation, bilingual support"
    - Slide 9: Pilot Program - "Test group opportunity for 3-5 schools"
    - Slide 10: Next Steps - "Schedule presentation, pilot proposal, teacher training"
    
    Language: Shell (public-facing) - "Global Integration," "Social Cohesion," "Digital Inclusion"
    Format: Markdown with slide separators
    Tone: Professional, accessible, culturally sensitive
    """
    
    result = engine.execute_with_claude(
        prompt=prompt,
        output_mode="shell",
        enforce_threshold=True
    )
    
    return {
        "type": "school_presentation_slides",
        "content": result["sanitized_content"],
        "siyem_compliant": result["siyem_compliant"],
        "violations": result["violations"]
    }


def generate_pilot_proposal(engine: AIExecutionEngine) -> dict:
    """Generate pilot proposal document (Shell - public-facing)"""
    
    prompt = """
    Create a pilot proposal document for North Cyprus schools.
    
    THE MISSION (Shell - Public Language):
    We are building an educational platform that transforms lives through values-based education, creating global impact through digital inclusion, honoring our mission to serve communities, and trusting in the process.
    
    Target Audience: School administrators, decision-makers
    Context: 3-5 school pilot program for educational platform
    Market: North Cyprus (Turkish Cypriot community)
    
    Document Structure:
    1. Executive Summary
       - Mission: Building an educational platform that transforms lives through values-based education
       - Opportunity: Pilot program for 3-5 schools
       - Timeline: 3-month pilot, Month 2-3 deployment
    
    2. Program Overview
       - 376 lessons (40 Laws + 7 Keys)
       - Bilingual (Turkish/English)
       - Age-appropriate (5-16 years)
       - Online platform + Raspberry Pi kit option
    
    3. Pilot Structure
       - Duration: 3 months
       - Schools: 3-5 schools
       - Students: 100-200 students
       - Teachers: 15-25 teachers
       - Support: Teacher training, technical support, progress tracking
    
    4. Benefits
       - Character building through universal values
       - Values education (honor, truth, loyalty, respect)
       - Cultural preservation (Turkish Cypriot heritage)
       - Bilingual support (Turkish/English)
       - Offline option (Raspberry Pi kit)
    
    5. Requirements
       - Internet connectivity (or Raspberry Pi kit)
       - Teacher commitment (training sessions)
       - Student participation (100-200 students)
       - Feedback collection (weekly surveys)
    
    6. Timeline
       - Month 1: School recruitment, teacher training
       - Month 2: Student enrollment, pilot launch
       - Month 3: Pilot execution, feedback collection
       - Month 4: Results analysis, full launch decision
    
    7. Investment
       - Pilot: FREE (beta testing opportunity)
       - Full Launch: $5K-$10K per school/year
    
    8. Next Steps
       - Schedule school presentation
       - Sign pilot agreement
       - Begin teacher training
       - Launch pilot program
    
    Language: Shell (public-facing) - "Global Integration," "Social Cohesion," "Digital Inclusion"
    Format: Professional proposal document (markdown)
    Tone: Professional, clear, compelling
    """
    
    result = engine.execute_with_claude(
        prompt=prompt,
        output_mode="shell",
        enforce_threshold=True
    )
    
    return {
        "type": "pilot_proposal",
        "content": result["sanitized_content"],
        "siyem_compliant": result["siyem_compliant"],
        "violations": result["violations"]
    }


def generate_teacher_training_materials(engine: AIExecutionEngine) -> dict:
    """Generate teacher training materials (Shell - public-facing)"""
    
    prompt = """
    Create teacher training materials for our scripture education platform.
    
    Target Audience: Teachers participating in pilot program
    Context: Training materials for North Cyprus pilot program
    Duration: 2-day training program
    
    Materials Structure:
    1. Training Overview
       - Platform introduction
       - Lesson structure (376 lessons)
       - Bilingual interface (Turkish/English toggle)
       - Progress tracking
       - Student engagement
    
    2. Lesson Delivery Guide
       - How to access lessons
       - Lesson structure (story, activity, assessment)
       - Age-appropriate delivery (5-16 years)
       - Bilingual instruction tips
    
    3. Student Management
       - Student enrollment process
       - Progress tracking
       - Assessment methods
       - Parent communication
    
    4. Platform Features
       - Teacher dashboard
       - Student progress analytics
       - Lesson scheduling
       - Bilingual content toggle
       - Offline option (Raspberry Pi kit)
    
    5. Best Practices
       - Engaging students with story-based learning
       - Facilitating character building discussions
       - Supporting bilingual learning
       - Tracking student progress
    
    6. Troubleshooting
       - Technical issues
       - Content questions
       - Student support
       - Parent inquiries
    
    7. Resources
       - Teacher guides (376 lessons)
       - Student worksheets
       - Assessment rubrics
       - Parent information packets
    
    Language: Shell (public-facing) - "Global Integration," "Social Cohesion," "Digital Inclusion"
    Format: Training manual (markdown)
    Tone: Clear, supportive, practical
    """
    
    result = engine.execute_with_claude(
        prompt=prompt,
        output_mode="shell",
        enforce_threshold=True
    )
    
    return {
        "type": "teacher_training_materials",
        "content": result["sanitized_content"],
        "siyem_compliant": result["siyem_compliant"],
        "violations": result["violations"]
    }


def generate_parent_information_packets(engine: AIExecutionEngine) -> dict:
    """Generate parent information packets (Shell - public-facing)"""
    
    prompt = """
    Create parent information packets for our scripture education platform.
    
    Target Audience: Parents of students in pilot program
    Context: Information about ethical education program for children
    Market: North Cyprus (Turkish Cypriot community, bilingual)
    
    Packet Structure:
    1. Welcome Letter
       - Program introduction
       - Vision: Character building through universal values
       - Benefits for children
    
    2. Program Overview
       - 376 lessons teaching universal values (honor, truth, loyalty, respect)
       - Story-based learning approach
       - Bilingual content (Turkish/English)
       - Age-appropriate (5-16 years)
    
    3. What Your Child Will Learn
       - Character building through universal values
       - Values education (honor, truth, loyalty, respect)
       - Cultural preservation (Turkish Cypriot heritage)
       - Bilingual skills (Turkish/English)
    
    4. How It Works
       - Online platform access
       - Lesson structure (story, activity, assessment)
       - Progress tracking
       - Parent portal access
    
    5. Benefits for Your Child
       - Character development
       - Values education
       - Cultural connection
       - Bilingual support
       - Offline option (Raspberry Pi kit)
    
    6. Parent Involvement
       - Parent portal access
       - Progress updates
       - Communication with teachers
       - Support resources
    
    7. Frequently Asked Questions
       - Is this religious education? (NO - universal values education)
       - Is it bilingual? (YES - Turkish/English)
       - What if we don't have internet? (Raspberry Pi kit available)
       - How much does it cost? (Free for pilot, $50/year for full launch)
    
    8. Contact Information
       - School contact
       - Program support
       - Technical support
       - Parent resources
    
    Language: Shell (public-facing) - "Global Integration," "Social Cohesion," "Digital Inclusion"
    Format: Parent information packet (markdown)
    Tone: Warm, informative, culturally sensitive
    """
    
    result = engine.execute_with_claude(
        prompt=prompt,
        output_mode="shell",
        enforce_threshold=True
    )
    
    return {
        "type": "parent_information_packets",
        "content": result["sanitized_content"],
        "siyem_compliant": result["siyem_compliant"],
        "violations": result["violations"]
    }


def generate_email_templates(engine: AIExecutionEngine) -> dict:
    """Generate email templates (Shell - public-facing)"""
    
    prompt = """
    Create email templates for school outreach and communication.
    
    Templates Needed:
    1. Initial Outreach Email (to school administrators)
       - Subject: "Ethical Education Pilot Program Opportunity"
       - Introduction
       - Program overview
       - Pilot opportunity
       - Call to action
    
    2. Follow-Up Email (after initial contact)
       - Thank you for interest
       - Presentation scheduling
       - Pilot proposal attachment
       - Next steps
    
    3. Teacher Welcome Email (pilot program start)
       - Welcome to pilot program
       - Training schedule
       - Platform access
       - Support resources
    
    4. Parent Introduction Email (pilot program start)
       - Program introduction
       - Parent information packet
       - Parent portal access
       - Support contact
    
    5. Progress Update Email (monthly)
       - Pilot progress summary
       - Student engagement metrics
       - Feedback highlights
       - Next steps
    
    Language: Shell (public-facing) - "Global Integration," "Social Cohesion," "Digital Inclusion"
    Format: Email templates (markdown)
    Tone: Professional, warm, clear
    """
    
    result = engine.execute_with_claude(
        prompt=prompt,
        output_mode="shell",
        enforce_threshold=True
    )
    
    return {
        "type": "email_templates",
        "content": result["sanitized_content"],
        "siyem_compliant": result["siyem_compliant"],
        "violations": result["violations"]
    }


def generate_landing_page_copy(engine: AIExecutionEngine) -> dict:
    """Generate landing page copy (Shell - public-facing)"""
    
    prompt = """
    Create landing page copy for our scripture education platform.
    
    Target Audience: Schools, teachers, parents (North Cyprus)
    Context: Public-facing website landing page
    Market: North Cyprus (Turkish Cypriot community, bilingual)
    
    Page Structure:
    1. Hero Section
       - Headline: "Ethical Education for the Next Generation"
       - Subheadline: "Character building through universal values - Bilingual Turkish/English"
       - Call to action: "Start Free Pilot"
    
    2. Vision Section
       - "Using universal values to teach children...to fix a broken world one child at a time"
       - Story-based learning approach
       - Character building focus
    
    3. Problem Section
       - "Modern education lacks character building, values education"
       - Children need ethical foundation
       - Values education gap
    
    4. Solution Section
       - 376 lessons teaching universal values (honor, truth, loyalty, respect)
       - The Book of Racon: 40 timeless laws found in all cultures (NOT religious scripture)
       - Bilingual content (Turkish/English)
       - Age-appropriate (5-16 years)
       - Online platform + Raspberry Pi kit (offline option)
    
    5. Benefits Section
       - Character building through universal values
       - Values education (honor, truth, loyalty, respect)
       - Cultural preservation (Turkish Cypriot heritage)
       - Bilingual support (Turkish/English)
       - Offline option (Raspberry Pi kit)
    
    6. Features Section
       - 376 lessons (40 Laws + 7 Keys)
       - Bilingual interface (Turkish/English toggle)
       - Age-appropriate (5-16 years)
       - Progress tracking
       - Teacher dashboards
       - Parent portals
       - Offline option (Raspberry Pi kit)
    
    7. Testimonials Section
       - (Placeholder for future testimonials)
       - "Join our pilot program and see the difference"
    
    8. Call to Action
       - "Start Free Pilot Program"
       - "Schedule School Presentation"
       - "Download Pilot Proposal"
    
    Language: Shell (public-facing) - "Global Integration," "Social Cohesion," "Digital Inclusion"
    Format: Landing page copy (markdown)
    Tone: Engaging, clear, culturally sensitive
    """
    
    result = engine.execute_with_claude(
        prompt=prompt,
        output_mode="shell",
        enforce_threshold=True
    )
    
    return {
        "type": "landing_page_copy",
        "content": result["sanitized_content"],
        "siyem_compliant": result["siyem_compliant"],
        "violations": result["violations"]
    }


def generate_all_deployment_materials():
    """Generate all deployment materials using AI Execution Engine"""
    
    if not AI_ENGINE_AVAILABLE:
        print("ERROR: AI Execution Engine not available. Cannot generate materials.")
        return None
    
    print("=" * 60)
    print("GENERATING DEPLOYMENT MATERIALS")
    print("AI Execution Engine: SIYEM Protocol Enforced")
    print("Output Mode: Shell (public-facing)")
    print("=" * 60)
    
    engine = AIExecutionEngine()
    
    materials = {}
    all_violations = []
    all_compliant = True
    
    # Generate all materials
    print("\n1. Generating school presentation slides...")
    materials["presentation_slides"] = generate_school_presentation_slides(engine)
    all_violations.extend(materials["presentation_slides"]["violations"])
    if not materials["presentation_slides"]["siyem_compliant"]:
        all_compliant = False
    
    print("2. Generating pilot proposal document...")
    materials["pilot_proposal"] = generate_pilot_proposal(engine)
    all_violations.extend(materials["pilot_proposal"]["violations"])
    if not materials["pilot_proposal"]["siyem_compliant"]:
        all_compliant = False
    
    print("3. Generating teacher training materials...")
    materials["teacher_training"] = generate_teacher_training_materials(engine)
    all_violations.extend(materials["teacher_training"]["violations"])
    if not materials["teacher_training"]["siyem_compliant"]:
        all_compliant = False
    
    print("4. Generating parent information packets...")
    materials["parent_packets"] = generate_parent_information_packets(engine)
    all_violations.extend(materials["parent_packets"]["violations"])
    if not materials["parent_packets"]["siyem_compliant"]:
        all_compliant = False
    
    print("5. Generating email templates...")
    materials["email_templates"] = generate_email_templates(engine)
    all_violations.extend(materials["email_templates"]["violations"])
    if not materials["email_templates"]["siyem_compliant"]:
        all_compliant = False
    
    print("6. Generating landing page copy...")
    materials["landing_page"] = generate_landing_page_copy(engine)
    all_violations.extend(materials["landing_page"]["violations"])
    if not materials["landing_page"]["siyem_compliant"]:
        all_compliant = False
    
    # Save all materials
    print("\n7. Saving materials to files...")
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    for material_type, material_data in materials.items():
        filename = f"{material_type}_{timestamp}.md"
        filepath = OUTPUT_DIR / filename
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(f"# {material_type.upper().replace('_', ' ')}\n\n")
            f.write(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"**SIYEM Compliant:** {material_data['siyem_compliant']}\n")
            f.write(f"**Violations:** {len(material_data['violations'])}\n\n")
            f.write("---\n\n")
            f.write(material_data['content'])
        
        print(f"   Saved: {filename}")
    
    # Save summary
    summary = {
        "generated": datetime.now().isoformat(),
        "materials": list(materials.keys()),
        "siyem_compliant": all_compliant,
        "total_violations": len(all_violations),
        "violations": all_violations,
        "output_directory": str(OUTPUT_DIR)
    }
    
    summary_file = OUTPUT_DIR / f"generation_summary_{timestamp}.json"
    with open(summary_file, 'w', encoding='utf-8') as f:
        json.dump(summary, f, indent=2)
    
    print(f"\n   Summary saved: {summary_file.name}")
    
    # Final report
    print("\n" + "=" * 60)
    print("DEPLOYMENT MATERIALS GENERATION COMPLETE")
    print(f"SIYEM Compliant: {all_compliant}")
    print(f"Total Violations: {len(all_violations)}")
    print(f"Output Directory: {OUTPUT_DIR}")
    print("=" * 60)
    
    return summary


if __name__ == "__main__":
    print("DEPLOYMENT MATERIALS GENERATOR")
    print("AI Execution Engine: SIYEM Protocol Enforced")
    print("Knowledge Over Belief: Active\n")
    
    if not AI_ENGINE_AVAILABLE:
        print("ERROR: AI Execution Engine not available.")
        print("Please ensure ANTHROPIC_API_KEY and/or GEMINI_API_KEY are set in environment.")
        sys.exit(1)
    
    result = generate_all_deployment_materials()
    
    if result:
        print("\n✅ All deployment materials generated successfully!")
        print(f"📁 Files saved to: {OUTPUT_DIR}")
    else:
        print("\n❌ Generation failed. Check API keys and try again.")
