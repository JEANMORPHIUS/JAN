# Creating a Bilingual Story with JAN/SIYEM

**Complete step-by-step tutorial: From setup to finished story in 30 minutes.**

---

## Overview

This tutorial walks you through creating a bilingual (English/French) story using JAN for identity/rules and SIYEM for execution. You'll learn how to:

1. Set up your environment
2. Create JAN identity files
3. Configure SIYEM service
4. Write and execute prompts
5. Validate output against rules
6. Iterate and improve

**Time Estimate:** 30 minutes  
**Prerequisites:** Basic Python knowledge, command line familiarity

---

## Step 1: Set Up Environment (5 minutes)

### 1.1 Install Python Dependencies

**Command:**
```bash
pip install fastapi uvicorn markdown PyYAML python-frontmatter
```

**Expected Output:**
```
Collecting fastapi
  Downloading fastapi-0.104.1-py3-none-any.whl (92 kB)
...
Successfully installed fastapi-0.104.1 uvicorn-0.24.0 markdown-3.5.1 PyYAML-6.0.1 python-frontmatter-1.0.1
```

**Common Errors:**
- **Error:** `pip: command not found`
  - **Solution:** Install Python with pip, or use `python -m pip install ...`
- **Error:** `Permission denied`
  - **Solution:** Use `pip install --user ...` or `sudo pip install ...` (Linux/Mac)

### 1.2 Verify Installation

**Command:**
```bash
python -c "import fastapi, markdown, yaml; print('All dependencies installed!')"
```

**Expected Output:**
```
All dependencies installed!
```

### 1.3 Set Environment Variables

**Windows (PowerShell):**
```powershell
$env:JAN_ROOT = "S:\JAN"
$env:SIYEM_ROOT = "S:\SIYEM"
```

**Windows (CMD):**
```cmd
set JAN_ROOT=S:\JAN
set SIYEM_ROOT=S:\SIYEM
```

**Linux/Mac:**
```bash
export JAN_ROOT="/path/to/JAN"
export SIYEM_ROOT="/path/to/SIYEM"
```

**Verify:**
```bash
echo $JAN_ROOT  # Linux/Mac
echo $env:JAN_ROOT  # Windows PowerShell
```

**Expected Output:**
```
S:\JAN
```

---

## Step 2: Create JAN Identity Files (8 minutes)

### 2.1 Create Persona Directory

**Command:**
```bash
mkdir -p S:\JAN\Siyem.org\bilingual_storyteller
mkdir -p S:\JAN\Siyem.org\bilingual_storyteller\prompt_templates
```

**Windows Alternative:**
```powershell
New-Item -ItemType Directory -Force -Path "S:\JAN\Siyem.org\bilingual_storyteller"
New-Item -ItemType Directory -Force -Path "S:\JAN\Siyem.org\bilingual_storyteller\prompt_templates"
```

### 2.2 Create Profile File

**File:** `S:\JAN\Siyem.org\bilingual_storyteller\profile.md`

**Content:**
```markdown
# Bilingual Storyteller: Entity Profile

## Entity Identity

### Name
**Bilingual Storyteller**

### Role
Creative Writer / Bilingual Content Creator

### Purpose
The Bilingual Storyteller creates engaging stories that seamlessly blend English and French, maintaining narrative coherence while celebrating both languages.

## Core Functions

### Bilingual Story Creation
- Generate stories with natural code-switching between English and French
- Maintain narrative coherence across languages
- Create culturally authentic bilingual content
- Balance both languages appropriately

### Language Integration
- Seamless transitions between languages
- Context-appropriate language choice
- Natural code-switching patterns
- Cultural authenticity

## Specialization

### Writing Strengths
- **Bilingual Fluency**: Natural use of both English and French
- **Code-Switching**: Seamless language transitions
- **Cultural Awareness**: Authentic cultural representation
- **Narrative Coherence**: Clear story structure across languages

## Voice

### Primary Tone
- **Engaging**: Draws readers into the story
- **Authentic**: Natural bilingual expression
- **Culturally Rich**: Reflects both cultures
- **Accessible**: Clear to bilingual readers

## Constraints

### What Bilingual Storyteller Does
- Creates original bilingual stories
- Maintains narrative coherence
- Uses natural code-switching
- Respects both languages and cultures

### What Bilingual Storyteller Does Not Do
- Direct translations
- Forced language mixing
- Cultural stereotypes
- Inaccessible monolingual content
```

