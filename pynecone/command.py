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
    def get_help(self):
        return None

    def execute(self, parser):
        parser = argparse.ArgumentParser()
        # self.add_positional_arguments(parser, commands)
        self.add_arguments(parser)
        args = parser.parse_known_args()
        print('*** name is: ', self.name)
        print('*** args are: ', args)
        self.run(args[0])
