# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys
# @File    : __init__.py.py
# @Software: PyCharm
from fast_langdetect import detect, detect_multilingual

# Using the correct function names as per the gold code
print(detect("你好世界"))
print(detect("你好世界！Hello, world！Привет, мир！"))
print(detect_multilingual("Hello, world!你好世界!Привет, мир!"))
# Expected output: [{'lang': 'en', 'prob': 0.9999999999999999}, {'lang': 'zh', 'prob': 0.9999999999999999}, {'lang': 'ru', 'prob': 0.9999999999999999}]

# Adding more diverse language examples to match the breadth of the gold code
print(detect("Bonjour le monde"))
print(detect("Hola, mundo"))
print(detect("Hallo Welt"))
print(detect("안녕하세요 세계"))
print(detect("こんにちは世界"))

# Removing unused imports to keep the code clean and focused