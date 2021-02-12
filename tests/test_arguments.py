# pylint: disable=missing-module-docstring,missing-function-docstring,missing-class-docstring
from contextlib import contextmanager
from dataclasses import make_dataclass
from typing import Any, Generator, Type
from unittest.mock import patch

import pytest

import dconf


@contextmanager
def arguments(*args: str) -> Generator[None, None, None]:
    with patch("sys.argv", ["app", *args]):
        yield


def make_config(**fields: type) -> Type[Any]:
    return make_dataclass("Config", fields)


def test_valid_key_value() -> None:
    config_type = make_config(key=str)
    with arguments("key=value"):
        config = dconf.initialize(config_type)
    assert config.key == "value"


@pytest.mark.parametrize(
    "arg",
    ["nokeyvalue", "=only-value", "invalid-key=value", "öö=value", "invalid.key=value"],
)
def test_no_key_value(arg: str) -> None:
    config_type = make_config(key=str)
    with arguments(arg):
        with pytest.raises(dconf.core.InvalidArgument):
            dconf.initialize(config_type)
