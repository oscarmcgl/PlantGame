import random
import random


def basic_question():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operator = random.choice(['+', '-', '*', '/'])
    
    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    elif operator == '*':
        answer = num1 * num2
    else:
        num1, num2 = num2 * random.randint(1, 10), num2
        answer = num1 // num2
    
    question = f"{num1} {operator} {num2} = ?"
    return question, answer
