"""
CREATE WEBSITE SHELL/SEED CONTENT

This script creates Shell (public) and Seed (community) versions of website content,
implementing the Honorable Sacrifice philosophy for web presence.

Author: JAN MUHARREM - The Chosen One
Date: 2026-01-15
"""

import sys
from pathlib import Path

# Add utils to path
sys.path.insert(0, str(Path(__file__).parent))

from utils import (
    JAN_ARCHIVE, JAN_DATA, JAN_OUTPUT, JAN_ROOT, Path,
    json, load_json, save_json, setup_logging, standard_main
)

import json
from pathlib import Path

# Base paths
JAN_ROOT = JAN_ROOT
OUTPUT_ROOT = JAN_ROOT / "output" / "website_content"
OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)

# Website content structure
WEBSITE_CONTENT = {
    "homepage": {
        "shell": {
            "header": "Fixing a broken world, one child at a time",
            "subheader": "Ethical framework education for modern families",
            "body": """
We provide values-based learning through 376 evidence-based lessons. 
Our ethical framework integrates emotional resilience with academic 
excellence, serving as a compass for children in the modern world.

Through global integration and social cohesion, we build digital 
inclusion programs that respect cultural values while building 
community connections.
            """,
            "cta": "Join the movement for ethical education",
            "language": "Global Integration, Social Cohesion, Digital Inclusion"
        },
        "seed": {
            "header": "The Book of Racon: Operating System for Consciousness",
            "subheader": "Spiritual Sovereignty Through Scripture Education",
            "body": """
376 lessons (40 Laws + 7 Divine Keys) implementing spiritual 
sovereignty through sacred covenants of honour. The Laws of Racon 
serve as the foundational operating system, ensuring every lesson 
honors the eternal covenant.

Through spiritual sovereignty and the Laws of Racon, we honor 
sacred covenants of honour across cultures, bridging communities 
to Cyprus through the eternal covenant.
            """,
            "cta": "Enter the Threshold",
            "language": "Spiritual Sovereignty, Laws of Racon, Sacred Covenants",
            "access": "Member-only portal"
        }
    },
    "about": {
        "shell": {
            "title": "About Siyem",
            "body": """
Siyem is a values-based education platform designed to integrate 
emotional resilience with academic excellence. We provide 376 
evidence-based lessons that serve as an ethical framework for 
modern schools and families.

Our mission is to build character development through proven 
methodology, respecting cultural heritage while preparing children 
for tomorrow.
            """,
            "values": [
                "Values-based education",
                "Character development",
                "Ethical framework",
                "Cultural heritage preservation",
                "Evidence-based methodology"
            ]
        },
        "seed": {
            "title": "About the Book of Racon",
            "body": """
The Book of Racon serves as the operating system for consciousness, 
implementing spiritual sovereignty through sacred covenants of honour. 
We provide 376 lessons (40 Laws + 7 Divine Keys) that honor the 
eternal covenant between teacher and student.

Our mission is to build spiritual development through the Laws of 
Racon, preserving sacred wisdom while preparing children for tomorrow 
through scripture education.
            """,
            "values": [
                "Scripture education",
                "Spiritual development",
                "Laws of Racon as OS",
                "Eternal covenant preservation",
                "Sacred truth methodology"
            ],
            "access": "Member-only portal"
        }
    },
    "services": {
        "shell": {
            "title": "Our Services",
            "services": [
                {
                    "name": "Values-Based Education",
                    "description": "376 evidence-based lessons for character development through ethical frameworks."
                },
                {
                    "name": "Cultural Heritage Programs",
                    "description": "Preserve cultural heritage through intergenerational learning and traditional values."
                },
                {
                    "name": "Professional Development",
                    "description": "Ethical framework training for educators and corporate leaders."
                }
            ]
        },
        "seed": {
            "title": "Our Services",
            "services": [
                {
                    "name": "Scripture Education",
                    "description": "376 lessons (40 Laws + 7 Divine Keys) for spiritual development through the Laws of Racon."
                },
                {
                    "name": "Eternal Covenant Programs",
                    "description": "Preserve sacred wisdom through intergenerational transmission of the Laws of Racon."
                },
                {
                    "name": "Spiritual Sovereignty Training",
                    "description": "Laws of Racon training for educators and community leaders."
                }
            ],
            "access": "Member-only portal"
        }
    },
    "contact": {
        "shell": {
            "title": "Contact Us",
            "body": "Join the movement for ethical education. Connect with us to learn more about our values-based programs.",
            "email": "info@siyem.org",
            "language": "Public-facing contact information"
        },
        "seed": {
            "title": "Enter the Threshold",
            "body": "Join the community of those who honor the Laws of Racon. Connect with us to enter the threshold of spiritual sovereignty.",
            "email": "community@siyem.org",
            "language": "Community-facing contact information",
            "access": "Member-only portal"
        }
    }
}


