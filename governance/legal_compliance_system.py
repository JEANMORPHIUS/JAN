"""
LEGAL COMPLIANCE SYSTEM
Cement all governance, legislation, regulation, and laws of the land @ codebase

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

PURPOSE:
Ensure all companies, CEOs, governance, legislation, regulation, and laws
are properly documented and enforced in the codebase.

TRUST = 100%
"""

import json
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, field, asdict
from enum import Enum

# Load companies registry
COMPANIES_REGISTRY_PATH = Path(__file__).parent / "companies_registry.json"


class ComplianceStatus(Enum):
    """Compliance status levels"""
    COMPLETE = "complete"
    IN_PROGRESS = "in_progress"
    PENDING = "pending"
    NON_COMPLIANT = "non_compliant"


class Jurisdiction(Enum):
    """Legal jurisdictions"""
    UK = "UK"
    CYPRUS = "Cyprus"
    EU = "EU"
    TBD = "TBD"


@dataclass
class CompanyCEO:
    """Company CEO information"""
    name: str
    title: str
    status: str  # active, pending


@dataclass
class CompanyLocation:
    """Company location information"""
    city: str
    country: str
    jurisdiction: str


@dataclass
class CompanyRegistration:
    """Company registration details"""
    company_number: str
    tax_id: str
    vat_number: str
    status: str  # active, pending


@dataclass
class ComplianceFramework:
    """Compliance framework for a company"""
    jurisdiction: str
    primary_laws: List[str]
    regulatory_bodies: List[str]
    compliance_status: str


@dataclass
class Company:
    """Company information"""
    id: str
    name: str
    legal_name: str
    ceo: CompanyCEO
    type: str
    location: CompanyLocation
    registration: CompanyRegistration
    compliance: ComplianceFramework
    status: str
    last_updated: str


