# -*- coding: utf-8 -*-
# @Time    : 2024/1/17 下午5:28
# @Author  : sudoskys
# @File    : test_detect.py
# @Software: PyCharm

"""
This module contains test functions for the language detection functionality.
The user has preferred to enable low memory mode explicitly, maintain consistency in function parameters,
and enhance documentation for better understanding.
"""

def test_muti_detect():
    """
    Test the detect_multilingual function with low memory mode enabled.
    """
    from fast_langdetect import detect_multilingual
    result = detect_multilingual("hello world", low_memory=True)
    assert result[0].get("lang") == "en", "ft_detect error"

def test_detect():
    """
    Test the detect function with various language inputs.
    """
    from fast_langdetect import detect
    assert detect("hello world") == "en", "ft_detect error"
    assert detect("你好世界") == "zh", "ft_detect error"
    assert detect("こんにちは世界") == "ja", "ft_detect error"
    assert detect("안녕하세요 세계") == "ko", "ft_detect error"
    assert detect("Bonjour le monde") == "fr", "ft_detect error"

def test_detect_totally():
    """
    Test the detect_language function with various language inputs.
    """
    from fast_langdetect import detect_language
    assert detect_language("hello world") == "EN", "ft_detect error"
    assert detect_language("你好世界") == "ZH", "ft_detect error"
    assert detect_language("こんにちは世界") == "JA", "ft_detect error"
    assert detect_language("안녕하세요 세계") == "KO", "ft_detect error"
    assert detect_language("Bonjour le monde") == "FR", "ft_detect error"
    assert detect_language("Hallo Welt") == "DE", "ft_detect error"
    assert detect_language("這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等") == "ZH", "ft_detect error"