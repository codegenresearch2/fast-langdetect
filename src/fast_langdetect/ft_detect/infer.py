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

def get_model_map(low_memory=False) -> tuple:
    """
    Get the model map based on the memory usage preference.

    Args:
        low_memory (bool): Whether to use the low memory model.

    Returns:
        tuple: A tuple containing the model type, cache directory, model name, and model URL.
    """
    if low_memory:
        return "low_mem", FTLANG_CACHE, "lid.176.ftz", "https://dl.fbaipublicfiles.com/fasttext/supervised-models/lid.176.ftz"
    else:
        return "high_mem", FTLANG_CACHE, "lid.176.bin", "https://dl.fbaipublicfiles.com/fasttext/supervised-models/lid.176.bin"

def get_model_loaded(low_memory: bool = False, download_proxy: str = None) -> fasttext.FastText:
    """
    Load the language detection model based on the memory usage preference.

    Args:
        low_memory (bool): Whether to use the low memory model.
        download_proxy (str): Proxy to use for downloading the model.

    Returns:
        fasttext.FastText: The loaded language detection model.

    Raises:
        DetectError: If the model path is a directory or if there is an error loading the model.
    """
    mode, cache, name, url = get_model_map(low_memory)
    loaded = MODELS.get(mode, None)
    if loaded:
        return loaded
    model_path = os.path.join(cache, name)
    if Path(model_path).exists():
        if Path(model_path).is_dir():
            raise DetectError(f"{model_path} is a directory")
        try:
            loaded_model = fasttext.load_model(model_path)
            MODELS[mode] = loaded_model
        except Exception as e:
            logger.error(f"Error loading model {model_path}: {e}")
            raise DetectError(f"Failed to load model: {e}") from e
        else:
            return loaded_model
    download(url=url, folder=cache, filename=name, proxy=download_proxy, retry_max=3, timeout=20)
    loaded_model = fasttext.load_model(model_path)
    MODELS[mode] = loaded_model
    return loaded_model

def detect(text: str, *, low_memory: bool = True, model_download_proxy: str = None) -> Dict[str, Union[str, float]]:
    """
    Detect the language of a given text.

    Args:
        text (str): The input text.
        low_memory (bool): Whether to use the low memory model.
        model_download_proxy (str): Proxy to use for downloading the model.

    Returns:
        Dict[str, Union[str, float]]: A dictionary containing the detected language and its score.

    Raises:
        DetectError: If there is an error during language detection.
    """
    try:
        model = get_model_loaded(low_memory=low_memory, download_proxy=model_download_proxy)
        labels, scores = model.predict(text)
        label = labels[0].replace("__label__", '')
        score = min(float(scores[0]), 1.0)
        return {"language": label, "score": score}
    except Exception as e:
        raise DetectError(f"Language detection failed: {e}") from e

def detect_multilingual(text: str, *, low_memory: bool = True, model_download_proxy: str = None, k: int = 5, threshold: float = 0.0, on_unicode_error: str = "strict") -> List[dict]:
    """
    Detect multiple languages in a given text.

    Args:
        text (str): The input text.
        low_memory (bool): Whether to use the low memory model.
        model_download_proxy (str): Proxy to use for downloading the model.
        k (int): The number of top languages to return.
        threshold (float): The minimum score threshold for language detection.
        on_unicode_error (str): The error handling strategy for Unicode errors.

    Returns:
        List[dict]: A list of dictionaries containing the detected languages and their scores.

    Raises:
        DetectError: If there is an error during multilingual detection.
    """
    try:
        model = get_model_loaded(low_memory=low_memory, download_proxy=model_download_proxy)
        labels, scores = model.predict(text=text, k=k, threshold=threshold, on_unicode_error=on_unicode_error)
        detect_result = []
        for label, score in zip(labels, scores):
            label = label.replace("__label__", '')
            score = min(float(score), 1.0)
            detect_result.append({"language": label, "score": score})
        return sorted(detect_result, key=lambda i: i['score'], reverse=True)
    except Exception as e:
        raise DetectError(f"Multilingual detection failed: {e}") from e

# Testing multilingual detection functionality
print("Testing multilingual detection with high memory:")
print(detect_multilingual("Hello, world!你好世界!Привет, мир!", low_memory=False))
print("\nTesting multilingual detection with low memory:")
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