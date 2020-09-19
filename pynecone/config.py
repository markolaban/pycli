import yaml
import os


class Config:
    def __init__(self, name, path):
        self.path = path
        self.full_path = os.path.join(path, name)
        self.data = {}

    def load(self):
        with open(self.full_path) as file:
            self.data = yaml.safe_load(file)

    def save(self):
        with open(self.full_path, 'w') as file:
            yaml.dump(self.data, file)

    def create_environment(self, name):
        environments = self.data.get('environments')
        if environments is None:
            self.data['environments'] = []
            environments = self.data['environments']

        env = { 'name': name,
                'auth': {},
                'database': {'url': 'sqlite:///{0}'.format(os.path.join(self.path, 'pynecone.db'))},
                'server': {'host': '0.0.0.0', 'port': '8080'}}

        environments.append(env)
        self.save()


    def generate(self):
        print('*** Generating default config file ***')

        dict_file = { 'environments': [
            {'name': 'local',
                'auth': {},
                'database': {'url': 'sqlite:///{0}'.format(os.path.join(self.path, 'pynecone.db'))},
                'server': {'host': '0.0.0.0', 'port': '8080'}}
        ]}

        with open(self.full_path, 'w') as file:
            yaml.dump(dict_file, file)

    def get_database_url(self):
        return self.data['database']['url']

    def get_server_host(self):
        return self.data['server']['host']

    def get_server_port(self):
        return self.data['server']['port']

    @classmethod
    def init(cls, name='pynecone.yml', path=os.getcwd()):
        cfg = Config(name, path)

        if not os.path.exists(cfg.full_path):
            cfg.generate()

        cfg.load()
        return cfg
