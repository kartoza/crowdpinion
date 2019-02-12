# Stubs for Crypto.Random.random (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

class StrongRandom:
    def __init__(self, rng: Optional[Any] = ..., randfunc: Optional[Any] = ...) -> None: ...
    def getrandbits(self, k): ...
    def randrange(self, *args): ...
    def randint(self, a, b): ...
    def choice(self, seq): ...
    def shuffle(self, x): ...
    def sample(self, population, k): ...

getrandbits = ...  # type: Any
randrange = ...  # type: Any
randint = ...  # type: Any
choice = ...  # type: Any
shuffle = ...  # type: Any
sample = ...  # type: Any
