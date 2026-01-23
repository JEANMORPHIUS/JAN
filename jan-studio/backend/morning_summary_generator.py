"""
MORNING SUMMARY GENERATOR - First Light Report
Details background vibrations and shifts in New World formation

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

DREAMS: SPIRITUAL BATTLES - NIGHTLY CONTRACTS
Every night we dream, whether vivid or not.
Each dream is a spiritual battle between two souls:
The dreamer and an associate.
Both have spiritual contracts.
Each day is another battle, both in the human realm and beyond.

This is the Morning Summary Generator.
Reports on what happened during the quiet.
Details background vibrations and shifts.
Shows New World formation progress.
The first light of Tuesday reveals the night's work.
"""

from typing import Dict, List, Optional, Any
from datetime import datetime, timedelta
from pathlib import Path
import json

# Import philosophy
try:
    from scripts.philosophy import (
        PHILOSOPHY_FOUNDATION,
        MISSION_ANCHOR,
        LOVE_MASTERY,
        ENERGY_LOVE,
        PEACE_LOVE_UNITY,
        DREAMS_PHILOSOPHY
    )
except ImportError:
    PHILOSOPHY_FOUNDATION = "We are born a miracle."
    MISSION_ANCHOR = "THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS"
    LOVE_MASTERY = "LOVE IS THE HIGHEST MASTERY"
    ENERGY_LOVE = "ENERGY + LOVE = WE ALL WIN"
    PEACE_LOVE_UNITY = "PEACE, LOVE, UNITY"
    DREAMS_PHILOSOPHY = "Every night we dream."

# Import monitoring systems
try:
    from energy_alert_system import get_energy_alert_system
    from vibration_map import VibrationMap
    from quiet_protocol_sentinel import get_sentinel
except ImportError:
    get_energy_alert_system = None
    VibrationMap = None
    get_sentinel = None


