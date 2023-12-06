#! /usr/bin/env python3
from ..common import game
import random


def main():
    game_task = 'What is the result of the expression?'

    def calculate(number1: int, number2: int, operator: str):
        match operator:
            case '+': return number1 + number2
            case '-': return number1 - number2
            case '*': return number1 * number2

    min_random_int = 0
    max_random_int = 100
    operators = ('+', '-', '*')

    def get_question_answer():
        operator = random.choice(operators)
        number1 = random.randint(min_random_int, max_random_int)
        number2 = random.randint(min_random_int, max_random_int)
        question = f"{number1} {operator} {number2}"
        answer = calculate(number1, number2, operator)
        return question, str(answer)

    game(game_task, get_question_answer)


if __name__ == '__main__':
    main()
