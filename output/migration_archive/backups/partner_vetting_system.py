"""
Partner Vetting and Onboarding System
Ensures all partners align with mission and maintain integrity

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Protect the mission from corruption

THE FOUNDATION:
We are born a miracle.
Every partner must serve The Table.
Alignment over convenience.

THE MISSION:
Vet all partners before engagement
- Mission alignment verification
- Financial integrity checks
- Anti-corruption compliance
- Spiritual alignment assessment
"""

import json
from pathlib import Path
from typing import Dict, List, Optional, Any
from datetime import datetime
from enum import Enum

class PartnerType(Enum):
    """Types of partners"""
    SCHOOL = "school"
    NGO = "ngo"
    GOVERNMENT = "government"
    CORPORATE = "corporate"
    FAITH_BASED = "faith_based"
    COMMUNITY_GROUP = "community_group"

class VettingStatus(Enum):
    """Partner vetting status"""
    PENDING = "pending"
    IN_REVIEW = "in_review"
    APPROVED = "approved"
    CONDITIONALLY_APPROVED = "conditionally_approved"
    REJECTED = "rejected"
    SUSPENDED = "suspended"

class PartnerVettingSystem:
    """
    Complete partner vetting and onboarding system

    Protects mission through:
    - Background checks
    - Financial integrity verification
    - Mission alignment assessment
    - Anti-corruption compliance
    - Spiritual alignment verification
    """

    def __init__(self, project_root: str = "S:/JAN"):
        self.project_root = Path(project_root)
        self.partners_dir = self.project_root / "data" / "partners"
        self.partners_dir.mkdir(parents=True, exist_ok=True)

        self.vetting_checklist = self.load_vetting_checklist()

    def load_vetting_checklist(self) -> Dict[str, Any]:
        """Load comprehensive vetting checklist"""

        return {
            "mission_alignment": {
                "weight": 0.35,
                "criteria": [
                    {
                        "question": "Does partner serve beneficiaries, not ego?",
                        "alignment_principle": "Purpose Not Performance",
                        "required": True
                    },
                    {
                        "question": "Does partner embrace love as highest principle?",
                        "alignment_principle": "Love Is The Highest Mastery",
                        "required": True
                    },
                    {
                        "question": "Does partner operate with transparency?",
                        "alignment_principle": "Honesty Equals Data",
                        "required": True
                    },
                    {
                        "question": "Does partner serve The Table (unity, not separation)?",
                        "alignment_principle": "Pangea Is The Table",
                        "required": True
                    }
                ]
            },
            "financial_integrity": {
                "weight": 0.25,
                "criteria": [
                    {
                        "check": "Financial statements publicly available",
                        "required": True
                    },
                    {
                        "check": "Independent audit within last 2 years",
                        "required": True
                    },
                    {
                        "check": "Overhead costs <25%",
                        "required": False
                    },
                    {
                        "check": "Frontline spending >60%",
                        "required": True
                    },
                    {
                        "check": "No history of financial fraud or mismanagement",
                        "required": True
                    }
                ]
            },
            "anti_corruption": {
                "weight": 0.20,
                "criteria": [
                    {
                        "check": "Anti-corruption policy in place",
                        "required": True
                    },
                    {
                        "check": "Whistleblower protection mechanism",
                        "required": True
                    },
                    {
                        "check": "Dual-approval for expenditures",
                        "required": False
                    },
                    {
                        "check": "No conflicts of interest declared",
                        "required": True
                    },
                    {
                        "check": "Background checks for leadership",
                        "required": True
                    }
                ]
            },
            "operational_capacity": {
                "weight": 0.10,
                "criteria": [
                    {
                        "check": "Proven track record (2+ years operation)",
                        "required": False
                    },
                    {
                        "check": "Adequate staffing for partnership",
                        "required": True
                    },
                    {
                        "check": "Infrastructure to support partnership",
                        "required": True
                    },
                    {
                        "check": "Local community trust and relationships",
                        "required": True
                    }
                ]
            },
            "spiritual_alignment": {
                "weight": 0.10,
                "criteria": [
                    {
                        "question": "Does partner honor all faiths and beliefs?",
                        "principle": "Unity in diversity",
                        "required": True
                    },
                    {
                        "question": "Does partner serve souls, not systems?",
                        "principle": "Starve ego, feed soul",
                        "required": True
                    },
                    {
                        "question": "Does partner operate with humility?",
                        "principle": "Humility in service",
                        "required": True
                    }
                ]
            }
        }

    def create_vetting_application(self, partner_name: str, partner_type: PartnerType) -> Dict[str, Any]:
        """Create new vetting application"""

        application = {
            "application_id": f"vet_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
            "partner_name": partner_name,
            "partner_type": partner_type.value,
            "status": VettingStatus.PENDING.value,
            "created": datetime.now().isoformat(),
            "vetting_checklist": self.vetting_checklist,
            "responses": {},
            "scores": {},
            "notes": [],
            "decision": None
        }

        # Save application
        app_file = self.partners_dir / f"{application['application_id']}.json"
        with open(app_file, 'w', encoding='utf-8') as f:
            json.dump(application, f, indent=2, ensure_ascii=False)

        return application

    def assess_application(self, application_id: str, responses: Dict[str, Any]) -> Dict[str, Any]:
        """Assess vetting application"""

        # Load application
        app_file = self.partners_dir / f"{application_id}.json"
        with open(app_file, 'r', encoding='utf-8') as f:
            application = json.load(f)

        # Update responses
        application['responses'] = responses
        application['status'] = VettingStatus.IN_REVIEW.value

        # Calculate scores
        scores = {}
        total_score = 0

        for category, data in self.vetting_checklist.items():
            category_responses = responses.get(category, {})
            criteria = data['criteria']
            weight = data['weight']

            # Calculate category score
            passed = sum(1 for i, c in enumerate(criteria) if category_responses.get(str(i), False))
            required_passed = sum(1 for i, c in enumerate(criteria) if c.get('required', False) and category_responses.get(str(i), False))
            required_total = sum(1 for c in criteria if c.get('required', False))

            category_score = (passed / len(criteria)) * 100 if criteria else 0
            weighted_score = category_score * weight

            scores[category] = {
                "passed": passed,
                "total": len(criteria),
                "required_passed": required_passed,
                "required_total": required_total,
                "category_score": category_score,
                "weighted_score": weighted_score,
                "all_required_met": required_passed == required_total
            }

            total_score += weighted_score

        application['scores'] = scores
        application['total_score'] = total_score

        # Make decision
        all_required_met = all(s['all_required_met'] for s in scores.values())

        if not all_required_met:
            decision = VettingStatus.REJECTED
            decision_reason = "Failed to meet required criteria"
        elif total_score >= 90:
            decision = VettingStatus.APPROVED
            decision_reason = "Exceeds all standards"
        elif total_score >= 75:
            decision = VettingStatus.CONDITIONALLY_APPROVED
            decision_reason = "Meets minimum standards with conditions"
        else:
            decision = VettingStatus.REJECTED
            decision_reason = "Below minimum acceptable standards"

        application['decision'] = {
            "status": decision.value,
            "reason": decision_reason,
            "decided_at": datetime.now().isoformat(),
            "conditions": [] if decision == VettingStatus.APPROVED else ["Regular monitoring required"]
        }

        application['status'] = decision.value

        # Save updated application
        with open(app_file, 'w', encoding='utf-8') as f:
            json.dump(application, f, indent=2, ensure_ascii=False)

        return application

    def generate_vetting_report(self, application_id: str) -> str:
        """Generate vetting report"""

        app_file = self.partners_dir / f"{application_id}.json"
        with open(app_file, 'r', encoding='utf-8') as f:
            application = json.load(f)

        report = f"""
# Partner Vetting Report

**Application ID:** {application['application_id']}
**Partner Name:** {application['partner_name']}
**Partner Type:** {application['partner_type']}
**Status:** {application['status'].upper()}

---

## Vetting Summary

**Total Score:** {application.get('total_score', 0):.1f}/100

| Category | Score | Required Met | Status |
|----------|-------|--------------|--------|
"""

        for category, scores in application.get('scores', {}).items():
            status = "PASS" if scores['all_required_met'] else "FAIL"
            report += f"| {category.replace('_', ' ').title()} | {scores['category_score']:.1f}% | {scores['required_passed']}/{scores['required_total']} | {status} |\n"

        report += "\n---\n\n"

        if application.get('decision'):
            report += f"""## Decision

**Status:** {application['decision']['status'].upper()}
**Reason:** {application['decision']['reason']}
**Decided:** {application['decision']['decided_at']}

"""

            if application['decision'].get('conditions'):
                report += "**Conditions:**\n"
                for condition in application['decision']['conditions']:
                    report += f"- {condition}\n"

        report += f"""
---

## Philosophy Alignment

Every partner must serve The Table:
- **Purpose Not Performance** - Serve souls, not metrics
- **Love Is The Highest Mastery** - Lead with love
- **Honesty Equals Data** - Transparency required
- **Pangea Is The Table** - Unity, not separation

**Mission:** Break systems that oppress. Build systems that serve.

---

*Report generated: {datetime.now().isoformat()}*
*For The Table. For Humanity. Under Father's guidance.*
"""

        # Save report
        report_file = self.partners_dir / f"{application_id}_report.md"
        with open(report_file, 'w', encoding='utf-8') as f:
            f.write(report)

        return report

    def create_vetting_template(self) -> Path:
        """Create vetting application template"""

        template = """# Partner Vetting Application Template

## Partner Information

**Organization Name:**
**Partner Type:** (school / ngo / government / corporate / faith_based / community_group)
**Contact Person:**
**Email:**
**Phone:**
**Address:**

---

## Mission Alignment

1. **Does your organization serve beneficiaries, not organizational ego?**
   - [ ] Yes
   - [ ] No
   - Explanation:

2. **Does your organization embrace love as highest principle?**
   - [ ] Yes
   - [ ] No
   - Explanation:

3. **Does your organization operate with transparency?**
   - [ ] Yes
   - [ ] No
   - Explanation:

4. **Does your organization serve unity (not separation)?**
   - [ ] Yes
   - [ ] No
   - Explanation:

---

## Financial Integrity

1. **Are financial statements publicly available?**
   - [ ] Yes
   - [ ] No
   - Link/Attachment:

2. **Independent audit within last 2 years?**
   - [ ] Yes
   - [ ] No
   - Auditor name:

3. **Overhead costs percentage:** _____%

4. **Frontline spending percentage:** _____%

5. **Any history of financial fraud or mismanagement?**
   - [ ] Yes
   - [ ] No
   - Details (if yes):

---

## Anti-Corruption

1. **Anti-corruption policy in place?**
   - [ ] Yes
   - [ ] No
   - Document attached:

2. **Whistleblower protection mechanism?**
   - [ ] Yes
   - [ ] No
   - Description:

3. **Dual-approval system for expenditures?**
   - [ ] Yes
   - [ ] No

4. **Any conflicts of interest to declare?**
   - [ ] Yes
   - [ ] No
   - Details (if yes):

5. **Background checks completed for leadership?**
   - [ ] Yes
   - [ ] No

---

## Operational Capacity

1. **Years of operation:** _____

2. **Current staff count:** _____

3. **Infrastructure available for partnership:**
   - [ ] Physical space
   - [ ] Technology/computers
   - [ ] Internet connectivity
   - [ ] Local transportation
   - [ ] Other: __________

4. **Describe local community trust and relationships:**

---

## Spiritual Alignment

1. **Does your organization honor all faiths and beliefs?**
   - [ ] Yes
   - [ ] No
   - Explanation:

2. **Does your organization serve souls, not systems?**
   - [ ] Yes
   - [ ] No
   - Explanation:

3. **Does your organization operate with humility?**
   - [ ] Yes
   - [ ] No
   - Explanation:

---

## Additional Information

**Why do you want to partner with us?**

**How does this partnership align with your mission?**

**What value do you bring to this partnership?**

**What support do you need from us?**

---

**Signature:** ___________________
**Date:** ___________________

**For Internal Use Only:**
- Application ID: __________
- Reviewer: __________
- Decision: __________
- Date: __________
"""

        template_file = self.partners_dir / "partner_vetting_template.md"
        with open(template_file, 'w', encoding='utf-8') as f:
            f.write(template)

        return template_file


