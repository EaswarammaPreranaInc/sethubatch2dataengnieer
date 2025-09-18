from  random  import  * # import all the members of random module
print(random()) # returns a float between 0.0 and 0.1(exclusive)
print(randint(1 , 100)) # returns a random integer between 1 and 100(inclusive)
print(uniform(1 , 100)) # return a float between 1.0 and 100.0
print(randrange(10)) # random integer from 0 to 9
print(randrange(1 , 11)) # random integer from 1 to 10
print(randrange(1 , 11 , 2)) # random integer from 1 to 10 in step of 2
list = [10 , 20 , 15 , 12 , 18] 
print(choice(list)) # prints random element from list 
print(choice('RAJESH')) # prints random character from the string
set  =  {10 , 20 , 30 , 40}
#print(choice(set)) # error : cannot use set as it is not indexed 


# Write  a  program  to  print  random  character  of  the  string  10  times 
import random
a=input('Enter a string : ')
for i in range(1,11):
    print(choice(a))

'''
o/p:
Enter a string : Rama rao
o
a
m

R
R
a
a
a
'''


#Write a program to generate 10 passwords each of 6 character length where 1st , 3rd , 5th characters are alphabets and 2nd, 4th , 6th  characters   are  digits
import random
alphabets='abcdefghijklmnopqrstuvwxyz'
digits='0123456789'
for i in range(1,11):
    pw=''
    for i in range(1,7):
        if i%2!=0:
            pw+=random.choice(alphabets)
        else:
            pw+=random.choice(digits)
    print(pw)
'''
o/p:
p1q9r0
u0y6d5
d4p1o7
a9r2f7
v8u9e8
m5u8a6
b8x7m2
p2b7e2
v5s1n7
t4n4y9
'''



# Write  a  program  to  print  random  element  of  the  list  ten  times  
import random
a=eval(input("Enter a list: "))
for i in range(1,11):
    print(random.choice(a))

'''
o/p:
Enter a list: [25,10.8,'Hyd',True,3+4j,None]
25
10.8
Hyd
True
10.8
10.8
10.8
Hyd
25
10.8
'''



# Write  a  program  to  generate  ten  six-digit  OTP's  
import random
digits='0123456789'
for i in range(1,11):
    otp=''
    for j in range(1,7):
        otp+=random.choice(digits)
    print(otp)

'''
o/p:
754664
160060
858410
960640
207987
465431
588487
234027
292418
175887
'''



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
a = ['google.com', 'rediff.com' , 'gmail.com' , 'amazon.com' , 'netflix.com']
for i in a:
    webbrowser.open('http://'+i)
    t=random.randint(5,20)
    print(time.sleep(5))




'''
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
a=['Rock','Paper','Scissors']
while True:
    user=int(input("What do you want to select (0-Rock, 1-Paper, 2-Scissors): "))
    print('User : ',a[user])
    comp=random.randint(0,2)
    print('Computer : ',a[comp])
    if user==comp:
        print('Draw')
    elif (user==0 and comp==2) or (user==1 and comp==0) or (user==2 and comp==1):
        print("user wins")
    else:
        print("computer wins")
    b=input("continue (y/n)? ")
    if b!='y':
        print("End of the game")
        break

'''
o/p:
What do you want to select (0-Rock, 1-Paper, 2-Scissors): 1
User :  Paper
Computer :  Paper
Draw
continue (y/n)? y
What do you want to select (0-Rock, 1-Paper, 2-Scissors): 2
User :  Scissors
Computer :  Scissors
Draw
continue (y/n)? y
What do you want to select (0-Rock, 1-Paper, 2-Scissors): 0
User :  Rock
Computer :  Paper
computer wins
continue (y/n)? n
End of the game
'''

