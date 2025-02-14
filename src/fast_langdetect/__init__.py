# -*- coding: utf-8 -*-

from fast_langdetect import detect, detect_multilingual, detect_language

def test_language_detection():
    assert detect("hello world")["lang"] == "en", "Language detection error for English"
    assert detect("你好世界")["lang"] == "zh", "Language detection error for Chinese"
    assert detect("こんにちは世界")["lang"] == "ja", "Language detection error for Japanese"
    assert detect("안녕하세요 세계")["lang"] == "ko", "Language detection error for Korean"
    assert detect("Bonjour le monde")["lang"] == "fr", "Language detection error for French"
    assert detect("Hallo Welt")["lang"] == "de", "Language detection error for German"
    assert detect("Hola mundo")["lang"] == "es", "Language detection error for Spanish"
    assert detect("這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等")["lang"] == "zh", "Language detection error for Traditional Chinese"

def test_multilingual_detection():
    result = detect_multilingual("hello world", low_memory=True)
    assert any(lang["lang"] == "en" for lang in result), "Language detection error for English"
    assert any(lang["lang"] == "zh" for lang in result), "Language detection error for Chinese"
    assert any(lang["lang"] == "ja" for lang in result), "Language detection error for Japanese"
    assert any(lang["lang"] == "ko" for lang in result), "Language detection error for Korean"
    assert any(lang["lang"] == "fr" for lang in result), "Language detection error for French"
    assert any(lang["lang"] == "de" for lang in result), "Language detection error for German"
    assert any(lang["lang"] == "es" for lang in result), "Language detection error for Spanish"
    assert any(lang["lang"] == "zh" for lang in result), "Language detection error for Traditional Chinese"

def test_language_detection_totally():
    assert detect_language("hello world") == "EN", "Language detection error for English"
    assert detect_language("你好世界") == "ZH", "Language detection error for Chinese"
    assert detect_language("こんにちは世界") == "JA", "Language detection error for Japanese"
    assert detect_language("안녕하세요 세계") == "KO", "Language detection error for Korean"
    assert detect_language("Bonjour le monde") == "FR", "Language detection error for French"
    assert detect_language("Hallo Welt") == "DE", "Language detection error for German"
    assert detect_language("Hola mundo") == "ES", "Language detection error for Spanish"
    assert detect_language("這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等") == "ZH", "Language detection error for Traditional Chinese"