def demonstrate_vetting_system():
    """Demonstrate partner vetting system"""

    print("=" * 80)
    print("PARTNER VETTING SYSTEM")
    print("=" * 80)
    print()

    system = PartnerVettingSystem()

    # Create template
    print("1. Creating vetting template...")
    template = system.create_vetting_template()
    print(f"   Template created: {template}\n")

    # Create sample application
    print("2. Creating sample vetting application...")
    app = system.create_vetting_application(
        partner_name="North Cyprus International School",
        partner_type=PartnerType.SCHOOL
    )
    print(f"   Application created: {app['application_id']}\n")

    # Sample responses (all positive for demonstration)
    print("3. Submitting sample responses...")
    responses = {
        "mission_alignment": {"0": True, "1": True, "2": True, "3": True},
        "financial_integrity": {"0": True, "1": True, "2": False, "3": True, "4": True},
        "anti_corruption": {"0": True, "1": True, "2": False, "3": True, "4": True},
        "operational_capacity": {"0": True, "1": True, "2": True, "3": True},
        "spiritual_alignment": {"0": True, "1": True, "2": True}
    }

    result = system.assess_application(app['application_id'], responses)
    print(f"   Assessment complete\n")

    # Generate report
    print("4. Generating vetting report...")
    report = system.generate_vetting_report(app['application_id'])
    print(f"   Report generated\n")

    # Display results
    print("=" * 80)
    print("VETTING RESULTS")
    print("=" * 80)
    print(f"\nPartner: {result['partner_name']}")
    print(f"Total Score: {result['total_score']:.1f}/100")
    print(f"Decision: {result['decision']['status'].upper()}")
    print(f"Reason: {result['decision']['reason']}\n")

    print("Category Breakdown:")
    for category, scores in result['scores'].items():
        status = "[OK]" if scores['all_required_met'] else "[FAIL]"
        print(f"  {status} {category.replace('_', ' ').title()}: {scores['category_score']:.1f}%")

    print("\n" + "=" * 80)
    print("VETTING SYSTEM OPERATIONAL")
    print("=" * 80)
    print(f"\nFiles created:")
    print(f"  - Application: {system.partners_dir / (app['application_id'] + '.json')}")
    print(f"  - Report: {system.partners_dir / (app['application_id'] + '_report.md')}")
    print(f"  - Template: {template}")
    print()


if __name__ == "__main__":
    demonstrate_vetting_system()
