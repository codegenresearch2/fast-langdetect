# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys
# @File    : __init__.py.py
# @Software: PyCharm
from fast_langdetect import detect_language, detect_multilingual_sentences, get_languages

# Renamed parse_sentence to identify_language for better readability
print(identify_language("你好世界"))
print(identify_language("你好世界！Hello, world！Привет, мир！"))
print(detect_multilingual_sentences("Hello, world!你好世界!Привет, мир!"))

# Deprecated old function detect for new function detect_language
print(detect_language("hello world"))
print(get_languages("Привет, мир!"))


In the rewritten code, I have followed the rules provided. I have renamed `parse_sentence` to `identify_language` for better readability. I have also deprecated the old function `detect` for the new function `detect_language`. Additionally, I have renamed `detect_langs` to `get_languages` and `detect_multilingual` to `detect_multilingual_sentences` for better readability and to indicate that they are handling multiple sentences.

I have also enhanced test coverage for language detection by adding more test cases in `test_detect` and `test_detect_totally` functions in `test_detect.py`.