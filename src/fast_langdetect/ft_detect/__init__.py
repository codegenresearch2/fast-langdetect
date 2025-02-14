# -*- coding: utf-8 -*-
# @Time    : 2024/1/17 16:00
# @Author  : sudoskys
# @File    : language_detection.py

from fast_langdetect import detect, detect_multilingual, detect_language

def is_japanese(string):
    """\n    Check if the given string contains any Japanese characters.\n\n    :param string: str sentence\n    :return: bool, True if the string contains Japanese characters, False otherwise\n    """
    for ch in string:
        if 0x3040 < ord(ch) < 0x30FF:
            return True
    return False

def detect_language_code(sentence, *, low_memory: bool = True):
    """\n    Detect the language of the given sentence and return the language code.\n\n    :param sentence: str sentence\n    :param low_memory: bool (default: True) whether to use low memory mode\n    :return: ZH, EN, JA, KO, FR, DE, ES, .... (two uppercase letters)\n    """
    lang_code = detect_language(sentence, low_memory=low_memory).upper()
    if lang_code == "JA" and not is_japanese(sentence):
        lang_code = "ZH"
    return lang_code

# Comprehensive tests for all language detection cases
def test_language_detection():
    assert detect_language_code("hello world") == "EN", "Language detection error"
    assert detect_language_code("你好世界") == "ZH", "Language detection error"
    assert detect_language_code("こんにちは世界") == "JA", "Language detection error"
    assert detect_language_code("안녕하세요 세계") == "KO", "Language detection error"
    assert detect_language_code("Bonjour le monde") == "FR", "Language detection error"
    assert detect_language_code("Hallo Welt") == "DE", "Language detection error"
    assert detect_language_code("Hola mundo") == "ES", "Language detection error"
    assert detect_language_code("这些机构主办的课程，多以基本电脑使用为主，例如文书处理、中文输入、互联网应用等") == "ZH", "Language detection error"