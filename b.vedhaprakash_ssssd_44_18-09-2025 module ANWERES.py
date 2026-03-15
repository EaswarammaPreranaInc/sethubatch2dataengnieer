# home works 18/09/2025

------------------------------------------------------------------------
# cal.py
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
1) What  is  the  module  name ?  --->  cal

2) py  cal.py
    What  is  the  value  of  __name__ ?  ---> '__main__'
    What  are  the  outputs ?  --->  Hyd ,  Sec  and  Cyb  becoz  if  condition  is  True

3) import  cal
    What  is  the  value  of  __name__ ?  ---> The  imported  module  name  i.e. 'cal'
	What  are  the  outputs ?  ---> Nothing  becoz  if  condition  is   False
'''
## outputs 

Hyd
Sec
Cyb

--------------------------------------------------------------------------
#  Find  outputs  (Home  work)
import  sys , time , math
print(dir(sys))
print()
print()
print(dir(time))
print()
print(dir(math))


#####
outputs

dir() returns all names (attributes, functions, classes, variables) defined inside that module 

sys , time ,math are the standard python modulus 
-------------------------------------------------------------------
#  Find  outputs  (Home  work)
import  cal
print(dir(cal))

# outputs 

since we have written the import cal , so we import the whole 4 function and 1 class , 2 variables , and the default attributes of every module 

['__builtins__', '__cached__', '__doc__', '__file__', '__loader__',
 '__name__', '__package__', '__spec__',
 'add', 'c1', 'div', 'mul', 'sub', 'x', 'y']

----------------------------------------------------------------------
#  Find  outputs  (Home  work)
x = 25
def  disp():
	print('Hello')
class  c1:
        def  m1(self):
                pass
print(dir())
print(type(dir()))
print(type(dir))

#outputs 

['__annotations__', '__builtins__', '__doc__', '__loader__',
 '__name__', '__package__', '__spec__', 'c1', 'disp', 'x']
<class 'list'>
<class 'builtin_function_or_method'>

-----------------------------------------------------------------------
'''
Write  a  program  to  print  all  the  members  of  cal  module  without  environment  variables

1) What  is  the  result  of  '__name__' . startswith('__')  ?  ---> True

2) What  is  the  result  of  '__spec__' . endswith('__')  ?  --->  True

3) What  is  the  result  of  'spec__' . startswith('__')  ?  ---> False

4) a = []
    Append  all  the  elements  of  list  returned  by  dir()  function  to  list  'a'  except  environment  variables
