#! /usr/local/env python3

import prompt
from .cli import welcome_user


def game(game_task, get_question_answer):
    user_name = welcome_user()
    print(game_task)
    rounds_count = 4
    for round_number in range(1, rounds_count):
        question, correct_answer = get_question_answer()
        print(f"Question: {question}")
        user_answer = prompt.string('Your answer: ')
        if user_answer == correct_answer:
            print('Correct!')
        else:
            error_text = ' is wrong answer :(. Correct answer was '
            print(f"'{user_answer}'{error_text}'{correct_answer}'.")
            print(f"Let's try again, {user_name}")
            return
    print(f"Congratulations, {user_name}!")
