# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys
# @File    : __init__.py.py
# @Software: PyCharm

from fast_langdetect import detect, detect_language, detect_multilingual

# Demonstrate multilingual detection
multilingual_sentence = "Hello, world!你好世界!Привет, мир!這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等"
multilingual_result = detect_multilingual(multilingual_sentence)
print("Multilingual detection: ")
for result in multilingual_result:
    print(f"Language: {result['lang']}, Probability: {result['prob']}")

# Demonstrate language detection for various languages
print("\nLanguage detection examples:")
print("English: ", detect("hello world"))
print("Chinese: ", detect("你好世界"))
print("Japanese: ", detect("こんにちは世界"))
print("Korean: ", detect("안녕하세요 세계"))
print("French: ", detect("Bonjour le monde"))
print("German: ", detect("Hallo Welt"))
print("Spanish: ", detect("Hola mundo"))
print("Traditional Chinese: ", detect("這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等"))