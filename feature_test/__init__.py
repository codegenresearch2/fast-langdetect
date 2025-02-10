# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys

"""
This module contains the rewritten code snippet that addresses the feedback received.
"""

from fast_langdetect import detect, detect_multilingual, detect_language

# Testing detect_multilingual function with multiple languages
# Expected output: [{'lang': 'en', 'score': 0.9999999999999999}, {'lang': 'zh', 'score': 0.9999999999999999}, {'lang': 'ru', 'score': 0.9999999999999999}]
print(detect_multilingual("Hello, world!你好世界!Привет, мир!", low_memory=False))
# Testing detect_multilingual function with the same input for consistency
print(detect_multilingual("Hello, world!你好世界!Привет, мир!"))

# Testing detect function with English and Chinese inputs
print(detect("hello world"))
print(detect("你好世界"))

# Testing detect_language function with various languages
print(detect_language("Привет, мир!"))
print(detect_language("こんにちは世界"))
print(detect_language("안녕하세요 세계"))
print(detect_language("Bonjour le monde"))
print(detect_language("Hallo Welt"))
print(detect_language("Hola mundo"))
print(detect_language("这些机构主办的课程，多以基本电脑使用为主，例如文书处理、中文输入、互联网应用等"))