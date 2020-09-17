from .cmd import Cmd
from jinja2 import Environment, PackageLoader, select_autoescape
env = Environment(
    loader=PackageLoader('pynecone', 'templates'),
    autoescape=select_autoescape(['html', 'xml'])
)

class Gen(Cmd):

    def __init__(self):
        super().__init__("gen")

    def add_arguments(self, parser):
        parser.add_argument('op', choices=['cmd'],
                            help="authenticate", default='cmd', const='cmd', nargs='?')

    def run(self, args):
        template = env.get_template('cmd.jinja')
        print(template.render(class_name='TestName', go='testname'))

    def get_help(self):
        return 'generate a new command'