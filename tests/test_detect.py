# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys
# @File    : test_detect.py
# @Software: PyCharm

def test_muti_detect():
    """
    Test the detect_multilingual function with a multilingual input.
    """
    from fast_langdetect.ft_detect import detect_multilingual
    result = detect_multilingual("Hello, world! 你好世界! Привет, мир!", low_memory=True)
    assert result[0].get('lang') == 'en', "ft_detect error: English not detected as primary language"

def test_detect():
    """
    Test the detect function with various language inputs.
    """
    from fast_langdetect import detect
    assert detect("hello world")["lang"] == "en", "ft_detect error: Incorrect language detected"
    assert detect("你好世界")["lang"] == "zh", "ft_detect error: Incorrect language detected"
    assert detect("こんにちは世界")["lang"] == "ja", "ft_detect error: Incorrect language detected"
    assert detect("안녕하세요 세계")["lang"] == "ko", "ft_detect error: Incorrect language detected"
    assert detect("Bonjour le monde")["lang"] == "fr", "ft_detect error: Incorrect language detected"
    assert detect("Hallo Welt")["lang"] == "de", "ft_detect error: Incorrect language detected"
    assert detect("Hola mundo")["lang"] == "es", "ft_detect error: Incorrect language detected"

def test_detect_totally():
    """
    Test the detect_language function with various language inputs.
    """
    from fast_langdetect import detect_language
    assert detect_language("hello world") == "EN", "ft_detect error: Incorrect language detected"
    assert detect_language("你好世界") == "ZH", "ft_detect error: Incorrect language detected"
    assert detect_language("こんにちは世界") == "JA", "ft_detect error: Incorrect language detected"
    assert detect_language("안녕하세요 세계") == "KO", "ft_detect error: Incorrect language detected"
    assert detect_language("Bonjour le monde") == "FR", "ft_detect error: Incorrect language detected"
    assert detect_language("Hallo Welt") == "DE", "ft_detect error: Incorrect language detected"
    assert detect_language("Hola mundo") == "ES", "ft_detect error: Incorrect language detected"
    assert detect_language("這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等") == "ZH", "ft_detect error: Incorrect language detected"

def test_failed_example():
    """
    Test the detect_language function with an invalid input.
    """
    from fast_langdetect import detect
    try:
        detect(123)
    except Exception as e:
        assert isinstance(e, TypeError), "ft_detect error: Incorrect exception type raised"
        assert str(e) == "Input must be a string", "ft_detect error: Incorrect error message for invalid input"