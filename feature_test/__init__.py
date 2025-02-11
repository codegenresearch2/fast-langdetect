# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys
# @File    : __init__.py
# @Software: PyCharm

import logging
from fast_langdetect import detect, detect_multilingual, detect_langs

# Configure logging
logging.basicConfig(level=logging.WARNING)

# Print statements with expected output
print("Expected output for 'hello world':", detect("hello world"))
print("Expected output for '你好世界':", detect("你好世界"))
print("Expected output for 'こんにちは世界':", detect("こんにちは世界"))
print("Expected output for '안녕하세요 세계':", detect("안녕하세요 세계"))
print("Expected output for 'Bonjour le monde':", detect("Bonjour le monde"))
print("Expected output for 'Hallo Welt':", detect("Hallo Welt"))
print("Expected output for '這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等':", detect("這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等"))
print("Expected output for 'Hola mundo':", detect("Hola mundo"))  # Adding Spanish for variety

# Multilingual detection example
print("Multilingual detection output:", detect_multilingual("Hello, world! Hola mundo! こんにちは世界! 안녕하세요 세계! Bonjour le monde! Hallo Welt!", low_memory=True))

# Language detection variety
print("Language detection for various texts:", detect_langs("Hello, world! Hola mundo! こんにちは世界! 안녕하세요 세계! Bonjour le monde! Hallo Welt!"))

# Comment describing the languages being tested
# The following print statements demonstrate language detection for various texts, including Spanish.
# Expected output format: {'lang': 'language_code'}