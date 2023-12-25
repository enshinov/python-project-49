#! /usr/bin/env python3
from ..common import game
import random


def main():
    game_task = 'Answer "yes" if given number is prime. Otherwise answer "no".'

    def is_prime(number: int):
        if number < 2:
            return False
        for i in range(2, number // 2 + 1):
            if number % i == 0:
                return False
        return True

    min_random_int = 0
    max_random_int = 100

    def get_question_answer():
        question = random.randint(min_random_int, max_random_int)
        answer = 'yes' if is_prime(question) else 'no'
        return question, answer

    game(game_task, get_question_answer)


if __name__ == '__main__':
    main()
