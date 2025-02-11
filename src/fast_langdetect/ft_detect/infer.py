# -*- coding: utf-8 -*-
# @Time    : 2024/1/17 下午8:30
# @Author  : sudoskys
# @File    : infer.py
# @Software: PyCharm
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
    # silences warnings as the package does not properly use the python 'warnings' package
    # see https://github.com/facebookresearch/fastText/issues/1056
    fasttext.FastText.eprint = lambda *args, **kwargs: None
except Exception:
    pass


class DetectError(Exception):
    """Custom exception for detect related errors."""
    pass


def get_model_map(low_memory=False):
    """
    Returns the model map based on the low_memory flag.
    
    :param low_memory: bool - If True, returns the model for low memory usage.
    :return: tuple - (str, str, str, str) - The mode, cache directory, model name, and model URL.
    """
    if low_memory:
        return "low_mem", FTLANG_CACHE, "lid.176.ftz", "https://dl.fbaipublicfiles.com/fasttext/supervised-models/lid.176.ftz"
    else:
        return "high_mem", FTLANG_CACHE, "lid.176.bin", "https://dl.fbaipublicfiles.com/fasttext/supervised-models/lid.176.bin"


def load_model(low_memory: bool = False, download_proxy: str = None):
    """
    Loads the FastText model based on the low_memory flag.
    
    :param low_memory: bool - If True, loads the model for low memory usage.
    :param download_proxy: str - Optional proxy for downloading the model.
    :return: fasttext.Model - The loaded FastText model.
    """
    mode, cache, name, url = get_model_map(low_memory)
    if MODELS[mode] is not None:
        return MODELS[mode]

    model_path = os.path.join(cache, name)
    if Path(model_path).exists():
        if Path(model_path).is_dir():
            raise Exception(f"{model_path} is a directory")
        try:
            loaded_model = fasttext.load_model(model_path)
            MODELS[mode] = loaded_model
            return loaded_model
        except Exception as e:
            logger.error(f"Error loading model {model_path}: {e}")
            raise e

    try:
        download(url=url, folder=cache, filename=name, proxy=download_proxy, retry_max=3, timeout=20)
        loaded_model = fasttext.load_model(model_path)
        MODELS[mode] = loaded_model
        return loaded_model
    except Exception as e:
        logger.error(f"Error downloading or loading model {model_path}: {e}")
        raise e


def detect(text: str, *, low_memory: bool = True, model_download_proxy: str = None) -> Dict[str, Union[str, float]]:
    """
    Detects the language of the given text using the FastText model.
    
    :param text: str - The input text to detect the language of.
    :param low_memory: bool - If True, uses the model optimized for low memory usage.
    :param model_download_proxy: str - Optional proxy for downloading the model.
    :return: Dict[str, Union[str, float]] - A dictionary containing the detected language and its confidence score.
    :raises DetectError: If an error occurs during the detection process.
    """
    try:
        model = load_model(low_memory=low_memory, download_proxy=model_download_proxy)
        labels, scores = model.predict(text)
        label = labels[0].replace("__label__", '')
        score = min(float(scores[0]), 1.0)
        return {"lang": label, "score": score}
    except ValueError as ve:
        raise DetectError(f"Error during detection: {ve}")


def detect_multilingual(text: str, *, low_memory: bool = True, model_download_proxy: str = None, k: int = 5, threshold: float = 0.0, on_unicode_error: str = "strict") -> List[dict]:
    """
    Detects the languages of the given text using the FastText model for multiple languages.
    
    :param text: str - The input text to detect the languages of.
    :param low_memory: bool - If True, uses the model optimized for low memory usage.
    :param model_download_proxy: str - Optional proxy for downloading the model.
    :param k: int - Number of top language predictions to return.
    :param threshold: float - Minimum confidence score for a language to be included.
    :param on_unicode_error: str - Handling strategy for Unicode errors.
    :return: List[dict] - A list of dictionaries containing the detected languages and their confidence scores.
    :raises DetectError: If an error occurs during the multilingual detection process.
    """
    try:
        model = load_model(low_memory=low_memory, download_proxy=model_download_proxy)
        labels, scores = model.predict(text=text, k=k, threshold=threshold, on_unicode_error=on_unicode_error)
        detect_result = []
        for label, score in zip(labels, scores):
            label = label.replace("__label__", '')
            score = min(float(score), 1.0)
            detect_result.append({"lang": label, "score": score})
        return sorted(detect_result, key=lambda i: i['score'], reverse=True)
    except Exception as e:
        raise DetectError(f"Error during multilingual detection: {e}")