# -*- coding: utf-8 -*-
# @Time    : 2024/1/17 下午5:28
# @Author  : sudoskys
# @File    : test_detect.py
# @Software: PyCharm

from fast_langdetect import detect, detect_language

def test_muti_detect():
    from fast_langdetect.ft_detect import detect_multilingual
    result = detect_multilingual("hello world", low_memory=True)
    assert result[0].get("lang") == "en", "ft_detect error"

def test_detect():
    from fast_langdetect import detect
    assert detect("hello world")["lang"] == "en", "ft_detect error"
    assert detect("你好世界")["lang"] == "zh", "ft_detect error"
    assert detect("こんにちは世界")["lang"] == "ja", "ft_detect error"
    assert detect("안녕하세요 세계")["lang"] == "ko", "ft_detect error"
    assert detect("Bonjour le monde")["lang"] == "fr", "ft_detect error"
    assert detect("Hallo Welt")["lang"] == "de", "ft_detect error"
    assert detect("Hola mundo")["lang"] == "es", "ft_detect error"

def test_detect_totally():
    from fast_langdetect import detect_language
    assert detect_language("hello world").upper() == "EN", "ft_detect error"
    assert detect_language("你好世界").upper() == "ZH", "ft_detect error"
    assert detect_language("こんにちは世界").upper() == "JA", "ft_detect error"
    assert detect_language("안녕하세요 세계").upper() == "KO", "ft_detect error"
    assert detect_language("Bonjour le monde").upper() == "FR", "ft_detect error"
    assert detect_language("Hallo Welt").upper() == "DE", "ft_detect error"
    assert detect_language("Hola mundo").upper() == "ES", "ft_detect error"