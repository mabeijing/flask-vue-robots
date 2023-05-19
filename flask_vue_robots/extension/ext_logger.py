import re
import logging.config
from typing import TYPE_CHECKING

import yaml
from flask.logging import default_handler

if TYPE_CHECKING:
    from flask import Flask

VARIABLE_PATTERN: re.Pattern = re.compile(r'^\$\{(.*)}$')


def logging_init_app(app: "Flask", config_yaml: str = "logging.yaml", kwargs: dict = None):
    app.logger.removeHandler(default_handler)
    with open(config_yaml, mode="r", encoding="utf-8") as f:
        config = yaml.safe_load(f.read())

    kwargs = {} if kwargs is None else kwargs
    config: dict = parser(config, kwargs)
    logging.config.dictConfig(config)


def parser(config, kwargs: dict):
    if isinstance(config, list):
        for index, element in enumerate(config):
            config[index] = parser(element, kwargs)

    if isinstance(config, dict):
        return _parser_map(config, kwargs)

    if isinstance(config, (int, float)):
        return config

    if isinstance(config, str):
        match = VARIABLE_PATTERN.match(config)
        if match:
            key = match.group(1)
            value = kwargs.get(key)
            if value is None:
                raise ValueError(f"{config} not a key in {kwargs}")
            return value
    return config


def _parser_map(value: dict, kwargs: dict) -> dict:
    target_config = {}
    for key, value in value.items():
        match = VARIABLE_PATTERN.match(key)
        if match:
            _key = match.group(1)
            key = kwargs.get(_key)
            if key is None:
                raise ValueError(f"{_key} not a key in {kwargs}")
        target_config[key] = parser(value, kwargs)
    return target_config
