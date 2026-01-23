"""
AI Orchestrator - Intelligent dispatcher for Claude Code and Gemini
Part of JAN Expansion Protocol
Version: 1.0 Genesis
Date: 2026-01-15

This module intelligently routes tasks to the appropriate AI assistant:
- Claude Code: Technical depth, architecture, complex analysis
- Gemini: Creative bursts, rapid ideation, content variation
"""

import sys
import os
from typing import Dict, List, Optional, Any
from enum import Enum
from dataclasses import dataclass
import json

# Add scripts directory to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'scripts'))

from claude_assistant import generate_with_claude, create_marketing_strategy, analyze_competitors
from gemini_assistant import generate_content, generate_social_post, generate_blog_outline


class AIAssistant(Enum):
    """Available AI assistants"""
    CLAUDE_CODE = "claude_code"
    GEMINI = "gemini"
    BOTH = "both"  # Hybrid workflow
    NONE = "none"  # No AI assistance needed


class TaskType(Enum):
    """Types of tasks that can be routed"""
    # Technical tasks (→ Claude Code)
    ARCHITECTURE_DESIGN = "architecture_design"
    ALGORITHM_OPTIMIZATION = "algorithm_optimization"
    CODE_REVIEW = "code_review"
    DEBUGGING = "debugging"
    TECHNICAL_DOCUMENTATION = "technical_documentation"
    API_DESIGN = "api_design"
    
    # Creative tasks (→ Gemini)
    SOCIAL_CONTENT = "social_content"
    BLOG_OUTLINE = "blog_outline"
    MARKETING_COPY = "marketing_copy"
    CONTENT_VARIATION = "content_variation"
    RAPID_IDEATION = "rapid_ideation"
    
    # Hybrid tasks (→ Both)
    CASE_STUDY = "case_study"
    COMPREHENSIVE_STRATEGY = "comprehensive_strategy"
    CONTENT_WITH_STRUCTURE = "content_with_structure"
    
    # Analysis tasks (→ Claude Code)
    CORRELATION_ANALYSIS = "correlation_analysis"
    PERFORMANCE_ANALYSIS = "performance_analysis"
    DATA_INTERPRETATION = "data_interpretation"


@dataclass
class TaskRequest:
    """Structured task request"""
    task_type: TaskType
    prompt: str
    context: Optional[Dict[str, Any]] = None
    priority: str = "normal"  # low, normal, high, critical
    max_tokens: int = 4096
    temperature: float = 0.7
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "task_type": self.task_type.value,
            "prompt": self.prompt,
            "context": self.context,
            "priority": self.priority,
            "max_tokens": self.max_tokens,
            "temperature": self.temperature
        }


@dataclass
class TaskResult:
    """Structured task result"""
    success: bool
    assistant_used: AIAssistant
    result: str
    task_request: TaskRequest
    error: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "success": self.success,
            "assistant_used": self.assistant_used.value,
            "result": self.result,
            "task_request": self.task_request.to_dict(),
            "error": self.error,
            "metadata": self.metadata
        }


