#  Find  outputs  (Home  work)
import  sys , time , math
print(dir(sys)) # prints all the members of sys module and environment variables in the form of list of strings
print() # prints nothing
print() # prints nothing
print(dir(time)) # prints all the members of time module and environment variables in the form of list of strings
print() # prints nothing
print(dir(math)) # prints all the members of math module and environment variables in the form of list of strings









#  Find  outputs  (Home  work)
import  cal # cal module is imported
print(dir(cal)) # prints all the members of cal module and environment variables  
'''
['add', 'sub', 'mul', 'div', 'c1', 'x', 'y', '__name__', '__annotations__'.... ]
'''









#  Find  outputs  (Home  work)
x = 25
def disp():
	print('Hello')
class c1:
    def m1(self):
        pass
print(dir()) # prints members of current module in the form of list of strings
print(type(dir())) # prints the type of dir
print(type(dir))
'''
Outputs
['x', 'disp', 'c1']
<class 'list'>
<class 'builtin_function'>
'''









'''
Write  a  program  to  print  all  the  members  of  cal  module  without  environment  variables

1) What  is  the  result  of  '_name' . startswith('_')  ?  ---> True

2) What  is  the  result  of  '_spec' . endswith('_')  ?  --->  True

3) What  is  the  result  of  'spec_' . startswith('_')  ?  ---> False

4) a = []
    Append  all  the  elements  of  list  returned  by  dir()  function  to  list  'a'  except  environment  variables
'''
import cal
a = dir(cal)
b = []
for i in a:
	if not i.startswith('__') and not i.endswith('__'):
		b.append(i)
print(b)








#  Find  outputs
print(dir()) # prints all the members of the current module in the form of list of strings i.e., []
print() # prints nothing
import cal # imports cal module
print() # prints nothing
print(dir()) # prints all the members of the current module in the form of list of strings i.e., ['add', 'sub', 'mul', 'div','c1', 'x', 'y']









#  Find  outputs
print(dir()) # prints all the members of the current module in the form of list of strings i.e., []
print() # prints nothing
from cal import  * # imports all the members of cal module
print() # prints nothing
print(dir()) # prints ['add', 'sub', 'mul', 'div', 'c1', 'x', 'y']









#  Find  outputs
print(dir()) # prints members of current module i.e., []
print() # prints nothing
from  cal  import  add , mul , x # imports members of cal module
print() # prints nothing
print(dir()) # prints ['add', 'mul', 'x']









# sys . path  demo   program
import sys # importing sys module
print('Original  sys.path') # prints Original sys.path
for x in sys.path:
	print(x) # cwd<nextline>2nd<nextline>3rd<nextline>4th<nextline>5th<nextline>6th<nextline>
print(len(sys.path)) # prints 6 or more, minimum 6
#import cal






# Store  sample.py  module  in  c:\\sairam  folder  before  the  program  is  executed  (Home  work)
import sys
print(sys.path) #How  to  print  number  of  directories  (or)  folders  in  sys.path
sys.path.append('c:\\sairam') # How  to  append  c:\sairam  folder  to  sys.path
print(len(sys.path)) # How  to  print  number  of  directories  (or)  folders  in  sys.path
import sample
print(sample.x) # How  to  print  object  'x'  of  sample   module  which  is  in  c:\sairam  folder
print(sample.f1()) # How  to  call   function  f1()  of  sample  module  which  is  in  c:\sairam  folder
a = sample.c1
a.m1() # How  to  call   method  m1()  of  class  c1  of  sample  module  which  is  in  c:\sairam  folder










from random import  *
print(random()) # prints random number
print(randint(1 , 100)) # prints random integer number from 1 to 100 and 1 and 100 are included
print(uniform(1 , 100)) # prints random float number between 1 and 100 and 1 and 100 are excluded
print(randrange(10)) # prints random number between 0 and 9 and 0 and 9 is included
print(randrange(1 , 11)) # prints random number between 1 ans 10 and 1 and 10 is included
print(randrange(1 , 11 , 2)) # prints random number between 1 and 10 in steps of 2 and 1 and 10 are included
list = [10 , 20 , 15 , 12 , 18] # Ref 'list' points to list of 5 elements
print(choice(list)) # prints random element from the list
print(choice('RAJESH')) # prints random character from string 'RAJESH'
set  =  {10 , 20 , 30 , 40} # Ref 'set' points to set of 4 elements
print(choice(set)) # Error because argument of choice cannot be a set









