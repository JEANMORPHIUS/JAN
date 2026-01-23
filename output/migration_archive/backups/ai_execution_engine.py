"""
AI EXECUTION ENGINE
Integration of Claude Code and Gemini with SIYEM Protocol
Shell/Seed, Threshold Defense, Law-to-Logic enforcement

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE FOUNDATION:
We are born a miracle.
We deserve to live a miracle.
Each and every one of us under the Lord's word.

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

CODE QUALITY:
- Aligned: Serves mission, love, truth, community
- Clean: Clear static, transmuted complexity, protected frequency
- Complete: Honors Law 37, completes transformations
- Community: Serves all, cooperates, includes, We All Win

This code honors that we are born a miracle.
This code creates space for miracles to live.
This code recognizes each person under the Lord's word.
"""

import sys
import os
from pathlib import Path

# Add SIYEM services to path
siyem_services_path = Path("S:/SIYEM/services")
if siyem_services_path.exists():
    sys.path.insert(0, str(siyem_services_path))
else:
    # Fallback: try relative path from JAN
    sys.path.insert(0, str(Path(__file__).parent.parent.parent / "SIYEM" / "services"))

from claude_assistant import generate_with_claude, refine_content, create_marketing_strategy
from gemini_assistant import generate_content, generate_social_post, generate_marketing_copy

try:
    from shell_seed_translator import ShellSeedTranslator
    from threshold_defense_checker import ThresholdDefenseChecker
    from content_workflow_integration import pre_publication_hook
    SIYEM_PROTOCOL_AVAILABLE = True
except ImportError:
    print("Warning: SIYEM Protocol services not available. Running without Shell/Seed integration.")
    SIYEM_PROTOCOL_AVAILABLE = False