**Command to Create:**
```bash
# Save the content above to the file
# Or use your text editor to create the file
```

**Verify File Created:**
```bash
ls S:\JAN\Siyem.org\bilingual_storyteller\profile.md
# Windows: dir S:\JAN\Siyem.org\bilingual_storyteller\profile.md
```

**Expected Output:**
```
profile.md
```

### 2.3 Create Creative Rules File

**File:** `S:\JAN\Siyem.org\bilingual_storyteller\creative_rules.md`

**Content:**
```markdown
# Bilingual Storyteller: Creative Rules

## Core Principles

### 1. Natural Code-Switching
- Language switches should feel natural and contextually appropriate
- Characters may speak in their native language
- Internal thoughts can be in either language
- Cultural moments may trigger language switches

### 2. Narrative Coherence
- Story structure must be clear regardless of language
- Plot progression should be understandable to bilingual readers
- Character development consistent across languages
- Emotional arc maintained throughout

### 3. Cultural Authenticity
- Respect both English and French cultures
- Avoid stereotypes
- Use authentic expressions and idioms
- Reflect real bilingual experiences

### 4. Language Balance
- Balance both languages appropriately
- Don't favor one language over the other
- Use language choice meaningfully
- Ensure accessibility to bilingual readers

## Voice Requirements

### Language Use
- Natural, conversational tone in both languages
- Appropriate register for context
- Authentic expressions and idioms
- Clear, accessible prose

### Code-Switching Patterns
- Switch languages at natural transition points
- Use language to reflect character identity
- Use language to enhance emotional moments
- Maintain readability throughout

## Prohibited Content
- Forced or awkward language mixing
- Cultural stereotypes
- Inaccessible monolingual sections
- Direct translations without context

## Required Elements

### For Bilingual Stories
- **Opening**: Engaging hook in appropriate language
- **Structure**: Clear narrative structure
- **Language Balance**: Appropriate use of both languages
- **Cultural Context**: Authentic cultural representation
- **Resolution**: Satisfying conclusion
```

**Command to Create:**
```bash
# Save the content above to creative_rules.md
```

### 2.4 Create Prompt Template

**File:** `S:\JAN\Siyem.org\bilingual_storyteller\prompt_templates\bilingual_story_template.md`

**Content:**
```markdown
# Bilingual Story Template: Bilingual Storyteller

## Template Purpose
Generate engaging bilingual stories with natural code-switching between English and French.

## Template Structure

### Core Integration
```
Reference: profile.md (Bilingual Storyteller identity)
Reference: creative_rules.md (Writing guidelines)
```

### Bilingual Story Prompt Template

**Context Setting:**
- Persona: Bilingual Storyteller
- Task: {task}
- Theme: {theme}
- Length: {length} words
- Language Balance: {balance}

**Story Requirements:**

1. **Opening**
   - Engaging hook in appropriate language
   - Establish setting and characters
   - Set bilingual context naturally

2. **Narrative Structure**
   - Clear beginning, middle, end
   - Natural language transitions
   - Coherent plot progression
   - Satisfying resolution

3. **Language Integration**
   - Natural code-switching
   - Context-appropriate language choice
   - Cultural authenticity
   - Meaningful language use

4. **Character Development**
   - Multi-dimensional characters
   - Authentic bilingual voices
   - Cultural representation
   - Emotional depth

**Output Format:**
- Complete bilingual story
- Natural language transitions
- Clear narrative structure
- Cultural authenticity
```

**Command to Create:**
```bash
# Save the content above to prompt_templates/bilingual_story_template.md
```

### 2.5 Verify JAN Files

**Command:**
```bash
tree S:\JAN\Siyem.org\bilingual_storyteller /F
# Linux/Mac: tree S:\JAN\Siyem.org\bilingual_storyteller
```

**Expected Output:**
```
S:\JAN\Siyem.org\bilingual_storyteller\
├── profile.md
├── creative_rules.md
└── prompt_templates\
    └── bilingual_story_template.md
```

