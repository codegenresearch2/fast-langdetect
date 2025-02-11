# -*- coding: utf-8 -*-

from .ft_detect import detect_language, detect_multilingual, detect, detect_langs  # noqa: F401

def detect(text):
    """Detect the language of a single text input."""
    lang = detect_language(text).lower()
    return {"lang": lang}

def detect_multi(text):
    """Detect multiple languages in a text input."""
    return detect_multilingual(text)