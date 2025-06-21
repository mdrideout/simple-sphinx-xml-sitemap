"""Simple hello world package."""

def say_hello() -> str:
    """Return a hello world message."""
    return "Hello, world!"


def main() -> None:
    """Print the hello message."""
    print(say_hello())

if __name__ == "__main__":
    main()
