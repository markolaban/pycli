class Cfg:

    def __init__(self,
                 api_base_url,
                 auth_url,
                 callback_url,
                 client_id,
                 client_key,
                 client_secret,
                 token_url,
                 debug=False,
                 client_cert=None,
                 client_cert_key=None,
                 ca_bundle=None,
                 timeout=10):

        '''
        os.getenv('REALNET_API_BASE_URL', 'https://api.realnet.io/v1/'),
                      os.getenv('REALNET_AUTH_URL', 'https://auth.realnet.io/auth/realms/realnet/protocol/openid-connect/auth'),
                      os.getenv('REALNET_CALLBACK_URL', 'http://localhost:8080'),
                      os.getenv('REALNET_CLIENT_ID', 'realnet'),
                      os.getenv('REALNET_CLIENT_KEY'),
                      os.getenv('REALNET_CLIENT_SECRET'),
                      os.getenv('REALNET_TOKEN_URL', 'https://auth.realnet.io/auth/realms/realnet/protocol/openid-connect/token'),
                      bool(os.getenv('REALNET_DEBUG', False))
        :param api_base_url:
        :param auth_url:
        :param callback_url:
        :param client_id:
        :param client_key:
        :param client_secret:
        :param token_url:
        :param debug:
        :param client_cert:
        :param client_cert_key:
        :param ca_bundle:
        :param timeout:
        '''

        self.api_base_url = api_base_url
        self.auth_url = auth_url
        self.callback_url = callback_url
        self.client_id = client_id
        self.client_key = client_key
        self.client_secret = client_secret
        self.token_url = token_url
        self.debug = debug
        self.client_cert = client_cert
        self.client_cert_key = client_cert_key
        self.ca_bundle = ca_bundle
        self.timeout = timeout

    def get_client_id(self):
        return self.client_id

    def get_client_key(self):
        return self.client_key

    def get_client_secret(self):
        return self.client_secret

    def get_callback_url(self):
        return self.callback_url

    def get_auth_url(self):
        return self.auth_url

    def get_api_base_url(self):
        return self.api_base_url

    def get_token_url(self):
        return self.token_url

    def get_debug(self):
        return self.debug

    def get_client_cert(self):
        return self.client_cert

    def get_client_cert_key(self):
        return self.client_cert_key

    def get_ca_bundle(self):
        return self.ca_bundle

    def get_timeout(self):
        return self.timeout
