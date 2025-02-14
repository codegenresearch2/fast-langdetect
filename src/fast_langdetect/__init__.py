import warnings

from .ft_detect import detect as _detect, detect_langs, detect_multilingual as _detect_multilingual

def detect_language(text):
    warnings.warn("Function 'detect_language' is deprecated. Please use 'detect' instead.", DeprecationWarning)
    return _detect(text)['lang'].upper()

def detect_text(text):
    return _detect(text)

def detect_languages(text):
    return _detect_multilingual(text)