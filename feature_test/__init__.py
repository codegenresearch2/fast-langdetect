# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys
# @File    : __init__.py.py
# @Software: PyCharm

from fast_langdetect import detect, detect_language, detect_multilingual

# 多语言检测
multilingual_sentence = "Hello, world!你好世界!Привет, мир!こんにちは世界!안녕하세요 세계!Bonjour le monde!Hallo Welt!Hola mundo!這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等"
print(f"多语言检测: {detect_multilingual(multilingual_sentence)}")

# 单语言检测
print("\n单语言检测示例:")
print("英语: ", detect_language("hello world"))
print("中文: ", detect_language("你好世界"))
print("日语: ", detect_language("こんにちは世界"))
print("韩语: ", detect_language("안녕하세요 세계"))
print("法语: ", detect_language("Bonjour le monde"))
print("德语: ", detect_language("Hallo Welt"))
print("西班牙语: ", detect_language("Hola mundo"))
print("繁体中文: ", detect_language("這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等"))

# 使用 detect 函数进行单语言检测
print("\n使用 detect 函数进行单语言检测:")
print("英语: ", detect("hello world"))