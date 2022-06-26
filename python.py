#!/usr/bin/env python3
"""
some code to do a job
"""
import time


class MyClass():
    """
    a class to do a job
    """

    def __init__(self):
        self.val_a = 4
        self.val_b = 5
        self.val_c = self.val_a * self.val_b

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
