# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys
# @File    : __init__.py.py
# @Software: PyCharm

from fast_langdetect import detect, detect_language, detect_multilingual

# Demonstrate language detection for various languages
print("English: ", detect("hello world"))
print("Chinese: ", detect("你好世界"))
print("Japanese: ", detect("こんにちは世界"))
print("Korean: ", detect("안녕하세요 세계"))
print("French: ", detect("Bonjour le monde"))
print("German: ", detect("Hallo Welt"))
print("Spanish: ", detect("Hola mundo"))

# Detect language of a multilingual sentence
print("Multilingual: ", detect_language("你好世界！Hello, world！Привет, мир！"))

# Detect languages in a multilingual sentence
print("Multilingual detection: ", detect_multilingual("Hello, world!你好世界!Привет, мир!"))