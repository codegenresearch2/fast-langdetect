# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys

"""
This module contains functions for detecting the language of a given text.
"""

from fast_langdetect import detect, detect_multilingual, detect_language

# Test detect_multilingual function with a multilingual input and low_memory parameter
print(detect_multilingual("Hello, world!你好世界!Привет, мир!", low_memory=False))

# Test detect function with English input
print(detect("hello world"))

# Test detect_language function with various language inputs
print(detect_language("Привет, мир!"))
print(detect_language("你好世界"))
print(detect_language("こんにちは世界"))
print(detect_language("안녕하세요 세계"))
print(detect_language("Bonjour le monde"))
print(detect_language("Hallo Welt"))
print(detect_language("Hola mundo"))
print(detect_language("這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等"))

# Test error handling of the detect function
try:
    detect("hello world\nNEW LINE", low_memory=True)
except Exception as e:
    print(f"Caught exception: {e}")