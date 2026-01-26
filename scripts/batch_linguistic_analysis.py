"""BATCH LINGUISTIC ANALYSIS
Batch process multiple documents for linguistic control analysis

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

PURPOSE:
Batch process multiple documents/files for linguistic analysis:
- Analyze entire directories
- Generate comparative reports
- Create antidote versions
- Export results to JSON/CSV

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity


PANGEA IS THE TABLE.
YOU DON'T BETRAY THE TABLE.

THE TRUTH:
WE MUST DEBUG AND BE 100% FOR WHAT COMES AT US.
THE REST IS UP TO BABA X."""

import sys
import json
import csv
import logging
from pathlib import Path
from typing import Dict, List, Optional, Any
from dataclasses import asdict
from datetime import datetime

# Add utils to path
sys.path.insert(0, str(Path(__file__).parent))

from utils import (
    Path, json, load_json, save_json,
    setup_logging, standard_main
)

from linguistic_control_analyzer import LinguisticControlAnalyzer
from antidote_language_generator import AntidoteLanguageGenerator
from document_decoder import DocumentDecoder

logger = logging.getLogger(__name__)


class BatchLinguisticAnalysis:
    """Batch process documents for linguistic analysis."""
    
    def __init__(self):
        """Initialize batch processor."""
        self.analyzer = LinguisticControlAnalyzer()
        self.generator = AntidoteLanguageGenerator()
        self.decoder = DocumentDecoder()
        logger.info("Batch Linguistic Analysis initialized")
    
    def process_directory(
        self,
        directory: Path,
        output_dir: Optional[Path] = None,
        file_pattern: str = "*.txt",
        generate_antidotes: bool = True
    ) -> List[Dict[str, Any]]:
        """
        Process all files in a directory.
        
        Args:
            directory: Directory containing files to process
            output_dir: Directory to save results
            file_pattern: File pattern to match
            generate_antidotes: Whether to generate antidote versions
            
        Returns:
            List of analysis results
        """
        logger.info(f"Processing directory: {directory}")
        
        if not directory.exists():
            logger.error(f"Directory does not exist: {directory}")
            return []
        
        files = list(directory.glob(file_pattern))
        logger.info(f"Found {len(files)} files to process")
        
        results = []
        
        for file_path in files:
            try:
                logger.info(f"Processing: {file_path.name}")
                
                # Read file
                text = file_path.read_text(encoding='utf-8')
                
                # Analyze
                analysis = self.analyzer.analyze(text)
                
                # Generate antidote if requested
                antidote = None
                if generate_antidotes:
                    antidote = self.generator.generate(
                        text,
                        target_language="bilingual",
                        cultural_context="turkish_english"
                    )
                
                # Build result
                result = {
                    "file_name": file_path.name,
                    "file_path": str(file_path),
                    "text_length": len(text),
                    "control_score": analysis.overall_control_score,
                    "authenticity_score": analysis.authenticity_score,
                    "duygu_score": analysis.duygu_analysis.duygu_score,
                    "plastic_words_count": len(analysis.plastic_words_found),
                    "passive_voice_score": analysis.passive_voice.accountability_removal_score,
                    "frequency_paradox_score": analysis.frequency_analysis.paradox_score,
                    "control_entities": analysis.control_entity_indicators,
                    "detections_count": len(analysis.detections),
                    "antidote_resistance_score": antidote.resistance_score if antidote else None,
                    "timestamp": datetime.now().isoformat()
                }
                
                results.append(result)
                
                # Save individual result if output_dir specified
                if output_dir:
                    self._save_individual_result(
                        file_path.name,
                        analysis,
                        antidote,
                        output_dir
                    )
                
            except Exception as e:
                logger.error(f"Error processing {file_path.name}: {str(e)}", exc_info=True)
                results.append({
                    "file_name": file_path.name,
                    "error": str(e),
                    "timestamp": datetime.now().isoformat()
                })
        
        # Save batch summary
        if output_dir:
            self._save_batch_summary(results, output_dir)
        
        return results
    
    def _save_individual_result(
        self,
        file_name: str,
        analysis: Any,
        antidote: Optional[Any],
        output_dir: Path
    ):
        """Save individual analysis result."""
        output_dir.mkdir(parents=True, exist_ok=True)
        
        # Save analysis JSON
        analysis_file = output_dir / f"{Path(file_name).stem}_analysis.json"
        analysis_data = {
            "control_score": analysis.overall_control_score,
            "authenticity_score": analysis.authenticity_score,
            "duygu_score": analysis.duygu_analysis.duygu_score,
            "plastic_words": analysis.plastic_words_found,
            "detections": [
                {
                    "type": d.detection_type,
                    "pattern": d.pattern_found,
                    "severity": d.severity,
                    "explanation": d.explanation
                }
                for d in analysis.detections
            ],
            "antidote_suggestions": analysis.antidote_suggestions
        }
        
        save_json(analysis_data, analysis_file)
        
        # Save antidote if available
        if antidote:
            antidote_file = output_dir / f"{Path(file_name).stem}_antidote.txt"
            antidote_file.write_text(antidote.antidote_text, encoding='utf-8')
    
    def _save_batch_summary(self, results: List[Dict[str, Any]], output_dir: Path):
        """Save batch summary report."""
        output_dir.mkdir(parents=True, exist_ok=True)
        
        # Save JSON summary
        summary_file = output_dir / "batch_summary.json"
        save_json(results, summary_file)
        
        # Save CSV summary
        csv_file = output_dir / "batch_summary.csv"
        if results:
            fieldnames = list(results[0].keys())
            with open(csv_file, 'w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                for result in results:
                    # Flatten nested structures for CSV
                    row = {}
                    for key, value in result.items():
                        if isinstance(value, list):
                            row[key] = ', '.join(str(v) for v in value)
                        else:
                            row[key] = value
                    writer.writerow(row)
        
        logger.info(f"Batch summary saved to {output_dir}")
    
    def compare_documents(
        self,
        documents: List[Dict[str, str]],
        output_path: Optional[Path] = None
    ) -> Dict[str, Any]:
        """
        Compare multiple documents.
        
        Args:
            documents: List of {"name": "...", "text": "..."}
            output_path: Path to save comparison report
            
        Returns:
            Comparison results
        """
        logger.info(f"Comparing {len(documents)} documents")
        
        analyses = []
        
        for doc in documents:
            analysis = self.analyzer.analyze(doc["text"])
            analyses.append({
                "name": doc["name"],
                "analysis": analysis
            })
        
        # Build comparison
        comparison = {
            "timestamp": datetime.now().isoformat(),
            "documents": []
        }
        
        for item in analyses:
            comparison["documents"].append({
                "name": item["name"],
                "control_score": item["analysis"].overall_control_score,
                "authenticity_score": item["analysis"].authenticity_score,
                "duygu_score": item["analysis"].duygu_analysis.duygu_score,
                "plastic_words_count": len(item["analysis"].plastic_words_found),
                "passive_voice_score": item["analysis"].passive_voice.accountability_removal_score
            })
        
        # Calculate averages
        if analyses:
            comparison["averages"] = {
                "control_score": sum(a["analysis"].overall_control_score for a in analyses) / len(analyses),
                "authenticity_score": sum(a["analysis"].authenticity_score for a in analyses) / len(analyses),
                "duygu_score": sum(a["analysis"].duygu_analysis.duygu_score for a in analyses) / len(analyses)
            }
        
        if output_path:
            save_json(comparison, output_path)
            logger.info(f"Comparison saved to {output_path}")
        
        return comparison


def main():
    """Main execution function."""
    setup_logging()
    
    batch_processor = BatchLinguisticAnalysis()
    
    # Example: Process a directory
    example_dir = Path(__file__).parent.parent / "docs"
    output_dir = Path(__file__).parent.parent / "output" / "linguistic_batch"
    
    if example_dir.exists():
        results = batch_processor.process_directory(
            example_dir,
            output_dir=output_dir,
            file_pattern="*.md",
            generate_antidotes=True
        )
        
        print(f"\nProcessed {len(results)} files")
        print(f"Results saved to {output_dir}")
    else:
        print(f"Example directory not found: {example_dir}")


if __name__ == "__main__":
    standard_main(main)
