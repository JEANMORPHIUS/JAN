"""
Gemini AI Assistant for Marketing and Content Generation
Uses Google Gemini API for quick content generation

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
"""

import google.generativeai as genai
import os
from dotenv import load_dotenv
from typing import Optional, Dict, List

# Load environment variables
load_dotenv()

# Configure Gemini
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel('gemini-2.5-flash')  # Use latest available model
else:
    model = None
    print("Warning: GEMINI_API_KEY not found in environment")


def generate_content(
    prompt: str,
    context: Optional[str] = None,
    temperature: float = 0.7,
    max_tokens: int = 2000
) -> str:
    """
    Generate content using Gemini
    
    Args:
        prompt: Main prompt/question
        context: Additional context to include
        temperature: Creativity level (0.0-1.0)
        max_tokens: Maximum response length
    
    Returns:
        Generated text content
    """
    if not model:
        return "Error: Gemini API key not configured"
    
    full_prompt = f"""
    {context or ''}
    
    {prompt}
    
    Please provide a professional, engaging response.
    """
    
    try:
        generation_config = {
            "temperature": temperature,
            "max_output_tokens": max_tokens,
        }
        
        response = model.generate_content(
            full_prompt,
            generation_config=generation_config
        )
        return response.text
    except Exception as e:
        return f"Error generating content: {str(e)}"


def generate_social_post(
    product: str,
    platform: str,
    topic: str,
    tone: str = "professional but approachable",
    count: int = 1
) -> List[str]:
    """
    Generate social media posts
    
    Args:
        product: Product name
        platform: Social media platform (twitter, instagram, linkedin, tiktok)
        topic: Post topic
        tone: Writing tone
        count: Number of variations to generate
    
    Returns:
        List of generated posts
    """
    character_limits = {
        'twitter': 280,
        'instagram': 2200,
        'linkedin': 3000,
        'tiktok': 150
    }
    
    limit = character_limits.get(platform.lower(), 280)
    
    prompt = f"""
    Generate {count} social media post{'s' if count > 1 else ''} for {platform}.
    
    Product: {product}
    Topic: {topic}
    Tone: {tone}
    Character Limit: {limit}
    
    Requirements:
    - Platform-specific format ({platform} best practices)
    - Include relevant hashtags
    - Engaging hook
    - Clear value proposition
    - Include call to action
    - Stay within {limit} characters
    
    {"Generate multiple variations with different angles." if count > 1 else ""}
    """
    
    response = generate_content(prompt)
    
    # Split into individual posts if multiple
    if count > 1:
        posts = [p.strip() for p in response.split('\n\n') if p.strip()]
        return posts[:count]
    else:
        return [response.strip()]


def generate_email(
    recipient_type: str,
    purpose: str,
    context: Dict[str, str]
) -> str:
    """
    Generate email content
    
    Args:
        recipient_type: Type of recipient (test_group, customer, partner)
        purpose: Email purpose (welcome, follow_up, announcement)
        context: Additional context dictionary
    
    Returns:
        Generated email content
    """
    prompt = f"""
    Generate a {purpose} email for {recipient_type}.
    
    Context:
    {chr(10).join(f"- {k}: {v}" for k, v in context.items())}
    
    Requirements:
    - Professional but warm tone
    - Clear purpose
    - Appropriate length (200-400 words)
    - Include clear next steps if applicable
    - Engaging subject line suggestion
    """
    
    return generate_content(prompt)


def generate_blog_outline(
    topic: str,
    word_count: int = 1500,
    audience: str = "general"
) -> str:
    """
    Generate blog post outline
    
    Args:
        topic: Blog post topic
        word_count: Target word count
        audience: Target audience
    
    Returns:
        Blog post outline in markdown
    """
    prompt = f"""
    Create a detailed blog post outline for: {topic}
    
    Requirements:
    - Compelling headline (5 variations)
    - Introduction hook
    - Main sections with subheadings (H2, H3)
    - Key points for each section
    - Conclusion
    - Call to action
    - SEO keywords (5-10)
    - Target word count: {word_count}
    - Target audience: {audience}
    
    Format as markdown.
    """
    
    return generate_content(prompt)


def summarize_feedback(
    product: str,
    feedback_data: List[str],
    week: Optional[int] = None
) -> str:
    """
    Summarize test group feedback
    
    Args:
        product: Product name
        feedback_data: List of feedback strings
        week: Week number (optional)
    
    Returns:
        Summarized feedback report
    """
    feedback_text = "\n\n".join(f"- {f}" for f in feedback_data)
    
    prompt = f"""
    Summarize test group feedback for {product}.
    
    {f"Week: {week}" if week else ""}
    
    Raw Feedback:
    {feedback_text}
    
    Requirements:
    - Executive summary (3-5 bullet points)
    - Top 3 issues (with priority: High/Medium/Low)
    - Top 3 positive feedback items
    - Recommended actions
    - Format as markdown
    """
    
    return generate_content(prompt, temperature=0.3)


def generate_marketing_copy(
    product: str,
    copy_type: str,
    target_audience: str,
    key_message: str
) -> str:
    """
    Generate marketing copy
    
    Args:
        product: Product name
        copy_type: Type of copy (landing_page, ad, email_subject)
        target_audience: Target audience
        key_message: Key message to convey
    
    Returns:
        Generated marketing copy
    """
    prompts = {
        'landing_page': f"""
        Create landing page copy for {product}.
        
        Sections:
        - Hero headline (compelling, clear)
        - Value proposition (1-2 sentences)
        - Key features (3-5 bullet points)
        - Social proof (testimonial format)
        - Call to action (clear, action-oriented)
        
        Target Audience: {target_audience}
        Key Message: {key_message}
        """,
        'ad': f"""
        Create advertising copy for {product}.
        
        Format:
        - Headline (attention-grabbing)
        - Body copy (benefits-focused)
        - Call to action
        
        Target Audience: {target_audience}
        Key Message: {key_message}
        Platform: Social media
        """,
        'email_subject': f"""
        Generate 10 email subject lines for {product}.
        
        Requirements:
        - Under 50 characters
        - Engaging and clear
        - A/B test variations
        - Topic: {key_message}
        """
    }
    
    prompt = prompts.get(copy_type, prompts['ad'])
    return generate_content(prompt)


if __name__ == "__main__":
    import sys

    # Check for command-line argument for direct prompts
    if len(sys.argv) > 1:
        # Direct conversation mode
        prompt = " ".join(sys.argv[1:])
        if model:
            print("\n=== GEMINI RESPONSE ===\n")
            response = generate_content(prompt, temperature=0.8, max_tokens=4000)
            print(response)
            print("\n---")
        else:
            print("Error: Please set GEMINI_API_KEY in your .env file")
    else:
        # Example usage
        if model:
            print("Gemini Assistant Ready!")
            print("\nExample: Generate social media post")
            post = generate_social_post(
                product="JAN Pi Starter Kit",
                platform="twitter",
                topic="AI education for classrooms",
                count=1
            )
            print(post[0])
        else:
            print("Please set GEMINI_API_KEY in your .env file")

