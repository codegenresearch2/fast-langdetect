# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys
# @File    : __init__.py.py
# @Software: PyCharm

import warnings
from fast_langdetect import detect, detect_multilingual, detect_langs
from fast_langdetect import parse_sentence

def consolidate_language_detection(text):
    result = detect_multilingual(text, low_memory=True)
    return result[0].get("lang") if result else None

def deprecated_function_warning(old_func, new_func):
    warnings.warn(f"The function {old_func} is deprecated. Please use {new_func} instead.", DeprecationWarning)

# Deprecate old functions
deprecated_function_warning("detect", "consolidate_language_detection")
deprecated_function_warning("detect_langs", "consolidate_language_detection")

print(parse_sentence("你好世界"))
print(parse_sentence("你好世界！Hello, world！Привет, мир！"))
print(consolidate_language_detection("Hello, world!你好世界!Привет, мир!"))

print(detect("hello world"))
print(detect_langs("Привет, мир!"))