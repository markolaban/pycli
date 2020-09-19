from pynecone import Cmd


class EnvActive(Cmd):

        def __init__(self):
            super().__init__('active')

        def add_arguments(self, parser):
            parser.add_argument('op', choices=['get', 'set'],
                                help="a choice between one and two", default='two', const='two', nargs='?')
            parser.add_argument('--name', help="specifies the name", default="somename")

        def run(self, args):
            pass

        def get_help(self):
            return 'manage active environment'