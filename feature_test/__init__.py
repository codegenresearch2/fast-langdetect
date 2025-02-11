# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys
# @File    : __init__.py
# @Software: PyCharm
import logging
from fast_langdetect import detect, detect_multilingual, detect_langs
from fast_langdetect import parse_sentence

# Configure logging
logging.basicConfig(level=logging.WARNING)

def test_detect(text):
    result = detect(text)
    assert result["lang"] == "en", "Language detection error"

def test_detect_multilingual(text):
    result = detect_multilingual(text, low_memory=True)
    assert result[0].get("lang") == "en", "Language detection error"

def test_detect_langs(text):
    result = detect_langs(text)
    assert result[0].get("lang") == "en", "Language detection error"

print(parse_sentence("你好世界"))
print(parse_sentence("你好世界！Hello, world！Привет, мир！"))
print(detect_multilingual("Hello, world!你好世界!Привет, мир!"))

print(detect("hello world"))
test_detect("hello world")

print(detect_langs("Привет, мир!"))
test_detect_langs("Привет, мир!")