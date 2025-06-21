
"""Simple hello world package providing a small library."""


class HelloWorld:
    """Utility class to print a hello world message."""

    @staticmethod
    def say_hello() -> None:
        """Print ``"Hello, world!"`` to standard output."""
        print("Hello, world!")


def main() -> None:
    """Demonstrate the :class:`HelloWorld` API by printing the message."""
    HelloWorld.say_hello()

if __name__ == "__main__":
    main()
