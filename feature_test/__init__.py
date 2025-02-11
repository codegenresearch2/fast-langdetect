# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys
# @File    : language_detection.py
# @Software: PyCharm

from fast_langdetect import detect_language, detect_multilingual

# Detect language of a single sentence
print(detect_language("你好世界"))  # Expected output: {'lang': 'zh', 'score': 0.9999999999999999}

# Detect language of a multilingual sentence
print(detect_language("你好世界！Hello, world！Привет, мир！"))  # Expected output: {'lang': 'zh', 'score': 0.9999999999999999}

# Detect languages in a multilingual sentence
print(detect_multilingual("Hello, world!你好世界!Привет, мир!"))
# Expected output: [{'lang': 'en', 'score': 0.9999999999999999}, {'lang': 'zh', 'score': 0.9999999999999999}, {'lang': 'ru', 'score': 0.9999999999999999}]

# Detect language of English sentence
print(detect_language("hello world"))  # Expected output: {'lang': 'en', 'score': 0.9999999999999999}

# Detect language of Russian sentence
print(detect_language("Привет, мир!"))  # Expected output: {'lang': 'ru', 'score': 0.9999999999999999}

# Detect language of Japanese sentence
print(detect_language("こんにちは世界"))  # Expected output: {'lang': 'ja', 'score': 0.9999999999999999}

# Detect language of Korean sentence
print(detect_language("안녕하세요 세계"))  # Expected output: {'lang': 'ko', 'score': 0.9999999999999999}

# Detect language of French sentence
print(detect_language("Bonjour le monde"))  # Expected output: {'lang': 'fr', 'score': 0.9999999999999999}

# Detect language of German sentence
print(detect_language("Hallo Welt"))  # Expected output: {'lang': 'de', 'score': 0.9999999999999999}