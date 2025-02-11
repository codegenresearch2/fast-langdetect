# -*- coding: utf-8 -*-

from .ft_detect import detect, detect_language, detect_langs, detect_multilingual  # noqa: F401

# Additional language detection examples and test cases
def test_additional_languages():
    assert detect_multilingual("Hola mundo")[0].get("lang") == "es", "Error: Spanish language detection failed"
    assert detect_multilingual("Ciao mondo")[0].get("lang") == "it", "Error: Italian language detection failed"
    assert detect_multilingual("Hej världen")[0].get("lang") == "sv", "Error: Swedish language detection failed"
    assert detect_multilingual("Hallo Welt")[0].get("lang") == "de", "Error: German language detection failed"
    assert detect_multilingual("Привет, мир!")[0].get("lang") == "ru", "Error: Russian language detection failed"

# Test cases from the gold code
def test_detect():
    assert detect("hello world")["lang"] == "en", "Error: English language detection failed"
    assert detect("你好世界")["lang"] == "zh", "Error: Chinese language detection failed"
    assert detect("こんにちは世界")["lang"] == "ja", "Error: Japanese language detection failed"
    assert detect("안녕하세요 세계")["lang"] == "ko", "Error: Korean language detection failed"
    assert detect("Bonjour le monde")["lang"] == "fr", "Error: French language detection failed"

def test_detect_totally():
    assert detect_language("hello world") == "EN", "Error: English language detection failed"
    assert detect_language("你好世界") == "ZH", "Error: Chinese language detection failed"
    assert detect_language("こんにちは世界") == "JA", "Error: Japanese language detection failed"
    assert detect_language("안녕하세요 세계") == "KO", "Error: Korean language detection failed"
    assert detect_language("Bonjour le monde") == "FR", "Error: French language detection failed"
    assert detect_language("Hallo Welt") == "DE", "Error: German language detection failed"
    assert detect_language("Hola mundo") == "ES", "Error: Spanish language detection failed"
    assert detect_language("這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等") == "ZH", "Error: Chinese language detection failed"