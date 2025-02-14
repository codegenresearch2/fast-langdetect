# -*- coding: utf-8 -*-

from .ft_detect import detect, detect_langs, detect_multilingual  # noqa: F401

# Deprecating old functions with warnings
import warnings

def deprecated_detect():
    warnings.warn("The function 'detect' is deprecated. Please use 'detect_multilingual' instead.", DeprecationWarning)
    return detect("hello world")

def deprecated_detect_langs():
    warnings.warn("The function 'detect_langs' is deprecated. Please use 'detect_multilingual' instead.", DeprecationWarning)
    return detect_langs("hello world")

# Adding comprehensive language detection tests
def test_comprehensive_detection():
    from .ft_detect import detect_multilingual
    result = detect_multilingual("hello world", low_memory=True)
    assert result[0].get("lang") == "en", "ft_detect error"

    from .ft_detect import detect_language
    assert detect_language("hello world") == "en", "ft_detect error"
    assert detect_language("你好世界") == "zh", "ft_detect error"
    assert detect_language("こんにちは世界") == "ja", "ft_detect error"
    assert detect_language("안녕하세요 세계") == "ko", "ft_detect error"
    assert detect_language("Bonjour le monde") == "fr", "ft_detect error"
    assert detect_language("Hallo Welt") == "de", "ft_detect error"
    assert detect_language("Hola mundo") == "es", "ft_detect error"
    assert detect_language("這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等") == "zh", "ft_detect error"

# Renaming functions for clarity and consistency
def new_detect(text):
    return detect(text)

def new_detect_multilingual(text, **kwargs):
    return detect_multilingual(text, **kwargs)

def new_detect_language(text):
    return detect_language(text)