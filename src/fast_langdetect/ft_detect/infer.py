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
    pass

def get_model_map(low_memory=False):
    """
    Returns the model map based on the memory usage preference.

    :param low_memory: A boolean indicating whether to use low memory mode.
    :return: A tuple containing the model mode, cache directory, model name, and model URL.
    """
    if low_memory:
        return "low_mem", FTLANG_CACHE, "lid.176.ftz", "https://dl.fbaipublicfiles.com/fasttext/supervised-models/lid.176.ftz"
    else:
        return "high_mem", FTLANG_CACHE, "lid.176.bin", "https://dl.fbaipublicfiles.com/fasttext/supervised-models/lid.176.bin"

def get_model_loaded(low_memory=False, download_proxy=None):
    """
    Loads the language detection model based on the memory usage preference.

    :param low_memory: A boolean indicating whether to use low memory mode.
    :param download_proxy: A string containing the proxy URL to use for downloading the model.
    :return: The loaded language detection model.
    :raises Exception: If the model fails to load.
    """
    mode, cache, name, url = get_model_map(low_memory)
    loaded = MODELS.get(mode, None)
    if loaded:
        return loaded
    model_path = os.path.join(cache, name)
    if Path(model_path).exists():
        if Path(model_path).is_dir():
            raise Exception(f"{model_path} is a directory")
        try:
            loaded_model = fasttext.load_model(model_path)
            MODELS[mode] = loaded_model
        except Exception as e:
            logger.error(f"Error loading model {model_path}: {e}")
            raise Exception("Failed to load model")
    else:
        download(url=url, folder=cache, filename=name, proxy=download_proxy, retry_max=3, timeout=20)
        loaded_model = fasttext.load_model(model_path)
        MODELS[mode] = loaded_model
    return loaded_model

def detect(text: str, *, low_memory: bool = True, model_download_proxy: str = None) -> Dict[str, Union[str, float]]:
    """
    Detects the language of the input text.

    :param text: A string containing the input text.
    :param low_memory: A boolean indicating whether to use low memory mode.
    :param model_download_proxy: A string containing the proxy URL to use for downloading the model.
    :return: A dictionary containing the detected language and its confidence score.
    :raises DetectError: If the detection fails.
    """
    try:
        model = get_model_loaded(low_memory=low_memory, download_proxy=model_download_proxy)
        labels, scores = model.predict(text)
        label = labels[0].replace("__label__", '')
        score = min(float(scores[0]), 1.0)
        return {"language": label, "confidence": score}
    except Exception as e:
        logger.error(f"Error in detection: {e}")
        raise DetectError("Detection failed")

def detect_multilingual(text: str, *, low_memory: bool = True, model_download_proxy: str = None, k: int = 5, threshold: float = 0.0, on_unicode_error: str = "strict") -> List[dict]:
    """
    Detects multiple languages in the input text.

    :param text: A string containing the input text.
    :param low_memory: A boolean indicating whether to use low memory mode.
    :param model_download_proxy: A string containing the proxy URL to use for downloading the model.
    :param k: An integer indicating the number of languages to return.
    :param threshold: A float indicating the minimum confidence score for a language to be returned.
    :param on_unicode_error: A string indicating how to handle Unicode errors.
    :return: A list of dictionaries containing the detected languages and their confidence scores.
    :raises DetectError: If the multilingual detection fails.
    """
    try:
        model = get_model_loaded(low_memory=low_memory, download_proxy=model_download_proxy)
        labels, scores = model.predict(text=text, k=k, threshold=threshold, on_unicode_error=on_unicode_error)
        detect_result = []
        for label, score in zip(labels, scores):
            label = label.replace("__label__", '')
            score = min(float(score), 1.0)
            detect_result.append({"language": label, "confidence": score})
        return sorted(detect_result, key=lambda i: i['confidence'], reverse=True)
    except Exception as e:
        logger.error(f"Error in multilingual detection: {e}")
        raise DetectError("Multilingual detection failed")

# Additional test cases for coverage
def test_detect():
    assert detect("Hola, mundo!")["language"] == "es", "ft_detect error"
    assert detect("Ciao, mondo!")["language"] == "it", "ft_detect error"
    assert detect("Hej, världen!")["language"] == "sv", "ft_detect error"
    assert detect("Привет, мир!")["language"] == "ru", "ft_detect error"
    assert detect("Hallo, Welt!")["language"] == "de", "ft_detect error"
    assert detect("Bonjour, le monde!")["language"] == "fr", "ft_detect error"
    assert detect("Hello, world!\nNEW LINE")["language"] == "en", "ft_detect error"

test_detect()