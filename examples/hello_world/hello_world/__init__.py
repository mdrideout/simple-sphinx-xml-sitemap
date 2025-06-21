"""Simple hello world package providing a small library.

The package exposes :class:`.HelloWorld` and a :func:`.main` helper used
throughout the documentation.
"""

from .hello import HelloWorld, main

__all__ = ["HelloWorld", "main"]
