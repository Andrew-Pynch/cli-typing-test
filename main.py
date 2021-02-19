import os
import sys
import time
import random
from util.util import get_remaining_time, clear
from word.wordmanager import WordManager


def main():
    manager = WordManager()

    print("To being, press space")
    start = manager.get_custom_input()
    start_time = time.time()
    remaining_time = get_remaining_time(start_time)

    while remaining_time <= 60:
        clear()
        print(f"{60 - remaining_time} seconds remaining")
        manager.print_current_words()
        user_word = manager.get_custom_input()
        manager.manage_word_input(user_word)
        clear()
        remaining_time = get_remaining_time(start_time)

    handle_post_run(manager)


def handle_post_run(manager):
    print(f'{"-"*5}Run Statistics{"-"*5}')
    manager.compute_statistics()
    manager.print_statistics()

if __name__ == "__main__":
    main()
