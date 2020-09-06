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


class MySubshell1(Subshell):

    def get_help(self):
        return "mysubshell1 help"

    def __init__(self):
        super().__init__("mysubshell1")

    def get_commands(self):
        return [MyCommand()]

    def add_arguments(self, parser):
        parser.add_argument('--bar1', help='bar1 help')

class MySubshell2(Subshell):

    def get_help(self):
        return "mysubshell2 help"

    def __init__(self):
        super().__init__("mysubshell2")

    def get_commands(self):
        return [MyCommand()]

    def add_arguments(self, parser):
        parser.add_argument('--bar2', help='bar2 help')



class MyShell(Shell):

    def get_help(self):
        return "you can run mysubshell1 or mysubshell2 commands"

    def __init__(self):
        super().__init__('myshell')

    def get_commands(self):
        return [MySubshell1(), MySubshell2()]

    def add_arguments(self, parser):
        parser.add_argument('--oof', help='oof help')

MyShell().run()