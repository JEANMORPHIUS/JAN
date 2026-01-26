#!/usr/bin/env python3
"""JAN Studio Installation Verification Script

Run this script to verify your JAN Studio installation is ready.
Checks all prerequisites, dependencies, and configuration.

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

import os
import sys
import subprocess
from pathlib import Path
from typing import Tuple

# Color codes for terminal output
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
RESET = '\033[0m'
BOLD = '\033[1m'

def print_header(text: str):
    """Print a formatted header."""
    print(f"\n{BOLD}{BLUE}{'='*60}{RESET}")
    print(f"{BOLD}{BLUE}{text.center(60)}{RESET}")
    print(f"{BOLD}{BLUE}{'='*60}{RESET}\n")

def print_check(name: str, status: bool, message: str = ""):
    """Print a check result."""
    icon = f"{GREEN}✓{RESET}" if status else f"{RED}✗{RESET}"
    status_text = f"{GREEN}PASS{RESET}" if status else f"{RED}FAIL{RESET}"
    print(f"{icon} {name:.<40} {status_text}")
    if message:
        print(f"  {YELLOW}→{RESET} {message}")

def check_command_version(command: str, min_version: str = None) -> Tuple[bool, str]:
    """Check if a command exists and optionally verify version."""
    try:
        result = subprocess.run(
            [command, '--version'],
            capture_output=True,
            text=True,
            timeout=5
        )
        version_output = result.stdout + result.stderr
        version_line = version_output.split('\n')[0]
        return True, version_line
    except (subprocess.TimeoutExpired, FileNotFoundError, subprocess.SubprocessError):
        return False, ""

def check_python():
    """Check Python installation."""
    print_header("Python Environment")

    # Check Python version
    version = sys.version_info
    is_valid = version.major == 3 and version.minor >= 8
    print_check(
        "Python Version",
        is_valid,
        f"Found: Python {version.major}.{version.minor}.{version.micro}" +
        ("" if is_valid else " (Need 3.8+)")
    )

    # Check pip
    pip_exists, pip_version = check_command_version('pip')
    print_check("pip", pip_exists, pip_version if pip_exists else "pip not found")

    return is_valid and pip_exists

def check_node():
    """Check Node.js installation."""
    print_header("Node.js Environment")

    # Check Node.js
    node_exists, node_version = check_command_version('node')
    node_valid = node_exists and (
        'v18' in node_version or
        'v19' in node_version or
        'v20' in node_version or
        int(node_version.split('.')[0].replace('v', '')) >= 18
    )
    print_check(
        "Node.js Version",
        node_valid,
        node_version if node_exists else "Node.js not found (Need 18+)"
    )

    # Check npm
    npm_exists, npm_version = check_command_version('npm')
    print_check("npm", npm_exists, npm_version if npm_exists else "npm not found")

    return node_valid and npm_exists

def check_files():
    """Check required files exist."""
    print_header("Required Files")

    script_dir = Path(__file__).parent
    checks = []

    # Backend files
    backend_dir = script_dir / "backend"
    checks.append(("requirements.txt", backend_dir / "requirements.txt"))
    checks.append(("main.py", backend_dir / "main.py"))
    checks.append(("setup_jan_structure.py", backend_dir / "setup_jan_structure.py"))

    # Frontend files
    frontend_dir = script_dir / "frontend"
    checks.append(("package.json", frontend_dir / "package.json"))
    checks.append(("next.config.js", frontend_dir / "next.config.js"))

    # Config files
    checks.append((".env.example", script_dir / ".env.example"))

    all_exist = True
    for name, path in checks:
        exists = path.exists()
        all_exist = all_exist and exists
        print_check(name, exists, str(path.relative_to(script_dir)))

    return all_exist

def check_backend_dependencies():
    """Check backend Python dependencies."""
    print_header("Backend Dependencies")

    required = [
        'fastapi',
        'uvicorn',
        'pydantic',
        'dotenv'
    ]

    all_installed = True
    for package in required:
        try:
            __import__(package.replace('-', '_'))
            print_check(package, True, "Installed")
        except ImportError:
            print_check(package, False, "Not installed")
            all_installed = False

    return all_installed

def check_environment():
    """Check environment configuration."""
    print_header("Environment Configuration")

    script_dir = Path(__file__).parent
    env_file = script_dir / ".env"
    env_example = script_dir / ".env.example"

    # Check .env file exists
    env_exists = env_file.exists()
    print_check(
        ".env file",
        env_exists,
        "Found" if env_exists else "Missing (copy from .env.example)"
    )

    # Check JAN_ROOT
    jan_root = os.getenv('JAN_ROOT', './jan')
    jan_path = Path(jan_root).resolve()
    jan_exists = jan_path.exists()
    print_check(
        "JAN_ROOT directory",
        jan_exists,
        f"{jan_path}" + ("" if jan_exists else " (run setup_jan_structure.py)")
    )

    # Check Siyem.org
    siyem_path = jan_path / "Siyem.org"
    siyem_exists = siyem_path.exists() if jan_exists else False
    print_check(
        "Siyem.org directory",
        siyem_exists,
        str(siyem_path) if siyem_exists else "Not found"
    )

    return env_exists and jan_exists and siyem_exists

def check_ports():
    """Check if required ports are available."""
    print_header("Port Availability")

    ports = {
        8000: "Backend API",
        3000: "Frontend UI"
    }

    all_available = True
    for port, service in ports.items():
        # Try to bind to port
        import socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        try:
            result = sock.connect_ex(('localhost', port))
            if result == 0:
                print_check(f"Port {port}", False, f"{service} - Port in use")
                all_available = False
            else:
                print_check(f"Port {port}", True, f"{service} - Available")
        except:
            print_check(f"Port {port}", True, f"{service} - Available")
        finally:
            sock.close()

    return all_available

def print_next_steps(all_passed: bool):
    """Print next steps based on results."""
    print_header("Summary")

    if all_passed:
        print(f"{GREEN}{BOLD}✓ All checks passed!{RESET}\n")
        print("Your JAN Studio installation is ready.\n")
        print(f"{BOLD}Next steps:{RESET}")
        print("1. Start backend:  cd backend && python main.py")
        print("2. Start frontend: cd frontend && npm run dev")
        print("3. Open browser:   http://localhost:3000")
    else:
        print(f"{RED}{BOLD}✗ Some checks failed{RESET}\n")
        print(f"{BOLD}To fix issues:{RESET}")
        print("1. Install missing dependencies:")
        print("   - Backend:  cd backend && pip install -r requirements.txt")
        print("   - Frontend: cd frontend && npm install")
        print("2. Create .env file:")
        print("   - Copy: cp .env.example .env")
        print("3. Setup JAN structure:")
        print("   - Run: cd backend && python setup_jan_structure.py")
        print("\nSee INSTALL.md for detailed instructions.")

def main():
    """Run all verification checks."""
    print(f"\n{BOLD}JAN Studio Installation Verification{RESET}")
    print("This script will verify your installation is ready.\n")

    results = []

    # Run checks
    results.append(("Python", check_python()))
    results.append(("Node.js", check_node()))
    results.append(("Files", check_files()))

    # Only check dependencies if basics are good
    if results[0][1]:  # If Python is OK
        results.append(("Backend Dependencies", check_backend_dependencies()))

    results.append(("Environment", check_environment()))
    results.append(("Ports", check_ports()))

    # Print summary
    all_passed = all(result[1] for result in results)
    print_next_steps(all_passed)

    return 0 if all_passed else 1

if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print(f"\n{YELLOW}Verification cancelled{RESET}")
        sys.exit(1)
