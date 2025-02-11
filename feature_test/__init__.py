# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys

from fast_langdetect import detect, detect_multilingual, detect_language

# Test detect_multilingual function with a multilingual input and low_memory=False
# Expected output: [{'lang': 'en', 'score': ...}, {'lang': 'zh', 'score': ...}, {'lang': 'ru', 'score': ...}, ...]
print(detect_multilingual("Hello, world!你好世界!Привет, мир!こんにちは世界!안녕하세요 세계!Bonjour le monde!Hallo Welt!Hola mundo!Este es un ejemplo en español.Este é um exemplo em português.", low_memory=False))

# Test detect_multilingual function with a multilingual input without low_memory parameter
# Expected output: [{'lang': 'en', 'score': ...}, {'lang': 'zh', 'score': ...}, {'lang': 'ru', 'score': ...}, ...]
print(detect_multilingual("Hello, world!你好世界!Привет, мир!こんにちは世界!안녕하세요 세계!Bonjour le monde!Hallo Welt!Hola mundo!Este es un ejemplo en español.Este é um exemplo em português."))

# Testing various languages: English, Chinese, Russian, Japanese, Korean, French, German, Spanish, Portuguese
print(detect("hello world"))  # Expected output: {'lang': 'en', 'score': ...}
print(detect("你好世界"))  # Expected output: {'lang': 'zh', 'score': ...}
print(detect("Привет, мир!"))  # Expected output: {'lang': 'ru', 'score': ...}
print(detect("こんにちは世界"))  # Expected output: {'lang': 'ja', 'score': ...}
print(detect("안녕하세요 세계"))  # Expected output: {'lang': 'ko', 'score': ...}
print(detect("Bonjour le monde"))  # Expected output: {'lang': 'fr', 'score': ...}
print(detect("Hallo Welt"))  # Expected output: {'lang': 'de', 'score': ...}
print(detect("Hola mundo"))  # Expected output: {'lang': 'es', 'score': ...}
print(detect("Este é um exemplo em português."))  # Expected output: {'lang': 'pt', 'score': ...}

# Testing detect_language function for various languages
print(detect_language("hello world"))  # Expected output: 'en'
print(detect_language("你好世界"))  # Expected output: 'zh'
print(detect_language("Привет, мир!"))  # Expected output: 'ru'
print(detect_language("こんにちは世界"))  # Expected output: 'ja'
print(detect_language("안녕하세요 세계"))  # Expected output: 'ko'
print(detect_language("Bonjour le monde"))  # Expected output: 'fr'
print(detect_language("Hallo Welt"))  # Expected output: 'de'
print(detect_language("Hola mundo"))  # Expected output: 'es'
print(detect_language("Este é um exemplo em português."))  # Expected output: 'pt'