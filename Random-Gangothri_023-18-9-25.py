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
if  __name__ ==  '_main_':
	print('Hyd')
	print('Sec')
	print('Cyb')

#1) What  is  the  module  name ?  --->  cal
#2) py  cal.py
    #What  is  the  value  of  _name_ ?  ---> '__main__'
    #What  are  the  outputs ?  --->  Hyd ,  Sec  and  Cyb  becoz  if  condition  is  True
#3) import  cal
    #What  is  the  value  of  __name__ ?  ---> The  imported  module  name  i.e. 'cal'
	#What  are  the  outputs ?  ---> Nothing  becoz  if  condition  is   False
#  Find  outputs  (Home  work)
import  sys , time , math
print(dir(sys)) # [Environment variables All the members of sys module]
print()
print()
print(dir(time)) # [Environment variables All the members of time module]
print()
print(dir(math)) # [Environment variables All the members of math module]

#  Find  outputs  (Home  work)
import  cal # import cal module
print(dir(cal)) # ['Environment variables', 'add', 'c1', 'div', 'mul', 'sub', 'x', 'y']

#  Find  outputs  (Home  work)
x = 25
def  disp():
	print('Hello')
class  c1:
    def  m1(self):
        pass
print(dir()) # ['Environment variables', 'c1', 'disp', 'x']
print(type(dir())) # <class 'list'>
print(type(dir)) # <class 'builtin_function_or_method'>


# Write  a  program  to  print  all  the  members  of  cal  module  without  environment  variables
#1) What  is  the  result  of  '_name' . startswith('_')  ?  ---> True
#2) What  is  the  result  of  '_spec' . endswith('_')  ?  --->  True
#3) What  is  the  result  of  'spec_' . startswith('_')  ?  ---> False
#4) a = []
#Append  all  the  elements  of  list  returned  by  dir()  function  to  list  'a'  except  environment  variables

import cal
a=[]
for x in dir(cal):
      if not (x.startswith('__') and x.endswith('__')):
           a.append(x)
print(a)

#  Find  outputs
print(dir()) # [Environment variables]
print()
import  cal # 
print()
print(dir()) # ['Environment variables', 'add', 'c1', 'div', 'mul', 'sub', 'x', 'y']

#  Find  outputs
print(dir()) # [Environment variables]
print()
from  cal  import  *
print()
print(dir()) # ['Environment variables', 'add', 'c1', 'div', 'mul', 'sub', 'x', 'y']

#  Find  outputs
print(dir())
print()
from  cal  import  add , mul , x
print()
print(dir()) # [Environment variables,'add','mul','x']

# sys . path  demo   program
import  sys
print('Original  sys.path')
for  x  in   sys.path:
	print(x)
print(len(sys.path))
import  cal # Error-> ModuleotFoundError

# Store  sample.py  module  in  c:\\sairam  folder  before  the  program  is  executed  (Home  work)
import sys
print(len(sys.path)) #How  to  print  number  of  directories  (or)  folders  in  sys.path
sys.path.append('c:\\sairam') # How  to  append  c:\\sairam  folder  to  sys.path
print(len(sys.path)) #How  to  print  number  of  directories  (or)  folders  in  sys.path
import sample
print(sample.x) #How  to  print  object  'x'  of  sample   module  which  is  in  c:\\sairam  folder
sample.f1()  #How  to  call   function  f1()  of  sample  module  which  is  in  c:\\sairam  folder
a=sample.c1() 
a.m1() #How  to  call   method  m1()  of  class  c1  of  sample  module  which  is  in  c:\\sairam  folder

from  random  import  *
print(random()) # any number between 0 and 1,both are not excluded
print(randint(1 , 100)) # any random integer number between 1 included and 100 included
print(uniform(1 , 100)) # Any random float number between 1 and 100 excluded
print(randrange(10)) # Any random integer number between 0 and 9 included
print(randrange(1 , 11)) # Any random integer number between 1 and 10 are includedd
print(randrange(1 , 11 , 2)) # Any random integer number between 1 included and 10 included in steps of 2 
list = [10 , 20 , 15 , 12 , 18]
print(choice(list)) # Any random elemnent of list
print(choice('RAJESH')) # Any random char of string
set  =  {10 , 20 , 30 , 40}
print(choice(set)) # Error set is not indexed

# Write  a  program  to  print  random  character  of  the  string  10  times (Home  work)

import random
try:
	str = input('Enter any string : ')
	for x in range(10):
		print(random.choice(str))
except:
	print('Input can not be empty string')
'''
Output:
Enter  any  string :  Rama Rao
 
a
R
R
m
m
o
a
'''

#Write  a  program to  generate  10  passwords  each  of  6 character  length  where 1st , 3rd , 5th  characters  are  alphabets  and  2nd , 4th , 6th  characters   are  digits
from random import randint
def digit():
	return randint(0,9)
def alpha():
	return chr(randint(65, 90))
for i in range(10):
	print(alpha(), digit(), alpha(), digit(), alpha(), digit(), sep='')
'''
output
X9V6I2
E5V6O7
T0K7P8
H5M8H3
H5A5G9
C6C3M9
W6M4B9
G6A5T1
G7A5H4
N1V8J8
'''
# Write  a  program  to  print  random  element  of  the  list  ten  times   (Home  work)
import random
try:
    list = eval(input('Enter a List: '))
    for x in range(10):
        print(random.choice(list))
except:
    print('Enter atleast one element')

'''Output:
Enter a List: [25,10.8,'Hyd',True,3+4j,None]
25
Hyd
Hyd
None
(3+4j)
25
None
(3+4j)
None
25'''

# Write  a  program  to  generate  ten  six-digit  OTP's  (Home  work)
import random
for x in range(10):
	print(random.randint(100000, 999999))
'''
741567
706473
548507
717616
900337
586279
322370
295359
939602
174297
'''

# Write  a  program to  open  any  website  from  gmail ,  google ,  rediff ,  ...   with  a  time  gap  of  5  to  20   sec
# 1) What  does  open('http://google.com')  do ?  ---> Opens  google.com  website
# 2) Where  is  open()  function  defined  ?  ---> In  webbrowser  module
# 3) list = ['google.com' , 'rediff.com' , 'gmail.com' , 'amazon.com' , 'netflix.com']
# 4) Provide  a  time  gap  of  5  to  20 sec  between  the  websites

from random import *
import webbrowser
import time
list = ['google.com', 'youtube.com', 'gmail.com', 'rediff.com', 'amazon.com', 'bing.com', 'flipkart.com']
while True:
	site = choice(list)
	webbrowser.open(F'http://{site}')
	sec = randint(5, 20)
	time.sleep(sec)

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
from random import choice
list = ['Rock','Paper', 'Scissors']
while True:
	ch = int(input('What do you want to select (0-Rock,1-Paper,2-Scissors):'))
	if ch < 0 or ch > 2:
		print('Invalid Input')
	else:
		user = list[ch]
		comp = choice(list)
		print('User :', user)
		print('Computer : ', comp)
		if user == comp:
			print('Draw')
		elif (comp == 'Paper' and user == 'Rock') or (comp == 'Rock' and user == 'Scissors') or (comp == 'Scissors' and user == 'Paper'):
			print('Computer wins')
		else:
			print('User wins')
		option = input('Continue (y/n) ? ')
		if option == 'n' or option == 'N':
			break
print('End of the game')	