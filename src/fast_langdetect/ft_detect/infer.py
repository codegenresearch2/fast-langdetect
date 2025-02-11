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

def get_model_map(low_memory=True):
    if low_memory:
        return "low_mem", FTLANG_CACHE, "lid.176.ftz", "https://dl.fbaipublicfiles.com/fasttext/supervised-models/lid.176.ftz"
    else:
        return "high_mem", FTLANG_CACHE, "lid.176.bin", "https://dl.fbaipublicfiles.com/fasttext/supervised-models/lid.176.bin"

def get_model_loaded(low_memory=True, download_proxy=None):
    mode, cache, name, url = get_model_map(low_memory)
    loaded = MODELS.get(mode, None)
    if loaded:
        return loaded
    model_path = os.path.join(cache, name)
    if Path(model_path).exists():
        try:
            loaded_model = fasttext.load_model(model_path)
            MODELS[mode] = loaded_model
        except Exception as e:
            logger.error(f"Error loading model {model_path}: {e}")
            download(url=url, folder=cache, filename=name, proxy=download_proxy)
            raise DetectError("Failed to load model")
        else:
            return loaded_model
    download(url=url, folder=cache, filename=name, proxy=download_proxy, retry_max=3, timeout=20)
    loaded_model = fasttext.load_model(model_path)
    MODELS[mode] = loaded_model
    return loaded_model

def detect(text: str, low_memory: bool = True, model_download_proxy: str = None) -> Dict[str, Union[str, float]]:
    try:
        model = get_model_loaded(low_memory=low_memory, download_proxy=model_download_proxy)
        labels, scores = model.predict(text)
        label = labels[0].replace("__label__", '')
        score = min(float(scores[0]), 1.0)
        return {"lang": label, "score": score}
    except Exception as e:
        logger.error(f"Error in detection: {e}")
        raise DetectError("Detection failed")

def detect_multilingual(text: str, low_memory: bool = True, model_download_proxy: str = None, k: int = 5, threshold: float = 0.0, on_unicode_error: str = "strict") -> List[dict]:
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
        logger.error(f"Error in multilingual detection: {e}")
        raise DetectError("Multilingual detection failed")

# Additional test cases for coverage
assert detect("Hola, mundo!")["lang"] == "es", "ft_detect error"
assert detect("Ciao, mondo!")["lang"] == "it", "ft_detect error"
assert detect("Hej, världen!")["lang"] == "sv", "ft_detect error"
assert detect("Привет, мир!")["lang"] == "ru", "ft_detect error"
assert detect("Hallo, Welt!")["lang"] == "de", "ft_detect error"
assert detect("Bonjour, le monde!")["lang"] == "fr", "ft_detect error"
assert detect("Hello, world!\nNEW LINE")["lang"] == "en", "ft_detect error"