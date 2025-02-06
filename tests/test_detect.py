import pytest

# -*- coding: utf-8 -*-
# @Time    : 2024/1/17 下午5:28
# @Author  : sudoskys
# @File    : test_detect.py
# @Software: PyCharm


@pytest.mark.parametrize("text, expected_lang", [
    ("hello world", "en"),
    ("你好世界", "zh"),
    ("こんにちは世界", "ja"),
    ("안녕하세요 세계", "ko"),
    ("Bonjour le monde", "fr"),
    ("Hallo Welt", "de"),
    ("這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等", "zh")
])
def test_detect(text, expected_lang):
    from fast_langdetect import detect
    result = detect(text)
    assert result['lang'] == expected_lang, 'ft_detect error'


@pytest.mark.parametrize("text, expected_lang", [
    ("hello world", "en"),
    ("你好世界", "zh"),
    ("こんにちは世界", "ja"),
    ("안녕하세요 세계", "ko"),
    ("Bonjour le monde", "fr"),
    ("Hallo Welt", "de"),
    ("這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等", "zh")
])
def test_detect_totally(text, expected_lang):
    from fast_langdetect import detect_language
    assert detect_language(text).upper() == expected_lang, 'ft_detect error'
