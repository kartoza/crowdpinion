# Stubs for werkzeug.contrib.iterio (Python 2)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

greenlet = ...  # type: Any

class IterIO:
    def __new__(cls, obj, sentinel=''): ...
    def __iter__(self): ...
    def tell(self): ...
    def isatty(self): ...
    def seek(self, pos, mode=0): ...
    def truncate(self, size=None): ...
    def write(self, s): ...
    def writelines(self, list): ...
    def read(self, n=-1): ...
    def readlines(self, sizehint=0): ...
    def readline(self, length=None): ...
    def flush(self): ...
    def __next__(self): ...

class IterI(IterIO):
    def __new__(cls, func, sentinel=''): ...
    closed = ...  # type: Any
    def close(self): ...
    def write(self, s): ...
    def writelines(self, list): ...
    def flush(self): ...

class IterO(IterIO):
    sentinel = ...  # type: Any
    closed = ...  # type: Any
    pos = ...  # type: Any
    def __new__(cls, gen, sentinel=''): ...
    def __iter__(self): ...
    def close(self): ...
    def seek(self, pos, mode=0): ...
    def read(self, n=-1): ...
    def readline(self, length=None): ...
    def readlines(self, sizehint=0): ...
