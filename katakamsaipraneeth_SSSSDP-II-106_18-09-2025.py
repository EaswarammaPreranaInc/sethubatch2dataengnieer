#  Find  outputs  (Home  work)
import  sys , time , math
print(dir(sys)) # prints list of all sys members and environment  variables 
print()
print()
print(dir(time)) # prints list of all time members and environment  variables
print()
print(dir(math)) # prints list of all math members and environment  variables


#  Find  outputs  (Home  work)
import  cal
print(dir(cal)) # prints list of all cal members and environment  variables


#  Find  outputs  (Home  work)
x = 25
def  disp():
	print('Hello')
class  c1:
        def  m1(self):
                pass
print(dir()) # list of all dir members
print(type(dir())) # <class 'list'>
print(type(dir)) # error


'''
Write  a  program  to  print  all  the  members  of  cal  module  without  environment  variables

1) What  is  the  result  of  '_name' . startswith('_')  ?  ---> True

2) What  is  the  result  of  '_spec' . endswith('_')  ?  --->  True

3) What  is  the  result  of  'spec_' . startswith('_')  ?  ---> False

4) a = []
    Append  all  the  elements  of  list  returned  by  dir()  function  to  list  'a'  except  environment  variables
'''
import cal 

a = []

dir = dir(cal)

for i in dir:
    if i.startswith('__') and i.endswith('__'):
        continue
    else:
        a.append(i)
print(a)


#  Find  outputs
print(dir()) # ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', 			'__package__', '__spec__']
print() # new line
import  cal # importing module
print() # new line
print(dir()) # ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 		'add', 'c1', 'div', 'mul', 'sub', 'x', 'y']


#  Find  outputs
print(dir()) # ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', 			'__package__', '__spec__']
print() # new line
from  cal  import  * # importing all cal fun members
print() # new line
print(dir()) # ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', 			'__package__', '__spec__', 'add', 'c1', 'div', 'mul', 'sub', 'x', 'y']


#  Find  outputs
print(dir()) # ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', 			'__package__', '__spec__']
print() # new line 
from  cal  import  add , mul , x # importing cal fun mebers add , mul, x
print() # new line
print(dir()) # ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__',  			'__package__', '__spec__', 'add', 'mul', 'x']


# sys . path  demo   program
import  sys # importing sys module
print('Original  sys.path') # Original  sys.path
for  x  in   sys . path:
	print(x) # prints all the elements all sys module
print(len(sys . path)) # len of sys module
#import  cal


# Store  sample.py  module  in  c:\\sairam  folder  before  the  program  is  executed  (Home  work)
print(sys.path) # How  to  print  number  of  directories  (or)  folders  in  sys.path
sys.path.append('c:\sairam') # How  to  append  c:\sairam  folder  to  sys.path
print(sys.path) # How  to  print  number  of  directories  (or)  folders  in  sys.path
print(c:\sairam.x) # How  to  print  object  'x'  of  sample   module  which  is  in  c:\sairam  folder
c:\sairam.f1() # How  to  call   function  f1()  of  sample  module  which  is  in  c:\sairam  folder
a = c:\sairam.c1() # How  to  call   method  m1()  of  class  c1  of  sample  module  which  is  in  c:\sairam  folder
a.m1()


from  random  import  *
print(random()) # prints random number exclusing 0 to 1
print(randint(1 , 100)) # prints random number between 1,100
print(uniform(1 , 100)) # gives float random number
print(randrange(10)) # gives int random num 
print(randrange(1 , 11)) # gives 1 to 10 anyone random number
print(randrange(1 , 11 , 2)) # gives random num b/w 1 to 11 in steps of 2
list = [10 , 20 , 15 , 12 , 18] # list obj
print(choice(list)) # picks anyone random number from list
print(choice('RAJESH')) #picks anyone random number from string 
set  =  {10 , 20 , 30 , 40} # set obj
print(choice(set)) # error


# Write  a  program  to  print  random  character  of  the  string  10  times (Home  work)
######### program ###########
from random import * 
a = input()

for i in range(1,11):
    print(choice(a))

Enter  any  string :  Rama Rao
R

a
R
R
a
R
R
m


Write  a  program to  generate  10  passwords  each  of  6 character  length  where
1st , 3rd , 5th  characters  are  alphabets  and  2nd , 4th , 6th  characters   are  digits

########### program ############3
from random import * 

for i in range(10):
    for j in range(6):
        if j%2==0:
            print(chr(randrange(65,91)), end = "")
        else:
            print(randint(0, 9),end = "")
    print()

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


# Write  a  program  to  print  random  element  of  the  list  ten  times   (Home  work)

########## program #############
from random import *
a = eval(input('-->'))
for i in range(10):
    print(choice(a))

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


# Write  a  program  to  generate  ten  six-digit  OTP's  (Home  work)
######### program ###########
from random import *
for i in range(10):
    for j in range(6):
        print(randint(0, 9),end = "")
    print()


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

'''
Write  a  program to  open  any  website  from  gmail ,  google ,  rediff ,  ...   with  a  time  gap  of  5  to  20   sec

1) What  does  open('http://google.com')  do ?  ---> Opens  google.com  website

2) Where  is  open()  function  defined  ?  ---> In  webbrowser  module

3) list = ['google.com' , 'rediff.com' , 'gmail.com' , 'amazon.com' , 'netflix.com']

4) Provide  a  time  gap  of  5  to  20 sec  between  the  websites
'''
######## program ##########33
import time 
from random import *
from webbrowser import *

list = ['http://google.com' , 'http://rediff.com' , 'http://gmail.com' , 'http://amazon.com' , 'http://netflix.com']
for i in range(len(list)):
    print(open(choice(list)))
    time.sleep(randint(5,20))



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
############### program #############
from random import *
while True:
    a = int(input('What  do  you  want  to  select  (0 - Rock , 1 - Paper , 2 - Scissors) :'))
    b = ['Rock','Paper','Scissors']
    print('User:',b[a])
    c = choice(b)
    print('Computer:',c)
    if (c == 'Scissors' and a == 1) or (c == 'Paper' and a == 0) or (c == 'Rock' and a == 2):
        print("Computer win")
    elif (c == 'Scissors' and a == 2) or (c == 'Paper' and a == 1) or (c == 'Rock' and a == 0):
        print("Draw")
    else:
        print("User win")
    d = input('Continue  (  y / n)  ? ')
    if d == 'y':
        continue
    elif d == 'n':
        print('End of the game')
        break

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