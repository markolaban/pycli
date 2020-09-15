import importlib.util
import pika
from .command import Command

class AMQPCommand(Command):

    def __init__(self,
                 script_path,
                 function_name,
                 amqp_client_key,
                 amqp_client_secret,
                 amqp_host,
                 amqp_port,
                 amqp_path,
                 amqp_queue_name,
                 debug=False,
                 client_cert=None,
                 client_cert_key=None,
                 ca_bundle=None,
                 timeout=10):

        self.script_path = script_path
        self.function_name = function_name
        self.amqp_client_key = amqp_client_key
        self.amqp_client_secret = amqp_client_secret
        self.amqp_host = amqp_host
        self.amqp_port = amqp_port
        self.amqp_path = amqp_path
        self.amqp_queue_name = amqp_queue_name
        self.debug = debug
        self.client_cert = client_cert
        self.client_cert_key = client_cert_key
        self.ca_bundle = ca_bundle
        self.timeout = timeout

    def get_handler(self, args, file, callback):
        spec = importlib.util.spec_from_file_location('testmod', file)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        def handler(ch, method, properties, body):
            getattr(module, callback)({'args': args,
                                       'amqp': {'channel': ch,
                                                 'method': method,
                                                 'properties': properties,
                                                 'body': body}})

        return handler

    def add_arguments(self, parser):
        pass

    def run(self, args):
        credentials = pika.PlainCredentials(self.amqp_client_key, self.amqp_client_secret)
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(self.amqp_host, self.amqp_port, self.amqp_path, credentials))
        channel = connection.channel()
        channel.basic_consume(queue=self.amqp_queue_name, on_message_callback=self.get_handler(args, self.script_path, self.function_name))
        channel.start_consuming()

    def get_help(self):
            pass

