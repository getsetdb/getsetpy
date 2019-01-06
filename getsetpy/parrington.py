"""
filename : parrington.py

author : mentix02
datetime : 6/1/19 4:53 AM
"""

import re
import uuid

from .exceptions import ImproperPairSyntaxError, DatabaseError


class Parrington:
    """
    parser written for simple
    key value pair extraction
    from responses but is
    extended for more
    complex or simple types
    """

    def __init__(self, response: str = ''):

        self.response = ''
        self.response_dict = {}
        self.response_list = []

        self.set_response(response)

        self.response_type = str

    def set_response(self, response: str = ''):
        """
        inspired by C++'s fstream::open()
        function that doesn't force user to
        enter a filename during 'construction'
        or initialisation but lets them set
        the path later too
        """
        self.response = response

        # if there are new lines in
        # response provided meaning
        # that the type of command
        # was to list databases or
        # show the info like size
        # in bytes or something along
        # those lines
        if '\n' in self.response:
            # if there are multiple
            # lines in the response and
            # there's also a colon ":"
            # in it then the lines have
            # pairs in them so we
            # map these keys and values
            # as separate entities in
            # a Python dictionary object
            # else we simply return
            # a list of strings split
            # by a newline "\n" delimiter
            if ':' in self.response:

                self.response_dict = {}

                for line in self.response.splitlines():
                    key, value = Parrington.get_key(line), Parrington.get_value(line)
                    self.response_dict[key] = value

                self.response_type = dict

            else:

                self.response_list = response.splitlines()
                self.response_type = list

        elif ':' in self.response:

            self.response = response.split()

        else:

            self.response_type = str

    # ---- static methods ---- #

    @staticmethod
    def is_pair(pair: str) -> bool:
        """
        tries matching syntax
        of a pair using
        regular expressions
        """
        if re.match(r'([^\s]+)\s:\s.*[^$\n]', pair):
            return True
        return False

    @staticmethod
    def get_key(pair: str):

        if Parrington.is_pair(pair):
            key = pair.split()[0]
            return float(key) if str.isnumeric(key) else key
        else:
            raise ImproperPairSyntaxError(f'pair `{pair}` is not properly formatted')

    @staticmethod
    def get_value(pair: str):

        if Parrington.is_pair(pair):
            key = Parrington.get_key(pair)

            if key == 'error':
                # if type received is error
                # then raise a DatabaseError
                # for the value that is derived
                # by returning the string from
                # index 8 till end by measuring
                # len('error : ') which is
                # equal to eight (8)
                raise DatabaseError(pair[8:])

            # no data type validation
            # happens on the client code.
            # the data is trusted and
            # is assumed to be correct
            # and thus Parrington.py
            # relies entirely on GetSetDB
            # for data type inferring

            if key == 'list':
                return pair[2:].split()
            elif key == 'uuid':
                return uuid.UUID(' '.join(pair[2:]))
            elif key == 'number':
                return float(pair.split()[2])
            else:
                return ' '.join(pair.split()[2:])
        else:
            raise ImproperPairSyntaxError(f'pair `{pair}` is not properly formatted')
