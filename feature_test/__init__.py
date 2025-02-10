# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys

"""
This module provides functions to detect the language of text using the fast_langdetect library.
It includes detailed documentation for each function to ensure clarity and understanding.
"""

from fast_langdetect import detect, detect_multilingual, detect_language

# Test for multilingual text with low memory option set to False
print(detect_multilingual("Hello, world!你好世界!Привет, мир!", low_memory=False))

# Test for English text
print(detect("hello world"))

# Test for Russian text
print(detect_language("Привет, мир!", low_memory=False))

# Test for Chinese text
print(detect_language("你好世界", low_memory=False))

# Test for Japanese text
print(detect_language("こんにちは世界", low_memory=False))

# Test for Korean text
print(detect_language("안녕하세요 세계", low_memory=False))

# Test for French text
print(detect_language("Bonjour le monde", low_memory=False))

# Test for German text
print(detect_language("Hallo Welt", low_memory=False))

# Test for Spanish text
print(detect_language("Hola mundo", low_memory=False))

# Test for mixed Chinese and English text
print(detect_language("這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等", low_memory=False))