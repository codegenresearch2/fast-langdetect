# -*- coding: utf-8 -*-
# @Time    : 2024/1/17 下午4:00
# @Author  : sudoskys
# @File    : __init__.py

from .infer import detect, detect_multilingual  # Ensure these imports are correct
import logging

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
    :return: ZH, EN, JA, KO, FR, DE, ES, .... (two uppercase letters)
    """
    result = detect(sentence, low_memory=low_memory)
    lang_code = result["lang"].upper()
    if lang_code == "JA" and not is_japanese(sentence):
        lang_code = "ZH"
    return lang_code

def detect_langs(sentence, *, low_memory: bool = True):
    """
    Deprecated function. Use `detect_language` instead.
    :param sentence: str sentence
    :param low_memory: bool (default: True) whether to use low memory mode
    :return: ZH, EN, JA, KO, FR, DE, ES, .... (two uppercase letters)
    """
    logging.warning("detect_langs is deprecated, use detect_language instead.")
    return detect_language(sentence, low_memory=low_memory)