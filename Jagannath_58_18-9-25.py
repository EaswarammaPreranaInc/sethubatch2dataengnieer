#  Find  outputs  (Home  work)
import  sys , time , math
print(dir(sys))                             ['__displayhook__', '__doc__', ..., 'version', 'version_info', 'warnoptions']
print()
print()
print(dir(time))                            ['__doc__', 'altzone', 'asctime', ..., 'time', 'timezone', 'tzname']
print()
print(dir(math))                            ['__doc__', 'acos', 'asin', 'atan', ..., 'tan', 'tau', 'trunc']

#  Find  outputs  (Home  work)
import  cal
print(dir(cal))                             ['__builtins__', '__cached__', '__doc__', '__file__','__loader__', '__name__', '__package__', '__spec__','add', 'c1', 'div', 'mul', 'sub', 'x', 'y']

#  Find  outputs  (Home  work)
x = 25
def  disp():
	print('Hello')
class  c1:
        def  m1(self):
                pass
print(dir())                            ['__annotations__', '__builtins__', '__doc__', '__loader__','__name__', '__package__', '__spec__', 'c1', 'disp', 'x']
print(type(dir()))                      <class 'list'>
print(type(dir))                        <class 'builtin_function_or_method'>

Write  a  program  to  print  all  the  members  of  cal  module  without  environment  variables
a = []
for name in dir(cal):
    if not name.startswith("__"):
        a.append(name)
print(a)

#  Find  outputs
print(dir())                            ['__annotations__', '__builtins__', '__doc__','__loader__', '__name__', '__package__', '__spec__']
print()
import  cal
print()
print(dir())                           ['__annotations__', '__builtins__', '__doc__','__loader__', '__name__', '__package__', '__spec__','cal']

#  Find  outputs
print(dir())                           ['__annotations__', '__builtins__', '__doc__','__loader__', '__name__', '__package__', '__spec__']
print()
from  cal  import  *
print()
print(dir())                          ['__annotations__', '__builtins__', '__doc__','__loader__', '__name__', '__package__', '__spec__','add', 'c1', 'div', 'mul', 'sub', 'x', 'y']

#  Find  outputs
print(dir())                                         ['__annotations__', '__builtins__', '__doc__','__loader__', '__name__', '__package__', '__spec__']
print()
from  cal  import  add , mul , x
print()
print(dir())                                       ['__annotations__', '__builtins__', '__doc__','__loader__', '__name__', '__package__', '__spec__', 'add', 'mul', 'x']

# sys . path  demo   program
import  sys
print('Original  sys.path')                           Original sys.path
for  x  in   sys . path:
	print(x)                                            C:\Users\YourName\project
                                                      C:\Python312\python312.zip
                                                      C:\Python312\DLLs
                                                      C:\Python312\Lib
                                                      C:\Python312
                                                      C:\Python312\Lib\site-packages
print(len(sys . path))                                6

# Store  sample.py  module  in  c:\\sairam  folder  before  the  program  is  executed  (Home  work)
How  to  print  number  of  directories  (or)  folders  in  sys.path                                                               print("Before:", len(sys.path))
How  to  append  c:\sairam  folder  to  sys.path                                                                                   sys.path.append("C:\\sairam")
How  to  print  number  of  directories  (or)  folders  in  sys.path                                                               print("After:", len(sys.path))                              
How  to  print  object  'x'  of  sample   module  which  is  in  c:\sairam  folder                                                 import sample
                                                                                                                                   print("x =", sample.x)
How  to  call   function  f1()  of  sample  module  which  is  in  c:\sairam  folder                                               sample.f1()
How  to  call   method  m1()  of  class  c1  of  sample  module  which  is  in  c:\sairam  folder                                  obj = sample.c1()
                                                                                                                                   obj.m1()

from  random  import  *
print(random())                                            0.374832
print(randint(1 , 100))                                    57
print(uniform(1 , 100))                                    24.678
print(randrange(10))                                       6
print(randrange(1 , 11))                                   4
print(randrange(1 , 11 , 2))                               7
list = [10 , 20 , 15 , 12 , 18]                            
print(choice(list))                                        15
print(choice('RAJESH'))                                    J
set  =  {10 , 20 , 30 , 40}
print(choice(set))                                         30

 Write  a  program  to  print  random  character  of  the  string  10  times (Home  work)
from random import choice
my_string = "RAJESH"
print("Random characters:")
for i in range(10):
    char = choice(my_string)
    print(char, end=' ')

Write  a  program to  generate  10  passwords  each  of  6 character  length  where
1st , 3rd , 5th  characters  are  alphabets  and  2nd , 4th , 6th  characters   are  digits
import random
import string
n=10
lenght=6
for _ in range(n):
    password = ""
    for i in range(length):
        if i % 2 == 0:  
            password += random.choice(string.ascii_letters)  
        else:           
            password += random.choice(string.digits)        
    print(password)

# Write  a  program  to  print  random  element  of  the  list  ten  times   (Home  work)
from random import choice
my_list = [10, 20, 15, 12, 18]
print("Random elements from the list:")
for _ in range(10):
    elem = choice(my_list)
    print(elem, end=' ')

# Write  a  program  to  generate  ten  six-digit  OTP's  (Home  work)
import random
print("Ten 6-digit OTPs:")
for _ in range(10):
    otp = random.randint(100000, 999999)
    print(otp)

Write  a  program to  open  any  website  from  gmail ,  google ,  rediff ,  ...   with  a  time  gap  of  5  to  20   sec
import webbrowser
import time
import random
websites = [
    "https://www.gmail.com",
    "https://www.google.com",
    "https://www.rediff.com"
]
print("Opening websites with random time gaps...")
for site in websites:
    webbrowser.open(site)  
    delay = random.randint(5, 20)  
    print(f"Waiting for {delay} seconds before opening next site...")
    time.sleep(delay)

Write  a  program  to  implement  Rock , paper  and  scissors  game  between  user  and  computer
import random
choices = ["Rock", "Paper", "Scissors"]
print("Welcome to Rock-Paper-Scissors Game!")
while True:
    user_input = input("What do you want to select (0 - Rock, 1 - Paper, 2 - Scissors) : ")
    if user_input not in ['0', '1', '2']:
        print("Invalid input! Please enter 0, 1, or 2.")
        continue
    user_choice = int(user_input)
    computer_choice = random.randint(0, 2)
    print(f"User  :  {choices[user_choice]}")
    print(f"Computer  :  {choices[computer_choice]}")
    if user_choice == computer_choice:
        print("Draw")
    elif (user_choice == 0 and computer_choice == 2) or (user_choice == 1 and computer_choice == 0) or (user_choice == 2 and computer_choice == 1):
        print("User wins")
    else:
        print("Computer wins")
    cont = input("Continue (y/n)? ").lower()
    if cont != 'y':
        print("End of the game")
        break



