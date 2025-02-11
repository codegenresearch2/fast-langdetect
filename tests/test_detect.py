# -*- coding: utf-8 -*-
# @Time    : 2024/1/17 下午5:28
# @Author  : sudoskys
# @File    : test_detect.py
# @Software: PyCharm

from fast_langdetect.ft_detect import detect, detect_language

def test_muti_detect():
    from fast_langdetect.ft_detect import detect_multilingual
    result = detect_multilingual("hello world", low_memory=True)
    assert result[0].get("lang") == "en", "ft_detect error"

def test_detect():
    result = detect("hello world")
    assert result == "en", "ft_detect error"

    result = detect("你好世界")
    assert result == "zh", "ft_detect error"

    result = detect("こんにちは世界")
    assert result == "ja", "ft_detect error"

def test_detect_totally():
    result = detect_language("hello world")
    assert result.lower() == "en", "ft_detect error"

    result = detect_language("你好世界")
    assert result.lower() == "zh", "ft_detect error"

    result = detect_language("こんにちは世界")
    assert result.lower() == "ja", "ft_detect error"