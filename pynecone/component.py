import os
from pathlib import Path

from pynecone import ProtoShell, ProtoCmd

from flask import Blueprint, jsonify

from jinja2 import Environment, PackageLoader, select_autoescape
env = Environment(
    loader=PackageLoader('pynecone', 'templates'),
    autoescape=select_autoescape(['html', 'xml'])
)

blueprint = Blueprint('component', __name__)

class Component(ProtoShell):

    class Create(ProtoShell):

        def __init__(self):
            super().__init__('create', [], 'create a component')

        def gen_component(self, name="NewComponent", children=[], output_folder='./components'):

            template = env.get_template('component.jinja')

            Path(output_folder).mkdir(parents=True, exist_ok=True)

            path = os.path.join(output_folder, name.lower() + '.py')

            if not os.path.exists(path):
                with open(path, "w") as fh:
                    fh.write(template.render(class_name=name.title(), name=name.lower(),
                                             names=[child.lower() for child in children]))
            else:
                print('Child already exists at path {0} skipping'.format(path))

        def add_arguments(self, parser):
            parser.add_argument('name', help="specifies the name of the component to be created", default='NewComponent')
            parser.add_argument('children', help="child component names", nargs='*')

        def run(self, args):
            self.gen_component(args.name)

            if args.children:
                self.gen_component(args.children[0], args.children[1:])

    class List(ProtoCmd):

        def __init__(self):
            super().__init__('list',
                             'lists components')

    class Delete(ProtoCmd):

        def __init__(self):
            super().__init__('delete',
                             'delete a component')

        def add_arguments(self, parser):
            parser.add_argument('name', help="specifies the name of the component to be deleted")

    class Get(ProtoCmd):

        def __init__(self):
            super().__init__('get',
                             'get a component')

        def add_arguments(self, parser):
            parser.add_argument('name', help="specifies the name of the component to be retrieved")

    def __init__(self,  name):
        super().__init__(name, [Component.Create(), Component.List(), Component.Delete(), Component.Get()], name)

    def get_blueprint(self):
        print('&&& get blueprint {}'.format(self.name))
        return blueprint

    def get_route_name(self):
        return self.name
