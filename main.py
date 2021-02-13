import os
import sys
import time
import random
from util.util import get_remaining_time
from word.wordmanager import WordManager
from util import *


def main():
    manager = WordManager()
    clear = lambda: os.system("clear")  # on Linux System

    print("To being, press space")
    start = manager.get_custom_input()
    start_time = time.time()
    remaining_time = get_remaining_time(start_time)
    while remaining_time <= 60:
        clear()
        print(f"{remaining_time} seconds\n")
        manager.print_current_words()
        user_word = manager.get_custom_input()
        manager.manage_word_input(user_word)
        clear()
    handle_post_run(manager)


def handle_post_run(manager):
    pass


if __name__ == "__main__":
    main()
