# -*- coding: utf-8 -*-
# @Time    : 2024/1/17 下午5:28
# @Author  : sudoskys
# @File    : test_detect.py
# @Software: PyCharm

from fast_langdetect import detect

def test_language_detection_en():
    result = detect("hello world")
    assert result == "en", f"Expected 'en' but got {result}"

def test_language_detection_zh():
    result = detect("你好世界")
    assert result == "zh", f"Expected 'zh' but got {result}"

def test_language_detection_ja():
    result = detect("こんにちは世界")
    assert result == "ja", f"Expected 'ja' but got {result}"

def test_language_detection_ru():
    result = detect("Привет, мир!")
    assert result == "ru", f"Expected 'ru' but got {result}"

def test_language_detection_fr():
    result = detect("Bonjour le monde")
    assert result == "fr", f"Expected 'fr' but got {result}"

def test_language_detection_de():
    result = detect("Hallo Welt")
    assert result == "de", f"Expected 'de' but got {result}"

def test_language_detection_es():
    result = detect("Hola mundo")
    assert result == "es", f"Expected 'es' but got {result}"

def test_language_detection_ko():
    result = detect("안녕하세요 세계")
    assert result == "ko", f"Expected 'ko' but got {result}"

def test_language_detection_zh_traditional():
    result = detect("這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等")
    assert result == "zh", f"Expected 'zh' but got {result}"