# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys
# @File    : __init__.py.py
# @Software: PyCharm
from fast_langdetect import detect, detect_language, detect_multilingual

# Testing language detection for single sentences
print(detect("hello world"))  # Expected output: {'lang': 'en', 'score': 0.9999999999999999}
print(detect("Привет, мир!"))  # Expected output: {'lang': 'ru', 'score': 0.9999999999999999}

# Testing language detection for multiple sentences
results = detect_multilingual("Hello, world!你好世界!Привет, мир!")
# Expected output format: [{'lang': 'en', 'score': 0.9999999999999999}, {'lang': 'zh-Hans', 'score': 0.9999999999999999}, {'lang': 'ru', 'score': 0.9999999999999999}]
print(results)

# Testing language detection for single sentences using detect_language
print(detect_language("Bonjour le monde"))  # Expected output: 'FR'
print(detect_language("Hola, mundo"))  # Expected output: 'ES'
print(detect_language("Hallo Welt"))  # Expected output: 'DE'
print(detect_language("안녕하세요 세계"))  # Expected output: 'KO'
print(detect_language("こんにちは世界"))  # Expected output: 'JA'
print(detect_language("Привіт, світ!"))  # Expected output: 'UK'
print(detect_language("Здраво, свет!"))  # Expected output: 'SR'
print(detect_language("这些机构主办的课程，多以基本电脑使用为主，例如文书处理、中文输入、互联网应用等"))  # Expected output: 'ZH-Hans'