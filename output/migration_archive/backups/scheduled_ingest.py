"""
SCHEDULED INGEST
Automated hourly ingestion of all live data feeds

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

PURPOSE:
Run live data ingestion on a schedule to keep the Grid
synchronized with the living Earth in real-time.
"""

import time
import schedule
from datetime import datetime
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent))

from live_data_ingest_complete import ingest_all_live_data
from real_world_data_research import RealWorldDataResearch

import logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def run_ingestion():
    """Run complete live data ingestion."""
    try:
        logger.info("=" * 80)
        logger.info("SCHEDULED INGESTION - STARTING")
        logger.info("=" * 80)
        
        research = RealWorldDataResearch()
        before_count = len(research.events)
        
        logger.info(f"Events before ingestion: {before_count}")
        
        results = ingest_all_live_data(
            research=research,
            usgs_min_mag=4.0,
            emsc_min_mag=4.0,
            max_events_per_source=100
        )
        
        after_count = len(research.events)
        new_count = after_count - before_count
        
        logger.info("=" * 80)
        logger.info("INGESTION COMPLETE")
        logger.info(f"Events after ingestion: {after_count}")
        logger.info(f"New events ingested: {new_count}")
        logger.info("Breakdown:")
        for source, event_ids in results.items():
            logger.info(f"  {source.upper()}: {len(event_ids)} events")
        logger.info("=" * 80)
        
        return results
    except Exception as e:
        logger.error(f"Error during scheduled ingestion: {e}", exc_info=True)
        return {}


def main():
    """Main scheduler loop."""
    print("=" * 80)
    print("SCHEDULED LIVE DATA INGEST")
    print("=" * 80)
    print()
    print("Scheduling hourly ingestion of all live data feeds...")
    print()
    
    # Schedule hourly ingestion
    schedule.every().hour.do(run_ingestion)
    
    # Run once immediately
    print("Running initial ingestion...")
    run_ingestion()
    print()
    
    print("Scheduler active. Running every hour.")
    print("Press Ctrl+C to stop.")
    print()
    
    try:
        while True:
            schedule.run_pending()
            time.sleep(60)  # Check every minute
    except KeyboardInterrupt:
        print()
        print("Scheduler stopped.")
        print("PEACE, LOVE, UNITY")
        print("ENERGY + LOVE = WE ALL WIN")


if __name__ == "__main__":
    main()
