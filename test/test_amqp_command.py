import unittest
import os

from pynecone import AMQPCommand

class AMQPCommandTestCase(unittest.TestCase):
    def test_something(self):
        path = os.path.join(os.getcwd(),'scripts.py')
        cmd = AMQPCommand(path,
                          'test_something_script',
                          'aaaaaa',
                          '123456',
                          '1.1.1.1',
                          5672,
                          '/',
                          'broadcast')

        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
