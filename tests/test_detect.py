# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys

def test_muti_detect():
    """
    This function tests the detect_multilingual function with a simple English sentence.
    It checks if the detected language is English.
    """
    from fast_langdetect import detect_multilingual
    result = detect_multilingual("hello world", low_memory=True)
    assert result[0].get("lang") == "en", "ft_detect error"

def test_detect():
    """
    This function tests the detect function with sentences in English, Chinese, Japanese, and Korean.
    It checks if the detected language matches the expected language.
    """
    from fast_langdetect import detect
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
    from fast_langdetect import detect_language
    assert detect_language("hello world") == "EN", "ft_detect error"
    assert detect_language("你好世界") == "ZH", "ft_detect error"
    assert detect_language("こんにちは世界") == "JA", "ft_detect error"
    assert detect_language("안녕하세요 세계") == "KO", "ft_detect error"
    assert detect_language("Bonjour le monde") == "FR", "ft_detect error"
    assert detect_language("Hallo Welt") == "DE", "ft_detect error"
    assert detect_language("這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等") == "ZH", "ft_detect error"

def test_failed_example():
    """
    This function tests the behavior of the language detection functions when an unexpected input is provided.
    It checks if the functions handle the error gracefully and return an appropriate error message.
    """
    from fast_langdetect import detect, detect_language, detect_multilingual
    try:
        detect(12345)
    except TypeError as e:
        assert str(e) == "Expected a string input, but received an integer instead.", "ft_detect error"
    try:
        detect_language(None)
    except TypeError as e:
        assert str(e) == "Expected a string input, but received a NoneType instead.", "ft_detect error"
    try:
        detect_multilingual(["hello", "world"])
    except TypeError as e:
        assert str(e) == "Expected a string input, but received a list instead.", "ft_detect error"

# Adding type checks to the language detection functions
def detect(text):
    if not isinstance(text, str):
        raise TypeError("Expected a string input, but received a {} instead.".format(type(text).__name__))
    # Rest of the function code

def detect_language(text):
    if not isinstance(text, str):
        raise TypeError("Expected a string input, but received a {} instead.".format(type(text).__name__))
    # Rest of the function code

def detect_multilingual(text, low_memory=False):
    if not isinstance(text, str):
        raise TypeError("Expected a string input, but received a {} instead.".format(type(text).__name__))
    # Rest of the function code