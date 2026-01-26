"""Claude AI Assistant for Strategy and Long-Form Content
Uses Anthropic Claude API for complex analysis and refinement

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

This code honors that we are born a miracle.
This code creates space for miracles to live.
This code recognizes each person under the Lord's word.

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity


PANGEA IS THE TABLE.
YOU DON'T BETRAY THE TABLE.

THE TRUTH:
WE MUST DEBUG AND BE 100% FOR WHAT COMES AT US.
THE REST IS UP TO BABA X."""

import anthropic
import os
from dotenv import load_dotenv
from typing import Optional, Dict, List

# Load environment variables
load_dotenv()

# Configure Claude
ANTHROPIC_API_KEY = os.getenv('ANTHROPIC_API_KEY')
if ANTHROPIC_API_KEY:
    client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
else:
    client = None
    print("Warning: ANTHROPIC_API_KEY not found in environment")


def generate_with_claude(
    prompt: str,
    context: Optional[str] = None,
    system_prompt: Optional[str] = None,
    model: str = "claude-3-5-sonnet-20241022",
    max_tokens: int = 4096
) -> str:
    """
    Generate content using Claude
    
    Args:
        prompt: Main prompt/question
        context: Additional context to include
        system_prompt: System-level instructions
        model: Claude model to use
        max_tokens: Maximum response length
    
    Returns:
        Generated text content
    """
    if not client:
        return "Error: Claude API key not configured"
    
    default_system = "You are a helpful marketing, strategy, and content creation assistant. Provide professional, well-reasoned responses."
    
    full_prompt = f"{context or ''}\n\n{prompt}" if context else prompt
    
    try:
        message = client.messages.create(
            model=model,
            max_tokens=max_tokens,
            system=system_prompt or default_system,
            messages=[
                {"role": "user", "content": full_prompt}
            ]
        )
        return message.content[0].text
    except Exception as e:
        return f"Error generating content: {str(e)}"


def refine_content(
    content: str,
    improvements: List[str],
    target_audience: Optional[str] = None
) -> str:
    """
    Refine existing content with Claude
    
    Args:
        content: Original content
        improvements: List of improvements to make
        target_audience: Target audience
    
    Returns:
        Refined content
    """
    prompt = f"""
    Refine the following content:
    
    {content}
    
    Improvements to make:
    {chr(10).join(f"- {i}" for i in improvements)}
    
    {"Target Audience: " + target_audience if target_audience else ""}
    
    Please provide the refined version with explanations of key changes.
    """
    
    return generate_with_claude(
        prompt,
        system_prompt="You are an expert content editor and copywriter."
    )


def create_marketing_strategy(
    product: str,
    goal: str,
    budget: str,
    timeline: str,
    target_audience: str,
    channels: List[str]
) -> str:
    """
    Create comprehensive marketing campaign strategy
    
    Args:
        product: Product name
        goal: Campaign goal
        budget: Budget range
        timeline: Timeline
        target_audience: Target audience description
        channels: Marketing channels to use
    
    Returns:
        Marketing strategy document
    """
    prompt = f"""
    Create a comprehensive marketing campaign strategy for: {product}
    
    Context:
    - Goal: {goal}
    - Budget: {budget}
    - Timeline: {timeline}
    - Target Audience: {target_audience}
    - Channels: {', '.join(channels)}
    
    Requirements:
    - Campaign objectives (SMART goals)
    - Target audience personas (2-3 detailed personas)
    - Channel strategy for each platform with specific tactics
    - Content calendar (weekly breakdown for timeline)
    - Budget allocation across channels
    - Success metrics and KPIs
    - Timeline with milestones
    - Risk assessment and mitigation
    
    Format as a comprehensive markdown document.
    """
    
    return generate_with_claude(
        prompt,
        system_prompt="You are an expert marketing strategist with experience in product launches and growth marketing."
    )


