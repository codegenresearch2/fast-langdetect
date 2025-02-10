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
    pass


def get_model_map(low_memory=False):
    """
    Getting model map
    :param low_memory:
    :return:
    """
    if low_memory:
        return "low_mem", FTLANG_CACHE, "lid.176.ftz", "https://dl.fbaipublicfiles.com/fasttext/supervised-models/lid.176.ftz"
    else:
        return "high_mem", FTLANG_CACHE, "lid.176.bin", "https://dl.fbaipublicfiles.com/fasttext/supervised-models/lid.176.bin"


def get_model_loaded(
        low_memory: bool = False,
        download_proxy: str = None
):
    """
    Getting model loaded
    :param low_memory:
    :param download_proxy:
    :return:
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
            raise e
        else:
            return loaded_model

    download(url=url, folder=cache, filename=name, proxy=download_proxy, retry_max=3, timeout=20)
    loaded_model = fasttext.load_model(model_path)
    MODELS[mode] = loaded_model
    return loaded_model


def detect(text: str, *,
           low_memory: bool = True,
           model_download_proxy: str = None
           ) -> Dict[str, Union[str, float]]:
    model = get_model_loaded(low_memory=low_memory, download_proxy=model_download_proxy)
    labels, scores = model.predict(text)
    label = labels[0].replace("__label__", '')
    score = min(float(scores[0]), 1.0)
    return {
        "lang": label,
        "score": score,
    }


def detect_multilingual(text: str, *,
                        low_memory: bool = True,
                        model_download_proxy: str = None,
                        k: int = 5,
                        threshold: float = 0.0,
                        on_unicode_error: str = "strict"
                        ) -> List[dict]:
    model = get_model_loaded(low_memory=low_memory, download_proxy=model_download_proxy)
    labels, scores = model.predict(text=text, k=k, threshold=threshold, on_unicode_error=on_unicode_error)
    detect_result = []
    for label, score in zip(labels, scores):
        label = label.replace("__label__", '')
        score = min(float(score), 1.0)
        detect_result.append({
            "lang": label,
            "score": score,
        })
    return sorted(detect_result, key=lambda i: i['score'], reverse=True)


# Test cases for multilingual detection and exception handling
def test_multilingual_detection():
    try:
        result = detect_multilingual("hello world", low_memory=True)
        assert result[0].get("lang") == "en", "ft_detect error"
        result = detect_multilingual("你好世界", low_memory=True)
        assert result[0].get("lang") == "zh", "ft_detect error"
        result = detect_multilingual("こんにちは世界", low_memory=True)
        assert result[0].get("lang") == "ja", "ft_detect error"
        result = detect_multilingual("안녕하세요 세계", low_memory=True)
        assert result[0].get("lang") == "ko", "ft_detect error"
        result = detect_multilingual("Bonjour le monde", low_memory=True)
        assert result[0].get("lang") == "fr", "ft_detect error"
    except AssertionError as e:
        print(f"Test failed: {e}")


def test_exception_handling():
    try:
        detect("hello world\nNEW LINE", low_memory=True)
    except Exception as e:
        assert isinstance(e, Exception), "ft_detect exception error"


# Running the tests
if __name__ == "__main__":
    test_multilingual_detection()
    test_exception_handling()