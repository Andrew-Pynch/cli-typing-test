import os
import sys
import time
import random


def get_remaining_time(start_time):
    return round((time.time() - start_time), 0)


def clear():
    if sys.platform == "win32":
        os.system("cls")
    else:
        os.system("clear")
