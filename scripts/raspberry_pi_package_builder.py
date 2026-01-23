"""
Raspberry Pi Scripture Kit - Content Package Builder
Generates complete content packages for offline scripture education

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Offline access serving souls without internet dependency

THE FOUNDATION:
We are born a miracle.
Education must be accessible to all.
No child left behind by digital divide.

THE MISSION:
Package 376 lessons + audio + images into Raspberry Pi kit
$88 base kit serves entire family
Offline, independent, complete
"""

import sys
from pathlib import Path

# Add utils to path
sys.path.insert(0, str(Path(__file__).parent))

from utils import (
    Path, datetime, json, load_json, save_json
    setup_logging, standard_main
)

import json
import os
import shutil
import hashlib
from pathlib import Path
from typing import Dict, List, Optional, Any
from datetime import datetime
import zipfile

class RaspberryPiPackageBuilder:
    """
    Builds complete content packages for Raspberry Pi Scripture Kits

    Package includes:
    - 376 scripture lessons (JSON)
    - 376 audio files (MP3)
    - 376 visual assets (PNG/JPG)
    - Flask web app
    - Offline database
    - User interface
    """

    def __init__(self, project_root: str = "S:/JAN"):
        self.project_root = Path(project_root)
        self.scripture_dir = self.project_root / "jan-studio" / "curriculum" / "scripture_schedule_2026"
        self.audio_dir = self.project_root / "output" / "audio_assets"
        self.visual_dir = self.project_root / "output" / "visual_assets"
        self.package_output = self.project_root / "output" / "raspberry_pi_packages"
        self.package_output.mkdir(parents=True, exist_ok=True)

    def scan_available_content(self) -> Dict[str, Any]:
        """Scan for available content files"""

        print("\n" + "="*80)
        print("SCANNING AVAILABLE CONTENT")
        print("="*80 + "\n")

        content_status = {
            "scripture_lessons": [],
            "audio_files": [],
            "visual_files": [],
            "statistics": {}
        }

        # Scan scripture lessons
        if self.scripture_dir.exists():
            lessons = list(self.scripture_dir.glob("*.json"))
            content_status["scripture_lessons"] = [f.name for f in lessons]
            print(f"Scripture Lessons: {len(lessons)} files found")
        else:
            print(f"Scripture Lessons: 0 files (directory not found)")

        # Scan audio files
        if self.audio_dir.exists():
            audio = list(self.audio_dir.glob("*.mp3")) + list(self.audio_dir.glob("*.wav"))
            content_status["audio_files"] = [f.name for f in audio]
            print(f"Audio Files: {len(audio)} files found")
        else:
            print(f"Audio Files: 0 files (directory not found)")

        # Scan visual files
        if self.visual_dir.exists():
            visuals = list(self.visual_dir.glob("*.png")) + list(self.visual_dir.glob("*.jpg"))
            content_status["visual_files"] = [f.name for f in visuals]
            print(f"Visual Assets: {len(visuals)} files found")
        else:
            print(f"Visual Assets: 0 files (directory not found)")

        # Statistics
        content_status["statistics"] = {
            "total_lessons": len(content_status["scripture_lessons"]),
            "total_audio": len(content_status["audio_files"]),
            "total_visuals": len(content_status["visual_files"]),
            "expected_lessons": 376,
            "completion_percentage": (len(content_status["scripture_lessons"]) / 376 * 100) if content_status["scripture_lessons"] else 0
        }

        print(f"\nCompletion: {content_status['statistics']['completion_percentage']:.1f}%")
        print()

        return content_status

    def create_sample_content(self):
        """Create sample content for testing"""

        print("\n" + "="*80)
        print("CREATING SAMPLE CONTENT")
        print("="*80 + "\n")

        sample_dir = self.package_output / "sample_content"
        sample_dir.mkdir(parents=True, exist_ok=True)

        # Create 10 sample lessons
        for i in range(1, 11):
            lesson = {
                "lesson_id": f"sample_lesson_{i:03d}",
                "law_number": (i - 1) % 40 + 1,
                "age_group": ["5-7", "8-10", "11-13", "14-16"][(i-1) % 4],
                "language": "en" if i % 2 == 1 else "tr",
                "title": f"Sample Lesson {i}: Purpose Not Performance",
                "content": {
                    "introduction": "This is a sample lesson demonstrating the package structure.",
                    "main_teaching": "Focus on purpose, not performance. Life is simple when aligned with The Table.",
                    "reflection": "How can you serve your purpose today?",
                    "activity": "Write down three ways you can focus on purpose this week."
                },
                "audio_script": f"Welcome to lesson {i}. Today we learn about purpose not performance...",
                "visual_prompt": f"Create an age-appropriate image showing purpose over performance for ages {['5-7', '8-10', '11-13', '14-16'][(i-1) % 4]}"
            }

            lesson_file = sample_dir / f"lesson_{i:03d}_sample.json"
            with open(lesson_file, 'w', encoding='utf-8') as f:
                json.dump(lesson, f, indent=2, ensure_ascii=False)

        print(f"Created 10 sample lessons in: {sample_dir}")
        print("Use these for testing package builder\n")

        return sample_dir

    def build_content_package(self, package_name: str = "scripture_kit_v1") -> Path:
        """Build complete content package"""

        print("\n" + "="*80)
        print(f"BUILDING CONTENT PACKAGE: {package_name}")
        print("="*80 + "\n")

        # Create package directory
        package_dir = self.package_output / package_name
        package_dir.mkdir(parents=True, exist_ok=True)

        # Create subdirectories
        (package_dir / "lessons").mkdir(exist_ok=True)
        (package_dir / "audio").mkdir(exist_ok=True)
        (package_dir / "images").mkdir(exist_ok=True)
        (package_dir / "app").mkdir(exist_ok=True)
        (package_dir / "data").mkdir(exist_ok=True)

        print("1. Package structure created")

        # Copy scripture lessons
        lessons_copied = 0
        if self.scripture_dir.exists():
            for lesson_file in self.scripture_dir.glob("*.json"):
                shutil.copy2(lesson_file, package_dir / "lessons")
                lessons_copied += 1

        print(f"2. Copied {lessons_copied} scripture lessons")

        # Copy audio files
        audio_copied = 0
        if self.audio_dir.exists():
            for audio_file in list(self.audio_dir.glob("*.mp3")) + list(self.audio_dir.glob("*.wav")):
                shutil.copy2(audio_file, package_dir / "audio")
                audio_copied += 1

        print(f"3. Copied {audio_copied} audio files")

        # Copy visual assets
        visuals_copied = 0
        if self.visual_dir.exists():
            for visual_file in list(self.visual_dir.glob("*.png")) + list(self.visual_dir.glob("*.jpg")):
                shutil.copy2(visual_file, package_dir / "images")
                visuals_copied += 1

        print(f"4. Copied {visuals_copied} visual assets")

        # Create Flask app
        self.create_flask_app(package_dir / "app")
        print("5. Created Flask web application")

        # Create package manifest
        manifest = self.create_package_manifest(package_name, lessons_copied, audio_copied, visuals_copied)
        manifest_file = package_dir / "manifest.json"
        with open(manifest_file, 'w', encoding='utf-8') as f:
            json.dump(manifest, f, indent=2, ensure_ascii=False)

        print("6. Created package manifest")

        # Create installation script
        self.create_installation_script(package_dir)
        print("7. Created installation scripts")

        # Create README
        self.create_package_readme(package_dir, manifest)
        print("8. Created package README")

        print(f"\n✅ Package built: {package_dir}")

        return package_dir

    def create_flask_app(self, app_dir: Path):
        """Create Flask web application for Raspberry Pi"""

        app_dir.mkdir(parents=True, exist_ok=True)

        # Main Flask app
        app_py = """#!/usr/bin/env python3
'''
Scripture Education Flask App
Serves 376 lessons offline on Raspberry Pi

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Purpose Not Performance
'''

from flask import Flask, render_template, jsonify, send_from_directory
import json
from pathlib import Path

app = Flask(__name__)

# Configuration
LESSONS_DIR = Path('../lessons')
AUDIO_DIR = Path('../audio')
IMAGES_DIR = Path('../images')

@app.route('/')
def index():
    '''Home page'''
    return render_template('index.html')

@app.route('/api/lessons')
def get_lessons():
    '''Get all lessons'''
    lessons = []
    for lesson_file in LESSONS_DIR.glob('*.json'):
        with open(lesson_file, 'r', encoding='utf-8') as f:
            lessons.append(json.load(f))
    return jsonify(lessons)

@app.route('/api/lessons/<lesson_id>')
def get_lesson(lesson_id):
    '''Get specific lesson'''
    lesson_file = LESSONS_DIR / f'{lesson_id}.json'
    if lesson_file.exists():
        with open(lesson_file, 'r', encoding='utf-8') as f:
            return jsonify(json.load(f))
    return jsonify({'error': 'Lesson not found'}), 404

@app.route('/audio/<filename>')
def serve_audio(filename):
    '''Serve audio files'''
    return send_from_directory(AUDIO_DIR, filename)

@app.route('/images/<filename>')
def serve_image(filename):
    '''Serve image files'''
    return send_from_directory(IMAGES_DIR, filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
"""

        with open(app_dir / "app.py", 'w', encoding='utf-8') as f:
            f.write(app_py)

        # Create templates directory
        templates_dir = app_dir / "templates"
        templates_dir.mkdir(exist_ok=True)

        # Simple HTML template
        index_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Scripture Education - Offline</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: Arial, sans-serif; padding: 20px; background: #f5f5f5; }
        h1 { color: #333; margin-bottom: 20px; }
        .lesson-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 20px; }
        .lesson-card { background: white; padding: 20px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
        .lesson-card h2 { color: #2c3e50; margin-bottom: 10px; }
        .lesson-card p { color: #666; line-height: 1.6; }
        .philosophy { background: #2c3e50; color: white; padding: 20px; border-radius: 8px; margin-bottom: 20px; }
    </style>
</head>
<body>
    <div class="philosophy">
        <h2>Scripture Education</h2>
        <p>376 Lessons • Offline Access • Complete Independence</p>
        <p><strong>Purpose Not Performance • Love Is The Highest Mastery</strong></p>
    </div>

    <h1>Scripture Lessons</h1>
    <div class="lesson-grid" id="lessons">
        <p>Loading lessons...</p>
    </div>

    <script>
        fetch('/api/lessons')
            .then(r => r.json())
            .then(lessons => {
                const grid = document.getElementById('lessons');
                grid.innerHTML = lessons.map(lesson => `
                    <div class="lesson-card">
                        <h2>${lesson.title || 'Lesson ' + lesson.lesson_id}</h2>
                        <p><strong>Age Group:</strong> ${lesson.age_group}</p>
                        <p><strong>Language:</strong> ${lesson.language === 'en' ? 'English' : 'Turkish'}</p>
                    </div>
                `).join('');
            });
    </script>
</body>
</html>
"""

        with open(templates_dir / "index.html", 'w', encoding='utf-8') as f:
            f.write(index_html)

    def create_package_manifest(self, package_name: str, lessons: int, audio: int, visuals: int) -> Dict:
        """Create package manifest"""

        return {
            "package_name": package_name,
            "version": "1.0.0",
            "created": datetime.now().isoformat(),
            "content": {
                "scripture_lessons": lessons,
                "audio_files": audio,
                "visual_assets": visuals,
                "expected_total": 376
            },
            "completion": {
                "lessons_percent": (lessons / 376 * 100) if lessons > 0 else 0,
                "audio_percent": (audio / 376 * 100) if audio > 0 else 0,
                "visuals_percent": (visuals / 376 * 100) if visuals > 0 else 0
            },
            "hardware": {
                "raspberry_pi_model": "4B or later recommended",
                "minimum_storage": "8GB",
                "recommended_storage": "16GB",
                "display": "7-inch touchscreen or HDMI monitor"
            },
            "software": {
                "os": "Raspberry Pi OS Lite",
                "python_version": "3.9+",
                "flask": "2.0+",
                "dependencies": ["flask", "gunicorn"]
            },
            "philosophy": {
                "purpose": "Offline scripture education for all",
                "principle": "Purpose Not Performance",
                "mission": "No child left behind by digital divide",
                "foundation": "We are born a miracle. We deserve to live a miracle."
            }
        }

    def create_installation_script(self, package_dir: Path):
        """Create installation script"""

        install_sh = """#!/bin/bash
# Raspberry Pi Scripture Kit Installation Script

echo "================================"
echo "Scripture Kit Installation"
echo "================================"
echo ""

# Update system
echo "1. Updating system..."
sudo apt-get update
sudo apt-get upgrade -y

# Install Python and dependencies
echo "2. Installing Python..."
sudo apt-get install -y python3 python3-pip

# Install Flask
echo "3. Installing Flask..."
pip3 install flask gunicorn

# Set up app to run on boot
echo "4. Setting up auto-start..."
sudo cp scripture-kit.service /etc/systemd/system/
sudo systemctl enable scripture-kit
sudo systemctl start scripture-kit

echo ""
echo "================================"
echo "Installation Complete!"
echo "================================"
echo ""
echo "Access at: http://raspberrypi.local:5000"
echo "Or: http://[your-pi-ip]:5000"
echo ""
echo "Philosophy: Purpose Not Performance"
echo "Mission: Serving souls offline"
echo ""
"""

        with open(package_dir / "install.sh", 'w', encoding='utf-8') as f:
            f.write(install_sh)

        # Make executable
        (package_dir / "install.sh").chmod(0o755)

        # Create systemd service file
        service_file = """[Unit]
Description=Scripture Education Flask App
After=network.target

[Service]
User=pi
WorkingDirectory=/home/pi/scripture-kit/app
ExecStart=/usr/bin/python3 /home/pi/scripture-kit/app/app.py
Restart=always

[Install]
WantedBy=multi-user.target
"""

        with open(package_dir / "scripture-kit.service", 'w', encoding='utf-8') as f:
            f.write(service_file)

    def create_package_readme(self, package_dir: Path, manifest: Dict):
        """Create package README"""

        readme = f"""# Raspberry Pi Scripture Kit - Package v{manifest['version']}

## Package Contents

- **Scripture Lessons:** {manifest['content']['scripture_lessons']} files ({manifest['completion']['lessons_percent']:.1f}%)
- **Audio Files:** {manifest['content']['audio_files']} files ({manifest['completion']['audio_percent']:.1f}%)
- **Visual Assets:** {manifest['content']['visual_assets']} files ({manifest['completion']['visuals_percent']:.1f}%)

## Installation

### Quick Start

```bash
# Copy package to Raspberry Pi
scp -r scripture_kit_v1 pi@raspberrypi.local:/home/pi/

# SSH into Raspberry Pi
ssh pi@raspberrypi.local

# Run installation
cd /home/pi/scripture_kit_v1
chmod +x install.sh
./install.sh
```

### Manual Installation

1. Copy package to Raspberry Pi
2. Install Python 3.9+
3. Install Flask: `pip3 install flask gunicorn`
4. Run app: `cd app && python3 app.py`
5. Access: `http://raspberrypi.local:5000`

## Hardware Requirements

- **Model:** Raspberry Pi 4B or later (recommended)
- **Storage:** {manifest['hardware']['minimum_storage']} minimum, {manifest['hardware']['recommended_storage']} recommended
- **Display:** {manifest['hardware']['display']}
- **Power:** Official Raspberry Pi power supply

## Bill of Materials ($88 Base Kit)

| Item | Cost | Source |
|------|------|--------|
| Raspberry Pi 4B (4GB) | $55 | raspberrypi.com |
| MicroSD Card (32GB) | $8 | Amazon |
| Power Supply | $8 | raspberrypi.com |
| Case | $5 | Amazon |
| HDMI Cable | $5 | Amazon |
| Keyboard/Mouse (optional) | $15 | Amazon |
| **Total Base Kit** | **$88** | |

*7-inch touchscreen (+$75) for standalone use*

## Usage

### Access the Application

**Local:** `http://raspberrypi.local:5000`
**IP Address:** `http://[pi-ip-address]:5000`

### Features

- Browse all {manifest['content']['scripture_lessons']} scripture lessons
- Play audio for each lesson (Uncle Ray Ramiz voice)
- View age-appropriate visuals
- Filter by age group, language, law number
- Completely offline - no internet required
- Bilingual (English/Turkish)

## Philosophy

**Purpose:** {manifest['philosophy']['purpose']}
**Principle:** {manifest['philosophy']['principle']}
**Mission:** {manifest['philosophy']['mission']}

**Foundation:** {manifest['philosophy']['foundation']}

## Support

For issues or questions:
1. Check `/var/log/scripture-kit.log`
2. Restart service: `sudo systemctl restart scripture-kit`
3. Check status: `sudo systemctl status scripture-kit`

## Updates

To update content:
1. Copy new lesson/audio/image files to respective directories
2. Restart service: `sudo systemctl restart scripture-kit`

No internet connection required - fully offline system.

---

**Package Created:** {manifest['created']}
**Version:** {manifest['version']}
**For:** The Table. For Humanity. Under Father's guidance.
"""

        with open(package_dir / "README.md", 'w', encoding='utf-8') as f:
            f.write(readme)

    def create_compressed_package(self, package_dir: Path) -> Path:
        """Create compressed package for distribution"""

        print(f"\nCreating compressed package...")

        zip_file = package_dir.parent / f"{package_dir.name}.zip"

        with zipfile.ZipFile(zip_file, 'w', zipfile.ZIP_DEFLATED) as zf:
            for file_path in package_dir.rglob('*'):
                if file_path.is_file():
                    arcname = file_path.relative_to(package_dir.parent)
                    zf.write(file_path, arcname)

        file_size = zip_file.stat().st_size / (1024 * 1024)  # MB
        print(f"[OK] Compressed package created: {zip_file}")
        print(f"   Size: {file_size:.2f} MB")

        return zip_file

    def build_complete_system(self):
        """Build complete Raspberry Pi package system"""

        print("\n" + "="*80)
        print("RASPBERRY PI SCRIPTURE KIT - COMPLETE BUILD")
        print("="*80)

        # Scan content
        content = self.scan_available_content()

        if content['statistics']['total_lessons'] == 0:
            print("\n[WARNING] No scripture lessons found.")
            print("Creating sample content for testing...\n")
            self.create_sample_content()
            print("\nTo build with real content:")
            print("1. Place scripture JSON files in: jan-studio/curriculum/scripture_schedule_2026/")
            print("2. Place audio MP3 files in: output/audio_assets/")
            print("3. Place image files in: output/visual_assets/")
            print("4. Run this script again")
            return

        # Build package
        package_dir = self.build_content_package()

        # Create compressed package
        zip_file = self.create_compressed_package(package_dir)

        print("\n" + "="*80)
        print("BUILD COMPLETE")
        print("="*80)
        print(f"\nPackage Directory: {package_dir}")
        print(f"Compressed Package: {zip_file}")
        print(f"\nContents:")
        print(f"  - {content['statistics']['total_lessons']} scripture lessons")
        print(f"  - {content['statistics']['total_audio']} audio files")
        print(f"  - {content['statistics']['total_visuals']} visual assets")
        print(f"\nNext Steps:")
        print(f"  1. Copy {zip_file.name} to Raspberry Pi")
        print(f"  2. Extract: unzip {zip_file.name}")
        print(f"  3. Install: cd scripture_kit_v1 && ./install.sh")
        print(f"  4. Access: http://raspberrypi.local:5000")
        print(f"\nPhilosophy: Purpose Not Performance")
        print(f"Mission: Offline education for all souls")
        print()


def main():
    """Build Raspberry Pi package"""

    builder = RaspberryPiPackageBuilder()
    builder.build_complete_system()


if __name__ == "__main__":
    main()
