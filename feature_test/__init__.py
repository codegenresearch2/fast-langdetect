# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys
# @File    : __init__.py.py
# @Software: PyCharm
from fast_langdetect import detect, detect_language, detect_multilingual

# Testing language detection for single sentences
print(detect("hello world"))
print(detect("Привет, мир!"))

# Testing language detection for multiple sentences
print(detect_multilingual("Hello, world!你好世界!Привет, мир!"))

# Testing language detection for single sentences using detect_language
print(detect_language("Bonjour le monde"))
print(detect_language("Hola, mundo"))
print(detect_language("Hallo Welt"))
print(detect_language("안녕하세요 세계"))
print(detect_language("こんにちは世界"))
print(detect_language("Привіт, світ!"))
print(detect_language("Здраво, свет!"))
print(detect_language("这些机构主办的课程，多以基本电脑使用为主，例如文书处理、中文输入、互联网应用等"))