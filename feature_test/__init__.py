# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys

from fast_langdetect import detect, detect_multilingual, detect_language

# Test detect_multilingual function with a multilingual input and low_memory=False
# Expected output: [{'lang': 'en', 'score': ...}, {'lang': 'zh', 'score': ...}, {'lang': 'ru', 'score': ...}, ...]
print(detect_multilingual("Hello, world!你好世界!Привет, мир!こんにちは世界!안녕하세요 세계!Bonjour le monde!Hallo Welt!Hola mundo!", low_memory=False))

# Test detect_multilingual function with a multilingual input without low_memory parameter
# Expected output: [{'lang': 'en', 'score': ...}, {'lang': 'zh', 'score': ...}, {'lang': 'ru', 'score': ...}, ...]
print(detect_multilingual("Hello, world!你好世界!Привет, мир!こんにちは世界!안녕하세요 세계!Bonjour le monde!Hallo Welt!Hola mundo!"))

# Testing various languages: English, Chinese, Russian, Japanese, Korean, French, German, Spanish
print(detect("hello world"))  # Expected output: {'lang': 'en', 'score': ...}
print(detect("你好世界"))  # Expected output: {'lang': 'zh', 'score': ...}
print(detect_language("Привет, мир!"))  # Expected output: 'RU'
print(detect_language("こんにちは世界"))  # Expected output: 'JA'
print(detect_language("안녕하세요 세계"))  # Expected output: 'KO'
print(detect_language("Bonjour le monde"))  # Expected output: 'FR'
print(detect_language("Hallo Welt"))  # Expected output: 'DE'
print(detect_language("Hola mundo"))  # Expected output: 'ES'