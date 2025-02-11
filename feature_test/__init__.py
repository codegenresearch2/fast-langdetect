# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys

"""
This script tests the language detection functionalities provided by the fast_langdetect library.
"""

from fast_langdetect import detect, detect_multilingual, detect_language

# Test cases for detect_multilingual function
print("Testing detect_multilingual with mixed languages:")
print(detect_multilingual("Hello, world! 你好世界! Привет, мир!", low_memory=False))
print(detect_multilingual("こんにちは世界", low_memory=False))
print(detect_multilingual("안녕하세요 세계", low_memory=False))
print(detect_multilingual("Bonjour le monde", low_memory=False))
print(detect_multilingual("Hallo Welt", low_memory=False))
print(detect_multilingual("Hola mundo", low_memory=False))
print(detect_multilingual("這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等", low_memory=False))

# Test cases for detect function
print("\nTesting detect function with various languages:")
print(detect("hello world"))
print(detect("你好世界"))
print(detect("こんにちは世界"))
print(detect("안녕하세요 세계"))
print(detect("Bonjour le monde"))
print(detect("Hallo Welt"))
print(detect("Hola mundo"))
print(detect("這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等"))

# Test cases for detect_language function
print("\nTesting detect_language function with different languages:")
print(detect_language("hello world"))  # Expected output: "EN"
print(detect_language("你好世界"))  # Expected output: "ZH"
print(detect_language("こんにちは世界"))  # Expected output: "JA"
print(detect_language("안녕하세요 세계"))  # Expected output: "KO"
print(detect_language("Bonjour le monde"))  # Expected output: "FR"
print(detect_language("Hallo Welt"))  # Expected output: "DE"
print(detect_language("Hola mundo"))  # Expected output: "ES"
print(detect_language("這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等"))  # Expected output: "ZH"