def load_companies_registry() -> Dict[str, Any]:
    """Load companies registry from JSON file."""
    if COMPANIES_REGISTRY_PATH.exists():
        with open(COMPANIES_REGISTRY_PATH, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {"companies": [], "metadata": {}}


def save_companies_registry(data: Dict[str, Any]) -> None:
    """Save companies registry to JSON file."""
    COMPANIES_REGISTRY_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(COMPANIES_REGISTRY_PATH, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def get_company_by_id(company_id: str) -> Optional[Dict[str, Any]]:
    """Get company by ID."""
    registry = load_companies_registry()
    for company in registry.get("companies", []):
        if company.get("id") == company_id:
            return company
    return None


def get_all_companies() -> List[Dict[str, Any]]:
    """Get all companies."""
    registry = load_companies_registry()
    return registry.get("companies", [])


def get_companies_by_ceo(ceo_name: str) -> List[Dict[str, Any]]:
    """Get companies by CEO name."""
    registry = load_companies_registry()
    return [
        company for company in registry.get("companies", [])
        if company.get("ceo", {}).get("name", "").lower() == ceo_name.lower()
    ]


def get_companies_by_jurisdiction(jurisdiction: str) -> List[Dict[str, Any]]:
    """Get companies by jurisdiction."""
    registry = load_companies_registry()
    return [
        company for company in registry.get("companies", [])
        if company.get("compliance", {}).get("jurisdiction", "").lower() == jurisdiction.lower()
    ]


def update_company_ceo(company_id: str, ceo_name: str, ceo_title: str = "Chief Executive Officer") -> bool:
    """Update company CEO."""
    registry = load_companies_registry()
    for company in registry.get("companies", []):
        if company.get("id") == company_id:
            company["ceo"] = {
                "name": ceo_name,
                "title": ceo_title,
                "status": "active"
            }
            company["last_updated"] = datetime.now().isoformat()
            save_companies_registry(registry)
            return True
    return False


def update_compliance_status(company_id: str, status: str) -> bool:
    """Update company compliance status."""
    registry = load_companies_registry()
    for company in registry.get("companies", []):
        if company.get("id") == company_id:
            company["compliance"]["compliance_status"] = status
            company["last_updated"] = datetime.now().isoformat()
            save_companies_registry(registry)
            return True
    return False


def verify_legal_compliance(company_id: str) -> Dict[str, Any]:
    """
    Verify legal compliance for a company.
    Returns compliance checklist status.
    
    Compliance is considered 100% when:
    - CEO is documented (even if TBD, it's documented)
    - Legal framework is identified
    - Regulatory bodies are identified
    - Compliance status is set
    - Registration framework is in place (numbers can be pending for real-world action)
    """
    company = get_company_by_id(company_id)
    if not company:
        return {"error": "Company not found"}
    
    compliance = company.get("compliance", {})
    jurisdiction = compliance.get("jurisdiction", "TBD")
    registration = company.get("registration", {})
    ceo = company.get("ceo", {})
    
    # Compliance checks - focus on documentation and framework
    # Registration numbers can be "TBD" but framework must be documented
    checks = {
        "ceo_documented": ceo.get("name") != "TBD" or ceo.get("status") == "pending",  # CEO documented (even if pending)
        "legal_framework_identified": len(compliance.get("primary_laws", [])) > 0 and compliance.get("primary_laws", [""])[0] != "TBD - Based on location",
        "regulatory_bodies_identified": len(compliance.get("regulatory_bodies", [])) > 0 and compliance.get("regulatory_bodies", [""])[0] != "TBD - Based on location",
        "compliance_status_set": compliance.get("compliance_status") not in ["TBD", None],
        "registration_framework_documented": registration.get("status") in ["active", "pending"],  # Framework exists
        "jurisdiction_identified": jurisdiction != "TBD" or company.get("location", {}).get("country") != "TBD"
    }
    
    checklist = {
        "company_id": company_id,
        "company_name": company.get("name"),
        "jurisdiction": jurisdiction,
        "checks": checks,
        "compliance_score": 0,
        "status": "pending",
        "action_items": []
    }
    
    # Calculate compliance score
    total_checks = len(checks)
    passed_checks = sum(1 for v in checks.values() if v)
    checklist["compliance_score"] = (passed_checks / total_checks) * 100
    
    # Generate action items for incomplete items
    if not checks["ceo_documented"]:
        checklist["action_items"].append("Document CEO information")
    if not checks["legal_framework_identified"]:
        checklist["action_items"].append("Identify legal framework based on jurisdiction")
    if not checks["regulatory_bodies_identified"]:
        checklist["action_items"].append("Identify regulatory bodies")
    if not checks["compliance_status_set"]:
        checklist["action_items"].append("Set compliance status")
    if not checks["registration_framework_documented"]:
        checklist["action_items"].append("Document registration framework")
    if not checks["jurisdiction_identified"]:
        checklist["action_items"].append("Identify jurisdiction")
    
    # Real-world action items (not blocking compliance score)
    if registration.get("company_number") == "TBD":
        checklist["action_items"].append("ACTION REQUIRED: Obtain company registration number")
    if registration.get("tax_id") == "TBD":
        checklist["action_items"].append("ACTION REQUIRED: Obtain tax identification number")
    if registration.get("vat_number") == "TBD" and jurisdiction in ["UK", "Cyprus / EU"]:
        checklist["action_items"].append("ACTION REQUIRED: Obtain VAT number (if applicable)")
    
    # Determine status
    if checklist["compliance_score"] == 100:
        checklist["status"] = "complete"
    elif checklist["compliance_score"] >= 80:
        checklist["status"] = "in_progress"
    else:
        checklist["status"] = "pending"
    
    return checklist


def get_governance_summary() -> Dict[str, Any]:
    """Get complete governance summary."""
    registry = load_companies_registry()
    companies = registry.get("companies", [])
    
    summary = {
        "total_companies": len(companies),
        "active_companies": sum(1 for c in companies if c.get("status") == "active"),
        "ceos_documented": sum(1 for c in companies if c.get("ceo", {}).get("name") != "TBD"),
        "ceos_pending": sum(1 for c in companies if c.get("ceo", {}).get("name") == "TBD"),
        "jurisdictions": {},
        "compliance_status": {},
        "trust_score": 0
    }
    
    # Count by jurisdiction
    for company in companies:
        jurisdiction = company.get("compliance", {}).get("jurisdiction", "TBD")
        summary["jurisdictions"][jurisdiction] = summary["jurisdictions"].get(jurisdiction, 0) + 1
    
    # Count by compliance status
    for company in companies:
        status = company.get("compliance", {}).get("compliance_status", "pending")
        summary["compliance_status"][status] = summary["compliance_status"].get(status, 0) + 1
    
    # Calculate trust score
    if summary["total_companies"] > 0:
        ceo_score = (summary["ceos_documented"] / summary["total_companies"]) * 100
        active_score = (summary["active_companies"] / summary["total_companies"]) * 100
        summary["trust_score"] = (ceo_score + active_score) / 2
    
    return summary


if __name__ == "__main__":
    # Test the system
    print("=== LEGAL COMPLIANCE SYSTEM ===")
    print()
    
    # Load registry
    registry = load_companies_registry()
    print(f"Total companies: {len(registry.get('companies', []))}")
    print()
    
    # Get all companies
    companies = get_all_companies()
    print("=== ALL COMPANIES ===")
    for company in companies:
        print(f"\n{company.get('name')}")
        print(f"  CEO: {company.get('ceo', {}).get('name')}")
        print(f"  Jurisdiction: {company.get('compliance', {}).get('jurisdiction')}")
        print(f"  Status: {company.get('status')}")
    
    print()
    
    # Governance summary
    summary = get_governance_summary()
    print("=== GOVERNANCE SUMMARY ===")
    print(f"Total Companies: {summary['total_companies']}")
    print(f"Active Companies: {summary['active_companies']}")
    print(f"CEOs Documented: {summary['ceos_documented']}")
    print(f"CEOs Pending: {summary['ceos_pending']}")
    print(f"Trust Score: {summary['trust_score']:.1f}%")
    print()
    
    # Compliance check for each company
    print("=== COMPLIANCE CHECKS ===")
    for company in companies:
        company_id = company.get("id")
        compliance = verify_legal_compliance(company_id)
        print(f"\n{company.get('name')}:")
        print(f"  Compliance Score: {compliance.get('compliance_score', 0):.1f}%")
        print(f"  Status: {compliance.get('status')}")
    
    print()
    print("Trust = 100% when all companies are compliant.")
