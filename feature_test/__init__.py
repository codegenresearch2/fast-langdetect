# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys

from fast_langdetect import detect, detect_multilingual, detect_language

# Testing multilingual detection with English, Chinese (Simplified and Traditional), Russian, Japanese, Korean, French, German, and Spanish
print("Detect Multilingual:")
# Testing low memory mode
print(detect_multilingual("Hello, world!你好世界!こんにちは世界!안녕하세요 세계!Bonjour le monde!Hallo Welt!Hola mundo!Привет, мир!", low_memory=True))
# Testing high accuracy mode
print(detect_multilingual("Hello, world!你好世界!こんにちは世界!안녕하세요 세계!Bonjour le monde!Hallo Welt!Hola mundo!Привет, мир!", low_memory=False))

# Testing single language detection with English, Russian, Chinese (Simplified and Traditional), Japanese, Korean, French, German, and Spanish
print("\nDetect Language:")
print(detect("hello world"))
print(detect("Привет, мир!"))
print(detect("你好世界"))
print(detect("こんにちは世界"))
print(detect("안녕하세요 세계"))
print(detect("Bonjour le monde"))
print(detect("Hallo Welt"))
print(detect("Hola mundo"))

# Testing single language detection with Traditional Chinese
print(detect("這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等"))

# Testing single language detection with full output
print("\nDetect Language (Full Output):")
print(detect_language("hello world"))
print(detect_language("Привет, мир!"))
print(detect_language("你好世界"))
print(detect_language("こんにちは世界"))
print(detect_language("안녕하세요 세계"))
print(detect_language("Bonjour le monde"))
print(detect_language("Hallo Welt"))
print(detect_language("Hola mundo"))
print(detect_language("這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等"))