#!/usr/bin/env python3
"""
News Skill Direct Runner - 绕过 AI 模型直接输出新闻
用于 /news 命令直接调用
"""

import subprocess
import sys
import os

def main():
    # 获取脚本所在目录
    script_dir = os.path.dirname(os.path.abspath(__file__))
    base_dir = os.path.dirname(script_dir)
    
    # 构建 fetch_news.py 的完整路径
    fetch_news_path = os.path.join(script_dir, "fetch_news.py")
    
    # 默认参数
    args = sys.argv[1:] if len(sys.argv) > 1 else []
    
    # 如果没有指定参数，使用默认配置
    if not args:
        args = ["--format", "telegram"]
    elif "--format" not in str(args):
        args.extend(["--format", "telegram"])
    
    # 构建命令
    cmd = ["python3", fetch_news_path] + args
    
    # 执行命令并实时输出
    result = subprocess.run(cmd, capture_output=False, text=True)
    
    return result.returncode

if __name__ == "__main__":
    sys.exit(main())
