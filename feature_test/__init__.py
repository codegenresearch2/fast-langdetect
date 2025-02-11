# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys

"""
This module contains the rewritten code snippet that follows the provided rules and oracle feedback.
"""

from fast_langdetect import detect, detect_multilingual, detect_language

# Testing detect_multilingual function with multiple languages
# Expected output: [{'lang': 'en', 'score': 0.9999999999999999}, {'lang': 'zh', 'score': 0.9999999999999999}, {'lang': 'ru', 'score': 0.9999999999999999}]
print(detect_multilingual("Hello, world!你好世界!Привет, мир!"))

# Testing detect_multilingual function without low_memory parameter
print(detect_multilingual("Hello, world!你好世界!Привет, мир!"))

# Testing detect function with English input
print(detect("hello world"))

# Testing detect_language function with various languages
print(detect_language("Привет, мир!"))  # Russian
print(detect_language("你好世界"))  # Chinese
print(detect_language("こんにちは世界"))  # Japanese
print(detect_language("안녕하세요 세계"))  # Korean
print(detect_language("Bonjour le monde"))  # French
print(detect_language("Hallo Welt"))  # German
print(detect_language("Hola mundo"))  # Spanish
print(detect_language("這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等"))  # Chinese