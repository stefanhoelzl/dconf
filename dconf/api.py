"""dconf core"""
from typing import Type, TypeVar

from .builder import DataclassBuilder
from .provider import ArgumentProvider

ConfigType = TypeVar("ConfigType")


def initialize(
    config_type: Type[ConfigType],
) -> ConfigType:
    """Initialize configuration"""
    builder = DataclassBuilder(config_type)
    for key, value in ArgumentProvider().items():
        builder.set(key, value)
    return builder.build()
