# cal.py
def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    return a / b
class c1:
    def m1(self):
        pass
x = 100
y = 200
if __name__ == '__main__':
    print('Hyd')# Hyd
    print('Sec')# Sec
    print('Cyb')# Cyb

# Find outputs (Home work)
import sys, time, math
print(dir(sys))# List of names in sys module
print()
print()
print(dir(time))# List of names in time module
print()
print(dir(math))# List of names in math module


#  Find  outputs
import cal
print(dir(cal))# List of names in cal module (including add, sub, mul, div, c1, x, y, etc.)


#  Find  outputs
x = 25
def disp():
    print('Hello')
class c1:
    def m1(self):
        pass
print(dir())             # Current module symbols: ['__builtins__', '__name__', ...,'x', 'disp', 'c1']
print(type(dir()))       # <class 'list'>
print(type(dir))         # <class 'builtin_function_or_method'>

'''
Write  a  program  to  print  all  the  members  of  cal  module  without  environment  variables

1) What  is  the  result  of  '_name' . startswith('_')  ?  ---> True

2) What  is  the  result  of  '_spec' . endswith('_')  ?  --->  True

3) What  is  the  result  of  'spec_' . startswith('_')  ?  ---> False

4) a = []
    Append  all  the  elements  of  list  returned  by  dir()  function  to  list  'a'  except  environment  variables
'''
import cal
a = [name for name in dir(cal) if not (name.startswith('_') or name.endswith('_'))]
print(a)# Prints only names that are not env vars


#  Find  outputs
print(dir())# current module names
print()
import cal
print()
print(dir())# names after import cal


#  Find  outputs
print(dir())# names in current namespace
print()
from cal import *
print()
print(dir())# Now cal's members like add, mul, x are shown in the namespace


#  Find  outputs
print(dir())# names in current namespace
print()
from cal import add, mul, x
print()
print(dir())# Only add, mul, x added to namespace

# sys.path demo program
import sys
print('Original sys.path')
for x in sys.path:
    print(x)
print(len(sys.path))     # Number of entries in sys.path

# To use sample.py in c:\sairam folder:
import sys
print(len(sys.path))# Number of folders
sys.path.append(r"c:\sairam")# Append c:\sairam to sys.path
print(len(sys.path))# Number increases by 1
import sample
print(sample.x)# Prints x from sample.py
sample.f1()# Calls f1() function from sample.py
obj = sample.c1()
obj.m1()# Calls m1() method of class c1 of sample.py

from random import *
print(random())# Random float between 0 and 1
print(randint(1, 100))# Random integer between 1 and 100
print(uniform(1, 100))# Random float between 1 and 100
print(randrange(10))# Random integer 0-9
print(randrange(1, 11))# Random integer 1-10
print(randrange(1, 11, 2)) # Random odd number 1-10
list = [10, 20, 15, 12, 18]
print(choice(list))# Random element from list
print(choice('RAJESH'))# Random character from 'RAJESH'
set = {10, 20, 30, 40}
print(choice(list(set)))# Random element from set (convert set to list)


# Write  a  program  to  print  random  character  of  the  string  10  times (Home  work)
from random import choice
s = "Rama Rao"
for _ in range(10):
    print(choice(s))



'''Write  a  program to  generate  10  passwords  each  of  6 character  length  where
1st , 3rd , 5th  characters  are  alphabets  and  2nd , 4th , 6th  characters   are  digits'''
from random import choice
import string
for _ in range(10):
    pwd = ''
    for i in range(6):
        if i % 2 == 0:
            pwd += choice(string.ascii_letters)
        else:
            pwd += choice(string.digits)
    print(pwd)



# Write  a  program  to  print  random  element  of  the  list  ten  times   (Home  work)
from random import choice
lst = [25, 10.8, 'Hyd', True, 3+4j, None]
for _ in range(10):
    print(choice(lst))


# Write  a  program  to  generate  ten  six-digit  OTP's  (Home  work)
from random import randint
for _ in range(10):
    print(randint(100000, 999999))


# Open websites with random delay between 5 and 20 sec
'''
Write  a  program to  open  any  website  from  gmail ,  google ,  rediff ,  ...   with  a  time  gap  of  5  to  20   sec

1) What  does  open('http://google.com')  do ?  ---> Opens  google.com  website

2) Where  is  open()  function  defined  ?  ---> In  webbrowser  module

3) list = ['google.com' , 'rediff.com' , 'gmail.com' , 'amazon.com' , 'netflix.com']

4) Provide  a  time  gap  of  5  to  20 sec  between  the  websites
'''
import webbrowser, time, random
sites = ['http://google.com', 'http://rediff.com', 'http://gmail.com', 'http://amazon.com', 'http://netflix.com']
for site in sites:
    webbrowser.open(site)
    time.sleep(random.randint(5, 20))



# Rock, paper, scissors game
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
import random
options = ['Rock', 'Paper', 'Scissors']
while True:
    user = int(input("What do you want to select (0 - Rock, 1 - Paper, 2 - Scissors) : "))
    print('User :  ', options[user])
    comp = random.randint(0, 2)
    print('Computer :  ', options[comp])
    if user == comp:
        print('Draw')
    elif (comp == 1 and user == 0) or (comp == 2 and user == 1) or (comp == 0 and user == 2):
        print('Computer wins')
    else:
        print('User wins')
    ch = input('Continue (  y / n)  ? ')
    if ch != 'y':
        print('End of the game')
        break
