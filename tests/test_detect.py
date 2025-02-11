# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys
# @File    : test_detect.py
# @Software: PyCharm

def test_muti_detect():
    """Test multi-language detection."""
    from fast_langdetect.ft_detect import detect_multilingual
    result = detect_multilingual("hello world", low_memory=True)
    assert result[0].get('lang') == "en", "ft_detect error"

def test_detect():
    """Test language detection for multiple languages."""
    from fast_langdetect import detect
    assert detect("hello world")['lang'] == "en", "ft_detect error"
    assert detect("你好世界")['lang'] == "zh", "ft_detect error"
    assert detect("こんにちは世界")['lang'] == "ja", "ft_detect error"
    assert detect("안녕하세요 세계")['lang'] == "ko", "ft_detect error"
    assert detect("Bonjour le monde")['lang'] == "fr", "ft_detect error"
    assert detect("Hallo Welt")['lang'] == "de", "ft_detect error"
    assert detect("这些机构主办的课程，多以基本电脑使用为主，例如文书处理、中文输入、互联网应用等")['lang'] == "zh", "ft_detect error"

def test_detect_totally():
    """Test language detection for multiple languages using detect_language."""
    from fast_langdetect import detect_language
    assert detect_language("hello world") == "EN", "ft_detect error"
    assert detect_language("你好世界") == "ZH", "ft_detect error"
    assert detect_language("こんにちは世界") == "JA", "ft_detect error"
    assert detect_language("안녕하세요 세계") == "KO", "ft_detect error"
    assert detect_language("Bonjour le monde") == "FR", "ft_detect error"
    assert detect_language("Hallo Welt") == "DE", "ft_detect error"
    assert detect_language("这些机构主办的课程，多以基本电脑使用为主，例如文书处理、中文输入、互联网应用等") == "ZH", "ft_detect error"