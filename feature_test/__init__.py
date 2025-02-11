# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys
# @File    : language_detection.py
# @Software: PyCharm

from fast_langdetect import detect, detect_language, detect_multilingual

# Detect language of a single sentence
print(detect("你好世界"))  # Expected output: {'lang': 'zh', 'score': 0.9999999999999999}

# Detect language of a multilingual sentence
print(detect_language("你好世界！Hello, world！Привет, мир！"))  # Expected output: {'lang': 'zh', 'score': 0.9999999999999999}

# Detect languages in a multilingual sentence
print(detect_multilingual("Hello, world!你好世界!Привет, мир!"))
# Expected output: [{'lang': 'en', 'score': 0.9999999999999999}, {'lang': 'zh', 'score': 0.9999999999999999}, {'lang': 'ru', 'score': 0.9999999999999999}]

# Detect language of English sentence
print(detect("hello world"))  # Expected output: {'lang': 'en', 'score': 0.9999999999999999}

# Detect language of Russian sentence
print(detect("Привет, мир!"))  # Expected output: {'lang': 'ru', 'score': 0.9999999999999999}

# Detect language of Japanese sentence
print(detect("こんにちは世界"))  # Expected output: {'lang': 'ja', 'score': 0.9999999999999999}

# Detect language of Korean sentence
print(detect("안녕하세요 세계"))  # Expected output: {'lang': 'ko', 'score': 0.9999999999999999}

# Detect language of French sentence
print(detect("Bonjour le monde"))  # Expected output: {'lang': 'fr', 'score': 0.9999999999999999}

# Detect language of German sentence
print(detect("Hallo Welt"))  # Expected output: {'lang': 'de', 'score': 0.9999999999999999}

# Detect language of Spanish sentence
print(detect("Hola mundo"))  # Expected output: {'lang': 'es', 'score': 0.9999999999999999}

# Detect language of a complex Chinese sentence
print(detect("这些机构主办的课程，多以基本电脑使用为主，例如文书处理、中文输入、互联网应用等"))  # Expected output: {'lang': 'zh', 'score': 0.9999999999999999}