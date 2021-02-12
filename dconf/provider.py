"""configuration provider"""
import sys
from typing import Generator, List, Optional, Tuple


class Provider:
    """Base class for all configuration provider"""

    def items(self) -> Generator[Tuple[str, str], None, None]:
        """yield a key value pair for each argument"""
        raise NotImplementedError()  # pragma: no cover


class ArgumentProvider(Provider):
    """Provider based on command line arguments"""

    def __init__(
        self,
        arguments: Optional[List[str]] = None,  # pylint: disable=unsubscriptable-object
    ):
        super().__init__()
        self.arguments = sys.argv[1:] if arguments is None else arguments

    def items(self) -> Generator[Tuple[str, str], None, None]:
        """yield a key value pair for each argument"""
        for arg in self.arguments:
            splitted = arg.split("=")
            yield splitted.pop(0), "" if not splitted else splitted.pop(0)
