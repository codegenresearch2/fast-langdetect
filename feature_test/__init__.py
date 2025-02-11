# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys

"""
This module contains functions for detecting the language of a given text.
"""

from fast_langdetect import detect, detect_multilingual, detect_language

# Test the detect_multilingual function with a multilingual input
# Expected output: [{'lang': 'en', 'score': ...}, {'lang': 'zh', 'score': ...}, {'lang': 'ru', 'score': ...}]
print(detect_multilingual("Hello, world!你好世界!Привет, мир!"))
print(detect_multilingual("Hello, world!你好世界!Привет, мир!"))  # Second call without low_memory parameter

# Test the detect function with English and Chinese inputs
print(detect("hello world"))
print(detect("你好世界"))

# Test the detect_language function with various language inputs
# Testing Chinese language using detect_language with the same input as detect
print(detect_language("你好世界"))
print(detect_language("Привет, мир!"))
print(detect_language("こんにちは世界"))
print(detect_language("안녕하세요 세계"))
print(detect_language("Bonjour le monde"))
print(detect_language("Hallo Welt"))
print(detect_language("Hola mundo"))
print(detect_language("Ці організації організовують курси, які в основному орієнтовані на базове використання комп'ютера, такі як обробка тексту, введення китайських символів та застосування Інтернету."))