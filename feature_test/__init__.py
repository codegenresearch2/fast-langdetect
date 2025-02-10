# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys

"""
This module contains the rewritten code snippet that addresses the feedback received.
"""

from fast_langdetect import detect, detect_multilingual, detect_language

# Testing detect_multilingual function with multiple languages
# Expected output: [{'lang': 'en', 'score': 0.9999999999999999}, {'lang': 'zh', 'score': 0.9999999999999999}, {'lang': 'ru', 'score': 0.9999999999999999}]
print("Testing detect_multilingual with English, Chinese, and Russian:")
print(detect_multilingual("Hello, world!你好世界!Привет, мир!", low_memory=False))

# Testing detect_multilingual function with the same input for consistency
print("Testing detect_multilingual with the same input for consistency:")
print(detect_multilingual("Hello, world!你好世界!Привет, мир!"))

# Testing detect function with English and Chinese inputs
print("Testing detect function with English and Chinese inputs:")
print(detect("hello world"))
print(detect("你好世界"))

# Testing detect_language function with various languages
print("Testing detect_language function with English, Russian, Japanese, Korean, French, German, Spanish, and Traditional Chinese inputs:")
print(detect_language("Привет, мир!"))
print(detect_language("こんにちは世界"))
print(detect_language("안녕하세요 세계"))
print(detect_language("Bonjour le monde"))
print(detect_language("Hallo Welt"))
print(detect_language("Hola mundo"))
print(detect_language("這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等"))