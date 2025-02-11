# -*- coding: utf-8 -*-
# @Time    : 2024/1/17 下午5:28
# @Author  : sudoskys
# @File    : test_detect.py
# @Software: PyCharm

from fast_langdetect import detect_multilingual, detect_language

def test_language_detection():
    result = detect_multilingual("hello world", low_memory=True)
    assert result[0].get("lang").lower() == "en", "Language detection failed"

def test_language_code():
    assert detect_language("hello world").upper() == "EN", "Language code mismatch"
    assert detect_language("你好世界").upper() == "ZH", "Language code mismatch"
    assert detect_language("こんにちは世界").upper() == "JA", "Language code mismatch"
    assert detect_language("Привет, мир!").upper() == "RU", "Language code mismatch"
    assert detect_language("Bonjour le monde").upper() == "FR", "Language code mismatch"
    assert detect_language("Hallo Welt").upper() == "DE", "Language code mismatch"
    assert detect_language("Hola mundo").upper() == "ES", "Language code mismatch"
    assert detect_language("안녕하세요 세계").upper() == "KO", "Language code mismatch"

# Additional test case for Chinese
def test_chinese_detection():
    assert detect_language("這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等").upper() == "ZH", "Language code mismatch"