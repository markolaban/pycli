from abc import abstractmethod
from pynecone import Cmd
from .auth import Auth
from .cfg import Cfg

import os
import requests
from requests_toolbelt.utils import dump

from urllib.parse import urljoin

class REST(Cmd):

    def run(self, args):
        return self.execute(args, self)

    def get_token(self, force=False):
        authenticator = Auth(self.get_config().get_client_id(),
                             self.get_config().get_callback_url(),
                             self.get_config().get_auth_url(),
                             self.get_config().get_token_url(),
                             self.get_config().get_debug())

        client_key = self.get_config().get_client_key()
        client_secret = self.get_config().get_client_secret()
        client_cert = self.get_config().get_client_cert()
        client_cert_key = self.get_config().get_client_cert_key()

        if client_key is not None and client_secret is not None:
            token = authenticator.get_api_token(client_key, client_secret)
        elif client_cert is None or client_cert_key is None:
            token = authenticator.retrieve_token(force)

        return token

    @abstractmethod
    def execute(self, args, client):
        pass

    def get_endpoint_url(self, path):
        return urljoin(self.api_base_url, path)

    def get_arguments(self):
        arguments = {'headers': None, 'cookies': None,
            'auth': None, 'timeout': self.timeout, 'allow_redirects': True, 'proxies': None,
            'hooks': None, 'stream': None, 'verify': None, 'cert': None, 'json': None}

        if self.token is None:
            self.token = self.get_token()

        if self.token:
            arguments['headers'] = {"Authorization": "Bearer " + self.token}

        if self.ca_bundle is not None:
            arguments['verify'] = self.ca_bundle

        if self.client_cert is not None and self.client_cert_key is not None:
            arguments['cert'] = (self.client_cert, self.client_cert_key)

        return arguments

    def dump(self, response):
        data = dump.dump_all(response)
        print(data.decode('utf-8'))

    def get(self, path, params=None):

        resp = requests.get(self.get_endpoint_url(path),  params=params, **self.get_arguments())

        if self.debug:
            self.dump(resp)

        if resp.status_code == requests.codes.ok:
            if resp.headers.get('content-type').startswith('application/json'):
                return resp.json()
            else:
                return resp.content
        elif resp.status_code == 401:
            self.token = self.get_token(True)
            return self.get(path, params)
        else:
            if not self.debug:
                self.dump(resp)
            return None

    def post(self, path, params):

        resp = requests.post(self.get_endpoint_url(path), data=params, **self.get_arguments())

        if self.debug:
            self.dump(resp)

        if resp.status_code == requests.codes.ok:
            return resp.json()
        elif resp.status_code == 401:
            self.token = self.get_token(True)
            return self.post(path, params)
        else:
            if not self.debug:
                self.dump(resp)
            return None

    def put(self, path, params):

        resp = requests.put(self.get_endpoint_url(path), data=params, **self.get_arguments())

        if self.debug:
            self.dump(resp)

        if resp.status_code == requests.codes.ok:
            return resp.json()
        elif resp.status_code == 401:
            self.token = self.get_token(True)
            return self.put(path, params)
        else:
            print(resp.status_code, resp.text)
            if not self.debug:
                self.dump(resp)
            return None

    def put_file(self, path, file):

        resp = requests.put(self.get_endpoint_url(path), files=dict(file=file), **self.get_arguments())

        if self.debug:
            self.dump(resp)

        if resp.status_code == requests.codes.ok:
            return resp.status_code
        elif resp.status_code == 401:
            self.token = self.get_token(True)
            return self.put_file(path, file)
        else:
            print(resp.status_code, resp.text)
            if not self.debug:
                self.dump(resp)
            return None

    def delete(self, path, id):
        target = urljoin(path, id)

        resp = requests.delete(self.get_endpoint_url(target), **self.get_arguments())

        if self.debug:
            self.dump(resp)

        if resp.status_code == requests.codes.ok:
            return resp.json()
        elif resp.status_code == 401:
            self.token = self.get_token(True)
            return self.delete(path, id)
        else:
            if not self.debug:
                self.dump(resp)
            return None

