# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys
# @File    : __init__.py.py
# @Software: PyCharm

import warnings
from fast_langdetect import detect_language, detect_multilingual

# Detect the language of a single sentence
print(detect_language("你好世界"))

# Detect the language of a multilingual sentence
print(detect_language("你好世界！Hello, world！Привет, мир！"))

# Detect languages in a multilingual sentence
print(detect_multilingual("Hello, world!你好世界!Привет, мир!"))

# Deprecate the use of 'detect' function
warnings.warn("The 'detect' function is deprecated. Use 'detect_language' instead.", DeprecationWarning)

# Test with English
print(detect_language("hello world"))

# Test with Russian
print(detect_multilingual("Привет, мир!"))