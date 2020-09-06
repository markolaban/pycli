from abc import ABC, abstractmethod
from .command import Command

import argparse


class Shell(Command, ABC):

    def run(self):
        parser = argparse.ArgumentParser(prog=self.name)
        self.add_arguments(parser)
        subparsers = parser.add_subparsers(help=self.get_help())
        for c in self.get_commands():
            c.setup(subparsers)
        # self.add_positional_arguments(parser, self.get_commands())
        args = parser.parse_args()
        print(args)

        return
        # parser.parse_args()

        command = next(iter([c for c in self.get_commands() if c.name == args[0].command]), None)

        if command:
            command.execute(self.get_commands())
        else:
            print("{0} is not a valid command".format(args[0].command))

    @abstractmethod
    def get_commands(self):
        return []

    def add_positional_arguments(self, parser, commands):
        parser.add_argument("command", help="select one of the different commands ",
                            choices=[c.name for c in commands])





