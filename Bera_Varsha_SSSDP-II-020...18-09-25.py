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
if  _name_ ==  '_main_':
	print('Hyd')
	print('Sec')
	print('Cyb')
# output:
'''
Hyd
Sec
Cyb
'''


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
print(dir(sys))
print()
print()
print(dir(time))
print()
print(dir(math))
# output:
'''
[environment variables,all the members of sys module]


[environment variables,all the members of time module]

[environment variables,all the members of math module]


'''
#  Find  outputs  (Home  work)
import  cal
print(dir(cal))

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

'''
Write  a  program  to  print  all  the  members  of  cal  module  without  environment  variables

1) What  is  the  result  of  '_name' . startswith('_')  ?  ---> True

2) What  is  the  result  of  '_spec' . endswith('_')  ?  --->  True

3) What  is  the  result  of  'spec_' . startswith('_')  ?  ---> False

4) a = []
    Append  all  the  elements  of  list  returned  by  dir()  function  to  list  'a'  except  environment  variables
'''

import cal
a = []  #  Empty  list
for  x  in  dir(cal) :  #   ['_builtins', 'cached', 'doc', 'file', 'loader', 'name', 'package', 'spec_', 'add', 'c1', 'div', 'mul', 'sub', 'x', 'y']
	if  not  (x . startswith('') and x . endswith('')):
		a . append(x)  #  Appends 'x'  to  list  'a'   if  it  is  not  environment  variable
print(a)  #  ['add', 'c1', 'div', 'mul', 'sub', 'x', 'y']

#  Find  outputs
print(dir())
print()
import  cal
print()
print(dir())
'''
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__']

 
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'cal']

'''

# Find  outputs
print(dir()) #  [Ev's]
print()
from  cal  import  *  #  Imports  all  the  members  of  cal  module  which  become  members  of  current  module
print()
print(dir()) #  [Ev's , 'add' , 'c1', 'div' ,'mul' , 'sub' , 'x' , 'y']

# Find  outputs
print(dir()) #  [Ev's]
print()
from  cal  import  *  #  Imports  all  the  members  of  cal  module  which  become  members  of  current  module
print()
print(dir()) #  [Ev's , 'add' , 'c1', 'div' ,'mul' , 'sub' , 'x' , 'y']

# sys . path  demo   program
import  sys
print('Original  sys.path')
for  x  in   sys . path:
	print(x)
print(len(sys . path))

'''
Original  sys.path
C:\Users\B.Varsha\AppData\Local\Programs\Python\Python311\Lib\idlelib
C:\Users\B.Varsha\AppData\Local\Programs\Python\Python311\python311.zip
C:\Users\B.Varsha\AppData\Local\Programs\Python\Python311\DLLs
C:\Users\B.Varsha\AppData\Local\Programs\Python\Python311\lib
C:\Users\B.Varsha\AppData\Local\Programs\Python\Python311
C:\Users\B.Varsha\AppData\Roaming\Python\Python311\site-packages
C:\Users\B.Varsha\AppData\Roaming\Python\Python311\site-packages\win32
C:\Users\B.Varsha\AppData\Roaming\Python\Python311\site-packages\win32\lib
C:\Users\B.Varsha\AppData\Roaming\Python\Python311\site-packages\Pythonwin
C:\Users\B.Varsha\AppData\Local\Programs\Python\Python311\lib\site-packages
#10

'''
from  random  import  *
print(random())#0.61
print(randint(1 , 100))#40
print(uniform(1 , 100))#96.17
print(randrange(10))#9
print(randrange(1 , 11))#10
print(randrange(1 , 11 , 2))#3
list = [10 , 20 , 15 , 12 , 18]#
print(choice(list))#12
print(choice('RAJESH'))#E
set  =  {10 , 20 , 30 , 40}
print(choice(set))#TypeError: 'set' object is not subscriptable 



