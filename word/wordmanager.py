import os
import random
import sys


class WordManager:
    def __init__(self):
        self.words = self.get_word_data()
        self.current_words = []
        self.set_initial_random_words()
        self.total_chars = 0
        self.correct_chars = 0
        self.incorrect_chars = 0
        self.total_words = 0
        self.correct_words = 0
        self.incorrect_words = 0
        self.word_accuracy = 0
        self.char_accuracy = 0
        self.words_seen = 0
        self.wpm = 0

    def manage_word_input(self, user_input):
        if user_input == self.current_words[0]:
            self.correct_chars += len(list(self.current_words[0]))
            self.correct_words += 1
            self.words_seen += 1
            self.set_next_word()
        else:
            self.incorrect_words += 1
            self.compute_incorrect_chars(user_input)
            self.words_seen += 1
            self.set_next_word()

    def compute_incorrect_chars(self, user_input):
        current_chars = list(self.current_words[0])
        total_chars = len(current_chars)
        user_input_chars = list(user_input)
        if total_chars == len(user_input_chars):
            self.incorrect_chars += self.get_word_char_difference(
                current_chars, user_input_chars
            )
        elif total_chars > len(user_input_chars):
            user_input_chars += [""] * (total_chars - len(user_input_chars))
            self.incorrect_chars += self.get_word_char_difference(
                current_chars, user_input_chars
            )
        elif total_chars < len(user_input_chars):
            amount_to_cut_off = len(user_input_chars) - total_chars
            user_input_chars = user_input_chars[
                : len(user_input_chars) - amount_to_cut_off
            ]
            self.incorrect_chars += self.get_word_char_difference(
                current_chars, user_input_chars, amount_to_cut_off
            )
        self.correct_chars += total_chars - self.incorrect_chars
        # print(f"Correct: {self.correct_chars}")
        # print(f"Incorrect: {self.incorrect_chars}")

    def get_word_char_difference(
        self, current_chars, user_input_chars, pre_difference=0
    ):
        difference = 0 + pre_difference
        for i, char in enumerate(current_chars):
            if char != user_input_chars[i]:
                difference += 1
        return difference

    def compute_statistics(self):
        self.compute_wpm()
        self.compute_word_accuracy()
        self.compute_char_accuracy()

    def compute_wpm(self):
        self.wpm = self.correct_words

    def compute_word_accuracy(self):
        self.total_words = self.correct_words + self.incorrect_words
        if self.incorrect_words != 0:
            self.word_accuracy = round((self.correct_words / self.total_words) * 100, 2)
        else:
            self.word_accuracy = 100

    def compute_char_accuracy(self):
        self.total_chars = self.correct_chars + self.incorrect_chars
        if self.incorrect_chars != 0:
            self.char_accuracy = round((self.correct_chars / self.total_chars) * 100, 2)
        else:
            self.char_accuracy = 100

    def get_word_data(self):
        with open("most-common-words.txt", "r") as file:
            data = file.read().splitlines()
        return data

    def print_statistics(self):
        print(f"WPM: {self.wpm}")
        print(
            f"Word Accuracy: ( {self.correct_words} | {self.incorrect_words} ) -> {self.word_accuracy}%"
        )
        print(
            f"Char Accuracy: ( {self.correct_chars} | {self.incorrect_chars} ) -> {self.char_accuracy}%"
        )

    def print_current_words(self):
        print(*self.current_words)

    def get_random_word(self):
        choice = random.choice(self.words)
        return choice

    def set_next_word(self):
        self.current_words.pop(0)
        self.current_words.append(self.get_random_word())

    def set_initial_random_words(self):
        for i in range(10):
            self.current_words.append(self.get_random_word())

    def get_custom_input(self, prefix=""):
        """Custom string input that submits with space rather than enter"""
        concatenated_string = ""
        sys.stdout.write(prefix)
        sys.stdout.flush()
        while True:
            key = ord(self.get_key())
            if key == 32:
                break
            concatenated_string = concatenated_string + chr(key)
            # Print the characters as they're entered
            sys.stdout.write(chr(key))
            sys.stdout.flush()
        return concatenated_string

    def get_key(self):
        if sys.platform == "win32":
            import msvcrt

            return msvcrt.getch()
        else:
            import getch

            return getch.getch()

    def reset(self):
        self.words = self.get_word_data()
        self.current_words = []
        self.set_initial_random_words()
        self.total_chars = 0
        self.correct_chars = 0
        self.incorrect_chars = 0
        self.total_words = 0
        self.correct_words = 0
        self.incorrect_words = 0
        self.word_accuracy = 0
        self.char_accuracy = 0
        self.words_seen = 0
        self.wpm = 0