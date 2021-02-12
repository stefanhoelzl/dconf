"""dconf global error definitions"""


class InvalidConfiguration(Exception):
    """Exception for invalid configurations"""

    def __init__(self, key: str, value: str):
        super().__init__(f"invalid configuration: {key}={value}")


class UnknownConfiguration(Exception):
    """Exception for unknown configurations"""

    def __init__(self, key: str):
        super().__init__(f"unkown configuration: {key}")
