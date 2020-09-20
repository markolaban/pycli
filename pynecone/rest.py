from .shell import Shell
from .rest_get import Rest_Get
from .rest_put import Rest_Put
from .rest_post import Rest_Post
from .rest_delete import Rest_Delete
from .config import Config

class Rest(Shell):

    def get_commands(self):
        return [Rest_Get(),
                Rest_Put(),
                Rest_Post(),
                Rest_Delete()]

    def add_arguments(self, parser):
        pass

    def __init__(self):
        super().__init__('rest')



    def get_help(self):
        return 'makes standard Rest calls'

    @classmethod
    def api(cls, name=None):
        auth = Config.get_api(name)['auth']
        pass