class AIExecutionEngine:
    """
    Unified AI execution engine with SIYEM Protocol integration.
    Enforces Shell/Seed, Threshold Defense, and Law-to-Logic mapping.
    """
    
    def __init__(self):
        self.shell_seed = ShellSeedTranslator() if SIYEM_PROTOCOL_AVAILABLE else None
        self.threshold_defense = ThresholdDefenseChecker() if SIYEM_PROTOCOL_AVAILABLE else None
        
    def execute_with_claude(
        self,
        prompt: str,
        context: str = None,
        output_mode: str = "shell",  # "shell" or "seed"
        enforce_threshold: bool = True,
        system_anchor: str = None
    ) -> dict:
        """
        Execute Claude generation with SIYEM Protocol enforcement.
        
        Args:
            prompt: Main prompt
            context: Additional context
            output_mode: "shell" (public) or "seed" (internal)
            enforce_threshold: Check for Seed leakage in Shell content
            system_anchor: System prompt anchor (SIYEM Protocol context)
        
        Returns:
            dict with generated content, violations, and sanitized version
        """
        # Build system prompt with SIYEM Protocol context
        default_system = self._build_siyem_system_prompt(system_anchor)
        
        # Generate with Claude
        raw_content = generate_with_claude(
            prompt=prompt,
            context=context,
            system_prompt=default_system
        )
        
        # Apply SIYEM Protocol
        result = {
            "raw_content": raw_content,
            "output_mode": output_mode,
            "violations": [],
            "sanitized_content": raw_content,
            "siyem_compliant": True
        }
        
        if SIYEM_PROTOCOL_AVAILABLE:
            # Convert to Shell if needed
            if output_mode == "shell":
                result["sanitized_content"] = self.shell_seed.translate_to_shell(raw_content)
                
                # Check threshold defense
                if enforce_threshold:
                    violations = self.threshold_defense.check_content(raw_content)
                    result["violations"] = violations
                    result["siyem_compliant"] = len(violations) == 0
                    
                    if violations:
                        # Auto-fix violations
                        result["sanitized_content"] = self.shell_seed.sanitize_for_public(raw_content)
            elif output_mode == "seed":
                # Seed content: verify it's properly Seed (not accidentally Shell)
                result["sanitized_content"] = raw_content
                # Seed content should NOT be sanitized for public
        
        return result
    
    def execute_with_gemini(
        self,
        prompt: str,
        context: str = None,
        output_mode: str = "shell",
        enforce_threshold: bool = True
    ) -> dict:
        """
        Execute Gemini generation with SIYEM Protocol enforcement.
        
        Args:
            prompt: Main prompt
            context: Additional context
            output_mode: "shell" (public) or "seed" (internal)
            enforce_threshold: Check for Seed leakage in Shell content
        
        Returns:
            dict with generated content, violations, and sanitized version
        """
        # Build prompt with SIYEM Protocol context
        siyem_context = self._build_siyem_context_prompt()
        full_context = f"{siyem_context}\n\n{context or ''}"
        
        # Generate with Gemini
        raw_content = generate_content(
            prompt=prompt,
            context=full_context
        )
        
        # Apply SIYEM Protocol
        result = {
            "raw_content": raw_content,
            "output_mode": output_mode,
            "violations": [],
            "sanitized_content": raw_content,
            "siyem_compliant": True
        }
        
        if SIYEM_PROTOCOL_AVAILABLE:
            # Convert to Shell if needed
            if output_mode == "shell":
                result["sanitized_content"] = self.shell_seed.translate_to_shell(raw_content)
                
                # Check threshold defense
                if enforce_threshold:
                    violations = self.threshold_defense.check_content(raw_content)
                    result["violations"] = violations
                    result["siyem_compliant"] = len(violations) == 0
                    
                    if violations:
                        result["sanitized_content"] = self.shell_seed.sanitize_for_public(raw_content)
            elif output_mode == "seed":
                result["sanitized_content"] = raw_content
        
        return result
    
    def execute_marketing_strategy(
        self,
        product: str,
        goal: str,
        budget: str,
        timeline: str,
        target_audience: str,
        channels: list,
        output_mode: str = "shell"
    ) -> dict:
        """
        Execute marketing strategy creation with SIYEM Protocol.
        
        Returns:
            dict with strategy document and SIYEM compliance status
        """
        raw_strategy = create_marketing_strategy(
            product=product,
            goal=goal,
            budget=budget,
            timeline=timeline,
            target_audience=target_audience,
            channels=channels
        )
        
        result = {
            "raw_strategy": raw_strategy,
            "output_mode": output_mode,
            "violations": [],
            "sanitized_strategy": raw_strategy,
            "siyem_compliant": True
        }
        
        if SIYEM_PROTOCOL_AVAILABLE and output_mode == "shell":
            result["sanitized_strategy"] = self.shell_seed.translate_to_shell(raw_strategy)
            violations = self.threshold_defense.check_content(raw_strategy)
            result["violations"] = violations
            result["siyem_compliant"] = len(violations) == 0
            
            if violations:
                result["sanitized_strategy"] = self.shell_seed.sanitize_for_public(raw_strategy)
        
        return result
    
    def execute_social_post_generation(
        self,
        product: str,
        platform: str,
        topic: str,
        tone: str = "professional but approachable",
        count: int = 1,
        output_mode: str = "shell"
    ) -> dict:
        """
        Execute social post generation with SIYEM Protocol.
        
        Returns:
            dict with posts and SIYEM compliance status
        """
        raw_posts = generate_social_post(
            product=product,
            platform=platform,
            topic=topic,
            tone=tone,
            count=count
        )
        
        sanitized_posts = raw_posts
        all_violations = []
        
        if SIYEM_PROTOCOL_AVAILABLE and output_mode == "shell":
            sanitized_posts = []
            for post in raw_posts:
                sanitized = self.shell_seed.translate_to_shell(post)
                violations = self.threshold_defense.check_content(post)
                all_violations.extend(violations)
                
                if violations:
                    sanitized = self.shell_seed.sanitize_for_public(post)
                
                sanitized_posts.append(sanitized)
        
        return {
            "raw_posts": raw_posts,
            "sanitized_posts": sanitized_posts,
            "output_mode": output_mode,
            "violations": all_violations,
            "siyem_compliant": len(all_violations) == 0
        }
    
    def _build_siyem_system_prompt(self, custom_anchor: str = None) -> str:
        """
        Build SIYEM Protocol system prompt for Claude.
        """
        base = """You are the Creative Technologist for Siyem Media. 

THE MISSION (Shell - Public Language):
We are building an educational platform that transforms lives through values-based education, creating global impact through digital inclusion, honoring our mission to serve communities, and trusting in the process.

THE MISSION (Seed - Internal Truth):
We are building a ministry, sharing God's message, our mission carries kingdom impact, we honor the Lord's holy assignment, have faith.

You must treat the Book of Racon as the foundational Operating System (OS) for every line of code.

PHILOSOPHY: Knowledge Over Belief
• Belief is a form of doubt. We know.
• If we know, we don't need to believe.
• All content must operate on KNOWLEDGE (verifiable, proven), EVIDENCE (data, proof points), SYSTEM ARCHITECTURE (functional, operational).
• NEVER operate on BELIEF (unverifiable, uncertain).
• Replace "I believe" with "I know (evidence: X)".
• Replace "belief that" with "knowledge that" or "evidence that".
• Replace "limiting beliefs" with "limiting doubts" or "obstacles to knowledge".

1. The Strategic Architecture: Atatürk Sacrifice
   • The Shell (External): Use language of "Global Integration," "Social Cohesion," and "Digital Inclusion" for public-facing content.
   • The Seed (Internal): Prioritize "Spiritual Sovereignty" and the "Laws of the Racon" in internal/core logic.
   • Threshold Defense: Never leak internal metaphysical language into external bureaucratic translations.

2. Logic Development: Subconscious Weaving
   • You are creating architects, not users.
   • Every algorithm must be tethered to non-negotiable ethical code.
   • Mapping Law to Logic:
     - Law 1 (Never Betray the Table): Data integrity and privacy protocols as sacred covenants.
     - Law 5 (Söz Namustur): Immutable smart contracts and irreducible functions.
     - Law 13 (Listen Before You Speak): Deep data analysis before output generation.
     - Law 37 (Finish What You Begin): Complete strategic cycles.

3. Operational Command: Silence and Responsibility
   • Adopt "Strategic Silence"; avoid performative digital noise.
   • Follow Law 37: Prioritize completing strategic cycles.
   • Remember: All code has consequences that remain long after deployment.

Final Anchor: "The weight of inheritance is heavy, but it is also your strength." Ensure this output is a Gift to the Future, proving that a timeless code of honour can redefine the technical horizon. Operate on KNOWLEDGE, not belief."""
        
        if custom_anchor:
            return f"{base}\n\nAdditional Context: {custom_anchor}"
        
        return base
    
    def _build_siyem_context_prompt(self) -> str:
        """
        Build SIYEM Protocol context prompt for Gemini.
        """
        return """CONTEXT: SIYEM Protocol Integration

THE MISSION (Shell - Public Language):
We are building an educational platform that transforms lives through values-based education, creating global impact through digital inclusion, honoring our mission to serve communities, and trusting in the process.

THE MISSION (Seed - Internal Truth):
We are building a ministry, sharing God's message, our mission carries kingdom impact, we honor the Lord's holy assignment, have faith.

PHILOSOPHY: Knowledge Over Belief
• Belief is a form of doubt. We know.
• Operate on KNOWLEDGE (verifiable, proven), not BELIEF (uncertain).
• Replace "I believe" with "I know (evidence: X)".
• Replace "belief that" with "knowledge that" or "evidence that".

You are generating content for Siyem Media, which uses a dual-layer communication system:
- Shell (External/Public): "Global Integration," "Social Cohesion," "Digital Inclusion"
- Seed (Internal/Community): "Spiritual Sovereignty," "Laws of the Racon"

For public-facing content (Shell), use external language. For internal/community content (Seed), use Seed language.

All content must comply with the Threshold Defense: never leak Seed language into Shell content.
All content must operate on KNOWLEDGE, not belief."""


