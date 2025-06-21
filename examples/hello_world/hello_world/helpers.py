"""Additional helper utilities for greeting people.

The module contains a small API consisting of a function and a dataclass
that showcase Sphinx-style docstrings.
"""

from dataclasses import dataclass


def greet(name: str) -> str:
    """Return a personalized greeting message.

    :param name: Name of the person to greet.
    :type name: str
    :return: A greeting containing ``name``.
    :rtype: str
    """

    return f"Hello, {name}!"


@dataclass
class Greeter:
    """Class for creating greeter objects.

    :param default_name: Fallback when ``name`` is not provided.
    :type default_name: str
    :param prefix: Text used before the name in greetings.
    :type prefix: str
    """

    default_name: str = "world"
    prefix: str = "Hello"

    def greet(self, name: str | None = None, times: int = 1) -> str:
        """Return a greeting.

        :param name: Optional name to greet. If omitted, ``default_name`` is used.
        :type name: str | None
        :param times: Number of times to repeat the greeting.
        :type times: int
        :return: The greeting repeated ``times`` times.
        :rtype: str
        """

        target = name or self.default_name
        message = f"{self.prefix}, {target}!"
        return " ".join([message] * times)
