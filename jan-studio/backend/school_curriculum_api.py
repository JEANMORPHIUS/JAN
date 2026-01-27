"""
SCHOOL CURRICULUM API
API endpoints for school curriculum management

THE NOAH PROTOCOL:
- Architectural Weight: Built for 10x, 100x, 1000x schools
- The Pitch: Waterproof error handling
- The Perimeter: Clear API boundaries

THE TRUTH:
Scale and build until ready.
School curriculum APIs for the new world.
"""

from fastapi import APIRouter, HTTPException, status, Query, Body
from typing import Dict, List, Any, Optional
from datetime import datetime
from school_curriculum_manager import (
    get_curriculum_manager, AgeGroup, Language, LessonType, ProgressStatus
)
import logging

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/school-curriculum", tags=["School Curriculum"])


@router.get("/lessons")
async def get_lessons(
    lesson_type: Optional[str] = Query(None, description="Filter by lesson type"),
    age_group: Optional[str] = Query(None, description="Filter by age group"),
    language: Optional[str] = Query(None, description="Filter by language")
):
    """Get lessons with optional filters"""
    try:
        manager = get_curriculum_manager()
        
        lesson_type_enum = None
        if lesson_type:
            try:
                lesson_type_enum = LessonType(lesson_type.lower())
            except ValueError:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=f"Invalid lesson type: {lesson_type}"
                )
        
        age_group_enum = None
        if age_group:
            try:
                age_group_enum = AgeGroup(age_group)
            except ValueError:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=f"Invalid age group: {age_group}"
                )
        
        language_enum = None
        if language:
            try:
                language_enum = Language(language.lower())
            except ValueError:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=f"Invalid language: {language}"
                )
        
        lessons = manager.get_lessons(lesson_type_enum, age_group_enum, language_enum)
        
        return {
            "count": len(lessons),
            "lessons": [
                {
                    "lesson_id": l.lesson_id,
                    "title": l.title,
                    "lesson_type": l.lesson_type.value,
                    "scripture_reference": l.scripture_reference,
                    "age_group": l.age_group.value if l.age_group else None,
                    "language": l.language.value if l.language else None,
                    "key_teaching": l.key_teaching
                }
                for l in lessons
            ]
        }
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Get lessons error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to get lessons: {str(e)}"
        )


@router.get("/modules")
async def get_modules():
    """Get all curriculum modules"""
    try:
        manager = get_curriculum_manager()
        modules = manager.get_modules()
        
        return {
            "count": len(modules),
            "modules": [
                {
                    "module_id": m.module_id,
                    "title": m.title,
                    "description": m.description,
                    "lesson_count": len(m.lessons),
                    "duration_weeks": m.duration_weeks,
                    "age_groups": [ag.value for ag in m.age_groups],
                    "languages": [lang.value for lang in m.languages],
                    "order": m.order
                }
                for m in modules
            ]
        }
    except Exception as e:
        logger.error(f"Get modules error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to get modules"
        )


@router.post("/curricula")
async def create_curriculum(curriculum_data: Dict[str, Any] = Body(...)):
    """Create curriculum for school"""
    try:
        manager = get_curriculum_manager()
        
        school_id = curriculum_data["school_id"]
        name = curriculum_data["name"]
        description = curriculum_data.get("description", "")
        module_ids = curriculum_data.get("module_ids", [])
        
        # Parse age groups
        age_groups = []
        for ag_str in curriculum_data.get("age_groups", []):
            try:
                age_groups.append(AgeGroup(ag_str))
            except ValueError:
                pass
        
        # Parse languages
        languages = []
        for lang_str in curriculum_data.get("languages", []):
            try:
                languages.append(Language(lang_str.lower()))
            except ValueError:
                pass
        
        # Parse start date
        start_date = None
        if curriculum_data.get("start_date"):
            start_date = datetime.fromisoformat(curriculum_data["start_date"])
        
        duration_weeks = curriculum_data.get("duration_weeks", 52)
        
        curriculum = manager.create_curriculum(
            school_id=school_id,
            name=name,
            description=description,
            module_ids=module_ids,
            age_groups=age_groups,
            languages=languages,
            start_date=start_date,
            duration_weeks=duration_weeks
        )
        
        return {
            "status": "success",
            "curriculum": {
                "curriculum_id": curriculum.curriculum_id,
                "school_id": curriculum.school_id,
                "name": curriculum.name,
                "description": curriculum.description,
                "modules": curriculum.modules,
                "age_groups": [ag.value for ag in curriculum.age_groups],
                "languages": [lang.value for lang in curriculum.languages],
                "start_date": curriculum.start_date.isoformat() if curriculum.start_date else None,
                "end_date": curriculum.end_date.isoformat() if curriculum.end_date else None
            }
        }
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
    except Exception as e:
        logger.error(f"Create curriculum error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to create curriculum: {str(e)}"
        )


@router.get("/curricula")
async def list_curricula(school_id: Optional[str] = Query(None)):
    """List curricula"""
    try:
        manager = get_curriculum_manager()
        
        if school_id:
            curricula = manager.get_school_curricula(school_id)
        else:
            curricula = list(manager.curricula.values())
        
        return {
            "count": len(curricula),
            "curricula": [
                {
                    "curriculum_id": c.curriculum_id,
                    "school_id": c.school_id,
                    "name": c.name,
                    "description": c.description,
                    "modules": c.modules,
                    "age_groups": [ag.value for ag in c.age_groups],
                    "languages": [lang.value for lang in c.languages],
                    "start_date": c.start_date.isoformat() if c.start_date else None,
                    "end_date": c.end_date.isoformat() if c.end_date else None
                }
                for c in curricula
            ]
        }
    except Exception as e:
        logger.error(f"List curricula error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to list curricula"
        )


