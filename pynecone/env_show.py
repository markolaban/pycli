from pynecone import Cmd


class EnvShow(Cmd):

        def __init__(self):
            super().__init__('show')

        def add_arguments(self, parser):
            parser.add_argument('op', choices=['get', 'set'],
                                help="get or set the active environment", default='get', const='get', nargs='?')
            parser.add_argument('--name', help="specifies the name of the environment to be set as active")

        def run(self, args):
            pass

        def get_help(self):
            return 'show environment values'