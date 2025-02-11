# -*- coding: utf-8 -*-
# @Time    : 2024/1/17 17:28
# @Author  : sudoskys
# @File    : test_language_detection.py
# @Software: PyCharm

def test_multilingual_detection():
    from fast_langdetect import detect_multilingual
    result = detect_multilingual("hello world", low_memory=True)
    assert result[0].get("lang") == "en", "Language detection error: Expected 'en', but got '{}'".format(result[0].get("lang"))

def test_language_detection():
    from fast_langdetect import detect_language
    assert detect_language("hello world") == "en", "Language detection error: Expected 'en', but got '{}'".format(detect_language("hello world"))
    assert detect_language("你好世界") == "zh", "Language detection error: Expected 'zh', but got '{}'".format(detect_language("你好世界"))
    assert detect_language("こんにちは世界") == "ja", "Language detection error: Expected 'ja', but got '{}'".format(detect_language("こんにちは世界"))

def test_enhanced_multilingual_detection():
    from fast_langdetect import detect_multilingual
    result = detect_multilingual("Hello, world!你好世界!Привет, мир!")
    expected_languages = ["en", "zh", "ru"]
    detected_languages = [res.get("lang") for res in result]
    assert all(lang in detected_languages for lang in expected_languages), "Enhanced multilingual detection error: Expected languages {} not found in detected languages {}".format(expected_languages, detected_languages)


In the revised code, I have addressed the syntax error by properly formatting the comments and documentation strings. I have also made the suggested changes to the function naming, import statements, assertions, and added additional test cases for enhanced multilingual detection. The language codes used in the assertions are now consistent with the expected output, and the error messages are formatted consistently.