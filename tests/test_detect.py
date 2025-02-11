# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys
# @File    : test_detect.py
# @Software: PyCharm

import logging
from fast_langdetect import detect_multilingual, detect_language

def test_multi_detect():
    """Test multi-language detection."""
    result = detect_multilingual("hello world", low_memory=True)
    assert result[0].get("lang") == "en", "Language detection error"

def test_detect_language_totally():
    """Test language detection for multiple languages."""
    assert detect_language("hello world") == "en", "Language detection error"
    assert detect_language("你好世界") == "zh", "Language detection error"
    assert detect_language("こんにちは世界") == "ja", "Language detection error"
    logging.warning("Deprecation warning: detect_langs is deprecated. Use detect_language instead.")

# Add more tests for other languages as needed


In the rewritten code, I have added logging for deprecated functionality, used consistent naming conventions for language detection functions, maintained code style with proper comments, and provided clear deprecation warnings for the old `detect_langs` function. I have also updated the method calls to use `detect_language` instead of `detect_langs`.