from .cmd import Cmd

import os
from pathlib import Path

from jinja2 import Environment, PackageLoader, select_autoescape
env = Environment(
    loader=PackageLoader('pynecone', 'templates'),
    autoescape=select_autoescape(['html', 'xml'])
)

class Gen(Cmd):

    def __init__(self):
        super().__init__("gen")

    def add_arguments(self, parser):
        parser.add_argument('op', choices=['cmd', 'shell'],
                            help="authenticate", default='cmd', const='cmd', nargs='?')
        parser.add_argument('names', help="command names", nargs='+')
        parser.add_argument('--output_folder', help="use the specified output folder", default=os.path.join(os.getcwd(), 'commands'))

    def run(self, args):
        if args.op == 'shell':
            shell_name = args.names[0]
            cmd_names = args.names[1:]
            shell_template = env.get_template('shell.jinja')
            cmd_template = env.get_template('cmd.jinja')

            Path(args.output_folder).mkdir(parents=True, exist_ok=True)

            with open(os.path.join(args.output_folder, shell_name.lower() + '.py'), "w") as fh:
                fh.write(shell_template.render(class_name=shell_name.title(), name=shell_name.lower(), names=[cmd.lower() for cmd in cmd_names]))

            for cmd_name in cmd_names:
                with open(os.path.join(args.output_folder, cmd_name.lower() + '.py'), "w") as fh:
                    fh.write(cmd_template.render(class_name=cmd_name.title(), name=cmd_name.lower()))
        else:
            Path(args.output_folder).mkdir(parents=True, exist_ok=True)

            cmd_template = env.get_template('cmd.jinja')

            cmd_names = args.names

            for cmd_name in cmd_names:
                with open(os.path.join(args.output_folder, cmd_name.lower() + '.py'), "w") as fh:
                    fh.write(cmd_template.render(class_name=cmd_name.title(), name=cmd_name.lower()))

    def get_help(self):
        return 'generate a new command'