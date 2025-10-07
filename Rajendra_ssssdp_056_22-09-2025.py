

#  Find  outputs  (Home  work)
import  sys , time , math
print(dir(sys)) 		# Prints all available names inside the sys module.
print()
print()
print(dir(time))    		# Prints all available names inside the time module.
print()
print(dir(math))    		# Prints all available names inside the math module.






#  Find  outputs  (Home  work)
import  cal
print(dir(cal))			#Returns list consisting of all members of module cal

output:-
['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', 
'__spec__', 'add', 'c1', 'div', 'mul', 'sub', 'x', 'y']





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

output:-
['__annotations__', '__builtins__', '__cached__',
 '__doc__', '__file__', '__loader__', '__name__',
 '__package__', '__spec__', 'c1', 'disp', 'x']
<class 'list'>
<class 'builtin_function_or_method'>







Write  a  program  to  print  all  the  members  of  cal  module  without  environment  variables

1) What  is  the  result  of  '_name' . startswith('_')  ?  ---> True
2) What  is  the  result  of  '_spec' . endswith('_')  ?  --->  True
3) What  is  the  result  of  'spec_' . startswith('_')  ?  ---> False
4) a = []
    Append  all  the  elements  of  list  returned  by  dir()  function  to  list  'a'  except  environment  variables


import cal
a=[]
for i in dir(cal):
    if i.startswith('__') and  i.endswith('__'):
        continue
    else:
        a.append(i)
print(a)

output:-
['add', 'c1', 'div', 'mul', 'sub', 'x', 'y']






#  Find  outputs
print(dir())
print()
import  cal
print()
print(dir())

output:-
['__annotations__', '__builtins__', '__cached__', '__doc__', 
'__file__', '__loader__', '__name__', '__package__', '__spec__']


['__annotations__', '__builtins__', '__cached__', '__doc__', 
'__file__', '__loader__', '__name__', '__package__', '__spec__',
 'cal']






#  Find  outputs
print(dir())
print()
from  cal  import  *
print()
print(dir())

output:-
['__annotations__', '__builtins__', '__cached__', '__doc__',
 '__file__', '__loader__', '__name__', '__package__', '__spec__']


['__annotations__', '__builtins__', '__cached__', '__doc__', 
'__file__', '__loader__', '__name__', '__package__', '__spec__',
 'add', 'c1', 'div', 'mul', 'sub', 'x', 'y']






#  Find  outputs
print(dir())
print()
from  cal  import  add , mul , x
print()
print(dir())


output:-
['__annotations__', '__builtins__', '__cached__', '__doc__',
 '__file__', '__loader__', '__name__', '__package__', '__spec__']


['__annotations__', '__builtins__', '__cached__', '__doc__', 
'__file__', '__loader__', '__name__', '__package__', '__spec__',
 'add', 'mul', 'x']







# sys . path  demo   program
import  sys
print('Original  sys.path')
for  x  in   sys . path:
	print(x)
print(len(sys . path))
#import  cal


output:-
Original  sys.path
C:\Users\directory location
C:\Program Files\Python313\python313.zip
C:\Program Files\Python313\DLLs
C:\Program Files\Python313\Lib
C:\Program Files\Python313
C:\Users\raksh\AppData\Roaming\Python\Python313t\site-packages
C:\Program Files\Python313\Lib\site-packages
7 






# Store  sample.py  module  in  c:\\sairam  folder  before  the  program  is  executed  (Home  work)
import sys,sample
print(len(sys.path)) 	#How  to  print  number  of  directories  (or)  folders  in  sys.path
sys.path.append(r'c:\\sairam') #How  to  append  c:\sairam  folder  to  sys.path
print(len(sys.path) #How  to  print  number  of  directories  (or)  folders  in  sys.path
print(sample.x) #How  to  print  object  'x'  of  sample   module  which  is  in  c:\sairam  folder
sample.f1() #How  to  call   function  f1()  of  sample  module  which  is  in  c:\sairam  folder
a=sample.c1()
a.m1() #How  to  call   method  m1()  of  class  c1  of  sample  module  which  is  in  c:\sairam  folder






from  random  import  *
print(random()) 		# 0.6952031344272716
print(randint(1 , 100)) 	# 77
print(uniform(1 , 100)) 	# 88.85025107048679
print(randrange(10))    	# 4
print(randrange(1 , 11))    	# 5
print(randrange(1 , 11 , 2))    # 9
list = [10 , 20 , 15 , 12 , 18]
print(choice(list)) 		# 15
print(choice('RAJESH')) 	# S
set  =  {10 , 20 , 30 , 40}
print(choice(set))  		# Error as Set object is not subscriptable







# Write  a  program  to  print  random  character  of  the  string  10  times (Home  work)

from random import *
import time
s=input('Enter a string : ')
for i in range(10):
    print(choice(s))			#R<next_line> <next_line>a<next_line>R<next_line>R<next_line>a<next_line>R<next_line>R<next_line>m
    time.sleep(1)








Write  a  program to  generate  10  passwords  each  of  6 character  length  where 1st , 3rd , 5th  characters  are  alphabets  and  2nd , 4th , 6th  characters   are  digits

import time
from random import *
a=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
b=['0','1','2','3','4','5','6','7','8','9']
for i in range(10):
    s=choice(a)+choice(b)+choice(a)+choice(b)+choice(a)+choice(b)
    print(s)
    time.sleep(1)








# Write  a  program  to  print  random  element  of  the  list  ten  times   (Home  work)
Enter a List : [25,10.8,'Hyd',True,3+4j,None]
 
from random import *
import time
List=[25,10.8,'Hyd',True,3+4j,None]
for i in range(10):
    print(choice(List))
    time.sleep(2)
    








# Write  a  program  to  generate  ten  six-digit  OTP's  (Home  work)

from random import *
import time
for i in range(10):
    print(randrange(100000,999999))
    time.sleep(2)
  







Write  a  program to  open  any  website  from  gmail ,  google ,  rediff ,  ...   with  a  time  gap  of  5  to  20   sec

1) What  does  open('http://google.com')  do ?  ---> Opens  google.com  website
2) Where  is  open()  function  defined  ?  ---> In  webbrowser  module
3) list = ['google.com' , 'rediff.com' , 'gmail.com' , 'amazon.com' , 'netflix.com']
4) Provide  a  time  gap  of  5  to  20 sec  between  the  websites

import random,time,webbrowser
List=['google.com' , 'rediff.com' , 'gmail.com' , 'amazon.com' , 'netflix.com']
while True:
    a=random.choice(List)
    webbrowser.open(f'http://{a}')
    time.sleep(random.randrange(5,20))






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

from random import *
game='y'
d=['Rock','paper', 'Scissors']
while game=='y':
    u=int(input('What  do  you  want  to  select  (0 - Rock , 1 - Paper , 2 - Scissors)  :  '))
    print('User : ',d[u])
    com=randrange(0,2)
    print('Computer : ',d[com])
    if com==u:
        print('Draw')
    elif (com==1 and u==0) or (com==2 and u==1) or (com==0 and u==2):
        print('Computer Wins')
    else:
        print('User Wins')
    game=input('Continue (y/n) ? ')
print('End of the game')
