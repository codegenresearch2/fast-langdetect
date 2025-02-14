# -*- coding: utf-8 -*-
# @Time    : 2024/1/17 下午4:00
# @Author  : sudoskys
# @File    : __init__.py
from .infer import detect
from .infer import detect_multilingual  # noqa: F401


def is_japanese(string):
    for ch in string:
        if 0x3040 < ord(ch) < 0x30FF:
            return True
    return False


def detect_language(sentence, *, low_memory: bool = True):
    """\n    Detect language\n    :param sentence: str sentence\n    :param low_memory: bool (default: True) whether to use low memory mode\n    :return: ZH, EN, JA, KO, FR, DE, ES, .... (two uppercase letters)\n    """
    result = detect(sentence, low_memory=low_memory)
    lang_code = result.get("lang").upper()
    if lang_code == "JA" and not is_japanese(sentence):
        lang_code = "ZH"
    return lang_code


def test_language_detection():
    from fast_langdetect import detect
    assert detect_language("hello world") == "EN"
    assert detect_language("你好世界") == "ZH"
    assert detect_language("こんにちは世界") == "JA"
    assert detect_language("안녕하세요 세계") == "KO"
    assert detect_language("Bonjour le monde") == "FR"
    assert detect_language("Hallo Welt") == "DE"
    assert detect_language("Hola mundo") == "ES"
    assert detect_language("這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等") == "ZH"


# Add more comprehensive tests for language detection
def test_multilingual_detection():
    from fast_langdetect import detect_multilingual
    result = detect_multilingual("hello world 你好世界 Привет, мир!", low_memory=True)
    langs = [lang.get("lang").upper() for lang in result]
    assert "EN" in langs
    assert "ZH" in langs
    assert "JA" in langs
    assert "KO" in langs
    assert "FR" in langs
    assert "DE" in langs
    assert "ES" in langs