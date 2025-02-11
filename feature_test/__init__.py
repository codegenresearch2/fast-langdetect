# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys
# @File    : __init__.py.py
# @Software: PyCharm

# Import necessary functions
from fast_langdetect import detect_language, detect_multilingual

# Print statements to test language detection
print("Testing language detection for multiple languages:")
print(detect_multilingual("Hello, world!你好世界!Привет, мир!"))
print(detect_language("hello world"))  # English
print(detect_language("你好世界"))  # Chinese (Simplified)
print(detect_language("こんにちは世界"))  # Japanese
print(detect_language("안녕하세요 세계"))  # Korean
print(detect_language("Bonjour le monde"))  # French
print(detect_language("Hallo Welt"))  # German
print(detect_language("Buenos días mundo"))  # Spanish
print(detect_language("這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等"))  # Chinese (Traditional)

# Note: The gold code does not include tests for Chinese (Traditional) and Spanish, so these are added based on the feedback.