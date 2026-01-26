"""UPDATE SUNO PROMPTS - Remove Direct Artist References, Infuse Style Essence

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity
"""

from pathlib import Path
import re

# Style essence mapping (removes direct artist references)
STYLE_ESSENCE = {
    "J Dilla": "swing and soul, rhythmic pocket, human groove",
    "Flying Lotus": "cosmic layers, experimental textures, space and depth",
    "Nujabes": "contemplative depth, emotional resonance, lo-fi warmth",
    "Orhan Gencebay": "Turkish Arabesk longing, emotional depth, traditional soul",
    "Sezen Aksu": "vulnerability, poetic truth, emotional honesty",
    "Jeff Buckley": "intimate power, vulnerable strength, soaring emotion",
    "Bon Iver": "space and breath, minimal arrangement, emotional clarity",
    "James Blake": "minimal soul, space over clutter, emotional precision"
}

def update_prompt_file(file_path: Path) -> bool:
    """Update a single prompt file to use style essence"""
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Replace artist references with essence (case-insensitive)
        for artist, essence in STYLE_ESSENCE.items():
            # Direct name replacement
            content = content.replace(artist, essence)
            content = content.replace(artist.lower(), essence)
            content = content.replace(artist.upper(), essence)
            
            # Pattern-based replacement (handles variations)
            patterns = [
                rf'\b{re.escape(artist)}\'s\s+',
                rf'\b{re.escape(artist.lower())}\'s\s+',
                rf'\b{re.escape(artist)}\'s\s+',
            ]
            
            for pattern in patterns:
                content = re.sub(pattern, f'{essence}, ', content, flags=re.IGNORECASE)
        
        # Only write if content changed
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        
        return False
    
    except Exception as e:
        print(f"Error updating {file_path}: {e}")
        return False

def main():
    """Update all Suno prompts in the directory"""
    
    prompts_dir = Path("s:\\JAN\\SIYEM\\output\\suno_prompts")
    
    if not prompts_dir.exists():
        print(f"Directory not found: {prompts_dir}")
        return
    
    # Find all markdown and text files
    prompt_files = list(prompts_dir.glob("*.md")) + list(prompts_dir.glob("*.txt"))
    
    updated_count = 0
    skipped_count = 0
    
    print("=" * 80)
    print("UPDATING SUNO PROMPTS - Style Essence Infusion")
    print("=" * 80)
    
    for prompt_file in prompt_files:
        if "essence" in prompt_file.name:
            skipped_count += 1
            continue
        
        print(f"\n[PROCESSING] {prompt_file.name}")
        
        if update_prompt_file(prompt_file):
            print(f"  [UPDATED] Style essence infused")
            updated_count += 1
        else:
            print(f"  [SKIPPED] No artist references found or already updated")
            skipped_count += 1
    
    print("\n" + "=" * 80)
    print(f"[RESULTS]")
    print(f"Updated: {updated_count} files")
    print(f"Skipped: {skipped_count} files")
    print("=" * 80)

if __name__ == "__main__":
    main()