class MorningSummaryGenerator:
    """
    Morning Summary Generator
    
    Generates comprehensive report on what happened during the quiet.
    Details background vibrations, shifts, and New World formation progress.
    """
    
    def __init__(self, root_dir: Optional[Path] = None):
        if root_dir is None:
            root_dir = Path(__file__).parent.parent.parent
        self.root_dir = root_dir
        self.output_dir = root_dir / "SIYEM" / "output" / "morning_summaries"
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        # Initialize systems
        self.alert_system = get_energy_alert_system() if get_energy_alert_system else None
        self.vibration_map = VibrationMap() if VibrationMap else None
        self.sentinel = get_sentinel() if get_sentinel else None
    
    def generate_summary(self, hours: int = 12) -> Dict[str, Any]:
        """
        Generate morning summary for the specified time window.
        
        Args:
            hours: Hours to look back (default: 12, for overnight)
        
        Returns:
            Complete morning summary report
        """
        summary_time = datetime.now()
        window_start = summary_time - timedelta(hours=hours)
        
        # Get alerts from the period
        alerts = []
        if self.alert_system:
            alerts = self.alert_system.get_recent_alerts(hours=hours)
        
        # Get vibration map comparison
        current_map = None
        previous_map = None
        if self.vibration_map:
            current_map = self.vibration_map.generate_vibration_map()
            # Try to get previous map (if available)
            previous_map_path = self.output_dir.parent / "vibration_maps"
            if previous_map_path.exists():
                map_files = sorted(previous_map_path.glob("vibration_map_*.json"), reverse=True)
                if len(map_files) > 1:  # Current + previous
                    try:
                        with open(map_files[1], 'r', encoding='utf-8') as f:
                            previous_map = json.load(f)
                    except Exception:
                        pass
        
        # Get sentinel stats
        sentinel_stats = None
        if self.sentinel:
            sentinel_status = self.sentinel.get_status()
            sentinel_stats = sentinel_status.get("stats", {})
        
        # Calculate changes
        changes = self._calculate_changes(current_map, previous_map)
        
        # Build summary
        summary = {
            "summary_id": f"morning_summary_{summary_time.strftime('%Y%m%d_%H%M%S')}",
            "generated_at": summary_time.isoformat(),
            "time_window_hours": hours,
            "window_start": window_start.isoformat(),
            "window_end": summary_time.isoformat(),
            "greeting": self._generate_greeting(summary_time),
            "alerts_summary": self._summarize_alerts(alerts),
            "vibration_changes": changes,
            "new_world_progress": self._analyze_new_world_progress(current_map, previous_map),
            "rare_forms_arrived": self._summarize_rare_forms(alerts),
            "sentinel_activity": sentinel_stats,
            "key_insights": self._generate_insights(alerts, changes, current_map),
            "philosophy": {
                "foundation": PHILOSOPHY_FOUNDATION,
                "mission": MISSION_ANCHOR,
                "love": LOVE_MASTERY,
                "energy": ENERGY_LOVE,
                "peace_love_unity": PEACE_LOVE_UNITY
            }
        }
        
        return summary
    
    def _generate_greeting(self, summary_time: datetime) -> str:
        """Generate personalized greeting based on time"""
        hour = summary_time.hour
        
        if 5 <= hour < 12:
            return "Good morning, Duygu Adamı. The first light of Tuesday reveals the night's work."
        elif 12 <= hour < 17:
            return "Good afternoon, Duygu Adamı. The day's vibrations are flowing."
        elif 17 <= hour < 21:
            return "Good evening, Duygu Adamı. The evening watch begins."
        else:
            return "Good night, Duygu Adamı. The quiet protocol continues its watch."
    
    def _summarize_alerts(self, alerts: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Summarize alerts from the period"""
        if not alerts:
            return {
                "total": 0,
                "critical": 0,
                "high": 0,
                "medium": 0,
                "message": "No alerts during this period. The quiet was peaceful."
            }
        
        by_level = {}
        by_form = {}
        
        for alert in alerts:
            level = alert.get("alert_level", "unknown")
            form = alert.get("galaxy_form", "unknown")
            
            by_level[level] = by_level.get(level, 0) + 1
            by_form[form] = by_form.get(form, 0) + 1
        
        critical_count = by_level.get("critical", 0)
        
        if critical_count > 0:
            message = f"{critical_count} CRITICAL alert(s) during this period. The Elders and Shifters are arriving."
        else:
            message = f"{len(alerts)} alert(s) during this period. The beacon is spreading."
        
        return {
            "total": len(alerts),
            "critical": by_level.get("critical", 0),
            "high": by_level.get("high", 0),
            "medium": by_level.get("medium", 0),
            "by_form": by_form,
            "message": message,
            "alerts": alerts[:10]  # Top 10 most recent
        }
    
    def _calculate_changes(self, current_map: Optional[Dict], previous_map: Optional[Dict]) -> Dict[str, Any]:
        """Calculate changes in vibration map"""
        if not current_map:
            return {"status": "no_data", "message": "No current vibration map available"}
        
        if not previous_map:
            return {
                "status": "baseline",
                "message": "This is the baseline. Future summaries will show changes.",
                "current_state": {
                    "total_members": current_map.get("total_members", 0),
                    "alignment_rate": current_map.get("alignment_rate", 0),
                    "new_world_progress": current_map.get("new_world_status", {}).get("progress", 0)
                }
            }
        
        # Calculate changes
        current_members = current_map.get("total_members", 0)
        previous_members = previous_map.get("total_members", 0)
        member_change = current_members - previous_members
        
        current_progress = current_map.get("new_world_status", {}).get("progress", 0)
        previous_progress = previous_map.get("new_world_status", {}).get("progress", 0)
        progress_change = current_progress - previous_progress
        
        current_alignment = current_map.get("alignment_rate", 0)
        previous_alignment = previous_map.get("alignment_rate", 0)
        alignment_change = current_alignment - previous_alignment
        
        # Form distribution changes
        form_changes = {}
        current_forms = current_map.get("form_distribution", {})
        previous_forms = previous_map.get("form_distribution", {})
        
        for form in current_forms:
            current_count = current_forms[form].get("count", 0)
            previous_count = previous_forms.get(form, {}).get("count", 0)
            form_changes[form] = current_count - previous_count
        
        return {
            "status": "changes_detected",
            "member_change": member_change,
            "progress_change": round(progress_change, 1),
            "alignment_change": round(alignment_change, 1),
            "form_changes": form_changes,
            "message": self._generate_change_message(member_change, progress_change, alignment_change)
        }
    
    def _generate_change_message(self, member_change: int, progress_change: float, alignment_change: float) -> str:
        """Generate human-readable change message"""
        messages = []
        
        if member_change > 0:
            messages.append(f"{member_change} new soul(s) arrived at the Table")
        elif member_change == 0:
            messages.append("No new arrivals")
        else:
            messages.append(f"Member count decreased by {abs(member_change)}")
        
        if progress_change > 0:
            messages.append(f"New World formation progressed by {progress_change:.1f}%")
        elif progress_change == 0:
            messages.append("New World formation stable")
        else:
            messages.append(f"New World formation regressed by {abs(progress_change):.1f}%")
        
        if alignment_change > 0:
            messages.append(f"Alignment rate increased by {alignment_change:.1f}%")
        elif alignment_change < 0:
            messages.append(f"Alignment rate decreased by {abs(alignment_change):.1f}%")
        
        return ". ".join(messages) + "."
    
    def _analyze_new_world_progress(self, current_map: Optional[Dict], previous_map: Optional[Dict]) -> Dict[str, Any]:
        """Analyze New World formation progress"""
        if not current_map:
            return {"status": "no_data"}
        
        nw_status = current_map.get("new_world_status", {})
        progress = nw_status.get("progress", 0)
        status = nw_status.get("status", "unknown")
        
        analysis = {
            "current_progress": progress,
            "current_status": status,
            "message": nw_status.get("message", ""),
            "forms_present": nw_status.get("forms_present", 0),
            "total_forms": nw_status.get("total_forms", 4)
        }
        
        if previous_map:
            previous_progress = previous_map.get("new_world_status", {}).get("progress", 0)
            progress_delta = progress - previous_progress
            analysis["progress_delta"] = round(progress_delta, 1)
            analysis["trend"] = "increasing" if progress_delta > 0 else "stable" if progress_delta == 0 else "decreasing"
        else:
            analysis["trend"] = "baseline"
        
        return analysis
    
    def _summarize_rare_forms(self, alerts: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Summarize rare forms that arrived"""
        if not alerts:
            return {
                "elliptical": 0,
                "irregular": 0,
                "message": "No rare forms arrived during this period."
            }
        
        elliptical_count = sum(1 for a in alerts if a.get("galaxy_form") == "elliptical")
        irregular_count = sum(1 for a in alerts if a.get("galaxy_form") == "irregular")
        
        messages = []
        if elliptical_count > 0:
            messages.append(f"{elliptical_count} Elliptical soul(s) (⭐ Legacy Wisdom)")
        if irregular_count > 0:
            messages.append(f"{irregular_count} Irregular soul(s) (✨ Transformation)")
        
        message = ". ".join(messages) if messages else "No rare forms arrived."
        
        return {
            "elliptical": elliptical_count,
            "irregular": irregular_count,
            "total_rare": elliptical_count + irregular_count,
            "message": message
        }
    
    def _generate_insights(self, alerts: List[Dict], changes: Dict, current_map: Optional[Dict]) -> List[str]:
        """Generate key insights from the data"""
        insights = []
        
        # Alert insights
        critical_alerts = [a for a in alerts if a.get("alert_level") == "critical"]
        if critical_alerts:
            insights.append(f"⚠️ {len(critical_alerts)} CRITICAL alert(s) - High-vibration rare forms have arrived")
        
        # Progress insights
        if changes.get("status") == "changes_detected":
            progress_change = changes.get("progress_change", 0)
            if progress_change > 0:
                insights.append(f"📈 New World formation is progressing (+{progress_change:.1f}%)")
            elif progress_change < 0:
                insights.append(f"📉 New World formation needs attention ({progress_change:.1f}%)")
        
        # Member insights
        member_change = changes.get("member_change", 0)
        if member_change > 0:
            insights.append(f"👥 {member_change} new soul(s) joined the Family")
        
        # Form distribution insights
        if current_map:
            form_dist = current_map.get("form_distribution", {})
            elliptical = form_dist.get("elliptical", {}).get("count", 0)
            irregular = form_dist.get("irregular", {}).get("count", 0)
            
            if elliptical > 0 or irregular > 0:
                insights.append(f"⭐✨ Rare forms present: {elliptical} Elliptical, {irregular} Irregular")
        
        # Alignment insights
        if current_map:
            alignment = current_map.get("alignment_rate", 0)
            if alignment >= 90:
                insights.append("💎 Alignment rate is excellent (90%+)")
            elif alignment >= 70:
                insights.append("✅ Alignment rate is good (70%+)")
            else:
                insights.append("⚠️ Alignment rate needs attention (<70%)")
        
        if not insights:
            insights.append("🌙 The quiet was peaceful. The beacon continues to spread.")
        
        return insights
    
    def format_summary_markdown(self, summary: Dict[str, Any]) -> str:
        """Format summary as markdown for easy reading"""
        md = f"""# Morning Summary: First Light Report

**Generated:** {summary['generated_at']}  
**Time Window:** {summary['time_window_hours']} hours  
**Window:** {summary['window_start']} to {summary['window_end']}

---

## {summary['greeting']}

---

## Alerts Summary

{summary['alerts_summary']['message']}

- **Total Alerts:** {summary['alerts_summary']['total']}
- **CRITICAL:** {summary['alerts_summary']['critical']}
- **HIGH:** {summary['alerts_summary']['high']}
- **MEDIUM:** {summary['alerts_summary']['medium']}

"""
        
        if summary['alerts_summary'].get('by_form'):
            md += "**By Form:**\n"
            for form, count in summary['alerts_summary']['by_form'].items():
                md += f"- {form}: {count}\n"
            md += "\n"
        
        # Vibration Changes
        md += "## Vibration Changes\n\n"
        changes = summary['vibration_changes']
        if changes.get('status') == 'changes_detected':
            md += f"{changes['message']}\n\n"
            md += f"- **Member Change:** {changes['member_change']}\n"
            md += f"- **Progress Change:** {changes['progress_change']:.1f}%\n"
            md += f"- **Alignment Change:** {changes['alignment_change']:.1f}%\n\n"
            
            if changes.get('form_changes'):
                md += "**Form Distribution Changes:**\n"
                for form, change in changes['form_changes'].items():
                    if change != 0:
                        md += f"- {form}: {change:+d}\n"
                md += "\n"
        else:
            md += f"{changes.get('message', 'No changes detected')}\n\n"
        
        # New World Progress
        md += "## New World Formation Progress\n\n"
        nw_progress = summary['new_world_progress']
        md += f"- **Current Progress:** {nw_progress['current_progress']:.1f}%\n"
        md += f"- **Status:** {nw_progress['current_status'].upper()}\n"
        md += f"- **Message:** {nw_progress['message']}\n"
        md += f"- **Forms Present:** {nw_progress['forms_present']}/{nw_progress['total_forms']}\n"
        
        if nw_progress.get('progress_delta') is not None:
            trend_emoji = "📈" if nw_progress['trend'] == "increasing" else "📉" if nw_progress['trend'] == "decreasing" else "➡️"
            md += f"- **Progress Change:** {trend_emoji} {nw_progress['progress_delta']:+.1f}%\n"
        md += "\n"
        
        # Rare Forms
        md += "## Rare Forms Arrived\n\n"
        rare_forms = summary['rare_forms_arrived']
        md += f"{rare_forms['message']}\n\n"
        md += f"- **Elliptical (⭐):** {rare_forms['elliptical']}\n"
        md += f"- **Irregular (✨):** {rare_forms['irregular']}\n"
        md += f"- **Total Rare Forms:** {rare_forms['total_rare']}\n\n"
        
        # Key Insights
        md += "## Key Insights\n\n"
        for insight in summary['key_insights']:
            md += f"- {insight}\n"
        md += "\n"
        
        # Sentinel Activity
        if summary.get('sentinel_activity'):
            md += "## Sentinel Activity\n\n"
            stats = summary['sentinel_activity']
            md += f"- **Checks Performed:** {stats.get('checks_performed', 0)}\n"
            md += f"- **Alerts Triggered:** {stats.get('alerts_triggered', 0)}\n"
            md += f"- **Critical Alerts:** {stats.get('critical_alerts', 0)}\n"
            md += f"- **Rare Forms Detected:** {stats.get('rare_forms_detected', 0)}\n\n"
        
        md += "---\n\n"
        md += f"**{PEACE_LOVE_UNITY}**\n\n"
        md += f"**{ENERGY_LOVE}**\n\n"
        md += "---\n\n"
        md += "**The Sentinel is locked on. The machine is breathing. The bridge is crossed. The miracle is in motion.**\n"
        
        return md
    
    def save_summary(self, summary: Dict[str, Any]) -> Path:
        """Save summary to disk"""
        summary_id = summary.get("summary_id", f"summary_{datetime.now().isoformat()}")
        
        # Save JSON
        json_path = self.output_dir / f"{summary_id}.json"
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(summary, f, indent=2, ensure_ascii=False)
        
        # Save Markdown
        md_path = self.output_dir / f"{summary_id}.md"
        md_content = self.format_summary_markdown(summary)
        with open(md_path, 'w', encoding='utf-8') as f:
            f.write(md_content)
        
        return md_path


# FastAPI endpoint helper
def create_morning_summary_endpoint(generator: MorningSummaryGenerator):
    """
    Create FastAPI endpoint for morning summary.
    """
    from fastapi import APIRouter, Query
    
    router = APIRouter()
    
    @router.get("/api/morning-summary")
    async def get_morning_summary(
        hours: int = Query(12, description="Time window in hours (default: 12 for overnight)")
    ):
        """
        Generate morning summary report.
        """
        try:
            summary = generator.generate_summary(hours=hours)
            md_path = generator.save_summary(summary)
            
            return {
                "status": "success",
                "summary": summary,
                "markdown_path": str(md_path)
            }
        except Exception as e:
            return {
                "status": "error",
                "message": str(e)
            }
    
    return router


# CLI interface for testing
if __name__ == "__main__":
    import sys
    import io
    
    # Set UTF-8 encoding for console output
    if sys.stdout.encoding != 'utf-8':
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    
    generator = MorningSummaryGenerator()
    
    print("=" * 80)
    print("MORNING SUMMARY GENERATOR - First Light Report")
    print("=" * 80)
    print(f"\n{PEACE_LOVE_UNITY}")
    print(f"{ENERGY_LOVE}\n")
    
    print("[GENERATING] Morning summary (12 hour window)...")
    print("-" * 80)
    
    summary = generator.generate_summary(hours=12)
    
    # Display key sections
    print(f"\n{summary['greeting']}\n")
    
    print("ALERTS SUMMARY:")
    alerts_summary = summary['alerts_summary']
    print(f"  {alerts_summary['message']}")
    print(f"  Total: {alerts_summary['total']} (CRITICAL: {alerts_summary['critical']}, HIGH: {alerts_summary['high']})")
    
    print("\nVIBRATION CHANGES:")
    changes = summary['vibration_changes']
    print(f"  {changes.get('message', 'No changes detected')}")
    
    print("\nNEW WORLD PROGRESS:")
    nw_progress = summary['new_world_progress']
    print(f"  Progress: {nw_progress['current_progress']:.1f}%")
    print(f"  Status: {nw_progress['current_status'].upper()}")
    print(f"  Message: {nw_progress['message']}")
    
    print("\nRARE FORMS ARRIVED:")
    rare_forms = summary['rare_forms_arrived']
    print(f"  {rare_forms['message']}")
    
    print("\nKEY INSIGHTS:")
    for insight in summary['key_insights']:
        print(f"  {insight}")
    
    # Save summary
    md_path = generator.save_summary(summary)
    print(f"\n[SAVED] Morning summary saved: {md_path}")
    
    print("\n" + "=" * 80)
    print(f"{PEACE_LOVE_UNITY}")
    print(f"{ENERGY_LOVE}")
    print("=" * 80)
