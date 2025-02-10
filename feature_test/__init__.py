# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys

from fast_langdetect import detect, detect_multilingual, detect_language

def test_language_detection():
    # 测试多语言检测，不使用低内存模式
    result_multilingual_low_memory = detect_multilingual("Hello, world!你好世界!Привет, мир!", low_memory=True)
    print("Multilingual Detection (low memory):", result_multilingual_low_memory)

    # 测试多语言检测，使用低内存模式
    result_multilingual_no_low_memory = detect_multilingual("Hello, world!你好世界!Привет, мир!", low_memory=False)
    print("Multilingual Detection (no low memory):", result_multilingual_no_low_memory)

    # 测试英语检测
    print("English Detection:", detect("hello world"))

    # 测试中文检测
    print("Chinese Detection:", detect("你好世界"))  # Output: {'lang': 'zh', 'confidence': 0.99}

    # 测试日文检测
    print("Japanese Detection:", detect("こんにちは世界"))  # Output: {'lang': 'ja', 'confidence': 0.99}

    # 测试韩文检测
    print("Korean Detection:", detect("안녕하세요 세계"))  # Output: {'lang': 'ko', 'confidence': 0.99}

    # 测试法文检测
    print("French Detection:", detect("Bonjour le monde"))  # Output: {'lang': 'fr', 'confidence': 0.99}

    # 测试德文检测
    print("German Detection:", detect("Hallo Welt"))  # Output: {'lang': 'de', 'confidence': 0.99}

    # 测试西班牙文检测
    print("Spanish Detection:", detect("Hola mundo"))  # Output: {'lang': 'es', 'confidence': 0.99}

    # 测试繁体中文检测
    print("Traditional Chinese Detection:", detect("這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等"))  # Output: {'lang': 'zh', 'confidence': 0.99}

if __name__ == "__main__":
    test_language_detection()