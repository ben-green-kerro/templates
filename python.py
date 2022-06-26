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
        time.sleep(1)

    def print_output(self):
        """
        prints the output of calculation.
        """
        print(f'The output of the calculation is {self.val_c}')

    def


if __name__ == 'main':
    instance = MyClass()
    instance.print_output()
