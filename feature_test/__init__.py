# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys
# @File    : __init__.py.py
# @Software: PyCharm

from fast_langdetect import detect, detect_multilingual, detect_langs
from fast_langdetect import parse_sentence

# Directly use the functions without additional wrapper functions
print(parse_sentence("你好世界"))
print(parse_sentence("你好世界！Hello, world！Привет, мир！"))
print(detect_multilingual("Hello, world!你好世界!Привет, мир!"))

print(detect("hello world"))
print(detect_langs("Привет, мир!"))
print(detect("こんにちは世界"))
print(detect("안녕하세요 세계"))
print(detect("Bonjour le monde"))