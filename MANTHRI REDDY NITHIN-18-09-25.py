# 1) cal.py

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




# 2) Find  outputs  (Home  work)

import  sys , time , math
print(dir(sys))     # dir(sys) prints list of all the members and also environment variables of sys module
print()
print()
print(dir(time))    # dir(time) prints list of all the members and also environment variables of time module
print()
print(dir(math))    # dir(math) prints list of all the members and also environment variables of math module




# 3) Find  outputs  (Home  work)

import  cal
print(dir(cal))     # dir(cal) prints list of all the members and also environment variables of cal module




# 4) Find  outputs  (Home  work)

x = 25
def  disp():
	print('Hello')
class  c1:
        def  m1(self):
                pass
print(dir())        # dir() prints list of all the members and also environment variables of current module
print(type(dir()))  # <class 'list'>
print(type(dir))    # <class 'builtin_function_or_method'>




''' 5) Write  a  program  to  print  all  the  members  of  cal  module  without  environment  variables

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
        continue
    else:
        a.append(i)
print(a)        

'''
output:
['add', 'c1', 'div', 'mul', 'sub', 'x', 'y']
'''



# 6) Find  outputs

print(dir())    # dir() prints list of all the members and also environment variables of current module
print()
import  cal     # cal module is imported
print()
print(dir())    # dir() prints list of all the members and also environment variables of current module





# 7) Find  outputs
 
print(dir())    # dir() prints list of all the members and also environment variables of current module
print()
from  cal  import  *    # all the members and statements of the cal module are imported due to *
print()
print(dir())    # here dir() prints list of all the members and also environment variables of cal module 


# 8) Find  outputs

print(dir())     # dir() prints list of all the members and also environment variables of current module
print()
from  cal  import  add , mul , x    # not all members only add,mul,x and statements of the cal module are imported
print()
print(dir())    # dir() prints list of add,mul,x and also environment variables of cal module


# 9) sys . path  demo   program

import  sys
print('Original  sys.path')
for  x  in   sys . path:
	print(x)
print(len(sys . path))
#import  cal

'''
output:
Original  sys.path
C:\Users\Chandu\Desktop
C:\Users\Chandu\AppData\Local\Programs\Python\Python313\python313.zip
C:\Users\Chandu\AppData\Local\Programs\Python\Python313\DLLs
C:\Users\Chandu\AppData\Local\Programs\Python\Python313\Lib
C:\Users\Chandu\AppData\Local\Programs\Python\Python313
C:\Users\Chandu\AppData\Local\Programs\Python\Python313\Lib\site-packages
6
'''




# 10) Store  sample.py  module  in  c:\\sairam  folder  before  the  program  is  executed  (Home  work)

import sys 
print(len(sys.path))# How  to  print  number  of  directories  (or)  folders  in  sys.path
sys.path.append ('C:\\Users\\Chandu\\Desktop\\sairam')    # How  to  append  c:\sairam  folder  to  sys.path
print(len(sys.path))# How  to  print  number  of  directories  (or)  folders  in  sys.path
import sample
print(sample.x)     # How  to  print  object  'x'  of  sample   module  which  is  in  c:\sairam  folder
sample.f1()         # How  to  call   function  f1()  of  sample  module  which  is  in  c:\sairam  folder
a=sample.c1()       # How  to  call   method  m1()  of  class  c1  of  sample  module  which  is  in  c:\sairam  folder
a.m1()

'''
output:
6
7
10
disp  function  of  sample module
m1  method  of  class  c1  in  sample module
'''




# 11) find outputs

from  random  import  *
print(random())             # print random float number between 0 to 1(both 0 and 1 are excluded)
print(randint(1 , 100))     # print random integer number between 1 to 100(both included)
print(uniform(1 , 100))     # print random float number between 1 to 100(both 1 and 100 are excluded)
print(randrange(10))        # print random integer 0 to 10-1 in steps of 1
print(randrange(1 , 11))    # print random integer 1 to 11-1 in steps of 1
print(randrange(1 , 11 , 2))# print random integer 1 to 11-1 in steps of 2
list = [10 , 20 , 15 , 12 , 18]
print(choice(list))         # print random element of the list of 5 elements
print(choice('RAJESH'))     # print random element of the string "RAJESH" 
set  =  {10 , 20 , 30 , 40} 
print(choice(set))          # Error as set is not indexed we cannot perform choice function to set

'''
output:
0.13391664016078175
48
6.938445656090156
8
6
1
15
R
'''




# 12) Write  a  program  to  print  random  character  of  the  string  10  times (Home  work)

import random as r
n=input('Enter any string : ')
for i in range(10):
    i=r.choice(n)
    print(i)
'''  
output:  
Enter any string : Mahesh
h
M
h
h
h
M
M
a
a
h
'''
    



''' 13) Write  a  program to  generate  10  passwords  each  of  6 character  length  where
1st , 3rd , 5th  characters  are  alphabets  and  2nd , 4th , 6th  characters   are  digits
'''
import random as r
for i in range(10):
    s=''
    for j in range(6):
        if j%2==0:
            s+=chr(r.randint(65,90))
        else:    
            s+=chr(r.randint(48,57))
    print(s)    

'''
output:
Q7M9X4
D0P3A7
M4H9I7
V4F9T4
P8N9X8
S8W8B4
O4N2X2
L7W9E2
R8U5Z6
C3Q7J6
'''
    
    
    
# 14) Write  a  program  to  print  random  element  of  the  list  ten  times   (Home  work)

import random as r
n=eval(input('Enter a List : '))
for i in range(10):
    i=r.choice(n)
    print(i)

'''
Enter a List : [25,10.8,'Hyd',True,3+4j,None]
(3+4j)
Hyd
None
25
True
Hyd
(3+4j)
25
(3+4j)
(3+4j)
'''




# 15) Write  a  program  to  generate  ten  six-digit  OTP's  (Home  work)

import random as r
for i in range(10):
    otp=r.randint(100000,999999)
    print(otp)

'''
output:
407562
659514
495499
157046
841295
443061
100433
872181
916707
576967
'''




''' 16) Write  a  program to  open  any  website  from  gmail ,  google ,  rediff ,  ...   with  a  time  gap  of  5  to  20   sec

