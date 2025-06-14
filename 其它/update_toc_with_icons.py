#!/usr/bin/env python3
import os
import re

# Define the icons for completed and incomplete files
COMPLETED_ICON = "✅"
INCOMPLETE_ICON = "⬜"

def get_file_status_icon(file_path):
    """Get the status icon from a file's name."""
    if not os.path.exists(file_path):
        return INCOMPLETE_ICON
        
    filename = os.path.basename(file_path)
    if filename.startswith(COMPLETED_ICON):
        return COMPLETED_ICON
    elif filename.startswith(INCOMPLETE_ICON):
        return INCOMPLETE_ICON
    else:
        return ""  # No icon found

def update_toc():
    """Update the table of contents with status icons."""
    
    # Read the TOC file
    toc_path = "目录.md"
    with open(toc_path, 'r', encoding='utf-8') as f:
        toc_content = f.read()
    
    # Pattern to find links in markdown: [Title](path/to/file.md)
    link_pattern = r'\[(.*?)\]\((.*?)\)'
    
    def replace_link(match):
        title = match.group(1)
        file_path = match.group(2)
        
        # Skip if it's not a .md file
        if not file_path.endswith('.md'):
            return match.group(0)
            
        # If the title already has an icon, remove it
        if title.startswith(COMPLETED_ICON) or title.startswith(INCOMPLETE_ICON):
            title = title[1:].strip()
        
        # Get the actual file path by checking for the icon in the filename
        dir_name = os.path.dirname(file_path)
        base_name = os.path.basename(file_path)
        
        # Look for the file with an icon prefix
        found_file = None
        if os.path.exists(dir_name):
            for filename in os.listdir(dir_name):
                if filename.endswith(base_name) or filename[1:] == base_name:
                    found_file = os.path.join(dir_name, filename)
                    break
        
        # Get the icon from the filename
        icon = ""
        if found_file:
            icon = get_file_status_icon(found_file)
            
            # Update file_path to the actual file with icon
            if icon:
                file_path = found_file
        else:
            icon = INCOMPLETE_ICON  # File doesn't exist
            
        return f"[{icon} {title}]({file_path})"
    
    # Update links in the TOC
    updated_toc = re.sub(link_pattern, replace_link, toc_content)
    
    # Write the updated TOC
    with open(toc_path, 'w', encoding='utf-8') as f:
        f.write(updated_toc)
    
    print(f"Updated table of contents with status icons!")

if __name__ == "__main__":
    update_toc() 