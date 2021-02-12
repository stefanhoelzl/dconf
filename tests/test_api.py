# pylint: disable=missing-module-docstring,missing-function-docstring,missing-class-docstring

import dconf
from tests.testlib import arguments, make_config


def test_initialize_config() -> None:
    config_type = make_config(key=str)
    with arguments("key=value"):
        config = dconf.initialize(config_type)
    assert config.key == "value"
