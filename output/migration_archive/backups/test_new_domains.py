#!/usr/bin/env python3
"""Test new Deep Search domains"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from scripts.deep_search_frequency_opportunities import DeepSearchFrequencyOpportunities, OpportunityDomain

searcher = DeepSearchFrequencyOpportunities()

print("Testing New Domains:")
print("=" * 80)

# Test Immigration Services
opps = searcher.search_domain(OpportunityDomain.IMMIGRATION_SERVICES)
print(f"\nImmigration Services: {len(opps)} opportunities")
if opps:
    print(f"  Top: {opps[0].title}")
    print(f"  Frequency: {opps[0].frequency_score:.2f}")

# Test Foreign Investment Analysis
opps = searcher.search_domain(OpportunityDomain.FOREIGN_INVESTMENT_ANALYSIS)
print(f"\nForeign Investment Analysis: {len(opps)} opportunities")
if opps:
    print(f"  Top: {opps[0].title}")
    print(f"  Frequency: {opps[0].frequency_score:.2f}")

# Test Philanthropic Finance
opps = searcher.search_domain(OpportunityDomain.PHILANTHROPIC_FINANCE)
print(f"\nPhilanthropic Finance: {len(opps)} opportunities")
if opps:
    print(f"  Top: {opps[0].title}")
    print(f"  Frequency: {opps[0].frequency_score:.2f}")

# Test Enhanced Agriculture
opps = searcher.search_domain(OpportunityDomain.AGRICULTURE)
print(f"\nAgriculture (Enhanced): {len(opps)} opportunities")
if opps:
    print(f"  Top: {opps[0].title}")
    print(f"  Frequency: {opps[0].frequency_score:.2f}")

print("\n" + "=" * 80)
print("All new domains operational!")
