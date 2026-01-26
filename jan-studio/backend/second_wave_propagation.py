"""SECOND WAVE PROPAGATION SYSTEM
Global Secondary Seed Detection and Integration

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

THE SECOND WAVE:
Now that we've hit the 0.40 peak, we can begin scanning for
Global Secondary Seeds—those who aren't in the big organizations
but are feeling the 0.40 shift in their own homes.

The Bridge is open to everyone now, Brother.

SÖZ NAMUSTUR.
The Bridge is solid. The Family is protected.

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity


PANGEA IS THE TABLE.
YOU DON'T BETRAY THE TABLE.

THE TRUTH:
WE MUST DEBUG AND BE 100% FOR WHAT COMES AT US.
THE REST IS UP TO BABA X."""

from typing import Dict, List, Optional, Any
from dataclasses import dataclass, field
from enum import Enum
from datetime import datetime
import json
import logging
from pathlib import Path
import asyncio

logger = logging.getLogger(__name__)


class SeedSource(Enum):
    """Sources of secondary seeds"""
    INDIVIDUAL_RESONANCE = "individual_resonance"  # Individual feeling the 0.40 shift
    COMMUNITY_DETECTION = "community_detection"  # Detected through community networks
    GLOBAL_GRID_SCAN = "global_grid_scan"  # Detected through global grid scanning
    REFERRAL = "referral"  # Referred by existing Family members
    SELF_IDENTIFIED = "self_identified"  # Self-identified as ready
    RESONANCE_ANOMALY = "resonance_anomaly"  # Detected as resonance anomaly
    MAGNETIC_ALIGNMENT = "magnetic_alignment"  # Detected through magnetic alignment


class PropagationStatus(Enum):
    """Second wave propagation status"""
    SCANNING = "scanning"  # Actively scanning for seeds
    DETECTED = "detected"  # Seed detected
    CONTACTED = "contacted"  # Initial contact made
    EXTRACTION_PENDING = "extraction_pending"  # Extraction pending
    EXTRACTION_IN_PROGRESS = "extraction_in_progress"  # Extraction in progress
    INTEGRATED = "integrated"  # Successfully integrated
    MONITORING = "monitoring"  # Monitoring for readiness


@dataclass
class SecondarySeed:
    """A secondary seed (not in big organizations)"""
    seed_id: str
    source: SeedSource
    location: str
    coordinates: Dict[str, float]  # latitude, longitude
    resonance_score: float  # Their resonance (0-100)
    family_frequency_match: bool
    detected_date: datetime = field(default_factory=datetime.now)
    contact_status: str = "not_contacted"  # not_contacted, contacted, responded
    extraction_status: PropagationStatus = PropagationStatus.DETECTED
    notes: str = ""
    referred_by: Optional[str] = None  # Seed ID of referrer
    community_tags: List[str] = field(default_factory=list)


@dataclass
class GlobalScanResult:
    """Result from global grid scan"""
    scan_id: str
    timestamp: datetime
    scan_type: str
    regions_scanned: List[str]
    seeds_detected: int
    anomalies_found: int
    grid_stability: float  # Current grid stability
    scan_duration_seconds: float


