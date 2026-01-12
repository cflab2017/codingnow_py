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
        
        if str(value) in ['+', '-', '*', '/', '//', '%']:
            op = value
            continue
        
        values.append(value)
    
    calculate = str(values[0]) + op + str(values[1])
    answer = eval(calculate)

    result = coding_test.answer(answer)
    if result:
        continue
    else:
        break
    