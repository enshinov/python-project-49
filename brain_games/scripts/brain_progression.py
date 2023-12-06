#! /usr/bin/env python3
from ..common import game
import random


def main():
    game_task = 'What number is missing in the progression?'

    min_random_int = 0
    max_random_int = 100

    progression_length = 10
    min_step = -10
    max_step = 10

    def get_question_answer():
        init = random.randint(min_random_int, max_random_int)
        step = random.randint(min_step, max_step)
        missing_position = random.randint(0, progression_length)
        progression = []
        for i in range(progression_length + 1):
            if i == missing_position:
                progression.append('..')
            else:
                progression.append(str(init + step * i))
        question = ' '.join(progression)
        answer = str(init + step * missing_position)
        return question, answer

    game(game_task, get_question_answer)


if __name__ == '__main__':
    main()
