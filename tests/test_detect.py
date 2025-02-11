# -*- coding: utf-8 -*-
# @Time    : 2024/1/17 17:28
# @Author  : sudoskys
# @File    : test_language_detection.py
# @Software: PyCharm

def test_single_language_detection():
    from fast_langdetect import detect
    assert detect("hello world").upper() == "EN", "Language detection error"

def test_multilingual_detection():
    from fast_langdetect import detect_multilingual
    result = detect_multilingual("hello world", low_memory=True)
    assert result[0].get("lang") == "en", "Multilingual detection error"

def test_extended_language_detection():
    from fast_langdetect import detect
    assert detect("你好世界").upper() == "ZH", "Language detection error"
    assert detect("こんにちは世界").upper() == "JA", "Language detection error"
    assert detect("안녕하세요 세계").upper() == "KO", "Language detection error"
    assert detect("Bonjour le monde").upper() == "FR", "Language detection error"
    assert detect("Hallo Welt").upper() == "DE", "Language detection error"
    assert detect("Hola mundo").upper() == "ES", "Language detection error"

def test_chinese_sentence_detection():
    from fast_langdetect import detect
    assert detect("这些机构主办的课程，多以基本电脑使用为主，例如文书处理、中文输入、互联网应用等").upper() == "ZH", "Language detection error"

def test_enhanced_multilingual_detection():
    from fast_langdetect import detect_multilingual
    result = detect_multilingual("Hello, world!你好世界!Привет, мир!")
    # Add assertions based on expected results for enhanced multilingual detection