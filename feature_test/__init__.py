# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys
# @File    : __init__.py.py
# @Software: PyCharm
from fast_langdetect import detect, detect_multilingual, detect_language

# Detecting single language for a sentence
print(detect_language("你好世界"))
print(detect_language("こんにちは世界"))
print(detect_language("안녕하세요 세계"))
print(detect_language("Привет, мир!"))
print(detect_language("Hola, mundo!"))
print(detect_language("Bonjour le monde"))
print(detect_language("Ciao mondo"))
print(detect_language("Hallo Welt"))
print(detect_language("Здравствуйте, мир"))
print(detect_language("Привіт, світ!"))
print(detect_language("你好，世界"))

# Detecting multiple languages in a sentence
print(detect_multilingual("你好世界！Hello, world！Привет, мир！"))
print(detect_multilingual("Hello, world!你好，世界!Привіт, світ!"))

# Detecting single language for various sentences
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
print(detect_multilingual("Hello, world!你好，世界!Привіт, світ!"))