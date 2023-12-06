#! /usr/bin/env python3
from ..common import game
import random


def main():
    game_task = 'Answer "yes" if number even otherwise answer "no".'

    def is_even(number: int):
        return number % 2 == 0

    min_random_int = 0
    max_random_int = 100

    def get_question_answer():
        question = random.randint(min_random_int, max_random_int)
        answer = 'yes' if is_even(question) else 'no'
        return str(question), answer

    game(game_task, get_question_answer)


if __name__ == '__main__':
    main()