'''

# outputs 

import cal 
a=[]
for name in dir(cal):
	if not (name.startswith('__') and name.endswith('__')):
	a.append(name)
print(a)
------------------------------------------------------------------------
#  Find  outputs
print(dir())
print()
import  cal
print()
print(dir())


#outputs 

['__annotations__', '__builtins__', '__doc__', '__loader__',
 '__name__', '__package__', '__spec__']

['__annotations__', '__builtins__', '__doc__', '__loader__',
 '__name__', '__package__', '__spec__', 'cal']

-----------------------------------------------------------------
#  Find  outputs
print(dir())
print()
from  cal  import  *
print()
print(dir())

#outputs

['__annotations__', '__builtins__', '__doc__', '__loader__',
 '__name__', '__package__', '__spec__']

['__annotations__', '__builtins__', '__doc__', '__loader__',
 '__name__', '__package__', '__spec__',
 'add', 'c1', 'div', 'mul', 'sub', 'x', 'y']

-------------------------------------------------------------
#  Find  outputs
print(dir())
print()
from  cal  import  add , mul , x
print()
print(dir())


#outputs 

['__annotations__', '__builtins__', '__doc__', '__loader__',
 '__name__', '__package__', '__spec__']

['__annotations__', '__builtins__', '__doc__', '__loader__',
 '__name__', '__package__', '__spec__', 'add', 'mul', 'x']

---------------------------------------------------------------------------
# sys . path  demo   program
import  sys
print('Original  sys.path')
for  x  in   sys . path:
	print(x)
print(len(sys . path))
#import  cal

#outputs 
"Original sys.path"
A list of directories line by line (varies by system).
The length of that list
----------------------------------------------------------
# Store  sample.py  module  in  c:\\sairam  folder  before  the  program  is  executed  (Home  work)
How  to  print  number  of  directories  (or)  folders  in  sys.path
How  to  append  c:\sairam  folder  to  sys.path
How  to  print  number  of  directories  (or)  folders  in  sys.path
How  to  print  object  'x'  of  sample   module  which  is  in  c:\sairam  folder
How  to  call   function  f1()  of  sample  module  which  is  in  c:\sairam  folder
How  to  call   method  m1()  of  class  c1  of  sample  module  which  is  in  c:\sairam  folder

#outputs 
import sys

# 1. Print number of directories in sys.path
print(len(sys.path))

# 2. Append c:\sairam folder to sys.path
sys.path.append("c:\\sairam")

# 3. Print number of directories again
print(len(sys.path))

# 4. Import sample module
import sample

# 5. Print object x from sample
print(sample.x)

# 6. Call function f1() from sample
sample.f1()

# 7. Call method m1() of class c1 from sample
obj = sample.c1()
obj.m1()

-------------------------------------------------
from  random  import  *
print(random()) # 0.3748294723
print(randint(1 , 100)) # 57
print(uniform(1 , 100)) # 82.54637291
print(randrange(10)) # 6
print(randrange(1 , 11)) # 4
print(randrange(1 , 11 , 2)) #7
list = [10 , 20 , 15 , 12 , 18] # 12 
print(choice(list)) #12
print(choice('RAJESH')) #A
set  =  {10 , 20 , 30 , 40}
print(choice(set)) # 30

#outputs
0.3748294723
57
82.54637291
6
4
7
12
A
30

--------------------------------------------------------------

# Write  a  program  to  print  random  character  of  the  string  10  times (Home  work)
Enter  any  string :  Rama Rao
R

a
R
R
a
R
R
m
#outputs 
import random

s = input("Enter any string: ")   # take string input
for i in range(10):               # run exactly 10 times
    print(random.choice(s))       # pick a random character

-----------------------------------------------------------

Write  a  program to  generate  10  passwords  each  of  6 character  length  where
1st , 3rd , 5th  characters  are  alphabets  and  2nd , 4th , 6th  characters   are  digits
U7U2X8
V9I6X8
G4M8S2
M4U3C3
I7K2B8
F0E9Q1
Y8H8L7
K1U5S0
W7G0J3
Y9B9J6

#outputs

import random
import string

# Generate 10 passwords
for _ in range(10):
    password = ""
    for i in range(1, 7):  # 6 characters
        if i % 2 == 0:   # 2nd, 4th, 6th → digits
            password += random.choice(string.digits)
        else:            # 1st, 3rd, 5th → alphabets
            password += random.choice(string.ascii_uppercase)  # uppercase only
    print(password)



--------------------------------------------------------------
# Write  a  program  to  print  random  element  of  the  list  ten  times   (Home  work)

Enter a List : [25,10.8,'Hyd',True,3+4j,None]
True
Hyd
Hyd
None
Hyd
(3+4j)
None
True
25
10.8

#outputs
import random

# Take input from user
lst = eval(input("Enter a List : "))

# Print random element 10 times
for i in range(10):
    print(random.choice(lst))
-------------
Enter a List : [25,10.8,'Hyd',True,3+4j,None]
True
Hyd
Hyd
None
Hyd
(3+4j)
None
True
25
10.8


-----------------------------------------------------------------
# Write  a  program  to  generate  ten  six-digit  OTP's  (Home  work)

700690
664735
472299
820818
886311
912752
323114
971162
930848
404338

#OUTPUTS 
import random

# Generate 10 OTPs
for i in range(10):
    otp = random.randint(100000, 999999)  # ensures 6-digit number
    print(otp)

------------------------------------------------------------
'''
Write  a  program to  open  any  website  from  gmail ,  google ,  rediff ,  ...   with  a  time  gap  of  5  to  20   sec

1) What  does  open('http://google.com')  do ?  ---> Opens  google.com  website

2) Where  is  open()  function  defined  ?  ---> In  webbrowser  module

3) list = ['google.com' , 'rediff.com' , 'gmail.com' , 'amazon.com' , 'netflix.com']

4) Provide  a  time  gap  of  5  to  20 sec  between  the  websites
'''


#OUTPUTS 
# open_sites_with_random_delay.py
import webbrowser
import random
import time

sites = [
    "https://www.gmail.com",
    "https://www.google.com",
    "https://www.rediff.com",
    "https://www.amazon.com",
    "https://www.netflix.com"
]

# How many sites to open (set to len(sites) to do each once,
# or set to a larger number to keep opening random sites)
count = 10

for i in range(count):
    site = random.choice(sites)            # pick a random site
    wait_seconds = random.randint(5, 20)   # random integer seconds between 5 and 20
    print(f"[{i+1}/{count}] Opening: {site}  (waiting {wait_seconds} s before next)")
    webbrowser.open(site)                  # opens the URL in the default web browser
    time.sleep(wait_seconds)

print("Done.")





--------------------------
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
----

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


#OUTPUTS 
# Rock, Paper, Scissors Game
import random

choices = ["Rock", "Paper", "Scissors"]

while True:
    user = int(input("What do you want to select (0 - Rock , 1 - Paper , 2 - Scissors)  :  "))
    print("User  :  ", choices[user])

    comp = random.randint(0, 2)
    print("Computer  :  ", choices[comp])

    # check results
    if user == comp:
        print("Draw")
    elif (comp == 0 and user == 2) or (comp == 1 and user == 0) or (comp == 2 and user == 1):
        print("Computer wins")
    else:
        print("User wins")

    ch = input("Continue  (  y / n)  ?  ")
    if ch.lower() == "n":
        print("End  of  the  game")
        break

------------------------------------------------------
