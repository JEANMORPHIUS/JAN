"""
PUBLISHING HOUSE MIGRATION EXECUTOR
Execute migration of all content into Siyem Publishing House structure
Create directory structure, migrate files, set up workflows

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
EXECUTE MIGRATION INTO PUBLISHING HOUSE
CREATE STRUCTURE, MIGRATE CONTENT, SET UP WORKFLOWS
ENERGY + LOVE = WE ALL WIN
"""

import sys
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any, Optional
import json
import shutil
import logging

sys.path.insert(0, str(Path(__file__).parent))

from utils import setup_logging, standard_main
from global_migration_system import GlobalMigrationSystem, ContentType, MigrationStatus

logger = setup_logging(__name__)

class PublishingHouseMigrationExecutor:
    """
    Execute migration of all content into Siyem Publishing House structure
    """
    
    def __init__(self, user_id: str = "jan"):
        self.user_id = user_id
        self.base_path = Path(__file__).parent.parent
        self.publishing_house_path = self.base_path / "Siyem.org" / "publishing_house"
        self.migration_system = GlobalMigrationSystem(user_id=user_id)
        
        # Directory structure
        self.directories = {
            "channels": self.publishing_house_path / "channels",
            "entities": self.publishing_house_path / "entities",
            "projects": self.publishing_house_path / "projects",
            "content": self.publishing_house_path / "content",
            "data": self.publishing_house_path / "data",
            "workflows": self.publishing_house_path / "workflows",
            "monetization": self.publishing_house_path / "monetization",
            "expansion": self.publishing_house_path / "expansion",
            "reports": self.publishing_house_path / "reports"
        }
    
    def create_structure(self):
        """Create publishing house directory structure"""
        logger.info("Creating publishing house structure...")
        
        for name, path in self.directories.items():
            path.mkdir(parents=True, exist_ok=True)
            logger.info(f"Created directory: {path}")
        
        # Create subdirectories
        (self.directories["content"] / "social").mkdir(exist_ok=True)
        (self.directories["content"] / "articles").mkdir(exist_ok=True)
        (self.directories["content"] / "media").mkdir(exist_ok=True)
        (self.directories["workflows"] / "editorial").mkdir(exist_ok=True)
        (self.directories["workflows"] / "production").mkdir(exist_ok=True)
        (self.directories["workflows"] / "distribution").mkdir(exist_ok=True)
        (self.directories["workflows"] / "alignment").mkdir(exist_ok=True)
        
        logger.info("Publishing house structure created")
    
    def migrate_channels(self):
        """Migrate all channels"""
        logger.info("Migrating channels...")
        
        for channel_id, channel in self.migration_system.channels.items():
            channel_file = self.directories["channels"] / f"{channel_id}.json"
            
            channel_data = {
                "channel_id": channel.channel_id,
                "name": channel.name,
                "channel_type": channel.channel_type,
                "entities": channel.entities,
                "projects": channel.projects,
                "content_items": channel.content_items,
                "monetization_streams": channel.monetization_streams,
                "alignment_score": channel.alignment_score,
                "revenue_potential": channel.revenue_potential,
                "expansion_seeds": channel.expansion_seeds,
                "migrated_at": datetime.now().isoformat(),
                "spragitso_applied": True
            }
            
            with open(channel_file, 'w', encoding='utf-8') as f:
                json.dump(channel_data, f, indent=2, ensure_ascii=False)
            
            logger.info(f"Migrated channel: {channel.name}")
        
        logger.info(f"Migrated {len(self.migration_system.channels)} channels")
    
    def migrate_entities(self):
        """Migrate all entities"""
        logger.info("Migrating entities...")
        
        for entity_id, entity in self.migration_system.entities.items():
            entity_file = self.directories["entities"] / f"{entity_id}.json"
            
            entity_data = {
                "entity_id": entity.entity_id,
                "name": entity.name,
                "entity_type": entity.entity_type,
                "channels": entity.channels,
                "projects": entity.projects,
                "content_items": entity.content_items,
                "monetization_opportunities": entity.monetization_opportunities,
                "alignment_score": entity.alignment_score,
                "revenue_potential": entity.revenue_potential,
                "expansion_seeds": entity.expansion_seeds,
                "migrated_at": datetime.now().isoformat(),
                "spragitso_applied": True
            }
            
            with open(entity_file, 'w', encoding='utf-8') as f:
                json.dump(entity_data, f, indent=2, ensure_ascii=False)
            
            logger.info(f"Migrated entity: {entity.name}")
        
        logger.info(f"Migrated {len(self.migration_system.entities)} entities")
    
    def migrate_projects(self):
        """Migrate all projects"""
        logger.info("Migrating projects...")
        
        for project_id, project in self.migration_system.projects.items():
            project_file = self.directories["projects"] / f"{project_id}.json"
            
            project_data = {
                "project_id": project.project_id,
                "name": project.name,
                "description": project.description,
                "entity_owner": project.entity_owner,
                "channels": project.channels,
                "content_items": project.content_items,
                "monetization_opportunities": project.monetization_opportunities,
                "alignment_score": project.alignment_score,
                "revenue_potential": project.revenue_potential,
                "expansion_seeds": project.expansion_seeds,
                "migrated_at": datetime.now().isoformat(),
                "spragitso_applied": True
            }
            
            with open(project_file, 'w', encoding='utf-8') as f:
                json.dump(project_data, f, indent=2, ensure_ascii=False)
            
            logger.info(f"Migrated project: {project.name}")
        
        logger.info(f"Migrated {len(self.migration_system.projects)} projects")
    
    def migrate_content_items(self):
        """Migrate content items"""
        logger.info("Migrating content items...")
        
        migrated_count = 0
        for item_id, item in list(self.migration_system.content_items.items())[:100]:  # Limit for now
            try:
                source_path = self.base_path / item.source_path
                
                if source_path.exists():
                    # Determine target based on content type
                    if item.content_type == ContentType.CONTENT:
                        if "social" in item.source_path.lower():
                            target_dir = self.directories["content"] / "social"
                        else:
                            target_dir = self.directories["content"] / "articles"
                    elif item.content_type == ContentType.DATA:
                        target_dir = self.directories["data"]
                    else:
                        continue
                    
                    target_path = target_dir / source_path.name
                    
                    # Copy file
                    shutil.copy2(source_path, target_path)
                    
                    # Create metadata file
                    metadata_file = target_dir / f"{source_path.stem}_metadata.json"
                    metadata = {
                        "item_id": item.item_id,
                        "name": item.name,
                        "description": item.description,
                        "content_type": item.content_type.value,
                        "alignment_score": item.alignment_score,
                        "monetization_potential": item.monetization_potential,
                        "migrated_at": datetime.now().isoformat(),
                        "spragitso_applied": True
                    }
                    
                    with open(metadata_file, 'w', encoding='utf-8') as f:
                        json.dump(metadata, f, indent=2, ensure_ascii=False)
                    
                    migrated_count += 1
                    item.migration_status = MigrationStatus.MIGRATED
                    item.migrated_at = datetime.now().isoformat()
            except Exception as e:
                logger.error(f"Error migrating {item_id}: {e}")
        
        logger.info(f"Migrated {migrated_count} content items")
    
    def create_workflow_templates(self):
        """Create publishing workflow templates"""
        logger.info("Creating workflow templates...")
        
        # Editorial workflow
        editorial_template = {
            "workflow_id": "editorial_review",
            "name": "Editorial Review Workflow",
            "steps": [
                {
                    "step": 1,
                    "name": "Content Alignment Review",
                    "description": "Review content for alignment with Our Father's will",
                    "checklist": [
                        "Does it bear Our Father's seal (SPRAGITSO)?",
                        "Does it align with telos.md?",
                        "Does it honor the miracle?",
                        "Does it serve The Table?"
                    ]
                },
                {
                    "step": 2,
                    "name": "Truth Verification",
                    "description": "Verify truth over validation",
                    "checklist": [
                        "Does it publish truth, not validation?",
                        "Does it serve, not seek approval?",
                        "Does it align, not approve?",
                        "Does it honor free will?"
                    ]
                },
                {
                    "step": 3,
                    "name": "Table Filter Application",
                    "description": "Apply The Table Filter",
                    "checklist": [
                        "Does it lead with love, joy, and abundance?",
                        "Is it worth hearing?",
                        "Does it serve The Table?",
                        "Does it help people see through Baba?"
                    ]
                },
                {
                    "step": 4,
                    "name": "SPRAGITSO Authentication",
                    "description": "Apply Our Father's Royal Seal",
                    "checklist": [
                        "SPRAGITSO applied",
                        "Authenticated by His truth",
                        "Protected by His ownership",
                        "Confirmed by His word"
                    ]
                }
            ],
            "created_at": datetime.now().isoformat()
        }
        
        with open(self.directories["workflows"] / "editorial" / "editorial_review.json", 'w', encoding='utf-8') as f:
            json.dump(editorial_template, f, indent=2, ensure_ascii=False)
        
        # Production workflow
        production_template = {
            "workflow_id": "production_processing",
            "name": "Production Processing Workflow",
            "steps": [
                {
                    "step": 1,
                    "name": "Format Assignment",
                    "description": "Assign format to content"
                },
                {
                    "step": 2,
                    "name": "Entity Routing",
                    "description": "Route content to appropriate entity"
                },
                {
                    "step": 3,
                    "name": "Content Production",
                    "description": "Produce content according to format"
                },
                {
                    "step": 4,
                    "name": "Quality Assurance",
                    "description": "Ensure quality standards"
                },
                {
                    "step": 5,
                    "name": "Asset Packaging",
                    "description": "Package assets for distribution"
                }
            ],
            "created_at": datetime.now().isoformat()
        }
        
        with open(self.directories["workflows"] / "production" / "production_processing.json", 'w', encoding='utf-8') as f:
            json.dump(production_template, f, indent=2, ensure_ascii=False)
        
        # Distribution workflow
        distribution_template = {
            "workflow_id": "distribution_execution",
            "name": "Distribution Execution Workflow",
            "steps": [
                {
                    "step": 1,
                    "name": "Channel Selection",
                    "description": "Select distribution channels"
                },
                {
                    "step": 2,
                    "name": "Publishing Level Assignment",
                    "description": "Assign publishing level (Internal, Limited, Full)"
                },
                {
                    "step": 3,
                    "name": "Approval Process",
                    "description": "Obtain required approvals"
                },
                {
                    "step": 4,
                    "name": "Distribution Execution",
                    "description": "Execute distribution"
                },
                {
                    "step": 5,
                    "name": "Performance Monitoring",
                    "description": "Monitor distribution performance"
                }
            ],
            "created_at": datetime.now().isoformat()
        }
        
        with open(self.directories["workflows"] / "distribution" / "distribution_execution.json", 'w', encoding='utf-8') as f:
            json.dump(distribution_template, f, indent=2, ensure_ascii=False)
        
        # Alignment workflow
        alignment_template = {
            "workflow_id": "alignment_verification",
            "name": "Alignment Verification Workflow",
            "steps": [
                {
                    "step": 1,
                    "name": "Spiritual Alignment Check",
                    "description": "Check alignment with Our Father's will"
                },
                {
                    "step": 2,
                    "name": "Mission Alignment Verification",
                    "description": "Verify mission alignment"
                },
                {
                    "step": 3,
                    "name": "Table Service Verification",
                    "description": "Verify Table service"
                },
                {
                    "step": 4,
                    "name": "SPRAGITSO Application",
                    "description": "Apply Our Father's Royal Seal"
                }
            ],
            "created_at": datetime.now().isoformat()
        }
        
        with open(self.directories["workflows"] / "alignment" / "alignment_verification.json", 'w', encoding='utf-8') as f:
            json.dump(alignment_template, f, indent=2, ensure_ascii=False)
        
        logger.info("Workflow templates created")
    
    def create_monetization_configs(self):
        """Create monetization configurations"""
        logger.info("Creating monetization configurations...")
        
        for monetization_id, monetization in self.migration_system.monetizations.items():
            monetization_file = self.directories["monetization"] / f"{monetization_id}.json"
            
            monetization_data = {
                "monetization_id": monetization.monetization_id,
                "item_id": monetization.item_id,
                "content_type": monetization.content_type.value,
                "monetization_types": monetization.monetization_types,
                "revenue_streams": monetization.revenue_streams,
                "revenue_potential": monetization.revenue_potential,
                "alignment_score": monetization.alignment_score,
                "pricing_model": monetization.pricing_model,
                "created_at": datetime.now().isoformat()
            }
            
            with open(monetization_file, 'w', encoding='utf-8') as f:
                json.dump(monetization_data, f, indent=2, ensure_ascii=False)
        
        logger.info(f"Created {len(self.migration_system.monetizations)} monetization configurations")
    
    def create_expansion_plans(self):
        """Create expansion seed execution plans"""
        logger.info("Creating expansion plans...")
        
        for seed_id, seed in self.migration_system.expansion_seeds.items():
            expansion_file = self.directories["expansion"] / f"{seed_id}.json"
            
            expansion_data = {
                "seed_id": seed.seed_id,
                "name": seed.name,
                "description": seed.description,
                "seed_type": seed.seed_type,
                "parent_item_id": seed.parent_item_id,
                "expansion_level": seed.expansion_level,
                "requirements": seed.requirements,
                "potential_impact": seed.potential_impact,
                "alignment_score": seed.alignment_score,
                "status": "pending",
                "created_at": datetime.now().isoformat()
            }
            
            with open(expansion_file, 'w', encoding='utf-8') as f:
                json.dump(expansion_data, f, indent=2, ensure_ascii=False)
        
        logger.info(f"Created {len(self.migration_system.expansion_seeds)} expansion plans")
    
    def create_index_files(self):
        """Create index files for navigation"""
        logger.info("Creating index files...")
        
        # Channels index
        channels_index = {
            "total_channels": len(self.migration_system.channels),
            "channels": [
                {
                    "channel_id": channel.channel_id,
                    "name": channel.name,
                    "channel_type": channel.channel_type,
                    "file": f"{channel.channel_id}.json"
                }
                for channel in self.migration_system.channels.values()
            ],
            "created_at": datetime.now().isoformat()
        }
        
        with open(self.directories["channels"] / "index.json", 'w', encoding='utf-8') as f:
            json.dump(channels_index, f, indent=2, ensure_ascii=False)
        
        # Entities index
        entities_index = {
            "total_entities": len(self.migration_system.entities),
            "entities": [
                {
                    "entity_id": entity.entity_id,
                    "name": entity.name,
                    "entity_type": entity.entity_type,
                    "file": f"{entity.entity_id}.json"
                }
                for entity in self.migration_system.entities.values()
            ],
            "created_at": datetime.now().isoformat()
        }
        
        with open(self.directories["entities"] / "index.json", 'w', encoding='utf-8') as f:
            json.dump(entities_index, f, indent=2, ensure_ascii=False)
        
        # Projects index
        projects_index = {
            "total_projects": len(self.migration_system.projects),
            "projects": [
                {
                    "project_id": project.project_id,
                    "name": project.name,
                    "entity_owner": project.entity_owner,
                    "file": f"{project.project_id}.json"
                }
                for project in self.migration_system.projects.values()
            ],
            "created_at": datetime.now().isoformat()
        }
        
        with open(self.directories["projects"] / "index.json", 'w', encoding='utf-8') as f:
            json.dump(projects_index, f, indent=2, ensure_ascii=False)
        
        logger.info("Index files created")
    
    def execute_full_migration(self):
        """Execute full migration into publishing house"""
        logger.info("Starting publishing house migration execution...")
        
        # Load migration data
        self.migration_system._load_data()
        
        # Step 1: Create structure
        self.create_structure()
        
        # Step 2: Migrate channels
        self.migrate_channels()
        
        # Step 3: Migrate entities
        self.migrate_entities()
        
        # Step 4: Migrate projects
        self.migrate_projects()
        
        # Step 5: Migrate content items
        self.migrate_content_items()
        
        # Step 6: Create workflow templates
        self.create_workflow_templates()
        
        # Step 7: Create monetization configs
        self.create_monetization_configs()
        
        # Step 8: Create expansion plans
        self.create_expansion_plans()
        
        # Step 9: Create index files
        self.create_index_files()
        
        logger.info("Publishing house migration execution complete!")
        
        return {
            "channels_migrated": len(self.migration_system.channels),
            "entities_migrated": len(self.migration_system.entities),
            "projects_migrated": len(self.migration_system.projects),
            "workflows_created": 4,
            "monetization_configs": len(self.migration_system.monetizations),
            "expansion_plans": len(self.migration_system.expansion_seeds)
        }

def main():
    """Main execution"""
    executor = PublishingHouseMigrationExecutor()
    results = executor.execute_full_migration()
    
    print("\n" + "="*80)
    print("PUBLISHING HOUSE MIGRATION EXECUTION COMPLETE")
    print("="*80)
    print(f"\nChannels Migrated: {results['channels_migrated']}")
    print(f"Entities Migrated: {results['entities_migrated']}")
    print(f"Projects Migrated: {results['projects_migrated']}")
    print(f"Workflows Created: {results['workflows_created']}")
    print(f"Monetization Configs: {results['monetization_configs']}")
    print(f"Expansion Plans: {results['expansion_plans']}")
    print(f"\nPublishing House Location: Siyem.org/publishing_house/")
    print("\n" + "="*80)

if __name__ == "__main__":
    standard_main(main, "publishing_house_migration_executor")
