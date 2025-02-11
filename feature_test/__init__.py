# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys
# @File    : __init__.py.py
# @Software: PyCharm
from fast_langdetect import detect, detect_multilingual

# Using the exact function names as in the gold code
print(detect("你好世界"))
print(detect("你好世界！Hello, world！Привет, мир！"))
print(detect_multilingual("Hello, world!你好世界!Привет, мир!"))

# Adding more test cases that include different languages
print(detect("Bonjour le monde"))
print(detect("Hallo Welt"))
print(detect("안녕하세요 세계"))
print(detect("こんにちは世界"))

# Ensuring the print statements reflect the expected output format
results = detect_multilingual("Hello, world!你好世界!Привет, мир!")
for result in results:
    print(f"Language: {result['lang']}, Probability: {result['prob']}")

# Adding comments to improve clarity
# Testing language detection for single sentences
print(detect("hello world"))
print(detect("Привет, мир!"))

# Testing language detection for multiple sentences
print(detect_multilingual("Hello, world!Привет, мир!"))