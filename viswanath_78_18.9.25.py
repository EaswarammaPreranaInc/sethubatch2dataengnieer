import sys, time, math
print(dir(sys))  # ['argv', 'base_exec_prefix', 'base_prefix', 'breakpointhook', 'builtin_module_names', 'byteorder', 'call_tracing', ... , 'version_info', 'warnoptions']
print()   # prints an empty line
print()   # prints an empty line
print(dir(time))  # ['altzone', 'asctime', 'clock', 'clock_getres', 'clock_gettime', 'clock_gettime_ns', 'clock_settime', ... , 'tzname']
print()   # prints an empty line
print(dir(math))  # ['acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'comb', ... , 'trunc']

import  cal
print(dir(cal))  # ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'add', 'c1', 'div', 'mul', 'sub', 'x', 'y']

x = 25
def  disp():
	print('Hello')
class  c1:
        def  m1(self):
                pass
print(dir())  # ['__annotations__', '__builtins__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'c1', 'disp', 'x']
print(type(dir()))  # <class 'list'>
print(type(dir))  #<class 'builtin_function_or_method'>

q)Write  a  program  to  print  all  the  members  of  cal  module  without  environment  variables
ans) import cal 
a = []  
for x in dir(cal):
    if not x.startswith('__'):  
        a.append(x)
print(a)

print(dir())  #['__annotations__', '__builtins__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']
print()  # prints an empty line
import  cal
print()  # prints an empty line
print(dir())  # ['__annotations__', '__builtins__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'cal']


print(dir())  # ['__annotations__', '__builtins__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']
print()  # prints an empty line
from  cal  import  *
print()  # prints an empty line
print(dir())  # ['__annotations__', '__builtins__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'add', 'c1', 'div', 'mul', 'sub', 'x', 'y']

print(dir())  # ['__annotations__', '__builtins__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']
print()  # prints an empty line
from  cal  import  add , mul , x
print()  # prints an empty line
print(dir())  # ['__annotations__', '__builtins__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'add', 'mul', 'x']

# sys . path  demo   program
import sys
print('Original sys.path')  # Original sys.path
for x in sys.path:  
    print(x) # C:\Users\<username>\AppData\Local\Programs\Python\Python310\Lib\site-packages
# C:\Users\<username>\AppData\Local\Programs\Python\Python310\Lib
# C:\Users\<username>\AppData\Local\Programs\Python\Python310
# ... (other paths in sys.path)
print(len(sys.path))  # 6 

# Store  sample.py  module  in  c:\\sairam  folder  before  the  program  is  executed  
(Home  work)
print(len(sys.path))  #How  to  print  number  of  directories  (or)  folders  in  sys.path
sys.path.append('c:\\sairam')  #How  to  append  c:\sairam  folder  to  sys.path
print(len(sys.path))  # How  to  print  number  of  directories  (or)  folders  in  sys.path
import sample
print(sample.x)  # How  to  print  object  'x'  of  sample   module  which  is  in  c:\sairam  folder
sample.f1()  # How  to  call   function  f1()  of  sample  module  which  is  in  c:\sairam  folder
obj = sample.c1()
obj.m1()  # How  to  call   method  m1()  of  class  c1  of  sample  module  which  is  in  c:\sairam  folder

from random import *
print(random())  # 0.375 random float between 0 and 1 (exclusive)
print(randint(1, 100))  # 57 random int between 1 and 100 (inclusive)
print(uniform(1, 100))  # 42.783914 random float between 1 and 100
print(randrange(10))  # 7  random integer from 0 to 9

print(randrange(1, 11))  # 3 random integer from 1 to 10
print(randrange(1, 11, 2))  # 9  random odd number between 1 and 10
list = [10, 20, 15, 12, 18]  
print(choice(list))  # 12 random element from list
print(choice('RAJESH'))  # 'J' random character from string
set_ = {10, 20, 30, 40}  # avoid using reserved word 'set'
print(choice(list(set_)))  # 30  random element from set converted to list

q) Write  a  program  to  print  random  character  of  the  string  10  times
ans) from random import *
a = eval(input('Enter the sequence : '))
count = 0
while count<10:
    print(choice(a))
    count += 1

q) Write  a  program to  generate  10  passwords  each  of  6 character  length  where
1st , 3rd , 5th  characters  are  alphabets  and  2nd , 4th , 6th  characters   are  digits
Ans) from random import choice, randint
import string
for _ in range(10):  
    pwd = ''
    for i in range(6):
        if i % 2 == 0:  
            pwd += choice(string.ascii_letters)
        else:           
            pwd += str(randint(0, 9))
    print(pwd)

q) Write  a  program  to  print  random  element  of  the  list  ten  times
Ans) from random import *
print("10 six digit otp's")
for i in range(10):
    for j in range(6):
        print(randint(0,9),end='')
    print()   

q) Write  a  program to  open  any  website  from  gmail ,  google ,  rediff ,  ...   with  a  time  gap  of  5  to  20   sec
Ans) import time
import webbrowser 
from random import *
list = ['google.com' , 'rediff.com' , 'gmail.com' , 'amazon.com' , 'netflix.com']
for x in list:
    webbrowser.open(x)
    time.sleep(randint(5,20))

q) Write  a  program  to  implement  Rock , paper  and  scissors  game  between  user  and  computer
Ans) from random import randint
options = ['Rock', 'Paper', 'Scissors']
while True:
    user_input = int(input("What do you want to select (0 - Rock, 1 - Paper, 2 - Scissors): "))
    user_choice = options[user_input]
    print("User  :", user_choice)
      comp_input = randint(0, 2)
    comp_choice = options[comp_input]
    print("Computer  :", comp_choice)
        if user_input == comp_input:
        print("Draw")
    elif (comp_choice == 'Paper' and user_choice == 'Rock') or \
         (comp_choice == 'Scissors' and user_choice == 'Paper') or \
         (comp_choice == 'Rock' and user_choice == 'Scissors'):
        print("Computer wins")
    else:
        print("User wins")
       cont = input("Continue (y/n)? ")
    if cont.lower() != 'y':
        print("End of the game")
        break
