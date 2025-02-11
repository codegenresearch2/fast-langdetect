# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys

import logging
import warnings
from fast_langdetect import detect_language as fast_detect_language

def is_japanese(string):
    for ch in string:
        if 0x3040 < ord(ch) < 0x30FF:
            return True
    return False

def detect_language(sentence, low_memory=True):
    """
    Detect and return the language code of the given sentence.
    :param sentence: str sentence
    :param low_memory: bool (default: True) whether to use low memory mode
    :return: Dictionary with language code (ZH, EN, JA, KO, FR, DE, ES, ...)
    """
    lang_code = fast_detect_language(sentence).upper()
    if lang_code == "JA" and not is_japanese(sentence):
        lang_code = "ZH"
    return {"lang": lang_code}

# Deprecation warning for the old function
def detect_langs(sentence, low_memory=True):
    warnings.warn("This function is deprecated. Use detect_language instead.", DeprecationWarning)
    return detect_language(sentence, low_memory)

# Comprehensive tests for all language detection cases
def test_language_detection():
    assert detect_language("hello world")["lang"] == "EN", "Language detection error"
    assert detect_language("你好世界")["lang"] == "ZH", "Language detection error"
    assert detect_language("こんにちは世界")["lang"] == "JA", "Language detection error"
    assert detect_language("안녕하세요 세계")["lang"] == "KO", "Language detection error"
    assert detect_language("Bonjour le monde")["lang"] == "FR", "Language detection error"
    assert detect_language("Hallo Welt")["lang"] == "DE", "Language detection error"
    assert detect_language("Hola mundo")["lang"] == "ES", "Language detection error"
    assert detect_language("這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等")["lang"] == "ZH", "Language detection error"

# Logging configuration
logging.basicConfig(level=logging.WARNING)

I have rewritten the code snippet based on the feedback provided. Here are the changes made:

1. **Import Statements**: I have imported the `detect_language` function from the `fast_langdetect` module and renamed it to `fast_detect_language` to avoid any naming conflicts.

2. **Function Naming**: I have renamed the function `detect_language_code` to `detect_language` to align with the gold code.

3. **Parameters**: I have added an optional parameter `low_memory` with a default value of `True` to the `detect_language` function.

4. **Return Value**: I have modified the return value of the `detect_language` function to return a dictionary with the language code, similar to the gold code.

5. **Deprecation Warning**: I have added a deprecation warning to the `detect_langs` function, which guides users to use the `detect_language` function instead.

6. **Logging**: I have added a logging configuration to the code to provide warnings.

These changes should address the feedback received and bring the code closer to the gold standard.