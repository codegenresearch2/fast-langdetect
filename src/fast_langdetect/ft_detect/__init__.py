# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys

import logging
from fast_langdetect.ft_detect import detect

def is_japanese(string):
    for ch in string:
        if 0x3040 < ord(ch) < 0x30FF:
            return True
    return False

def detect_language(sentence, *, low_memory=True):
    """
    Detect and return the language code of the given sentence.

    :param sentence: str sentence
    :param low_memory: bool (default: True) whether to use low memory mode
    :return: Two uppercase letters representing the language code (ZH, EN, JA, KO, FR, DE, ES, ...)
    """
    lang_code = detect(sentence, low_memory=low_memory).get("lang").upper()
    if lang_code == "JA" and not is_japanese(sentence):
        lang_code = "ZH"
    return lang_code

# Deprecation warning for the old function
def detect_langs(sentence, *, low_memory=True):
    logging.warning("The 'detect_langs' function is deprecated. Please use 'detect_language' instead.")
    return detect_language(sentence, low_memory=low_memory)

# Comprehensive tests for all language detection cases
def test_language_detection():
    assert detect_language("hello world") == "EN", "Language detection error"
    assert detect_language("你好世界") == "ZH", "Language detection error"
    assert detect_language("こんにちは世界") == "JA", "Language detection error"
    assert detect_language("안녕하세요 세계") == "KO", "Language detection error"
    assert detect_language("Bonjour le monde") == "FR", "Language detection error"
    assert detect_language("Hallo Welt") == "DE", "Language detection error"
    assert detect_language("Hola mundo") == "ES", "Language detection error"
    assert detect_language("這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等") == "ZH", "Language detection error"

# Logging configuration
logging.basicConfig(level=logging.WARNING)