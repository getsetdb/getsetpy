"""
filename : space.py

author : manan
datetime : 6/1/19 6:28 PM
"""

from socket import *
from .constants import PORT
from .parrington import Parrington


class Space:
    """
    space inter-actor class for
    GetSetDB that sends commands
    directly to the 'space' for
    CRUD functions over databases
    """

    def __init__(self):

        self.parser = Parrington()
        self.sock = socket(AF_INET, SOCK_STREAM)

        try:
            self._connect()
        except ConnectionRefusedError:
            print('connection to getsetdb failed')
            print(f'are you sure it\'s running on port {PORT}')
            quit(1)

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

        self.sock.send(f'{command}\n'.encode())
        return self.sock.recv(4096).decode()

    # ---- space commands ---- #

    def new(self, database_names: str) -> list:
        """
        creates new databases
        and returns a list
        of names of them
        """
        response = self.response(f'new {database_names}')
        value = self.parser.get_value(response)

        value = value.replace('`', '')
        value = value.replace(' ', '')
        return value.split(',')

    def delete(self, database_names: str) -> list:
        """
        same as "self.new"
        just reversed creation
        and implements deletion
        """
        response = self.response(f'del {database_names}')
        value = self.parser.get_value(response)

        value = value.replace('`', '')
        value = value.replace(' ', '')
        return value.split(',')

    def ls(self) -> dict:
        """
        returns a list of
        databases available
        on GetSetDB as a
        dictionary
        """
        response = self.response(f'list')
        self.parser.set_response(response)

        return self.parser.response_dict

    def rename(self, old_database_name: str, new_database_name: str) -> str:
        """
        renames old database
        to new one and returns
        name of new database
        """
        response = self.response(f'rename {old_database_name} {new_database_name}')
        return self.parser.get_value(response)

    def commands(self) -> list:
        """
        returns a list of
        all available commands
        """
        response = self.response('commands')
        self.parser.set_response(response)

        return self.parser.response_list

    def version(self) -> float:
        response = self.response('version')
        return float(response)

    def datetime(self):
        return self.response('datetime')[:-1]
