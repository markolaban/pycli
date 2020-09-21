from .proto import ProtoShell, ProtoCmd

from os import listdir
from os.path import isfile, isdir, join


class MountLocal(ProtoShell):

    def __init__(self, path='.'):
        self.path = path

    def get(self, path):
        if isdir(path):
            return Folder(path, self.path)
        else:
            return File(path, self.path)

    def list(self, path):
        return [File(f, path) if isfile(join(path, f)) else Folder(f, path) for f in listdir(path)]

    def put(self, path, f):
        pass


class File(ProtoShell):

    def __init__(self, path, mount_path='.'):
        self.path = path
        self.mount_path = mount_path


class Folder(ProtoShell):

    def __init__(self, path, mount_path):
        self.path = path
        self.mount_path = mount_path

    class Get(ProtoCmd):

        def __init__(self, mount_path='.'):
            super().__init__('get',
                             'get folder or file from path',
                             lambda args: MountLocal(mount_path).get(args.path))

        def add_arguments(self, parser):
            parser.add_argument('path', help="specifies the path", default='.', const='.', nargs='?')

    class Put(ProtoCmd):

        def __init__(self, mount_path='.'):
            super().__init__('put',
                             'put folder or file to path',
                             lambda args: MountLocal(mount_path).put(args.path, args.f))

        def add_arguments(self, parser):
            parser.add_argument('path', help="specifies the path", default='.', const='.', nargs='?')

    class Delete(ProtoCmd):

        def __init__(self, mount_path='.'):
            super().__init__('delete',
                             'delete path',
                             lambda args: MountLocal(mount_path).delete(args.path))

        def add_arguments(self, parser):
            parser.add_argument('path', help="specifies the path to be deleted", default='.', const='.', nargs='?')

    class List(ProtoCmd):

        def __init__(self, mount_path='.'):
            super().__init__('list',
                             'list files and folders on path',
                             lambda args: MountLocal(mount_path).list(args.path))

        def add_arguments(self, parser):
            parser.add_argument('path', help="specifies the path to be listed", default='.', const='.', nargs='?')

    def __init__(self):
        super().__init__('folder', [Folder.Get(), Folder.Put(), Folder.Delete(), Folder.List()], 'folder shell')
