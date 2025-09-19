
#  Find  outputs  (Home  work)
import  sys , time , math
print(dir(sys)) #list of elements in sys
print()
print()
print(dir(time)) #list of elements in time 
print()
print(dir(math)) #list of elements in math 


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
      

#  Find  outputs  (Home  work)
import  cal
print(dir(cal)) #['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'add', 'c1', 'div', 'mul', 'sub', 'x', 'y']#  Find  outputs  (Home  work)
x = 25
def  disp():
	print('Hello')
class  c1:
        def  m1(self):
                pass
print(dir()) #['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'c1', 'disp', 'x']
print(type(dir())) #<class 'list'>
print(type(dir))    #<class 'builtin_function_or_method'>


'''
Write  a  program  to  print  all  the  members  of  cal  module  without  environment  variables

1) What  is  the  result  of  '_name' . startswith('_')  ?  ---> True

2) What  is  the  result  of  '_spec' . endswith('_')  ?  --->  True

3) What  is  the  result  of  'spec_' . startswith('_')  ?  ---> False

4) a = []
    Append  all  the  elements  of  list  returned  by  dir()  function  to  list  'a'  except  environment  variables
'''
import  cal
a = []
for item in dir(cal):
    if not item.startswith('__'):
        a.append(item)
print(a) 

#  Find  outputs
print(dir()) #['_', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'a', 'cal']
print()
import  cal
print()
print(dir()) #['_', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'a', 'cal']#  Find  outputs
print(dir())   #['_dh', '__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__']
print()
from  cal  import  *
print()
print(dir()) # ['_dh', '__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'add', 'c1', 'div', 'mul', 'sub', 'x', 'y']#  Find  outputs
print(dir()) #['_', '__build_class__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'a', 'item']
print()
from  cal  import  add , mul , x
print()
print(dir()) #['_', '__build_class__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'a', 'add', 'item', 'mul', 'x'] # sys . path  demo   program
import  sys
print('Original  sys.path')
for  x  in   sys . path:
	print(x)  #elements of sys list
print(len(sys . path)) #len of sys

#import  calfrom  random  import  *
print(random()) #any random no between 0-1 
print(randint(1 , 100)) #any random int no between 0-1 
print(uniform(1 , 100)) #any random float no between 0-1 
print(randrange(10)) #any random no from 0 to 9 
print(randrange(1 , 11))  #any random no from 1 to 10
print(randrange(1 , 11 , 2))  #any random no from 1 to 10 in steps of 2
list = [10 , 20 , 15 , 12 , 18]
print(choice(list)) #any elements in list
print(choice('RAJESH')) #any char form string
set  =  {10 , 20 , 30 , 40}
print(choice(set)) #error any sequence except set and dict


# Write  a  program  to  print  random  character  of  the  string  10  times (Home  work)
from random import *
a=input("enter any string")
for i in range(10):
    print(choice(a))



'''Write  a  program to  generate  10  passwords  each  of  6 character  length  where
1st , 3rd , 5th  characters  are  alphabets  and  2nd , 4th , 6th  characters   are  digits'''
from random import *
a=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
b=['1','2','3','4','5','6','7','8','9','0']
for i in range(10):
    c=''
    for i in range(3):
        c+=choice(a)
        c+=choice(b)
    print(c)



# Write  a  program  to  print  random  element  of  the  list  ten  times   (Home  work)
from random import *
a=eval(input('enter list: '))
for i in range(10):
    print(choice(a))



# Write  a  program  to  generate  ten  six-digit  OTP's  (Home  work)
from random import *
b=['1','2','3','4','5','6','7','8','9','0']
for i in range(10):
    c=''
    for j in range(6):
        c+=choice(b)
    print(c)




'''
Write  a  program to  open  any  website  from  gmail ,  google ,  rediff ,  ...   with  a  time  gap  of  5  to  20   sec

1) What  does  open('http://google.com')  do ?  ---> Opens  google.com  website

2) Where  is  open()  function  defined  ?  ---> In  webbrowser  module

3) list = ['google.com' , 'rediff.com' , 'gmail.com' , 'amazon.com' , 'netflix.com']

4) Provide  a  time  gap  of  5  to  20 sec  between  the  websites
'''
import time
from random import *
from webbrowser import open
list = ['google.com' , 'rediff.com' , 'gmail.com' , 'amazon.com' , 'netflix.com']
while True:
    open(choice(list))
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
a2=[1,2,3]
a1=['Rock','Paper','Scissors']
b=True
while b:
    c=int(input("What  do  you  want  to  select  (1 - Rock , 2 - Paper , 3 - Scissors)  :"))
    while c>3 or c<1:
        c=int(input("What  do  you  want  to  select  (1 - Rock , 2 - Paper , 3 - Scissors)  :"))
    user=a1[c-1]
    print("user : ",user)
    d=choice(a1)
    print("Computer  :   ",d)
    if user==d:
        print('Draw')
    if d=='Rock' and user=='Scissors' or d=='Paper' and user=='Rock' or d=='Scissors' and user=='Paper':
        print('Computer wins')
    else:
        print("user wins")
    again=input('Continue  (  y / n) ?')
    while again!='y' and  again!='n':
        again=input('Continue  (  y / n) ?')
    if again=='n':
        b=False
print('End of the game')


