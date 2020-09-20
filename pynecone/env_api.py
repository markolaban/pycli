from pynecone import Shell

from .env_api_new import EnvApiNew
from .env_api_delete import EnvApiDelete
from .env_api_list import EnvApiList
from .env_api_manage import EnvApiManage


class EnvApi(Shell):

        def __init__(self):
            super().__init__('api')

        def get_commands(self):
            return [
                    EnvApiNew(),
                    EnvApiDelete(),
                    EnvApiList(),
                    EnvApiManage()
            ]

        def add_arguments(self, parser):
            pass

        def get_help(self):
            return 'manage APIs'