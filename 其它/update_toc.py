#!/usr/bin/env python3
import os
import re

# 读取目录文件
with open('目录.md', 'r', encoding='utf-8') as f:
    content = f.read()

# 替换链接格式
def update_links(content):
    pattern = r'\[(\d+\.\d+) ([^\]]+)\]\(([^)]+)\)'
    
    def replace_link(match):
        chapter_num = match.group(1)
        chapter_title = match.group(2)
        file_path = match.group(3)
        
        dir_name = os.path.dirname(file_path)
        new_file_name = f"{chapter_num}-{chapter_title}.md"
        new_file_path = os.path.join(dir_name, new_file_name)
        
        return f"[{chapter_num} {chapter_title}]({new_file_path})"
    
    updated_content = re.sub(pattern, replace_link, content)
    return updated_content

# 更新目录文件
updated_content = update_links(content)

# 写入更新后的目录文件
with open('目录.md', 'w', encoding='utf-8') as f:
    f.write(updated_content)

print("目录文件已更新！") 