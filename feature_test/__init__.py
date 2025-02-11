# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys

"""
This module contains the rewritten code snippet that addresses the feedback received.
"""

from fast_langdetect import detect, detect_multilingual, detect_language

# Testing detect_multilingual function with multiple languages and low_memory set to False
print(detect_multilingual("Hello, world!你好世界!Привет, мир!", low_memory=False))

# Testing detect_multilingual function without low_memory parameter
print(detect_multilingual("Hello, world!你好世界!Привет, мир!"))

# Testing detect function with various languages
print(detect("hello world"))  # English
print(detect("你好世界"))  # Chinese
print(detect("こんにちは世界"))  # Japanese
print(detect("안녕하세요 세계"))  # Korean
print(detect("Bonjour le monde"))  # French
print(detect("Hallo Welt"))  # German
print(detect("Hola mundo"))  # Spanish
print(detect("Ciao mondo"))  # Italian
print(detect("Olá mundo"))  # Portuguese

# Testing detect_language function with various languages
print(detect_language("Привет, мир!"))  # Russian
print(detect_language("你好世界"))  # Chinese
print(detect_language("こんにちは世界"))  # Japanese
print(detect_language("안녕하세요 세계"))  # Korean
print(detect_language("Bonjour le monde"))  # French
print(detect_language("Hallo Welt"))  # German
print(detect_language("Hola mundo"))  # Spanish
print(detect_language("Ciao mondo"))  # Italian
print(detect_language("Olá mundo"))  # Portuguese
print(detect_language("こんにちは、世界"))  # Japanese
print(detect_language("Hola, mundo"))  # Spanish
print(detect_language("Bonjour, le monde"))  # French
print(detect_language("Hallo, Welt"))  # German
print(detect_language("Ciao, mondo"))  # Italian
print(detect_language("Olá, mundo"))  # Portuguese