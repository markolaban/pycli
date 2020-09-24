from abc import abstractmethod
from .config import Config
from .module import TaskProvider


class Client(TaskProvider):

    def __init__(self):
        self.cfg = Config.init()

    def get_config(self):
        return self.cfg

    @abstractmethod
    def get_client(self):
        pass
