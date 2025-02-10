# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys
# @File    : __init__.py.py
# @Software: PyCharm

# Import necessary functions from fast_langdetect
from fast_langdetect import detect, detect_language, detect_multilingual

# Testing language detection for various languages

# English using detect function
print(detect("hello world"))

# Chinese
print(detect_language("你好世界"))

# Multilingual sentence
print(detect_language("你好世界！Hello, world！Привет, мир！"))

# Russian
print(detect_multilingual("Привет, мир!"))

# Japanese
print(detect_language("こんにちは世界"))

# Korean
print(detect_language("안녕하세요 세계"))

# French
print(detect_language("Bonjour le monde"))

# German
print(detect_language("Hallo Welt"))

# Spanish
print(detect_language("Hola mundo"))

# Multilingual detection
print(detect_multilingual("Hello, world!你好世界!Привет, мир!"))

# Complex Chinese sentence
print(detect_language("這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等"))