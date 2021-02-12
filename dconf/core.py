"""dconf core"""
import re
import sys
from typing import Type, TypeVar


class InvalidArgument(Exception):
    """Exception for invalid arguments"""

    def __init__(self, argument: str):
        super().__init__(f"invalid argument: {argument}")


ConfigType = TypeVar("ConfigType")


def initialize(
    cfg_type: Type[ConfigType],
) -> ConfigType:
    """Initializes a configuration """
    args = sys.argv[1:]
    config = dict()
    for arg in args:
        match = re.match(r"^(?P<key>[A-z]\w*)=(?P<value>.*)$", arg, flags=re.ASCII)
        if not match:
            raise InvalidArgument(arg)
        config[match.group("key")] = match.group("value")
    return cfg_type(**config)  # type: ignore
