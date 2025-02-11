# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys

"""
此模块包含根据提供的规则和Oracle反馈重写的代码片段。
"""

from fast_langdetect import detect, detect_multilingual, detect_language

# 测试detect_multilingual函数，使用多种语言和low_memory设置为False
# 预期输出：[{'lang': 'en', 'score': 0.9999999999999999}, {'lang': 'zh', 'score': 0.9999999999999999}, {'lang': 'ru', 'score': 0.9999999999999999}]
print(detect_multilingual("Hello, world!你好世界!Привет, мир!", low_memory=False))

# 测试detect_multilingual函数，不使用low_memory参数
# 预期输出：[{'lang': 'en', 'score': 0.9999999999999999}, {'lang': 'zh', 'score': 0.9999999999999999}, {'lang': 'ru', 'score': 0.9999999999999999}]
print(detect_multilingual("Hello, world!你好世界!Привет, мир!"))

# 测试detect函数，使用各种语言
print(detect("hello world"))  # 英语
print(detect("你好世界"))  # 中文
print(detect("こんにちは世界"))  # 日语
print(detect("안녕하세요 세계"))  # 韩语
print(detect("Bonjour le monde"))  # 法语
print(detect("Hallo Welt"))  # 德语
print(detect("Hola mundo"))  # 西班牙语

# 测试detect_language函数，使用各种语言
print(detect_language("Привет, мир!"))  # 俄语
print(detect_language("你好世界"))  # 中文
print(detect_language("こんにちは世界"))  # 日语
print(detect_language("안녕하세요 세계"))  # 韩语
print(detect_language("Bonjour le monde"))  # 法语
print(detect_language("Hallo Welt"))  # 德语
print(detect_language("Hola mundo"))  # 西班牙语
print(detect_language("這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等"))  # 中文