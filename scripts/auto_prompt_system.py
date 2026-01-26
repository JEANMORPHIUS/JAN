"""Auto-Prompting System
Automatically triggers AI assistance based on events

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity


PANGEA IS THE TABLE.
YOU DON'T BETRAY THE TABLE.

THE TRUTH:
WE MUST DEBUG AND BE 100% FOR WHAT COMES AT US.
THE REST IS UP TO BABA X."""

import os
from datetime import datetime, timedelta
from typing import Dict, List, Optional
from dotenv import load_dotenv

# Import assistants
try:
    from gemini_assistant import (
        generate_content,
        generate_social_post,
        generate_email,
        summarize_feedback
    )
    from claude_assistant import (
        generate_with_claude,
        refine_content,
        prioritize_feedback,
        create_case_study
    )
except ImportError:
    print("Warning: Assistant modules not found. Some features may not work.")


load_dotenv()


class AutoPromptSystem:
    """Automated prompting system for marketing and operations"""
    
    def __init__(self):
        self.events = []
        self.templates = self._load_templates()
    
    def _load_templates(self) -> Dict:
        """Load prompt templates"""
        return {
            'test_group_selected': {
                'trigger': 'test_group_member_selected',
                'action': 'generate_welcome_email',
                'ai': 'gemini'
            },
            'weekly_feedback': {
                'trigger': 'weekly_feedback_collected',
                'action': 'summarize_feedback',
                'ai': 'claude'
            },
            'marketing_campaign': {
                'trigger': 'campaign_launched',
                'action': 'generate_campaign_content',
                'ai': 'gemini'
            },
            'product_update': {
                'trigger': 'product_update_announced',
                'action': 'generate_announcement',
                'ai': 'gemini'
            }
        }
    
    def handle_event(self, event_type: str, data: Dict) -> Optional[str]:
        """
        Handle an event and trigger appropriate AI assistance
        
        Args:
            event_type: Type of event
            data: Event data
        
        Returns:
            Generated content or None
        """
        template = self.templates.get(event_type)
        if not template:
            return None
        
        action = template['action']
        ai = template['ai']
        
        # Route to appropriate handler
        if action == 'generate_welcome_email':
            return self._generate_welcome_email(data, ai)
        elif action == 'summarize_feedback':
            return self._summarize_feedback(data, ai)
        elif action == 'generate_campaign_content':
            return self._generate_campaign_content(data, ai)
        elif action == 'generate_announcement':
            return self._generate_announcement(data, ai)
        
        return None
    
    def _generate_welcome_email(self, data: Dict, ai: str) -> str:
        """Generate welcome email for test group member"""
        prompt = f"""
        Generate a personalized welcome email for a test group member.
        
        Context:
        - Product: {data.get('product', 'Unknown')}
        - Member Name: {data.get('name', 'Valued Tester')}
        - Member Background: {data.get('background', 'Not provided')}
        - Test Period: {data.get('start_date', 'TBD')} to {data.get('end_date', 'TBD')}
        
        Requirements:
        - Warm, professional tone
        - Clear next steps
        - Include onboarding link placeholder: [ONBOARDING_LINK]
        - Mention community access
        - Keep under 200 words
        """
        
        if ai == 'gemini':
            return generate_email(
                recipient_type='test_group',
                purpose='welcome',
                context=data
            )
        else:
            return generate_with_claude(prompt)
    
    def _summarize_feedback(self, data: Dict, ai: str) -> str:
        """Summarize weekly feedback"""
        feedback = data.get('feedback', [])
        product = data.get('product', 'Product')
        week = data.get('week', None)
        
        if ai == 'claude':
            feedback_text = "\n\n".join(f"- {f}" for f in feedback)
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
            return generate_with_claude(prompt)
        else:
            return summarize_feedback(product, feedback, week)
    
    def _generate_campaign_content(self, data: Dict, ai: str) -> str:
        """Generate marketing campaign content"""
        product = data.get('product', 'Product')
        platforms = data.get('platforms', ['twitter'])
        topic = data.get('topic', 'Product launch')
        
        if ai == 'gemini':
            content = []
            for platform in platforms:
                posts = generate_social_post(
                    product=product,
                    platform=platform,
                    topic=topic,
                    count=3
                )
                content.extend(posts)
            return "\n\n---\n\n".join(content)
        else:
            prompt = f"""
            Generate comprehensive marketing campaign content for {product}.
            
            Topic: {topic}
            Platforms: {', '.join(platforms)}
            
            Create content for each platform with:
            - Platform-specific format
            - Engaging hooks
            - Clear value propositions
            - Call to action
            """
            return generate_with_claude(prompt)
    
    def _generate_announcement(self, data: Dict, ai: str) -> str:
        """Generate product update announcement"""
        product = data.get('product', 'Product')
        update = data.get('update', 'New features')
        audience = data.get('audience', 'users')
        
        prompt = f"""
        Create an announcement for {product} update.
        
        Update Details: {update}
        Target Audience: {audience}
        
        Requirements:
        - Engaging subject line/headline
        - Clear explanation of update
        - Benefits to users
        - Call to action
        - Professional but exciting tone
        """
        
        if ai == 'gemini':
            return generate_content(prompt)
        else:
            return generate_with_claude(prompt)
    
    def schedule_followup(self, member_data: Dict, days: List[int]) -> List[Dict]:
        """
        Schedule follow-up communications
        
        Args:
            member_data: Test member data
            days: Days from start to send follow-ups
        
        Returns:
            List of scheduled communications
        """
        scheduled = []
        start_date = datetime.strptime(member_data['start_date'], '%Y-%m-%d')
        
        for day in days:
            followup_date = start_date + timedelta(days=day)
            scheduled.append({
                'date': followup_date.strftime('%Y-%m-%d'),
                'type': 'follow_up',
                'member': member_data['name'],
                'email': member_data['email'],
                'week': (day // 7) + 1
            })
        
        return scheduled


# Example usage
if __name__ == "__main__":
    system = AutoPromptSystem()
    
    # Example: Test group member selected
    test_member = {
        'name': 'Sarah Johnson',
        'email': 'sarah@example.com',
        'product': 'JAN Pi Starter Kit',
        'background': 'Elementary school teacher with 5 years experience',
        'start_date': '2025-02-01',
        'end_date': '2025-02-28'
    }
    
    print("Generating welcome email...")
    email = system.handle_event('test_group_selected', test_member)
    if email:
        print(email)
    
    # Example: Weekly feedback
    feedback_data = {
        'product': 'JAN Pi Starter Kit',
        'week': 2,
        'feedback': [
            'Love the kid-friendly interface!',
            'Had trouble connecting to WiFi initially',
            'Students are really engaged',
            'Need more example projects'
        ]
    }
    
    print("\n\nSummarizing feedback...")
    summary = system.handle_event('weekly_feedback', feedback_data)
    if summary:
        print(summary)

