# -*- coding: utf-8 -*-
# @Time    : 2024/1/17 17:28
# @Author  : sudoskys
# @File    : test_language_detection.py
# @Software: PyCharm

def test_single_language_detection():
    from fast_langdetect import detect_language
    assert detect_language("hello world") == "en", "Language detection error"

def test_multilingual_detection():
    from fast_langdetect import detect_multilingual
    result = detect_multilingual("hello world", low_memory=True)
    assert result[0].get("lang") == "en", "Multilingual detection error"

def test_extended_language_detection():
    from fast_langdetect import detect_language
    assert detect_language("你好世界") == "zh", "Language detection error"
    assert detect_language("こんにちは世界") == "ja", "Language detection error"
    assert detect_language("안녕하세요 세계") == "ko", "Language detection error"
    assert detect_language("Bonjour le monde") == "fr", "Language detection error"
    assert detect_language("Hallo Welt") == "de", "Language detection error"
    assert detect_language("Hola mundo") == "es", "Language detection error"

def test_enhanced_multilingual_detection():
    from fast_langdetect import detect_multilingual
    result = detect_multilingual("Hello, world!你好世界!Привет, мир!")
    # Add assertions based on expected results for enhanced multilingual detection