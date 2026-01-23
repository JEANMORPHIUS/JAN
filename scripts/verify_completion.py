
import sys
from pathlib import Path

# Add utils to path
sys.path.insert(0, str(Path(__file__).parent))

from utils import (
    Path, json, load_json, save_json, setup_logging
)
"""Verify completion status"""
import json
from pathlib import Path

data_path = Path(__file__).parent.parent / 'data' / 'heritage_meridian' / 'round1_activation_log.json'
with open(data_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

print("=" * 80)
print("COMPLETION VERIFICATION")
print("=" * 80)
print()
print(f"Total Acts in Log: {len(data['activation_log'])}")
print(f"Current Unity: {data['unity_progress']['current_unity']:.1%}")
print(f"Acts Logged: {data['unity_progress']['total_acts_logged']}")
print(f"Unity Contributed: {data['unity_progress']['total_unity_contributed']:.4f}")
print()
print("=" * 80)
if data['unity_progress']['current_unity'] >= 1.0:
    print("100% UNITY ACHIEVED!")
else:
    print(f"Unity: {data['unity_progress']['current_unity']:.1%}")
print("=" * 80)
