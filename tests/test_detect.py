# -*- coding: utf-8 -*-
# @Time    : 2024/1/17 下午5:28
# @Author  : sudoskys
# @File    : test_detect.py
# @Software: PyCharm

from fast_langdetect import detect_multilingual, detect_language

def test_multilingual_detection():
    result = detect_multilingual("hello world", low_memory=True)
    assert result[0].get("lang").lower() == "en", "Language detection error"

def test_language_detection():
    assert detect_language("hello world").lower() == "en"
    assert detect_language("你好世界").lower() == "zh"
    assert detect_language("こんにちは世界").lower() == "ja"
    # Additional test cases
    assert detect_language("Привет, мир!").lower() == "ru"
    assert detect_language("Bonjour le monde").lower() == "fr"
    assert detect_language("Hallo Welt").lower() == "de"
    assert detect_language("Hola mundo").lower() == "es"
    assert detect_language("안녕하세요 세계").lower() == "ko"