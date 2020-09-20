from .cmd import Cmd
from .auth import Auth, AuthMode
from .config import Config

import requests

from requests_toolbelt.utils import dump

from urllib.parse import urljoin

class Rest_Put(Cmd):

        def __init__(self):
            super().__init__('put')

        def add_arguments(self, parser):
            parser.add_argument('op', choices=['one', 'two'],
                                help="a choice between one and two", default='two', const='two', nargs='?')
            parser.add_argument('--name', help="specifies the name", default="somename")

        def run(self, args):
            pass

        def get_help(self):
            return 'help'

        def get_endpoint_url(self, path):
            return urljoin(self.get_config().get_api(self.name)['url'], path)

        def dump(self, response):
            data = dump.dump_all(response)
            print(data.decode('utf-8'))

        def put(self, path, params):

            resp = requests.put(self.get_endpoint_url(path), data=params, **self.get_arguments())

            if self.get_config().get_debug():
                self.dump(resp)

            if resp.status_code == requests.codes.ok:
                return resp.json()
            elif resp.status_code == 401:
                auth = Auth(self.get_config())
                mode = auth.get_mode()
                if mode == AuthMode.AUTH_URL:
                    auth.login()
                    return self.put(path, params)
                else:
                    print('Unauthorized')
            else:
                print(resp.status_code, resp.text)
                if not self.get_config().get_debug():
                    self.dump(resp)
                return None

        def put_file(self, path, file):

            resp = requests.put(self.get_endpoint_url(path), files=dict(file=file), **self.get_arguments())

            if self.get_config().get_debug():
                self.dump(resp)

            if resp.status_code == requests.codes.ok:
                return resp.status_code
            elif resp.status_code == 401:
                auth = Auth(self.get_config())
                mode = auth.get_mode()
                if mode == AuthMode.AUTH_URL:
                    auth.login()
                    return self.put_file(path, file)
                else:
                    print('Unauthorized')
            else:
                print(resp.status_code, resp.text)
                if not self.get_config().get_debug():
                    self.dump(resp)
                return None

        @classmethod
        def api(cls, name=None):
            auth = Config.get_api(name)['auth']
            pass