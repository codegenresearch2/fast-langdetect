# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys
# @File    : __init__.py
# @Software: PyCharm
from fast_langdetect import detect, detect_multilingual, detect_language

# Testing language detection with multiple languages
print(detect("Hello, world!"))  # Expected output: {"lang": "en", "confidence": 0.99}
print(detect("こんにちは世界"))  # Expected output: {"lang": "ja", "confidence": 0.95}
print(detect("안녕하세요 세계"))  # Expected output: {"lang": "ko", "confidence": 0.98}
print(detect("Bonjour le monde"))  # Expected output: {"lang": "fr", "confidence": 0.97}
print(detect("Hallo Welt"))  # Expected output: {"lang": "de", "confidence": 0.96}
print(detect("你好世界"))  # Expected output: {"lang": "zh", "confidence": 0.95}

# Testing detect_multilingual with multiple languages in a single string
print(detect_multilingual("Hello, world! こんにちは世界 안녕하세요 세계 Bonjour le monde Hallo Welt 你好世界"))
# Expected output: [{"lang": "en", "confidence": 0.99}, {"lang": "ja", "confidence": 0.95}, {"lang": "ko", "confidence": 0.98}, {"lang": "fr", "confidence": 0.97}, {"lang": "de", "confidence": 0.96}, {"lang": "zh", "confidence": 0.95}]