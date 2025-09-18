
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



#  Find  outputs  (Home  work)
import  sys , time , math
print(dir(sys))  #  prints sys module list of names
print()
print()
print(dir(time))  #  prints time module list of names
print()
print(dir(math))  #  prints math module list of names



#  Find  outputs  (Home  work)
import  cal
print(dir(cal))  #  prints list of members of cal module



#  Find  outputs  (Home  work)
x = 25
def  disp():
	print('Hello')
class  c1:
        def  m1(self):
                pass
print(dir())  #  list of names members of current module
print(type(dir()))  #  class list
print(type(dir))  #  class type of method


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
for i in dir(cal):
    if i.startswith('__') and i.endswith('__'):
        pass
    else:
        a.append(i)
print(a)
    


#  Find  outputs
print(dir())  #  ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']
print()
import  cal
print()
print(dir())  #  ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'cal']



#  Find  outputs
print(dir())  #  list of predefined dunder names
print()
from  cal  import  *
print()
print(dir())  #  list of names of predefined +  members of cal module




#  Find  outputs
print(dir())  #  #  list of predefined dunder names
print()
from  cal  import  add , mul , x
print()
print(dir())  #  #  list of predefined dunder names with add,mul,x membrs of cal module



# sys . path  demo   program
import  sys
print('Original  sys.path')  #  Original sys.path
for  x  in   sys . path:
	print(x)  #  prints 7 directories
print(len(sys . path))  #  7
#import  cal



# Store  sample.py  module  in  c:\\sairam  folder  before  the  program  is  executed  (Home  work)
import sys
print(len(sys.path))  #  How  to  print  number  of  directories  (or)  folders  in  sys.path
sys.path.append('c:\\sairam')  #How  to  append  c:\sairam  folder  to  sys.path
print(len(sys.path))  #   How  to  print  number  of  directories  (or)  folders  in  sys.path
import sample
print(sample.x)   #  How  to  print  object  'x'  of  sample   module  which  is  in  c:\sairam  folder
sample.f1()  #  How  to  call   function  f1()  of  sample  module  which  is  in  c:\sairam  folder
o=sample.c1()   #How  to  call   method  m1()  of  class  c1  of  sample  module  which  is  in  c:\sairam  folder
o.m1()



from  random  import  *
print(random())  #  prints float value between 0 and 1
print(randint(1 , 100))  #  random number between 1 and 100
print(uniform(1 , 100))  # random float number between  1  and 100
print(randrange(10))  #  random number between 0 to  9
print(randrange(1 , 11))  #  number between 1 to 10
print(randrange(1 , 11 , 2))  #   between 1 to 10 in steps of 2
list = [10 , 20 , 15 , 12 , 18]
print(choice(list))  #  random element in list
print(choice('RAJESH'))  #  random char from 'RAJESH'
set  =  {10 , 20 , 30 , 40}
print(choice(set))  # Error due to set  not have Choice function



# Write  a  program  to  print  random  character  of  the  string  10  times (Home  work)
from random import * 
import time
a=input("Enter any String : ")
for i in range(10):
    print(choice(a))
    time.sleep(1)



# Write  a  program to  generate  10  passwords  each  of  6 character  length  where
# 1st , 3rd , 5th  characters  are  alphabets  and  2nd , 4th , 6th  characters   are  digits

import time
from random import *
a=[]
for i in range(10):
    b=""
    for k in range(3):
        b+=choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        b+=str(randrange(10))
    a.append(b)
for p in a:
    print(p)
    time.sleep(1)



# Write  a  program  to  print  random  element  of  the  list  ten  times   (Home  work)
from random import *
list=eval(input("Enter a list : "))
for i in range(10):
    print(choice(list))



# Write  a  program  to  generate  ten  six-digit  OTP's  (Home  work)
from random import *
for i in range(10):
    print(randrange(100000,1000000))


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
sites = ['https://www.youtube.com','https://www.google.com','https://www.rediff.com',
         'https://www.gmail.com','https://www.amazon.com','https://www.netflix.com']
while True:
    webbrowser.open(choice(sites))
    time.sleep(8)



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
from random import *
p='y'
while True:
    list={1:'Rock',2:'Paper',3:'Scissors'}
    if p=='y':
        user=int(input("What  do  you  want  to  select  (1 - Rock , 2 - Paper , 3 - Scissors)  :"))
        com=choice(range(1,4))
        if user==com:
            print("Daw")
        elif com==1 and user==3 or com==2 and user==1 or com==3 and user==2:
            print(f"Computer  wins  becoz  {list[com]}  dominates  {list[user]}")
        else:
            print(f"User  wins  becoz  {list[user]}  dominates  {list[com]}")
        k=input("Continue  (  y / n)  ?  ")
        p=k
    else:
        print("End of the game.")
        break


