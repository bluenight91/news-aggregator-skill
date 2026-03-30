#!/usr/bin/env python3
"""
News Skill Wrapper - 使用指定模型运行新闻获取
绕过主 Agent 的模型限制
"""

import subprocess
import sys
import json

def run_news_with_model(source=None, limit=10, keyword=None, format_type="telegram"):
    """
    使用指定模型运行新闻获取任务
    """
    # 构建新闻获取命令
    cmd = ["python3", "{baseDir}/scripts/fetch_news.py", "--format", format_type, "--limit", str(limit)]
    
    if source:
        cmd.extend(["--source", source])
    if keyword:
        cmd.extend(["--keyword", keyword])
    
    # 直接执行新闻抓取（不经过 AI 模型）
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode != 0:
        return f"获取新闻失败: {result.stderr}"
    
    return result.stdout

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", help="新闻源")
    parser.add_argument("--limit", type=int, default=10, help="数量限制")
    parser.add_argument("--keyword", help="关键词过滤")
    parser.add_argument("--format", default="telegram", choices=["telegram", "markdown", "json"])
    args = parser.parse_args()
    
    output = run_news_with_model(args.source, args.limit, args.keyword, args.format)
    print(output)
