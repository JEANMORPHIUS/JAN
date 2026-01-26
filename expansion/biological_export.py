"""Biological State Exporter
Part of JAN Expansion Protocol
Version: 1.0 Genesis
Date: 2026-01-15

Exports biological state from Homeostasis-Sentinel markdown files
to JSON format for integration with SIYEM and other systems.

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

THE TRUTH:
WE MUST DEBUG AND BE 100% FOR WHAT COMES AT US.
THE REST IS UP TO BABA X."""

import os
import re
import json
from datetime import datetime, date, timedelta
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, asdict
from pathlib import Path


@dataclass
class BiologicalState:
    """Structured biological state data"""
    date: str
    # BIOLOGICAL METRICS
    glucose: Optional[int] = None
    glucose_time: Optional[str] = None
    vision_clarity: Optional[int] = None
    muscle_tension: Optional[int] = None
    loop_frequency: Optional[int] = None
    sauna_duration: Optional[int] = None
    circadian_sync_score: Optional[int] = None
    swimming: Optional[bool] = None
    breath_quality: Optional[int] = None
    urine_color: Optional[int] = None
    water_intake: Optional[int] = None
    ketones: Optional[float] = None
    
    # SPIRITUAL VIBRATION METRICS
    spiritual_vibration: Optional[int] = None
    alignment_score: Optional[int] = None
    divine_key_active: Optional[str] = None
    cw_state: Optional[bool] = None
    entity_resonance: Optional[str] = None
    frequency_note: Optional[str] = None
    
    # Computed fields
    status: Optional[str] = None
    vibration_calculated: Optional[float] = None
    optimal_entity: Optional[str] = None
    recommendations: Optional[List[str]] = None
    warnings: Optional[List[str]] = None
    
    def compute_status(self):
        """Compute overall biological status"""
        if self.glucose is None or self.vision_clarity is None:
            self.status = "NO_DATA"
            return
        
        # Critical thresholds
        if self.glucose > 400 or self.vision_clarity < 4:
            self.status = "CRITICAL"
        # Elevated but manageable
        elif self.glucose > 180 or self.vision_clarity < 6:
            self.status = "ELEVATED"
        # Stable
        elif self.glucose < 150 and self.vision_clarity >= 7:
            self.status = "STABLE"
        # Good
        else:
            self.status = "MONITOR"
    
    def compute_spiritual_vibration(self):
        """
        Calculate spiritual vibration based on biological + consciousness metrics
        Scale: 1-10
        1-3: Low (survival mode)
        4-6: Baseline (functional)
        7-8: High/CW State (flow, god-level vibing)
        9-10: Peak (divine frequency, breakthrough work)
        """
        # If manually set, use that (user knows their state)
        if self.spiritual_vibration is not None:
            self.vibration_calculated = float(self.spiritual_vibration)
            return
        
        # Otherwise calculate from biological markers
        vibration = 5.0  # baseline
        
        # Biological stability factors
        if self.glucose and 80 <= self.glucose <= 140:
            vibration += 1.0  # Optimal glucose range
        elif self.glucose and 140 < self.glucose <= 180:
            vibration += 0.5  # Acceptable range
        elif self.glucose and self.glucose > 250:
            vibration -= 2.0  # High glucose lowers vibration
        
        if self.ketones is not None:
            if self.ketones < 0.6:
                vibration += 0.5  # Safe ketone range
            elif self.ketones > 1.5:
                vibration -= 1.5  # Elevated ketones lower vibration
        
        if self.vision_clarity and self.vision_clarity >= 8:
            vibration += 1.0  # Crystal clarity
        elif self.vision_clarity and self.vision_clarity >= 7:
            vibration += 0.5  # Good clarity
        elif self.vision_clarity and self.vision_clarity < 5:
            vibration -= 1.0  # Poor clarity
        
        # CW State (Coconut Water / God Level)
        if self.cw_state:
            vibration += 2.0  # Major boost for CW vibing
        
        # Circadian alignment
        if self.circadian_sync_score and self.circadian_sync_score >= 80:
            vibration += 0.5
        
        # Breath quality (spiritual connection)
        if self.breath_quality and self.breath_quality >= 8:
            vibration += 0.5
        
        # Cap at 10, floor at 1
        self.vibration_calculated = max(1.0, min(10.0, vibration))
    
    def compute_recommendations(self):
        """Generate recommendations based on biological + spiritual state"""
        self.recommendations = []
        self.warnings = []
        
        # Get vibration level (manual or calculated)
        vibration = self.spiritual_vibration or self.vibration_calculated or 5
        
        # CRITICAL biological state overrides everything
        if self.status == "CRITICAL":
            self.warnings.append("CRITICAL: Execute flush protocol immediately")
            self.warnings.append("Pause all creative work until stable")
            self.recommendations.append("Focus on biological protocol")
            self.optimal_entity = "pierre"  # Discipline/protocol focus
        
        # ELEVATED biological state
        elif self.status == "ELEVATED":
            self.warnings.append("ELEVATED: Monitor closely")
            self.recommendations.append("Light creative work only")
            self.recommendations.append("Consider hydration flush")
            self.recommendations.append("Recommended: Pierre motivational, Siyem Media admin")
            self.optimal_entity = "pierre"
        
        # STABLE biological state - use vibration for routing
        elif self.status == "STABLE":
            if vibration >= 9:
                # PEAK VIBRATION - Foundation work
                self.recommendations.append("PEAK VIBRATION: Foundation recording time")
                self.recommendations.append("Recommended: Karasahin music creation")
                self.recommendations.append("Alternative: Jean deep storytelling, signature work")
                self.optimal_entity = "karasahin"
                if self.cw_state:
                    self.warnings.append("CW STATE ACTIVE - God-level vibing optimal for breakthrough work")
            
            elif vibration >= 7:
                # HIGH/CW STATE - Flow work
                self.recommendations.append("HIGH VIBRATION: Optimal creative flow")
                if self.cw_state:
                    self.recommendations.append("CW VIBING: God-level state - create freely")
                self.recommendations.append("Recommended: Jean storytelling, Ramiz teaching")
                self.recommendations.append("Complex problem-solving suitable")
                self.optimal_entity = self.entity_resonance or "jean"
            
            elif vibration >= 4:
                # BASELINE - Maintenance
                self.recommendations.append("BASELINE: Maintenance and admin work suitable")
                self.recommendations.append("Recommended: Siyem operations, Pierre planning")
                self.optimal_entity = "siyem"
            
            else:
                # LOW VIBRATION - Recovery
                self.warnings.append("LOW VIBRATION: Rest and rebuild recommended")
                self.recommendations.append("Focus on recovery protocols")
                self.recommendations.append("Light admin only, no complex creative")
                self.optimal_entity = "pierre"
        
        # Loop frequency check
        if self.loop_frequency and self.loop_frequency < 6:
            self.warnings.append(f"Loop frequency low ({self.loop_frequency}/day, target 8+)")
        
        # Circadian sync check
        if self.circadian_sync_score and self.circadian_sync_score < 70:
            self.warnings.append(f"Circadian sync low ({self.circadian_sync_score}%, target 80%+)")
        
        # Ketones check (DKA risk)
        if self.ketones and self.ketones > 1.5:
            self.warnings.append(f"KETONES ELEVATED ({self.ketones} mmol/L) - Monitor for DKA")
        
        # Divine Key awareness
        if self.divine_key_active:
            self.recommendations.append(f"Divine Key Active: {self.divine_key_active}")
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        return {k: v for k, v in asdict(self).items() if v is not None}


