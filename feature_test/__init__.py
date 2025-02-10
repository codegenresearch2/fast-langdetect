# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys

"""
This module contains functions for detecting the language of a given text.
"""

from fast_langdetect import detect, detect_multilingual, detect_language

# Test detect_multilingual function with a multilingual input and low_memory parameter
# Expected output: [{'lang': 'en', 'score': ...}, {'lang': 'zh', 'score': ...}, {'lang': 'ru', 'score': ...}]
print(detect_multilingual("Hello, world!你好世界!Привет, мир!"))
print(detect_multilingual("Hello, world!你好世界!Привет, мир!", low_memory=False))

# Test detect function with English input
# Expected output: {'lang': 'en', 'score': ...}
print(detect("hello world"))

# Test detect_language function with various language inputs
# Expected output: 'RU'
print(detect_language("Привет, мир!"))
# Expected output: 'ZH'
print(detect_language("你好世界"))
# Expected output: 'JA'
print(detect_language("こんにちは世界"))
# Expected output: 'KO'
print(detect_language("안녕하세요 세계"))
# Expected output: 'FR'
print(detect_language("Bonjour le monde"))
# Expected output: 'DE'
print(detect_language("Hallo Welt"))
# Expected output: 'ES'
print(detect_language("Hola mundo"))
# Expected output: 'ZH'
print(detect_language("這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等"))

# No error handling section is included in the gold code, so it's removed from this version