# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys
# @File    : __init__.py.py
# @Software: PyCharm

from fast_langdetect import detect_language, detect_multilingual

# Demonstrate multilingual detection
multilingual_sentence = "Hello, world!你好世界!Привет, мир!這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等"
print(f"Multilingual detection: {detect_multilingual(multilingual_sentence)}")

# Demonstrate language detection for various languages
# Languages: English, Chinese, Japanese, Korean, French, German, Spanish, Traditional Chinese
print("\nLanguage detection examples:")
print("English: ", detect_language("hello world"))
print("Chinese: ", detect_language("你好世界"))
print("Japanese: ", detect_language("こんにちは世界"))
print("Korean: ", detect_language("안녕하세요 세계"))
print("French: ", detect_language("Bonjour le monde"))
print("German: ", detect_language("Hallo Welt"))
print("Spanish: ", detect_language("Hola mundo"))
print("Traditional Chinese: ", detect_language("這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等"))