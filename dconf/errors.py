"""dconf global error definitions"""


class ConfigurationException(Exception):
    """Base exception for invalid configurations"""


class InvalidConfigurationKey(ConfigurationException):
    """Exception for invalid configurations"""

    def __init__(self, key: str):
        super().__init__(f"invalid configuration key: {key}")


class UnknownConfigurationKey(ConfigurationException):
    """Exception for unknown configurations"""

    def __init__(self, key: str):
        super().__init__(f"unkown configuration: {key}")
