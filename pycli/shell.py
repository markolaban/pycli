from abc import ABC, abstractmethod
import argparse


class Shell(ABC):

    def run(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("command")
        parser.add_argument("--verbose", help="increase output verbosity",
                            action="store_true")
        args = parser.parse_args()
        command = self.get_command(args.command)

        if command:
            command.run(args)
        else:
            print("{0} is not a valid command".format(args.command))
            print(self.get_usage())

    @abstractmethod
    def get_command(self, name):
        return None

    @abstractmethod
    def get_usage(selfe):
        return "This is usage info..."