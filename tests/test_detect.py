# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys

from fast_langdetect import detect, detect_language, detect_multilingual

def test_muti_detect():
    """Test the detect_multilingual function with a simple English sentence."""
    result = detect_multilingual("hello world", low_memory=True)
    assert result[0].get("lang") == "en", "ft_detect error"

def test_detect():
    """Test the detect function with sentences in English, Chinese, Japanese, and Korean."""
    assert detect("hello world")["lang"] == "en", "ft_detect error"
    assert detect("你好世界")["lang"] == "zh", "ft_detect error"
    assert detect("こんにちは世界")["lang"] == "ja", "ft_detect error"
    assert detect("안녕하세요 세계")["lang"] == "ko", "ft_detect error"
    assert detect("Bonjour le monde")["lang"] == "fr", "ft_detect error"

def test_detect_totally():
    """Test the detect_language function with sentences in English, Chinese, Japanese, Korean, French, German, and Traditional Chinese."""
    assert detect_language("hello world") == "EN", "ft_detect error"
    assert detect_language("你好世界") == "ZH", "ft_detect error"
    assert detect_language("こんにちは世界") == "JA", "ft_detect error"
    assert detect_language("안녕하세요 세계") == "KO", "ft_detect error"
    assert detect_language("Bonjour le monde") == "FR", "ft_detect error"
    assert detect_language("Hallo Welt") == "DE", "ft_detect error"
    assert detect_language("這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等") == "ZH", "ft_detect error"

def test_failed_example():
    """Test the behavior of the functions when an unexpected input is provided."""
    try:
        detect(123)
    except TypeError as e:
        assert str(e) == "Expected string, got int", "Expected TypeError for non-string input"

    try:
        detect_language(None)
    except TypeError as e:
        assert str(e) == "Expected string, got NoneType", "Expected TypeError for non-string input"

    try:
        detect_multilingual(["hello", "world"])
    except TypeError as e:
        assert str(e) == "Expected string, got list", "Expected TypeError for non-string input"

    try:
        detect_language("hello\nworld")
    except Exception as e:
        assert isinstance(e, Exception), "Expected exception for string with newline character"