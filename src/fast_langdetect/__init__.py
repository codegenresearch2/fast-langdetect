# -*- coding: utf-8 -*-

from .ft_detect import detect_multilingual
import warnings

def detect(text):
    warnings.warn("The 'detect' function is deprecated. Use 'detect_multilingual' instead.", DeprecationWarning)
    result = detect_multilingual(text, low_memory=True)
    return result[0] if result else {"lang": "unknown", "score": 0.0}

def detect_langs(text):
    warnings.warn("The 'detect_langs' function is deprecated. Use 'detect_multilingual' instead.", DeprecationWarning)
    return detect_multilingual(text)

# Adding more language detection examples and test cases for coverage
def test_more_languages():
    assert detect_multilingual("Hola mundo")[0].get("lang") == "es", "ft_detect error"
    assert detect_multilingual("Ciao mondo")[0].get("lang") == "it", "ft_detect error"
    assert detect_multilingual("Привет, мир!")[0].get("lang") == "ru", "ft_detect error"
    assert detect_multilingual("Hallo Welt")[0].get("lang") == "de", "ft_detect error"
    assert detect_multilingual("Hej världen")[0].get("lang") == "sv", "ft_detect error"