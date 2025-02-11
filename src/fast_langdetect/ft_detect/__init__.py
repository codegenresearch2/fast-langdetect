# -*- coding: utf-8 -*-
# @Time    : 2024/1/17 下午4:00
# @Author  : sudoskys
# @File    : __init__.py

import logging
from .infer import detect
from .infer import detect_multilingual  # noqa: F401

def is_japanese(string):
    for ch in string:
        if 0x3040 < ord(ch) < 0x30FF:
            return True
    return False

def detect_language(sentence, *, low_memory: bool = True):
    """
    Detect language
    :param sentence: str sentence
    :param low_memory: bool (default: True) whether to use low memory mode
    :return: str language code (two uppercase letters)
    Examples:
        - "ZH" for Chinese
        - "EN" for English
        - "JA" for Japanese
        - "KO" for Korean
        - "FR" for French
        - "DE" for German
        - "ES" for Spanish
        and so on.
    """
    result = detect(sentence, low_memory=low_memory)
    lang_code = result.get("lang").upper()
    if lang_code == "JA" and not is_japanese(sentence):
        lang_code = "ZH"
    return lang_code

def detect_langs(sentence, *, low_memory: bool = True):
    """
    Deprecated: This function is deprecated. Please use detect_language instead.
    Detect language
    :param sentence: str sentence
    :param low_memory: bool (default: True) whether to use low memory mode
    :return: str language code (two uppercase letters)
    """
    logging.warning("Function 'detect_langs' is deprecated. Please use 'detect_language' instead.")
    return detect_language(sentence, low_memory=low_memory)