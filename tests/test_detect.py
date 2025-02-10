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
    assert detect_language("hello world").lower() == "en", "Language detection error: expected 'en' but got something else"
    assert detect_language("你好世界").lower() == "zh", "Language detection error: expected 'zh' but got something else"
    assert detect_language("こんにちは世界").lower() == "ja", "Language detection error: expected 'ja' but got something else"
    assert detect_language("Привет, мир!").lower() == "ru", "Language detection error: expected 'ru' but got something else"
    assert detect_language("Bonjour le monde").lower() == "fr", "Language detection error: expected 'fr' but got something else"
    assert detect_language("Hallo Welt").lower() == "de", "Language detection error: expected 'de' but got something else"
    assert detect_language("Hola mundo").lower() == "es", "Language detection error: expected 'es' but got something else"
    assert detect_language("안녕하세요 세계").lower() == "ko", "Language detection error: expected 'ko' but got something else"
    assert detect_language("這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等").lower() == "zh", "Language detection error: expected 'zh' but got something else"