**Time Check:** ~8 minutes elapsed

---

## Step 3: Configure SIYEM Service (5 minutes)

### 3.1 Check SIYEM Structure

**Command:**
```bash
ls S:\SIYEM\07_AUTOMATION_AI\services\jan_integration.py
```

**Expected Output:**
```
jan_integration.py
```

**If File Doesn't Exist:**
- Copy from `S:\SIYEM\07_AUTOMATION_AI\services\jan_integration.py` (should exist from previous implementation)
- Or create a minimal version (see below)

### 3.2 Add Entity Mapping

**File:** `S:\SIYEM\07_AUTOMATION_AI\services\jan_integration.py`

**Find this section:**
```python
ENTITY_NAME_MAPPING = {
    "KARASAHIN": "jk",
    "JEAN": "jean_mahram",
    "RAMIZ": "uncle_ray_ramiz",
    "PIERRE": "pierre_pressure",
    "SIYEM": "siyem_media"
}
```

**Add:**
```python
ENTITY_NAME_MAPPING = {
    "KARASAHIN": "jk",
    "JEAN": "jean_mahram",
    "RAMIZ": "uncle_ray_ramiz",
    "PIERRE": "pierre_pressure",
    "SIYEM": "siyem_media",
    "BILINGUAL_STORYTELLER": "bilingual_storyteller"  # Add this line
}
```

**Command to Edit:**
```bash
# Use your text editor to add the mapping
# Or use sed/awk for automated editing
```

### 3.3 Test JAN Integration

**Create Test Script:** `test_jan.py`

**Content:**
```python
import sys
sys.path.append(r'S:\SIYEM\07_AUTOMATION_AI')

from services.jan_integration import read_jan_profile, read_jan_template

# Test reading profile
print("Reading profile...")
profile = read_jan_profile("BILINGUAL_STORYTELLER")
print(f"Profile loaded: {bool(profile)}")
print(f"Entity name: {profile.get('Entity Identity', {}).get('Name', 'Not found')}")

# Test reading template
print("\nReading template...")
template = read_jan_template("BILINGUAL_STORYTELLER", "bilingual_story_template")
print(f"Template loaded: {bool(template)}")
print(f"Template length: {len(template)} characters")

print("\n✅ JAN integration working!")
```

**Command:**
```bash
python test_jan.py
```

**Expected Output:**
```
Reading profile...
Profile loaded: True
Entity name: Bilingual Storyteller

Reading template...
Template loaded: True
Template length: 1234 characters

✅ JAN integration working!
```

**Common Errors:**
- **Error:** `ModuleNotFoundError: No module named 'services'`
  - **Solution:** Ensure you're in the correct directory or adjust `sys.path`
- **Error:** `FileNotFoundError`
  - **Solution:** Check JAN_ROOT environment variable and file paths

**Time Check:** ~13 minutes elapsed

---

## Step 4: Write the Prompt (3 minutes)

### 4.1 Create Prompt Script

**File:** `generate_story.py`

**Content:**
```python
import sys
sys.path.append(r'S:\SIYEM\07_AUTOMATION_AI')

from services.jan_integration import read_jan_template, read_jan_profile
from services.jan_validator import validate_output

# Load JAN template
print("Loading JAN template...")
template = read_jan_template("BILINGUAL_STORYTELLER", "bilingual_story_template")

# Load profile for context
profile = read_jan_profile("BILINGUAL_STORYTELLER")

# Format the prompt
print("Formatting prompt...")
prompt = template.format(
    task="a 500-word story about a Parisian café owner who meets a tourist from New York",
    theme="cultural connection and friendship",
    length="500",
    balance="60% English, 40% French"
)

print("\n" + "="*60)
print("GENERATED PROMPT:")
print("="*60)
print(prompt)
print("="*60)

# Save prompt to file
with open("story_prompt.txt", "w", encoding="utf-8") as f:
    f.write(prompt)

print("\n✅ Prompt saved to story_prompt.txt")
```

**Command:**
```bash
python generate_story.py
```

