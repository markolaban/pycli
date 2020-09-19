from .shell import Shell
from .auth import Auth
from .gen import Gen
from .env import Env
from .task import Task
from .folder import Folder
from .server import Server
from .job import Job
from .repl import Repl

class Pynecone(Shell):

    def __init__(self):
        super().__init__('pynecone')

    def get_commands(self):
        return [Auth(), Gen(), Env(), Task(), Folder(), Server(), Job(), Repl()]

    def add_arguments(self, parser):
        pass

    def get_help(self):
        return 'pynecone shell'