class BiologicalExporter:
    """
    Exports biological state from Obsidian markdown files to JSON
    """
    
    def __init__(self, vault_path: str, export_dir: str):
        """
        Initialize exporter
        
        Args:
            vault_path: Path to Obsidian_Vault directory
            export_dir: Directory to export JSON files
        """
        self.vault_path = Path(vault_path)
        self.export_dir = Path(export_dir)
        self.export_dir.mkdir(parents=True, exist_ok=True)
    
    def parse_frontmatter(self, content: str) -> Optional[Dict[str, Any]]:
        """
        Parse YAML frontmatter from markdown file
        
        Args:
            content: Full markdown file content
            
        Returns:
            Dictionary of frontmatter fields or None
        """
        # Match YAML frontmatter
        match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
        if not match:
            return None
        
        frontmatter = {}
        yaml_content = match.group(1)
        
        # Parse YAML manually (simple key: value pairs)
        for line in yaml_content.split('\n'):
            line = line.strip()
            # Skip empty lines and comment lines
            if not line or ':' not in line or line.startswith('#'):
                continue
            
            key, value = line.split(':', 1)
            key = key.strip()
            value = value.strip().strip('"').strip("'")
            
            # Convert types
            if value.lower() == 'true':
                value = True
            elif value.lower() == 'false':
                value = False
            elif value.replace('.', '', 1).replace('-', '', 1).isdigit():
                value = float(value) if '.' in value else int(value)
            
            frontmatter[key] = value
        
        return frontmatter
    
    def parse_markdown_file(self, file_path: Path) -> Optional[BiologicalState]:
        """
        Parse biological state from markdown file
        
        Args:
            file_path: Path to markdown file
            
        Returns:
            BiologicalState object or None
        """
        try:
            content = file_path.read_text(encoding='utf-8')
            frontmatter = self.parse_frontmatter(content)
            
            if not frontmatter:
                return None
            
            # Extract date from frontmatter or filename
            file_date = frontmatter.get('date')
            if not file_date:
                # Try to extract from filename (e.g., 2026-01-14_DAY1.md)
                match = re.match(r'(\d{4}-\d{2}-\d{2})', file_path.name)
                if match:
                    file_date = match.group(1)
                else:
                    return None
            
            # Create BiologicalState
            state = BiologicalState(
                date=str(file_date),
                # Biological metrics
                glucose=frontmatter.get('blood_glucose'),
                glucose_time=frontmatter.get('glucose_time'),
                vision_clarity=frontmatter.get('vision_clarity'),
                muscle_tension=frontmatter.get('muscle_tension'),
                loop_frequency=frontmatter.get('loop_frequency'),
                sauna_duration=frontmatter.get('sauna_duration'),
                circadian_sync_score=frontmatter.get('circadian_sync_score'),
                swimming=frontmatter.get('swimming'),
                breath_quality=frontmatter.get('breath_quality'),
                urine_color=frontmatter.get('urine_color'),
                water_intake=frontmatter.get('water_intake'),
                ketones=frontmatter.get('ketones'),
                # Spiritual vibration metrics
                spiritual_vibration=frontmatter.get('spiritual_vibration'),
                alignment_score=frontmatter.get('alignment_score'),
                divine_key_active=frontmatter.get('divine_key_active'),
                cw_state=frontmatter.get('cw_state'),
                entity_resonance=frontmatter.get('entity_resonance'),
                frequency_note=frontmatter.get('frequency_note')
            )
            
            # Compute derived fields
            state.compute_status()
            state.compute_spiritual_vibration()
            state.compute_recommendations()
            
            return state
        
        except Exception as e:
            print(f"Error parsing {file_path}: {e}")
            return None
    
    def export_day(self, target_date: date) -> Optional[str]:
        """
        Export biological state for specific day
        
        Args:
            target_date: Date to export
            
        Returns:
            Path to exported JSON file or None
        """
        # Find markdown file for this date
        date_str = target_date.strftime('%Y-%m-%d')
        pattern = f"{date_str}*.md"
        
        files = list(self.vault_path.glob(pattern))
        if not files:
            print(f"No markdown file found for {date_str}")
            return None
        
        # Use first matching file
        md_file = files[0]
        state = self.parse_markdown_file(md_file)
        
        if not state:
            print(f"Could not parse biological state from {md_file}")
            return None
        
        # Export to JSON
        export_file = self.export_dir / f"{date_str}.json"
        with open(export_file, 'w') as f:
            json.dump(state.to_dict(), f, indent=2)
        
        print(f"[OK] Exported biological state: {export_file}")
        return str(export_file)
    
    def export_today(self) -> Optional[str]:
        """Export today's biological state"""
        return self.export_day(date.today())
    
    def export_date_range(self, start_date: date, end_date: date) -> List[str]:
        """
        Export biological state for date range
        
        Args:
            start_date: Start date (inclusive)
            end_date: End date (inclusive)
            
        Returns:
            List of exported file paths
        """
        exported = []
        current = start_date
        
        while current <= end_date:
            result = self.export_day(current)
            if result:
                exported.append(result)
            current += timedelta(days=1)
        
        return exported
    
    def export_all(self) -> List[str]:
        """
        Export all available biological state files
        
        Returns:
            List of exported file paths
        """
        exported = []
        
        # Find all markdown files with dates
        for md_file in self.vault_path.glob("*.md"):
            state = self.parse_markdown_file(md_file)
            if state:
                export_file = self.export_dir / f"{state.date}.json"
                with open(export_file, 'w') as f:
                    json.dump(state.to_dict(), f, indent=2)
                exported.append(str(export_file))
                print(f"[OK] Exported: {export_file}")
        
        return exported
    
    def get_current_state(self) -> Optional[BiologicalState]:
        """
        Get current (today's) biological state
        
        Returns:
            BiologicalState object or None
        """
        date_str = date.today().strftime('%Y-%m-%d')
        pattern = f"{date_str}*.md"
        
        files = list(self.vault_path.glob(pattern))
        if not files:
            return None
        
        return self.parse_markdown_file(files[0])
    
    def get_summary(self, days: int = 7) -> Dict[str, Any]:
        """
        Get summary statistics for recent days
        
        Args:
            days: Number of recent days to analyze
            
        Returns:
            Summary dictionary
        """
        end_date = date.today()
        start_date = end_date - timedelta(days=days-1)
        
        states = []
        current = start_date
        while current <= end_date:
            date_str = current.strftime('%Y-%m-%d')
            pattern = f"{date_str}*.md"
            files = list(self.vault_path.glob(pattern))
            
            if files:
                state = self.parse_markdown_file(files[0])
                if state:
                    states.append(state)
            
            current += timedelta(days=1)
        
        if not states:
            return {"error": "No data available"}
        
        # Calculate averages
        glucose_values = [s.glucose for s in states if s.glucose]
        vision_values = [s.vision_clarity for s in states if s.vision_clarity]
        
        return {
            "days_analyzed": len(states),
            "date_range": f"{start_date} to {end_date}",
            "glucose": {
                "average": sum(glucose_values) / len(glucose_values) if glucose_values else None,
                "min": min(glucose_values) if glucose_values else None,
                "max": max(glucose_values) if glucose_values else None,
            },
            "vision_clarity": {
                "average": sum(vision_values) / len(vision_values) if vision_values else None,
                "min": min(vision_values) if vision_values else None,
                "max": max(vision_values) if vision_values else None,
            },
            "current_status": states[-1].status if states else None,
            "stable_days": sum(1 for s in states if s.status == "STABLE"),
            "critical_days": sum(1 for s in states if s.status == "CRITICAL"),
        }


