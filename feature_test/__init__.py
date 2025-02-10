# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys

from fast_langdetect import detect, detect_multilingual, detect_language

# Test detection of multiple languages with low memory
result_multilingual = detect_multilingual("Hello, world!你好世界!Привет, мир!", low_memory=False)
print(result_multilingual)
# [{'lang': 'en', 'score': 0.9999999999999999}, {'lang': 'zh', 'score': 0.9999999999999999}, {'lang': 'ru', 'score': 0.9999999999999999}, {'lang': 'uk', 'score': 0.9999999999999999}, {'lang': 'ja', 'score': 0.9999999999999999}]

# Test detection of English
result_english = detect("hello world")
print(result_english)

# Test detection of languages
print(detect_language("Привет, мир!"))  # Output: 'ru'
print(detect_language("你好世界"))  # Output: 'zh'
print(detect_language("こんにちは世界"))  # Output: 'ja'
print(detect_language("안녕하세요 세계"))  # Output: 'ko'
print(detect_language("Bonjour le monde"))  # Output: 'fr'
print(detect_language("Hallo Welt"))  # Output: 'de'
print(detect_language("Hola mundo"))  # Output: 'es'
print(detect_language("這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等"))  # Output: 'zh'