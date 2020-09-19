from pynecone import Shell

from .env_api_auth import EnvApiAuth
from .env_api_url import EnvApiUrl


class EnvApiManage(Shell):

        def __init__(self):
            super().__init__('manage')

        def get_commands(self):
            return [
                    EnvApiAuth(),
                    EnvApiUrl()
            ]

        def add_arguments(self, parser):
            pass

        def get_help(self):
            return 'manage the api'