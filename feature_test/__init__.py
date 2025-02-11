# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys
# @File    : __init__.py
# @Software: PyCharm
from fast_langdetect import detect, detect_language, detect_multilingual

# Import statements should be in the same order as in the gold code
# from fast_langdetect import detect, detect_language, detect_multilingual

# 测试不同语言的检测
print(detect_language("hello world"))  # 英语
print(detect_language("你好世界"))  # 中文
print(detect_language("こんにちは世界"))  # 日语
print(detect_language("안녕하세요 세계"))  # 韩语
print(detect_language("Bonjour le monde"))  # 法语
print(detect_language("Hallo Welt"))  # 德语
print(detect_language("Привет, мир!"))  # 俄语
print(detect_language("Hola mundo"))  # 西班牙语

# 检测多种语言
print(detect_multilingual("Hello, world!你好世界!Привет, мир!Hola mundo"))

# 检测特定语言
print(detect("hello world"))  # 英语
print(detect("你好世界"))  # 中文
print(detect("こんにちは世界"))  # 日语
print(detect("안녕하세요 세계"))  # 韩语
print(detect("Bonjour le monde"))  # 法语
print(detect("Hallo Welt"))  # 德语
print(detect("Привет, мир!"))  # 俄语
print(detect("Hola mundo"))  # 西班牙语