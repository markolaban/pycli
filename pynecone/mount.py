from .proto import ProtoShell, ProtoCmd


class Mount(ProtoShell):

    class Create(ProtoShell):

        class Local(ProtoCmd):

            def __init__(self):
                super().__init__('local',
                                 'mount local path',
                                 lambda args: args.path)

            def add_arguments(self, parser):
                parser.add_argument('path', help="specifies the local path", default='.', const='.', nargs='?')

        class Aws(ProtoCmd):

            def __init__(self):
                super().__init__('aws',
                                 'mount aws bucket',
                                 lambda args: args.path)

            def add_arguments(self, parser):
                parser.add_argument('bucket', help="specifies the bucket name")

        def __init__(self):
            super().__init__('create', [Mount.Create.Local(), Mount.Create.Aws()], 'create a mount')

        def add_arguments(self, parser):
            parser.add_argument('name', help="specifies the name of the mount to be created")

    class List(ProtoCmd):

        def __init__(self):
            super().__init__('list',
                             'list mounts',
                             lambda args: args)

        def add_arguments(self, parser):
            pass

    class Delete(ProtoCmd):

        def __init__(self):
            super().__init__('delete',
                             'delete a mount',
                             lambda args: args.name)

        def add_arguments(self, parser):
            parser.add_argument('name', help="specifies the name of the mount to be deleted")

    class Get(ProtoCmd):

        def __init__(self):
            super().__init__('get',
                             'get mount',
                             lambda args: args.name)

        def add_arguments(self, parser):
            parser.add_argument('name', help="specifies the name of the mount to be retrieved")

    def __init__(self):
        super().__init__('mount', [Mount.Create(), Mount.List(), Mount.Delete(), Mount.Get()], 'mount shell')