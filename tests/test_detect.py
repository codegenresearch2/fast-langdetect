# -*- coding: utf-8 -*-
# @Time    : 2024/1/17 下午5:28
# @Author  : sudoskys
# @File    : test_language_detection.py
# @Software: PyCharm

import warnings
from fast_langdetect import detect_language, detect_multilingual

def test_multi_language_detection():
    result = detect_multilingual("hello world", low_memory=True)
    assert result[0].get("lang") == "en", "Language detection error"

def test_language_detection():
    assert detect_language("hello world") == "EN", "Language detection error"
    assert detect_language("你好世界") == "ZH", "Language detection error"
    assert detect_language("こんにちは世界") == "JA", "Language detection error"

# Deprecate old function with warning
def test_detect_totally():
    warnings.warn("test_detect_totally is deprecated, use test_language_detection instead", DeprecationWarning)
    assert detect_language("hello world") == "EN", "Language detection error"
    assert detect_language("你好世界") == "ZH", "Language detection error"
    assert detect_language("こんにちは世界") == "JA", "Language detection error"