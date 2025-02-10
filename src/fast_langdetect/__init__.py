# -*- coding: utf-8 -*-

from .ft_detect import detect, detect_language, detect_langs, detect_multilingual
import warnings

# Deprecation warning for old functions
def detect(*args, **kwargs):
    warnings.warn("The 'detect' function is deprecated. Use 'detect_multilingual' instead.", DeprecationWarning)
    results = detect_multilingual(*args, **kwargs)
    return results[0] if results else None

# Alias for detect_multilingual
def detect_language(*args, **kwargs):
    results = detect_multilingual(*args, **kwargs)
    return results[0].get("lang") if results else None

# Additional language detection examples and test cases
def test_additional_languages():
    assert detect_multilingual("Hola mundo")[0].get("lang") == "es", "ft_detect error"
    assert detect_multilingual("Ciao mondo")[0].get("lang") == "it", "ft_detect error"
    assert detect_multilingual("Hej världen")[0].get("lang") == "sv", "ft_detect error"
    assert detect_multilingual("Hallo Welt")[0].get("lang") == "de", "ft_detect error"
    assert detect_multilingual("Привет, мир!")[0].get("lang") == "ru", "ft_detect error"

# Additional tests for deprecated functions
def test_deprecated_functions():
    assert detect("hello world")["lang"] == "en", "ft_detect error"
    assert detect_langs("Bonjour le monde")[0].get("lang") == "fr", "ft_detect error"
    assert detect_language("こんにちは世界") == "ja", "ft_detect error"