# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys
# @File    : __init__.py
# @Software: PyCharm

import logging
from fast_langdetect import detect, detect_language, detect_langs, detect_multilingual

# Configure logging
logging.basicConfig(level=logging.WARNING)

# Test cases for language detection
def test_detect(text):
    result = detect(text)
    assert result["lang"] == "en", "Language detection error"

def test_detect_multilingual(text):
    result = detect_multilingual(text, low_memory=True)
    assert result[0].get("lang") == "en", "Language detection error"

def test_detect_langs(text):
    result = detect_langs(text)
    assert result[0].get("lang") == "en", "Language detection error"

# Print statements with expected output
print("Expected output for '你好世界':", detect_multilingual("你好世界", low_memory=True))
print("Expected output for 'Hello, world!':", detect_multilingual("Hello, world!", low_memory=True))
print("Expected output for 'こんにちは世界':", detect_multilingual("こんにちは世界", low_memory=True))
print("Expected output for '안녕하세요 세계':", detect_multilingual("안녕하세요 세계", low_memory=True))
print("Expected output for 'Bonjour le monde':", detect_multilingual("Bonjour le monde", low_memory=True))
print("Expected output for 'Hallo Welt':", detect_multilingual("Hallo Welt", low_memory=True))
print("Expected output for '這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等':", detect_multilingual("這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等", low_memory=True))

# Running tests
test_detect("hello world")
test_detect_multilingual("hello world")
test_detect_langs("hello world")