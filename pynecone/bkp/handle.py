from .amqp import AMQP
from .run import Run


class Handle(AMQP):

    def __init__(self):
        super().__init__("handle")

    def execute(self, args, client):
        client['channel'].basic_consume(queue=args.amqp_queue_name,
                                        on_message_callback=Run.load_script(args.script_path, args.func_name, {'args': args, 'client': client}))
        client['channel'].start_consuming()

    def add_command_arguments(self, parser):
        parser.add_argument('script_path', help="path to the script to be executed")
        parser.add_argument('func_name', help="name of the function in the script to be executed")

    def get_help(self):
        return 'handle help'