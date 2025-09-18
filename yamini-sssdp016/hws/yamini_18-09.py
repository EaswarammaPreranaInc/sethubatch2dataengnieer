#  Find  outputs  (Home  work)
import  sys , time , math
print(dir(sys)) # returns all the members and environment variables of sys module
print()
print()
print(dir(time)) # returns all the members and environment variables of time module
print()
print(dir(math))   # returns all the members and environment variables of math module

#  Find  outputs  (Home  work)
import  cal
print(dir(cal)) # retuns the environment variables of cal mod and functions add sub mul div and class c1 and objects x and y

#  Find  outputs  (Home  work)
x = 25
def  disp():
	print('Hello')
class  c1:
        def  m1(self):
                pass
print(dir())    # retuns the members and environment variables of current directory like x,disp,c1
print(type(dir()))  # class list    
print(type(dir))    # class

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
    if not (i. startswith('__') or i.endswith('__')):
        a.append(i)
print(a)

#  Find  outputs
print(dir())    # prints env variables of current mod
print()
import  cal
print()
print(dir())    # along with env variables prints cal as imported modules becomes mebers of current module

#  Find  outputs
print(dir())    # prints env variables of current mod
print()
from  cal  import  *
print()
print(dir())  # along with env variables prints mebers of cal modules becomes members of current module


# sys . path  demo   program
import  sys
print('Original  sys.path') # prints Original  sys.path 
for  x  in   sys . path:
	print(x)    # prints current working directory along with 5 other standard directories
print(len(sys . path))  # 6
#import  cal

# Store  sample.py  module  in  c:\\sairam  folder  before  the  program  is  executed  (Home  work)
import sys
import samp # which is in sairam directory
print(len(sys.path))    #How  to  print  number  of  directories  (or)  folders  in  sys.path
sys.path.appned('c:\sairam')    #How  to  append  c:\sairam  folder  to  sys.path
print(len(sys.path))    #How  to  print  number  of  directories  (or)  folders  in  sys.path
print(samp.x)    #How  to  print  object  'x'  of  sample   module  which  is  in  c:\sairam  folder
print(samp.f1)  #How  to  call   function  f1()  of  sample  module  which  is  in  c:\sairam  folder
a=samp.c1()
a.m1    #How  to  call   method  m1()  of  class  c1  of  sample  module  which  is  in  c:\sairam  folder

from  random  import  *
print(random()) # prints random number between 0 and 1
print(randint(1 , 100)) # prints random number between 1 and 100
print(uniform(1 , 100)) # prints integer between 1 and 100
print(randrange(10))    # prints the element in range of 0 to 9
print(randrange(1 , 11))    # prints random number in range of 1 to 11
print(randrange(1 , 11 , 2))    # # prints random number in range of 1 to 11 in step of 2
list = [10 , 20 , 15 , 12 , 18]
print(choice(list)) # prints the random element of the list
print(choice('RAJESH')) # prints random character in string
set  =  {10 , 20 , 30 , 40}
#print(choice(set)) # error as set is not indexed so choice method doesnt work


# Write  a  program  to  print  random  character  of  the  string  10  times (Home  work)
from  random  import  *
n=input()
for i in range(10):
    print(choice(n))


#Write  a  program to  generate  10  passwords  each  of  6 character  length  where 1st , 3rd , 5th  characters  are  alphabets  and  2nd , 4th , 6th  characters   are  digits
import random

for i in range(10):
    s=''
    for j in range(6):
        if j%2==0:
            s+=str(random.randrange(1,10))
        else:
            k=random.randrange(65,90)
            s+=chr(k)
    print(s)

# Write  a  program  to  print  random  element  of  the  list  ten  times   (Home  work)
import random
n=eval(input())
for i in range(10):
    print(random.choice(n))


# Write  a  program  to  generate  ten  six-digit  OTP's  (Home  work)
import random
for i in range(10):
    s=''
    for j in range(6):
        s+=str(random.randint(0,9))
    print(s)


'''
Write  a  program to  open  any  website  from  gmail ,  google ,  rediff ,  ...   with  a  time  gap  of  5  to  20   sec

1) What  does  open('http://google.com')  do ?  ---> Opens  google.com  website

2) Where  is  open()  function  defined  ?  ---> In  webbrowser  module

3) list = ['google.com' , 'rediff.com' , 'gmail.com' , 'amazon.com' , 'netflix.com']

4) Provide  a  time  gap  of  5  to  20 sec  between  the  websites
'''
import webbrowser
import time
import random
list = ['https://www.google.com', 'https://www.spotify.com', 'https://www.gmail.com',
         'https://www.amazon.com', 'https://www.netflix.com']

while(True):
    webbrowser.open(random.choice(list))
    time.sleep(random.randint(5,20))

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
import random
while(True):
    n=int(input('What  do  you  want  to  select  (0 - Rock , 1 - Paper , 2 - Scissors)  : '))
    k=random.randint(0,3)
    print('computer selects:',k)
    if (k==1 and n==0 ) or (k==2 and n==1) or (k==0 and n==2):
        print('Computer  wins')
    elif k==n:
        print('Draw')
    else:
        print('User  wins')
