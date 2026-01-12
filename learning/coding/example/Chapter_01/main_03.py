import os
os.system('pip install codingnow --upgrade')
from codingnow.learning.coding.codingTest import *

coding_test = CodingTest()
coding_test.start(chapter=1)

while True:
    answer = 0
    cnt = 0
    op = ''
    values = []
    
    while True:
        value = coding_test.get()
        
        if value == 'END':
            break        
        if value == '+' or value == '-' or value == '*' or value == '/' or value == '//' or value == '%':
            op = value
            continue        
        values.append(value)
        
    if op == '+':
        answer = values[0] + values[1]
    elif op == '-':
        answer = values[0] - values[1]
    elif op == '*':
        answer = values[0] * values[1]
    elif op == '/':
        answer = values[0] / values[1]
    elif op == '//':
        answer = values[0] // values[1]
    elif op == '%':
        answer = values[0] % values[1]
        
    result = coding_test.answer(answer)
    if result:
        continue
    else:
        break
    