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
    Test the detection of various languages including English, Chinese, Japanese, Korean, French, German, and Spanish.
    """
    # Test detection of multiple languages
    result_multilingual = detect_multilingual("Hello, world!你好世界!Привет, мир!")
    print(result_multilingual)
    # [{'lang': 'ja', 'score': 0.32009604573249817}, {'lang': 'uk', 'score': 0.27781224250793457}, {'lang': 'zh', 'score': 0.17542070150375366}, {'lang': 'sr', 'score': 0.08751443773508072}, {'lang': 'bg', 'score': 0.05222449079155922}]

    # Test detection of English
    result_english = detect("hello world")
    print(result_english)

    # Test detection of languages
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