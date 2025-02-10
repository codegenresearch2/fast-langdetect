# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys
# @File    : test_detect.py
# @Software: PyCharm

from fast_langdetect.ft_detect import detect_multilingual, detect_language

def test_muti_detect():
    """Test multi-language detection."""
    result = detect_multilingual("hello world", low_memory=True)
    assert result[0].get("lang").upper() == "EN", "ft_detect error"

def test_detect():
    """Test language detection using a different method."""
    assert detect_language("こんにちは世界").upper() == "JA", "ft_detect error"

# Add more tests for other languages as needed