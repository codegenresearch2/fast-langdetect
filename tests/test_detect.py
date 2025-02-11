# -*- coding: utf-8 -*-
# @Time    : 2024/1/17 下午5:28
# @Author  : sudoskys
# @File    : test_detect.py
# @Software: PyCharm

import logging
from fast_langdetect.ft_detect import detect_multilingual, detect_language, detect_langs

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def test_muti_detect():
    from fast_langdetect.ft_detect import detect_multilingual
    result = detect_multilingual("hello world", low_memory=True)
    assert result[0].get("lang") == "en", "ft_detect error"
    logging.debug("Multi-language detection test passed.")

def test_detect():
    assert detect_langs("hello world")["lang"] == "en", "ft_detect error"
    assert detect_langs("你好世界")["lang"] == "zh", "ft_detect error"
    assert detect_langs("こんにちは世界")["lang"] == "ja", "ft_detect error"
    logging.debug("Language detection tests passed.")

def test_detect_totally():
    from fast_langdetect.ft_detect import detect_langs
    assert detect_langs("hello world")["lang"] == "en", "ft_detect error"
    assert detect_langs("你好世界")["lang"] == "zh", "ft_detect error"
    assert detect_langs("こんにちは世界")["lang"] == "ja", "ft_detect error"
    logging.debug("Language detection tests passed.")