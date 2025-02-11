# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys

"""
This module contains functions for detecting the language of a given text.
"""

from fast_langdetect import detect, detect_multilingual, detect_language

# Test the detect_multilingual function with a multilingual input
# Expected output: [{'lang': 'en', 'score': ...}, {'lang': 'zh', 'score': ...}, {'lang': 'ru', 'score': ...}]
print(detect_multilingual("Hello, world!你好世界!Привет, мир!", low_memory=True))  # Explicitly using low_memory parameter
print(detect_multilingual("Bonjour le monde!Hallo Welt!Hola mundo!", low_memory=False))  # Testing with low_memory=False

# Test the detect function with English and Chinese inputs
print(detect("hello world"))
print(detect("你好世界"))

# Test the detect_language function with various language inputs
# Testing English, Chinese, Russian, Japanese, Korean, French, German, Spanish, and Ukrainian
print(detect_language("hello world"))  # English
print(detect_language("你好世界"))  # Chinese
print(detect_language("Привет, мир!"))  # Russian
print(detect_language("こんにちは世界"))  # Japanese
print(detect_language("안녕하세요 세계"))  # Korean
print(detect_language("Bonjour le monde"))  # French
print(detect_language("Hallo Welt"))  # German
print(detect_language("Hola mundo"))  # Spanish
print(detect_language("Привіт, світ!"))  # Ukrainian