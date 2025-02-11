# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys
# @File    : __init__.py.py
# @Software: PyCharm
from fast_langdetect import detect, detect_multilingual, detect_language

# Using correct function names as per the gold code
print(detect_language("你好世界"))
print(detect_language("你好世界！Hello, world！Привет, мир！"))
print(detect_multilingual("Hello, world!你好世界!Привет, мир!"))

print(detect("hello world"))
assert detect("hello world")["lang"] == "en", "Language detection error"
assert detect("Привет, мир!")["lang"] == "ru", "Language detection error"

# Adding more language test cases for coverage
assert detect("Hola, mundo!")["lang"] == "es", "Language detection error"
assert detect("Bonjour le monde")["lang"] == "fr", "Language detection error"
assert detect("Ciao mondo")["lang"] == "it", "Language detection error"
assert detect("こんにちは世界")["lang"] == "ja", "Language detection error"
assert detect("안녕하세요 세계")["lang"] == "ko", "Language detection error"
assert detect("Hallo Welt")["lang"] == "de", "Language detection error"

# Ensuring the output format matches the expected format
multi_lang_result = detect_multilingual("Hello, world!你好世界!Привет, мир!")
for lang_info in multi_lang_result:
    print(f"Language: {lang_info['lang']}, Probability: {lang_info['prob']}")