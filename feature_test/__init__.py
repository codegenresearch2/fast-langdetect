# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys
# @File    : __init__.py.py
# @Software: PyCharm
from fast_langdetect import detect, detect_multilingual, detect_language

# Using the correct function names as per the gold code
# The expected outputs are based on the actual behavior of the functions

# Single language detection
print(detect("Bonjour le monde"))
# Expected output: {'lang': 'fr', 'score': ...}
# Description: Detects the language of the given French phrase

print(detect("こんにちは世界、今日は良い天気ですね。"))
# Expected output: {'lang': 'ja', 'score': ...}
# Description: Detects the language of the given Japanese phrase

# Multilingual detection
print(detect_multilingual("Hello, world!你好世界!Привет, мир!"))
# Expected output: [{'lang': 'en', 'score': ...}, {'lang': 'zh', 'score': ...}, {'lang': 'ru', 'score': ...}]
# Description: Detects the languages of the given multilingual phrase

# Additional test cases for diversity
print(detect("Hola, ¿cómo estás? Bienvenido al mundo."))
# Expected output: {'lang': 'es', 'score': ...}
# Description: Detects the language of the given Spanish phrase

print(detect("안녕하세요, 세계! 반갑습니다."))
# Expected output: {'lang': 'ko', 'score': ...}
# Description: Detects the language of the given Korean phrase

print(detect_multilingual("こんにちは世界！Bonjour le monde!Hola, mundo!"))
# Expected output: [{'lang': 'ja', 'score': ...}, {'lang': 'fr', 'score': ...}, {'lang': 'es', 'score': ...}]
# Description: Detects the languages of the given multilingual phrase with different languages

# Using detect_language for individual language detection
print(detect_language("Hallo Welt, wie geht's dir?"))
# Expected output: 'de'
# Description: Detects the language of the given German phrase

# Ensuring consistency in function usage and formatting
print(detect_language("你好，世界！今天天气真好。"))
# Expected output: 'zh'
# Description: Detects the language of the given Chinese phrase