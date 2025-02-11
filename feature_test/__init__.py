# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys

from fast_langdetect import detect, detect_multilingual, detect_language

# 测试多语言检测函数，使用低内存模式
# 预期输出：[{'lang': 'en', 'score': ...}, {'lang': 'zh', 'score': ...}, {'lang': 'ru', 'score': ...}, ...]
print(detect_multilingual("Hello, world!你好世界!Привет, мир!こんにちは世界!안녕하세요 세계!Bonjour le monde!Hallo Welt!Hola mundo!", low_memory=False))

# 测试多语言检测函数，不使用低内存模式
# 预期输出：[{'lang': 'en', 'score': ...}, {'lang': 'zh', 'score': ...}, {'lang': 'ru', 'score': ...}, ...]
print(detect_multilingual("Hello, world!你好世界!Привет, мир!こんにちは世界!안녕하세요 세계!Bonjour le monde!Hallo Welt!Hola mundo!"))

# 测试各种语言：英语，中文，俄语，日语，韩语，法语，德语，西班牙语
print(detect("hello world"))  # 预期输出：{'lang': 'en', 'score': ...}
print(detect("你好世界"))  # 预期输出：{'lang': 'zh', 'score': ...}
print(detect("Привет, мир!"))  # 预期输出：{'lang': 'ru', 'score': ...}
print(detect("こんにちは世界"))  # 预期输出：{'lang': 'ja', 'score': ...}
print(detect("안녕하세요 세계"))  # 预期输出：{'lang': 'ko', 'score': ...}
print(detect("Bonjour le monde"))  # 预期输出：{'lang': 'fr', 'score': ...}
print(detect("Hallo Welt"))  # 预期输出：{'lang': 'de', 'score': ...}
print(detect("Hola mundo"))  # 预期输出：{'lang': 'es', 'score': ...}

# 测试检测语言函数
print(detect_language("hello world"))  # 预期输出：'en'
print(detect_language("你好世界"))  # 预期输出：'zh'
print(detect_language("Привет, мир!"))  # 预期输出：'ru'
print(detect_language("こんにちは世界"))  # 预期输出：'ja'
print(detect_language("안녕하세요 세계"))  # 预期输出：'ko'
print(detect_language("Bonjour le monde"))  # 预期输出：'fr'
print(detect_language("Hallo Welt"))  # 预期输出：'de'
print(detect_language("Hola mundo"))  # 预期输出：'es'