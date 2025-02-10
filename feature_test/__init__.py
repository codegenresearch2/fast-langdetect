# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys

"""
此模块包含用于检测给定文本语言的函数。
"""

from fast_langdetect import detect, detect_multilingual, detect_language

# 测试 detect_multilingual 函数，使用多语言输入和 low_memory 参数
# 预期输出：包含语言代码 ('lang') 和置信度分数 ('score') 的字典列表
print(detect_multilingual("Hello, world!你好世界!Привет, мир!"))
# 预期输出：包含语言代码 ('lang') 和置信度分数 ('score') 的字典列表
print(detect_multilingual("Hello, world!你好世界!Привет, мир!", low_memory=False))

# 测试 detect 函数，使用多种语言输入
# 预期输出：包含语言代码 ('lang') 和置信度分数 ('score') 的字典
print(detect("hello world"))  # 预期输出：{'lang': 'en', 'score': ...}
print(detect("你好世界"))  # 预期输出：{'lang': 'zh', 'score': ...}
print(detect("こんにちは世界"))  # 预期输出：{'lang': 'ja', 'score': ...}
print(detect("안녕하세요 세계"))  # 预期输出：{'lang': 'ko', 'score': ...}
print(detect("Bonjour le monde"))  # 预期输出：{'lang': 'fr', 'score': ...}
print(detect("Hallo Welt"))  # 预期输出：{'lang': 'de', 'score': ...}
print(detect("Hola mundo"))  # 预期输出：{'lang': 'es', 'score': ...}

# 测试 detect_language 函数，使用各种语言输入
# 预期输出：表示语言代码的字符串
print(detect_language("Привет, мир!"))  # 预期输出：'RU'
print(detect_language("你好世界"))  # 预期输出：'ZH'
print(detect_language("こんにちは世界"))  # 预期输出：'JA'
print(detect_language("안녕하세요 세계"))  # 预期输出：'KO'
print(detect_language("Bonjour le monde"))  # 预期输出：'FR'
print(detect_language("Hallo Welt"))  # 预期输出：'DE'
print(detect_language("Hola mundo"))  # 预期输出：'ES'
print(detect_language("這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等"))  # 预期输出：'ZH'