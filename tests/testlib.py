"""common test libraries"""
from contextlib import contextmanager
from dataclasses import make_dataclass
from typing import Any, Generator, Type
from unittest.mock import patch


def make_config(**fields: type) -> Type[Any]:
    """makes a dataclass config type"""
    return make_dataclass("Config", fields)


@contextmanager
def arguments(*args: str) -> Generator[None, None, None]:
    """contextmanager with custom arguments in sys.argv"""
    with patch("sys.argv", ["app", *args]):
        yield