class AIOrchestrator:
    """
    Intelligent AI task orchestrator
    
    Routes tasks to appropriate AI assistants based on:
    - Task type and complexity
    - Assistant availability
    - Historical performance
    - Priority level
    """
    
    def __init__(self, log_dir: Optional[str] = None):
        """
        Initialize AI Orchestrator
        
        Args:
            log_dir: Directory to log AI invocations (optional)
        """
        self.log_dir = log_dir or os.path.join(os.path.dirname(__file__), '..', 'logs', 'ai_invocations')
        os.makedirs(self.log_dir, exist_ok=True)
        
        # Task routing rules
        self.routing_rules = {
            # Technical → Claude Code
            TaskType.ARCHITECTURE_DESIGN: AIAssistant.CLAUDE_CODE,
            TaskType.ALGORITHM_OPTIMIZATION: AIAssistant.CLAUDE_CODE,
            TaskType.CODE_REVIEW: AIAssistant.CLAUDE_CODE,
            TaskType.DEBUGGING: AIAssistant.CLAUDE_CODE,
            TaskType.TECHNICAL_DOCUMENTATION: AIAssistant.CLAUDE_CODE,
            TaskType.API_DESIGN: AIAssistant.CLAUDE_CODE,
            TaskType.CORRELATION_ANALYSIS: AIAssistant.CLAUDE_CODE,
            TaskType.PERFORMANCE_ANALYSIS: AIAssistant.CLAUDE_CODE,
            TaskType.DATA_INTERPRETATION: AIAssistant.CLAUDE_CODE,
            
            # Creative → Gemini
            TaskType.SOCIAL_CONTENT: AIAssistant.GEMINI,
            TaskType.BLOG_OUTLINE: AIAssistant.GEMINI,
            TaskType.MARKETING_COPY: AIAssistant.GEMINI,
            TaskType.CONTENT_VARIATION: AIAssistant.GEMINI,
            TaskType.RAPID_IDEATION: AIAssistant.GEMINI,
            
            # Hybrid → Both
            TaskType.CASE_STUDY: AIAssistant.BOTH,
            TaskType.COMPREHENSIVE_STRATEGY: AIAssistant.BOTH,
            TaskType.CONTENT_WITH_STRUCTURE: AIAssistant.BOTH,
        }
    
    def route_task(self, task_request: TaskRequest) -> AIAssistant:
        """
        Route task to appropriate AI assistant
        
        Args:
            task_request: Structured task request
            
        Returns:
            AIAssistant enum indicating which assistant to use
        """
        return self.routing_rules.get(task_request.task_type, AIAssistant.NONE)
    
    def execute_task(self, task_request: TaskRequest) -> TaskResult:
        """
        Execute task with appropriate AI assistant
        
        Args:
            task_request: Structured task request
            
        Returns:
            TaskResult with outcome
        """
        assistant = self.route_task(task_request)
        
        try:
            if assistant == AIAssistant.CLAUDE_CODE:
                result = self._execute_claude(task_request)
                return TaskResult(
                    success=True,
                    assistant_used=AIAssistant.CLAUDE_CODE,
                    result=result,
                    task_request=task_request
                )
            
            elif assistant == AIAssistant.GEMINI:
                result = self._execute_gemini(task_request)
                return TaskResult(
                    success=True,
                    assistant_used=AIAssistant.GEMINI,
                    result=result,
                    task_request=task_request
                )
            
            elif assistant == AIAssistant.BOTH:
                result = self._execute_hybrid(task_request)
                return TaskResult(
                    success=True,
                    assistant_used=AIAssistant.BOTH,
                    result=result,
                    task_request=task_request
                )
            
            else:
                return TaskResult(
                    success=False,
                    assistant_used=AIAssistant.NONE,
                    result="",
                    task_request=task_request,
                    error="No AI assistant available for this task type"
                )
        
        except Exception as e:
            return TaskResult(
                success=False,
                assistant_used=assistant,
                result="",
                task_request=task_request,
                error=str(e)
            )
        
        finally:
            # Log the invocation
            self._log_invocation(task_request, assistant)
    
    def _execute_claude(self, task_request: TaskRequest) -> str:
        """Execute task with Claude Code"""
        context_str = json.dumps(task_request.context, indent=2) if task_request.context else None
        
        return generate_with_claude(
            prompt=task_request.prompt,
            context=context_str,
            max_tokens=task_request.max_tokens
        )
    
    def _execute_gemini(self, task_request: TaskRequest) -> str:
        """Execute task with Gemini"""
        context_str = json.dumps(task_request.context, indent=2) if task_request.context else None
        
        return generate_content(
            prompt=task_request.prompt,
            context=context_str,
            temperature=task_request.temperature,
            max_tokens=task_request.max_tokens
        )
    
    def _execute_hybrid(self, task_request: TaskRequest) -> str:
        """
        Execute hybrid workflow (Claude + Gemini)
        
        Workflow:
        1. Claude creates structure/outline
        2. Gemini generates content sections
        3. Claude reviews and refines
        """
        # Step 1: Claude creates structure
        structure_prompt = f"Create a detailed structure/outline for: {task_request.prompt}"
        structure = self._execute_claude(
            TaskRequest(
                task_type=TaskType.TECHNICAL_DOCUMENTATION,
                prompt=structure_prompt,
                context=task_request.context,
                max_tokens=2000
            )
        )
        
        # Step 2: Gemini generates content
        content_prompt = f"Generate content based on this structure:\n\n{structure}\n\nOriginal request: {task_request.prompt}"
        content = self._execute_gemini(
            TaskRequest(
                task_type=TaskType.CONTENT_VARIATION,
                prompt=content_prompt,
                context=task_request.context,
                temperature=0.8,
                max_tokens=4000
            )
        )
        
        # Step 3: Claude refines
        refinement_prompt = f"Review and refine this content:\n\n{content}\n\nEnsure technical accuracy and consistency."
        final = self._execute_claude(
            TaskRequest(
                task_type=TaskType.TECHNICAL_DOCUMENTATION,
                prompt=refinement_prompt,
                context=task_request.context,
                max_tokens=4000
            )
        )
        
        return final
    
    def _log_invocation(self, task_request: TaskRequest, assistant: AIAssistant):
        """Log AI invocation for tracking and optimization"""
        import datetime
        
        log_entry = {
            "timestamp": datetime.datetime.now().isoformat(),
            "assistant": assistant.value,
            "task_type": task_request.task_type.value,
            "priority": task_request.priority,
            "prompt_length": len(task_request.prompt),
            "has_context": task_request.context is not None
        }
        
        log_file = os.path.join(
            self.log_dir,
            f"{datetime.date.today().isoformat()}_invocations.jsonl"
        )
        
        with open(log_file, 'a') as f:
            f.write(json.dumps(log_entry) + '\n')


# ============================================================================
# CONVENIENCE FUNCTIONS
# ============================================================================

