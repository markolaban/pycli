from .cmd import Cmd


class Gen(Cmd):

    def __init__(self):
        super().__init__("gen")

    def add_arguments(self, parser):
        parser.add_argument('op', choices=['cmd'],
                            help="authenticate", default='cmd', const='cmd', nargs='?')

    def run(self, args):
        pass

    def get_help(self):
        return 'generate a new command'