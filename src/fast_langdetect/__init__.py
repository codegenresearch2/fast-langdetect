# -*- coding: utf-8 -*-

from .ft_detect import detect_language, detect_multilingual

def detect(text):
    """Detect the language of a single text input."""
    return detect_language(text)

def detect_multi(text):
    """Detect multiple languages in a text input."""
    return detect_multilingual(text)