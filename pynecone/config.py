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
        self.generate()

        found = [env for env in self.data.get('environments') if env['name'] == name]

        if found:
            return None

        env = { 'name': name,
                'auth': {},
                'database': {'url': 'sqlite:///{0}'.format(os.path.join(self.path, 'pynecone.db'))},
                'server': {'host': '0.0.0.0', 'port': '8080'}}

        self.data['environments'].append(env)
        self.save()
        return env

    def delete_environment(self, name):
        self.generate()

        found = [env for env in self.data.get('environments') if env['name'] == name]

        if found:
            if found[0]['name'] == self.data['active_environment']:
                print('cannot delete the active environment {0}'.format(name))
                return None
            else:
                self.data['environments'] = [i for i in self.data['environments'] if i['name'] != name]
                self.save()
                return name
        else:
            return None

    def set_active_environment(self, name):
        self.generate()

        found = [env for env in self.data.get('environments') if env['name'] == name]
        if found:
            self.data['active_environment'] = name
            self.save()
            return found
        else:
            return None

    def get_active_environment(self):
        self.generate()

        return self.data['active_environment']

    def list_environments(self):
        self.generate()

        return self.data['environments']

    def get_environment(self, name):
        self.generate()

        found = [env for env in self.data.get('environments') if env['name'] == name]
        if found:
            return yaml.dump(found)
        else:
            return None


    def generate(self, force=False):
        if self.data.get('environments') is None or force:
            print('*** generating default config file ***')

            self.data = {
                'environments': [
                        {
                            'name': 'local',
                            'auth': {},
                            'database': {'url': 'sqlite:///{0}'.format(os.path.join(self.path, 'pynecone.db'))},
                            'server': {'host': '0.0.0.0', 'port': '8080'}
                        }
                ],
                'active_environment': 'local'}

            self.save()

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
