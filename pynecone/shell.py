from abc import abstractmethod
from .cmd import Cmd

import argparse


class Shell(Cmd):

    def run(self, args=None):
        if args is None:
            parser = argparse.ArgumentParser(prog=self.name)
            self.add_arguments(parser)

            subparsers = parser.add_subparsers(dest='command', help=self.get_help())

            for c in self.get_commands():
                c.setup(subparsers)
            args = parser.parse_args()

        # print(args)

        if getattr(args,'command'):
            command = next(iter([c for c in self.get_commands() if c.name == getattr(args, 'command')]), None)
            if command:
                if hasattr(args, 'subcommand'):
                    subcommand = next(iter([c for c in command.get_commands() if c.name == getattr(args, 'subcommand')]), None)
                    if subcommand:
                        return subcommand.run(args)
                    else:
                        print(args)
                        print('command: ', command.name)
                        print('subcommands: ', [c.name for c in command.get_commands()])
                        print("{0} is not a valid subcommand".format(args.subcommand))
                else:
                    return command.run(args)
            else:
                print("{0} is not a valid command".format(args.command))


    @abstractmethod
    def get_commands(self):
        return []

    def setup(self, subparsers):
        # print('*** running command setup for {0}'.format(self.name))
        parser = super().setup(subparsers)
        commands = self.get_commands()
        if commands:
            subsubparsers = parser.add_subparsers(dest='subcommand')
            for c in commands:
                # print('*** running subcommand setup for {0}'.format(c.name))
                c.setup(subsubparsers)

    def __call__(self, args):

        parser = argparse.ArgumentParser(prog=self.name)

        self.add_arguments(parser)
        subparsers = parser.add_subparsers(dest='command', help=self.get_help())

        for c in self.get_commands():
            c.setup(subparsers)

        return self.run(parser.parse_args(args))
