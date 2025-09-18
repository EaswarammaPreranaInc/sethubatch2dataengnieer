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





#  Find  outputs  (Home  work)
import  sys , time , math
print(dir(sys))
print()
print()
print(dir(time))
print()
print(dir(math))

#Output:
prints directories for sys, time, match




#  Find  outputs  (Home  work)
import  cal
print(dir(cal))				# ['x', 'y', 'add','sub','mul','div','c1', directories of cal]




#  Find  outputs  (Home  work)
x = 25
def  disp():
	print('Hello')
class  c1:
        def  m1(self):
                pass
print(dir())				# list of directories
print(type(dir()))			# <class 'list'>
print(type(dir))			# <class 'builtin_function_or_method'>




'''
Write  a  program  to  print  all  the  members  of  cal  module  without  environment  variables

1) What  is  the  result  of  '_name' . startswith('_')  ?  ---> True

2) What  is  the  result  of  '_spec' . endswith('_')  ?  --->  True

3) What  is  the  result  of  'spec_' . startswith('_')  ?  ---> False

4) a = []
    Append  all  the  elements  of  list  returned  by  dir()  function  to  list  'a'  except  environment  variables
'''

#Program:
import cal
a = []
for item in dir(cal):
    if not item.startswith('__'):
        a.append(item)
print(a)





#  Find  outputs
print(dir())			# list of directories
print()
import  cal
print()
print(dir())			# list of directories and cal also , [ ' ' , 'cal']





#  Find  outputs
print(dir())			# list of directories
print()
from  cal  import  *
print()
print(dir())			# [list of directories, 'x', 'y', 'add','sub','mul','div','c1']




#  Find  outputs
print(dir())				# list of directories
print()
from  cal  import  add , mul , x
print()
print(dir())				# [list of directories, 'x', 'add', 'mul']




# sys . path  demo   program
import  sys
print('Original  sys.path')		# Original sys.path
for  x  in   sys . path:
	print(x)			# [cwd, ' ', '']
print(len(sys . path))			# 7
#import  cal






from  random  import  *
print(random())				# 0.7935210661938715
print(randint(1 , 100))			# 91
print(uniform(1 , 100))			# 78.58453194445698
print(randrange(10))			# 6
print(randrange(1 , 11))		# 4
print(randrange(1 , 11 , 2))		# 5
list = [10 , 20 , 15 , 12 , 18]
print(choice(list))			# 20
print(choice('RAJESH'))			# R
set  =  {10 , 20 , 30 , 40}
print(choice(set))			# Error





'''
# Write  a  program  to  print  random  character  of  the  string  10  times (Home  work)
#Sample output:
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
#Program:
import random
n = input("Enter any string: ")
for i in range(10):
    print(random.choice(n))





'''
Write  a  program to  generate  10  passwords  each  of  6 character  length  where
1st , 3rd , 5th  characters  are  alphabets  and  2nd , 4th , 6th  characters   are  digits
#Sample output:
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

#Program:
import random
import string
for i in range(10):
    password = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    print(password)





'''
# Write  a  program  to  print  random  element  of  the  list  ten  times   (Home  work)
Enter a List : [25,10.8,'Hyd',True,3+4j,None]
#Sample output:
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

#Program:
import random
list = list(input("Enter the list of elements: "))
for i in range(10):
    print(random.choice(list))




'''
# Write  a  program  to  generate  ten  six-digit  OTP's  (Home  work)
#Sample output:
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

#Program:
import random
for i in range(10):
    otp = random.randint(100000, 999999)
    print(otp)





'''
Write  a  program to  open  any  website  from  gmail ,  google ,  rediff ,  ...   with  a  time  gap  of  5  to  20   sec

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
Write  a  program  to  implement  Rock , paper  and  scissors  game  between  user  and  computer

1) What  is  the  result  if  user  input  and  computer  random  number  are  same  ?  ---> Draw

2) What  is  the  result  if  computer  selects  paper  and  user  input  is  rock ?  --->
																												Computer  wins  becoz  parer  dominates  rock

3) What  is  the  result  if  computer  selects  scissors  and  user  input  is  paper ?  --->
																										Computer  wins  becoz  scissors  dominates  paper

4) What  is  the  result  if  computer  selects  rock  and  user  input  is  scissors ?  --->
																										Computer  wins  becoz  rock  dominates  scissors

5) What  is  the  result  in  all  other  cases  ?  --->  User  wins

#Sample output:
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