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
    fasttext.FastText.eprint = lambda *args, **kwargs: None
except Exception:
    pass

class DetectError(Exception):
    """Custom exception for language detection errors."""
    pass

def get_model_map(low_memory=False):
    """
    Returns a tuple containing the model mode, cache directory, model name, and model URL.

    :param low_memory: A boolean indicating whether to use the low memory model.
    :return: A tuple containing the model mode, cache directory, model name, and model URL.
    """
    if low_memory:
        return "low_mem", FTLANG_CACHE, "lid.176.ftz", "https://dl.fbaipublicfiles.com/fasttext/supervised-models/lid.176.ftz"
    else:
        return "high_mem", FTLANG_CACHE, "lid.176.bin", "https://dl.fbaipublicfiles.com/fasttext/supervised-models/lid.176.bin"

def get_model_loaded(low_memory: bool = False, download_proxy: str = None) -> fasttext.FastText._FastText:
    """
    Loads the language detection model based on the low_memory parameter.

    :param low_memory: A boolean indicating whether to use the low memory model.
    :param download_proxy: A string containing the proxy URL to use for downloading the model.
    :return: The loaded language detection model.
    :raises DetectError: If there is an error loading the model.
    """
    mode, cache, name, url = get_model_map(low_memory)
    loaded = MODELS.get(mode)
    if loaded:
        return loaded

    model_path = os.path.join(cache, name)
    if Path(model_path).exists():
        if Path(model_path).is_dir():
            raise IsADirectoryError(f"{model_path} is a directory")

        try:
            loaded_model = fasttext.load_model(model_path)
            MODELS[mode] = loaded_model
        except Exception as e:
            logger.error(f"Error loading model {model_path}: {e}")
            download(url=url, folder=cache, filename=name, proxy=download_proxy)
            raise DetectError(f"Failed to load model: {e}")
        else:
            return loaded_model

    download(url=url, folder=cache, filename=name, proxy=download_proxy, retry_max=3, timeout=20)
    loaded_model = fasttext.load_model(model_path)
    MODELS[mode] = loaded_model
    return loaded_model

def detect(text: str, *, low_memory: bool = True, model_download_proxy: str = None) -> Dict[str, Union[str, float]]:
    """
    Detects the language of the input text using the language detection model.

    :param text: A string containing the text to detect the language of.
    :param low_memory: A boolean indicating whether to use the low memory model.
    :param model_download_proxy: A string containing the proxy URL to use for downloading the model.
    :return: A dictionary containing the detected language and confidence score.
    :raises DetectError: If there is an error detecting the language.
    """
    try:
        model = get_model_loaded(low_memory=low_memory, download_proxy=model_download_proxy)
        labels, scores = model.predict(text)
        label = labels[0].replace("__label__", '')
        score = min(float(scores[0]), 1.0)
        return {"lang": label, "score": score}
    except Exception as e:
        raise DetectError(f"Language detection failed: {e}")

def detect_multilingual(text: str, *, low_memory: bool = True, model_download_proxy: str = None, k: int = 5, threshold: float = 0.0, on_unicode_error: str = "strict") -> List[dict]:
    """
    Detects the languages of the input text using the language detection model and returns the top k results.

    :param text: A string containing the text to detect the languages of.
    :param low_memory: A boolean indicating whether to use the low memory model.
    :param model_download_proxy: A string containing the proxy URL to use for downloading the model.
    :param k: An integer indicating the number of top results to return.
    :param threshold: A float indicating the minimum confidence score to include a result.
    :param on_unicode_error: A string indicating how to handle Unicode errors.
    :return: A list of dictionaries containing the detected languages and confidence scores.
    :raises DetectError: If there is an error detecting the languages.
    """
    try:
        model = get_model_loaded(low_memory=low_memory, download_proxy=model_download_proxy)
        labels, scores = model.predict(text=text, k=k, threshold=threshold, on_unicode_error=on_unicode_error)
        detect_result = []
        for label, score in zip(labels, scores):
            label = label.replace("__label__", '')
            score = min(float(score), 1.0)
            detect_result.append({"lang": label, "score": score})
        return sorted(detect_result, key=lambda i: i['score'], reverse=True)
    except Exception as e:
        raise DetectError(f"Multilingual detection failed: {e}")

# Testing multilingual detection functionality
print("Testing multilingual detection functionality:")
print(detect_multilingual("Hello, world!你好世界!Привет, мир!", low_memory=False))
print(detect_multilingual("Hello, world!你好世界!Привет, мир!"))

# Testing language detection with diverse examples
print("\nTesting language detection with diverse examples:")
print(detect("hello world"))
print(detect("你好世界"))
print(detect("Привет, мир!"))
print(detect("こんにちは世界"))
print(detect("안녕하세요 세계"))
print(detect("Bonjour le monde"))
print(detect("Hallo Welt"))
print(detect("Hola mundo"))
print(detect("這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等"))