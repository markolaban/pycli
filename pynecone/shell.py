from abc import ABC, abstractmethod
from .command import Command

import argparse


class Shell(Command, ABC):

    def run(self):
        parser = argparse.ArgumentParser()
        self.add_positional_arguments(parser, self.get_commands())
        args = parser.parse_known_args()
        print(args[0])
        command = next(iter([c for c in self.get_commands() if c.name == args[0].command]), None)

        if command:
            command.execute(self.get_commands())
        else:
            print("{0} is not a valid command".format(args[0].command))





