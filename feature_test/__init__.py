# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys
# @File    : __init__.py.py
# @Software: PyCharm
from fast_langdetect import detect, detect_multilingual, detect_language

# Detecting single language for a sentence
print("\nSingle Language Detection:")
# Chinese
print(detect_language("你好世界"))
# Japanese
print(detect_language("こんにちは世界"))
# Korean
print(detect_language("안녕하세요 세계"))
# Russian
print(detect_language("Привет, мир!"))
# Spanish
print(detect_language("Hola, mundo!"))
# French
print(detect_language("Bonjour le monde"))
# Italian
print(detect_language("Ciao mondo"))
# German
print(detect_language("Hallo Welt"))
# Ukrainian
print(detect_language("Здравствуйте, мир"))
# Ukrainian
print(detect_language("Привіт, світ!"))
# Traditional Chinese
print(detect_language("這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等"))

# Detecting multiple languages in a sentence
print("\nMultilingual Detection:")
print(detect_multilingual("你好世界！Hello, world！Привет, мир！"))

# Detecting single language for various sentences
print("\nSingle Language Detection (Various Sentences):")
print(detect("hello world"))
print(detect("Привет, мир!"))
print(detect("Hola, mundo!"))
print(detect("Bonjour le monde"))
print(detect("Ciao mondo"))
print(detect("こんにちは世界"))
print(detect("안녕하세요 세계"))
print(detect("Hallo Welt"))
print(detect("Здравствуйте, мир"))
print(detect("Привіт, світ!"))
print(detect("你好，世界"))

# Detecting multiple languages in a sentence with various languages
print("\nMultilingual Detection (Various Sentences):")
print(detect_multilingual("Hello, world!你好，世界!Привіт, світ!"))