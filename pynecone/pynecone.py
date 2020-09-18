from .shell import Shell
from .auth import Auth
from .gen import Gen
from .task import Task
from .folder import Folder
from .server import Server
from .job import Job
from .config import Config

class Pynecone(Shell):

    def __init__(self):
        super().__init__('pynecone')

    def get_commands(self):
        return [Auth(), Gen(), Task(), Folder(), Server(), Job(), Config()]

    def add_arguments(self, parser):
        pass

    def get_help(self):
        return 'pynecone shell'