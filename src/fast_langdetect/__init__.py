# -*- coding: utf-8 -*-

from .ft_detect import detect, detect_language, detect_langs, detect_multilingual  # noqa: F401

def detect_single_language(text):
    """Detect the language of a single text input."""
    return detect(text)

def detect_multiple_languages(text):
    """Detect multiple languages in a text input."""
    return detect_multilingual(text)

def detect_language_code(text):
    """Detect the language code of a single text input."""
    return detect_language(text)