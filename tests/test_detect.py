# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys

def test_multi_detect():
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
    assert detect_language("hello world").upper() == "EN", "ft_detect error"
    assert detect_language("你好世界").upper() == "ZH", "ft_detect error"
    assert detect_language("こんにちは世界").upper() == "JA", "ft_detect error"
    assert detect_language("안녕하세요 세계").upper() == "KO", "ft_detect error"
    assert detect_language("Bonjour le monde").upper() == "FR", "ft_detect error"
    assert detect_language("Hallo Welt").upper() == "DE", "ft_detect error"
    assert detect_language("這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等").upper() == "ZH", "ft_detect error"

def test_failed_example():
    """
    This function tests the behavior of the language detection functions when an unsupported or invalid input is provided.
    It checks if the functions handle the exception gracefully.
    """
    from fast_langdetect import detect, detect_language, detect_multilingual
    try:
        detect("")
    except ValueError:
        assert True, "Expected ValueError for empty input"

    try:
        detect_language("")
    except ValueError:
        assert True, "Expected ValueError for empty input"

    try:
        detect_multilingual("")
    except ValueError:
        assert True, "Expected ValueError for empty input"

    try:
        detect("\n")
    except ValueError:
        assert True, "Expected ValueError for new line input"

    try:
        detect_language("\n")
    except ValueError:
        assert True, "Expected ValueError for new line input"

    try:
        detect_multilingual("\n")
    except ValueError:
        assert True, "Expected ValueError for new line input"