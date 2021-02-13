import sys
import time
import random


class Timer:
    def __init__(self, _seconds):
        self.seconds = _seconds

    def countdown(self):
        """Timer counting down from 60 seconds to 0"""
        t = 0
        while t in range(self.seconds):
            sys.stdout.write("\r{} seconds".format(self.seconds))
            time.sleep(1)
            self.seconds -= 1
            sys.stdout.flush()

    def reset(self):
        self.seconds = 60