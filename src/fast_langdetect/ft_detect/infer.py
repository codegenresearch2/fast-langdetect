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

def get_model_map(low_memory=False) -> tuple:
    """
    Returns a tuple containing the model mode, cache directory, model name, and model URL based on the low_memory flag.

    :param low_memory: A boolean flag indicating whether to use the low memory model.
    :return: A tuple containing the model mode, cache directory, model name, and model URL.
    """
    if low_memory:
        return "low_mem", FTLANG_CACHE, "lid.176.ftz", "https://dl.fbaipublicfiles.com/fasttext/supervised-models/lid.176.ftz"
    else:
        return "high_mem", FTLANG_CACHE, "lid.176.bin", "https://dl.fbaipublicfiles.com/fasttext/supervised-models/lid.176.bin"

def get_model_loaded(low_memory: bool = False, download_proxy: str = None) -> fasttext.FastText._FastText:
    """
    Loads the language detection model based on the low_memory flag and downloads it if necessary.

    :param low_memory: A boolean flag indicating whether to use the low memory model.
    :param download_proxy: The proxy to use for downloading the model.
    :return: The loaded language detection model.
    :raises Exception: If there is an error loading the model.
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
            download(url=url, folder=cache, filename=name, proxy=download_proxy)
            raise Exception(f"Error loading model {model_path}") from e
        else:
            return loaded_model

    download(url=url, folder=cache, filename=name, proxy=download_proxy, retry_max=3, timeout=20)
    loaded_model = fasttext.load_model(model_path)
    MODELS[mode] = loaded_model
    return loaded_model

def detect(text: str, *, low_memory: bool = True, model_download_proxy: str = None) -> Dict[str, Union[str, float]]:
    """
    Detects the language of the given text using the language detection model.

    :param text: The text to detect the language of.
    :param low_memory: A boolean flag indicating whether to use the low memory model.
    :param model_download_proxy: The proxy to use for downloading the model.
    :return: A dictionary containing the detected language and score.
    :raises Exception: If there is an error in the detect function.
    """
    try:
        model = get_model_loaded(low_memory=low_memory, download_proxy=model_download_proxy)
        labels, scores = model.predict(text)
        label = labels[0].replace("__label__", '')
        score = min(float(scores[0]), 1.0)
        return {"lang": label, "score": score}
    except Exception as e:
        raise Exception("Error in detect function") from e

def detect_multilingual(text: str, *, low_memory: bool = True, model_download_proxy: str = None, k: int = 5, threshold: float = 0.0, on_unicode_error: str = "strict") -> List[dict]:
    """
    Detects the languages of the given text using the language detection model and returns the top k results.

    :param text: The text to detect the languages of.
    :param low_memory: A boolean flag indicating whether to use the low memory model.
    :param model_download_proxy: The proxy to use for downloading the model.
    :param k: The number of top results to return.
    :param threshold: The minimum score threshold for a result to be included.
    :param on_unicode_error: The error handling strategy for Unicode errors.
    :return: A list of dictionaries containing the detected languages and scores.
    :raises Exception: If there is an error in the detect_multilingual function.
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
        raise Exception("Error in detect_multilingual function") from e