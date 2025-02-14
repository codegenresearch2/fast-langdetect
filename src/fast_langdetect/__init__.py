# -*- coding: utf-8 -*-

from .language_detection import detect_language  # Consolidated function for language detection

# No need to import unused functions

# Enhanced test coverage for various languages in the test code

def test_language_detection():
    assert detect_language("hello world") == "en", "Language detection error"
    assert detect_language("你好世界") == "zh", "Language detection error"
    assert detect_language("こんにちは世界") == "ja", "Language detection error"
    assert detect_language("안녕하세요 세계") == "ko", "Language detection error"
    assert detect_language("Bonjour le monde") == "fr", "Language detection error"
    assert detect_language("Hallo Welt") == "de", "Language detection error"
    assert detect_language("Hola mundo") == "es", "Language detection error"
    assert detect_language("這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等") == "zh", "Language detection error"
    assert detect_language("Привет, мир!") == "ru", "Language detection error"

The code snippet has been rewritten according to the provided rules. The function names have been made clearer for better readability. The language detection functionality has been consolidated into a single function called `detect_language`. Unnecessary imports have been removed. The test coverage has been enhanced to include additional languages for comprehensive testing.