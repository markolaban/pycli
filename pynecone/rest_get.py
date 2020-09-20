
from .cmd import Cmd
from .auth import Auth, AuthMode
from .config import Config

import requests
from requests_toolbelt.utils import dump

from urllib.parse import urljoin

class Rest_Get(Cmd):

        def __init__(self):
            super().__init__('get')
            self.cfg = Config.init()

        def add_arguments(self, parser):
            parser.add_argument('api', help="specifies the api to use")
            parser.add_argument('path', help="specifies the path")
            parser.add_argument('params', help="list of key:value pairs", nargs='+')

        def run(self, args):
            print(self.get(args.api, args.path, dict([kv.split(':') for kv in args.params])))

        def get_help(self):
            return 'help'

        def get_endpoint_url(self, api, path):
            return urljoin(self.get_config().get_api(self.name)['url'], path)

        def dump(self, response):
            data = dump.dump_all(response)
            print(data.decode('utf-8'))

        def get(self, api, path, params=None):

            resp = requests.get(self.get_endpoint_url(api, path), params=params, **self.get_arguments())

            if self.get_config().get_debug():
                self.dump(resp)

            if resp.status_code == requests.codes.ok:
                if resp.headers.get('content-type').startswith('application/json'):
                    return resp.json()
                else:
                    return resp.content
            elif resp.status_code == 401:
                auth = Auth(self.get_config())
                mode = auth.get_mode()
                if mode == AuthMode.AUTH_URL:
                    auth.login()
                    return self.get(path, params)
                else:
                    print('Unauthorized')
            else:
                if not self.get_config().get_debug():
                    self.dump(resp)
                return None

