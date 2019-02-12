# encoding: utf-8
# module psycopg2._psycopg
# from /usr/local/lib/python3.7/site-packages/psycopg2/_psycopg.cpython-37m-x86_64-linux-gnu.so
# by generator 1.145
""" psycopg PostgreSQL driver """

# imports
import psycopg2 as __psycopg2
import psycopg2.extensions as __psycopg2_extensions


from .tuple import tuple

class Column(tuple):
    """ Column(name, type_code, display_size, internal_size, precision, scale, null_ok) """
    def _asdict(self): # reliably restored by inspect
        """ Return a new OrderedDict which maps field names to their values. """
        pass

    @classmethod
    def _make(cls, *args, **kwargs): # real signature unknown
        """ Make a new Column object from a sequence or iterable """
        pass

    def _replace(_self, **kwds): # reliably restored by inspect
        """ Return a new Column object replacing specified fields with new values """
        pass

    def __getnewargs__(self): # reliably restored by inspect
        """ Return self as a plain tuple.  Used by copy and pickle. """
        pass

    def __init__(self, name, type_code, display_size, internal_size, precision, scale, null_ok): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(_cls, name, type_code, display_size, internal_size, precision, scale, null_ok): # reliably restored by inspect
        """ Create new instance of Column(name, type_code, display_size, internal_size, precision, scale, null_ok) """
        pass

    def __repr__(self): # reliably restored by inspect
        """ Return a nicely formatted representation string """
        pass

    display_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Alias for field number 2"""

    internal_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Alias for field number 3"""

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Alias for field number 0"""

    null_ok = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Alias for field number 6"""

    precision = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Alias for field number 4"""

    scale = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Alias for field number 5"""

    type_code = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Alias for field number 1"""


    _fields = (
        'name',
        'type_code',
        'display_size',
        'internal_size',
        'precision',
        'scale',
        'null_ok',
    )
    _fields_defaults = {}
    __slots__ = ()


