# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys

from fast_langdetect import detect, detect_multilingual, detect_language

# Test detect_multilingual function with a multilingual input and low_memory=False
print(detect_multilingual("Hello, world!你好世界!Привет, мир!こんにちは世界!안녕하세요 세계!Bonjour le monde!Hallo Welt!Hola mundo!這些機構主辦的課程，多以基本電腦使用為主。", low_memory=False))

# Test detect_multilingual function with a multilingual input without low_memory parameter
print(detect_multilingual("Hello, world!你好世界!Привет, мир!こんにちは世界!안녕하세요 세계!Bonjour le monde!Hallo Welt!Hola mundo!這些機構主辦的課程，多以基本電腦使用為主。"))

# Testing various languages: English, Chinese, Russian, Japanese, Korean, French, German, Spanish, Ukrainian, Traditional Chinese
print(detect("hello world"))
print(detect("你好世界"))
print(detect("Привет, мир!"))
print(detect("こんにちは世界"))
print(detect("안녕하세요 세계"))
print(detect("Bonjour le monde"))
print(detect("Hallo Welt"))
print(detect("Hola mundo"))
print(detect("Це ці організації організовують курси, які в основному орієнтовані на базове використання комп'ютера, наприклад, обробка текстів, введення китайських символів, застосування Інтернету тощо."))
print(detect("這些機構主辦的課程，多以基本電腦使用為主。"))

# Testing detect_language function for various languages
print(detect_language("hello world"))
print(detect_language("你好世界"))
print(detect_language("Привет, мир!"))
print(detect_language("こんにちは世界"))
print(detect_language("안녕하세요 세계"))
print(detect_language("Bonjour le monde"))
print(detect_language("Hallo Welt"))
print(detect_language("Hola mundo"))
print(detect_language("Це ці організації організовують курси, які в основному орієнтовані на базове використання комп'ютера, наприклад, обробка текстів, введення китайських символів, застосування Інтернету тощо."))
print(detect_language("這些機構主辦的課程，多以基本電腦使用為主。"))