# -*- coding: utf-8 -*-

from fast_langdetect import detect, detect_language, detect_multilingual
import warnings

# Detect language of a single sentence
print(detect("你好世界"))  # Expected output: {'lang': 'zh', 'prob': 0.9999999999999999}

# Detect language of a multilingual sentence
print(detect_language("你好世界！Hello, world！Привет, мир！"))  # Expected output: 'ZH'

# Detect languages in a multilingual sentence
print(detect_multilingual("Hello, world!你好世界!Привет, мир!"))
# Expected output: [{'lang': 'en', 'prob': 0.9999999999999999}, {'lang': 'zh', 'prob': 0.9999999999999999}, {'lang': 'ru', 'prob': 0.9999999999999999}]

# Detect language of English sentence
print(detect("hello world"))  # Expected output: {'lang': 'en', 'prob': 0.9999999999999999}

# Detect language of Russian sentence
print(detect("Привет, мир!"))  # Expected output: {'lang': 'ru', 'prob': 0.9999999999999999}

# Deprecation warning for using 'detect_langs'
warnings.warn("The 'detect_langs' function is deprecated. Use 'detect_multilingual' instead.", DeprecationWarning)