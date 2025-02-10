# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys
# @File    : __init__.py.py
# @Software: PyCharm

from fast_langdetect import detect, detect_multilingual, detect_langs
from fast_langdetect import parse_sentence

# 测试语言检测，包括英语、西班牙语、简体中文、日语、韩语、法语、德语、乌克兰语和繁体中文
print("测试语言检测，包括英语、西班牙语、简体中文、日语、韩语、法语、德语、乌克兰语和繁体中文。")

# 直接使用函数进行语言检测
print(parse_sentence("你好世界"))  # 简体中文
print(parse_sentence("こんにちは世界"))  # 日语
print(parse_sentence("안녕하세요 세계"))  # 韩语
print(parse_sentence("Bonjour le monde"))  # 法语
print(parse_sentence("Hallo Welt"))  # 德语
print(parse_sentence("Hello, world!"))  # 英语
print(parse_sentence("¡Hola, mundo!"))  # 西班牙语
print(parse_sentence("Привет, мир!"))  # 乌克兰语
print(parse_sentence("世界，你好"))  # 繁体中文

# 使用 detect_multilingual 函数进行多语言检测
print(detect_multilingual("Hello, world!你好世界!Привет, мир!¡Hola, mundo!Bonjour le monde"))

# 使用 detect 函数进行单语言检测
print(detect("hello world"))  # 英语
print(detect("こんにちは世界"))  # 日语
print(detect("안녕하세요 세계"))  # 韩语
print(detect("Bonjour le monde"))  # 法语
print(detect("Hallo Welt"))  # 德语
print(detect("你好世界"))  # 简体中文
print(detect("¡Hola, mundo!"))  # 西班牙语
print(detect("Привет, мир!"))  # 乌克兰语
print(detect("世界，你好"))  # 繁体中文

# 使用 detect_langs 函数获取语言及其置信度
print(detect_langs("Привет, мир!"))