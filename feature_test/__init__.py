import warnings

from fast_langdetect import detect_language, detect_multilingual

def parse_text(text):
    return detect_language(text)

def detect_languages(text):
    return detect_multilingual(text)

print(parse_text("你好世界"))
print(parse_text("你好世界！Hello, world！Привет, мир！"))
print(detect_languages("Hello, world!你好世界!Привет, мир!"))

warnings.warn("The 'detect' function is deprecated. Use 'parse_text' instead.", DeprecationWarning)
print(parse_text("hello world"))

warnings.warn("The 'detect_langs' function is deprecated. Use 'detect_languages' instead.", DeprecationWarning)
print(detect_languages("Привет, мир!"))