# Write  a  program  to  print  random  character  of  the  string  10  times (Home  work)
from random import *
s=input("Enter the string: ")
for i in range(10):
    print(choice(s))
#output:
'''
Enter the string: Rama Rao
a
m
R
a
a
R
a
R
m
'''
# Write  a  program to  generate  10  passwords  each  of  6 character  length  where
# 1st , 3rd , 5th  characters  are  alphabets  and  2nd , 4th , 6th  characters   are  digits
from random import*
import random
alphabets = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"
for _ in range(10):
    password = ""
    for i in range(6):
        if i % 2 == 0: 
            password += random.choice(alphabets)
        else:            
            password += random.choice(digits)
    print(password)
#output
# U0w5e0
# R8o5g9
# o2P2P0
# w7t9d8
# Y4e7l5
# e8r2Q3
# P9r0B1
# R9i7M9
# f6b0I3
# X7V2C9

# Write  a  program  to  print  random  element  of  the  list  ten  times   (Home  work)
from random import *
l=eval(input("Enter the list elemenst: "))
for i in range(10):
    print(choice(l))
#output:
'''
Enter the list elemenst: [25,'siri',True,3+4j,10.8]
25
True
siri
(3+4j)
(3+4j)
(3+4j)
(3+4j)
(3+4j)
siri
25
'''
# Write  a  program  to  generate  ten  six-digit  OTP's  (Home  work)
import random
for _ in range(10):
    otp = ""
    for i in range(6):
        otp += str(random.randint(0, 9))
    print(otp)
#output:
'''
384987
760076
682420
942269
174677
714825
300160
998046
785254
102045
'''
'''
Write  a  program to  open  any  website  from  gmail ,  google ,  rediff ,  ...   with  a  time  gap  of  5  to  20   sec

1) What  does  open('http://google.com')  do ?  ---> Opens  google.com  website

2) Where  is  open()  function  defined  ?  ---> In  webbrowser  module

3) list = ['google.com' , 'rediff.com' , 'gmail.com' , 'amazon.com' , 'netflix.com']

4) Provide  a  time  gap  of  5  to  20 sec  between  the  websites
'''

from  random  import  *
import  webbrowser
import  time
list = ['google.com' , 'youtube.com' , 'gmail.com' , 'rediff.com' , 'amazon.com' , 'bing.com' ,  'flipkart.com' ]  #  List  of  websites
while   True: #  Infinite  loop
	site = choice(list)  #  Random  website
	webbrowser . open(F'http://{site}')  # Opens  the  website
	sec = randint(5 , 20)  #  Random  number  between  5 and  20
	time . sleep(sec)  #  Website  remains  for  5  to  20  sec
	
# ===============================================

# (Home  work)
# Write  a  program  to  implement  Rock , paper  and  scissors  game  between  user  and  computer
from    random    import    choice
list = ['Rock' , 'Paper' , 'Scissors']  # List  of  options
while  True:
	ch = int(input('What  do  you  want  to  select  (0 - Rock , 1 - Paper , 2 - Scissors)  :  ')) #   Reads  0  ,  1  (or)  2
	if  ch  <  0  or  ch  >  2:  #  Is  input  valid
		print('Invalid  Input')
	else:
		user = list[ch]  #  String  corresponding  to  user  input
		comp = choice(list)  #  Random  string  of  the  list
		print('User  :  ' ,  user)
		print('Computer  :  ' , comp)
		if  user  ==  comp:
			print('Draw')
		elif  (comp  ==  'Paper'  and  user  ==  'Rock')   or  (comp  ==  'Rock'  and  user  ==  'Scissors')   or  (comp  ==  'Scissors'  and  user  ==  'Paper'):
			print('Computer  wins')
		else:
			print('User  wins')
		option = input('Continue  (  y / n)  ?  ')
		if  option  ==  'n'  or  option  ==  'N':
			break
# End  of  while  loop
print('End  of  the  game')