


class Client:

    def __init__(self,
                 api_base_url,
                 get_token,
                 debug=False,
                 client_cert=None,
                 client_cert_key=None,
                 ca_bundle=None,
                 timeout=10):

        self.api_base_url = api_base_url
        self.token = None
        self.get_token = get_token
        self.debug = debug
        self.client_cert = client_cert
        self.client_cert_key = client_cert_key
        self.ca_bundle = ca_bundle
        self.timeout = timeout
        if self.debug:
            print('debug: ', self.debug)





