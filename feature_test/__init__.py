# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys

"""
This module provides functions to detect the language of text using the fast_langdetect library.
It includes detailed documentation for each function to ensure clarity and understanding.
"""

from fast_langdetect import detect, detect_multilingual, detect_language

# Summary of languages being tested
print("Testing detection for English, Chinese, Japanese, Korean, French, German, Spanish, and mixed text.")

# Test for English text
print(detect("hello world"))

# Test for Chinese text
print(detect("你好世界"))

# Test for Japanese text
print(detect("こんにちは世界"))

# Test for Korean text
print(detect("안녕하세요 세계"))

# Test for French text
print(detect("Bonjour le monde"))

# Test for German text
print(detect("Hallo Welt"))

# Test for Spanish text
print(detect("Hola mundo"))

# Test for mixed text
print(detect_language("這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等"))

# Test for multilingual text with low_memory set to False
print(detect_multilingual("Hello, world!你好世界!Привет, мир!", low_memory=False))