# Write  a  program  to  print  random  character  of  the  string  10  times (Home  work)
from random import *
a = input("Enter any string:")
for i in range(10):
	print(choice(a))
'''
Outputs
Enter any string:Sairam
m
r
a
a
i
m
a
r
i
r
'''









'''
Write  a  program to  generate  10  passwords  each  of  6 character  length  where
1st , 3rd , 5th characters are alphabets and  2nd , 4th , 6th characters are digits
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
from random import *
a = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
b = '1234567890'
for i in range(10):
    for i in range(1, 4): 
        print(choice(a), end = '') 
        for j in range(i, i+1):
            print(choice(b), end = '')
    print()
'''
Outputs
A4S0Y9
A5M1J0
S3D8S8
A5R2W1
B8A5F8
C0O3H4
X7E9X2
F9D1F1
N6Z8V8
J2G5M1
'''









'''
# Write  a  program  to  print  random  element  of  the  list  ten  times   (Home  work)
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
from random import *
a = eval(input("Enter any list:"))
for i in range(10):
	print(choice(a))
'''
Outputs
Enter any list:[25,10.8,'Hyd',True,3+4j,None]
25
True
(3+4j)
25
None
10.8
(3+4j)
10.8
True
10.8
'''








'''
# Write  a  program  to  generate  ten  six-digit  OTP's (Home work)
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
from random import *
for i in range(10):
	for j in range(6):
		print(randrange(10), end = '')
	print()
'''
Outputs
715415
735342
476443
557321
399866
652264
901100
288444
600817
074436
'''





'''
Write a program to open any website from gmail , google , rediff ,  ... with a time  gap  of  5  to  20   sec

1) What does open('http://google.com')  do ?  ---> Opens  google.com  website

2) Where is open() function defined ?  ---> In  webbrowser  module

3) list = ['google.com' , 'rediff.com' , 'gmail.com' , 'amazon.com' , 'netflix.com']

4) Provide  a  time  gap  of  5  to  20 sec between the websites
'''
from random import *
import time
import webbrowser
list = ['google.com' , 'rediff.com' , 'gmail.com' , 'amazon.com' , 'netflix.com']
for i in range(10):
    webbrowser.open('https://'+ choice(list))
    time.sleep(20)










'''
(Home  work)
Write a program to implement Rock , paper  and  scissors  game  between  user  and  computer

1) What is the result if user input and computer random number are same ?  ---> Draw

2) What is the result if computer selects paper and  user  input  is  rock ?  --->
																			Computer  wins  becoz  parer  dominates  rock

3) What  is  the  result  if  computer  selects  scissors  and  user  input  is  paper ?  --->
																			Computer  wins  becoz  scissors  dominates  paper

4) What  is  the  result  if  computer  selects  rock  and  user  input  is  scissors ?  --->
																			Computer  wins  becoz  rock  dominates  scissors

5) What  is  the  result  in  all  other  cases  ?  ---> User wins

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
End of the game
'''
from random import *
list = ["Rock", "Paper", "Scissors"]
while True:
	n = int(input("What  do  you  want  to  select  (0 - Rock , 1 - Paper , 2 - Scissors):"))
	user = list[n]
	computer = randint(0,2)
	computer = list[computer]
	print(F'User : {user}')
	print(F'Computer : {computer}')
	if (computer == 1 and user == 0) or (computer == 2 and user == 1) or (computer == 0 and user == 2):
		print("Computer wins")
	elif user == computer:
		print("Draw")
	else:
		print("User wins")
	a = input("Continue (y/n):")
	if a != 'y':
		print("End of the game")
		break	
'''
What  do  you  want  to  select  (0 - Rock , 1 - Paper , 2 - Scissors):0
User : Rock
Computer : Scissors
User wins
Continue (y/n):y
What  do  you  want  to  select  (0 - Rock , 1 - Paper , 2 - Scissors):1
User : Paper
Computer : Rock
User wins
Continue (y/n):y
What  do  you  want  to  select  (0 - Rock , 1 - Paper , 2 - Scissors):2
User : Scissors
Computer : Rock
User wins
Continue (y/n):y
What  do  you  want  to  select  (0 - Rock , 1 - Paper , 2 - Scissors):2
User : Scissors
Computer : Scissors
Draw
Continue (y/n):n
End of the game
'''