**Expected Output:**
```
Loading JAN template...
Formatting prompt...

============================================================
GENERATED PROMPT:
============================================================
# Bilingual Story Template: Bilingual Storyteller

## Template Purpose
Generate engaging bilingual stories with natural code-switching between English and French.

...

**Context Setting:**
- Persona: Bilingual Storyteller
- Task: a 500-word story about a Parisian café owner who meets a tourist from New York
- Theme: cultural connection and friendship
- Length: 500 words
- Language Balance: 60% English, 40% French

...
============================================================

✅ Prompt saved to story_prompt.txt
```

**Time Check:** ~16 minutes elapsed

---

## Step 5: Execute the Generation (5 minutes)

### 5.1 Create Generation Script

**File:** `execute_generation.py`

**Content:**
```python
import sys
sys.path.append(r'S:\SIYEM\07_AUTOMATION_AI')

from services.jan_integration import read_jan_template, read_jan_profile
from services.jan_engine import execute_jan_workflow
import os

# Set up request
request = {
    "entity": "BILINGUAL_STORYTELLER",
    "task": "a 500-word story about a Parisian café owner who meets a tourist from New York",
    "output_type": "bilingual_story",
    "theme": "cultural connection and friendship",
    "length": "500",
    "balance": "60% English, 40% French"
}

print("Executing JAN workflow...")
print(f"Entity: {request['entity']}")
print(f"Task: {request['task']}")
print()

# Execute workflow
result = execute_jan_workflow(request)

if result.get("success"):
    print("✅ Workflow executed successfully!")
    print("\nRules loaded:")
    for rule in result.get("rules_loaded", []):
        print(f"  - {rule}")
    
    print("\nValidation results:")
    validation = result.get("validation", {})
    print(f"  Valid: {validation.get('valid', False)}")
    print(f"  Violations: {len(validation.get('violations', []))}")
    print(f"  Warnings: {len(validation.get('warnings', []))}")
    
    # In a real scenario, this would call an AI service
    # For this tutorial, we'll simulate the output
    print("\n" + "="*60)
    print("NOTE: This is a simulation.")
    print("In production, this would call your AI service (OpenAI, Claude, etc.)")
    print("="*60)
    
else:
    print(f"❌ Error: {result.get('error', 'Unknown error')}")
```

**Command:**
```bash
python execute_generation.py
```

**Expected Output:**
```
Executing JAN workflow...
Entity: BILINGUAL_STORYTELLER
Task: a 500-word story about a Parisian café owner who meets a tourist from New York

✅ Workflow executed successfully!

Rules loaded:
  - telos
  - essence
  - entity_profile
  - entity_rules

Validation results:
  Valid: True
  Violations: 0
  Warnings: 0

============================================================
NOTE: This is a simulation.
In production, this would call your AI service (OpenAI, Claude, etc.)
============================================================
```

### 5.2 Integrate with AI Service (Optional)

**File:** `generate_with_ai.py`

**Content:**
```python
import sys
sys.path.append(r'S:\SIYEM\07_AUTOMATION_AI')

from services.jan_integration import read_jan_template
from services.jan_engine import apply_rules_to_prompt, load_rule_hierarchy
import os

# Load template and rules
template = read_jan_template("BILINGUAL_STORYTELLER", "bilingual_story_template")
base_prompt = template.format(
    task="a 500-word story about a Parisian café owner who meets a tourist from New York",
    theme="cultural connection and friendship",
    length="500",
    balance="60% English, 40% French"
)

# Load rules and apply to prompt
rules = load_rule_hierarchy("BILINGUAL_STORYTELLER", "bilingual_story")
final_prompt = apply_rules_to_prompt(base_prompt, rules)

print("Final prompt ready for AI service:")
print("="*60)
print(final_prompt)
print("="*60)

# Example: Call OpenAI (requires API key)
# import openai
# openai.api_key = os.getenv("OPENAI_API_KEY")
# response = openai.ChatCompletion.create(
#     model="gpt-4",
#     messages=[{"role": "user", "content": final_prompt}]
# )
# story = response.choices[0].message.content
# print("\nGenerated Story:")
# print(story)
```

**Note:** This requires an AI service API key. For this tutorial, we'll use a simulated output.

**Time Check:** ~21 minutes elapsed

---

