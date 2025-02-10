# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys
# @File    : __init__.py.py
# @Software: PyCharm

from fast_langdetect import detect_language, detect_multilingual

# 测试语言检测，包括英语、日语、韩语、法语、德语
print("测试语言检测，包括英语、日语、韩语、法语、德语。")

# 使用 detect_multilingual 函数进行多语言检测
result = detect_multilingual("Hello, world! こんにちは世界! 안녕하세요 세계! Bonjour le monde! Hallo Welt!")
print(f"Detected languages: {result}")

# 使用 detect_language 函数进行单语言检测
print(f"Detect 'hello world': {detect_language('hello world')}")  # 英语
print(f"Detect 'こんにちは世界': {detect_language('こんにちは世界')}")  # 日语
print(f"Detect '안녕하세요 세계': {detect_language('안녕하세요 세계')}")  # 韩语
print(f"Detect 'Bonjour le monde': {detect_language('Bonjour le monde')}")  # 法语
print(f"Detect 'Hallo Welt': {detect_language('Hallo Welt')}")  # 德语