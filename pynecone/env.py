from pynecone import Shell

from .env_list import EnvList
from .env_create import EnvCreate
from .env_delete import EnvDelete
from .env_update import EnvUpdate
from .env_activate import EnvActivate


class Env(Shell):

        def __init__(self):
            super().__init__('env')

        def get_commands(self):
            return [
                    Env_List(),
                    Env_Create(),
                    Env_Delete(),
                    Env_Update(),
                    Env_Activate()
            ]

        def add_arguments(self, parser):
            pass

        def get_help(self):
            return 'Env shell'