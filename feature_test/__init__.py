# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys
# @File    : __init__.py.py
# @Software: PyCharm

from fast_langdetect import detect, detect_language, detect_multilingual

# 测试各种语言的语言检测

# 中文
print(detect_language("你好世界"))
# 预期输出: 'zh'

# 多语言句子
print(detect_language("你好世界！Hello, world！Привет, мир！"))
# 预期输出: 概率最高的语言

# 多语言检测
print(detect_multilingual("Hello, world!你好世界!Привет, мир!"))
# 预期输出: 检测到的语言及其概率列表

# 使用detect函数检测英语
print(detect("hello world"))
# 预期输出: 'en'

# 俄语
print(detect_multilingual("Привет, мир!"))
# 预期输出: 包含'ru'的语言列表

# 日语
print(detect_language("こんにちは世界"))
# 预期输出: 'ja'

# 韩语
print(detect_language("안녕하세요 세계"))
# 预期输出: 'ko'

# 法语
print(detect_language("Bonjour le monde"))
# 预期输出: 'fr'

# 德语
print(detect_language("Hallo Welt"))
# 预期输出: 'de'

# 西班牙语
print(detect_language("Hola mundo"))
# 预期输出: 'es'

# 复杂的中文句子
print(detect_language("這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等"))
# 预期输出: 'zh'