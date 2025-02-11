# -*- coding: utf-8 -*-
# @Time    : 2024/1/17 下午4:00
# @Author  : sudoskys
# @File    : __init__.py

import logging
from .infer import detect, detect_multilingual  # noqa: F401

# Configure logging
logging.basicConfig(level=logging.INFO)

def is_japanese(string):
    for ch in string:
        if 0x3040 < ord(ch) < 0x30FF:
            return True
    return False

def detect_language(sentence, *, low_memory: bool = True):
    """
    Detects the language of the given sentence.
    
    :param sentence: str sentence to detect language for
    :param low_memory: bool (default: True) whether to use low memory mode
    :return: str language code (two uppercase letters)
    """
    result = detect(sentence, low_memory=low_memory)
    lang_code = result.get("lang").upper()
    if lang_code == "JA" and not is_japanese(sentence):
        lang_code = "ZH"
    return lang_code

def detect_langs(sentence, *, low_memory: bool = True):
    """
    Deprecated function. Use detect_language instead.
    
    :param sentence: str sentence to detect language for
    :param low_memory: bool (default: True) whether to use low memory mode
    :return: str language code (two uppercase letters)
    """
    logging.warning("Function 'detect_langs' is deprecated. Use 'detect_language' instead.")
    return detect_language(sentence, low_memory=low_memory)

def test_all_languages():
    from fast_langdetect import detect_language
    assert detect_language("hello world") == "EN"
    assert detect_language("你好世界") == "ZH"
    assert detect_language("こんにちは世界") == "JA"
    assert detect_language("안녕하세요 세계") == "KO"
    assert detect_language("Bonjour le monde") == "FR"
    assert detect_language("Hallo Welt") == "DE"
    assert detect_language("Hola mundo") == "ES"
    assert detect_language("這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等") == "ZH"

def test_multilingual_detection():
    from fast_langdetect import detect_multilingual
    result = detect_multilingual("hello world", low_memory=True)
    assert result[0].get("lang") == "en", "ft_detect error"