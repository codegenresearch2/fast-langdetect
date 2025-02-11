# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys

from fast_langdetect import detect, detect_multilingual, detect_language

# Test detect_multilingual function with a multilingual input and low_memory=False
# Expected output: [{'lang': 'en', 'score': ...}, {'lang': 'zh', 'score': ...}, {'lang': 'ru', 'score': ...}]
print(detect_multilingual("Hello, world!你好世界!Привет, мир!", low_memory=False))

# Test detect_multilingual function with a multilingual input without low_memory parameter
# Expected output: [{'lang': 'en', 'score': ...}, {'lang': 'zh', 'score': ...}, {'lang': 'ru', 'score': ...}]
print(detect_multilingual("Hello, world!你好世界!Привет, мир!"))

# Testing various languages: English, Chinese, Russian
print(detect("hello world"))  # Expected output: {'lang': 'en', 'score': ...}
print(detect("你好世界"))  # Expected output: {'lang': 'zh', 'score': ...}
print(detect_language("Привет, мир!"))  # Expected output: 'RU'