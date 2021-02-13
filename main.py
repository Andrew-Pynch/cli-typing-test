import os
import sys
import time
import random
from word.wordmanager import WordManager
from util.timer import Timer


def main():
    manager = WordManager()
    clear = lambda: os.system("clear")  # on Linux System
    # timer = Timer(60)
    # timer.countdown()
    while True:
        manager.print_current_words()
        user_word = manager.get_custom_input()
        manager.manage_word_input(user_word)
        clear()


if __name__ == "__main__":
    main()
