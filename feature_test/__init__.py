# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys
# @File    : __init__.py.py
# @Software: PyCharm
import logging
from fast_langdetect import detect_single_language, detect_multi_language, detect_all_languages
from fast_langdetect import analyze_sentence

# Adding logging for deprecated function
logging.warning("The function 'parse_sentence' is deprecated. Please use 'analyze_sentence' instead.")

print(analyze_sentence("你好世界"))
print(analyze_sentence("你好世界！Hello, world！Привет, мир！"))
print(detect_multi_language("Hello, world!你好世界!Привет, мир!"))

print(detect_single_language("hello world"))
assert detect_single_language("hello world")["lang"] == "en", "Language detection error"
assert detect_single_language("Привет, мир!")["lang"] == "ru", "Language detection error"
print(detect_all_languages("Привет, мир!"))

# Adding more language test cases for coverage
assert detect_single_language("Hola, mundo!")["lang"] == "es", "Language detection error"
assert detect_single_language("Bonjour le monde")["lang"] == "fr", "Language detection error"
assert detect_single_language("Ciao mondo")["lang"] == "it", "Language detection error"