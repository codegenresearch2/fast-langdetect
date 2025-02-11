# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys

"""
This module contains functions for detecting the language of a given text.
"""

from fast_langdetect import detect, detect_multilingual, detect_language

# Test the detect_multilingual function with a multilingual input and low_memory=False
print("Detect Multilingual: ", detect_multilingual("Hello, world!你好世界!Привет, мир!", low_memory=False))

# Test the detect function with English and Chinese inputs
print("Detect English: ", detect("hello world"))
print("Detect Chinese: ", detect("你好世界"))

# Test the detect_language function with various language inputs
print("Detect Russian: ", detect_language("Привет, мир!"))
print("Detect Japanese: ", detect_language("こんにちは世界"))
print("Detect Korean: ", detect_language("안녕하세요 세계"))
print("Detect French: ", detect_language("Bonjour le monde"))
print("Detect German: ", detect_language("Hallo Welt"))
print("Detect Spanish: ", detect_language("Hola mundo"))
print("Detect Chinese (complex): ", detect_language("這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等"))

# Test the error handling of the detect function
try:
    print("Detect with new line: ", detect("hello world\nNEW LINE", low_memory=True))
except Exception as e:
    print(f"Caught exception: {e}")