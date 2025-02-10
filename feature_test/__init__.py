# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys

"""
This module provides functions to detect the language of text using the fast_langdetect library.
It includes detailed documentation for each function to ensure clarity and understanding.
"""

from fast_langdetect import detect_language, detect_multilingual

# Summary of languages being tested
print("Testing detection for English, Chinese (Traditional), Japanese, Korean, French, German, Spanish, and mixed text.")

# Test for English text
print(detect_language("hello world"))

# Test for Chinese (Traditional) text
print(detect_language("你好世界"))

# Test for Japanese text
print(detect_language("こんにちは世界"))

# Test for Korean text
print(detect_language("안녕하세요 세계"))

# Test for French text
print(detect_language("Bonjour le monde"))

# Test for German text
print(detect_language("Hallo Welt"))

# Test for Spanish text
print(detect_language("Hola mundo"))

# Test for mixed text with low_memory=False
print(detect_multilingual("Hello, world!你好世界!こんにちは世界!안녕하세요 세계!Bonjour le monde!Hallo Welt!Hola mundo!這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等", low_memory=False))