# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys
# @File    : __init__.py.py
# @Software: PyCharm

from fast_langdetect import detect, detect_language, detect_multilingual

# Detect language of a single sentence
print(detect("你好世界"))

# Detect language of a multilingual sentence
print(detect_language("你好世界！Hello, world！Привет, мир！"))

# Detect languages in a multilingual sentence
print(detect_multilingual("Hello, world!你好世界!Привет, мир!"))

# Demonstrate language detection for various languages
print(detect("hello world"))
print(detect("Bonjour le monde"))
print(detect("Hallo Welt"))
print(detect("こんにちは世界"))
print(detect("안녕하세요 세계"))

# Detect languages in a sentence with multiple languages
print(detect_multilingual("Привет, мир!"))