# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys
# @File    : __init__.py
# @Software: PyCharm
from fast_langdetect import detect, detect_language, detect_multilingual

# Testing different languages
print(detect_language("hello world"))  # English
print(detect_language("你好世界"))  # Chinese
print(detect_language("こんにちは世界"))  # Japanese
print(detect_language("안녕하세요 세계"))  # Korean
print(detect_language("Bonjour le monde"))  # French
print(detect_language("Hallo Welt"))  # German
print(detect_language("Привет, мир!"))  # Russian
print(detect_language("Hola mundo"))  # Spanish

# Detecting languages in a single call
print(detect("hello world"))  # English
print(detect("你好世界"))  # Chinese
print(detect_multilingual("Hello, world!你好世界!Привет, мир!Hola mundo"))