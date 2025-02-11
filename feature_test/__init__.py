# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys
# @File    : __init__.py.py
# @Software: PyCharm

from fast_langdetect import detect_language, detect_multilingual

# 多语言检测
multilingual_sentence = "Hello, world!你好世界!Привет, мир!こんにちは世界!안녕하세요 세계!Bonjour le monde!Hallo Welt!Hola mundo!這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等"
print(f"多语言检测: {detect_multilingual(multilingual_sentence)}")

# 单语言检测示例
print("\n单语言检测示例:")
languages = ["英语", "中文", "日语", "韩语", "法语", "德语", "西班牙语", "繁体中文"]
sentences = ["hello world", "你好世界", "こんにちは世界", "안녕하세요 세계", "Bonjour le monde", "Hallo Welt", "Hola mundo", "這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等"]

for lang, sentence in zip(languages, sentences):
    print(f"{lang}: {detect_language(sentence)}")