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
print(dir(sys)) #prints all the members of the module and also environmental variables
print()         #list of string characters
print()
print(dir(time))#prints all the members of the module and also environmental variables
print()         #list of string characters
print(dir(math))#prints all the members of the module and also environmental variables
                #list of string characters

 #  Find  outputs  (Home  work)
import  cal
print(dir(cal)) #prints everything comes under cal.py 
#Output: ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'add', 'c1', 'div', 'mul', 'sub', 'x', 'y']

#  Find  outputs  (Home  work)
x = 25
def  disp():
	print('Hello')
class  c1:
        def  m1(self):
                pass
print(dir()) #prints members from current directory
print(type(dir()))#<class 'list'>
print(type(dir))#<class 'builtin_function_or_method'>


'''
Write  a  program  to  print  all  the  members  of  cal  module  without  environment  variables

1) What  is  the  result  of  '_name' . startswith('_')  ?  ---> True

2) What  is  the  result  of  '_spec' . endswith('_')  ?  --->  True

3) What  is  the  result  of  'spec_' . startswith('_')  ?  ---> False

4) a = []
    Append  all  the  elements  of  list  returned  by  dir()  function  to  list  'a'  except  environment  variables
'''

#Program
import cal
a=[]
for name in dir(cal):
        if not (name.startswith('__') or name.endswith('__')):
               a.append(name)

print('members of cal module excluding builtins')
for x in a:
    print(a)


#  Find  outputs
print(dir())#builtin functions #[environmental variables]
print()#skipped
import  cal
print()#skipped
print(dir())#same but with cal


#  Find  outputs
print(dir())#builtin functions  #[environmental variables]
print()#skipped
from  cal  import  *
print()#skipped
print(dir())#builtin functions with members 


 #  Find  outputs
print(dir())#builtin functions  #[environmental variables]
print()
from  cal  import  add , mul , x
print()
print(dir())#builtin functions with add,mul,x

# sys . path  demo   program
import  sys
print('Original  sys.path')
for  x  in   sys . path:
	print(x)#all the directory 
print(len(sys . path)) #6
#import  cal #shows error module not found 


# Store  sample.py  module  in  c:\\sairam  folder  before  the  program  is  executed  (Home  work)
import sys
print(len(sys.path))                #How  to  print  number  of  directories  (or)  folders  in  sys.path
sys.path.append('c:\\sairam')       #How  to  append  c:\\sairam  folder  to  sys.path
print(len(sys.path))                #How  to  print  number  of  directories  (or)  folders  in  sys.path
import sample                       #How  to  print  object  'x'  of  sample   module  which  is  in  c:\sairam  folder
sample.f1()                         #How  to  call   function  f1()  of  sample  module  which  is  in  c:\sairam  folder
a=sample.c1()
a.m1()                              #How  to  call   method  m1()  of  class  c1  of  sample  module  which  is  in  c:\sairam  folder

#random program
from  random  import  *
print(random())                  #generates a random float digit between 0 to 1 excluding 0 and 1 #0.23874
print(randint(1 , 100))          #generates random integer between 1 to 100 including 1st and last no. #5
print(uniform(1 , 100))          #generates random float number between 1 to 100 excluding 1st and last no.#4.5
print(randrange(10))             #generates random numbers in range 0 to 9  
print(randrange(1 , 11))         #generates random integers between 1 to 10 
print(randrange(1 , 11 , 2))     #generates random integers between 1 to 10 in steps of 2
list = [10 , 20 , 15 , 12 , 18]
print(choice(list))              #prints random elements of list
print(choice('RAJESH'))          #prints random characters from strings
set  =  {10 , 20 , 30 , 40}
print(choice(set))               #error becoz set don't have indexes and choice internally uses index



 # Write  a  program  to  print  random  character  of  the  string  10  times (Home  work)
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
import random
a = "satyanarayana"
for i in range(10):
     ch = random.choice(a)
     print(ch)
       




#Write  a  program to  generate  10  passwords  each  of  6 character  length  where
#1st , 3rd , 5th  characters  are  alphabets  and  2nd , 4th , 6th  characters   are  digits
'''expected Output:
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
#Program
import random

alphabets =[chr(i) for i in range(65,91)]
digits = [str(i) for i in range(10)]

for _ in range(10):
       a = ''
       for pos in range(1,7):
              if pos % 2 == 1:
                     a += random.choice(alphabets)
              else:
                     a += random.choice(digits)
       print(a)

'''
Output:
P0N7G7
E3J0F1
P0S8H7
J0V1O2
P4X8S5
N2F6E8
L0D2W4
N2U4L6
Z6U1G5
F9A7F0
'''
#Another way of writing this program
from random import randint
def digit():
     return randint(0,9)
def alpha():
     return chr(randint(65,90))
for i in range(10):
     print(alpha(),digit(),alpha(),digit(),alpha(),digit(),sep='')


# Write  a  program  to  print  random  element  of  the  list  ten  times   (Home  work)
'''
Enter a List : [25,10.8,'Hyd',True,3+4j,None]
expected output:
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
#program
import random
a=[25,10.8,'Hyd',True,3+4j,None]
for i in range(10):
       print(random.choice(a))

'''
# Write  a  program  to  generate  ten  six-digit  OTP's  (Home  work)

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
#program
import random 
for _ in range(10):
  print(random.randint(000000,999999))
       

'''
Write  a  program to  open  any  website  from  gmail ,  google ,  rediff ,  ...   with  a  time  gap  of  5  to  20   sec

1) What  does  open('http://google.com')  do ?  ---> Opens  google.com  website

2) Where  is  open()  function  defined  ?  ---> In  webbrowser  module

3) list = ['google.com' , 'rediff.com' , 'gmail.com' , 'amazon.com' , 'netflix.com']

4) Provide  a  time  gap  of  5  to  20 sec  between  the  websites
'''
#Program
import webbrowser
import time
import random

sites = [
    "https://google.com",
    "https://rediff.com",
    "https://gmail.com",
    "https://amazon.com",
    "https://netflix.com"
]

for site in sites:
    print(f"Opening: {site}")
    webbrowser.open_new_tab(site)

    # Random delay between 5 and 20 seconds
    delay = random.randint(5, 10)
    print(f"Waiting {delay} seconds before opening next site...")
    time.sleep(delay)

print("Done — all sites opened.")


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
import random

choices = ['Rock','Paper','Scissors']

user = input("Enter rock , paper or scissors: ").lower()

computer = random.choice(choices)
print("Computer chose:",computer)

while True:
       if user == computer:
        print("Draw")
       elif computer == "paper" and user == "rock":
        print('Computer wins')
       elif computer == "scissors" and user == "paper":
        print('Computer wins')
       elif computer == 'rock' and user == 'scissors':
        print('Computer wins')
       else:
        print("user wins")

       choice = input("Do you want to continue? (y/n): ").lower()
       if choice == "n" :
        print("Thanks for playing")
        break
