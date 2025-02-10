# -*- coding: utf-8 -*-
# @Time    : 2024/1/17 下午5:28
# @Author  : sudoskys
# @File    : test_detect.py
# @Software: PyCharm

from fast_langdetect import detect, detect_multilingual

def test_language_detection_en():
    result = detect("hello world")
    assert result.lower() == "en", "Language detection error: expected 'en' but got something else"

def test_language_detection_zh():
    result = detect("你好世界")
    assert result.lower() == "zh", "Language detection error: expected 'zh' but got something else"

def test_language_detection_ja():
    result = detect("こんにちは世界")
    assert result.lower() == "ja", "Language detection error: expected 'ja' but got something else"

def test_language_detection_ru():
    result = detect("Привет, мир!")
    assert result.lower() == "ru", "Language detection error: expected 'ru' but got something else"

def test_language_detection_fr():
    result = detect("Bonjour le monde")
    assert result.lower() == "fr", "Language detection error: expected 'fr' but got something else"

def test_language_detection_de():
    result = detect("Hallo Welt")
    assert result.lower() == "de", "Language detection error: expected 'de' but got something else"

def test_language_detection_es():
    result = detect("Hola mundo")
    assert result.lower() == "es", "Language detection error: expected 'es' but got something else"

def test_language_detection_ko():
    result = detect("안녕하세요 세계")
    assert result.lower() == "ko", "Language detection error: expected 'ko' but got something else"

def test_language_detection_zh_traditional():
    result = detect("這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等")
    assert result.lower() == "zh", "Language detection error: expected 'zh' but got something else"

def test_multilingual_detection():
    result = detect_multilingual("Hello, world!你好世界!Привет, мир!")
    assert result[0].get("lang").lower() == "ja" or result[0].get("lang").lower() == "ru", "Language detection error: expected 'ja' or 'ru' but got something else"