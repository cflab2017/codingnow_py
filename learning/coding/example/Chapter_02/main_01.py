# import os
# os.system('pip install codingnow --upgrade')
from codingnow.learning.coding.codingTest import *

problem = CodingTest()
problem.start(chapter=2)

#최대 값
a = problem.get()
b = problem.get()

if a > b:
    c = a
else:
    c = b

problem.answer(c)

#최소 값
a = problem.get()
b = problem.get()

if a < b:
    c = a
else:
    c = b

problem.answer(c)


#짝수개수
a = problem.get()
b = problem.get()

cnt = 0
if a % 2 == 0:
    cnt += 1
if b % 2 == 0:
    cnt += 1
problem.answer(cnt)
        
    
#짝수개수
a = problem.get()
b = problem.get()

cnt = 0
if a % 2 == 1:
    cnt += 1
if b % 2 == 1:
    cnt += 1
problem.answer(cnt)

#합계
a = problem.get()
b = problem.get()
c = a + b
problem.answer(c)

#평균
a = problem.get()
b = problem.get()
c = a + b
c = c / 2
problem.answer(c)