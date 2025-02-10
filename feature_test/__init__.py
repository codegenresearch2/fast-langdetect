# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys
# @File    : __init__.py
# @Software: PyCharm
from fast_langdetect import detect_language, detect_multilingual

# Testing language detection with multiple languages
print(detect_language("Hello, world!"))  # Expected output: "EN"
print(detect_language("こんにちは世界"))  # Expected output: "JA"
print(detect_language("안녕하세요 세계"))  # Expected output: "KO"
print(detect_language("Bonjour le monde"))  # Expected output: "FR"
print(detect_language("Hallo Welt"))  # Expected output: "DE"
print(detect_language("你好世界"))  # Expected output: "ZH"

# Testing detect_multilingual with multiple languages in a single string
print(detect_multilingual("Hello, world! こんにちは世界 안녕하세요 세계 Bonjour le monde Hallo Welt 你好世界"))