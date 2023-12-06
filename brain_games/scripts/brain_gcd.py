#! /usr/bin/env python3
from ..common import game
import random


def main():
    game_task = 'Find the greatest common divisor of given numbers.'

    def find_greatest_divisor(number1: int, number2: int):
        a = number1
        b = number2
        while (a != 0) and (b != 0):
            if (a > b):
                a %= b
            else:
                b %= a
        return a + b

    min_random_int = 0
    max_random_int = 100

    def get_question_answer():
        number1 = random.randint(min_random_int, max_random_int)
        number2 = random.randint(min_random_int, max_random_int)
        question = f"{number1} {number2}"
        answer = find_greatest_divisor(number1, number2)
        return question, str(answer)

    game(game_task, get_question_answer)


if __name__ == '__main__':
    main()
