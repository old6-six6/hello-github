# -*- coding: utf-8 -*-
"""
hello_github.py —— 我的第一个开源小程序

它能做两件事：

  1. 向你打个招呼
  2. 顺便当一当加法计算器

用法：

  python hello_github.py              # 打招呼
  python hello_github.py 3 5          # 计算 3 + 5

作者：old6-six6
"""

import sys


def greet(name="GitHub"):
    """返回一句问候语。"""
    return f"Hello, {name}! 欢迎来到开源世界。"


def add(a, b):
    """把两个数相加，返回结果。"""
    return a + b


def pretty(number):
    """让输出更好看：3.0 显示成 3，3.5 还是 3.5。"""
    if number == int(number):
        return int(number)
    return number


def main():
    args = sys.argv[1:]

    # 传了两个参数 → 进入计算器模式
    if len(args) == 2:
        try:
            a = float(args[0])
            b = float(args[1])
        except ValueError:
            print("参数必须是数字哦，例如：python hello_github.py 3 5")
            return 1

        print(f"{pretty(a)} + {pretty(b)} = {pretty(add(a, b))}")
        return 0

    # 其他情况 → 打招呼
    print(greet())
    print("想试试加法？运行：python hello_github.py 3 5")
    return 0


if __name__ == "__main__":
    sys.exit(main())
