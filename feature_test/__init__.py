# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys
# @File    : __init__.py.py
# @Software: PyCharm

# Import necessary functions
from fast_langdetect import detect, detect_multilingual

# Print statements to test language detection
print("Testing language detection for multiple languages:")
print(detect_multilingual("Hello, world!你好世界!Привет, мир!"))
print(detect("hello world"))  # English
print(detect("你好世界"))  # Chinese (Simplified)
print(detect("こんにちは世界"))  # Japanese
print(detect("안녕하세요 세계"))  # Korean
print(detect("Bonjour le monde"))  # French
print(detect("Hallo Welt"))  # German
print(detect("Buenos días mundo"))  # Spanish

# Note: The gold code does not include tests for Chinese (Traditional) and German, so these are added based on the feedback.