# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys
# @File    : __init__.py.py
# @Software: PyCharm
from fast_langdetect import detect, detect_language, detect_multilingual

# 测试单个句子的语言检测
print(detect("hello world"))  # 预期输出: {'lang': 'en', 'score': 0.9999999999999999}
print(detect("Привет, мир!"))  # 预期输出: {'lang': 'ru', 'score': 0.9999999999999999}

# 测试多个句子的语言检测
results = detect_multilingual("Hello, world!你好世界!Привет, мир!")
# 预期输出格式: [{'lang': 'en', 'score': 0.9999999999999999}, {'lang': 'zh-Hans', 'score': 0.9999999999999999}, {'lang': 'ru', 'score': 0.9999999999999999}]
print(results)

# 使用 detect_language 测试单个句子的语言检测
print(detect_language("Bonjour le monde"))  # 预期输出: 'FR'
print(detect_language("Hola, mundo"))  # 预期输出: 'ES'
print(detect_language("Hallo Welt"))  # 预期输出: 'DE'
print(detect_language("안녕하세요 세계"))  # 预期输出: 'KO'
print(detect_language("こんにちは世界"))  # 预期输出: 'JA'
print(detect_language("Привіт, світ!"))  # 预期输出: 'UK'
print(detect_language("Здраво, свет!"))  # 预期输出: 'SR'
print(detect_language("这些机构主办的课程，多以基本电脑使用为主，例如文书处理、中文输入、互联网应用等"))  # 预期输出: 'ZH-Hans'