1) What  does  open('http://google.com')  do ?  ---> Opens  google.com  website

2) Where  is  open()  function  defined  ?  ---> In  webbrowser  module

3) list = ['google.com' , 'rediff.com' , 'gmail.com' , 'amazon.com' , 'netflix.com']

4) Provide  a  time  gap  of  5  to  20 sec  between  the  websites
'''

import random as r, time as t,webbrowser as web
websites = ['google.com' ,'gmail.com' ,'amazon.com' ,'netflix.com', 'youtube.com']
while True: 
    site = r.choice(websites)
    web.open("http://" + site)   
    delay = r.randint(5, 20)
    t.sleep(delay)





''' 17) (Home  work)
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
import random as r
game="y"
choices=["Rock","Paper","Scissors"]

while game=="y":
    
    u=int(input('What  do  you  want  to  select  (0 - Rock , 1 - Paper , 2 - Scissors)  :  '))
    print('User  :   ',choices[u])
    com=r.randrange(0,3)
    print('Computer  :   ',choices[com])
    
    if com==u:
        print('Draw')
        
    elif (u==0 and com==1)  or   (u==1 and com==2)  or   (u==2 and com==0):
        print('Computer  wins')
        
    else:
        print('User wins')  
        
    game = input("Continue (y/n)? ")
     
print("End of the game")          

'''
output:
What  do  you  want  to  select  (0 - Rock , 1 - Paper , 2 - Scissors)  :  0
User  :    Rock
Computer  :    Scissors
User wins
Continue (y/n)? y
What  do  you  want  to  select  (0 - Rock , 1 - Paper , 2 - Scissors)  :  1
User  :    Paper
Computer  :    Paper
Draw
Continue (y/n)? y
What  do  you  want  to  select  (0 - Rock , 1 - Paper , 2 - Scissors)  :  2
User  :    Scissors
Computer  :    Rock
Computer  wins
Continue (y/n)? n
End of the game
'''
