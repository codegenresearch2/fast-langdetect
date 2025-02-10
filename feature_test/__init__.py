# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys
# @File    : __init__.py.py
# @Software: PyCharm

from fast_langdetect import detect_language, detect_multilingual, detect
from fast_langdetect import parse_sentence

# Comment describing the languages being tested
print("Testing language detection with various languages: English, Spanish, Traditional Chinese, Japanese, Korean, French, and German.")

# Directly use the functions without additional wrapper functions
print(parse_sentence("你好世界"))  # Traditional Chinese
print(parse_sentence("こんにちは世界"))  # Japanese
print(parse_sentence("안녕하세요 세계"))  # Korean
print(parse_sentence("Bonjour le monde"))  # French
print(parse_sentence("Hallo Welt"))  # German
print(parse_sentence("Hello, world!"))  # English
print(parse_sentence("¡Hola, mundo!"))  # Spanish

print(detect_multilingual("Hello, world!你好世界!Привет, мир!¡Hola, mundo!Bonjour le monde"))

# Add more language tests
print(detect_language("hello world"))  # English
print(detect_language("こんにちは世界"))  # Japanese
print(detect_language("안녕하세요 세계"))  # Korean
print(detect_language("Bonjour le monde"))  # French
print(detect_language("Hallo Welt"))  # German
print(detect_language("你好世界"))  # Traditional Chinese
print(detect_language("¡Hola, mundo!"))  # Spanish