#  Find  outputs  (Home  work)
import  sys , time , math
print(dir(sys)) #[path]
print()
print()
print(dir(time)) #[time, timec,sleep]
print()
print(dir(math)) #[max,min]

#  Find  outputs  (Home  work)
import  cal
print(dir(cal)) #[add,sub,mul,div,c1,x,y]

#  Find  outputs  (Home  work)
x = 25
def  disp():
	print('Hello')
class  c1:
        def  m1(self):
                pass
print(dir()) #[x,disp,c1]
print(type(dir())) #<class 'list'>
print(type(dir)) #<class 'function'>

'''
Write  a  program  to  print  all  the  members  of  cal  module  without  environment  variables

1) What  is  the  result  of  '__name__' . startswith('__')  ?  ---> True

2) What  is  the  result  of  '__spec__' . endswith('__')  ?  --->  True

3) What  is  the  result  of  'spec__' . startswith('__')  ?  ---> False

4) a = []
    Append  all  the  elements  of  list  returned  by  dir()  function  to  list  'a'  except  environment  variables
'''
import cal
l=dir(cal)
for x in l:
        if not x.startswith('__') and not x.endswith('__'):
                print(x)
                
#  Find  outputs
print(dir()) #[]
print()
import  cal
print()
print(dir())  #[cal]

#  Find  outputs
print(dir()) #[]
print()
from  cal  import  *
print()
print(dir()) #[add,c1,div,mul,sub,x,y]

#  Find  outputs
print(dir()) #[]
print()
from  cal  import  add , mul , x
print()
print(dir()) #[add,mul,x]

# sys . path  demo   program
import  sys
print('Original  sys.path')
for  x  in   sys . path:
	print(x) #cwd and other 5 standard directories
print(len(sys . path)) #6
#import  cal

# Store  sample.py  module  in  c:\\sairam  folder  before  the  program  is  executed  (Home  work)
import sys
print(len(sys.path)) #How  to  print  number  of  directories  (or)  folders  in  sys.path
# How  to  append  c:\sairam  folder  to  sys.path
sys.path.append('c:\\sairam')
print(len(sys.path)) #How  to  print  number  of  directories  (or)  folders  in  sys.path
# How  to  print  object  'x'  of  sample   module  which  is  in  c:\sairam  folder
import sairam 
print(sairam.x)
print(sairam.f1())#How  to  call   function  f1()  of  sample  module  which  is  in  c:\sairam  folder
# How  to  call   method  m1()  of  class  c1  of  sample  module  which  is  in  c:\sairam  folder
obj=sairam.c1()
obj.m1()

from  random  import  *
print(random()) #random number between 0 and 1
print(randint(1 , 100)) # any number from 1 to 100
print(uniform(1 , 100)) # (1,100)
print(randrange(10)) #(0 to 9 )
print(randrange(1 , 11)) # 1 to 10
print(randrange(1 , 11 , 2)) #1 3 5 7 9
list = [10 , 20 , 15 , 12 , 18]
print(choice(list)) # any element of list 
print(choice('RAJESH')) #any char of string RAJESH
set  =  {10 , 20 , 30 , 40}
print(choice(set)) #does not work with sets as choice internally uses index

# Write  a  program  to  print  random  character  of  the  string  10  times (Home  work)
from random import choice
s=input("Enter the string: ")
for i in range(10):
    print(choice(s))

# Write  a  program to  generate  10  passwords  each  of  6 character  length  where
# 1st , 3rd , 5th  characters  are  alphabets  and  2nd , 4th , 6th  characters   are  digits
from random import choice
def random_alphabet():
    s=""
    for i in range(26):
        s=s+chr(65+i)
    return choice(s)
def random_digit():
    s=""
    for i in range(10):
        s=s+str(i)
    return choice(s)
for i in range(10):
    s=""
    for j in range(3):
        s=s+random_alphabet()
        s=s+random_digit()
    print(s)

from random import choice
l=eval(input("Enter the list: "))
for i in range(10):
    print(choice(l))

# Write  a  program  to  generate  ten  six-digit  OTP's  (Home  work)
from random import choice
def random_digit():
    s=""
    for i in range(10):
        s=s+str(i)
    return choice(s)
for i in range(10):
    s=""
    for j in range(6):
        s=s+random_digit()
    print(s)

'''
Write  a  program to  open  any  website  from  gmail ,  google ,  rediff ,  ...   with  a  time  gap  of  5  to  20   sec

1) What  does  open('http://google.com')  do ?  ---> Opens  google.com  website

2) Where  is  open()  function  defined  ?  ---> In  webbrowser  module

3) list = ['google.com' , 'rediff.com' , 'gmail.com' , 'amazon.com' , 'netflix.com']

4) Provide  a  time  gap  of  5  to  20 sec  between  the  websites
'''
import time
from webbrowser import open 
list = ['google.com' , 'rediff.com' , 'gmail.com' , 'amazon.com' , 'netflix.com']
for x in list:
    open(x)
    time.sleep(5)

#Rock paper Scissor game  
from random import randrange
d={0:"Rock",1:"Paper",2:"Scissors"}
while True:
    u=int(input("What  do  you  want  to  select  (0 - Rock , 1 - Paper , 2 - Scissors)  :"))
    c=randrange(3)
    print(f'User: {d[u]}')
    print(f'Computer: {d[c]}')
    if (c==0 and u==2) or (c==1 and u==0) or (c==2 and u==1):
        print("Computer wins")
    elif c==u:
        print("Draw")
    else:
        print("User wins")
    want_to_continue=input("Continue  (  y / n)  ?")
    if want_to_continue=='n':
        break 
print("End  of  the  game")



