# -*- coding: utf-8 -*-

from .ft_detect import detect_languages, detect_multilingual_languages

def detect_single_language(text):
    """Detect the language of a single text input."""
    return detect_languages(text)[0].get("lang")

def detect_multiple_languages(text):
    """Detect multiple languages in a text input."""
    return detect_multilingual_languages(text)


This code snippet renames the imported functions for better readability and consolidates the language detection functionality into two functions: `detect_single_language` and `detect_multiple_languages`. The `detect_single_language` function returns the language code of the detected language for a single text input, while the `detect_multiple_languages` function returns a list of detected languages and their scores for a text input that may contain multiple languages.