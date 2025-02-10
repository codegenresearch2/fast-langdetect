# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys
# @File    : __init__.py.py
# @Software: PyCharm

from fast_langdetect import detect_language, detect_multilingual
from fast_langdetect import parse_sentence

# Comment describing the languages being tested
print("Testing language detection with various languages:")

# Directly use the functions without additional wrapper functions
print(parse_sentence("你好世界"))
print(parse_sentence("你好世界！Hello, world！Привет, мир！"))
print(detect_multilingual("Hello, world!你好世界!Привет, мир!"))

# Add more language tests
print(detect_language("hello world"))
print(detect_language("こんにちは世界"))
print(detect_language("안녕하세요 세계"))
print(detect_language("Bonjour le monde"))
print(detect_language("Hallo Welt"))
print(detect_language("こんにちは世界"))
print(detect_language("안녕하세요 세계"))
print(detect_language("Bonjour le monde"))