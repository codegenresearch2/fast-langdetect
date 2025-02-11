# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys

"""
This module provides functions to detect the language of text using the fast_langdetect library.
It includes detailed documentation for each function to ensure clarity and understanding.
"""

from fast_langdetect import detect, detect_multilingual, detect_language

# Test language detection with a variety of inputs
print("Testing detect_multilingual with low_memory=False:")
print(detect_multilingual("Hello, world!你好世界!Привет, мир!", low_memory=False))

print("\nTesting detect with English text:")
print(detect("hello world"))

print("\nTesting detect_language with Russian text:")
print(detect_language("Привет, мир!"))

print("\nTesting detect_language with Chinese text:")
print(detect_language("你好世界"))

print("\nTesting detect_language with Japanese text:")
print(detect_language("こんにちは世界"))

print("\nTesting detect_language with Korean text:")
print(detect_language("안녕하세요 세계"))

print("\nTesting detect_language with French text:")
print(detect_language("Bonjour le monde"))

print("\nTesting detect_language with German text:")
print(detect_language("Hallo Welt"))

print("\nTesting detect_language with Spanish text:")
print(detect_language("Hola mundo"))

print("\nTesting detect_language with mixed Chinese and English text:")
print(detect_language("這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等"))