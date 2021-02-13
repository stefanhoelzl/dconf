# pylint: disable=missing-module-docstring,missing-function-docstring,missing-class-docstring,no-self-use
import pytest

import dconf
from dconf.builder import DataclassBuilder
from tests.testlib import make_config


class TestDataclassBuilder:
    def test_set_value(self) -> None:
        builder = DataclassBuilder(make_config(key=str))
        builder.set("key", "value")
        assert builder.build().key == "value"  # type: ignore

    def test_build_dataclass(self) -> None:
        config_type = make_config()
        assert config_type() == DataclassBuilder(config_type).build()

    def test_unkown_key(self) -> None:
        builder = DataclassBuilder(make_config())
        with pytest.raises(dconf.errors.UnknownConfigurationKey):
            builder.set("unkown_key", "value")

    @pytest.mark.parametrize(
        "key",
        [
            "invalid-key",
            "öö",
            "invalid.key",
        ],
    )
    def test_invalid_keys(self, key: str) -> None:
        builder = DataclassBuilder(make_config())
        with pytest.raises(dconf.errors.InvalidConfigurationKey):
            builder.set(key, "value")
