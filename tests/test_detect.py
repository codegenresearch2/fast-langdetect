# -*- coding: utf-8 -*-
# @Time    : 2024/1/17 下午5:28
# @Author  : sudoskys
# @File    : test_detect.py
# @Software: PyCharm

from fast_langdetect import detect, detect_language

def test_muti_detect():
    from fast_langdetect.ft_detect import detect_multilingual
    result = detect_multilingual("hello world", low_memory=True)
    assert result[0].get("lang") == "en", "ft_detect error"

def test_detect():
    assert detect("hello world")["lang"] == "en", "ft_detect error"
    assert detect("你好世界")["lang"] == "zh", "ft_detect error"
    assert detect("こんにちは世界")["lang"] == "ja", "ft_detect error"

def test_detect_totally():
    assert detect_language("hello world").upper() == "EN", "ft_detect error"
    assert detect_language("你好世界").upper() == "ZH", "ft_detect error"
    assert detect_language("こんにちは世界").upper() == "JA", "ft_detect error"