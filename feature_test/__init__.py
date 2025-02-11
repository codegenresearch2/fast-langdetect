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

# Expected output: [{'lang': 'en', 'score': 0.99}, {'lang': 'zh', 'score': 0.01}, ...]
print(detect_multilingual("Hello, world!你好世界!Привет, мир!", low_memory=False))

# Expected output: {'lang': 'en'}
print(detect("hello world"))

# Expected output: 'RU'
print(detect_language("Привет, мир!"))

# Expected output: 'ZH'
print(detect_language("你好世界"))

# Expected output: 'JA'
print(detect_language("こんにちは世界"))

# Expected output: 'KO'
print(detect_language("안녕하세요 세계"))

# Expected output: 'FR'
print(detect_language("Bonjour le monde"))

# Expected output: 'DE'
print(detect_language("Hallo Welt"))

# Expected output: 'ES'
print(detect_language("Hola mundo"))

# Expected output: 'ZH'
print(detect_language("這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等"))