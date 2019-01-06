"""
filename : exceptions.py

author : manan
datetime : 6/1/19 2:33 PM
"""


class DatabaseNotFoundError(Exception):
    pass


class DatabaseError(Exception):
    pass


class KeyNotFoundError(Exception):
    pass


class ResponseTypeError(Exception):
    pass


class ImproperPairSyntaxError(Exception):
    pass
