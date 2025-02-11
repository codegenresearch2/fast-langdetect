# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys

"""
This module provides functions to detect the language of text using the fast_langdetect library.
It includes detailed documentation for each function to ensure clarity and understanding.
"""

from fast_langdetect import detect, detect_multilingual, detect_language

# 测试繁体，简体，日文，英文，韩文，法文，德文，西班牙文
print("测试多语言检测:")
print(detect_multilingual("Hello, world!你好世界!Привет, мир!", low_memory=False))

print("\n测试英文检测:")
print(detect("hello world"))

print("\n测试俄文检测:")
print(detect_language("Привет, мир!"))

print("\n测试中文检测:")
print(detect_language("你好世界"))

print("\n测试日文检测:")
print(detect_language("こんにちは世界"))

print("\n测试韩文检测:")
print(detect_language("안녕하세요 세계"))

print("\n测试法文检测:")
print(detect_language("Bonjour le monde"))

print("\n测试德文检测:")
print(detect_language("Hallo Welt"))

print("\n测试西班牙文检测:")
print(detect_language("Hola mundo"))

print("\n测试混合中文和英文检测:")
print(detect_language("這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等"))