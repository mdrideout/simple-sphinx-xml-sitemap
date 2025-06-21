Usage
=====

Run the example package to print the message::

   python -m hello_world

You can also use the :class:`hello_world.HelloWorld` class in your own code::

   from hello_world import HelloWorld

   hello = HelloWorld()
   hello.say_hello()

   hello.say_hello("Alice")

The :mod:`hello_world.helpers` module provides additional functions::

   from hello_world.helpers import greet

   print(greet("Alice"))
