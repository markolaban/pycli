import requests
from requests_toolbelt.utils import dump
import keyring
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs
from webbrowser import open_new
import os
from .cmd import Cmd

import dotenv
found_dotenv = dotenv.find_dotenv(usecwd=True)
print("using .env: ", found_dotenv)
if found_dotenv:
    dotenv.load_dotenv(found_dotenv)

class HTTPServerHandler(BaseHTTPRequestHandler):

    def __init__(self, request, address, server):
        super().__init__(request, address, server)

    def do_GET(self):
        if self.path.startswith('/auth?access_token='):
            self.server.access_token = parse_qs(self.path[6:])["access_token"][0]
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(bytes(
                "<html><head></head><h1>You may now close this window."
                + "</h1></html>", "utf-8"))
        elif self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(bytes("<html><head><script>window.location.href = '/auth?access_token=' + window.location.href.split('#')[1].split('&').filter(function(c) { return c.startsWith('access_token=')})[0].substring(13);</script></head><h1>You may now close this window."
                               + "</h1></html>", "utf-8"))
        return


class Auth(Cmd):

    def __init__(self,
                 client_id=os.getenv('CLIENT_ID'),
                 callback_url=os.getenv('CALLBACK_URL', 'http://localhost:8080'),
                 auth_url=os.getenv('AUTH_URL'),
                 token_url=os.getenv('TOKEN_URL'), debug=bool(os.getenv('DEBUG', False))):

        super().__init__("auth")
        self.client_id = client_id
        self.callback_url = callback_url
        self.auth_url = auth_url
        self.token_url = token_url
        self.debug = debug

    def login(self):
        httpServer = HTTPServer(('localhost', 8080),
                                lambda req, address, server: HTTPServerHandler(req, address, server))

        open_new(self.auth_url + '?client_id=' + self.client_id + '&redirect_uri=' + self.callback_url + '&response_type=token')

        httpServer.handle_request()
        httpServer.handle_request()

        self.store_token(httpServer.access_token)

        return httpServer.access_token

    def logout(self):
        self.store_token(None)

    def store_token(self, token):
        if token:
            last_index = 0
            for chunk in self.chunks(token, 256):
                keyring.set_password(self.client_id, "access_token_{0}".format(chunk[0]), chunk[1])
                last_index = chunk[0]
            keyring.set_password(self.client_id, "access_token_count", str(last_index))
        else:
            count = keyring.get_password(self.client_id, "access_token_count")
            if count:
                for index in range(0, int(count) + 1):
                    keyring.delete_password(self.client_id, "access_token_{0}".format(index))
            keyring.delete_password(self.client_id, "access_token_count")

    def retrieve_token(self, force=False):
        if force:
            access_token = self.login()
        else:
            count = keyring.get_password(self.client_id, "access_token_count")
            access_token = ''
            if count:
                for index in range(0, int(count) + 1):
                    access_token += keyring.get_password(self.client_id, "access_token_{0}".format(index))
            else:
                access_token = self.login()
        return access_token

    @classmethod
    def chunks(cls, s, n):
        for index, start in enumerate(range(0, len(s), n)):
            yield (index, s[start:start + n])

    def get_api_token(self, key, secret):
        print(key, secret)

        resp = requests.post(self.token_url, data={'response_type': 'token',
                                        'grant_type': 'password',
                                        'username': key,
                                        'password': secret,
                                        'client_id': self.client_id,
                                        'redirect_uri': self.callback_url}, verify=False)

        if self.debug:
            data = dump.dump_all(resp)
            print(data.decode('utf-8'))

        return resp.json()['access_token']

    def add_arguments(self, parser):
        parser.add_argument('op', choices=['login', 'logout', 'status'],
                            help="authenticate", default='status', const='status', nargs='?')

    def run(self, args):
        if args.op == 'login':
            self.login()
        elif args.op == 'logout':
            self.logout()
        else:
            print('Authenticated: {0}'.format(self.retrieve_token() is not None))

    def get_help(self):
        pass

