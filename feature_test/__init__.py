# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys
# @File    : __init__.py
# @Software: PyCharm

import logging
from fast_langdetect import detect_language

# Configure logging
logging.basicConfig(level=logging.WARNING)

# Print statements with expected output
print("Expected output for 'hello world':", detect_language("hello world"))
print("Expected output for '你好世界':", detect_language("你好世界"))
print("Expected output for 'こんにちは世界':", detect_language("こんにちは世界"))
print("Expected output for '안녕하세요 세계':", detect_language("안녕하세요 세계"))
print("Expected output for 'Bonjour le monde':", detect_language("Bonjour le monde"))
print("Expected output for 'Hallo Welt':", detect_language("Hallo Welt"))
print("Expected output for '這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等':", detect_language("這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等"))

# Comment describing the languages being tested
# The following print statements demonstrate language detection for various texts.
# Expected output format: {'lang': 'language_code'}