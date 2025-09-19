
#================================================= # cal.py

def  add(a , b):
	return  a + b
def  sub(a , b):
	return  a - b
def  mul(a , b):
	return  a * b
def  div(a , b):
	return  a / b
class    c1:
	def    m1(self):
		pass
#End  of  the  class
x = 100
y = 200
if  __name__ ==  '__main__':
	print('Hyd')
	print('Sec')
	print('Cyb')

'''
Hyd
Sec
Cyb
'''
#====================================
'''
1) What  is  the  module  name ?  --->  cal

2) py  cal.py
    What  is  the  value  of  __name__ ?  ---> '__main__'
    What  are  the  outputs ?  --->  Hyd ,  Sec  and  Cyb  becoz  if  condition  is  True

3) import  cal
    What  is  the  value  of  __name__ ?  ---> The  imported  module  name  i.e. 'cal'
	What  are  the  outputs ?  ---> Nothing  becoz  if  condition  is   False
'''

#================================================= cal.py  is  not  a  home  work

#================================================= #  Find  outputs  (Home  work)

import  sys , time , math
print(dir(sys))
print()
print()
print(dir(time))
print()
print(dir(math))

#================================================= #  Find  outputs  (Home  work)

import  cal
print(dir(cal))

#================================================= #  Find  outputs  (Home  work)

x = 25
def  disp():
	print('Hello')
class  c1:
        def  m1(self):
                pass
print(dir())
print(type(dir()))
print(type(dir))
'''
['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'c1', 'disp', 'x']
<class 'list'>
<class 'builtin_function_or_method'>
'''
#=================================================
# Write  a  program  to  print  all  the  members  of  cal  module  without  environment  variables

import cal
a=[]
for x in dir(cal):
   if x.startswith('__') and x.endswith('__'):
      a.append(x)
print(a)
# 1) What  is  the  result  of  '__name' . startswith('__')  ?  ---> True

# 2) What  is  the  result  of  '__spec' . endswith('__')  ?  --->  True

# 3) What  is  the  result  of  'spec__' . startswith('__')  ?  ---> False

import cal
print(dir(cal))
a=[]
for x in dir(cal):
   if not (x.startswith('__') and x.endswith('__')):
      a.append(x)
print(a)
# 4) a = []
#     Append  all  the  elements  of  list  returned  by  dir()  function  to  list  'a'  except  environment  variables


#================================================= #  Find  outputs

print(dir())
print()
import  cal
print()
print(dir())
'''
['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']


['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'cal']
'''
#================================================= #  Find  outputs

print(dir())
print()
from  cal  import  *
print()
print(dir())
'''
['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']


['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'add', 'c1', 'div', 'mul', 'sub', 'x', 'y']
'''
#================================================= #  Find  outputs

print(dir())
print()
from  cal  import  add , mul , x
print()
print(dir())
'''
['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']


['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'add', 'mul', 'x']
'''
#================================= # sys . path  demo   program

import  sys
print('Original  sys.path')
for  x  in   sys . path:
	print(x)
print(len(sys . path))
#import  cal

#================================= # Store  sample.py  module  in  c:\\sairam  folder  before  the  program  is  executed  (Home  work)
import sys
# How  to  print  number  of  directories  (or)  folders  in  sys.path
print(len(sys.path))
# How  to  append  c:\sairam  folder  to  sys.path
sys.path.append('c:\\sairam')
# How  to  print  number  of  directories  (or)  folders  in  sys.path
print(len(sys.path))
# How  to  print  object  'x'  of  sample   module  which  is  in  c:\sairam  folder
import sample
print(sample.x)
# How  to  call   function  f1()  of  sample  module  which  is  in  c:\sairam  folder
sample.f1()
# How  to  call   method  m1()  of  class  c1  of  sample  module  which  is  in  c:\sairam  folder
a=sample.c1()
a.m1()
#=================================

from  random  import  *
print(random())
print(randint(1 , 100))
print(uniform(1 , 100))
print(randrange(10))
print(randrange(1 , 11))
print(randrange(1 , 11 , 2))
list = [10 , 20 , 15 , 12 , 18]
print(choice(list))
print(choice('RAJESH'))
set  =  {10 , 20 , 30 , 40}
print(choice(set))
'''
0.687536473913371
38
5.362512996692099
3
8
1
20
R
#error becoz not indexed
'''
#================================= # Write  a  program  to  print  random  character  of  the  string  10  times (Home  work)
for i in range(10):
    print(choice('Lakshman'))
