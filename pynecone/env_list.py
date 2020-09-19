from pynecone import Cmd


class EnvList(Cmd):

        def __init__(self):
            super().__init__('list')

        def add_arguments(self, parser):
            pass

        def run(self, args):
            pass

        def get_help(self):
            return 'list available environments'