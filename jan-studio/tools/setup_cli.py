"""
Setup JAN CLI

Creates a 'jan' command that can be run from anywhere.
"""

import os
import sys
import shutil
from pathlib import Path

def setup_cli():
    """Set up the jan CLI command."""
    tools_dir = Path(__file__).parent
    cli_script = tools_dir / "jan_cli.py"
    
    # Determine where to install
    if sys.platform == "win32":
        # Windows: Add to user's Scripts directory or create batch file
        scripts_dir = Path.home() / "AppData" / "Local" / "Programs" / "Python" / "Scripts"
        if not scripts_dir.exists():
            scripts_dir = Path.home() / ".local" / "bin"
            scripts_dir.mkdir(parents=True, exist_ok=True)
        
        # Create batch file
        batch_file = scripts_dir / "jan.bat"
        with open(batch_file, 'w') as f:
            f.write(f'@echo off\n')
            f.write(f'python "{cli_script}" %*\n')
        
        print(f"✅ Created: {batch_file}")
        print(f"\nAdd to PATH:")
        print(f"  {scripts_dir}")
    else:
        # Unix-like: Create symlink or script
        local_bin = Path.home() / ".local" / "bin"
        local_bin.mkdir(parents=True, exist_ok=True)
        
        # Create wrapper script
        wrapper = local_bin / "jan"
        with open(wrapper, 'w') as f:
            f.write("#!/usr/bin/env python3\n")
            f.write(f"import sys\n")
            f.write(f"sys.path.insert(0, r'{tools_dir}')\n")
            f.write(f"from jan_cli import main\n")
            f.write(f"if __name__ == '__main__':\n")
            f.write(f"    main()\n")
        
        # Make executable
        os.chmod(wrapper, 0o755)
        
        print(f"✅ Created: {wrapper}")
        print(f"\nAdd to PATH:")
        print(f"  export PATH=\"$HOME/.local/bin:$PATH\"")
        print(f"\nOr add to ~/.bashrc or ~/.zshrc:")
        print(f"  echo 'export PATH=\"$HOME/.local/bin:$PATH\"' >> ~/.bashrc")


if __name__ == "__main__":
    setup_cli()

