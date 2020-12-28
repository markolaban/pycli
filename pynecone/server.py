import importlib
import pkgutil

from pynecone import ProtoCmd

from flask import Flask
app = Flask('pynecone')

class Server(ProtoCmd):

    def __init__(self):
        super().__init__('server',
                         'start server')

    def add_arguments(self, parser):
        pass #parser.add_argument('name', help="specifies the name of the component to be retrieved")

    def run(self, args):
        print('starting server')
        module = importlib.import_module('components')
        for pkg in [pkg_name for _, pkg_name, _ in pkgutil.iter_modules(['./components'])]:
            print('*** loading package {0}'.format(pkg))
            component = getattr(module, pkg.title())()
            print(type(component))
            component.get_blueprint()
            app.register_blueprint(component.get_blueprint(), url_prefix='/' + component.get_route_name())

        app.run()
