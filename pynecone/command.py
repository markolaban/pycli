from abc import ABC, abstractmethod
import argparse


class Command(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def add_arguments(self, parser):
        pass

    @abstractmethod
    def run(self, args):
        pass

    @abstractmethod
    def get_commands(self):
        return []

    def add_positional_arguments(self, parser, commands):
        parser.add_argument("command", help="select one of the different commands ",
                            choices=[c.name for c in commands])
        parser.add_argument("subcommand", nargs='?', help="specify a subcommand")

    def execute(self, commands):
        parser = argparse.ArgumentParser()
        self.add_positional_arguments(parser, commands)
        self.add_arguments(parser)
        args = parser.parse_known_args()
        self.run(args[0])
