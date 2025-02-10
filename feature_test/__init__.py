# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys

"""
This module contains the rewritten code snippet that follows the provided rules.
"""

from fast_langdetect import detect, detect_multilingual, detect_language

def test_language_detection():
    """
    This function tests the language detection functions with various inputs.
    It tests for exceptions and clarifies input assumptions for better understanding.
    """

    try:
        # Testing detect_multilingual function with multiple languages
        print(detect_multilingual("Hello, world!你好世界!Привет, мир!"))
    except Exception as e:
        print(f"An error occurred: {e}")

    try:
        # Testing detect function with English input
        print(detect("hello world"))
    except Exception as e:
        print(f"An error occurred: {e}")

    try:
        # Testing detect_language function with various languages
        print(detect_language("Привет, мир!"))
        print(detect_language("你好世界"))
        print(detect_language("こんにちは世界"))
        print(detect_language("안녕하세요 세계"))
        print(detect_language("Bonjour le monde"))
        print(detect_language("Hallo Welt"))
        print(detect_language("Hola mundo"))
        print(detect_language("這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等"))
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function to test language detection
test_language_detection()