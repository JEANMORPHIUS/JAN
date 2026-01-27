"""
SCHOOL CURRICULUM MANAGER
Complete curriculum management for schools

THE NOAH PROTOCOL:
- Architectural Weight: Built for 10x, 100x, 1000x schools
- The Pitch: Waterproof error handling
- The Perimeter: Clear curriculum boundaries

THE ARRIVAL PROTOCOL:
- Pre-Commissioning Scan: Can this handle 1000x schools?
- Frequency Anchor: Curriculum from "done" - production ready

THE TRUTH:
Scale and build until ready.
School curriculum management for the new world.
"""

from typing import Dict, List, Any, Optional
from datetime import datetime, timedelta
from enum import Enum
from dataclasses import dataclass, field
from pathlib import Path
import json
import logging

logger = logging.getLogger(__name__)


class AgeGroup(Enum):
    """Age groups"""
    AGES_5_7 = "5-7"
    AGES_8_10 = "8-10"
    AGES_11_13 = "11-13"
    AGES_14_16 = "14-16"


class Language(Enum):
    """Languages"""
    ENGLISH = "en"
    TURKISH = "tr"
    BILINGUAL = "bilingual"


class LessonType(Enum):
    """Lesson types"""
    LAW = "law"  # 40 Laws
    KEY = "key"  # 7 Divine Keys
    SCRIPTURE = "scripture"
    ACTIVITY = "activity"
    ASSESSMENT = "assessment"


class ProgressStatus(Enum):
    """Progress status"""
    NOT_STARTED = "not_started"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    ASSESSED = "assessed"


@dataclass
class Lesson:
    """Lesson"""
    lesson_id: str
    title: str
    lesson_type: LessonType
    scripture_reference: Optional[str] = None
    content: Optional[str] = None
    age_group: Optional[AgeGroup] = None
    language: Optional[Language] = None
    key_teaching: Optional[str] = None
    practical_application: Optional[str] = None
    reflection_question: Optional[str] = None
    visual_prompt: Optional[str] = None
    audio_script: Optional[str] = None
    scheduled_time: Optional[datetime] = None
    created: Optional[datetime] = None


@dataclass
class Module:
    """Curriculum module"""
    module_id: str
    title: str
    description: str
    lessons: List[str] = field(default_factory=list)  # Lesson IDs
    order: int = 0
    duration_weeks: int = 1
    age_groups: List[AgeGroup] = field(default_factory=list)
    languages: List[Language] = field(default_factory=list)


@dataclass
class Curriculum:
    """School curriculum"""
    curriculum_id: str
    school_id: str
    name: str
    description: str
    modules: List[str] = field(default_factory=list)  # Module IDs
    age_groups: List[AgeGroup] = field(default_factory=list)
    languages: List[Language] = field(default_factory=list)
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)


@dataclass
class StudentProgress:
    """Student progress"""
    student_id: str
    school_id: str
    curriculum_id: str
    lesson_id: str
    status: ProgressStatus = ProgressStatus.NOT_STARTED
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    score: Optional[float] = None
    notes: Optional[str] = None
    updated_at: datetime = field(default_factory=datetime.now)


