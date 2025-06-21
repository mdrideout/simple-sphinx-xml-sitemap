"""Utilities for printing greeting messages.

The module exposes :class:`HelloWorld`, which shows how to write
Sphinx-style docstrings. It also provides a ``main`` entry point that
invokes the class.
"""

class HelloWorld:
    """Print configurable greeting messages.

    :param default_name: Name used when no ``name`` is provided.
    :type default_name: str
    """

    def __init__(self, default_name: str = "world") -> None:
        self.default_name = default_name

    def build_message(self, name: str | None = None) -> str:
        """Create a greeting message.

        :param name: Person to greet. Defaults to ``default_name``.
        :type name: str | None
        :return: The formatted greeting.
        :rtype: str
        """

        target = name or self.default_name
        return f"Hello, {target}!"

    def say_hello(self, name: str | None = None) -> None:
        """Print a greeting message.

        :param name: Optional name to greet.
        :type name: str | None
        :returns: ``None``
        :rtype: None
        """

        print(self.build_message(name))


def main() -> None:
    """Run a short demonstration of :class:`HelloWorld`.

    :returns: ``None``
    :rtype: None
    """

    HelloWorld().say_hello()

if __name__ == "__main__":
    main()
