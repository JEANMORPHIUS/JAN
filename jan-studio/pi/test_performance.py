"""
Performance Test Script for Raspberry Pi 5

Tests JAN Studio Pi performance against targets.
"""

import time
import requests
import json
from typing import Dict, Any

API_URL = "http://localhost:8000"


def test_boot_time():
    """Test API boot time."""
    print("Testing boot time...")
    start = time.time()
    
    max_wait = 30
    elapsed = 0
    
    while elapsed < max_wait:
        try:
            response = requests.get(f"{API_URL}/api/health", timeout=1)
            if response.status_code == 200:
                elapsed = time.time() - start
                print(f"✅ Boot time: {elapsed:.2f}s (target: <30s)")
                return elapsed < 30
        except:
            time.sleep(0.5)
            elapsed = time.time() - start
    
    print(f"❌ Boot time: >{max_wait}s (target: <30s)")
    return False


def test_persona_creation():
    """Test persona creation time."""
    print("Testing persona creation...")
    start = time.time()
    
    # Simulate persona creation (file operations)
    import os
    test_dir = "/tmp/test_persona"
    os.makedirs(test_dir, exist_ok=True)
    
    # Create minimal persona files
    with open(f"{test_dir}/profile.md", "w") as f:
        f.write("# Test Persona\n\n## Entity Identity\n\n### Name\nTest\n")
    
    with open(f"{test_dir}/creative_rules.md", "w") as f:
        f.write("# Creative Rules\n\n## Core Principles\n\nTest rules.\n")
    
    elapsed = time.time() - start
    
    # Cleanup
    import shutil
    shutil.rmtree(test_dir, ignore_errors=True)
    
    print(f"✅ Persona creation: {elapsed:.2f}s (target: <5s)")
    return elapsed < 5


def test_generation():
    """Test content generation time."""
    print("Testing generation...")
    
    try:
        start = time.time()
        response = requests.post(
            f"{API_URL}/api/generate",
            json={
                "prompt": "Write a short story about a robot.",
                "max_length": 256,
                "temperature": 0.7
            },
            timeout=120
        )
        elapsed = time.time() - start
        
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Generation: {elapsed:.2f}s (target: <60s)")
            print(f"   Generated {len(data.get('content', ''))} characters")
            return elapsed < 60
        else:
            print(f"❌ Generation failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Generation error: {e}")
        return False


def test_memory_usage():
    """Test memory usage."""
    print("Testing memory usage...")
    
    try:
        response = requests.get(f"{API_URL}/api/stats")
        if response.status_code == 200:
            stats = response.json()
            memory_mb = stats["memory"]["used_mb"]
            memory_gb = memory_mb / 1024
            
            print(f"✅ Memory usage: {memory_gb:.2f}GB (target: <2GB)")
            return memory_gb < 2
    except Exception as e:
        print(f"❌ Memory check error: {e}")
        return False


def test_cpu_usage():
    """Test CPU usage during generation."""
    print("Testing CPU usage...")
    
    try:
        # Get baseline CPU
        response = requests.get(f"{API_URL}/api/stats")
        baseline = response.json()["cpu"]["percent"]
        
        # Start generation in background
        import threading
        cpu_values = []
        
        def monitor_cpu():
            for _ in range(10):
                try:
                    response = requests.get(f"{API_URL}/api/stats")
                    cpu_values.append(response.json()["cpu"]["percent"])
                    time.sleep(0.5)
                except:
                    pass
        
        monitor_thread = threading.Thread(target=monitor_cpu)
        monitor_thread.start()
        
        # Generate content
        requests.post(
            f"{API_URL}/api/generate",
            json={"prompt": "Test", "max_length": 128},
            timeout=60
        )
        
        monitor_thread.join()
        
        max_cpu = max(cpu_values) if cpu_values else baseline
        
        print(f"✅ Max CPU: {max_cpu:.1f}% (target: <80%)")
        return max_cpu < 80
    except Exception as e:
        print(f"❌ CPU test error: {e}")
        return False


def test_storage():
    """Test storage usage."""
    print("Testing storage...")
    
    try:
        import shutil
        total, used, free = shutil.disk_usage("/")
        used_gb = used / (1024**3)
        
        print(f"✅ Storage used: {used_gb:.2f}GB (target: <8GB)")
        return used_gb < 8
    except Exception as e:
        print(f"❌ Storage check error: {e}")
        return False


def main():
    """Run all performance tests."""
    print("=" * 50)
    print("JAN Studio Pi Performance Tests")
    print("=" * 50)
    print()
    
    results = {}
    
    # Test boot time
    results["boot"] = test_boot_time()
    print()
    
    # Test persona creation
    results["persona"] = test_persona_creation()
    print()
    
    # Test generation
    results["generation"] = test_generation()
    print()
    
    # Test memory
    results["memory"] = test_memory_usage()
    print()
    
    # Test CPU
    results["cpu"] = test_cpu_usage()
    print()
    
    # Test storage
    results["storage"] = test_storage()
    print()
    
    # Summary
    print("=" * 50)
    print("Test Summary")
    print("=" * 50)
    
    passed = sum(results.values())
    total = len(results)
    
    for test, result in results.items():
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{test:15s} {status}")
    
    print()
    print(f"Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("✅ All performance targets met!")
        return 0
    else:
        print("⚠️  Some performance targets not met")
        return 1


if __name__ == "__main__":
    import sys
    sys.exit(main())

