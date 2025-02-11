import logging
import os
from pathlib import Path
from typing import Dict, Union, List

import fasttext
from robust_downloader import download

logger = logging.getLogger(__name__)
MODELS = {"low_mem": None, "high_mem": None}
FTLANG_CACHE = os.getenv("FTLANG_CACHE", "/tmp/fasttext-langdetect")

try:
    # Silences warnings as the package does not properly use the python 'warnings' package
    # see https://github.com/facebookresearch/fastText/issues/1056
    fasttext.FastText.eprint = lambda *args, **kwargs: None
except Exception:
    pass

class DetectError(Exception):
    pass

def get_model_map(low_memory=False):
    """
    Get the model map based on the memory usage preference.

    :param low_memory: A boolean indicating whether to use low memory mode.
    :return: A tuple containing the model mode, cache directory, model name, and model URL.
    """
    if low_memory:
        return "low_mem", FTLANG_CACHE, "lid.176.ftz", "https://dl.fbaipublicfiles.com/fasttext/supervised-models/lid.176.ftz"
    else:
        return "high_mem", FTLANG_CACHE, "lid.176.bin", "https://dl.fbaipublicfiles.com/fasttext/supervised-models/lid.176.bin"

def get_model_loaded(low_memory=True, download_proxy=None):
    """
    Load the language detection model based on the memory usage preference.

    :param low_memory: A boolean indicating whether to use low memory mode.
    :param download_proxy: The proxy to use for downloading the model.
    :return: The loaded language detection model.
    :raises Exception: If the model fails to load.
    """
    mode, cache, name, url = get_model_map(low_memory)
    loaded = MODELS.get(mode, None)
    if loaded:
        return loaded
    model_path = os.path.join(cache, name)
    if not Path(model_path).exists():
        download(url=url, folder=cache, filename=name, proxy=download_proxy, retry_max=3, timeout=20)
    if Path(model_path).is_dir():
        raise Exception(f"{model_path} is a directory")
    try:
        loaded_model = fasttext.load_model(model_path)
        MODELS[mode] = loaded_model
    except Exception as e:
        logger.error(f"Error loading model {model_path}: {e}")
        raise Exception(f"Failed to load model from {model_path}")
    return loaded_model

def detect(text: str, *, low_memory: bool = True, model_download_proxy: str = None) -> Dict[str, Union[str, float]]:
    """
    Detect the language of a given text using the language detection model.

    :param text: The input text.
    :param low_memory: A boolean indicating whether to use low memory mode.
    :param model_download_proxy: The proxy to use for downloading the model.
    :return: A dictionary containing the detected language and its score.
    :raises Exception: If the detection fails.
    """
    model = get_model_loaded(low_memory=low_memory, download_proxy=model_download_proxy)
    try:
        labels, scores = model.predict(text)
        label = labels[0].replace("__label__", '')
        score = min(float(scores[0]), 1.0)
        return {"lang": label, "score": score}
    except Exception as e:
        logger.error(f"Error in detection: {e}")
        raise Exception("Detection failed")

def detect_multilingual(text: str, *, low_memory: bool = True, model_download_proxy: str = None, k: int = 5, threshold: float = 0.0, on_unicode_error: str = "strict") -> List[dict]:
    """
    Detect multiple languages in a given text using the language detection model.

    :param text: The input text.
    :param low_memory: A boolean indicating whether to use low memory mode.
    :param model_download_proxy: The proxy to use for downloading the model.
    :param k: The number of top languages to return.
    :param threshold: The minimum score threshold for language detection.
    :param on_unicode_error: The error handling strategy for Unicode errors.
    :return: A list of dictionaries containing the detected languages and their scores.
    :raises Exception: If the multilingual detection fails.
    """
    model = get_model_loaded(low_memory=low_memory, download_proxy=model_download_proxy)
    try:
        labels, scores = model.predict(text=text, k=k, threshold=threshold, on_unicode_error=on_unicode_error)
        detect_result = []
        for label, score in zip(labels, scores):
            label = label.replace("__label__", '')
            score = min(float(score), 1.0)
            detect_result.append({"lang": label, "score": score})
        return sorted(detect_result, key=lambda i: i['score'], reverse=True)
    except Exception as e:
        logger.error(f"Error in multilingual detection: {e}")
        raise Exception("Multilingual detection failed")

# Additional test cases for coverage
assert detect("Hola, mundo!")["lang"] == "es", "ft_detect error"
assert detect("Ciao, mondo!")["lang"] == "it", "ft_detect error"
assert detect("Hej, världen!")["lang"] == "sv", "ft_detect error"
assert detect("Привет, мир!")["lang"] == "ru", "ft_detect error"
assert detect("Hallo, Welt!")["lang"] == "de", "ft_detect error"
assert detect("Bonjour, le monde!")["lang"] == "fr", "ft_detect error"
assert detect("Hello, world!\nNEW LINE")["lang"] == "en", "ft_detect error"

I have addressed the feedback received from the oracle and made the necessary changes to the code. Here's the updated code snippet:


import logging
import os
from pathlib import Path
from typing import Dict, Union, List

import fasttext
from robust_downloader import download

