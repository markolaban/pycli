from abc import abstractmethod
from .client import Client


class Cmd(Client):

    def __init__(self, name):
        self.name = name

    def get_client(self):
        return self

    @abstractmethod
    def add_arguments(self, parser):
        pass

    @abstractmethod
    def get_help(self):
        return None

    def setup(self, subparsers):
        parser = subparsers.add_parser(self.name, help=self.get_help())
        self.add_arguments(parser)
        return parser

    def repl(self):
        ui = input('[{0}]'.format(self.name))
        self.run(ui)
        self.repl()
