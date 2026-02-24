#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re

def convert_txt_to_markdown(input_dir, output_dir):
    # 确保输出目录存在
    os.makedirs(output_dir, exist_ok=True)
    
    # 遍历输入目录中的所有txt文件
    for filename in os.listdir(input_dir):
        if filename.endswith('.txt'):
            txt_path = os.path.join(input_dir, filename)
            md_filename = filename[:-4] + '.md'
            md_path = os.path.join(output_dir, md_filename)
            
            try:
                # 读取txt文件内容
                with open(txt_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # 创建markdown内容
                markdown_content = generate_markdown_content(filename[:-4], content)
                
                # 写入markdown文件
                with open(md_path, 'w', encoding='utf-8') as f:
                    f.write(markdown_content)
                
                print(f"Successfully converted: {filename} -> {md_filename}")
            
            except Exception as e:
                print(f"Error converting {filename}: {e}")

def generate_markdown_content(title, content):
    # 提取视频编号和标题
    number_match = re.search(r'【([^\】]+)】', title)
    if number_match:
        video_number = number_match.group(1)
        clean_title = title.replace(f"【{video_number}】", "").strip()
    else:
        video_number = ""
        clean_title = title
    
    # 构建markdown内容
    markdown = f"---\ntitle: \"{title}\"\ndate: \"2026-02-24\"\ncategory: \"公孙田浩\"\ntags: [\"视频笔记\", \"调查实录\", \"黑产博弈\"]\nauthor: \"公孙田浩\"\n---\n\n# {title}\n\n"
    
    # 处理内容格式
    # 替换换行符
    content = content.replace('\r\n', '\n')
    content = content.replace('\r', '\n')
    
    # 简单的格式化
    lines = content.split('\n')
    for i, line in enumerate(lines):
        line = line.strip()
        if line:
            # 检查是否是标题
            if len(line) <= 30 and line.isupper() or line.startswith('===') or line.endswith('==='):
                markdown += f"## {line}\n\n"
            elif line.startswith('###') or line.startswith('##') or line.startswith('#'):
                markdown += f"{line}\n\n"
            # 检查是否是列表
            elif line.startswith('•') or line.startswith('*') or line.startswith('-') or line.startswith('1.') or line.startswith('2.') or line.startswith('3.'):
                markdown += f"{line}\n"
            else:
                markdown += f"{line}\n\n"
    
    return markdown

if __name__ == "__main__":
    input_directory = "/root/.openclaw/workspace/notebook/10-视频资料/公孙田浩"
    output_directory = "/root/.openclaw/workspace/notebook/公孙田浩视频笔记"
    
    convert_txt_to_markdown(input_directory, output_directory)
    
    print("Conversion completed!")
