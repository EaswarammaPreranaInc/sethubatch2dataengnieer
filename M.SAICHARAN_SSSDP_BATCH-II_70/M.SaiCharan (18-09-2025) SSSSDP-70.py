                           NAME:M.SAICHARAN                    HOMEWORK
                           DATE:18-09-2025

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

#Cal.py is reference





1.#  Find  outputs  (Home  work)
import  sys , time , math
print(dir(sys))		#list of strings of all the environment variables and members of sys module
print()
print()
print(dir(time))	#list of strings of all the environment variables and members of time module

print()
print(dir(math))	#list of strings of all the environment variables and members of math module




2.#  Find  outputs  (Home  work)
import  cal
print(dir(cal))		#List of strings of all the environment variables and add,div,mul,sub,x,y




3.#  Find  outputs  (Home  work)
x = 25
def  disp():
	print('Hello')
class  c1:
        def  m1(self):
                pass
print(dir())		#all the environment variables with c1 , disp and x of current module
print(type(dir()))	#<class 'list'>
print(type(dir))	#<class 'builtsinsormethod'>




'''
4.Write  a  program  to  print  all  the  members  of  cal  module  without  environment  variables

1) What  is  the  result  of  '_name' . startswith('_')  ?  ---> True

2) What  is  the  result  of  '_spec' . endswith('_')  ?  --->  True

3) What  is  the  result  of  'spec_' . startswith('_')  ?  ---> False

4) a = []
    Append  all  the  elements  of  list  returned  by  dir()  function  to  list  'a'  except  environment  variables
'''
#program:
import cal
a = []
for item in dir(cal):
    if not item.startswith('__'):
        a.append(item)
print(a)



5.#  Find  outputs
print(dir())	#only environment variables
print()
import  cal
print()
print(dir())	#list of strings of all the environment variables and cal module





6.#  Find  outputs
print(dir())	#only environment variables
print()
from  cal  import  *
print()
print(dir())	#List of strings of all the environment variables and add,div,mul,sub,x,y




7.#  Find  outputs
print(dir())		#[Ev's]
print()
from  cal  import  add , mul , x
print()
print(dir())		#[Ev's, add, mul, x]




8.# sys . path  demo   program
import  sys
print('Original  sys.path')
for  x  in   sys . path:  # x is each directory of syspath
	print(x)
print(len(sys . path))    #7
#import  cal




9.# Store  sample.py  module  in  c:\\sairam  folder  before  the  program  is  executed  (Home  work)
import sys
print(sys.path)  #How  to  print  number  of  directories  (or)  folders  in  sys.path
sys.path.append(c:\\sairam) #How  to  append  c:\sairam  folder  to  sys.path
len(sys.path) #How  to  print  number  of  directories  (or)  folders  in  sys.path
import sairam

#How  to  print  object  'x'  of  sample   module  which  is  in  c:\sairam  folder
print(sairam.x)

#How  to  call   function  f1()  of  sample  module  which  is  in  c:\sairam  folder
sairam.f1()

#How  to  call   method  m1()  of  class  c1  of  sample  module  which  is  in  c:\sairam  folder
a.sairam.c1()
a.m1()




10.from  random  import  *
print(random())			#random float number between 0 and 1 excluding both
print(randint(1 , 100))		# random integer between 1 and 100
print(uniform(1 , 100))		# random float number between 1 and 100
print(randrange(10))		# random integer number between 0 and 9 excluding 10
print(randrange(1 ,11)		# random integer number  between 1 to 10 excluding 11
print(randrange(1 , 11 , 2))	# random integer number between 1 to 10 insteps of 2
list = [10 , 20 , 15 , 12 , 18]
print(choice(list))		#any random element of list
print(choice('RAJESH'))		#any random element of string
set  =  {10 , 20 , 30 , 40}
print(choice(set))		#Error as set is not indexed




11.# Write  a  program  to  print  random  character  of  the  string  10  times (Home  work)
Enter  any  string :  Rama Rao
R

a
R
R
a
R
R
m

#Program:
import random
n = input("Enter any string: ")
for i in range(10):
    print(random.choice(n))


12.Write  a  program to  generate  10  passwords  each  of  6 character  length  where
1st , 3rd , 5th  characters  are  alphabets  and  2nd , 4th , 6th  characters   are  digits
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

#Program:
import random
import string
for i in range(10):
    password = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    print(password)

13.# Write  a  program  to  print  random  element  of  the  list  ten  times   (Home  work)
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

#Program:
import random
list = list(input("Enter the list of elements: "))
for i in range(10):
    print(random.choice(list))


14.# Write  a  program  to  generate  ten  six-digit  OTP's  (Home  work)
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

#Program:
import random
for i in range(10):
    otp = random.randint(100000, 999999)
    print(otp)


'''
15.Write  a  program to  open  any  website  from  gmail ,  google ,  rediff ,  ...   with  a  time  gap  of  5  to  20   sec

1) What  does  open('http://google.com')  do ?  ---> Opens  google.com  website

2) Where  is  open()  function  defined  ?  ---> In  webbrowser  module

3) list = ['google.com' , 'rediff.com' , 'gmail.com' , 'amazon.com' , 'netflix.com']

4) Provide  a  time  gap  of  5  to  20 sec  between  the  websites
'''
#Program:
import webbrowser
import time
import random
websites = ['google.com', 'rediff.com', 'gmail.com', 'amazon.com', 'netflix.com']
for site in websites:
    webbrowser.open(f'http://{site}')
    time.sleep(random.randint(5, 20))


'''
(Home  work)
16.Write  a  program  to  implement  Rock , paper  and  scissors  game  between  user  and  computer

1) What  is  the  result  if  user  input  and  computer  random  number  are  same  ?  ---> Draw

2) What  is  the  result  if  computer  selects  paper  and  user  input  is  rock ?  --->
																												Computer  wins  becoz  parer  dominates  rock

3) What  is  the  result  if  computer  selects  scissors  and  user  input  is  paper ?  --->
																										Computer  wins  becoz  scissors  dominates  paper

4) What  is  the  result  if  computer  selects  rock  and  user  input  is  scissors ?  --->
																										Computer  wins  becoz  rock  dominates  scissors

5) What  is  the  result  in  all  other  cases  ?  --->  User  wins
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

#Program:
import random
def play_game():
    choices = ['Rock', 'Paper', 'Scissors']
    while True:
        user_choice = int(input("What do you want to select (0 - Rock, 1 - Paper, 2 - Scissors): "))
        user_choice = choices[user_choice]
        computer_choice = random.choice(choices)
        print(f"User: {user_choice}")
        print(f"Computer: {computer_choice}")
        if user_choice == computer_choice:
            print("Draw")
        elif (computer_choice == 'Paper' and user_choice == 'Rock') or \
             (computer_choice == 'scissors' and user_choice == 'Paper') or \
             (computer_choice == 'rock' and user_choice == 'Scissors'):
            print("Computer wins")
        else:
            print("User wins")
        continue_game = input("Continue (y/n)? ")
        if continue_game.lower() != 'y':
            print("End of the game")
            break
play_game()