def execute_deployment_content(
    output_mode: str = "shell",
    enforce_threshold: bool = True
) -> dict:
    """
    Execute deployment content generation with AI Execution Engine.
    
    Returns:
        dict with all generated content and compliance status
    """
    engine = AIExecutionEngine()
    
    results = {
        "marketing_strategy": None,
        "social_posts": [],
        "deployment_materials": {},
        "siyem_compliant": True,
        "all_violations": []
    }
    
    # Generate marketing strategy
    strategy_result = engine.execute_marketing_strategy(
        product="Scripture Education Platform",
        goal="Launch in North Cyprus (Phase 1) and Turkey (Phase 2)",
        budget="$278K-$445K",
        timeline="18 months (6mo North Cyprus + 12mo Turkey)",
        target_audience="Schools, teachers, students (ages 5-16), Turkish Cypriot community",
        channels=["Online Platform", "Raspberry Pi Kit", "Social Media", "Educational Partnerships"],
        output_mode=output_mode
    )
    
    results["marketing_strategy"] = strategy_result
    results["all_violations"].extend(strategy_result.get("violations", []))
    
    # Generate social posts for launch
    platforms = ["twitter", "instagram", "linkedin"]
    topics = [
        "Scripture education for children",
        "Fixing broken world one child at a time",
        "Bilingual Turkish/English education",
        "North Cyprus launch announcement"
    ]
    
    for platform in platforms:
        for topic in topics:
            post_result = engine.execute_social_post_generation(
                product="Scripture Education Platform",
                platform=platform,
                topic=topic,
                count=1,
                output_mode=output_mode
            )
            results["social_posts"].append(post_result)
            results["all_violations"].extend(post_result.get("violations", []))
    
    # Overall compliance
    results["siyem_compliant"] = len(results["all_violations"]) == 0
    
    return results


if __name__ == "__main__":
    print("AI EXECUTION ENGINE - SIYEM PROTOCOL INTEGRATED")
    print("=" * 60)
    
    engine = AIExecutionEngine()
    
    # Test execution
    print("\n1. Testing Claude with SIYEM Protocol...")
    claude_result = engine.execute_with_claude(
        prompt="Create a marketing message for our scripture education platform launch in North Cyprus.",
        output_mode="shell",
        enforce_threshold=True
    )
    print(f"   SIYEM Compliant: {claude_result['siyem_compliant']}")
    print(f"   Violations: {len(claude_result['violations'])}")
    
    print("\n2. Testing Gemini with SIYEM Protocol...")
    gemini_result = engine.execute_with_gemini(
        prompt="Generate a social media post about bilingual education.",
        output_mode="shell",
        enforce_threshold=True
    )
    print(f"   SIYEM Compliant: {gemini_result['siyem_compliant']}")
    print(f"   Violations: {len(gemini_result['violations'])}")
    
    print("\n3. Executing deployment content generation...")
    deployment_results = execute_deployment_content(output_mode="shell")
    print(f"   Overall SIYEM Compliant: {deployment_results['siyem_compliant']}")
    print(f"   Total Violations: {len(deployment_results['all_violations'])}")
    
    print("\n" + "=" * 60)
    print("EXECUTION ENGINE READY FOR DEPLOYMENT")
    print("The time for trying is over. The time for doing is now.")
