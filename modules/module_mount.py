from abc import abstractmethod
from pynecone import ModuleProvider, ProtoShell, ProtoCmd, Config


class MountProvider(ModuleProvider):

    @abstractmethod
    def get_folder(self, path):
        pass


class Mount(ProtoShell):

    class Create(ProtoShell):

        class Local(ProtoCmd):

            def __init__(self):
                super().__init__('local',
                                 'mount local path',
                                 lambda args: print(Config.init().create_mount(args.name, {'type': 'local', 'path': args.path})))

            def add_arguments(self, parser):
                # parser.add_argument('name', help="specifies the mount name")
                parser.add_argument('path', help="specifies the local path")

        class Aws(ProtoCmd):

            def __init__(self):
                super().__init__('aws',
                                 'mount aws bucket',
                                 lambda args: print(Config.init().create_mount(args.name, {'type': 'aws', 'bucket': args.bucket})))

            def add_arguments(self, parser):
                # parser.add_argument('name', help="specifies the mount name")
                parser.add_argument('bucket', help="specifies the bucket name")

        def __init__(self):
            super().__init__('create', [Mount.Create.Local(), Mount.Create.Aws()], 'create a mount')

        def add_arguments(self, parser):
            parser.add_argument('name', help="specifies the name of the mount to be created")

    class List(ProtoCmd):

        def __init__(self):
            super().__init__('list',
                             'list mounts',
                             lambda args: print(Config.init().list_mount()))

    class Delete(ProtoCmd):

        def __init__(self):
            super().__init__('delete',
                             'delete a mount',
                             lambda args: print(Config.init().delete_mount(args.name)))

        def add_arguments(self, parser):
            parser.add_argument('name', help="specifies the name of the mount to be deleted")

    class Get(ProtoCmd):

        def __init__(self):
            super().__init__('get',
                             'get mount',
                             lambda args: print(Config.init().get_mount_cfg(args.name, True)))

        def add_arguments(self, parser):
            parser.add_argument('name', help="specifies the name of the mount to be retrieved")

    def __init__(self):
        super().__init__('mount', [Mount.Create(), Mount.List(), Mount.Delete(), Mount.Get()], 'mount shell')

    @classmethod
    def from_path(cls, path):
        config = Config.init()
        mount_path = '/{0}'.format(path.split('/')[1])
        return config.get_entry_instance('mounts', mount_path)


class Module(ModuleProvider):

    def get_instance(self, **kwargs):
        return Mount()