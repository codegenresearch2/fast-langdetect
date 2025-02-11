# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys
# @File    : __init__.py.py
# @Software: PyCharm
from fast_langdetect import detect, detect_multilingual, detect_language

# Detecting single language for a sentence
assert detect_language("你好世界") == "zh", "Language detection error"

# Detecting multiple languages in a sentence
assert detect_multilingual("你好世界！Hello, world！Привет, мир！") == [{'lang': 'zh', 'prob': 0.9999999999999999}, {'lang': 'en', 'prob': 0.9999999999999999}, {'lang': 'ru', 'prob': 0.9999999999999999}], "Multilingual detection error"

# Detecting single language for various sentences
assert detect("hello world") == "en", "Language detection error"
assert detect("Привет, мир!") == "ru", "Language detection error"
assert detect("Hola, mundo!") == "es", "Language detection error"
assert detect("Bonjour le monde") == "fr", "Language detection error"
assert detect("Ciao mondo") == "it", "Language detection error"
assert detect("こんにちは世界") == "ja", "Language detection error"
assert detect("안녕하세요 세계") == "ko", "Language detection error"
assert detect("Hallo Welt") == "de", "Language detection error"

# Detecting multiple languages in a sentence with various languages
assert detect_multilingual("Hello, world!你好世界!Привет, мир!") == [{'lang': 'en', 'prob': 0.9999999999999999}, {'lang': 'zh', 'prob': 0.9999999999999999}, {'lang': 'ru', 'prob': 0.9999999999999999}], "Multilingual detection error"