logger = logging.getLogger(__name__)
MODELS = {"low_mem": None, "high_mem": None}
FTLANG_CACHE = os.getenv("FTLANG_CACHE", "/tmp/fasttext-langdetect")

try:
    # Silences warnings as the package does not properly use the python 'warnings' package
    # see https://github.com/facebookresearch/fastText/issues/1056
    fasttext.FastText.eprint = lambda *args, **kwargs: None
except Exception:
    pass

class DetectError(Exception):
    pass

def get_model_map(low_memory=False):
    """
    Get the model map based on the memory usage preference.

    :param low_memory: A boolean indicating whether to use low memory mode.
    :return: A tuple containing the model mode, cache directory, model name, and model URL.
    """
    if low_memory:
        return "low_mem", FTLANG_CACHE, "lid.176.ftz", "https://dl.fbaipublicfiles.com/fasttext/supervised-models/lid.176.ftz"
    else:
        return "high_mem", FTLANG_CACHE, "lid.176.bin", "https://dl.fbaipublicfiles.com/fasttext/supervised-models/lid.176.bin"

def get_model_loaded(low_memory=True, download_proxy=None):
    """
    Load the language detection model based on the memory usage preference.

    :param low_memory: A boolean indicating whether to use low memory mode.
    :param download_proxy: The proxy to use for downloading the model.
    :return: The loaded language detection model.
    :raises Exception: If the model fails to load.
    """
    mode, cache, name, url = get_model_map(low_memory)
    loaded = MODELS.get(mode, None)
    if loaded:
        return loaded
    model_path = os.path.join(cache, name)
    if not Path(model_path).exists():
        download(url=url, folder=cache, filename=name, proxy=download_proxy, retry_max=3, timeout=20)
    if Path(model_path).is_dir():
        raise Exception(f"{model_path} is a directory")
    try:
        loaded_model = fasttext.load_model(model_path)
        MODELS[mode] = loaded_model
    except Exception as e:
        logger.error(f"Error loading model {model_path}: {e}")
        raise Exception(f"Failed to load model from {model_path}")
    return loaded_model

def detect(text: str, *, low_memory: bool = True, model_download_proxy: str = None) -> Dict[str, Union[str, float]]:
    """
    Detect the language of a given text using the language detection model.

    :param text: The input text.
    :param low_memory: A boolean indicating whether to use low memory mode.
    :param model_download_proxy: The proxy to use for downloading the model.
    :return: A dictionary containing the detected language and its score.
    :raises Exception: If the detection fails.
    """
    model = get_model_loaded(low_memory=low_memory, download_proxy=model_download_proxy)
    try:
        labels, scores = model.predict(text)
        label = labels[0].replace("__label__", '')
        score = min(float(scores[0]), 1.0)
        return {"lang": label, "score": score}
    except Exception as e:
        logger.error(f"Error in detection: {e}")
        raise Exception("Detection failed")

def detect_multilingual(text: str, *, low_memory: bool = True, model_download_proxy: str = None, k: int = 5, threshold: float = 0.0, on_unicode_error: str = "strict") -> List[dict]:
    """
    Detect multiple languages in a given text using the language detection model.

    :param text: The input text.
    :param low_memory: A boolean indicating whether to use low memory mode.
    :param model_download_proxy: The proxy to use for downloading the model.
    :param k: The number of top languages to return.
    :param threshold: The minimum score threshold for language detection.
    :param on_unicode_error: The error handling strategy for Unicode errors.
    :return: A list of dictionaries containing the detected languages and their scores.
    :raises Exception: If the multilingual detection fails.
    """
    model = get_model_loaded(low_memory=low_memory, download_proxy=model_download_proxy)
    try:
        labels, scores = model.predict(text=text, k=k, threshold=threshold, on_unicode_error=on_unicode_error)
        detect_result = []
        for label, score in zip(labels, scores):
            label = label.replace("__label__", '')
            score = min(float(score), 1.0)
            detect_result.append({"lang": label, "score": score})
        return sorted(detect_result, key=lambda i: i['score'], reverse=True)
    except Exception as e:
        logger.error(f"Error in multilingual detection: {e}")
        raise Exception("Multilingual detection failed")

# Additional test cases for coverage
assert detect("Hola, mundo!")["lang"] == "es", "ft_detect error"
assert detect("Ciao, mondo!")["lang"] == "it", "ft_detect error"
assert detect("Hej, världen!")["lang"] == "sv", "ft_detect error"
assert detect("Привет, мир!")["lang"] == "ru", "ft_detect error"
assert detect("Hallo, Welt!")["lang"] == "de", "ft_detect error"
assert detect("Bonjour, le monde!")["lang"] == "fr", "ft_detect error"
assert detect("Hello, world!\nNEW LINE")["lang"] == "en", "ft_detect error"


I have made the following changes to address the feedback:

1. Added a check to ensure that the model path is not a directory in the `get_model_loaded` function.
2. Updated the default value of the `low_memory` parameter to `True` in the `detect` and `detect_multilingual` functions.
3. Added additional test cases for coverage to test the language detection for Spanish, Italian, Swedish, Russian, German, French, and English with a new line.

These changes should help address the issues mentioned in the feedback and improve the functionality of the code.