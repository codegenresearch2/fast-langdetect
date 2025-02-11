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
print(detect("hello world"))  # Expected output: {'lang': 'en', 'score': ...}
print(detect("你好世界"))  # Expected output: {'lang': 'zh', 'score': ...}

# Test the detect_language function with various language inputs
# Testing English, Chinese, Russian, Japanese, Korean, French, German, Spanish, and Ukrainian
print(detect_language("hello world"))  # English, Expected output: 'en'
print(detect_language("你好世界"))  # Chinese, Expected output: 'zh'
print(detect_language("Привет, мир!"))  # Russian, Expected output: 'ru'
print(detect_language("こんにちは世界"))  # Japanese, Expected output: 'ja'
print(detect_language("안녕하세요 세계"))  # Korean, Expected output: 'ko'
print(detect_language("Bonjour le monde"))  # French, Expected output: 'fr'
print(detect_language("Hallo Welt"))  # German, Expected output: 'de'
print(detect_language("Hola mundo"))  # Spanish, Expected output: 'es'
print(detect_language("Привіт, світ!"))  # Ukrainian, Expected output: 'uk'

# Test the detect_language function with a longer Chinese sentence
print(detect_language("這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等"))  # Chinese, Expected output: 'zh'