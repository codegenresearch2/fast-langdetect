# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys
# @File    : __init__.py.py
# @Software: PyCharm

from fast_langdetect import detect, detect_language, detect_multilingual

# Testing language detection for various languages

# Chinese
print(detect_language("你好世界"))
# Expected output: 'zh'

# Multilingual sentence
print(detect_language("你好世界！Hello, world！Привет, мир！"))
# Expected output: The language with the highest probability

# Multilingual detection
print(detect_multilingual("Hello, world!你好世界!Привет, мир!"))
# Expected output: A list of detected languages with their probabilities

# English using detect function
print(detect("hello world"))
# Expected output: 'en'

# Russian
print(detect_multilingual("Привет, мир!"))
# Expected output: A list with 'ru' as the detected language

# Japanese
print(detect_language("こんにちは世界"))
# Expected output: 'ja'

# Korean
print(detect_language("안녕하세요 세계"))
# Expected output: 'ko'

# French
print(detect_language("Bonjour le monde"))
# Expected output: 'fr'

# German
print(detect_language("Hallo Welt"))
# Expected output: 'de'

# Spanish
print(detect_language("Hola mundo"))
# Expected output: 'es'

# Complex Chinese sentence
print(detect_language("這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等"))
# Expected output: 'zh'