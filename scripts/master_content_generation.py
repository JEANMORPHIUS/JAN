"""
MASTER CONTENT GENERATION - GENERATE EVERYTHING
Generate all content at scale using personas

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Generate content. Serve humanity.

PEACE. LOVE. UNITY.
"""

import sys
import requests
import json
import time
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any

project_root = Path(__file__).parent.parent
backend_url = "http://localhost:8000"

class MasterContentGenerator:
    """Generate all content at scale"""
    
    def __init__(self):
        self.results = {
            "timestamp": datetime.now().isoformat(),
            "content_generated": [],
            "errors": [],
            "status": "IN_PROGRESS"
        }
        
    def log(self, message: str, status: str = "INFO"):
        """Log progress"""
        symbol = "[OK]" if status == "SUCCESS" else "[FAIL]" if status == "ERROR" else "[...]"
        print(f"{symbol} {message}")
        
    def get_personas(self) -> List[str]:
        """Get available personas"""
        try:
            response = requests.get(f"{backend_url}/api/jan/personas", timeout=5)
            if response.status_code == 200:
                return response.json()
        except Exception as e:
            self.log(f"Failed to get personas: {e}", "ERROR")
        return []
        
    def generate_content(self, persona: str, prompt: str, output_type: str) -> Dict[str, Any]:
        """Generate content using persona"""
        try:
            response = requests.post(
                f"{backend_url}/api/jan/generate",
                json={
                    "persona": persona,
                    "prompt": prompt,
                    "output_type": output_type,
                    "options": {}
                },
                timeout=60
            )
            
            if response.status_code == 200:
                return response.json()
            else:
                return {"success": False, "error": f"Status {response.status_code}"}
        except Exception as e:
            return {"success": False, "error": str(e)}
            
    def generate_lessons(self, count: int = 376):
        """Generate lesson content"""
        personas = self.get_personas()
        if not personas:
            self.log("No personas available", "ERROR")
            return
            
        educator = "educator" if "educator" in personas else personas[0]
        
        self.log(f"Generating {count} lessons using {educator} persona", "INFO")
        
        generated = 0
        for i in range(1, count + 1):
            prompt = f"Create lesson {i} content for children aged 5-16. Include: title, key teaching, practical application, reflection question."
            result = self.generate_content(educator, prompt, "lesson")
            
            if result.get("success"):
                generated += 1
                if i % 10 == 0:
                    self.log(f"Generated {generated}/{count} lessons", "SUCCESS")
            else:
                self.log(f"Failed to generate lesson {i}: {result.get('error')}", "ERROR")
                self.results["errors"].append(f"Lesson {i}: {result.get('error')}")
                
            time.sleep(0.5)  # Rate limiting
            
        self.log(f"Generated {generated}/{count} lessons", "SUCCESS")
        self.results["content_generated"].append(f"Lessons: {generated}/{count}")
        
    def generate_social_posts(self, count: int = 208):
        """Generate social media posts"""
        personas = self.get_personas()
        if not personas:
            self.log("No personas available", "ERROR")
            return
            
        storyteller = "storyteller" if "storyteller" in personas else personas[0]
        
        self.log(f"Generating {count} social posts using {storyteller} persona", "INFO")
        
        generated = 0
        topics = [
            "Hope and inspiration",
            "Love and unity",
            "Education and learning",
            "Community and connection",
            "Peace and harmony"
        ]
        
        for i in range(1, count + 1):
            topic = topics[i % len(topics)]
            prompt = f"Create social media post {i} about {topic}. Make it engaging, positive, and inspiring."
            result = self.generate_content(storyteller, prompt, "social_post")
            
            if result.get("success"):
                generated += 1
                if i % 20 == 0:
                    self.log(f"Generated {generated}/{count} posts", "SUCCESS")
            else:
                self.log(f"Failed to generate post {i}: {result.get('error')}", "ERROR")
                self.results["errors"].append(f"Post {i}: {result.get('error')}")
                
            time.sleep(0.5)  # Rate limiting
            
        self.log(f"Generated {generated}/{count} social posts", "SUCCESS")
        self.results["content_generated"].append(f"Social Posts: {generated}/{count}")
        
    def save_report(self):
        """Save generation report"""
        self.results["status"] = "COMPLETE"
        report_file = project_root / "output" / "content_generation_report.json"
        report_file.parent.mkdir(parents=True, exist_ok=True)
        
        with open(report_file, 'w') as f:
            json.dump(self.results, f, indent=2)
            
        self.log(f"Report saved: {report_file}", "SUCCESS")
        
    def run_all(self, lessons: int = 10, posts: int = 10):
        """Run all content generation (limited for testing)"""
        print("\n" + "="*80)
        print("MASTER CONTENT GENERATION")
        print("="*80 + "\n")
        
        self.log("Starting content generation", "INFO")
        
        # Generate lessons
        self.generate_lessons(lessons)
        
        # Generate social posts
        self.generate_social_posts(posts)
        
        # Save report
        self.save_report()
        
        print("\n" + "="*80)
        print("CONTENT GENERATION COMPLETE")
        print("="*80 + "\n")
        
        print(f"[OK] Content generated: {len(self.results['content_generated'])} batches")
        if self.results["errors"]:
            print(f"[FAIL] Errors: {len(self.results['errors'])} issues")
        else:
            print("[OK] No errors")
            
        print("\nPEACE. LOVE. UNITY.")
        print("CONTENT GENERATED. READY TO SERVE.\n")

if __name__ == "__main__":
    generator = MasterContentGenerator()
    
    # Full generation - all content
    generator.run_all(lessons=376, posts=208)
