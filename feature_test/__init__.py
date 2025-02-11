# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys

"""
This module provides functions to detect the language of text using the fast_langdetect library.
It includes detailed documentation for each function to ensure clarity and understanding.
"""

from fast_langdetect import detect, detect_multilingual, detect_language

def test_language_detection():
    """
    Test the language detection functions with various text inputs.
    """
    # Test for multilingual text
    result_multilingual = detect_multilingual("Hello, world!你好世界!Привет, мир!")
    print(result_multilingual)
    # Expected output: [{'lang': 'ja', 'score': 0.32009604573249817}, {'lang': 'uk', 'score': 0.27781224250793457}, {'lang': 'zh', 'score': 0.17542070150375366}, {'lang': 'sr', 'score': 0.08751443773508072}, {'lang': 'bg', 'score': 0.05222449079155922}]

    # Test for English text
    result_english = detect("hello world")
    print(result_english)
    # Expected output: {'lang': 'en'}

    # Test for Russian text
    result_russian = detect_language("Привет, мир!")
    print(result_russian)
    # Expected output: 'ru'

    # Test for Chinese text
    result_chinese = detect_language("你好世界")
    print(result_chinese)
    # Expected output: 'zh'

    # Test for Japanese text
    result_japanese = detect_language("こんにちは世界")
    print(result_japanese)
    # Expected output: 'ja'

    # Test for Korean text
    result_korean = detect_language("안녕하세요 세계")
    print(result_korean)
    # Expected output: 'ko'

    # Test for French text
    result_french = detect_language("Bonjour le monde")
    print(result_french)
    # Expected output: 'fr'

    # Test for German text
    result_german = detect_language("Hallo Welt")
    print(result_german)
    # Expected output: 'de'

    # Test for Spanish text
    result_spanish = detect_language("Hola mundo")
    print(result_spanish)
    # Expected output: 'es'

    # Test for mixed Chinese and English text
    result_mixed_chinese_english = detect_language("這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等")
    print(result_mixed_chinese_english)
    # Expected output: 'zh'

def test_exceptions():
    """
    Test the exceptions that may arise during language detection.
    """
    try:
        detect("hello world\nNEW LINE", low_memory=True)
    except Exception as e:
        print(f"Exception occurred: {e}")
        assert isinstance(e, Exception), "ft_detect exception error"