# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys

"""
This module provides functions to detect the language of text using the fast_langdetect library.

Functions:
    detect_multilingual(text: str, low_memory: bool = True) -> List[Dict[str, Union[str, float]]]:
        Detects the language of the given text in multiple languages.
        Args:
            text (str): The text to be detected.
            low_memory (bool): If True, uses less memory but may be slower. Default is True.
        Returns:
            List[Dict[str, Union[str, float]]]: A list of dictionaries containing the detected language and its score.

    detect(text: str, low_memory: bool = True) -> Dict[str, str]:
        Detects the language of the given text.
        Args:
            text (str): The text to be detected.
            low_memory (bool): If True, uses less memory but may be slower. Default is True.
        Returns:
            Dict[str, str]: A dictionary containing the detected language.

    detect_language(text: str) -> str:
        Detects the language of the given text and returns it in uppercase.
        Args:
            text (str): The text to be detected.
        Returns:
            str: The detected language in uppercase.
"""

from typing import List, Dict, Union
from fast_langdetect import detect, detect_multilingual, detect_language

# 测试繁体，简体，日文，英文，韩文，法文，德文，西班牙文

print(detect_multilingual("Hello, world!你好世界!Привет, мир!"))
print(detect("hello world"))
print(detect_language("Привет, мир!"))
print(detect_language("你好世界"))
print(detect_language("こんにちは世界"))
print(detect_language("안녕하세요 세계"))
print(detect_language("Bonjour le monde"))
print(detect_language("Hallo Welt"))
print(detect_language("Hola mundo"))
print(detect_language("這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等"))