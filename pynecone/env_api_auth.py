from pynecone import Shell

from .env_api_auth_show import EnvApiAuthShow
from .env_api_auth_set_none import EnvApiAuthSetNone
from .env_api_auth_set_basic import EnvApiAuthSetBasic
from .env_api_auth_set_cert import EnvApiAuthSetCert
from .env_api_auth_set_secret import EnvApiAuthSetSecret
from .env_api_auth_set_user import EnvApiAuthSetUser


class EnvApiAuth(Shell):

        def __init__(self):
            super().__init__('auth')

        def get_commands(self):
            return [
                    EnvApiAuthShow(),
                    EnvApiAuthSetNone(),
                    EnvApiAuthSetBasic(),
                    EnvApiAuthSetCert(),
                    EnvApiAuthSetSecret(),
                    EnvApiAuthSetUser()
            ]

        def add_arguments(self, parser):
            pass

        def get_help(self):
            return 'configure api authentication'