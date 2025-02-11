# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys
# @File    : test_detect.py
# @Software: PyCharm

import logging

def test_muti_detect():
    """Test multi-language detection."""
    from fast_langdetect import detect_multilingual
    result = detect_multilingual("hello world", low_memory=True)
    assert result[0].get("lang") == "en", "ft_detect error"

def test_detect_totally():
    """Test language detection for multiple languages."""
    from fast_langdetect import detect_language
    assert detect_language("hello world") == "EN", "ft_detect error"
    assert detect_language("你好世界") == "ZH", "ft_detect error"
    assert detect_language("こんにちは世界") == "JA", "ft_detect error"
    # Add more tests for other languages as needed
    logging.warning("Deprecation warning: detect_langs is deprecated. Use detect_language instead.")