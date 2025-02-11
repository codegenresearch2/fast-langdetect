# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys

from fast_langdetect import detect, detect_multilingual, detect_language

def is_japanese(string):
    for ch in string:
        if 0x3040 < ord(ch) < 0x30FF:
            return True
    return False

def detect_language_comprehensive(sentence, low_memory=True):
    """
    Comprehensively detect language
    :param sentence: str sentence
    :param low_memory: bool (default: True) whether to use low memory mode
    :return: Two uppercase letters representing the language code
    """
    lang_code = detect_language(sentence)
    if lang_code == "JA" and not is_japanese(sentence):
        lang_code = "ZH"
    return lang_code

# Comprehensive language detection tests
def test_comprehensive_language_detection():
    assert detect_language_comprehensive("hello world") == "EN", "Language detection error"
    assert detect_language_comprehensive("你好世界") == "ZH", "Language detection error"
    assert detect_language_comprehensive("こんにちは世界") == "JA", "Language detection error"
    assert detect_language_comprehensive("안녕하세요 세계") == "KO", "Language detection error"
    assert detect_language_comprehensive("Bonjour le monde") == "FR", "Language detection error"
    assert detect_language_comprehensive("Hallo Welt") == "DE", "Language detection error"
    assert detect_language_comprehensive("Hola mundo") == "ES", "Language detection error"
    assert detect_language_comprehensive("這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等") == "ZH", "Language detection error"