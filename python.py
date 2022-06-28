#!/usr/bin/env python3
"""
some code to do a job
"""
# import os
import sys
import time

# could be "linux", "linux2", "linux3", ...
if sys.platform.startswith("linux"):
    # linux
    pass
elif sys.platform == "darwin":
    # MAC OS X
    pass
elif sys.platform == "win32":
    # Windows (either 32-bit or 64-bit)
    pass


class MyClass():
    """
    a class to do a job
    """

    def __init__(self):
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
