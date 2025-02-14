# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys

from fast_langdetect import detect_language

def is_japanese(string):
    for ch in string:
        if 0x3040 < ord(ch) < 0x30FF:
            return True
    return False

def detect_language_code(sentence):
    """\n    Detect and return the language code of the given sentence.\n    :param sentence: str sentence\n    :return: Two uppercase letters representing the language code (ZH, EN, JA, KO, FR, DE, ES, ...)\n    """
    lang_code = detect_language(sentence).upper()
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
    assert detect_language_code("這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等") == "ZH", "Language detection error"