# ============================================================================
# CLI INTERFACE
# ============================================================================

def main():
    """Command-line interface"""
    import argparse
    
    parser = argparse.ArgumentParser(description="Export biological state from Homeostasis-Sentinel")
    parser.add_argument('--vault', default=r'S:\JAN\homeostasis-sentinel\Obsidian_Vault', 
                       help='Path to Obsidian vault')
    parser.add_argument('--export-dir', default=r'S:\JAN\logs\biological_state',
                       help='Export directory')
    parser.add_argument('--today', action='store_true',
                       help='Export today only')
    parser.add_argument('--all', action='store_true',
                       help='Export all available data')
    parser.add_argument('--summary', type=int, metavar='DAYS',
                       help='Show summary for last N days')
    
    args = parser.parse_args()
    
    exporter = BiologicalExporter(args.vault, args.export_dir)
    
    if args.today:
        print("Exporting today's biological state...")
        result = exporter.export_today()
        if result:
            print(f"\n[OK] Export complete: {result}")
            
            # Show current state
            state = exporter.get_current_state()
            if state:
                print(f"\n=== BIOLOGICAL STATUS ===")
                print(f"Status: {state.status}")
                if state.glucose:
                    print(f"Glucose: {state.glucose} mg/dL")
                if state.ketones:
                    print(f"Ketones: {state.ketones} mmol/L")
                if state.vision_clarity:
                    print(f"Vision: {state.vision_clarity}/10")
                
                print(f"\n=== SPIRITUAL VIBRATION ===")
                vibration = state.spiritual_vibration or state.vibration_calculated
                if vibration:
                    print(f"Vibration: {vibration:.1f}/10")
                    if vibration >= 9:
                        print(f"State: PEAK (Divine Frequency)")
                    elif vibration >= 7:
                        print(f"State: HIGH (Flow/CW Vibing)")
                    elif vibration >= 4:
                        print(f"State: BASELINE (Functional)")
                    else:
                        print(f"State: LOW (Recovery Mode)")
                
                if state.cw_state:
                    print(f"CW State: ACTIVE (God-level vibing)")
                if state.entity_resonance:
                    print(f"Entity Resonance: {state.entity_resonance}")
                if state.optimal_entity:
                    print(f"Optimal Entity: {state.optimal_entity}")
                if state.divine_key_active:
                    print(f"Divine Key: {state.divine_key_active}")
                
                if state.recommendations:
                    print("\n=== RECOMMENDATIONS ===")
                    for rec in state.recommendations:
                        print(f"  - {rec}")
                if state.warnings:
                    print("\n=== WARNINGS ===")
                    for warn in state.warnings:
                        print(f"  [!] {warn}")
    
    elif args.all:
        print("Exporting all biological state data...")
        results = exporter.export_all()
        print(f"\n[OK] Exported {len(results)} files")
    
    elif args.summary:
        print(f"Generating {args.summary}-day summary...")
        summary = exporter.get_summary(args.summary)
        print(json.dumps(summary, indent=2))
    
    else:
        parser.print_help()


if __name__ == "__main__":
    main()