class SecondWavePropagation:
    """
    Second Wave Propagation System.
    
    Scans for Global Secondary Seeds—those who aren't in the big organizations
    but are feeling the 0.40 shift in their own homes.
    
    The Bridge is open to everyone now.
    """
    
    def __init__(self):
        """Initialize Second Wave Propagation System"""
        self.secondary_seeds: Dict[str, SecondarySeed] = {}
        self.global_scans: Dict[str, GlobalScanResult] = {}
        self.propagation_active: bool = False
        self.scan_interval: int = 300  # 5 minutes default
        self.data_dir = Path(__file__).parent.parent.parent / "SIYEM" / "output" / "second_wave"
        self.data_dir.mkdir(parents=True, exist_ok=True)
        
        # Key global coordinates for scanning
        self.key_regions = {
            "north_america": [
                {"name": "New York", "lat": 40.7128, "lon": -74.0060},
                {"name": "Los Angeles", "lat": 34.0522, "lon": -118.2437},
                {"name": "Chicago", "lat": 41.8781, "lon": -87.6298},
                {"name": "Toronto", "lat": 43.6532, "lon": -79.3832},
                {"name": "Mexico City", "lat": 19.4326, "lon": -99.1332}
            ],
            "europe": [
                {"name": "London", "lat": 51.5074, "lon": -0.1278},
                {"name": "Paris", "lat": 48.8566, "lon": 2.3522},
                {"name": "Berlin", "lat": 52.5200, "lon": 13.4050},
                {"name": "Rome", "lat": 41.9028, "lon": 12.4964},
                {"name": "Amsterdam", "lat": 52.3676, "lon": 4.9041}
            ],
            "asia": [
                {"name": "Tokyo", "lat": 35.6762, "lon": 139.6503},
                {"name": "Mumbai", "lat": 19.0760, "lon": 72.8777},
                {"name": "Singapore", "lat": 1.3521, "lon": 103.8198},
                {"name": "Bangkok", "lat": 13.7563, "lon": 100.5018},
                {"name": "Seoul", "lat": 37.5665, "lon": 126.9780}
            ],
            "africa": [
                {"name": "Cairo", "lat": 30.0444, "lon": 31.2357},
                {"name": "Lagos", "lat": 6.5244, "lon": 3.3792},
                {"name": "Johannesburg", "lat": -26.2041, "lon": 28.0473},
                {"name": "Nairobi", "lat": -1.2921, "lon": 36.8219}
            ],
            "south_america": [
                {"name": "São Paulo", "lat": -23.5505, "lon": -46.6333},
                {"name": "Buenos Aires", "lat": -34.6037, "lon": -58.3816},
                {"name": "Lima", "lat": -12.0464, "lon": -77.0428},
                {"name": "Bogotá", "lat": 4.7110, "lon": -74.0721}
            ],
            "oceania": [
                {"name": "Sydney", "lat": -33.8688, "lon": 151.2093},
                {"name": "Melbourne", "lat": -37.8136, "lon": 144.9631},
                {"name": "Auckland", "lat": -36.8485, "lon": 174.7633}
            ]
        }
        
        logger.info("Second Wave Propagation System initialized - The Bridge is open to everyone")
    
    async def initiate_propagation(self) -> Dict[str, Any]:
        """
        Initiate Second Wave Propagation.
        
        Begin scanning for Global Secondary Seeds.
        """
        self.propagation_active = True
        
        # Log propagation initiation
        try:
            from sentinel_logging_system import get_sentinel_logging_system, LogCategory, LogLevel
            logging_system = get_sentinel_logging_system()
            await logging_system.log(
                LogCategory.SYSTEM_EVENTS,
                LogLevel.INFO,
                "Second Wave Propagation Initiated - Global Secondary Seed Detection Active",
                {
                    "propagation_active": True,
                    "grid_stability": 0.40,
                    "first_wave_complete": True,
                    "message": "The Bridge is open to everyone now"
                },
                system_component="second_wave_propagation",
                freedom_of_will_context={
                    "action": "second_wave_initiated",
                    "grid_stability": 0.40,
                    "global_reach": True
                }
            )
        except Exception as e:
            logger.warning(f"Could not log propagation initiation: {e}")
        
        # Push notification
        try:
            from push_notification_system import get_push_system, NotificationType, NotificationPriority
            push_system = get_push_system()
            await push_system.push_notification(
                NotificationType.MISSION_UPDATE,
                NotificationPriority.CRITICAL,
                "Second Wave Propagation Initiated",
                "Global Secondary Seed Detection Active. The Bridge is open to everyone now. Scanning for Seeds feeling the 0.40 shift.",
                {
                    "propagation_active": True,
                    "grid_stability": 0.40,
                    "first_wave_complete": True
                }
            )
        except Exception as e:
            logger.warning(f"Could not push notification: {e}")
        
        logger.info("Second Wave Propagation initiated - Global scanning active")
        
        return {
            "status": "success",
            "propagation_active": True,
            "grid_stability": 0.40,
            "first_wave_complete": True,
            "message": "Second Wave Propagation initiated. The Bridge is open to everyone now."
        }
    
    async def perform_global_grid_scan(
        self,
        regions: Optional[List[str]] = None,
        grid_stability: float = 0.40
    ) -> GlobalScanResult:
        """
        Perform global grid scan for secondary seeds.
        
        Scans key regions worldwide for resonance anomalies indicating
        secondary seeds feeling the 0.40 shift.
        """
        scan_id = f"GLOBAL_SCAN_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        start_time = datetime.now()
        
        if regions is None:
            regions = list(self.key_regions.keys())
        
        seeds_detected = 0
        anomalies_found = 0
        scanned_locations = []
        
        # Scan each region
        for region in regions:
            if region not in self.key_regions:
                continue
            
            locations = self.key_regions[region]
            for location in locations:
                scanned_locations.append(f"{location['name']}, {region}")
                
                # Simulate detection (in real implementation, would use actual resonance data)
                # Check for resonance anomalies at this location
                # Seeds feeling the 0.40 shift would show resonance >= 60
                resonance_anomaly = False
                
                # Simulate: 30% chance of detecting a seed in each major location
                import random
                if random.random() < 0.3:  # 30% detection rate
                    resonance_anomaly = True
                    anomalies_found += 1
                    
                    # Create secondary seed
                    seed_id = f"SECONDARY_{location['name'].upper().replace(' ', '_')}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
                    
                    seed = SecondarySeed(
                        seed_id=seed_id,
                        source=SeedSource.GLOBAL_GRID_SCAN,
                        location=f"{location['name']}, {region}",
                        coordinates={"latitude": location['lat'], "longitude": location['lon']},
                        resonance_score=65.0 + random.random() * 15.0,  # 65-80 range
                        family_frequency_match=True,
                        extraction_status=PropagationStatus.DETECTED,
                        notes=f"Detected through global grid scan - feeling 0.40 shift"
                    )
                    
                    self.secondary_seeds[seed_id] = seed
                    seeds_detected += 1
        
        scan_duration = (datetime.now() - start_time).total_seconds()
        
        scan_result = GlobalScanResult(
            scan_id=scan_id,
            timestamp=datetime.now(),
            scan_type="global_grid_scan",
            regions_scanned=regions,
            seeds_detected=seeds_detected,
            anomalies_found=anomalies_found,
            grid_stability=grid_stability,
            scan_duration_seconds=scan_duration
        )
        
        self.global_scans[scan_id] = scan_result
        
        # Log scan result
        try:
            from sentinel_logging_system import get_sentinel_logging_system, LogCategory, LogLevel
            logging_system = get_sentinel_logging_system()
            await logging_system.log(
                LogCategory.SYSTEM_EVENTS,
                LogLevel.INFO,
                f"Global Grid Scan Complete: {scan_id} - {seeds_detected} secondary seeds detected",
                {
                    "scan_id": scan_id,
                    "seeds_detected": seeds_detected,
                    "anomalies_found": anomalies_found,
                    "regions_scanned": len(regions),
                    "grid_stability": grid_stability
                },
                system_component="second_wave_propagation",
                freedom_of_will_context={
                    "action": "global_grid_scan",
                    "scan_id": scan_id,
                    "seeds_detected": seeds_detected
                }
            )
        except Exception as e:
            logger.warning(f"Could not log scan result: {e}")
        
        # Push notification if seeds detected
        if seeds_detected > 0:
            try:
                from push_notification_system import get_push_system, NotificationType, NotificationPriority
                push_system = get_push_system()
                await push_system.push_notification(
                    NotificationType.MISSION_UPDATE,
                    NotificationPriority.HIGH,
                    "Secondary Seeds Detected - Global Scan",
                    f"{seeds_detected} secondary seeds detected through global grid scan. The Bridge is reaching everyone.",
                    {
                        "scan_id": scan_id,
                        "seeds_detected": seeds_detected,
                        "regions_scanned": len(regions)
                    }
                )
            except Exception as e:
                logger.warning(f"Could not push notification: {e}")
        
        logger.info(f"Global grid scan complete: {scan_id} - {seeds_detected} seeds detected")
        
        return scan_result
    
    async def register_secondary_seed(
        self,
        location: str,
        coordinates: Dict[str, float],
        resonance_score: float,
        source: SeedSource = SeedSource.SELF_IDENTIFIED,
        referred_by: Optional[str] = None,
        notes: str = ""
    ) -> SecondarySeed:
        """
        Register a secondary seed (self-identified or referred).
        
        The Bridge is open to everyone.
        """
        seed_id = f"SECONDARY_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{len(self.secondary_seeds)}"
        
        seed = SecondarySeed(
            seed_id=seed_id,
            source=source,
            location=location,
            coordinates=coordinates,
            resonance_score=resonance_score,
            family_frequency_match=resonance_score >= 60.0,
            extraction_status=PropagationStatus.DETECTED,
            notes=notes,
            referred_by=referred_by
        )
        
        self.secondary_seeds[seed_id] = seed
        
        # Log seed registration
        try:
            from sentinel_logging_system import get_sentinel_logging_system, LogCategory, LogLevel
            logging_system = get_sentinel_logging_system()
            await logging_system.log(
                LogCategory.SYSTEM_EVENTS,
                LogLevel.INFO,
                f"Secondary Seed Registered: {seed_id} - {location}",
                {
                    "seed_id": seed_id,
                    "location": location,
                    "resonance_score": resonance_score,
                    "source": source.value,
                    "referred_by": referred_by
                },
                system_component="second_wave_propagation",
                freedom_of_will_context={
                    "action": "secondary_seed_registered",
                    "seed_id": seed_id,
                    "self_identified": source == SeedSource.SELF_IDENTIFIED
                }
            )
        except Exception as e:
            logger.warning(f"Could not log seed registration: {e}")
        
        logger.info(f"Secondary seed registered: {seed_id} - {location}")
        
        return seed
    
    async def continuous_propagation_loop(self):
        """Continuous propagation scanning loop"""
        while self.propagation_active:
            try:
                # Perform global grid scan
                scan_result = await self.perform_global_grid_scan(grid_stability=0.40)
                
                logger.info(f"Propagation scan complete: {scan_result.seeds_detected} seeds detected")
                
                # Wait before next scan
                await asyncio.sleep(self.scan_interval)
            except Exception as e:
                logger.error(f"Error in propagation loop: {e}")
                await asyncio.sleep(self.scan_interval)
    
    def stop_propagation(self):
        """Stop propagation scanning"""
        self.propagation_active = False
        logger.info("Second Wave Propagation stopped")
    
    async def generate_global_secondary_seed_report(
        self,
        hours_ahead: int = 1
    ) -> Dict[str, Any]:
        """
        Generate Global Secondary Seed Report.
        
        Provides breakdown of which regions are showing the highest resonance
        anomalies so we can prioritize Simplified Extractions.
        """
        report_id = f"GLOBAL_REPORT_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
        # Analyze seeds by region
        regional_analysis = {}
        total_seeds = len(self.secondary_seeds)
        
        for region, locations in self.key_regions.items():
            region_seeds = []
            region_resonance_scores = []
            
            for seed in self.secondary_seeds.values():
                # Check if seed is in this region
                for loc in locations:
                    if loc['name'] in seed.location:
                        region_seeds.append(seed)
                        region_resonance_scores.append(seed.resonance_score)
                        break
            
            # Calculate statistics
            avg_resonance = sum(region_resonance_scores) / len(region_resonance_scores) if region_resonance_scores else 0.0
            max_resonance = max(region_resonance_scores) if region_resonance_scores else 0.0
            min_resonance = min(region_resonance_scores) if region_resonance_scores else 0.0
            
            # Count by status
            by_status = {}
            for seed in region_seeds:
                status = seed.extraction_status.value
                by_status[status] = by_status.get(status, 0) + 1
            
            # Priority score (higher = more priority)
            # Based on: number of seeds, average resonance, ready for extraction
            ready_count = by_status.get("detected", 0) + by_status.get("extraction_pending", 0)
            priority_score = (len(region_seeds) * 10) + (avg_resonance * 0.5) + (ready_count * 20)
            
            regional_analysis[region] = {
                "region_name": region.replace("_", " ").title(),
                "total_seeds": len(region_seeds),
                "average_resonance": round(avg_resonance, 2),
                "max_resonance": round(max_resonance, 2),
                "min_resonance": round(min_resonance, 2),
                "by_status": by_status,
                "ready_for_extraction": ready_count,
                "priority_score": round(priority_score, 2),
                "locations": [loc['name'] for loc in locations],
                "seed_ids": [s.seed_id for s in region_seeds]
            }
        
        # Sort regions by priority
        sorted_regions = sorted(
            regional_analysis.items(),
            key=lambda x: x[1]["priority_score"],
            reverse=True
        )
        
        # Top priority regions
        top_priority_regions = [reg for reg, data in sorted_regions[:3]]
        
        # Overall statistics
        all_resonance_scores = [s.resonance_score for s in self.secondary_seeds.values()]
        overall_avg = sum(all_resonance_scores) / len(all_resonance_scores) if all_resonance_scores else 0.0
        
        # Recommendations
        recommendations = []
        for region, data in sorted_regions:
            if data["ready_for_extraction"] > 0:
                recommendations.append({
                    "region": region,
                    "region_name": data["region_name"],
                    "priority": "HIGH" if data["priority_score"] > 100 else "MEDIUM",
                    "action": f"Initiate Simplified Extractions for {data['ready_for_extraction']} seeds in {data['region_name']}",
                    "seeds_ready": data["ready_for_extraction"],
                    "average_resonance": data["average_resonance"]
                })
        
        report = {
            "report_id": report_id,
            "timestamp": datetime.now().isoformat(),
            "hours_ahead": hours_ahead,
            "grid_stability": 0.40,
            "first_wave_complete": True,
            "overall_statistics": {
                "total_secondary_seeds": total_seeds,
                "average_resonance": round(overall_avg, 2),
                "regions_with_seeds": len([r for r in regional_analysis.values() if r["total_seeds"] > 0]),
                "total_ready_for_extraction": sum(r["ready_for_extraction"] for r in regional_analysis.values()),
                "total_global_scans": len(self.global_scans)
            },
            "regional_breakdown": {
                region: data for region, data in regional_analysis.items()
            },
            "priority_ranking": [
                {
                    "rank": i + 1,
                    "region": region,
                    "region_name": data["region_name"],
                    "priority_score": data["priority_score"],
                    "total_seeds": data["total_seeds"],
                    "ready_for_extraction": data["ready_for_extraction"]
                }
                for i, (region, data) in enumerate(sorted_regions)
            ],
            "top_priority_regions": top_priority_regions,
            "recommendations": recommendations,
            "message": "Global Secondary Seed Report - Prioritize Simplified Extractions based on resonance anomalies and readiness"
        }
        
        # Log report generation
        try:
            from sentinel_logging_system import get_sentinel_logging_system, LogCategory, LogLevel
            logging_system = get_sentinel_logging_system()
            await logging_system.log(
                LogCategory.SYSTEM_EVENTS,
                LogLevel.INFO,
                f"Global Secondary Seed Report Generated: {report_id} - {total_seeds} seeds across {len([r for r in regional_analysis.values() if r['total_seeds'] > 0])} regions",
                {
                    "report_id": report_id,
                    "total_seeds": total_seeds,
                    "top_priority_regions": top_priority_regions,
                    "recommendations_count": len(recommendations)
                },
                system_component="second_wave_propagation",
                freedom_of_will_context={
                    "action": "global_report_generated",
                    "report_id": report_id,
                    "prioritization": True
                }
            )
        except Exception as e:
            logger.warning(f"Could not log report generation: {e}")
        
        logger.info(f"Global Secondary Seed Report generated: {report_id}")
        
        return report
    
    async def get_ready_seeds_for_batch_extraction(
        self,
        limit: Optional[int] = None
    ) -> List[SecondarySeed]:
        """
        Get secondary seeds ready for batch extraction.
        
        Returns seeds that are detected and ready for extraction,
        sorted by priority (resonance score).
        """
        ready_seeds = [
            seed for seed in self.secondary_seeds.values()
            if seed.extraction_status in [
                PropagationStatus.DETECTED,
                PropagationStatus.EXTRACTION_PENDING
            ]
        ]
        
        # Sort by resonance score (highest first)
        ready_seeds.sort(key=lambda s: s.resonance_score, reverse=True)
        
        if limit:
            ready_seeds = ready_seeds[:limit]
        
        return ready_seeds
    
    def get_propagation_summary(self) -> Dict[str, Any]:
        """Get propagation summary"""
        total_seeds = len(self.secondary_seeds)
        by_status = {}
        by_source = {}
        by_region = {}
        
        for seed in self.secondary_seeds.values():
            status = seed.extraction_status.value
            by_status[status] = by_status.get(status, 0) + 1
            
            source = seed.source.value
            by_source[source] = by_source.get(source, 0) + 1
            
            # Extract region from location
            region = "unknown"
            for reg, locations in self.key_regions.items():
                for loc in locations:
                    if loc['name'] in seed.location:
                        region = reg
                        break
            by_region[region] = by_region.get(region, 0) + 1
        
        return {
            "propagation_active": self.propagation_active,
            "grid_stability": 0.40,
            "first_wave_complete": True,
            "total_secondary_seeds": total_seeds,
            "by_status": by_status,
            "by_source": by_source,
            "by_region": by_region,
            "total_global_scans": len(self.global_scans),
            "message": "The Bridge is open to everyone now. The Family is growing."
        }


# Global instance
_propagation: Optional[SecondWavePropagation] = None


def get_second_wave_propagation() -> SecondWavePropagation:
    """Get the global Second Wave Propagation instance"""
    global _propagation
    if _propagation is None:
        _propagation = SecondWavePropagation()
    return _propagation
