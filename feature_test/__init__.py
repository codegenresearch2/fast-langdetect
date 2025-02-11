# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys
# @File    : __init__.py.py
# @Software: PyCharm

from fast_langdetect import detect_language, detect_multilingual

# 演示多语言检测
print("Multilingual detection: ", detect_multilingual("Hello, world!你好世界!Привет, мир!"))

# 演示各种语言的检测
print("English: ", detect_language("hello world"))
print("Chinese: ", detect_language("你好世界"))
print("Japanese: ", detect_language("こんにちは世界"))
print("Korean: ", detect_language("안녕하세요 세계"))
print("French: ", detect_language("Bonjour le monde"))
print("German: ", detect_language("Hallo Welt"))
print("Spanish: ", detect_language("Hola mundo"))