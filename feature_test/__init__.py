# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys
# @File    : language_detection.py
# @Software: PyCharm

from fast_langdetect import detect, detect_language, detect_multilingual

# Detect language of a single sentence
print(detect_language("你好世界"))  # Expected output: {'lang': 'zh', 'score': ...}

# Detect language of a multilingual sentence
print(detect_language("你好世界！Hello, world！Привет, мир！"))  # Expected output: {'lang': 'zh', 'score': ...}

# Detect languages in a multilingual sentence
print(detect_multilingual("Hello, world!你好世界!Привет, мир!"))
# Expected output: [{'lang': 'en', 'score': ...}, {'lang': 'zh', 'score': ...}, {'lang': 'ru', 'score': ...}]

# Detect language of English sentence
print(detect_language("hello world"))  # Expected output: {'lang': 'en', 'score': ...}

# Detect language of Russian sentence
print(detect_language("Привет, мир!"))  # Expected output: {'lang': 'ru', 'score': ...}

# Detect language of Japanese sentence
print(detect_language("こんにちは世界"))  # Expected output: {'lang': 'ja', 'score': ...}

# Detect language of Korean sentence
print(detect_language("안녕하세요 세계"))  # Expected output: {'lang': 'ko', 'score': ...}

# Detect language of French sentence
print(detect_language("Bonjour le monde"))  # Expected output: {'lang': 'fr', 'score': ...}

# Detect language of German sentence
print(detect_language("Hallo Welt"))  # Expected output: {'lang': 'de', 'score': ...}

# Detect language of Spanish sentence
print(detect_language("Hola mundo"))  # Expected output: {'lang': 'es', 'score': ...}

# Detect language of a complex Chinese sentence (simplified and traditional characters)
print(detect_language("这些机构主办的课程，多以基本电脑使用为主，例如文书处理、中文输入、互联网应用等"))  # Expected output: {'lang': 'zh', 'score': ...}
print(detect_language("這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等"))  # Expected output: {'lang': 'zh', 'score': ...}