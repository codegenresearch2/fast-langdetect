# -*- coding: utf-8 -*-

import warnings
from .ft_detect import detect_single_language, detect_all_languages, detect_multilingual_languages

def deprecated(func):
    """This is a decorator which can be used to mark functions as deprecated.\n    It will result in a warning being emitted when the function is used."""
    def new_func(*args, **kwargs):
        warnings.warn("Call to deprecated function {}. Use new function instead.".format(func.__name__),
                      category=DeprecationWarning)
        return func(*args, **kwargs)
    new_func.__name__ = func.__name__
    new_func.__doc__ = func.__doc__
    new_func.__dict__.update(func.__dict__)
    return new_func

@deprecated
def detect(text):
    return detect_single_language(text)

@deprecated
def detect_langs(text):
    return detect_all_languages(text)

def test_comprehensive_language_detection():
    assert detect_single_language("hello world") == "en", "Language detection error"
    assert detect_single_language("你好世界") == "zh", "Language detection error"
    assert detect_single_language("こんにちは世界") == "ja", "Language detection error"
    assert detect_single_language("안녕하세요 세계") == "ko", "Language detection error"
    assert detect_single_language("Bonjour le monde") == "fr", "Language detection error"
    assert detect_single_language("Hallo Welt") == "de", "Language detection error"
    assert detect_single_language("Hola mundo") == "es", "Language detection error"
    assert detect_single_language("這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等") == "zh", "Language detection error"

    print(detect_multilingual_languages("Hello, world!你好世界!Привет, мир!"))


In the rewritten code, I have renamed the functions for clarity and consistency. The `detect` function has been renamed to `detect_single_language` and the `detect_langs` function has been renamed to `detect_all_languages`. I have also added a `detect_multilingual_languages` function for detecting multiple languages.

I have added a `deprecated` decorator to mark the old functions as deprecated. This will result in a warning being emitted when the old functions are used.

I have also added a `test_comprehensive_language_detection` function to test the language detection for various languages. This function asserts the expected language for each test case and prints the result of the `detect_multilingual_languages` function.