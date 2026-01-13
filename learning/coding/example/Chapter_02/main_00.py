# import os
# os.system('pip install codingnow --upgrade')
from codingnow.learning.coding.codingTest import *

problem = CodingTest()
problem.start(chapter=2)


problem.print_options()

oop = problem.get_option('operation')
print('oop:', oop)

length = problem.get_option('length')
print('length:', length)