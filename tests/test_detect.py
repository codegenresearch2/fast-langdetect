# -*- coding: utf-8 -*-
# @Time    : 2024/1/17 下午5:28
# @Author  : sudoskys
# @File    : test_detect.py
# @Software: PyCharm

from fast_langdetect import detect_multilingual, detect_language

def test_multilingual_detection():
    result = detect_multilingual("hello world", low_memory=True)
    assert result[0]["lang"] == "en", "ft_detect error"

def test_language_detection():
    result = detect_language("hello world")
    assert result.upper() == "EN", "ft_detect error"

def test_chinese_detection():
    result = detect_language("你好世界")
    assert result.upper() == "ZH", "ft_detect error"

def test_japanese_detection():
    result = detect_language("こんにちは世界")
    assert result.upper() == "JA", "ft_detect error"

def test_russian_detection():
    result = detect_language("Привет, мир!")
    assert result.upper() == "RU", "ft_detect error"

def test_french_detection():
    result = detect_language("Bonjour le monde")
    assert result.upper() == "FR", "ft_detect error"

def test_german_detection():
    result = detect_language("Hallo Welt")
    assert result.upper() == "DE", "ft_detect error"

def test_spanish_detection():
    result = detect_language("Hola mundo")
    assert result.upper() == "ES", "ft_detect error"

def test_korean_detection():
    result = detect_language("안녕하세요 세계")
    assert result.upper() == "KO", "ft_detect error"

def test_chinese_traditional_detection():
    result = detect_language("這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等")
    assert result.upper() == "ZH", "ft_detect error"