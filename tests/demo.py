from pynecone import Shell, Subshell, Command


class MyCommand(Command):

    def __init__(self):
        super().__init__("mycommand")

    def add_arguments(self, parser):
        parser.add_argument('--foo', help='foo help')

    def run(self, args):
        print("*** hello from mycommand, foo is {0}".format(args.foo))

    def get_commands(self):
        return [self]


class MySubshell(Subshell):

    def __init__(self):
        super().__init__("mysubshell")

    def get_commands(self):
        return [MyCommand()]

    def add_arguments(self, parser):
        pass
        # parser.add_argument('--bar', help='bar help')



class MyShell(Shell):

    def __init__(self):
        super().__init__('myshell')

    def get_commands(self):
        return [MySubshell()]

    def add_arguments(self, parser):
        pass

MyShell().run()