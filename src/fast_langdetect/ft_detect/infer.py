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

def get_model_path(low_memory=False) -> str:
    """
    Returns the model path based on the low_memory flag.

    Args:
        low_memory (bool): A boolean flag indicating whether to use the low memory model.

    Returns:
        str: The model path.
    """
    model_name = "lid.176.ftz" if low_memory else "lid.176.bin"
    return os.path.join(FTLANG_CACHE, model_name)

def get_model_url(low_memory=False) -> str:
    """
    Returns the model URL based on the low_memory flag.

    Args:
        low_memory (bool): A boolean flag indicating whether to use the low memory model.

    Returns:
        str: The model URL.
    """
    model_name = "lid.176.ftz" if low_memory else "lid.176.bin"
    return f"https://dl.fbaipublicfiles.com/fasttext/supervised-models/{model_name}"

def get_model_loaded(low_memory: bool = False, download_proxy: str = None) -> fasttext.FastText._FastText:
    """
    Loads the language detection model based on the low_memory flag.

    Args:
        low_memory (bool): A boolean flag indicating whether to use the low memory model.
        download_proxy (str): The proxy to use for downloading the model if it's not already cached.

    Returns:
        fasttext.FastText._FastText: The loaded language detection model.

    Raises:
        Exception: If there's an error loading the model.
    """
    model_path = get_model_path(low_memory)
    model_url = get_model_url(low_memory)
    model_key = "low_mem" if low_memory else "high_mem"

    loaded = MODELS.get(model_key, None)
    if loaded:
        return loaded

    if Path(model_path).exists():
        if Path(model_path).is_dir():
            raise Exception(f"{model_path} is a directory")
        try:
            loaded_model = fasttext.load_model(model_path)
            MODELS[model_key] = loaded_model
        except Exception as e:
            logger.error(f"Error loading model {model_path}: {e}")
            download(url=model_url, folder=FTLANG_CACHE, filename=os.path.basename(model_path), proxy=download_proxy)
            raise e
        else:
            return loaded_model

    download(url=model_url, folder=FTLANG_CACHE, filename=os.path.basename(model_path), proxy=download_proxy, retry_max=3, timeout=20)
    loaded_model = fasttext.load_model(model_path)
    MODELS[model_key] = loaded_model
    return loaded_model

def detect(text: str, *, low_memory: bool = True, model_download_proxy: str = None) -> Dict[str, Union[str, float]]:
    """
    Detects the language of the given text using the language detection model.

    Args:
        text (str): The text to detect the language of.
        low_memory (bool, optional): A boolean flag indicating whether to use the low memory model. Defaults to True.
        model_download_proxy (str, optional): The proxy to use for downloading the model if it's not already cached. Defaults to None.

    Returns:
        Dict[str, Union[str, float]]: A dictionary containing the detected language and its score.

    Raises:
        DetectError: If there's an error in the detect function.
        ValueError: If the input text is empty or contains more than one line.
    """
    if not text.strip():
        raise ValueError("Input text cannot be empty")
    if '\n' in text:
        raise ValueError("Input text should contain only one line")

    try:
        model = get_model_loaded(low_memory=low_memory, download_proxy=model_download_proxy)
        labels, scores = model.predict(text)
        label = labels[0].replace("__label__", '')
        score = min(float(scores[0]), 1.0)
        return {"lang": label, "score": score}
    except Exception as e:
        raise DetectError("Error in detect function") from e

def detect_multilingual(text: str, *, low_memory: bool = True, model_download_proxy: str = None, k: int = 5, threshold: float = 0.0, on_unicode_error: str = "strict") -> List[dict]:
    """
    Detects multiple languages in the given text using the language detection model.

    Args:
        text (str): The text to detect the languages of.
        low_memory (bool, optional): A boolean flag indicating whether to use the low memory model. Defaults to True.
        model_download_proxy (str, optional): The proxy to use for downloading the model if it's not already cached. Defaults to None.
        k (int, optional): The number of top languages to return. Defaults to 5.
        threshold (float, optional): The minimum probability threshold for a language to be considered. Defaults to 0.0.
        on_unicode_error (str, optional): The error handling strategy for Unicode errors. Defaults to "strict".

    Returns:
        List[dict]: A list of dictionaries containing the detected languages and their scores.

    Raises:
        DetectError: If there's an error in the detect_multilingual function.
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
        raise DetectError("Error in detect_multilingual function") from e