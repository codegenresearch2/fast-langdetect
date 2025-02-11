# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys

from fast_langdetect import detect, detect_multilingual, detect_language

# 测试多语言检测函数，包括英语、中文、俄语、日语、韩语、法语、德语和西班牙语
print("Detect Multilingual:")
# 测试低内存模式
print(detect_multilingual("Hello, world!你好世界!Привет, мир!こんにちは世界!안녕하세요 세계!Bonjour le monde!Hallo Welt!Hola mundo!", low_memory=True))
# 测试高精度模式
print(detect_multilingual("Hello, world!你好世界!Привет, мир!こんにちは世界!안녕하세요 세계!Bonjour le monde!Hallo Welt!Hola mundo!", low_memory=False))

# 测试单语言检测函数，包括英语、俄语、中文、日语、韩语、法语、德语和西班牙语
print("\nDetect Language:")
print(detect("hello world"))
print(detect("Привет, мир!"))
print(detect("你好世界"))
print(detect("こんにちは世界"))
print(detect("안녕하세요 세계"))
print(detect("Bonjour le monde"))
print(detect("Hallo Welt"))
print(detect("Hola mundo"))

# 测试单语言检测函数，返回完整的语言信息，包括英语、俄语、中文、日语、韩语、法语、德语和西班牙语
print("\nDetect Language (Full Output):")
print(detect_language("hello world"))
print(detect_language("Привет, мир!"))
print(detect_language("你好世界"))
print(detect_language("こんにちは世界"))
print(detect_language("안녕하세요 세계"))
print(detect_language("Bonjour le monde"))
print(detect_language("Hallo Welt"))
print(detect_language("Hola mundo"))