def analyze_biological_correlation(
    metrics_data: Dict[str, Any],
    question: str
) -> TaskResult:
    """
    Analyze biological correlation using Claude Code
    
    Args:
        metrics_data: Biological metrics data
        question: Specific question to analyze
        
    Returns:
        TaskResult with analysis
    """
    orchestrator = AIOrchestrator()
    
    task = TaskRequest(
        task_type=TaskType.CORRELATION_ANALYSIS,
        prompt=question,
        context=metrics_data,
        max_tokens=6000
    )
    
    return orchestrator.execute_task(task)


def generate_social_content_burst(
    topic: str,
    platform: str,
    count: int = 5
) -> TaskResult:
    """
    Generate multiple social media content variations using Gemini
    
    Args:
        topic: Content topic
        platform: Social platform (twitter, instagram, linkedin)
        count: Number of variations
        
    Returns:
        TaskResult with generated content
    """
    orchestrator = AIOrchestrator()
    
    task = TaskRequest(
        task_type=TaskType.SOCIAL_CONTENT,
        prompt=f"Generate {count} variations of social media content for {platform} about: {topic}",
        context={"platform": platform, "count": count},
        temperature=0.9,  # Higher creativity for social content
        max_tokens=2000
    )
    
    return orchestrator.execute_task(task)


def optimize_algorithm(
    algorithm_description: str,
    current_performance: Dict[str, Any],
    optimization_goals: List[str]
) -> TaskResult:
    """
    Optimize algorithm using Claude Code
    
    Args:
        algorithm_description: Current algorithm description/code
        current_performance: Performance metrics
        optimization_goals: List of optimization goals
        
    Returns:
        TaskResult with optimization recommendations
    """
    orchestrator = AIOrchestrator()
    
    task = TaskRequest(
        task_type=TaskType.ALGORITHM_OPTIMIZATION,
        prompt=f"Optimize this algorithm:\n\n{algorithm_description}\n\nGoals: {', '.join(optimization_goals)}",
        context={
            "current_performance": current_performance,
            "goals": optimization_goals
        },
        max_tokens=8000
    )
    
    return orchestrator.execute_task(task)


def create_comprehensive_case_study(
    subject: str,
    data: Dict[str, Any]
) -> TaskResult:
    """
    Create comprehensive case study using hybrid Claude + Gemini workflow
    
    Args:
        subject: Case study subject
        data: Supporting data
        
    Returns:
        TaskResult with case study
    """
    orchestrator = AIOrchestrator()
    
    task = TaskRequest(
        task_type=TaskType.CASE_STUDY,
        prompt=f"Create a comprehensive case study for: {subject}",
        context=data,
        max_tokens=8000
    )
    
    return orchestrator.execute_task(task)


# ============================================================================
# EXAMPLE USAGE
# ============================================================================

if __name__ == "__main__":
    print("AI Orchestrator - JAN Expansion Protocol")
    print("=" * 60)
    print()
    
    # Example 1: Technical analysis (Claude Code)
    print("Example 1: Biological correlation analysis (Claude Code)")
    print("-" * 60)
    
    result = analyze_biological_correlation(
        metrics_data={
            "day1_glucose": 124,
            "day1_vision": 8,
            "day2_glucose": 338,
            "day2_vision": 7,
            "day3_glucose": 520,
            "day3_vision": 5
        },
        question="What is the correlation between glucose levels and vision clarity? At what threshold does vision degrade?"
    )
    
    if result.success:
        print(f"✓ Analysis complete via {result.assistant_used.value}")
        print(f"Result preview: {result.result[:200]}...")
    else:
        print(f"✗ Error: {result.error}")
    
    print()
    
    # Example 2: Creative burst (Gemini)
    print("Example 2: Social content generation (Gemini)")
    print("-" * 60)
    
    result = generate_social_content_burst(
        topic="Day 30 of Homeostasis Protocol - glucose stability achieved",
        platform="twitter",
        count=3
    )
    
    if result.success:
        print(f"✓ Content generated via {result.assistant_used.value}")
        print(f"Result preview: {result.result[:200]}...")
    else:
        print(f"✗ Error: {result.error}")
    
    print()
    
    # Example 3: Hybrid workflow (Both)
    print("Example 3: Case study creation (Hybrid Claude + Gemini)")
    print("-" * 60)
    
    result = create_comprehensive_case_study(
        subject="JAN's Homeostasis Protocol - First 30 Days",
        data={
            "starting_glucose": 520,
            "current_glucose": 124,
            "vision_improvement": "5 → 8",
            "loop_frequency": "8+ per day",
            "symptoms_resolved": ["muscle cramps", "vision blur", "osmotic pressure"]
        }
    )
    
    if result.success:
        print(f"✓ Case study created via {result.assistant_used.value}")
        print(f"Result preview: {result.result[:200]}...")
    else:
        print(f"✗ Error: {result.error}")
    
    print()
    print("=" * 60)
    print("AI Orchestrator ready for integration")

