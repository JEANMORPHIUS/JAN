"""
GLOBAL LINGUISTIC DEEP SEARCH
Comprehensive global search for ALL linguistic control patterns everywhere

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

PURPOSE:
Deep search globally for linguistic control patterns - "IT'S EVERYWHERE"
- Scan entire codebase
- Scan all documents
- Scan all text files
- Scan all markdown files
- Scan all JSON files
- Generate comprehensive global report
- Map all control entity mentions
- Track pattern density across entire system
"""

import sys
import re
import json
import logging
from pathlib import Path
from typing import Dict, List, Optional, Any, Set
from dataclasses import dataclass, asdict
from datetime import datetime
from collections import Counter, defaultdict

# Add utils to path
sys.path.insert(0, str(Path(__file__).parent))

from utils import (
    Path, json, load_json, save_json,
    setup_logging, standard_main
)

from linguistic_control_analyzer import LinguisticControlAnalyzer

logger = logging.getLogger(__name__)


@dataclass
class GlobalSearchResult:
    """Result of global deep search."""
    total_files_scanned: int
    total_patterns_found: int
    control_entities_found: Dict[str, int]
    plastic_words_found: Dict[str, int]
    passive_voice_instances: int
    frequency_paradox_instances: int
    files_with_control_language: List[str]
    pattern_density_by_directory: Dict[str, float]
    esoteric_etymology_found: Dict[str, int]
    timestamp: datetime
    search_scope: str