'''
h
L
m
h
a
a
L
n
m
h

'''

#================================= Write  a  program to  generate  10  passwords  each  of  6 character  length  where

# 1st , 3rd , 5th  characters  are  alphabets  and  2nd , 4th , 6th  characters   are  digits

from random import *
def rand():
   for i in range(10):
      b=''
      for j in range(1,7):
         if j%2!=0:
               val=(chr(randint(ord('A'), ord('Z'))))
         else:
               val=str(randint(0,9))
         b=b+val
      print(b)
rand()
'''
Q5J3S8
G4J5C3
T9W7O3
T6M1L7
Q2X1Z8
V4Y2G5
R4G6N7
D8L2E0
T1I2K9
M5X4J3
'''

#================================= # Write  a  program  to  print  random  element  of  the  list  ten  times   (Home  work)

a=[25,10.8,'Hyd',True,3+4j,None]
for i in range(10):
	print(choice(a))

'''
(3+4j)
Hyd
None
None
Hyd
(3+4j)
Hyd
(3+4j)
Hyd
True
'''

#================================= # Write  a  program  to  generate  ten  six-digit  OTP's  (Home  work)
from random import *
for i in range(10):
    b=''
    for j in range(1,7):
        val=str(randint(0,9))
        b=b+val
    print(b)

'''
853022
968221
628323
440961
505994
766444
540231
710761
097509
392519
'''
#=================================
'''

Write  a  program to  open  any  website  from  gmail ,  google ,  rediff ,  ...   with  a  time  gap  of  5  to  20   sec

1) What  does  open('http://google.com')  do ?  ---> Opens  google.com  website

2) Where  is  open()  function  defined  ?  ---> In  webbrowser  module

3) list = ['google.com' , 'rediff.com' , 'gmail.com' , 'amazon.com' , 'netflix.com']

4) Provide  a  time  gap  of  5  to  20 sec  between  the  websites
'''
from random import *
import webbrowser
import time
list=['google.com','youtube.com','gmail.com','amazon.com','flipkart.com']
while True:
   site=choice(list)
   webbrowser.open(f'http://{site}')
   sec=randint(5,10)
   time.sleep(sec)

#=================================

'''

(Home  work)
Write  a  program  to  implement  Rock , paper  and  scissors  game  between  user  and  computer

1) What  is  the  result  if  user  input  and  computer  random  number  are  same  ?  ---> Draw

2) What  is  the  result  if  computer  selects  paper  and  user  input  is  rock ?  --->
																												Computer  wins  becoz  parer  dominates  rock

3) What  is  the  result  if  computer  selects  scissors  and  user  input  is  paper ?  --->
																										Computer  wins  becoz  scissors  dominates  paper

4) What  is  the  result  if  computer  selects  rock  and  user  input  is  scissors ?  --->
																										Computer  wins  becoz  rock  dominates  scissors

5) What  is  the  result  in  all  other  cases  ?  --->  User  wins
'''
from random import *
def rps():
    user=int(input('What  do  you  want  to  select  (1 - Rock , 2 - Paper , 3 - Scissors) :'))
    comp=randint(1,3)
    a={1:'Rock',2:'Paper',3:'scissors'}
    print(f'user : {a[user]}')
    print(f'computer : {a[comp]}')
    if comp==1 and user==3 or comp==2 and user==1 or comp==3 and user==2 :
        print(f'Compter wins becoz {a[comp]} dominates {a[user]}')
    elif comp==user:
        print('Draw')
    else:
        print(f'User wins becoz {a[user]} dominates {a[comp]}')


rps()
again=input('Continue  (  y / n) : ')
while again=='y':
    rps()
    again=input('Continue  (  y / n)  : ')




#=================================
'''


What  do  you  want  to  select  (0 - Rock , 1 - Paper , 2 - Scissors)  :  1

User  :   Paper
Computer  :   Rock
User  wins
Continue  (  y / n)  ?  y
What  do  you  want  to  select  (0 - Rock , 1 - Paper , 2 - Scissors)  :  2
User  :   Scissors
Computer  :   Scissors
Draw
Continue  (  y / n)  ?  y
What  do  you  want  to  select  (0 - Rock , 1 - Paper , 2 - Scissors)  :  0
User  :   Rock
Computer  :   Rock
Draw
Continue  (  y / n)  ?  y
What  do  you  want  to  select  (0 - Rock , 1 - Paper , 2 - Scissors)  :  1
User  :   Paper
Computer  :   Scissors
Computer  wins
Continue  (  y / n)  ?  n
End  of  the  game
'''