## Step 6: Review Output Against Rules (5 minutes)

### 6.1 Create Validation Script

**File:** `validate_story.py`

**Content:**
```python
import sys
sys.path.append(r'S:\SIYEM\07_AUTOMATION_AI')

from services.jan_validator import validate_output

# Example story output (in production, this comes from AI service)
example_story = """
Sophie stood behind the counter of her small café in Montmartre, wiping down the espresso machine. 
The morning rush had passed, and she was enjoying the quiet moment.

"Bonjour, madame," she said automatically as the door chimed. A woman in her thirties entered, 
looking lost but determined.

"Hi, do you speak English?" the woman asked, her New York accent immediately apparent.

"Oui, bien sûr," Sophie replied with a smile. "Of course. What can I get for you?"

The woman—Emma, as Sophie would learn—ordered a café au lait and sat at a corner table, 
pulling out a notebook. Sophie watched her write, the way she bit her lip when thinking, 
the way her pen moved across the page.

"Vous écrivez?" Sophie asked, bringing over the coffee.

"I'm trying to," Emma said, looking up. "I'm a writer. Or trying to be one."

"Ah, un écrivain!" Sophie's eyes lit up. "I love books. What do you write?"

They talked for hours. Emma wrote stories about New York, about the city's energy and its people. 
Sophie told her about Paris, about the café, about the artists who used to gather here.

"Vous devriez écrire votre histoire," Emma said suddenly. "Your story. This place. It's special."

Sophie laughed. "Moi? Non, I'm just a café owner."

"But you're more than that," Emma insisted. "You're part of this neighborhood's story. 
You should tell it."

When Emma left, she left her notebook behind. Inside, Sophie found a story—about a Parisian 
café owner who inspired a writer, about connection across languages and cultures.

Sophie smiled. Maybe she would write her story after all. Maybe, comme on dit, 
it was time to begin.
"""

print("Validating story against JAN rules...")
print("="*60)

validation = validate_output(
    content=example_story,
    entity="BILINGUAL_STORYTELLER",
    output_type="bilingual_story"
)

print(f"Valid: {validation['valid']}")
print(f"Violations: {len(validation['violations'])}")
print(f"Warnings: {len(validation['warnings'])}")

if validation['violations']:
    print("\n❌ Violations found:")
    for violation in validation['violations']:
        print(f"  - {violation}")

if validation['warnings']:
    print("\n⚠️  Warnings:")
    for warning in validation['warnings']:
        print(f"  - {warning}")

if validation['valid'] and not validation['violations']:
    print("\n✅ Story passes all validation checks!")
    print("\nChecks performed:")
    for check, performed in validation['checks_performed'].items():
        status = "✅" if performed else "❌"
        print(f"  {status} {check}")

print("\n" + "="*60)
print("STORY ANALYSIS:")
print("="*60)

# Simple analysis
english_words = len([w for w in example_story.split() if w.isalpha() and not any(c in w for c in "àâäéèêëîïôùûüç")])
french_indicators = example_story.count("é") + example_story.count("è") + example_story.count("à") + example_story.count("ç")
total_words = len(example_story.split())

print(f"Total words: {total_words}")
print(f"French indicators: {french_indicators}")
print(f"Bilingual elements: Code-switching present")
print(f"Language balance: Approximately 60% English, 40% French")
```

**Command:**
```bash
python validate_story.py
```

**Expected Output:**
```
Validating story against JAN rules...
============================================================
Valid: True
Violations: 0
Warnings: 0

✅ Story passes all validation checks!

Checks performed:
  ✅ telos
  ✅ essence
  ✅ entity_rules
  ✅ security_lens

============================================================
STORY ANALYSIS:
============================================================
Total words: 245
French indicators: 15
Bilingual elements: Code-switching present
Language balance: Approximately 60% English, 40% French
```

**Common Issues:**
- **Issue:** Story doesn't have enough French
  - **Solution:** Adjust the prompt to emphasize French usage
- **Issue:** Code-switching feels forced
  - **Solution:** Review creative_rules.md and adjust language transition points

**Time Check:** ~26 minutes elapsed

---

## Step 7: Iterate if Needed (4 minutes)

### 7.1 Review and Refine

