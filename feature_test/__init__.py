# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys
# @File    : __init__.py.py
# @Software: PyCharm
from fast_langdetect import detect_language, detect_multilingual

# Using the exact function names as in the gold code
print(detect_language("你好世界"))
print(detect_language("你好世界！Hello, world！Привет, мир！"))

# Adding more test cases that include different languages
print(detect_language("Bonjour le monde"))
print(detect_language("Hola, mundo"))
print(detect_language("Hallo Welt"))
print(detect_language("안녕하세요 세계"))
print(detect_language("こんにちは世界"))
print(detect_language("这些机构主办的课程，多以基本电脑使用为主，例如文书处理、中文输入、互联网应用等"))

# Using detect_multilingual for multiple sentences
results = detect_multilingual("Hello, world!你好世界!Привет, мир!")
# Expected output format: [{'lang': 'en', 'prob': 0.9999999999999999}, {'lang': 'zh', 'prob': 0.9999999999999999}, {'lang': 'ru', 'prob': 0.9999999999999999}]
print(results)

# Adding comments to improve clarity
# Testing language detection for single sentences
print(detect_language("hello world"))
print(detect_language("Привет, мир!"))

# Testing language detection for multiple sentences
print(detect_multilingual("Hello, world!Привет, мир!"))