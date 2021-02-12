# pylint: disable=missing-module-docstring,missing-function-docstring,missing-class-docstring,no-self-use
import dconf
from tests.testlib import arguments


class TestArgumentProvider:
    def test_items_from_sys_argv(self) -> None:
        with arguments("key=value"):
            provider = dconf.provider.ArgumentProvider()
            assert dict(provider.items()) == dict(key="value")

    def test_items_from_init(self) -> None:
        provider = dconf.provider.ArgumentProvider(arguments=["key=value"])
        assert dict(provider.items()) == dict(key="value")

    def test_item_without_value(self) -> None:
        provider = dconf.provider.ArgumentProvider(arguments=["key"])
        assert dict(provider.items()) == dict(key="")

    def test_empty_arguments(self) -> None:
        with arguments("key"):
            provider = dconf.provider.ArgumentProvider(arguments=[])
        assert dict(provider.items()) == dict()
