# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys
# @File    : __init__.py
# @Software: PyCharm

from fast_langdetect import detect_language

# Import statements to include all relevant functions

# Print statements to display the results of the detection functions
print(detect_language("hello world"))  # Expected output: {'lang': 'en'}
print(detect_language("你好世界"))  # Expected output: {'lang': 'zh'}
print(detect_language("こんにちは世界"))  # Expected output: {'lang': 'ja'}
print(detect_language("안녕하세요 세계"))  # Expected output: {'lang': 'ko'}
print(detect_language("Bonjour le monde"))  # Expected output: {'lang': 'fr'}
print(detect_language("Hallo Welt"))  # Expected output: {'lang': 'de'}
print(detect_language("Hola mundo"))  # Adding Spanish for variety
print(detect_language("Привет, мир"))  # Adding Russian for variety

# Multilingual detection example
print(detect_language("Hello, world! 你好世界! こんにちは世界! 안녕하세요 세계! Bonjour le monde! Hallo Welt! Hola mundo! Привет, мир!"))
# Expected output: {'lang': 'en'}

# Commenting to explain what each part of the code does
# The following print statements demonstrate language detection for various texts
# Expected output format: {'lang': 'language_code'}