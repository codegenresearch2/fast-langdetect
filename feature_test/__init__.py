# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys

from typing import List, Dict, Union
from fast_langdetect import detect, detect_multilingual, detect_language

# 测试繁体，简体，日文，英文，韩文，法文，德文，西班牙文

# Detect multiple languages
multilingual_result = detect_multilingual("Hello, world!你好世界!Привет, мир!", low_memory=False)
print(multilingual_result)

# Detect specific languages
print(detect("hello world"))  # Expected output: {'lang': 'en'}
print(detect("你好世界"))  # Expected output: {'lang': 'zh'}
print(detect("こんにちは世界"))  # Expected output: {'lang': 'ja'}
print(detect("안녕하세요 세계"))  # Expected output: {'lang': 'ko'}
print(detect("Bonjour le monde"))  # Expected output: {'lang': 'fr'}
print(detect("Hallo Welt"))  # Expected output: {'lang': 'de'}
print(detect("Hola mundo"))  # Expected output: {'lang': 'es'}
print(detect("這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等"))  # Expected output: {'lang': 'zh'}

# Detect languages and print them in uppercase
print(detect_language("Привет, мир!"))  # Expected output: RU
print(detect_language("你好世界"))  # Expected output: ZH
print(detect_language("こんにちは世界"))  # Expected output: JA
print(detect_language("안녕하세요 세계"))  # Expected output: KO
print(detect_language("Bonjour le monde"))  # Expected output: FR
print(detect_language("Hallo Welt"))  # Expected output: DE
print(detect_language("Hola mundo"))  # Expected output: ES
print(detect_language("這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等"))  # Expected output: ZH