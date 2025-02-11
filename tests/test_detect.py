# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys
# @File    : test_detect.py
# @Software: PyCharm

def test_multi_detect():
    """
    Test the detect_multilingual function with various language inputs.

    The function is expected to return a list of dictionaries, each containing the detected language and its score.
    The 'low_memory' option is included for testing.
    """
    from fast_langdetect.ft_detect import detect_multilingual
    result = detect_multilingual("Hello, world!你好世界!Привет, мир!", low_memory=True)
    assert isinstance(result, list), "Expected a list of dictionaries"
    assert all(isinstance(item, dict) for item in result), "Expected a list of dictionaries"

def test_detect():
    """
    Test the detect function with various language inputs.

    The function is expected to return a dictionary containing the detected language and its score.
    """
    from fast_langdetect import detect
    assert detect("hello world")["lang"] == "en", "Language detection error"
    assert detect("你好世界")["lang"] == "zh", "Language detection error"
    assert detect("こんにちは世界")["lang"] == "ja", "Language detection error"
    assert detect("안녕하세요 세계")["lang"] == "ko", "Language detection error"
    assert detect("Bonjour le monde")["lang"] == "fr", "Language detection error"
    assert detect("Hallo Welt")["lang"] == "de", "Language detection error"
    assert detect("Hola mundo")["lang"] == "es", "Language detection error"

def test_detect_totally():
    """
    Test the detect_language function with various language inputs.

    The function is expected to return the detected language in uppercase.
    """
    from fast_langdetect import detect_language
    assert detect_language("hello world") == "EN", "Language detection error"
    assert detect_language("你好世界") == "ZH", "Language detection error"
    assert detect_language("こんにちは世界") == "JA", "Language detection error"
    assert detect_language("안녕하세요 세계") == "KO", "Language detection error"
    assert detect_language("Bonjour le monde") == "FR", "Language detection error"
    assert detect_language("Hallo Welt") == "DE", "Language detection error"
    assert detect_language("Hola mundo") == "ES", "Language detection error"
    assert detect_language("這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等") == "ZH", "Language detection error"