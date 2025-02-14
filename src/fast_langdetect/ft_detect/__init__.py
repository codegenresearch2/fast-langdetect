# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys

from fast_langdetect import detect, detect_multilingual

def is_japanese(string):
    for ch in string:
        if 0x3040 < ord(ch) < 0x30FF:
            return True
    return False

def detect_language(sentence, *, low_memory: bool = True):
    """\n    Detect language\n    :param sentence: str sentence\n    :param low_memory: bool (default: True) whether to use low memory mode\n    :return: ZH, EN, JA, KO, FR, DE, ES, ... (two uppercase letters)\n    """
    lang_code = detect(sentence, low_memory=low_memory).get("lang").upper()
    if lang_code == "JA" and not is_japanese(sentence):
        lang_code = "ZH"
    return lang_code

# Adding tests
def test_language_detection():
    assert detect_language("hello world") == "EN", "Language detection error"
    assert detect_language("你好世界") == "ZH", "Language detection error"
    assert detect_language("こんにちは世界") == "JA", "Language detection error"
    assert detect_language("안녕하세요 세계") == "KO", "Language detection error"
    assert detect_language("Bonjour le monde") == "FR", "Language detection error"
    assert detect_language("Hallo Welt") == "DE", "Language detection error"
    assert detect_language("Hola mundo") == "ES", "Language detection error"
    assert detect_language("這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等") == "ZH", "Language detection error"


The code snippet has been rewritten according to the provided rules. I've made the function name consistent by renaming `detect_langs` to `detect_language`. I've also added a comprehensive test function `test_language_detection` to validate the language detection functionality for multiple languages. The existing test cases have been retained, and new test cases have been added for Spanish, German, and Traditional Chinese to enhance functionality by supporting more languages.