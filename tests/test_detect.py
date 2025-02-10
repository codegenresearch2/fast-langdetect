# -*- coding: utf-8 -*-
# @Time    : 2024/1/17 下午5:28
# @Author  : sudoskys
# @File    : test_detect.py
# @Software: PyCharm


def test_multilingual_detection():
    from fast_langdetect.ft_detect import detect_multilingual
    result = detect_multilingual("hello world", low_memory=True)
    assert result[0].get("lang") == "en", "Language detection error"


def test_language_detection():
    from fast_langdetect import detect_langs
    assert detect_langs("hello world") == "EN", "Language detection error"
    assert detect_langs("你好世界") == "ZH", "Language detection error"
    assert detect_langs("こんにちは世界") == "JA", "Language detection error"