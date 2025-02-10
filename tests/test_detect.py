# -*- coding: utf-8 -*-
# @Time    : 2024/1/17 下午5:28
# @Author  : sudoskys
# @File    : test_detect.py
# @Software: PyCharm

from fast_langdetect import detect, detect_language, detect_multilingual

def test_muti_detect():
    result = detect_multilingual("hello world", low_memory=True)
    assert result[0].get("lang") == "en", "ft_detect error"

def test_detect():
    assert detect("hello world")["lang"] == "EN", "ft_detect error"
    assert detect("你好世界")["lang"] == "ZH", "ft_detect error"
    assert detect("こんにちは世界")["lang"] == "JA", "ft_detect error"

def test_detect_totally():
    assert detect_language("hello world") == "EN", "ft_detect error"
    assert detect_language("你好世界") == "ZH", "ft_detect error"
    assert detect_language("こんにちは世界") == "JA", "ft_detect error"
    assert detect_language("這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等") == "ZH", "ft_detect error"