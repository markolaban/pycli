from pynecone import Cmd
from .config import Config

class ApiUrl(Cmd):

        def __init__(self):
            super().__init__('url')

        def add_arguments(self, parser):
            parser.add_argument('op', choices=['get', 'set'],
                                help="gets or sets the api", default='get', const='get', nargs='?')
            parser.add_argument('name', help="specifies the api name")
            parser.add_argument('url', help="specifies the api url")

        def run(self, args):
            if args.op == 'set':
                res = Config.init().modify_api_url(args.name, args.url)
                if res:
                    return res
                else:
                    print('Unable to modify url parameter for API {0}'.format(args.name))
            else:
                return Config.init().get_api(args.name)['url']

        def get_help(self):
            return 'manage api url'