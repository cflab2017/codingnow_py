import os
os.system('pip install codingnow --upgrade')
from codingnow.learning.coding.codingTest import *

problem = CodingTest()
problem.start(chapter=1)

a = problem.get()
b = problem.get()
# op = problem.get()
op = problem.get_option('operation')

if op == '+':
    c = a + b
elif op == '-':
    c = a - b
elif op == '*':
    c = a * b
elif op == '/':
    c = a / b
elif op == '//':
    c = a // b
elif op == '%':
    c = a % b

problem.answer(c)