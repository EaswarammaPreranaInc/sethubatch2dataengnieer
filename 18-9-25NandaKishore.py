#Nanda Kishore Vemula
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
    What  is  the  value  of  _name_ ?  ---> '_main_'
    What  are  the  outputs ?  --->  Hyd ,  Sec  and  Cyb  becoz  if  condition  is  True

3) import  cal
    What  is  the  value  of  _name_ ?  ---> The  imported  module  name  i.e. 'cal'
	What  are  the  outputs ?  ---> Nothing  becoz  if  condition  is   False
'''

 #Find  outputs  (Home  work)
import  sys , time , math
print(dir(sys)) #All the members of sys module and Environment variables
print()
print()
print(dir(time)) #All the members of time module and Environment variables
print()
print(dir(math)) #All the members of math module and Environment variables


#Find  outputs  (Home  work)
import  cal
print(dir(cal)) #['add','sub','mul','div','c1','x','y' and Environment Variables]

#  Find  outputs  (Home  work)
x = 25
def  disp():
	print('Hello')
class  c1:
        def  m1(self):
                pass
print(dir()) #['x','disp','c1' and Environment Variables]
print(type(dir())) #<class 'list'>
print(type(dir)) #<class 'builtins_function_or_method'>

'''
Write  a  program  to  print  all  the  members  of  cal  module  without  environment  variables

1) What  is  the  result  of  '_name' . startswith('_')  ?  ---> True

2) What  is  the  result  of  '_spec' . endswith('_')  ?  --->  True

3) What  is  the  result  of  'spec_' . startswith('_')  ?  ---> False

4) a = []
    Append  all  the  elements  of  list  returned  by  dir()  function  to  list  'a'  except  environment  variables
'''
import cal
a=[]
for x in dir(cal):
    if x.startswith('__') and x.endswith('__'):
        continue
    else:
        a.append(x)
print(a)


#  Find  outputs
print(dir()) #[Environment variables]
print()
import  cal
print()
print(dir()) #[cal and Environment Variables]

#  Find  outputs
print(dir()) #[Environment Variables]
print()
from  cal  import  *
print()
print(dir()) #['add','sub','mul','div','c1','x','y' and Environment Variables]

#  Find  outputs
print(dir()) #[Environment Variables]
print()
from  cal  import  add , mul , x
print()
print(dir()) #['add','mul','x' and Environment Variables]

# sys . path  demo   program
import  sys
print('Original  sys.path') #Original  sys.path
for  x  in   sys . path:
	print(x) #[cwd and 5 other directories]
print(len(sys . path)) #6
#import  cal

# Store  sample.py  module  in  c:\\sairam  folder  before  the  program  is  executed  (Home  work)
print(sys.path)#How  to  print  number  of  directories  (or)  folders  in  sys.path
sys.path.append('c:\\sairam')#How  to  append  c:\sairam  folder  to  sys.path
print(len(sys.path))#How  to  print  number  of  directories  (or)  folders  in  sys.path
import sample
print(sample.x)#How  to  print  object  'x'  of  sample   module  which  is  in  c:\sairam  folder
sample.f1()#How  to  call   function  f1()  of  sample  module  which  is  in  c:\sairam  folder
b=sample.c1()
b.m1()#How  to  call   method  m1()  of  class  c1  of  sample  module  which  is  in  c:\sairam  folder

from  random  import  *
print(random()) # a number b/w 0 and 1 (excluding 0 and 1) 
print(randint(1 , 100)) # a integer number b/w 1 and 100 (including 1 and 100)
print(uniform(1 , 100)) # a float number b/w 1 and 100(including 1 and 100)
print(randrange(10))#a integer number b/w 0 and 9
print(randrange(1 , 11)) # a integer number b/w 1 and 10
print(randrange(1 , 11 , 2))#a integer number b/w 1 and 10 in steps of 2
list = [10 , 20 , 15 , 12 , 18]
print(choice(list)) # a number from the list
print(choice('RAJESH')) # a character from sequence
set  =  {10 , 20 , 30 , 40}
print(choice(set)) #Error

# Write  a  program  to  print  random  character  of  the  string  10  times (Home  work)

from random import *
n=input("Enter a string")
for i in range(10):
    print(choice(n))
    
#Write  a  program to  generate  10  passwords  each  of  6 character  length  where
#1st , 3rd , 5th  characters  are  alphabets  and  2nd , 4th , 6th  characters   are  digits

from random import *
s='QWERTYUIOPLKJHGFDSAZXCVBNM'
D='1234567890'
for j in range(10):
    res=''
    for i in range(1,7):
        if i%2==0:
            res+=choice(D)
        else:
            res+=choice(s)
    print(res)
    
# Write  a  program  to  print  random  element  of  the  list  ten  times   (Home  work)
from random import *
list=eval(input())
for i in range(10):
    print(choice(list))
    
# Write  a  program  to  generate  ten  six-digit  OTP's  (Home  work)
from random import *
for i in range(10):
    for j in range(6):
        print(randint(0,9),end='')
    print()
    
'''
Write  a  program to  open  any  website  from  gmail ,  google ,  rediff ,  ...   with  a  time  gap  of  5  to  20   sec

1) What  does  open('http://google.com')  do ?  ---> Opens  google.com  website

2) Where  is  open()  function  defined  ?  ---> In  webbrowser  module

3) list = ['google.com' , 'rediff.com' , 'gmail.com' , 'amazon.com' , 'netflix.com']

4) Provide  a  time  gap  of  5  to  20 sec  between  the  websites
'''

import time
from random import *
import webbrowser
list = ['google.com' , 'rediff.com' , 'gmail.com' , 'amazon.com' , 'netflix.com']
for x in list:
    webbrowser.open(x)
    time.sleep(5)


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

#Program
from random import *
list=['Rock','Paper','Scissors']
a=True
while a:
    n=int(input("What  do  you  want  to  select  (0 - Rock , 1 - Paper , 2 - Scissors) : "))
    User=list[n]
    Computer=choice(list)
    if Computer=='Paper' and User=='Rock' or Computer=='Scissors' and User=='Paper' or Computer=='Rock' and User=='Scissors':
        print('Computer wins')
    elif Computer==User:
        print('Draw')
    else:
        print('User wins')
    b=input('Continue  (  y / n)  ? ')
    if b=='y':
        continue
    else:
        a=False
print('End of the game')