from pynecone import Shell

from .env_list import EnvList
from .env_create import EnvCreate
from .env_delete import EnvDelete
from .env_update import EnvUpdate
from .env_activate import EnvActivate
from .env_show import EnvShow


class Env(Shell):

        def __init__(self):
            super().__init__('env')

        def get_commands(self):
            return [
                    EnvList(),
                    EnvCreate(),
                    EnvDelete(),
                    EnvUpdate(),
                    EnvActivate(),
                    EnvShow()
            ]

        def add_arguments(self, parser):
            pass

        def get_help(self):
            return 'manage environments'