# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys
# @File    : __init__.py
# @Software: PyCharm

from fast_langdetect import detect_language

# Directly print the results of the detection functions
print(detect_language("hello world"))  # Expected output: {'lang': 'en'}
print(detect_language("你好世界"))  # Expected output: {'lang': 'zh'}
print(detect_language("こんにちは世界"))  # Expected output: {'lang': 'ja'}
print(detect_language("안녕하세요 세계"))  # Expected output: {'lang': 'ko'}
print(detect_language("Bonjour le monde"))  # Expected output: {'lang': 'fr'}
print(detect_language("Hallo Welt"))  # Expected output: {'lang': 'de'}

# Multilingual detection example
print(detect_language("Hello, world! 你好世界! こんにちは世界! 안녕하세요 세계! Bonjour le monde! Hallo Welt!"))  # Expected output: {'lang': 'en'}