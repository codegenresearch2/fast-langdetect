# -*- coding: utf-8 -*-

from .ft_detect import detect, detect_multilingual, detect_language

def test_comprehensive_language_detection():
    # Test for multilingual language detection
    result = detect_multilingual("hello world", low_memory=True)
    assert result[0].get("lang") == "en", "Language detection error"

    # Test for single language detection
    assert detect("hello world")["lang"] == "en", "Language detection error"
    assert detect("你好世界")["lang"] == "zh", "Language detection error"
    assert detect("こんにちは世界")["lang"] == "ja", "Language detection error"
    assert detect("안녕하세요 세계")["lang"] == "ko", "Language detection error"
    assert detect("Bonjour le monde")["lang"] == "fr", "Language detection error"

    # Test for language code consistency
    assert detect_language("hello world") == "EN", "Language code inconsistency"
    assert detect_language("你好世界") == "ZH", "Language code inconsistency"
    assert detect_language("こんにちは世界") == "JA", "Language code inconsistency"
    assert detect_language("안녕하세요 세계") == "KO", "Language code inconsistency"
    assert detect_language("Bonjour le monde") == "FR", "Language code inconsistency"
    assert detect_language("Hallo Welt") == "DE", "Language code inconsistency"
    assert detect_language("Hola mundo") == "ES", "Language code inconsistency"
    assert detect_language("這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等") == "ZH", "Language code inconsistency"

# Deprecate old functions
import warnings

def detect_langs(text):
    warnings.warn("Function 'detect_langs' is deprecated. Use 'detect_multilingual' instead.", DeprecationWarning)
    return detect_multilingual(text)

# Initialize the functions
if __name__ == "__main__":
    test_comprehensive_language_detection()