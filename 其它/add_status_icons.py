#!/usr/bin/env python3
import os
import re

# Define the minimum size in bytes for a file to be considered "completed"
MIN_COMPLETED_SIZE = 2000  # 2KB is a reasonable threshold for completed content

# Define the icons for completed and incomplete files
COMPLETED_ICON = "✅"
INCOMPLETE_ICON = "⬜"

def get_completion_status(file_path):
    """Determine if a file is completed based on its size and content."""
    try:
        if not os.path.exists(file_path):
            return False
            
        # Check file size
        file_size = os.path.getsize(file_path)
        if file_size < MIN_COMPLETED_SIZE:
            return False
            
        # Check content - if the file contains substantial text beyond the template
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # If the file has template placeholders like "<!-- 在此处填写章节内容 -->"
        # or just has headers without substantial content
        if "<!-- 在此处填写章节内容 -->" in content:
            return False
            
        # Check for substantial content in the 正文 section
        if "## 正文" in content:
            sections = content.split("## 正文")
            if len(sections) > 1:
                # If there's less than 500 characters in the 正文 section, consider incomplete
                if len(sections[1].split("## ")[0].strip()) < 500:
                    return False
                    
        return True
    except Exception as e:
        print(f"Error checking file {file_path}: {e}")
        return False

def update_filenames_in_directory(directory):
    """Add completion status icons to filenames in the specified directory."""
    
    # Get list of markdown files in the directory
    for filename in os.listdir(directory):
        if filename.endswith('.md') and not filename == 'README.md':
            file_path = os.path.join(directory, filename)
            
            # Determine if the file is completed
            is_completed = get_completion_status(file_path)
            
            # If the filename already has an icon, remove it
            if filename.startswith(COMPLETED_ICON) or filename.startswith(INCOMPLETE_ICON):
                new_filename = filename[1:]  # Remove the first character (icon)
            else:
                new_filename = filename
                
            # Add the appropriate icon
            icon = COMPLETED_ICON if is_completed else INCOMPLETE_ICON
            new_filename = f"{icon}{new_filename}"
            
            # Rename the file
            if new_filename != filename:
                new_file_path = os.path.join(directory, new_filename)
                os.rename(file_path, new_file_path)
                print(f"Renamed: {filename} → {new_filename}")

def main():
    """Main function to process all part directories."""
    # Process each PART directory
    for part in range(1, 6):
        directory = f"PART{part}"
        if os.path.exists(directory) and os.path.isdir(directory):
            print(f"Processing {directory}...")
            update_filenames_in_directory(directory)
            
    print("Finished adding status icons to all chapter files!")

if __name__ == "__main__":
    main() 