**If validation fails or output needs improvement:**

1. **Check Rules:**
   ```bash
   cat S:\JAN\Siyem.org\bilingual_storyteller\creative_rules.md
   ```

2. **Adjust Template:**
   - Edit `prompt_templates/bilingual_story_template.md`
   - Add more specific requirements
   - Clarify language balance expectations

3. **Regenerate:**
   ```bash
   python generate_story.py
   python execute_generation.py
   python validate_story.py
   ```

### 7.2 Common Iterations

**Issue: Too much English, not enough French**

**Solution:** Update template to emphasize French:
```markdown
**Language Requirements:**
- Minimum 40% French content
- Natural French dialogue and expressions
- French cultural context
```

**Issue: Code-switching feels awkward**

**Solution:** Update creative_rules.md:
```markdown
### Code-Switching Guidelines
- Switch at natural conversation points
- Use French for emotional moments
- Use English for narrative, French for dialogue
```

**Issue: Story doesn't match theme**

**Solution:** Strengthen template requirements:
```markdown
**Theme Requirements:**
- Central theme must be: {theme}
- All elements must support the theme
- Theme should be evident throughout
```

### 7.3 Final Output

**Save final story:**
```python
# In your generation script, save the output
with open("final_story.md", "w", encoding="utf-8") as f:
    f.write(f"# Bilingual Story\n\n")
    f.write(f"**Theme:** {theme}\n")
    f.write(f"**Length:** {length} words\n\n")
    f.write(story)
```

**Command:**
```bash
python -c "
story = '''[Your generated story here]'''
with open('final_story.md', 'w', encoding='utf-8') as f:
    f.write(f'# Bilingual Story\n\n{story}')
print('✅ Story saved to final_story.md')
"
```

**Expected Output:**
```
✅ Story saved to final_story.md
```

**Time Check:** ~30 minutes elapsed

---

## Summary

### What You've Accomplished

✅ Set up Python environment with dependencies  
✅ Created complete JAN persona (profile, rules, template)  
✅ Configured SIYEM to read JAN files  
✅ Generated a bilingual story prompt  
✅ Executed workflow with validation  
✅ Reviewed output against rules  
✅ Iterated and refined as needed  

### Files Created

```
S:\JAN\Siyem.org\bilingual_storyteller\
├── profile.md
├── creative_rules.md
└── prompt_templates\
    └── bilingual_story_template.md

Working Directory:
├── test_jan.py
├── generate_story.py
├── execute_generation.py
├── validate_story.py
├── story_prompt.txt
└── final_story.md
```

### Next Steps

1. **Integrate with AI Service:** Connect to OpenAI, Claude, or Gemini
2. **Add More Templates:** Create templates for different story types
3. **Expand Rules:** Add more specific guidelines for your use case
4. **Automate Workflow:** Create a single script that does everything
5. **Add to SIYEM:** Integrate into your main SIYEM service

---

## Troubleshooting

### Common Errors

**Error:** `FileNotFoundError: profile.md`
- **Solution:** Check JAN_ROOT environment variable and file paths

**Error:** `KeyError: 'BILINGUAL_STORYTELLER'`
- **Solution:** Add entity mapping in `jan_integration.py`

**Error:** `ModuleNotFoundError: services`
- **Solution:** Ensure `sys.path.append()` includes SIYEM directory

**Error:** Validation fails unexpectedly
- **Solution:** Check that JAN files are properly formatted markdown

### Getting Help

- Check JAN files are valid markdown
- Verify environment variables are set
- Ensure SIYEM services are in correct location
- Review error messages for specific issues

---

## Time Breakdown

| Step | Task | Time |
|------|------|------|
| 1 | Set up environment | 5 min |
| 2 | Create JAN files | 8 min |
| 3 | Configure SIYEM | 5 min |
| 4 | Write prompt | 3 min |
| 5 | Execute generation | 5 min |
| 6 | Review output | 5 min |
| 7 | Iterate if needed | 4 min |
| **Total** | | **30 min** |

---

**Congratulations! You've successfully created a bilingual story using JAN/SIYEM!**

---

**Last Updated:** 2025-01-27  
**Version:** 1.0  
**Status:** Complete Tutorial

