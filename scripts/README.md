# AI Assistant Scripts

Automated marketing and content generation using Gemini and Claude.

## Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Set Up API Keys

Create a `.env` file in the `JAN/` directory:

```env
GEMINI_API_KEY=your_gemini_api_key_here
ANTHROPIC_API_KEY=your_claude_api_key_here
```

**Get API Keys:**
- Gemini: https://makersuite.google.com/app/apikey
- Claude: https://console.anthropic.com/

### 3. Run Scripts

```bash
# Test Gemini
python gemini_assistant.py

# Test Claude
python claude_assistant.py

# Test Auto-Prompt System
python auto_prompt_system.py
```

## Usage

### Generate Content

```python
from gemini_assistant import generate_social_post

# Generate Twitter post
posts = generate_social_post(
    product="JAN Pi Starter Kit",
    platform="twitter",
    topic="AI education for classrooms",
    count=3
)

for post in posts:
    print(post)
```

### Summarize Feedback

```python
from claude_assistant import prioritize_feedback

feedback = """
- Love the interface!
- Had trouble with WiFi
- Students are engaged
- Need more examples
"""

summary = prioritize_feedback(
    feedback_summary=feedback,
    product="JAN Pi Starter Kit",
    resources="limited"
)

print(summary)
```

### Auto-Prompt System

```python
from auto_prompt_system import AutoPromptSystem

system = AutoPromptSystem()

# Handle test group member selection
test_member = {
    'name': 'Sarah Johnson',
    'email': 'sarah@example.com',
    'product': 'JAN Pi Starter Kit',
    'background': 'Elementary teacher',
    'start_date': '2025-02-01',
    'end_date': '2025-02-28'
}

email = system.handle_event('test_group_selected', test_member)
print(email)
```

## Scripts

### `gemini_assistant.py`
- Quick content generation
- Social media posts
- Email drafts
- Blog outlines

### `claude_assistant.py`
- Strategy refinement
- Long-form content
- Competitive analysis
- Feedback prioritization

### `auto_prompt_system.py`
- Event-driven automation
- Welcome emails
- Feedback summaries
- Campaign content

## Examples

See `AI_ASSISTANCE_AUTOMATION.md` for complete examples and templates.

## Troubleshooting

**API Key Errors:**
- Verify keys are in `.env` file
- Check key format (no spaces)
- Ensure keys are active

**Import Errors:**
- Run `pip install -r requirements.txt`
- Check Python version (3.8+)

**Rate Limits:**
- Gemini: 60 requests/minute (free tier)
- Claude: Check your plan limits
- Add delays between requests if needed

## Support

For issues or questions:
- Check documentation in `AI_ASSISTANCE_AUTOMATION.md`
- Review examples in scripts
- Contact: [Your Contact]

---

**Last Updated:** 2025-01-27

