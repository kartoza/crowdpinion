# encoding: utf-8
# module psycopg2._psycopg
# from /usr/local/lib/python3.7/site-packages/psycopg2/_psycopg.cpython-37m-x86_64-linux-gnu.so
# by generator 1.145
""" psycopg PostgreSQL driver """

# imports
import psycopg2 as __psycopg2
import psycopg2.extensions as __psycopg2_extensions


class DataError(__psycopg2.DatabaseError):
    """ Error related to problems with the processed data. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


