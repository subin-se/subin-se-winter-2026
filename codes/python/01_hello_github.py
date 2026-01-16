#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
第一个Python程序 - Hello GitHub!
作者：subin-se
日期：2026年1月16日
描述：学习仓库的第一个程序，展示基本信息
"""

def print_header():
    """打印程序标题"""
    print("=" * 50)
    print("🌟 Hello GitHub! - 我的第一个Python程序")
    print("=" * 50)

def print_student_info():
    """打印学生信息"""
    student = {
        "name": "subin-se",
        "major": "软件工程",
        "grade": "大一",
        "university": "你的大学名称",  # 可以修改
        "start_date": "2026年1月16日"
    }
    
    print("\n👨‍🎓 学生信息:")
    for key, value in student.items():
        print(f"  {key}: {value}")

def print_learning_goals():
    """打印学习目标"""
    goals = [
        "掌握Git和GitHub工作流",
        "提升Python编程能力",
        "学习Web开发基础",
        "完成个人项目作品集",
        "准备英语四级考试",
        "建立每日学习习惯"
    ]
    
    print("\n🎯 寒假学习目标:")
    for i, goal in enumerate(goals, 1):
        print(f"  {i:2d}. {goal}")

def print_repository_info():
    """打印仓库信息"""
    repo_info = {
        "name": "subin-se-winter-2026",
        "url": "https://github.com/subin-se/subin-se-winter-2026",
        "purpose": "记录寒假学习与实践",
        "structure": """
        📁 docs/          # 学习文档
        📁 code/          # 代码练习  
        📁 projects/      # 项目实践
        📄 README.md      # 项目说明
        """,
        "tech_stack": ["Python", "Git/GitHub", "Markdown", "VSCode"]
    }
    
    print("\n📦 仓库信息:")
    print(f"  名称: {repo_info['name']}")
    print(f"  地址: {repo_info['url']}")
    print(f"  目的: {repo_info['purpose']}")
    
    print("\n🛠️ 技术栈:")
    for tech in repo_info['tech_stack']:
        print(f"  • {tech}")

def print_encouragement():
    """打印鼓励话语"""
    messages = [
        "\n💪 今日学习格言:",
        "  代码不止是工具，更是思维的表达。",
        "  每一个成功的项目，都始于第一行代码。",
        "  坚持记录，时间会给你最好的回报。",
        "",
        "🚀 开始你的编程之旅吧！",
        "=" * 50
    ]
    
    for msg in messages:
        print(msg)

def main():
    """主函数"""
    print_header()
    print_student_info()
    print_learning_goals()
    print_repository_info()
    print_encouragement()

if __name__ == "__main__":
    main()