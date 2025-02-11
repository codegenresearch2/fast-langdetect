# -*- coding: utf-8 -*-

from .ft_detect import detect, detect_langs, detect_multilingual, detect_language  # noqa: F401

def test_comprehensive_language_detection():
    assert detect("hello world") == {"lang": "en", "score": 1.0}, "Language detection error for 'hello world'"
    assert detect("你好世界") == {"lang": "zh", "score": 1.0}, "Language detection error for '你好世界'"
    assert detect("こんにちは世界") == {"lang": "ja", "score": 1.0}, "Language detection error for 'こんにちは世界'"
    assert detect("안녕하세요 세계") == {"lang": "ko", "score": 1.0}, "Language detection error for '안녕하세요 세계'"
    assert detect("Bonjour le monde") == {"lang": "fr", "score": 1.0}, "Language detection error for 'Bonjour le monde'"
    assert detect("Hallo Welt") == {"lang": "de", "score": 1.0}, "Language detection error for 'Hallo Welt'"
    assert detect("Hola mundo") == {"lang": "es", "score": 1.0}, "Language detection error for 'Hola mundo'"
    assert detect("這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等") == {"lang": "zh", "score": 1.0}, "Language detection error for Chinese text"

    assert detect_langs("hello world")[0].lang == "en", "Language detection error for 'hello world' using detect_langs"
    assert detect_language("こんにちは世界") == "ja", "Language detection error for 'こんにちは世界' using detect_language"

    # Additional test cases can be added here to enhance test coverage
    # Ensure to include tests for detect_multilingual if it is relevant

# Additional functions or test cases from the gold code can be added here to enhance functionality coverage
# Ensure to follow the same import order, assertion message style, and include all relevant functions