"""
RASPBERRY PI DEPLOYMENT API
Complete deployment management for Raspberry Pi Scripture Kits

THE NOAH PROTOCOL:
- Architectural Weight: Built for 10x, 100x, 1000x deployments
- The Pitch: Waterproof error handling
- The Perimeter: Clear deployment boundaries

THE ARRIVAL PROTOCOL:
- Pre-Commissioning Scan: Can this handle 1000x deployments?
- Frequency Anchor: Deploy from "done" - production ready

THE TRUTH:
Scale and build until ready.
Raspberry Pi deployments for the new world.
"""

from fastapi import APIRouter, HTTPException, status, BackgroundTasks
from typing import Dict, List, Any, Optional
from datetime import datetime
from pathlib import Path
import json
import logging
import subprocess
import sys

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/raspberry-pi", tags=["Raspberry Pi Deployment"])


class RaspberryPiDeploymentManager:
    """
    Raspberry Pi Deployment Manager
    Manages deployments, builds, and monitoring
    """
    
    def __init__(self):
        """Initialize deployment manager"""
        self.project_root = Path(__file__).parent.parent.parent.parent
        self.package_builder_script = self.project_root / "scripts" / "raspberry_pi_package_builder.py"
        self.package_output = self.project_root / "output" / "raspberry_pi_packages"
        self.deployments: Dict[str, Dict[str, Any]] = {}
        
        logger.info("Raspberry Pi Deployment Manager initialized")
    
    def build_package(self, version: Optional[str] = None) -> Dict[str, Any]:
        """Build Raspberry Pi package"""
        try:
            if version is None:
                version = datetime.now().strftime("%Y%m%d_%H%M%S")
            
            # Run package builder
            result = subprocess.run(
                [sys.executable, str(self.package_builder_script)],
                capture_output=True,
                text=True,
                cwd=str(self.project_root)
            )
            
            if result.returncode != 0:
                raise Exception(f"Build failed: {result.stderr}")
            
            # Find generated package
            packages = list(self.package_output.glob("scripture_kit_*"))
            if not packages:
                raise Exception("No package generated")
            
            latest_package = max(packages, key=lambda p: p.stat().st_mtime)
            
            deployment_id = f"pi_deploy_{version}"
            self.deployments[deployment_id] = {
                "id": deployment_id,
                "version": version,
                "package_path": str(latest_package),
                "status": "built",
                "created_at": datetime.now().isoformat(),
                "build_log": result.stdout
            }
            
            return self.deployments[deployment_id]
        except Exception as e:
            logger.error(f"Build package error: {e}")
            raise
    
    def get_deployment_status(self, deployment_id: str) -> Dict[str, Any]:
        """Get deployment status"""
        if deployment_id not in self.deployments:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Deployment not found"
            )
        
        deployment = self.deployments[deployment_id]
        package_path = Path(deployment["package_path"])
        
        # Check if package exists
        if package_path.exists():
            deployment["package_size"] = package_path.stat().st_size
            deployment["package_exists"] = True
        else:
            deployment["package_exists"] = False
        
        return deployment
    
    def list_deployments(self) -> List[Dict[str, Any]]:
        """List all deployments"""
        return list(self.deployments.values())
    
    def get_package_info(self, deployment_id: str) -> Dict[str, Any]:
        """Get package information"""
        deployment = self.get_deployment_status(deployment_id)
        package_path = Path(deployment["package_path"])
        
        if not package_path.exists():
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Package file not found"
            )
        
        # Read manifest if available
        manifest_path = package_path.parent / "manifest.json"
        manifest = {}
        if manifest_path.exists():
            manifest = json.loads(manifest_path.read_text(encoding='utf-8'))
        
        return {
            "deployment": deployment,
            "manifest": manifest,
            "package_size_mb": deployment.get("package_size", 0) / (1024 * 1024),
            "download_url": f"/api/raspberry-pi/packages/{deployment_id}/download"
        }


# Global manager instance
_manager: Optional[RaspberryPiDeploymentManager] = None


def get_deployment_manager() -> RaspberryPiDeploymentManager:
    """Get global deployment manager"""
    global _manager
    if _manager is None:
        _manager = RaspberryPiDeploymentManager()
    return _manager


@router.post("/build")
async def build_package(version: Optional[str] = None, background_tasks: BackgroundTasks = None):
    """Build Raspberry Pi package"""
    try:
        manager = get_deployment_manager()
        
        # Build in background if requested
        if background_tasks:
            background_tasks.add_task(manager.build_package, version)
            return {
                "status": "building",
                "message": "Package build started in background",
                "version": version or "auto"
            }
        
        # Build synchronously
        deployment = manager.build_package(version)
        return {
            "status": "success",
            "deployment": deployment
        }
    except Exception as e:
        logger.error(f"Build package error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to build package: {str(e)}"
        )


@router.get("/deployments")
async def list_deployments():
    """List all deployments"""
    try:
        manager = get_deployment_manager()
        return {
            "deployments": manager.list_deployments(),
            "count": len(manager.deployments)
        }
    except Exception as e:
        logger.error(f"List deployments error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to list deployments"
        )


@router.get("/deployments/{deployment_id}")
async def get_deployment(deployment_id: str):
    """Get deployment status"""
    try:
        manager = get_deployment_manager()
        return manager.get_deployment_status(deployment_id)
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Get deployment error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to get deployment"
        )


@router.get("/deployments/{deployment_id}/info")
async def get_package_info(deployment_id: str):
    """Get package information"""
    try:
        manager = get_deployment_manager()
        return manager.get_package_info(deployment_id)
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Get package info error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to get package info"
        )


@router.get("/health")
async def deployment_health():
    """Check deployment system health"""
    try:
        manager = get_deployment_manager()
        
        # Check if builder script exists
        builder_exists = manager.package_builder_script.exists()
        
        # Check output directory
        output_exists = manager.package_output.exists()
        
        # Count existing packages
        package_count = len(list(manager.package_output.glob("scripture_kit_*"))) if output_exists else 0
        
        return {
            "status": "healthy" if builder_exists and output_exists else "degraded",
            "builder_script": builder_exists,
            "output_directory": output_exists,
            "existing_packages": package_count,
            "deployments": len(manager.deployments)
        }
    except Exception as e:
        logger.error(f"Health check error: {e}")
        return {
            "status": "unhealthy",
            "error": str(e)
        }