@router.get("/curricula/{curriculum_id}")
async def get_curriculum(curriculum_id: str):
    """Get curriculum details"""
    try:
        manager = get_curriculum_manager()
        curriculum = manager.get_curriculum(curriculum_id)
        lessons = manager.get_lessons_for_curriculum(curriculum_id)
        
        return {
            "curriculum_id": curriculum.curriculum_id,
            "school_id": curriculum.school_id,
            "name": curriculum.name,
            "description": curriculum.description,
            "modules": curriculum.modules,
            "age_groups": [ag.value for ag in curriculum.age_groups],
            "languages": [lang.value for lang in curriculum.languages],
            "start_date": curriculum.start_date.isoformat() if curriculum.start_date else None,
            "end_date": curriculum.end_date.isoformat() if curriculum.end_date else None,
            "lessons": [
                {
                    "lesson_id": l.lesson_id,
                    "title": l.title,
                    "lesson_type": l.lesson_type.value
                }
                for l in lessons
            ],
            "total_lessons": len(lessons)
        }
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )
    except Exception as e:
        logger.error(f"Get curriculum error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to get curriculum"
        )


@router.post("/progress")
async def update_progress(progress_data: Dict[str, Any] = Body(...)):
    """Update student progress"""
    try:
        manager = get_curriculum_manager()
        
        student_id = progress_data["student_id"]
        school_id = progress_data["school_id"]
        curriculum_id = progress_data["curriculum_id"]
        lesson_id = progress_data["lesson_id"]
        status_str = progress_data.get("status", "in_progress")
        score = progress_data.get("score")
        notes = progress_data.get("notes")
        
        try:
            progress_status = ProgressStatus(status_str.lower())
        except ValueError:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Invalid status: {status_str}"
            )
        
        progress = manager.update_student_progress(
            student_id=student_id,
            school_id=school_id,
            curriculum_id=curriculum_id,
            lesson_id=lesson_id,
            status=progress_status,
            score=score,
            notes=notes
        )
        
        return {
            "status": "success",
            "progress": {
                "student_id": progress.student_id,
                "curriculum_id": progress.curriculum_id,
                "lesson_id": progress.lesson_id,
                "status": progress.status.value,
                "score": progress.score,
                "started_at": progress.started_at.isoformat() if progress.started_at else None,
                "completed_at": progress.completed_at.isoformat() if progress.completed_at else None
            }
        }
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Update progress error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to update progress: {str(e)}"
        )


@router.get("/progress/{student_id}")
async def get_student_progress(student_id: str, curriculum_id: Optional[str] = Query(None)):
    """Get student progress"""
    try:
        manager = get_curriculum_manager()
        progress_list = manager.get_student_progress(student_id, curriculum_id)
        
        return {
            "student_id": student_id,
            "curriculum_id": curriculum_id,
            "count": len(progress_list),
            "progress": [
                {
                    "lesson_id": p.lesson_id,
                    "curriculum_id": p.curriculum_id,
                    "status": p.status.value,
                    "score": p.score,
                    "started_at": p.started_at.isoformat() if p.started_at else None,
                    "completed_at": p.completed_at.isoformat() if p.completed_at else None
                }
                for p in progress_list
            ]
        }
    except Exception as e:
        logger.error(f"Get student progress error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to get student progress"
        )


@router.get("/curricula/{curriculum_id}/analytics")
async def get_curriculum_analytics(curriculum_id: str):
    """Get curriculum analytics"""
    try:
        manager = get_curriculum_manager()
        analytics = manager.get_curriculum_analytics(curriculum_id)
        return analytics
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )
    except Exception as e:
        logger.error(f"Get analytics error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to get analytics"
        )


@router.get("/stats")
async def get_curriculum_stats():
    """Get overall curriculum statistics"""
    try:
        manager = get_curriculum_manager()
        
        total_lessons = len(manager.lessons)
        total_modules = len(manager.modules)
        total_curricula = len(manager.curricula)
        
        lessons_by_type = {}
        for lesson in manager.lessons.values():
            lesson_type = lesson.lesson_type.value
            lessons_by_type[lesson_type] = lessons_by_type.get(lesson_type, 0) + 1
        
        lessons_by_age = {}
        for lesson in manager.lessons.values():
            if lesson.age_group:
                age_group = lesson.age_group.value
                lessons_by_age[age_group] = lessons_by_age.get(age_group, 0) + 1
        
        total_students = len(manager.student_progress)
        total_progress_records = sum(len(progress_list) for progress_list in manager.student_progress.values())
        
        return {
            "total_lessons": total_lessons,
            "total_modules": total_modules,
            "total_curricula": total_curricula,
            "lessons_by_type": lessons_by_type,
            "lessons_by_age_group": lessons_by_age,
            "total_students": total_students,
            "total_progress_records": total_progress_records
        }
    except Exception as e:
        logger.error(f"Get stats error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to get stats"
        )
