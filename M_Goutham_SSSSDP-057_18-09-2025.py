#  Find  outputs  (Home  work)
import  sys , time , math
print(dir(sys)) #Here it prints the list of strings of all the members of sys module
print() #Prints nothing
print() #Prints nothing
print(dir(time)) #Here it prints the list of string of all the memebers of time module
print() #Prints nothing
print(dir(math)) #Here it prints the list of strings of all the memebers of math module



#  Find  outputs  (Home  work)
import  cal
print(dir(cal)) #Here it prints the list of strings of all the members of cal module 



# Find  outputs  (Home  work)
x = 25
def  disp():
	print('Hello')
class  c1:
        def  m1(self):
                pass
print(dir()) #Prints the members of current module and environement variables
print(type(dir())) #<class 'list'>
print(type(dir)) #<class 'builtin_function_or_method'>


'''
Write  a  program  to  print  all  the  members  of  cal  module  without  environment  variables

1) What  is  the  result  of  '_name' . startswith('_')  ?  ---> True

2) What  is  the  result  of  '_spec' . endswith('_')  ?  --->  True

3) What  is  the  result  of  'spec_' . startswith('_')  ?  ---> False

4) a = []
    Append  all  the  elements  of  list  returned  by  dir()  function  to  list  'a'  except  environment  variables
'''


#  Find  outputs
print(dir()) #Prints the env variables
print() #Prints nothing
#import  cal #Here we are imported cal madule
print() #Prints nothing
print(dir()) #Prints the members of current module and cal is added 



#  Find  outputs
print(dir()) #Prints the env variables
print() #Prints nothing
from  cal  import  * #Here we have imported the cal module where all the memebers are imported
print() #Prints nothing
print(dir()) #Prints the members of current module and also cal module


#  Find  outputs
print(dir()) #Prints the environment variables
print() #Prints nothing
from  cal  import  add , mul , x #Here from cal module we have imported add,mul,x
print() #Prints nothing
print(dir()) #Prints the current module memebers and also add mul x


# sys . path  demo   program
import  sys #sys module is imported and it is initialized to 6 dir
print('Original  sys.path') #Prints string Original sys.path
for  x  in   sys . path: 
	print(x) #Prints the current working dir and also standard dir #here we will get the paths
print(len(sys . path)) #6



#import  cal
# Store  sample.py  module  in  c:\\sairam  folder  before  the  program  is  executed  (Home  work)
import sys 
print(len(sys.path)) #How  to  print  number  of  directories  (or)  folders  in  sys.path
sys.path.append('c:\\sairam') #How  to  append  c:\sairam  folder  to  sys.path
print(len(sys.path)) #How  to  print  number  of  directories  (or)  folders  in  sys.path
import cal
print(cal.x) #How  to  print  object  'x'  of  sample   module  which  is  in  c:\sairam  folder
cal.f1() #How  to  call   function  f1()  of  sample  module  which  is  in  c:\sairam  folder
g = cal.c1()
print(g.m1()) #How  to  call   method  m1()  of  class  c1  of  sample  module  which  is  in  c:\sairam  folder



from  random  import  * #Here we are importing the random module and all its members
print(random()) #Prints the random number b/w 0 and 1 and here 0 and 1 are excluded
print(randint(1 , 100)) #Prints the random number b/w 1 and 100 and here 1 and 100 are included
print(uniform(1 , 100)) #Prints the random number b/w 1 and 100 and here 1 and 100 are excluded
print(randrange(10)) #Prints the random number b/w 0 and 10 and here 10 is excluded
print(randrange(1 , 11)) #Prints the random number b/w 1 and 10 in steps of 1
print(randrange(1 , 11 , 2)) #Prints the random number b/w 1 and 10 in steps of 2
list = [10 , 20 , 15 , 12 , 18] #Ref list points to list of int obj
print(choice(list)) #Here it returns a random element from the sequence i.e above list 
print(choice('RAJESH')) #Here it returns a random char from the string RAJESH
set  =  {10 , 20 , 30 , 40} #Here ref set points to set of elements
print(choice(set)) #Error #we cannot use choice for set as set is non-indexed



# Write  a  program  to  print  random  character  of  the  string  10  times (Home  work)
from random import choice
n = input("Enter any String: ")
for i in range(len(n)+1):
    print(random.choice(n))


'''
Enter  any  string :  Rama Rao
R

a
R
R
a
R
R
m
'''

'''
Write  a  program to  generate  10  passwords  each  of  6 character  length  where
1st , 3rd , 5th  characters  are  alphabets  and  2nd , 4th , 6th  characters   are  digits
'''
import random , string
alpha = string.ascii_uppercase
num = string.digits
for i in range(11):
    password = random.choice(alpha)+random.choice(num)+random.choice(alpha)+random.choice(num)+random.choice(alpha)+random.choice(num)
    print(password)
 
'''
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
'''


# Write a program to print random element of the list ten times (Home  work)

from random import *
n = eval(input("Enter list: "))
for i in range(11):
    print(choice(n))
    
'''
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
'''


# Write  a  program  to  generate  ten  six-digit  OTP's  (Home  work)
from random import *
for i in range(11):
    print(randint(100000,999999))

'''
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


'''
Write  a  program to  open  any  website  from  gmail ,  google ,  rediff ,  ...   with  a  time  gap  of  5  to  20   sec

1) What  does  open('http://google.com')  do ?  ---> Opens  google.com  website

2) Where  is  open()  function  defined  ?  ---> In  webbrowser  module

3) list = ['google.com' , 'rediff.com' , 'gmail.com' , 'amazon.com' , 'netflix.com']

4) Provide  a  time  gap  of  5  to  20 sec  between  the  websites
'''

import time
import random
import webbrowser

sites = ['google.com', 'rediff.com', 'gmail.com', 'amazon.com', 'netflix.com']

while True:
    url = f'https://{random.choice(sites)}'
    webbrowser.open(url)
    time.sleep(15)


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

while True:
    user = int(input("What do you want to select (0 - Rock, 1 - Paper, 2 - Scissors) : "))
    computer = random.randint(0, 2)

    choices = ["Rock", "Paper", "Scissors"]

    print(f"User     : {choices[user]}")
    print(f"Computer : {choices[computer]}")

    if user == computer:
        print("Draw")
    elif (user == 0 and computer == 2) or (user == 1 and computer == 0) or (user == 2 and computer == 1):
        print("User wins")
    else:
        print("Computer wins")

    cont = input("Continue ( y / n ) ? ").lower()
    if cont == 'n':
        print("End of the game")
        break

'''
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