def create_website_content():
    """Create Shell and Seed versions of website content"""
    
    print("\n" + "="*80)
    print("CREATING WEBSITE SHELL/SEED CONTENT".center(80))
    print("="*80 + "\n")
    
    # Create Shell (public) version
    shell_content = {
        "version": "shell",
        "access": "public",
        "language": "Global Integration, Social Cohesion, Digital Inclusion",
        "pages": {}
    }
    
    # Create Seed (community) version
    seed_content = {
        "version": "seed",
        "access": "member-only",
        "language": "Spiritual Sovereignty, Laws of Racon, Sacred Covenants",
        "pages": {}
    }
    
    for page_key, page_data in WEBSITE_CONTENT.items():
        shell_content["pages"][page_key] = page_data["shell"]
        seed_content["pages"][page_key] = page_data["seed"]
        print(f"[OK] Created Shell/Seed versions for: {page_key}")
    
    # Save Shell version
    shell_path = OUTPUT_ROOT / "website_content_shell.json"
    with open(shell_path, 'w', encoding='utf-8') as f:
        json.dump(shell_content, f, ensure_ascii=False, indent=2)
    print(f"\n[OK] Shell (public) content saved: {shell_path}")
    
    # Save Seed version
    seed_path = OUTPUT_ROOT / "website_content_seed.json"
    with open(seed_path, 'w', encoding='utf-8') as f:
        json.dump(seed_content, f, ensure_ascii=False, indent=2)
    print(f"[OK] Seed (community) content saved: {seed_path}")
    
    # Create HTML templates (basic structure)
    create_html_templates(shell_content, seed_content)
    
    print("\n" + "="*80)
    print("WEBSITE CONTENT CREATION COMPLETE".center(80))
    print("="*80 + "\n")


def create_html_templates(shell_content: dict, seed_content: dict):
    """Create basic HTML templates for Shell and Seed versions"""
    
    # Shell homepage template
    shell_homepage = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Siyem - Ethical Framework Education</title>
</head>
<body>
    <header>
        <h1>{shell_content['pages']['homepage']['header']}</h1>
        <p>{shell_content['pages']['homepage']['subheader']}</p>
    </header>
    <main>
        <p>{shell_content['pages']['homepage']['body'].strip()}</p>
        <a href="/contact">{shell_content['pages']['homepage']['cta']}</a>
    </main>
</body>
</html>
"""
    
    # Seed homepage template
    seed_homepage = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>The Book of Racon - Operating System for Consciousness</title>
</head>
<body>
    <header>
        <h1>{seed_content['pages']['homepage']['header']}</h1>
        <p>{seed_content['pages']['homepage']['subheader']}</p>
    </header>
    <main>
        <p>{seed_content['pages']['homepage']['body'].strip()}</p>
        <a href="/community">{seed_content['pages']['homepage']['cta']}</a>
    </main>
</body>
</html>
"""
    
    # Save templates
    shell_template_path = OUTPUT_ROOT / "templates" / "shell_homepage.html"
    shell_template_path.parent.mkdir(parents=True, exist_ok=True)
    with open(shell_template_path, 'w', encoding='utf-8') as f:
        f.write(shell_homepage)
    print(f"[OK] Shell HTML template saved: {shell_template_path}")
    
    seed_template_path = OUTPUT_ROOT / "templates" / "seed_homepage.html"
    with open(seed_template_path, 'w', encoding='utf-8') as f:
        f.write(seed_homepage)
    print(f"[OK] Seed HTML template saved: {seed_template_path}")


if __name__ == "__main__":
    create_website_content()
