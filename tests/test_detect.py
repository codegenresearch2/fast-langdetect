# -*- coding: utf-8 -*-
# @Time    : 2024/1/17 下午5:28
# @Author  : sudoskys
# @File    : test_detect.py
# @Software: PyCharm

from fast_langdetect import detect_language

def test_language_detection():
    from fast_langdetect import detect_language

    assert detect_language("hello world").upper() == "EN", "Language detection error: expected 'EN' but got something else"
    assert detect_language("你好世界").upper() == "ZH", "Language detection error: expected 'ZH' but got something else"
    assert detect_language("こんにちは世界").upper() == "JA", "Language detection error: expected 'JA' but got something else"
    assert detect_language("Привет, мир!").upper() == "RU", "Language detection error: expected 'RU' but got something else"
    assert detect_language("Bonjour le monde").upper() == "FR", "Language detection error: expected 'FR' but got something else"
    assert detect_language("Hallo Welt").upper() == "DE", "Language detection error: expected 'DE' but got something else"
    assert detect_language("Hola mundo").upper() == "ES", "Language detection error: expected 'ES' but got something else"
    assert detect_language("안녕하세요 세계").upper() == "KO", "Language detection error: expected 'KO' but got something else"
    assert detect_language("這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等").upper() == "ZH", "Language detection error: expected 'ZH' but got something else"