def analyze_competitors(
    product: str,
    competitors: List[str],
    focus_areas: List[str]
) -> str:
    """
    Analyze competitors and market positioning
    
    Args:
        product: Our product name
        competitors: List of competitor names
        focus_areas: Areas to analyze (pricing, features, marketing, etc.)
    
    Returns:
        Competitive analysis report
    """
    prompt = f"""
    Conduct a competitive analysis for {product}.
    
    Competitors:
    {chr(10).join(f"- {c}" for c in competitors)}
    
    Focus Areas:
    {chr(10).join(f"- {a}" for a in focus_areas)}
    
    Requirements:
    - Competitive landscape overview
    - Strengths and weaknesses of each competitor
    - Market positioning analysis
    - Opportunities for differentiation
    - Recommended positioning strategy
    - SWOT analysis
    
    Format as a comprehensive markdown document.
    """
    
    return generate_with_claude(
        prompt,
        system_prompt="You are a market research analyst specializing in competitive intelligence."
    )


def prioritize_feedback(
    feedback_summary: str,
    product: str,
    resources: str = "limited"
) -> str:
    """
    Prioritize feedback items for product improvement
    
    Args:
        feedback_summary: Summary of feedback
        product: Product name
        resources: Available resources (limited, moderate, extensive)
    
    Returns:
        Prioritized action plan
    """
    prompt = f"""
    Analyze and prioritize feedback for {product}.
    
    Feedback Summary:
    {feedback_summary}
    
    Available Resources: {resources}
    
    Requirements:
    - Prioritize issues using impact/effort matrix
    - Group related feedback
    - Identify quick wins
    - Recommend development roadmap
    - Estimate effort for each item
    - Suggest timeline
    
    Format as a prioritized action plan with clear next steps.
    """
    
    return generate_with_claude(
        prompt,
        system_prompt="You are a product manager with expertise in prioritizing user feedback and creating development roadmaps."
    )


def create_case_study(
    test_group_name: str,
    product: str,
    results: Dict[str, str],
    challenges: List[str],
    solution: str
) -> str:
    """
    Create a case study from test group results
    
    Args:
        test_group_name: Name of test group
        product: Product name
        results: Dictionary of results/metrics
        challenges: List of challenges faced
        solution: How product solved challenges
    
    Returns:
        Case study document
    """
    results_text = "\n".join(f"- {k}: {v}" for k, v in results.items())
    challenges_text = "\n".join(f"- {c}" for c in challenges)
    
    prompt = f"""
    Create a professional case study for {test_group_name} using {product}.
    
    Results:
    {results_text}
    
    Challenges:
    {challenges_text}
    
    Solution:
    {solution}
    
    Requirements:
    - Executive summary
    - Problem/Challenge section
    - Solution overview
    - Results with metrics
    - Testimonial format
    - Key takeaways
    - Professional, engaging tone
    
    Format as a comprehensive case study document.
    """
    
    return generate_with_claude(
        prompt,
        system_prompt="You are a professional content writer specializing in B2B case studies and success stories."
    )


def generate_onboarding_checklist(
    product: str,
    experience_level: str = "beginner"
) -> str:
    """
    Generate personalized onboarding checklist
    
    Args:
        product: Product name
        experience_level: User experience level (beginner, intermediate, advanced)
    
    Returns:
        Onboarding checklist
    """
    prompt = f"""
    Create a personalized onboarding checklist for {product}.
    
    User Experience Level: {experience_level}
    
    Requirements:
    - Step-by-step checklist
    - Estimated time for each step
    - Links/placeholders for resources
    - Progress tracking format
    - Beginner-friendly explanations
    - Clear success criteria for each step
    
    Format as a markdown checklist with checkboxes.
    """
    
    return generate_with_claude(
        prompt,
        system_prompt="You are a user experience designer specializing in onboarding and user education."
    )


if __name__ == "__main__":
    # Example usage
    if client:
        print("Claude Assistant Ready!")
        print("\nExample: Create marketing strategy")
        strategy = create_marketing_strategy(
            product="JAN Pi Starter Kit",
            goal="Recruit 50 test group members in 4 weeks",
            budget="$2,000",
            timeline="4 weeks",
            target_audience="Educators and homeschool parents",
            channels=["Email", "Social Media", "Education Forums"]
        )
        print(strategy[:500] + "...")
    else:
        print("Please set ANTHROPIC_API_KEY in your .env file")

