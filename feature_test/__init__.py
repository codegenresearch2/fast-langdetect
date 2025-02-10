# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys

"""
This module provides functions to detect the language of text using the fast_langdetect library.
It includes functions to detect the language of text in multiple languages, handle exceptions,
and maintain consistent code style and structure.
"""

from fast_langdetect import detect, detect_multilingual, detect_language

def test_language_detection():
    """
    测试多种语言的检测，包括英语、中文、日语、韩语、法语、德语、西班牙语等。
    """
    # 测试多语言检测，不使用低内存模式
    result_multilingual_low_memory = detect_multilingual("Hello, world!你好世界!Привет, мир!", low_memory=True)
    print(result_multilingual_low_memory)
    # [{'lang': 'en', 'score': 0.9999999999999999}, {'lang': 'zh', 'score': 0.9999999999999999}, {'lang': 'ru', 'score': 0.9999999999999999}, {'lang': 'uk', 'score': 0.9999999999999999}, {'lang': 'ja', 'score': 0.9999999999999999}]

    # 测试多语言检测，使用低内存模式
    result_multilingual_no_low_memory = detect_multilingual("Hello, world!你好世界!Привет, мир!", low_memory=False)
    print(result_multilingual_no_low_memory)
    # [{'lang': 'en', 'score': 0.9999999999999999}, {'lang': 'zh', 'score': 0.9999999999999999}, {'lang': 'ru', 'score': 0.9999999999999999}, {'lang': 'uk', 'score': 0.9999999999999999}, {'lang': 'ja', 'score': 0.9999999999999999}]

    # 测试英语检测
    result_english = detect("hello world")
    print(result_english)

    # 测试语言检测
    print(detect_language("Привет, мир!"))  # Output: 'ru'
    print(detect_language("你好世界"))  # Output: 'zh'
    print(detect_language("こんにちは世界"))  # Output: 'ja'
    print(detect_language("안녕하세요 세계"))  # Output: 'ko'
    print(detect_language("Bonjour le monde"))  # Output: 'fr'
    print(detect_language("Hallo Welt"))  # Output: 'de'
    print(detect_language("Hola mundo"))  # Output: 'es'
    print(detect_language("這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等"))  # Output: 'zh'

if __name__ == "__main__":
    test_language_detection()