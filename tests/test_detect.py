# -*- coding: utf-8 -*-
# @Time    : 2024/1/17 下午5:28
# @Author  : sudoskys
# @File    : test_detect.py
# @Software: PyCharm

from fast_langdetect import detect_multilingual, detect_language

def test_multilingual_detection():
    result = detect_multilingual("hello world", low_memory=True)
    assert result[0].get("lang") == "en", "Language detection error"

def test_language_detection():
    assert detect_language("hello world") == "en"
    assert detect_language("你好世界") == "zh"
    assert detect_language("こんにちは世界") == "ja"