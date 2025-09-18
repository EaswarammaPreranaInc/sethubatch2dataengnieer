# 1)Write  a  program  to  print  random  character  of  the  string  10  times (Home  work)
from random import*
a=input ('enter a string:')
for i in range(10):
 print(choice(a))

'''
output:
enter a string:karuna
k
a
u
a
a
a
r
u
u
n
''' 



'''
Write  a  program to  generate  10  passwords  each  of  6 character  length  where
1st , 3rd , 5th  characters  are  alphabets  and  2nd , 4th , 6th  characters   are  digits
'''

from random import *
S='GFDASKHJILBVNMLKJTY'
num='1234567890'
for i in range(10):
 pwd=''
 for j in range(1,7):
  if i%2==0:
   pwd+=choice(num)
  else:
   pwd+=choice(S) 
print(pwd) 

 


# Write  a  program  to  print  random  element  of  the  list  ten  times   (Home  work)
from random import *
a=eval(input('enter any list:'))
for i in a:
 print(choice(a))

'''
o\p:
enter any list:[25,10.8,'Hyd',True,3+4j,None]
True
True
25
25
None
10.8
''' 



# Write  a  program  to  generate  ten  six-digit  OTP's  (Home  work)

from random import*
for i in range(10):
 for j in range(6):
  print(randint(0,9),end='')
 print()
'''
o\p:
234784
486620
583549
455311
859899
475454
378179
348991
793922
281614
'''

'''
Write  a  program to  open  any  website  from  gmail ,  google ,  rediff ,  ...   with  a  time  gap  of  5  to  20   sec

1) What  does  open('http://google.com')  do ?  ---> Opens  google.com  website

2) Where  is  open()  function  defined  ?  ---> In  webbrowser  module

3) list = ['google.com' , 'rediff.com' , 'gmail.com' , 'amazon.com' , 'netflix.com']

4) Provide  a  time  gap  of  5  to  20 sec  between  the  websites
'''
import time
from random import*
import webbrowser
list=['google.com' , 'rediff.com' , 'gmail.com' , 'amazon.com' , 'netflix.com']
for i  in list:
 webbrowser.open(i)
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
from random import *
list=['Rock','Paper','Scissors']
a=True
while a:
    n=int(input("What  do  you  want  to  select  (0 - Rock , 1 - Paper , 2 - Scissors) : "))
    User=list[n]
    Computer=choice(list)
    if Computer=='Paper' and User=='Rock' or Computer=='Scissors' and User=='Paper' or Computer=='Rock' and User=='Scissors':
        print(F'User : {User}')
        print(F'Computer : {Computer}')
        print('Computer wins')
    elif Computer==User:
        print(F'User : {User}')
        print(F'Computer : {Computer}')
        print('Draw')
    else:
        print(F'User : {User}')
        print(F'Computer : {Computer}')
        print('User wins')
    b=input('Continue  (  y / n)  ? ')
    if b=='y':
        continue
    else:
        a=False
print('End of the game')






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
	if not (i.startswith("") and i.endswith("")):
		a.append(i)
print(a)