class SchoolCurriculumManager:
    """
    School Curriculum Manager
    Manages curriculum, lessons, modules, and student progress
    
    THE NOAH PROTOCOL:
    - Architectural Weight: Built for 10x, 100x, 1000x schools
    - The Pitch: Waterproof error handling
    - The Perimeter: Clear curriculum boundaries
    
    THE ARRIVAL PROTOCOL:
    - Pre-Commissioning Scan: Can this handle 1000x schools?
    - Frequency Anchor: Curriculum from "done" - production ready
    
    SYSTEM WIDE ALIGNMENT:
    - Integrated with Education Professional Deployment
    - Integrated with Monitoring System
    - Integrated with Performance Optimizer
    - Integrated with Channel Collaboration
    """
    
    def __init__(self, curriculum_path: Optional[Path] = None):
        """Initialize curriculum manager"""
        if curriculum_path is None:
            curriculum_path = Path(__file__).parent.parent.parent / "curriculum" / "scripture_schedule_2026"
        
        self.curriculum_path = Path(curriculum_path)
        self.lessons: Dict[str, Lesson] = {}
        self.modules: Dict[str, Module] = {}
        self.curricula: Dict[str, Curriculum] = {}
        self.student_progress: Dict[str, List[StudentProgress]] = {}  # student_id -> progress list
        
        self._load_lessons()
        self._initialize_default_modules()
        self._integrate_with_systems()
        
        logger.info(f"School Curriculum Manager initialized: {len(self.lessons)} lessons loaded")
    
    def _integrate_with_systems(self):
        """Integrate with other systems (System Wide Alignment)"""
        try:
            # Integrate with Education Professional Deployment
            from education_professional_deployment_api import get_education_manager
            self.education_manager = get_education_manager()
            logger.info("Curriculum integrated with Education Professional Deployment")
        except Exception as e:
            logger.warning(f"Could not integrate with Education Professional Deployment: {e}")
            self.education_manager = None
        
        try:
            # Integrate with Monitoring
            from monitoring_enhancements import get_monitoring
            self.monitoring = get_monitoring()
            logger.info("Curriculum integrated with Monitoring System")
        except Exception as e:
            logger.warning(f"Could not integrate with Monitoring: {e}")
            self.monitoring = None
        
        try:
            # Integrate with Performance Optimizer
            from performance_optimizer import get_optimizer
            self.optimizer = get_optimizer()
            logger.info("Curriculum integrated with Performance Optimizer")
        except Exception as e:
            logger.warning(f"Could not integrate with Performance Optimizer: {e}")
            self.optimizer = None
    
    def _load_lessons(self):
        """Load lessons from curriculum directory"""
        if not self.curriculum_path.exists():
            logger.warning(f"Curriculum path not found: {self.curriculum_path}")
            return
        
        lesson_files = list(self.curriculum_path.glob("lesson_*.json"))
        logger.info(f"Found {len(lesson_files)} lesson files")
        
        for lesson_file in lesson_files:
            try:
                with open(lesson_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                
                lesson_id = data.get("lesson_id") or lesson_file.stem
                
                # Determine lesson type
                lesson_type = LessonType.SCRIPTURE
                if "law" in lesson_id.lower() or "law" in data.get("title", "").lower():
                    lesson_type = LessonType.LAW
                elif "key" in lesson_id.lower() or "key" in data.get("title", "").lower():
                    lesson_type = LessonType.KEY
                
                # Parse age group
                age_group = None
                age_str = data.get("age_group")
                if age_str:
                    try:
                        age_group = AgeGroup(age_str)
                    except ValueError:
                        pass
                
                # Parse language
                language = None
                lang_str = data.get("language")
                if lang_str:
                    try:
                        language = Language(lang_str)
                    except ValueError:
                        pass
                
                lesson = Lesson(
                    lesson_id=lesson_id,
                    title=data.get("title", ""),
                    lesson_type=lesson_type,
                    scripture_reference=data.get("scripture_reference"),
                    content=data.get("content"),
                    age_group=age_group,
                    language=language,
                    key_teaching=data.get("key_teaching"),
                    practical_application=data.get("practical_application"),
                    reflection_question=data.get("reflection_question"),
                    visual_prompt=data.get("visual_prompt"),
                    audio_script=data.get("audio_script"),
                    scheduled_time=datetime.fromisoformat(data["scheduled_time"]) if data.get("scheduled_time") else None,
                    created=datetime.fromisoformat(data["created"]) if data.get("created") else None
                )
                
                self.lessons[lesson_id] = lesson
            except Exception as e:
                logger.error(f"Error loading lesson {lesson_file}: {e}")
    
    def _initialize_default_modules(self):
        """Initialize default curriculum modules"""
        # Module 1: The 40 Laws - Volume 1: Loyalty (Laws 1-10)
        law_lessons_1_10 = [l for l in self.lessons.values() if l.lesson_type == LessonType.LAW and "001" <= l.lesson_id.split("_")[-1] <= "010"]
        if law_lessons_1_10:
            self.modules["module_loyalty"] = Module(
                module_id="module_loyalty",
                title="Volume 1: Loyalty (Laws 1-10)",
                description="The foundation of loyalty and commitment",
                lessons=[l.lesson_id for l in law_lessons_1_10[:10]],
                order=1,
                duration_weeks=10,
                age_groups=[AgeGroup.AGES_8_10, AgeGroup.AGES_11_13, AgeGroup.AGES_14_16],
                languages=[Language.ENGLISH, Language.TURKISH]
            )
        
        # Module 2: The 7 Divine Keys
        key_lessons = [l for l in self.lessons.values() if l.lesson_type == LessonType.KEY]
        if key_lessons:
            self.modules["module_divine_keys"] = Module(
                module_id="module_divine_keys",
                title="The 7 Divine Keys",
                description="The seven keys to consciousness and transformation",
                lessons=[l.lesson_id for l in key_lessons[:7]],
                order=2,
                duration_weeks=7,
                age_groups=[AgeGroup.AGES_11_13, AgeGroup.AGES_14_16],
                languages=[Language.ENGLISH, Language.TURKISH]
            )
    
    def create_curriculum(self, school_id: str, name: str, description: str,
                         module_ids: List[str], age_groups: List[AgeGroup],
                         languages: List[Language], start_date: Optional[datetime] = None,
                         duration_weeks: int = 52) -> Curriculum:
        """Create curriculum for school"""
        curriculum_id = f"curriculum_{school_id}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
        # Validate modules
        for module_id in module_ids:
            if module_id not in self.modules:
                raise ValueError(f"Module not found: {module_id}")
        
        if start_date is None:
            start_date = datetime.now()
        
        end_date = start_date + timedelta(weeks=duration_weeks)
        
        curriculum = Curriculum(
            curriculum_id=curriculum_id,
            school_id=school_id,
            name=name,
            description=description,
            modules=module_ids,
            age_groups=age_groups,
            languages=languages,
            start_date=start_date,
            end_date=end_date
        )
        
        self.curricula[curriculum_id] = curriculum
        return curriculum
    
    def get_curriculum(self, curriculum_id: str) -> Curriculum:
        """Get curriculum"""
        if curriculum_id not in self.curricula:
            raise ValueError(f"Curriculum not found: {curriculum_id}")
        return self.curricula[curriculum_id]
    
    def get_school_curricula(self, school_id: str) -> List[Curriculum]:
        """Get all curricula for a school"""
        return [c for c in self.curricula.values() if c.school_id == school_id]
    
    def get_lessons_for_curriculum(self, curriculum_id: str) -> List[Lesson]:
        """Get all lessons for a curriculum"""
        curriculum = self.get_curriculum(curriculum_id)
        lesson_ids = set()
        
        for module_id in curriculum.modules:
            if module_id in self.modules:
                module = self.modules[module_id]
                lesson_ids.update(module.lessons)
        
        return [self.lessons[lesson_id] for lesson_id in lesson_ids if lesson_id in self.lessons]
    
    def update_student_progress(self, student_id: str, school_id: str,
                               curriculum_id: str, lesson_id: str,
                               status: ProgressStatus, score: Optional[float] = None,
                               notes: Optional[str] = None) -> StudentProgress:
        """Update student progress"""
        if student_id not in self.student_progress:
            self.student_progress[student_id] = []
        
        # Find existing progress or create new
        progress_list = self.student_progress[student_id]
        existing = next((p for p in progress_list if p.lesson_id == lesson_id and p.curriculum_id == curriculum_id), None)
        
        if existing:
            existing.status = status
            existing.score = score
            existing.notes = notes
            existing.updated_at = datetime.now()
            
            if status == ProgressStatus.IN_PROGRESS and not existing.started_at:
                existing.started_at = datetime.now()
            if status in [ProgressStatus.COMPLETED, ProgressStatus.ASSESSED]:
                existing.completed_at = datetime.now()
            
            return existing
        else:
            progress = StudentProgress(
                student_id=student_id,
                school_id=school_id,
                curriculum_id=curriculum_id,
                lesson_id=lesson_id,
                status=status,
                score=score,
                notes=notes,
                started_at=datetime.now() if status != ProgressStatus.NOT_STARTED else None
            )
            progress_list.append(progress)
            return progress
    
    def get_student_progress(self, student_id: str, curriculum_id: Optional[str] = None) -> List[StudentProgress]:
        """Get student progress"""
        if student_id not in self.student_progress:
            return []
        
        progress_list = self.student_progress[student_id]
        if curriculum_id:
            progress_list = [p for p in progress_list if p.curriculum_id == curriculum_id]
        
        return progress_list
    
    def get_curriculum_analytics(self, curriculum_id: str) -> Dict[str, Any]:
        """Get curriculum analytics"""
        curriculum = self.get_curriculum(curriculum_id)
        lessons = self.get_lessons_for_curriculum(curriculum_id)
        
        # Get all student progress for this curriculum
        all_progress = []
        for student_id, progress_list in self.student_progress.items():
            curriculum_progress = [p for p in progress_list if p.curriculum_id == curriculum_id]
            all_progress.extend(curriculum_progress)
        
        # Calculate statistics
        total_lessons = len(lessons)
        total_students = len(set(p.student_id for p in all_progress))
        
        completed_count = len([p for p in all_progress if p.status == ProgressStatus.COMPLETED])
        in_progress_count = len([p for p in all_progress if p.status == ProgressStatus.IN_PROGRESS])
        not_started_count = len([p for p in all_progress if p.status == ProgressStatus.NOT_STARTED])
        
        avg_score = None
        scores = [p.score for p in all_progress if p.score is not None]
        if scores:
            avg_score = sum(scores) / len(scores)
        
        # System-wide integration: Send metrics to monitoring
        if hasattr(self, 'monitoring') and self.monitoring:
            try:
                self.monitoring.add_metric("curriculum_completion_rate", 
                    (completed_count / (total_lessons * total_students)) * 100 if (total_lessons * total_students) > 0 else 0)
                self.monitoring.add_metric("curriculum_avg_score", avg_score if avg_score else 0)
                self.monitoring.add_metric("curriculum_total_students", total_students)
            except Exception as e:
                logger.warning(f"Could not send metrics to monitoring: {e}")
        
        return {
            "curriculum_id": curriculum_id,
            "curriculum_name": curriculum.name,
            "total_lessons": total_lessons,
            "total_students": total_students,
            "progress": {
                "completed": completed_count,
                "in_progress": in_progress_count,
                "not_started": not_started_count
            },
            "average_score": avg_score,
            "completion_rate": (completed_count / (total_lessons * total_students)) * 100 if (total_lessons * total_students) > 0 else 0
        }
    
    def get_modules(self) -> List[Module]:
        """Get all modules"""
        return list(self.modules.values())
    
    def get_lessons(self, lesson_type: Optional[LessonType] = None,
                   age_group: Optional[AgeGroup] = None,
                   language: Optional[Language] = None) -> List[Lesson]:
        """Get lessons with filters"""
        lessons = list(self.lessons.values())
        
        if lesson_type:
            lessons = [l for l in lessons if l.lesson_type == lesson_type]
        
        if age_group:
            lessons = [l for l in lessons if l.age_group == age_group]
        
        if language:
            lessons = [l for l in lessons if l.language == language]
        
        return lessons


# Global manager instance
_manager: Optional[SchoolCurriculumManager] = None


def get_curriculum_manager() -> SchoolCurriculumManager:
    """Get global curriculum manager"""
    global _manager
    if _manager is None:
        _manager = SchoolCurriculumManager()
    return _manager
