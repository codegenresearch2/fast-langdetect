# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys
# @File    : __init__.py
# @Software: PyCharm
from fast_langdetect import detect, detect_multilingual, detect_langs
from fast_langdetect import parse_sentence

# Testing different languages
print(parse_sentence("你好世界"))  # Chinese
print(parse_sentence("こんにちは世界"))  # Japanese
print(parse_sentence("안녕하세요 세계"))  # Korean
print(parse_sentence("Bonjour le monde"))  # French
print(parse_sentence("Hallo Welt"))  # German
print(parse_sentence("Hello, world!"))  # English
print(parse_sentence("Привет, мир!"))  # Russian

# Detecting languages in a single call
print(detect_multilingual("Hello, world!你好世界!Привет, мир!"))

# Detecting languages individually
print(detect("hello world"))  # English
print(detect("你好世界"))  # Chinese
print(detect("こんにちは世界"))  # Japanese
print(detect("안녕하세요 세계"))  # Korean
print(detect("Bonjour le monde"))  # French
print(detect("Hallo Welt"))  # German
print(detect("Привет, мир!"))  # Russian

# Detecting language codes
print(detect_langs("Привет, мир!"))