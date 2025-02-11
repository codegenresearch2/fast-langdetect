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
# Expected output: [{'lang': 'en', 'score': 0.99}, {'lang': 'zh-cn', 'score': 0.01}, {'lang': 'ru', 'score': 0.01}]

print("\nTesting detect with English text:")
print(detect("hello world"))
# Expected output: {'lang': 'en'}

print("\nTesting detect_language with Russian text:")
print(detect_language("Привет, мир!", low_memory=False))
# Expected output: 'ru'

print("\nTesting detect_language with Chinese text:")
print(detect_language("你好世界", low_memory=False))
# Expected output: 'zh'

print("\nTesting detect_language with Japanese text:")
print(detect_language("こんにちは世界", low_memory=False))
# Expected output: 'ja'

print("\nTesting detect_language with Korean text:")
print(detect_language("안녕하세요 세계", low_memory=False))
# Expected output: 'ko'

print("\nTesting detect_language with French text:")
print(detect_language("Bonjour le monde", low_memory=False))
# Expected output: 'fr'

print("\nTesting detect_language with German text:")
print(detect_language("Hallo Welt", low_memory=False))
# Expected output: 'de'

print("\nTesting detect_language with Spanish text:")
print(detect_language("Hola mundo", low_memory=False))
# Expected output: 'es'

print("\nTesting detect_language with mixed Chinese and English text:")
print(detect_language("這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等", low_memory=False))
# Expected output: 'zh'