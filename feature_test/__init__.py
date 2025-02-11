# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys

from fast_langdetect import detect, detect_multilingual, detect_language

# 测试多语言检测，包括多种语言和短语
print("多语言检测:")
multilingual_text = "Hello, world!你好世界!こんにちは世界!안녕하세요 세계!Bonjour le monde!Hallo Welt!Hola mundo!Привет, мир!Ciao mondo!Hola, mundo!"
print(detect_multilingual(multilingual_text, low_memory=False))

# 测试单一语言检测，包括多种语言
print("\n单一语言检测:")
print(detect("hello world"))
print(detect("Привет, мир!"))
print(detect("你好世界"))
print(detect("こんにちは世界"))
print(detect("안녕하세요 세계"))
print(detect("Bonjour le monde"))
print(detect("Hallo Welt"))
print(detect("Hola mundo"))
print(detect("Ciao mondo"))

# 测试繁体中文的单一语言检测
print(detect("這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等"))

# 测试单一语言检测，包括完整输出
print("\n单一语言检测（完整输出）:")
print(detect_language("hello world"))
print(detect_language("Привет, мир!"))
print(detect_language("你好世界"))
print(detect_language("こんにちは世界"))
print(detect_language("안녕하세요 세계"))
print(detect_language("Bonjour le monde"))
print(detect_language("Hallo Welt"))
print(detect_language("Hola mundo"))
print(detect_language("Ciao mondo"))
print(detect_language("這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等"))