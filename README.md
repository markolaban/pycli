# pynecone

A library to make writing cli applications easier

Usage example:

    from pynecone import Shell, Subshell, Command
    
    
    class MyCommand(Command):
    
        def __init__(self):
            super().__init__("mycommand")
    
        def add_arguments(self, parser):
            parser.add_argument('--foo', help='foo help')
    
        def run(self, args):
            print(args)
    
    class MySubshell(Subshell):
    
        def __init__(self):
            super().__init__("mysubshell")
    
        def get_commands(self):
            return [MyCommand()]
    
        def add_arguments(self, parser):
            pass
    
    
    class MyShell(Shell):
    
        def __init__(self):
            super().__init__('myshell')
    
        def get_commands(self):
            return [MySubshell()]
    
        def add_arguments(self, parser):
            pass
    
    MyShell().run()
    
    def main():
        MyShell().run()
    
    
    if __name__ == "__main__":
        main()