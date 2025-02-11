# -*- coding: utf-8 -*-
# @Time    : 2024/1/17 17:28
# @Author  : sudoskys
# @File    : test_language_detection.py
# @Software: PyCharm

def test_single_language_detection():
    from fast_langdetect import detect
    assert detect("hello world").lower() == "en", "Single language detection error"

def test_multilingual_detection():
    from fast_langdetect import detect_multilingual
    result = detect_multilingual("Hello, world!你好世界!Привет, мир!", low_memory=True)
    expected_languages = ["en", "zh", "ru"]
    detected_languages = [res.get("lang").lower() for res in result]
    assert all(lang in detected_languages for lang in expected_languages), "Multilingual detection error"

def test_additional_languages():
    from fast_langdetect import detect
    assert detect("안녕하세요 세계").lower() == "ko", "Language detection error"
    assert detect("Bonjour le monde").lower() == "fr", "Language detection error"
    assert detect("Hallo Welt").lower() == "de", "Language detection error"
    assert detect("Hola mundo").lower() == "es", "Language detection error"
    assert detect("こんにちは世界").lower() == "ja", "Language detection error"
    assert detect("这些机构主办的课程，多以基本电脑使用为主，例如文书处理、中文输入、互联网应用等").lower() == "zh", "Language detection error"