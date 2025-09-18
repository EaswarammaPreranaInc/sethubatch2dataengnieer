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
if  __name__ ==  '__main__':
	print('Hyd')
	print('Sec')
	print('Cyb')



1) What  is  the  module  name ?  --->  cal

2) py  cal.py
    What  is  the  value  of  __name__ ?  ---> '__main__'
    What  are  the  outputs ?  --->  Hyd ,  Sec  and  Cyb  becoz  if  condition  is  True

3) import  cal
    What  is  the  value  of  __name__ ?  ---> The  imported  module  name  i.e. 'cal'
	What  are  the  outputs ?  ---> Nothing  becoz  if  condition  is   False


 Find  outputs  (Home  work)
import  sys , time , math
print(dir(sys))#return the members of the sys module and environment variables
print()
print()
print(dir(time))#return the members of the time module
print()
print(dir(math))#return the members of math module

 #Find  outputs  (Home  work)
import  cal
print(dir(cal))#add,sub,mul,div,c1,x,y,__name__

 Find  outputs  (Home  work)
x = 25
def  disp():
	print('Hello')
class  c1:
        def  m1(self):
                pass
print(dir())#envirinment variables
print(type(dir()))#<class 'list'>
print(type(dir))#<class 'builtin_function_or_method>


Write  a  program  to  print  all  the  members  of  cal  module  without  environment  variables

1) What  is  the  result  of  '__name__' . startswith('__')  ?  ---> True

2) What  is  the  result  of  '__spec__' . endswith('__')  ?  --->  True

3) What  is  the  result  of  'spec__' . startswith('__')  ?  ---> False

4) a = []
    Append  all  the  elements  of  list  returned  by  dir()  function  to  list  'a'  except  environment  variables


import cal
a = []
for item in dir(cal):
	if not (item.startswith('--')and item.endswith('--')):
		a.append(item)
print("members of cal module(without environment variables)")
for item in a:
	print(a)

 Find  outputs
print(dir())#all environment variables
print()
import  cal
print()
print(dir())#environment variables,cal

 Find  outputs
print(dir())#environment variables
print()
from  cal  import  *
print()
print(dir())#environment variables,add,mul,sub,div,x

 Find  outputs
print(dir())#environment variables
print()
from  cal  import  add , mul , x
print()
print(dir())#environment variables,add,mul,x

# sys . path  demo   program
import  sys
print('Original  sys.path')#original sys.path
for  x  in   sys . path:
	print(x)#sys.path
print(len(sys . path))#6
#import  cal

Store  sample.py  module  in  c:\\sairam  folder  before  the  program  is  executed  (Home  work)
print(len(sys.path))#How  to  print  number  of  directories  (or)  folders  in  sys.path
sys.path.append(c:\sairam)#How  to  append  c:\sairam  folder  to  sys.path
print(len(sys.path))How  to  print  number  of  directories  (or)  folders  in  sys.path
import store sample as sample
print(sample.x)#How  to  print  object  'x'  of  sample   module  which  is  in  c:\sairam  folder
sample.f1#How  to  call   function  f1()  of  sample  module  which  is  in  c:\sairam  folder
a=sample.c1()
a.m1()#How  to  call   method  m1()  of  class  c1  of  sample  module  which  is  in  c:\sairam  folder


from  random  import  *
print(random())#print number 1 to 0 in float exclude 0 and 1
print(randint(1 , 100))#28
print(uniform(1 , 100))#80.85
print(randrange(10))#9
print(randrange(1 , 11))#7
print(randrange(1 , 11 , 2))#9
list = [10 , 20 , 15 , 12 , 18]
print(choice(list))#15
print(choice('RAJESH'))#j
set  =  {10 , 20 , 30 , 40}
print(choice(set))#error

Write  a  program  to  print  random  character  of  the  string  10  times (Home  work)
Enter  any  string :  Rama Rao
R

a
R
R
a
R
R
m

import random
s = input("enter string:")
print("\nRandom characters from the string")
for i in range(10):
    ch = random.choice(s)
    print(ch)
    
output:
R
a
 
o
m
 
r
a
a
a
Write  a  program to  generate  10  passwords  each  of  6 character  length  where
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

import random
import string

for i in range(10):  
    password = ""
    for pos in range(6):
        if pos % 2 == 0:  
            password += random.choice(string.ascii_letters)
        else:  
            password += random.choice(string.digits)
    print(password)

output:
e0Y0H5
P7i6i1
n2V2d3
a5H0v1
G3I4x6
j1h0L4
K0y3K9
X6B6t5
B4x9e3
D8M5p6


Write  a  program  to  print  random  element  of  the  list  ten  times   (Home  work)
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

import random
a = [25,10.8,'Hyd',True,3+4j,None]
for i in range(10):
  print(random.choice(a))
outputs:
True
25
Hyd
Hyd
10.8
25
True
(3+4j)
True
(3+4j)



Write  a  program  to  generate  ten  six-digit  OTP's  (Home  work)
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

import random 
for i in range(10):
   otp = random.randint(100000 , 999999) 
   print(otp)  

output:
401467
628605
524757
763075
458119
123146
450438
594225
675638
477353 


import webbrowser
import time
import random


sites = ['google.com', 'rediff.com', 'gmail.com', 'amazon.com', 'netflix.com']

for site in sites:
    webbrowser.open('http://' + site)  
    gap = random.randint(5, 20)  
    print(f"Opened {site}, waiting for {gap} seconds...")
    time.sleep(gap)  


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



import random
choices = ['rock', 'paper', 'scissors']
user = input("Enter your choice (rock/paper/scissors): ").lower()
computer = random.choice(choices)

print(f"Computer selected: {computer}")
if user == computer:
    print("Result: Draw")
elif (computer == 'paper' and user == 'rock') or \
     (computer == 'scissors' and user == 'paper') or \
     (computer == 'rock' and user == 'scissors'):
    print("Result: Computer wins")
else:
    print("Result: User wins")

output:
Enter your choice (rock/paper/scissors): rock
Computer selected: scissors
Result: User wins