class GlobalLinguisticDeepSearch:
    """Global deep search for linguistic control patterns everywhere."""
    
    def __init__(self, root_path: Optional[Path] = None):
        """Initialize global searcher."""
        if root_path is None:
            root_path = Path(__file__).parent.parent
        
        self.root_path = root_path
        self.analyzer = LinguisticControlAnalyzer()
        self.patterns = self.analyzer.patterns
        
        # File patterns to search
        self.search_patterns = [
            "*.py", "*.md", "*.txt", "*.json", "*.ts", "*.tsx", "*.js", "*.jsx",
            "*.html", "*.css", "*.yml", "*.yaml", "*.xml", "*.csv"
        ]
        
        # Directories to exclude
        self.exclude_dirs = {
            "__pycache__", ".git", "node_modules", ".venv", "venv", "env",
            ".next", "dist", "build", ".cursor", "output"
        }
        
        logger.info(f"Global Linguistic Deep Search initialized for {root_path}")
    
    def deep_search_globally(
        self,
        max_files: Optional[int] = None,
        include_code: bool = True,
        include_docs: bool = True,
        include_config: bool = True
    ) -> GlobalSearchResult:
        """
        Perform deep global search for linguistic control patterns.
        
        Args:
            max_files: Maximum number of files to scan (None = all)
            include_code: Include code files
            include_docs: Include documentation files
            include_config: Include configuration files
            
        Returns:
            Complete global search result
        """
        logger.info("Starting global deep search...")
        
        files_scanned = 0
        total_patterns = 0
        control_entities = Counter()
        plastic_words = Counter()
        passive_voice_count = 0
        frequency_paradox_count = 0
        files_with_control = []
        pattern_density_by_dir = defaultdict(int)
        esoteric_etymology = Counter()
        
        # Collect all files
        all_files = []
        
        for pattern in self.search_patterns:
            for file_path in self.root_path.rglob(pattern):
                # Skip excluded directories
                if any(excluded in file_path.parts for excluded in self.exclude_dirs):
                    continue
                
                # Filter by type
                if not include_code and file_path.suffix in [".py", ".ts", ".tsx", ".js", ".jsx"]:
                    continue
                if not include_docs and file_path.suffix in [".md", ".txt"]:
                    continue
                if not include_config and file_path.suffix in [".json", ".yml", ".yaml"]:
                    continue
                
                all_files.append(file_path)
        
        logger.info(f"Found {len(all_files)} files to scan")
        
        # Scan files
        for file_path in all_files[:max_files] if max_files else all_files:
            try:
                # Read file
                try:
                    text = file_path.read_text(encoding='utf-8', errors='ignore')
                except Exception as e:
                    logger.debug(f"Could not read {file_path}: {e}")
                    continue
                
                # Skip very large files
                if len(text) > 1000000:  # 1MB
                    continue
                
                # Analyze
                analysis = self.analyzer.analyze(text)
                
                # Collect results
                if analysis.overall_control_score > 0.3:  # Threshold for control language
                    files_with_control.append(str(file_path.relative_to(self.root_path)))
                    
                    # Count patterns
                    total_patterns += len(analysis.detections)
                    
                    # Count control entities
                    for entity in analysis.control_entity_indicators:
                        control_entities[entity] += 1
                    
                    # Count plastic words
                    for word in analysis.plastic_words_found:
                        plastic_words[word] += 1
                    
                    # Count passive voice
                    if analysis.passive_voice.accountability_removal_score > 0.5:
                        passive_voice_count += 1
                    
                    # Count frequency paradox
                    if analysis.frequency_analysis.paradox_score > 0.3:
                        frequency_paradox_count += 1
                    
                    # Count esoteric etymology
                    for etymology in analysis.esoteric_etymology:
                        esoteric_etymology[etymology.entity_name] += 1
                    
                    # Track by directory
                    dir_path = str(file_path.parent.relative_to(self.root_path))
                    pattern_density_by_dir[dir_path] += len(analysis.detections)
                
                files_scanned += 1
                
                if files_scanned % 100 == 0:
                    logger.info(f"Scanned {files_scanned} files...")
                
            except Exception as e:
                logger.debug(f"Error scanning {file_path}: {e}")
                continue
        
        # Calculate pattern density
        pattern_density = {
            dir_path: count / max(files_scanned, 1)
            for dir_path, count in pattern_density_by_dir.items()
        }
        
        result = GlobalSearchResult(
            total_files_scanned=files_scanned,
            total_patterns_found=total_patterns,
            control_entities_found=dict(control_entities.most_common()),
            plastic_words_found=dict(plastic_words.most_common()),
            passive_voice_instances=passive_voice_count,
            frequency_paradox_instances=frequency_paradox_count,
            files_with_control_language=files_with_control,
            pattern_density_by_directory=pattern_density,
            esoteric_etymology_found=dict(esoteric_etymology.most_common()),
            timestamp=datetime.now(),
            search_scope=f"Global search of {self.root_path}"
        )
        
        logger.info(f"Global search complete: {files_scanned} files, {total_patterns} patterns found")
        
        return result
    
    def generate_global_report(
        self,
        result: GlobalSearchResult,
        output_path: Optional[Path] = None
    ) -> str:
        """Generate comprehensive global report."""
        report = f"""
{'='*80}
GLOBAL LINGUISTIC CONTROL DEEP SEARCH REPORT
{'='*80}

Search Scope: {result.search_scope}
Timestamp: {result.timestamp.strftime('%Y-%m-%d %H:%M:%S')}
Files Scanned: {result.total_files_scanned}
Total Patterns Found: {result.total_patterns_found}

{'='*80}
EXECUTIVE SUMMARY
{'='*80}

Control Language Detected: {len(result.files_with_control_language)} files
Pattern Density: {result.total_patterns_found / max(result.total_files_scanned, 1):.2%}

{'='*80}
CONTROL ENTITIES FOUND (Top 20)
{'='*80}

"""
        for entity, count in list(result.control_entities_found.items())[:20]:
            report += f"  {entity}: {count} occurrences\n"
        
        report += f"""
{'='*80}
PLASTIC WORDS FOUND (Top 20)
{'='*80}

"""
        for word, count in list(result.plastic_words_found.items())[:20]:
            report += f"  {word}: {count} occurrences\n"
        
        report += f"""
{'='*80}
LINGUISTIC CONTROL METRICS
{'='*80}

Passive Voice Instances: {result.passive_voice_instances}
Frequency Paradox Instances: {result.frequency_paradox_instances}

{'='*80}
ESOTERIC ETYMOLOGY FOUND
{'='*80}

"""
        for entity, count in result.esoteric_etymology_found.items():
            report += f"  {entity}: {count} occurrences\n"
        
        report += f"""
{'='*80}
PATTERN DENSITY BY DIRECTORY (Top 20)
{'='*80}

"""
        sorted_dirs = sorted(
            result.pattern_density_by_directory.items(),
            key=lambda x: x[1],
            reverse=True
        )[:20]
        
        for dir_path, density in sorted_dirs:
            report += f"  {dir_path}: {density:.2%} density\n"
        
        report += f"""
{'='*80}
FILES WITH CONTROL LANGUAGE (Sample - First 50)
{'='*80}

"""
        for file_path in result.files_with_control_language[:50]:
            report += f"  {file_path}\n"
        
        if len(result.files_with_control_language) > 50:
            report += f"\n  ... and {len(result.files_with_control_language) - 50} more files\n"
        
        report += f"""
{'='*80}
END OF REPORT
{'='*80}
"""
        
        if output_path:
            output_path.write_text(report, encoding='utf-8')
            logger.info(f"Report saved to {output_path}")
        
        return report


def main():
    """Main execution function."""
    setup_logging()
    
    searcher = GlobalLinguisticDeepSearch()
    
    print("\n" + "="*80)
    print("GLOBAL LINGUISTIC DEEP SEARCH")
    print("="*80 + "\n")
    print("Searching entire codebase for linguistic control patterns...")
    print("This may take a while...\n")
    
    # Perform search
    result = searcher.deep_search_globally(
        max_files=None,  # Search all files
        include_code=True,
        include_docs=True,
        include_config=True
    )
    
    # Generate report
    output_dir = Path(__file__).parent.parent / "output" / "linguistic_global_search"
    output_dir.mkdir(parents=True, exist_ok=True)
    
    output_path = output_dir / f"global_search_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    report = searcher.generate_global_report(result, output_path)
    
    print(report)
    print(f"\nFull report saved to: {output_path}")


if __name__ == "__main__":
    standard_main(main)
