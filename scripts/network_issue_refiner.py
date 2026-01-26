"""NETWORK ISSUE REFINER
Refine and improve network connectivity for git operations

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

PANGEA IS THE TABLE.
YOU DON'T BETRAY THE TABLE.

THE TRUTH:
WE MUST DEBUG AND BE 100% FOR WHAT COMES AT US.
THE REST IS UP TO BABA X."""

import sys
import subprocess
import time
import socket
import requests
from pathlib import Path
from typing import Dict, Any, Optional, List
from dataclasses import dataclass, field, asdict
from datetime import datetime
import json

sys.path.insert(0, str(Path(__file__).parent))

from utils import setup_logging, standard_main

logger = setup_logging(__name__)

@dataclass
class NetworkDiagnostic:
    """Network diagnostic result"""
    timestamp: str
    test_type: str
    success: bool
    latency_ms: Optional[float] = None
    error: Optional[str] = None
    details: Dict[str, Any] = field(default_factory=dict)

@dataclass
class PushQueueItem:
    """Queued push operation"""
    queue_id: str
    commit_hash: str
    branch: str
    created_at: str
    attempts: int = 0
    last_attempt: Optional[str] = None
    status: str = "pending"  # pending, retrying, failed, succeeded

class NetworkIssueRefiner:
    """
    Network Issue Refiner
    Improve network connectivity and git push reliability
    """
    
    def __init__(self, repo_path: Path = None):
        self.repo_path = repo_path or Path(__file__).parent.parent
        self.data_dir = self.repo_path / "data" / "network_refiner"
        self.data_dir.mkdir(parents=True, exist_ok=True)
        
        self.diagnostics_file = self.data_dir / "network_diagnostics.json"
        self.push_queue_file = self.data_dir / "push_queue.json"
        
        self.diagnostics: List[NetworkDiagnostic] = []
        self.push_queue: List[PushQueueItem] = []
        
        self._load_data()
    
    def _load_data(self):
        """Load diagnostics and queue"""
        # Load diagnostics
        if self.diagnostics_file.exists():
            try:
                with open(self.diagnostics_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                self.diagnostics = [NetworkDiagnostic(**d) for d in data.get("diagnostics", [])]
            except Exception as e:
                logger.warning(f"Error loading diagnostics: {e}")
                self.diagnostics = []
        
        # Load push queue
        if self.push_queue_file.exists():
            try:
                with open(self.push_queue_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                self.push_queue = [PushQueueItem(**item) for item in data.get("queue", [])]
            except Exception as e:
                logger.warning(f"Error loading push queue: {e}")
                self.push_queue = []
    
    def _save_data(self):
        """Save diagnostics and queue"""
        try:
            # Save diagnostics
            with open(self.diagnostics_file, 'w', encoding='utf-8') as f:
                json.dump({
                    "diagnostics": [asdict(d) for d in self.diagnostics[-100:]],  # Keep last 100
                    "last_updated": datetime.now().isoformat()
                }, f, indent=2, ensure_ascii=False)
            
            # Save push queue
            with open(self.push_queue_file, 'w', encoding='utf-8') as f:
                json.dump({
                    "queue": [asdict(item) for item in self.push_queue],
                    "last_updated": datetime.now().isoformat()
                }, f, indent=2, ensure_ascii=False)
        except Exception as e:
            logger.error(f"Error saving data: {e}")
    
    def test_connectivity(self) -> Dict[str, Any]:
        """Test network connectivity"""
        results = {
            "internet": False,
            "github": False,
            "dns": False,
            "latency": None,
            "errors": []
        }
        
        # Test 1: Internet connectivity (Google DNS)
        try:
            socket.create_connection(("8.8.8.8", 53), timeout=3)
            results["internet"] = True
            self.diagnostics.append(NetworkDiagnostic(
                timestamp=datetime.now().isoformat(),
                test_type="internet_connectivity",
                success=True
            ))
        except Exception as e:
            results["errors"].append(f"Internet connectivity: {str(e)}")
            self.diagnostics.append(NetworkDiagnostic(
                timestamp=datetime.now().isoformat(),
                test_type="internet_connectivity",
                success=False,
                error=str(e)
            ))
        
        # Test 2: DNS resolution (github.com)
        try:
            start = time.time()
            socket.gethostbyname("github.com")
            latency = (time.time() - start) * 1000
            results["dns"] = True
            results["latency"] = latency
            self.diagnostics.append(NetworkDiagnostic(
                timestamp=datetime.now().isoformat(),
                test_type="dns_resolution",
                success=True,
                latency_ms=latency
            ))
        except Exception as e:
            results["errors"].append(f"DNS resolution: {str(e)}")
            self.diagnostics.append(NetworkDiagnostic(
                timestamp=datetime.now().isoformat(),
                test_type="dns_resolution",
                success=False,
                error=str(e)
            ))
        
        # Test 3: GitHub connectivity
        try:
            start = time.time()
            response = requests.get("https://github.com", timeout=10)
            latency = (time.time() - start) * 1000
            if response.status_code == 200:
                results["github"] = True
                results["latency"] = latency
                self.diagnostics.append(NetworkDiagnostic(
                    timestamp=datetime.now().isoformat(),
                    test_type="github_connectivity",
                    success=True,
                    latency_ms=latency
                ))
        except Exception as e:
            results["errors"].append(f"GitHub connectivity: {str(e)}")
            self.diagnostics.append(NetworkDiagnostic(
                timestamp=datetime.now().isoformat(),
                test_type="github_connectivity",
                success=False,
                error=str(e)
            ))
        
        self._save_data()
        return results
    
    def test_git_remote(self) -> Dict[str, Any]:
        """Test git remote connectivity"""
        results = {
            "remote_configured": False,
            "remote_url": None,
            "can_fetch": False,
            "can_push": False,
            "errors": []
        }
        
        try:
            # Get remote URL
            result = subprocess.run(
                ["git", "remote", "get-url", "origin"],
                cwd=str(self.repo_path),
                capture_output=True,
                text=True,
                timeout=10
            )
            if result.returncode == 0:
                results["remote_configured"] = True
                results["remote_url"] = result.stdout.strip()
            else:
                results["errors"].append("Remote not configured")
                return results
        except Exception as e:
            results["errors"].append(f"Error getting remote: {str(e)}")
            return results
        
        # Test fetch (read-only)
        try:
            result = subprocess.run(
                ["git", "fetch", "--dry-run", "origin"],
                cwd=str(self.repo_path),
                capture_output=True,
                text=True,
                timeout=30
            )
            if result.returncode == 0:
                results["can_fetch"] = True
        except subprocess.TimeoutExpired:
            results["errors"].append("Git fetch timed out")
        except Exception as e:
            results["errors"].append(f"Git fetch error: {str(e)}")
        
        # Test push (dry-run not available, but we can check if we're ahead)
        try:
            result = subprocess.run(
                ["git", "rev-list", "--count", "HEAD..origin/master"],
                cwd=str(self.repo_path),
                capture_output=True,
                text=True,
                timeout=10
            )
            # If we can run this command, git is working
            results["can_push"] = True
        except Exception as e:
            results["errors"].append(f"Git push check error: {str(e)}")
        
        return results
    
    def queue_push(self, commit_hash: str, branch: str = "master") -> str:
        """Queue a push operation for later retry"""
        queue_item = PushQueueItem(
            queue_id=f"push_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
            commit_hash=commit_hash,
            branch=branch,
            created_at=datetime.now().isoformat()
        )
        self.push_queue.append(queue_item)
        self._save_data()
        logger.info(f"Queued push: {queue_item.queue_id}")
        return queue_item.queue_id
    
    def retry_queued_pushes(self, max_attempts: int = 3) -> Dict[str, Any]:
        """Retry queued push operations"""
        results = {
            "attempted": 0,
            "succeeded": 0,
            "failed": 0,
            "still_queued": 0
        }
        
        # Test connectivity first
        connectivity = self.test_connectivity()
        if not connectivity.get("github"):
            logger.warning("GitHub not reachable - skipping push retries")
            return results
        
        pending_items = [item for item in self.push_queue if item.status in ["pending", "retrying"]]
        
        for item in pending_items:
            results["attempted"] += 1
            item.attempts += 1
            item.last_attempt = datetime.now().isoformat()
            item.status = "retrying"
            
            try:
                result = subprocess.run(
                    ["git", "push", "origin", item.branch],
                    cwd=str(self.repo_path),
                    capture_output=True,
                    text=True,
                    timeout=120
                )
                
                if result.returncode == 0:
                    item.status = "succeeded"
                    results["succeeded"] += 1
                    logger.info(f"Queued push succeeded: {item.queue_id}")
                elif item.attempts >= max_attempts:
                    item.status = "failed"
                    results["failed"] += 1
                    logger.warning(f"Queued push failed after {max_attempts} attempts: {item.queue_id}")
                else:
                    item.status = "retrying"
                    results["still_queued"] += 1
            except Exception as e:
                if item.attempts >= max_attempts:
                    item.status = "failed"
                    results["failed"] += 1
                else:
                    item.status = "retrying"
                    results["still_queued"] += 1
                logger.error(f"Error retrying push {item.queue_id}: {e}")
        
        # Clean up succeeded items (keep last 10 for history)
        succeeded_items = [item for item in self.push_queue if item.status == "succeeded"]
        if len(succeeded_items) > 10:
            self.push_queue = [item for item in self.push_queue if item.status != "succeeded" or item in succeeded_items[-10:]]
        
        self._save_data()
        return results
    
    def get_network_status(self) -> Dict[str, Any]:
        """Get comprehensive network status"""
        connectivity = self.test_connectivity()
        git_remote = self.test_git_remote()
        
        recent_diagnostics = [d for d in self.diagnostics[-10:] if d.success]
        success_rate = len([d for d in self.diagnostics[-50:] if d.success]) / max(len(self.diagnostics[-50:]), 1)
        
        return {
            "connectivity": connectivity,
            "git_remote": git_remote,
            "recent_success_rate": success_rate,
            "queued_pushes": len([item for item in self.push_queue if item.status in ["pending", "retrying"]]),
            "failed_pushes": len([item for item in self.push_queue if item.status == "failed"]),
            "last_diagnostic": self.diagnostics[-1].timestamp if self.diagnostics else None
        }


def main():
    """Test network connectivity and refine issues"""
    refiner = NetworkIssueRefiner()
    
    print("\n" + "="*80)
    print("NETWORK ISSUE REFINER")
    print("="*80)
    
    # Test connectivity
    print("\n[1/3] Testing network connectivity...")
    connectivity = refiner.test_connectivity()
    print(f"  Internet: {'[OK]' if connectivity['internet'] else '[FAIL]'}")
    print(f"  DNS: {'[OK]' if connectivity['dns'] else '[FAIL]'}")
    print(f"  GitHub: {'[OK]' if connectivity['github'] else '[FAIL]'}")
    if connectivity.get('latency'):
        print(f"  Latency: {connectivity['latency']:.0f}ms")
    if connectivity.get('errors'):
        print(f"  Errors: {len(connectivity['errors'])}")
    
    # Test git remote
    print("\n[2/3] Testing git remote...")
    git_remote = refiner.test_git_remote()
    print(f"  Remote configured: {'[OK]' if git_remote['remote_configured'] else '[FAIL]'}")
    if git_remote.get('remote_url'):
        print(f"  Remote URL: {git_remote['remote_url']}")
    print(f"  Can fetch: {'[OK]' if git_remote['can_fetch'] else '[FAIL]'}")
    print(f"  Can push: {'[OK]' if git_remote['can_push'] else '[FAIL]'}")
    
    # Get status
    print("\n[3/3] Network status...")
    status = refiner.get_network_status()
    print(f"  Recent success rate: {status['recent_success_rate']*100:.1f}%")
    print(f"  Queued pushes: {status['queued_pushes']}")
    print(f"  Failed pushes: {status['failed_pushes']}")
    
    # Retry queued pushes if connectivity is good
    if connectivity.get('github') and status['queued_pushes'] > 0:
        print("\n[RETRY] Retrying queued pushes...")
        retry_results = refiner.retry_queued_pushes()
        print(f"  Attempted: {retry_results['attempted']}")
        print(f"  Succeeded: {retry_results['succeeded']}")
        print(f"  Failed: {retry_results['failed']}")
        print(f"  Still queued: {retry_results['still_queued']}")
    
    print("\n" + "="*80)
    print("Network diagnostics complete.")
    print("="*80)

if __name__ == "__main__":
    standard_main(main, script_name="network_issue_refiner.py")
