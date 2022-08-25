#!/usr/bin/env python3
"""
some code to do a job
"""
# import os
import sys
import time

# Determine OS
if sys.platform.startswith("linux"):
    system = 'linux'
elif sys.platform == "darwin":
    system = 'macos'
elif sys.platform == "win32":
    system = 'windows'


class MyClass(object):
    """
    a class to do a job
    """

    def __init__(self):
        """
        Runs once when object is initialised
        """
        self.val_a = 4
        self.val_b = 5
        self.val_c = self.val_a * self.val_b

    def handler(self, signum, frame):  # pylint: disable=W0613
        """
        This is the handler for SIGINT events sent by the user pressing ctrl-c.
        """
        print('')
        print("Ctrl-c was pressed. Exiting...")
        sys.exit()

    def print_output(self):
        """
        prints the output of calculation.
        """
        print(f'The output of the calculation is {self.val_c}')

    def print_forever(self):
        """
        calls print_output for all eternity
        """
        while True:
            self.print_output()
            time.sleep(0.1)


if __name__ == '__main__':
    instance = MyClass()
    instance.print_forever()
