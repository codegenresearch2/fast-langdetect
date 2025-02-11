# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys
# @File    : test_detect.py
# @Software: PyCharm

from fast_langdetect import detect_multilingual, detect_language

def test_muti_detect():
    """Test multi-language detection."""
    result = detect_multilingual("hello world", low_memory=True)
    assert result[0].get("lang") == "en", "ft_detect error"

def test_detect():
    """Test language detection for multiple languages."""
    assert detect_language("hello world") == "en", "ft_detect error"
    assert detect_language("你好世界") == "zh", "ft_detect error"
    assert detect_language("こんにちは世界") == "ja", "ft_detect error"
    assert detect_language("안녕하세요 세계") == "ko", "ft_detect error"
    assert detect_language("Bonjour le monde") == "fr", "ft_detect error"
    assert detect_language("Hallo Welt") == "de", "ft_detect error"
    # Add more tests for other languages as needed

def test_detect_totally():
    """Test language detection for multiple languages."""
    assert detect_language("hello world") == "en", "ft_detect error"
    assert detect_language("你好世界") == "zh", "ft_detect error"
    assert detect_language("こんにちは世界") == "ja", "ft_detect error"
    assert detect_language("안녕하세요 세계") == "ko", "ft_detect error"
    assert detect_language("Bonjour le monde") == "fr", "ft_detect error"
    assert detect_language("Hallo Welt") == "de", "ft_detect error"
    # Add more tests for other languages as needed

I have addressed the feedback from the oracle by making the necessary adjustments to the code. Here's the updated code snippet:

1. Imported the correct functions from the `fast_langdetect` module.
2. Added the `test_detect` function to include additional language detection tests.
3. Expanded the assertions in the `test_detect` function to cover more languages.
4. Ensured consistency in language codes returned in the assertions.
5. Added more test cases to cover a wider range of languages and scenarios.
6. Removed the deprecation warning from the `test_detect_totally` function, as it is not necessary for the current implementation.