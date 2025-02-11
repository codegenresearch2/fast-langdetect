# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys
# @File    : __init__.py
# @Software: PyCharm

from fast_langdetect import detect, detect_multilingual, detect_language

# Import statements to include all relevant functions

# Print statements to display the results of the detection functions
print(detect("hello world"))  # Expected output: {'lang': 'en'}
print(detect("你好世界"))  # Expected output: {'lang': 'zh'}
print(detect("こんにちは世界"))  # Expected output: {'lang': 'ja'}
print(detect("안녕하세요 세계"))  # Expected output: {'lang': 'ko'}
print(detect("Bonjour le monde"))  # Expected output: {'lang': 'fr'}
print(detect("Hallo Welt"))  # Expected output: {'lang': 'de'}
print(detect("Hola mundo"))  # Adding Spanish for variety
print(detect("Привет, мир"))  # Adding Russian for variety

# Multilingual detection example
print(detect_multilingual("Hello, world! 你好世界! こんにちは世界! 안녕하세요 세계! Bonjour le monde! Hallo Welt! Hola mundo! Привет, мир!"))
# Expected output: [{'lang': 'en', 'score': 0.9}, {'lang': 'zh', 'score': 0.8}, {'lang': 'ja', 'score': 0.7}, {'lang': 'ko', 'score': 0.6}, {'lang': 'fr', 'score': 0.5}, {'lang': 'de', 'score': 0.4}, {'lang': 'es', 'score': 0.3}, {'lang': 'ru', 'score': 0.2}]

# Commenting to explain what each part of the code does
# The following print statements demonstrate language detection for various texts
# Expected output format: {'lang': 'language_code'}