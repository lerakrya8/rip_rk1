# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random


def gen_random(num_count, begin, end):
    for count in range(num_count):
        yield random.randint(begin, end)


if __name__ == "__main__":
    for i in gen_random(5, 0, 15):
        print(i)
