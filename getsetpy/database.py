"""
filename : database.py

author : mentix02
datetime : 6/1/19 2:27 PM
"""

from socket import *
from .constants import PORT
from .parrington import Parrington
from .exceptions import DatabaseNotFoundError


class Database:

    def __init__(self, database_name: str):

        self.parser = Parrington()
        self.database_name = database_name
        self.sock = socket(AF_INET, SOCK_STREAM)

        try:
            self._connect()
        except ConnectionRefusedError:
            print('connection to getsetdb failed')
            print(f'are you sure it\'s running on port {PORT}')
            quit(1)

        if not self.exists():
            self.sock.close()
            raise DatabaseNotFoundError(f'database {database_name} does not exist')

    def __del__(self):
        """
        destructor that simply
        closes the socket connection
        to the database
        """
        self.sock.close()

    def _connect(self):
        """
        connect to getsetdb
        on the tcp port 4998
        """
        self.sock.connect(('', PORT))

    def response(self, command: str) -> str:
        """
        perhaps the most used
        functions that can be
        used externally too if
        the user decides to parse
        responses in their own way
        """

        self.sock.send(f'{self.database_name} {command}\n'.encode())
        return self.sock.recv(4096).decode()

    # ---- database commands ---- #

    def get(self, key: str):
        response = self.response(f'get {key}')
        return self.parser.get_value(response)

    def set(self, key: str, value: str):
        response = self.response(f'set {key} {value}')
        return self.parser.get_value(response)

    def delete(self, key: str):
        response = self.response(f'del {key}')
        return self.parser.get_value(response)

    def all(self) -> dict:
        response = self.response(f'all')
        self.parser.set_response(response)

        return self.parser.response_dict

    def info(self) -> dict:
        response = self.response(f'info')
        self.parser.set_response(response)

        return self.parser.response_dict

    def count(self):
        response = self.response(f'count')
        return self.parser.get_value(response)

    def exists(self) -> bool:
        """
        implements a simple
        existence check for
        the provided database.
        it should always run
        during initialisation
        """
        exists = self.response('exists')
        return self.parser.get_value(exists) == 'true'
