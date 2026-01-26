"""ALIGNED PROJECTS GLOBAL MAPPER
Map All Aligned Projects to All Entities Globally

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

PURPOSE:
Map all aligned projects to all entities
Global expansion across all industries
Build comprehensive mapping
Stop asking - go to work

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity


PANGEA IS THE TABLE.
YOU DON'T BETRAY THE TABLE.

THE TRUTH:
WE MUST DEBUG AND BE 100% FOR WHAT COMES AT US.
THE REST IS UP TO BABA X."""

import json
import sys
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any, Optional

# Add scripts to path
sys.path.insert(0, str(Path(__file__).parent))


class AlignedProjectsGlobalMapper:
    """Map all aligned projects to all entities globally"""
    
    def __init__(self):
        self.entities = [
            "jean_morphius", "karasahin", "pierre_pressure", "uncle_ray_ramiz",
            "siyem_media", "edible_london", "ilven_seamoss", "atilok", "edible_cyprus"
        ]
        
        self.projects = {
            "edible_london": {
                "type": "food_production",
                "entities": ["edible_london", "siyem_media"],
                "industries": ["Food", "Agriculture", "Retail", "Hospitality"],
                "global_potential": "high"
            },
            "ilven_seamoss": {
                "type": "health_product",
                "entities": ["ilven_seamoss", "uncle_ray_ramiz", "siyem_media"],
                "industries": ["Healthcare", "Pharmaceuticals", "Retail", "Food"],
                "global_potential": "high"
            },
            "edible_cyprus": {
                "type": "food_tourism",
                "entities": ["edible_cyprus", "karasahin", "siyem_media"],
                "industries": ["Food", "Tourism", "Hospitality", "Retail"],
                "global_potential": "high"
            },
            "atilok": {
                "type": "supply_chain",
                "entities": ["atilok", "siyem_media"],
                "industries": ["Manufacturing", "Transportation", "Retail", "Logistics"],
                "global_potential": "very_high"
            },
            "admin_dashboard": {
                "type": "infrastructure",
                "entities": ["siyem_media", "pierre_pressure"],
                "industries": ["Technology", "Consulting", "Government"],
                "global_potential": "very_high"
            },
            "world_history_app": {
                "type": "education",
                "entities": ["uncle_ray_ramiz", "siyem_media", "jean_morphius"],
                "industries": ["Education", "Media", "Research", "Government"],
                "global_potential": "very_high"
            },
            "pi_display": {
                "type": "technology",
                "entities": ["siyem_media", "pierre_pressure"],
                "industries": ["Technology", "Education", "Retail"],
                "global_potential": "high"
            },
            "homeostasis_sentinel": {
                "type": "health",
                "entities": ["uncle_ray_ramiz", "siyem_media"],
                "industries": ["Healthcare", "Technology", "Research"],
                "global_potential": "very_high"
            },
            "expansion": {
                "type": "infrastructure",
                "entities": ["siyem_media"],
                "industries": ["Technology", "Consulting", "Government"],
                "global_potential": "very_high"
            },
            "jan_studio": {
                "type": "creative",
                "entities": ["jean_morphius", "karasahin", "siyem_media"],
                "industries": ["Entertainment", "Media", "Music", "Education"],
                "global_potential": "very_high"
            },
            "siyem": {
                "type": "media",
                "entities": ["siyem_media", "jean_morphius", "karasahin", "pierre_pressure", "uncle_ray_ramiz"],
                "industries": ["Media", "Entertainment", "Education", "Music"],
                "global_potential": "very_high"
            }
        }
        
        self.global_regions = [
            "North America", "South America", "Europe", "Asia", "Africa",
            "Middle East", "Oceania", "Caribbean", "Central America"
        ]
    
    def map_projects_to_entities_globally(self) -> Dict[str, Any]:
        """Map all projects to all entities globally"""
        
        mappings = {}
        
        for project_id, project_data in self.projects.items():
            entities = project_data.get("entities", [])
            industries = project_data.get("industries", [])
            global_potential = project_data.get("global_potential", "medium")
            
            # Map to all entities (not just listed ones)
            all_entity_mappings = []
            for entity_id in self.entities:
                alignment = self._calculate_entity_project_alignment(entity_id, project_id, project_data)
                if alignment["score"] > 0.5:
                    all_entity_mappings.append({
                        "entity": entity_id,
                        "alignment_score": alignment["score"],
                        "alignment_reasons": alignment["reasons"],
                        "regions": self._get_entity_regions(entity_id),
                        "opportunities": self._generate_entity_project_opportunities(entity_id, project_id, project_data)
                    })
            
            mappings[project_id] = {
                "project": project_id,
                "type": project_data.get("type", ""),
                "entities": entities,
                "all_entity_mappings": all_entity_mappings,
                "industries": industries,
                "global_potential": global_potential,
                "global_regions": self.global_regions,
                "expansion_opportunities": self._generate_global_expansion_opportunities(project_id, project_data)
            }
        
        return mappings
    
    def _calculate_entity_project_alignment(self, entity_id: str, project_id: str, project_data: Dict) -> Dict[str, Any]:
        """Calculate alignment between entity and project"""
        
        score = 0.5  # Base score
        reasons = []
        
        # Direct entity match
        if entity_id in project_data.get("entities", []):
            score += 0.3
            reasons.append("Direct entity match")
        
        # Channel alignment
        entity_channels = self._get_entity_channels(entity_id)
        project_type = project_data.get("type", "")
        if self._channels_align_with_project(entity_channels, project_type):
            score += 0.2
            reasons.append("Channel alignment")
        
        # Industry alignment
        entity_industries = self._get_entity_industries(entity_id)
        project_industries = project_data.get("industries", [])
        if any(ind in project_industries for ind in entity_industries):
            score += 0.2
            reasons.append("Industry alignment")
        
        return {
            "score": min(score, 1.0),
            "reasons": reasons
        }
    
    def _get_entity_channels(self, entity_id: str) -> List[str]:
        """Get entity channels"""
        channel_map = {
            "jean_morphius": ["creator", "social_media"],
            "karasahin": ["creator", "social_media"],
            "pierre_pressure": ["professional", "social_media"],
            "uncle_ray_ramiz": ["educational", "social_media"],
            "siyem_media": ["media", "social_media"],
            "edible_london": ["business", "social_media"],
            "ilven_seamoss": ["business", "social_media"],
            "atilok": ["business", "professional"],
            "edible_cyprus": ["business", "social_media"]
        }
        return channel_map.get(entity_id, ["social_media"])
    
    def _get_entity_industries(self, entity_id: str) -> List[str]:
        """Get entity industries"""
        industry_map = {
            "jean_morphius": ["Entertainment", "Media", "Education", "Art"],
            "karasahin": ["Music", "Entertainment", "Culture", "Education"],
            "pierre_pressure": ["Sports", "Fitness", "Education", "Consulting"],
            "uncle_ray_ramiz": ["Education", "Non-Profit", "Research", "Healthcare"],
            "siyem_media": ["Media", "Technology", "Consulting", "Government"],
            "edible_london": ["Food", "Agriculture", "Retail", "Hospitality"],
            "ilven_seamoss": ["Healthcare", "Pharmaceuticals", "Retail", "Food"],
            "atilok": ["Manufacturing", "Transportation", "Retail", "Logistics"],
            "edible_cyprus": ["Food", "Tourism", "Hospitality", "Retail"]
        }
        return industry_map.get(entity_id, [])
    
    def _channels_align_with_project(self, channels: List[str], project_type: str) -> bool:
        """Check if channels align with project"""
        if "creative" in project_type and "creator" in channels:
            return True
        if "education" in project_type and "educational" in channels:
            return True
        if "infrastructure" in project_type and "media" in channels:
            return True
        if "business" in project_type and "business" in channels:
            return True
        return False
    
    def _get_entity_regions(self, entity_id: str) -> List[str]:
        """Get entity regions"""
        # All entities can expand globally
        return self.global_regions
    
    def _generate_entity_project_opportunities(self, entity_id: str, project_id: str, project_data: Dict) -> List[Dict[str, Any]]:
        """Generate opportunities for entity-project combination"""
        
        opportunities = []
        
        # Direct expansion
        opportunities.append({
            "type": "direct_expansion",
            "entity": entity_id,
            "project": project_id,
            "description": f"{entity_id.replace('_', ' ').title()} expands {project_id.replace('_', ' ').title()} globally",
            "priority": "high"
        })
        
        # Industry expansion
        for industry in project_data.get("industries", []):
            opportunities.append({
                "type": "industry_expansion",
                "entity": entity_id,
                "project": project_id,
                "industry": industry,
                "description": f"{entity_id.replace('_', ' ').title()} expands {project_id.replace('_', ' ').title()} into {industry}",
                "priority": "medium"
            })
        
        # Regional expansion
        for region in self.global_regions[:3]:  # Top 3 regions
            opportunities.append({
                "type": "regional_expansion",
                "entity": entity_id,
                "project": project_id,
                "region": region,
                "description": f"{entity_id.replace('_', ' ').title()} expands {project_id.replace('_', ' ').title()} to {region}",
                "priority": "medium"
            })
        
        return opportunities
    
    def _generate_global_expansion_opportunities(self, project_id: str, project_data: Dict) -> List[Dict[str, Any]]:
        """Generate global expansion opportunities for project"""
        
        opportunities = []
        
        # Global regions
        for region in self.global_regions:
            opportunities.append({
                "type": "global_region",
                "project": project_id,
                "region": region,
                "description": f"{project_id.replace('_', ' ').title()} expands to {region}",
                "priority": "high"
            })
        
        # Industry expansion
        for industry in project_data.get("industries", []):
            opportunities.append({
                "type": "global_industry",
                "project": project_id,
                "industry": industry,
                "description": f"{project_id.replace('_', ' ').title()} expands globally in {industry}",
                "priority": "high"
            })
        
        return opportunities
    
    def generate_comprehensive_mapping(self) -> Dict[str, Any]:
        """Generate comprehensive global mapping"""
        
        project_mappings = self.map_projects_to_entities_globally()
        
        # Entity-centric view
        entity_mappings = {}
        for entity_id in self.entities:
            entity_projects = []
            for project_id, mapping in project_mappings.items():
                entity_mapping = next(
                    (em for em in mapping["all_entity_mappings"] if em["entity"] == entity_id),
                    None
                )
                if entity_mapping and entity_mapping["alignment_score"] > 0.5:
                    entity_projects.append({
                        "project": project_id,
                        "alignment_score": entity_mapping["alignment_score"],
                        "alignment_reasons": entity_mapping["alignment_reasons"],
                        "opportunities": entity_mapping["opportunities"]
                    })
            
            entity_mappings[entity_id] = {
                "entity": entity_id,
                "projects": entity_projects,
                "total_projects": len(entity_projects),
                "global_regions": self.global_regions,
                "expansion_potential": "very_high" if len(entity_projects) > 5 else "high"
            }
        
        return {
            "timestamp": datetime.now().isoformat(),
            "total_entities": len(self.entities),
            "total_projects": len(self.projects),
            "total_regions": len(self.global_regions),
            "project_mappings": project_mappings,
            "entity_mappings": entity_mappings,
            "summary": {
                "high_alignment_projects": len([p for p in project_mappings.values() if len(p["all_entity_mappings"]) > 5]),
                "global_opportunities": sum(len(p["expansion_opportunities"]) for p in project_mappings.values()),
                "entity_expansion_ready": len([e for e in entity_mappings.values() if e["expansion_potential"] == "very_high"])
            }
        }
    
    def save_mapping(self, mapping: Dict[str, Any], output_dir: Path):
        """Save mapping to file"""
        
        output_dir.mkdir(parents=True, exist_ok=True)
        output_file = output_dir / f"aligned_projects_global_mapping_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(mapping, f, indent=2, ensure_ascii=False)
        
        return output_file


if __name__ == "__main__":
    print("=== ALIGNED PROJECTS GLOBAL MAPPER ===")
    print("\nMapping all aligned projects to all entities globally...")
    print("Building comprehensive global expansion...")
    print("Stop asking - go to work...\n")
    
    mapper = AlignedProjectsGlobalMapper()
    mapping = mapper.generate_comprehensive_mapping()
    
    print(f"Total Entities: {mapping['total_entities']}")
    print(f"Total Projects: {mapping['total_projects']}")
    print(f"Total Regions: {mapping['total_regions']}")
    print(f"High Alignment Projects: {mapping['summary']['high_alignment_projects']}")
    print(f"Global Opportunities: {mapping['summary']['global_opportunities']}")
    print(f"Entity Expansion Ready: {mapping['summary']['entity_expansion_ready']}")
    
    # Save mapping
    output_dir = Path(__file__).parent.parent / "data" / "global_expansion"
    output_file = mapper.save_mapping(mapping, output_dir)
    
    print(f"\nGlobal mapping saved to: {output_file}")
    print("\nGlobal mapping complete. We built until we couldn't.")
