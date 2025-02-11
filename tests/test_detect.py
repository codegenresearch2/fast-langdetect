# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys

# Import necessary functions from the fast_langdetect module
from fast_langdetect import detect, detect_multilingual, detect_language

def test_muti_detect():
    """
    This function tests the detect_multilingual function with a simple English sentence.
    It checks if the detected language is English.
    """
    result = detect_multilingual("hello world", low_memory=True)
    assert result[0].get("lang") == "en", "ft_detect error"

def test_detect():
    """
    This function tests the detect function with sentences in English, Chinese, Japanese, and Korean.
    It checks if the detected language matches the expected language.
    """
    assert detect("hello world")["lang"] == "en", "ft_detect error"
    assert detect("你好世界")["lang"] == "zh", "ft_detect error"
    assert detect("こんにちは世界")["lang"] == "ja", "ft_detect error"
    assert detect("안녕하세요 세계")["lang"] == "ko", "ft_detect error"
    assert detect("Bonjour le monde")["lang"] == "fr", "ft_detect error"

def test_detect_totally():
    """
    This function tests the detect_language function with sentences in English, Chinese, Japanese, Korean, French, German, and Traditional Chinese.
    It checks if the detected language matches the expected language.
    """
    assert detect_language("hello world") == "EN", "ft_detect error"
    assert detect_language("你好世界") == "ZH", "ft_detect error"
    assert detect_language("こんにちは世界") == "JA", "ft_detect error"
    assert detect_language("안녕하세요 세계") == "KO", "ft_detect error"
    assert detect_language("Bonjour le monde") == "FR", "ft_detect error"
    assert detect_language("Hallo Welt") == "DE", "ft_detect error"
    assert detect_language("這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等") == "ZH", "ft_detect error"

# Example usage of detect_multilingual function with a multilingual sentence
print(detect_multilingual("Hello, world!你好世界!Привет, мир!", low_memory=False))
print(detect_multilingual("Hello, world!你好世界!Привет, мир!"))


This code includes example usage and enhanced documentation for better understanding. It also demonstrates the multilingual detection capabilities explicitly by using the `detect_multilingual` function with a sentence containing English, Chinese, and Russian.