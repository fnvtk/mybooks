#!/usr/bin/env python3
import os
import re

# 从目录文件中提取章节信息
def extract_chapter_info(content):
    chapter_info = {}
    pattern = r'\[(\d+\.\d+) ([^\]]+)\]\(([^)]+)\)'
    matches = re.findall(pattern, content)
    
    for match in matches:
        chapter_num = match[0]
        chapter_title = match[1]
        file_path = match[2]
        chapter_info[file_path] = {
            'num': chapter_num,
            'title': chapter_title
        }
    
    return chapter_info

# 读取目录文件
with open('目录.md', 'r', encoding='utf-8') as f:
    content = f.read()

# 提取章节信息
chapter_info = extract_chapter_info(content)

# 重命名文件
for file_path, info in chapter_info.items():
    if os.path.exists(file_path):
        dir_name = os.path.dirname(file_path)
        base_name = os.path.basename(file_path)
        new_file_name = f"{info['num']}-{info['title']}.md"
        new_file_path = os.path.join(dir_name, new_file_name)
        
        # 重命名文件
        os.rename(file_path, new_file_path)
        print(f"已将 {file_path} 重命名为 {new_file_path}")
    else:
        print(f"文件不存在: {file_path}")

print("重命名完成！") 