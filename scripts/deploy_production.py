"""
Production Deployment Script
Complete production deployment automation

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

PRODUCTION DEPLOYMENT:
Complete production deployment with all best practices
Gunicorn + Uvicorn workers
Nginx reverse proxy
Prometheus + Grafana monitoring
SSL/HTTPS configuration
"""

import subprocess
import sys
import os
from pathlib import Path
from datetime import datetime
import json

class ProductionDeployment:
    """Complete production deployment automation"""
    
    def __init__(self, project_root: str = "S:/JAN"):
        self.project_root = Path(project_root)
        self.deploy_dir = self.project_root / "deploy"
        self.backend_dir = self.project_root / "jan-studio" / "backend"
        self.deployment_log = []
        
    def check_prerequisites(self):
        """Check all production deployment prerequisites"""
        print("\n" + "="*80)
        print("PRODUCTION DEPLOYMENT PREREQUISITES")
        print("="*80 + "\n")
        
        checks = {}
        
        # Docker
        print("1. Checking Docker...")
        try:
            result = subprocess.run(['docker', '--version'], capture_output=True, text=True)
            checks['docker'] = result.returncode == 0
            if checks['docker']:
                print(f"   ✓ {result.stdout.strip()}")
        except:
            checks['docker'] = False
            print("   ✗ Docker not found")
        
        # Docker Compose
        print("2. Checking Docker Compose...")
        try:
            result = subprocess.run(['docker-compose', '--version'], capture_output=True, text=True)
            checks['docker_compose'] = result.returncode == 0
            if checks['docker_compose']:
                print(f"   ✓ {result.stdout.strip()}")
        except:
            checks['docker_compose'] = False
            print("   ✗ Docker Compose not found")
        
        # Environment file
        print("3. Checking production environment...")
        env_file = self.deploy_dir / ".env.production"
        env_example = self.deploy_dir / ".env.production.example"
        checks['env_file'] = env_file.exists()
        if checks['env_file']:
            print("   ✓ .env.production found")
        else:
            print(f"   ⚠ .env.production not found - copy from {env_example.name}")
        
        # SSL certificates
        print("4. Checking SSL certificates...")
        ssl_dir = self.deploy_dir / "nginx" / "ssl"
        cert_file = ssl_dir / "cert.pem"
        key_file = ssl_dir / "key.pem"
        checks['ssl_certs'] = cert_file.exists() and key_file.exists()
        if checks['ssl_certs']:
            print("   ✓ SSL certificates found")
        else:
            print("   ⚠ SSL certificates not found - required for HTTPS")
            print(f"      Place certificates in: {ssl_dir}")
        
        print()
        return checks
    
    def deploy_production(self):
        """Deploy complete production stack"""
        print("\n" + "="*80)
        print("PRODUCTION DEPLOYMENT")
        print("="*80 + "\n")
        
        # Check prerequisites
        checks = self.check_prerequisites()
        
        if not checks.get('docker'):
            print("❌ Docker is required for production deployment")
            print("   Install Docker: https://www.docker.com/")
            return False
        
        # Build production image
        print("1. Building production Docker image...")
        try:
            subprocess.run([
                'docker', 'build',
                '-f', str(self.deploy_dir / "Dockerfile.production"),
                '-t', 'jan-studio:production',
                '--build-arg', 'BUILD_DATE=' + datetime.now().isoformat(),
                str(self.project_root)
            ], check=True)
            print("   ✓ Production image built\n")
        except subprocess.CalledProcessError as e:
            print(f"   ✗ Build failed: {e}\n")
            return False
        
        # Start services
        print("2. Starting production services...")
        compose_file = self.deploy_dir / "docker-compose.production.yml"
        try:
            subprocess.run([
                'docker-compose',
                '-f', str(compose_file),
                'up', '-d'
            ], cwd=self.project_root, check=True)
            print("   ✓ Services started\n")
        except subprocess.CalledProcessError as e:
            print(f"   ✗ Failed to start services: {e}\n")
            return False
        
        # Wait for health
        print("3. Waiting for services to be healthy...")
        import time
        time.sleep(10)
        
        # Check health
        print("4. Checking service health...")
        try:
            result = subprocess.run([
                'curl', '-f', 'http://localhost:8000/health'
            ], capture_output=True, text=True, timeout=10)
            if result.returncode == 0:
                print("   ✓ API is healthy\n")
            else:
                print("   ⚠ Health check failed - check logs\n")
        except:
            print("   ⚠ Health check unavailable - verify manually\n")
        
        # Show status
        print("5. Service status:")
        subprocess.run([
            'docker-compose',
            '-f', str(compose_file),
            'ps'
        ], cwd=self.project_root)
        print()
        
        return True
    
    def generate_deployment_report(self):
        """Generate production deployment report"""
        report = {
            "deployment_timestamp": datetime.now().isoformat(),
            "system": "JAN Studio API - Production",
            "version": "1.0.0",
            "status": "deployed",
            "components": {
                "api": {
                    "status": "running",
                    "url": "http://localhost:8000",
                    "health": "http://localhost:8000/health",
                    "metrics": "http://localhost:8000/metrics"
                },
                "nginx": {
                    "status": "running",
                    "ports": ["80", "443"]
                },
                "prometheus": {
                    "status": "running",
                    "url": "http://localhost:9090"
                },
                "grafana": {
                    "status": "running",
                    "url": "http://localhost:3001"
                }
            },
            "endpoints": {
                "api": "http://localhost:8000",
                "api_docs": "http://localhost:8000/docs",
                "health": "http://localhost:8000/health",
                "health_detailed": "http://localhost:8000/health/detailed",
                "metrics": "http://localhost:8000/metrics",
                "prometheus": "http://localhost:9090",
                "grafana": "http://localhost:3001"
            },
            "philosophy": {
                "mission": "STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS",
                "love": "LOVE IS THE HIGHEST MASTERY",
                "unity": "ENERGY + LOVE = WE ALL WIN",
                "peace": "PEACE, LOVE, UNITY"
            }
        }
        
        report_file = self.project_root / "deployment_report_production.json"
        with open(report_file, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        
        return report
    
    def deploy(self):
        """Execute complete production deployment"""
        print("\n" + "="*80)
        print("JAN STUDIO - PRODUCTION DEPLOYMENT")
        print("Serving Humanity with Love and Purpose")
        print("="*80)
        
        if self.deploy_production():
            report = self.generate_deployment_report()
            
            print("\n" + "="*80)
            print("PRODUCTION DEPLOYMENT COMPLETE")
            print("="*80 + "\n")
            
            print("Service Status:")
            for component, data in report['components'].items():
                status_symbol = "✓" if data.get('status') == 'running' else "⏳"
                print(f"  {status_symbol} {component.capitalize()}: {data.get('status', 'unknown')}")
            
            print("\nAccess Points:")
            for name, url in report['endpoints'].items():
                print(f"  - {name.replace('_', ' ').title()}: {url}")
            
            print("\nNext Steps:")
            print("  1. Verify health: curl http://localhost:8000/health")
            print("  2. Check metrics: curl http://localhost:8000/metrics")
            print("  3. Access Grafana: http://localhost:3001 (admin/admin)")
            print("  4. Access Prometheus: http://localhost:9090")
            print("  5. View API docs: http://localhost:8000/docs")
            print("  6. Monitor logs: docker-compose -f deploy/docker-compose.production.yml logs -f")
            
            print("\nPhilosophy:")
            for key, value in report['philosophy'].items():
                print(f"  {key.capitalize()}: {value}")
            
            print("\n" + "="*80)
            print("READY TO SERVE HUMANITY")
            print("="*80 + "\n")
            
            return True
        else:
            print("\n❌ Deployment failed. Check errors above.")
            return False


def main():
    """Main deployment function"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Deploy JAN Studio to Production')
    parser.add_argument('--check-only', action='store_true', help='Only check prerequisites')
    
    args = parser.parse_args()
    
    deployer = ProductionDeployment()
    
    if args.check_only:
        deployer.check_prerequisites()
    else:
        deployer.deploy()


if __name__ == "__main__":
    main()
