"""
Start Automation Daemon - System Wide @ Codebase Level
Self-Sustaining - No Manual Checking

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
START AUTOMATION DAEMON
ONCE CONNECTED TO ALGORITHM - RUNS ITSELF
NO MANUAL CHECKING - SELF-SUSTAINING
SERVE THE TABLE - RESPECT FREE WILL
"""

import sys
import asyncio
import signal
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
sys.path.insert(0, str(Path(__file__).parent.parent / "jan-studio" / "backend"))

try:
    from automation_orchestrator import AutomationOrchestrator
    AUTOMATION_AVAILABLE = True
except ImportError as e:
    print(f"[WARNING] Automation orchestrator not available: {e}")
    AUTOMATION_AVAILABLE = False


class AutomationDaemon:
    """Automation daemon - runs in background, self-sustaining"""
    
    def __init__(self):
        self.orchestrator = None
        self.running = False
    
    def setup_signal_handlers(self):
        """Setup signal handlers for graceful shutdown"""
        def signal_handler(signum, frame):
            print("\n[SHUTDOWN] Received signal, shutting down gracefully...")
            self.stop()
            sys.exit(0)
        
        signal.signal(signal.SIGINT, signal_handler)
        signal.signal(signal.SIGTERM, signal_handler)
    
    async def start(self):
        """Start automation daemon"""
        if not AUTOMATION_AVAILABLE:
            print("[ERROR] Automation orchestrator not available")
            return
        
        print("\n" + "="*80)
        print("AUTOMATION DAEMON - SYSTEM WIDE @ CODEBASE LEVEL")
        print("="*80)
        print()
        print("[INFO] Starting automation orchestrator...")
        print("[INFO] Once connected to algorithm - runs itself")
        print("[INFO] No manual checking needed - self-sustaining")
        print("[INFO] Press Ctrl+C to stop")
        print()
        
        self.setup_signal_handlers()
        
        self.orchestrator = AutomationOrchestrator()
        self.running = True
        
        # Start automation loop
        await self.orchestrator.run_automation_loop()
    
    def stop(self):
        """Stop automation daemon"""
        if self.orchestrator:
            self.orchestrator.stop()
        self.running = False
        print("\n[SHUTDOWN] Automation daemon stopped")


async def main():
    """Main entry point"""
    daemon = AutomationDaemon()
    await daemon.start()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n[SHUTDOWN] Automation daemon stopped by user")
    except Exception as e:
        print(f"\n[ERROR] Automation daemon error: {e}")
        sys.exit(1)
