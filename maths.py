import random
import random

fruit = ['apple', 'banana', 'orange', 'pear', 'grape', 'mango', 'kiwi','raspberry']
fruitpl = ['apples', 'bananas', 'oranges', 'pears', 'grapes', 'mangoes', 'kiwis','raspberries']
item = ['pen', 'pencil', 'rubber', 'ruler', 'notebook', 'folder', 'scissors', 'glue stick']
itempl = ['pens', 'pencils', 'rubbers', 'rulers', 'notebooks', 'folders', 'scissors', 'glue sticks']
names = ['Alistair','Lara','Hannah','Ollie','Zoe','Ellie','Jess','Albie','Alex']
add_questions = '{name} has {num1} {choice1} and {name2} has {num2} {choice2}. How many {choice3} do {name} and {name2} have in total?'
sub_questions = [
    '{name} has {num1} {choice1} and gives {num2} {choice2} away. How many {choice3} does {name} have left?']
div_questions =[
    '{name} has {num1} {choice1} and wants to share between {num2} friends. How many {choice2} does each friend get?' ]

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

def worded_basic():
    choice = random.randint(1, 2)
    if choice == 1: # addition
        name = random.choice(names)
        name2 = random.choice(names)
        choices = random.randint(0,len(fruit)-1)
        
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        answer = num1 + num2

        if num1 == 1:
            choice1 = fruit[choices]
        else:
            choice1 = fruitpl[choices]
        
        if num2 == 1:
            choice2 = fruit[choices]
        else:
            choice2 = fruitpl[choices]

        choice3 = fruitpl[choices]

        question = add_questions.format(name=name, name2=name2, num1=num1, num2=num2, choice1=choice1, choice2=choice2, choice3=choice3)
        print(question, answer)

    else: #subtraction
        name = random.choice(names)
        choices = random.randint(0,len(fruit)-1)

        num1 = random.randint(1, 10)
        num2 = random.randint(1, num1)
        answer = num1 - num2

        if num1 == 1:
            choice1 = fruit[choices]
        else:
            choice1 = fruitpl[choices]
        if num2 == 1:
            choice2 = fruit[choices]
        else:
            choice2 = fruitpl[choices]

        choice3 = fruitpl[choices]

        question = sub_questions[0].format(name=name, num1=num1, num2=num2, choice1=choice1, choice2=choice2, choice3=choice3)
        print(question, answer)
    
worded_basic()

def worded_division():
    pass
