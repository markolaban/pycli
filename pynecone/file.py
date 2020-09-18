from pynecone import Cmd


class File(Cmd):

        def __init__(self):
            super().__init__('file')

        def add_arguments(self, parser):
            parser.add_argument('op', choices=['upload', 'download'],
                                help="a choice between one and two", default='two', const='two', nargs='?')
            parser.add_argument('--name', help="specifies the name", default="somename")
            parser.add_argument('--path', help="specifies the name", default="somename")
            parser.add_argument('--std', help="specifies the name", default="somename")

        def run(self, args):
            pass

        def get_help(self):
            return 'access files'