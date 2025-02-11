# -*- coding: utf-8 -*-
# @Time    : 2024/1/17 17:28
# @Author  : sudoskys
# @File    : test_language_detection.py
# @Software: PyCharm

def test_single_language_detection():
    from fast_langdetect import detect_language
    assert detect_language("hello world").upper() == "EN", "Language detection error"

def test_multilingual_detection():
    from fast_langdetect import detect_multilingual
    result = detect_multilingual("Hello, world!你好世界!Привет, мир!")
    expected_languages = ["EN", "ZH", "RU"]
    detected_languages = [res.get("lang").upper() for res in result]
    assert all(lang in detected_languages for lang in expected_languages), "Enhanced multilingual detection error"

def test_additional_languages():
    from fast_langdetect import detect_language
    assert detect_language("안녕하세요 세계").upper() == "KO", "Language detection error"
    assert detect_language("Bonjour le monde").upper() == "FR", "Language detection error"
    assert detect_language("Hallo Welt").upper() == "DE", "Language detection error"
    assert detect_language("Hola mundo").upper() == "ES", "Language detection error"
    assert detect_language("这些机构主办的课程，多以基本电脑使用为主，例如文书处理、中文输入、互联网应用等").upper() == "ZH", "Language detection error"