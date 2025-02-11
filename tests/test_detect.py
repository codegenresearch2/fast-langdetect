# -*- coding: utf-8 -*-
# @Time    : 2024/1/17 下午5:28
# @Author  : sudoskys
# @File    : test_detect.py
# @Software: PyCharm

from fast_langdetect import detect_multilingual, detect_language

def test_lang_detection():
    result = detect_multilingual("hello world", low_memory=True)
    assert result[0].get("lang").lower() == "en", f"Expected 'en' but got {result[0].get('lang')}"

def test_lang_code_check():
    assert detect_language("hello world").upper() == "EN", f"Expected 'EN' but got {detect_language('hello world')}"
    assert detect_language("你好世界").upper() == "ZH", f"Expected 'ZH' but got {detect_language('你好世界')}"
    assert detect_language("こんにちは世界").upper() == "JA", f"Expected 'JA' but got {detect_language('こんにちは世界')}"
    assert detect_language("Привет, мир!").upper() == "RU", f"Expected 'RU' but got {detect_language('Привет, мир!')}"
    assert detect_language("Bonjour le monde").upper() == "FR", f"Expected 'FR' but got {detect_language('Bonjour le monde')}"
    assert detect_language("Hallo Welt").upper() == "DE", f"Expected 'DE' but got {detect_language('Hallo Welt')}"
    assert detect_language("Hola mundo").upper() == "ES", f"Expected 'ES' but got {detect_language('Hola mundo')}"
    assert detect_language("안녕하세요 세계").upper() == "KO", f"Expected 'KO' but got {detect_language('안녕하세요 세계')}"

# Additional test case for Chinese
def test_chinese_detection():
    assert detect_language("這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等").upper() == "ZH", f"Expected 'ZH' but got {detect_language('這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等')}"