"""configuration builder"""
import re
from dataclasses import fields
from typing import Dict, Type, TypeVar

from .errors import InvalidConfiguration, UnknownConfiguration

ConfigType = TypeVar("ConfigType")


class DataclassBuilder:
    """builder for dataclass configurations"""

    def __init__(self, config_type: Type[ConfigType]):
        super().__init__()
        self._config_type = config_type
        self._values: Dict[str, str] = dict()

    def set(self, key: str, value: str) -> None:
        """Sets a value used to build the config instance"""
        if not re.match(r"^(?P<key>[A-z]\w*)$", key):
            raise InvalidConfiguration(key, value)
        if key not in [field.name for field in fields(self._config_type)]:
            raise UnknownConfiguration(key)
        self._values[key] = value

    def build(self) -> ConfigType:
        """Builds a config instance"""
        return self._config_type(**self._values)  # type: ignore
