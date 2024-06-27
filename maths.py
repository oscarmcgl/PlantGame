import random
import random

fruit = ['apple', 'banana', 'orange', 'pear', 'grape', 'mango', 'kiwi','raspberry']
fruitpl = ['apples', 'bananas', 'oranges', 'pears', 'grapes', 'mangoes', 'kiwis','raspberries']
item = ['pen', 'pencil', 'rubber', 'ruler', 'notebook', 'folder', 'scissors', 'glue stick']
itempl = ['pens', 'pencils', 'rubbers', 'rulers', 'notebooks', 'folders', 'scissors', 'glue sticks']
names = ['Alistair','Lara','Hannah','Ollie','Zoe','Ellie','Jess','Albie','Alex']
add_questions = [
    '{name} has {num1} {choice1} and {num2} {choice2}. How many {choice3} does {name} have in total?']
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
        choices = random.randint(0,len(fruit)-1)
        #! work out whether singular or plural etc.


