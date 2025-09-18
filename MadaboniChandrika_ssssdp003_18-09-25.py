'''def  add(a , b):
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
	print('Hyd')#Hyd
	print('Sec')#Sec
	print('Cyb')#Cyb

#2nd program
#  Find  outputs  (Home  work)
import  sys , time , math
print(dir(sys))#All the members of sys module
print()
print()
print(dir(time))#All the members of time module
print()
print(dir(math))#All the members of time module


#3rd program
#  Find  outputs  (Home  work)
import  cal
print(dir(cal))#All the members of cal module


#4th program
#  Find  outputs  (Home  work)
x = 25
def  disp():
	print('Hello')
class  c1:
        def  m1(self):
                pass
print(dir())#['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'c1', 'disp', 'x']
print(type(dir()))#<class'list'>
print(type(dir))#<class 'builtins function'>

#5th program
import cal

for member in dir(cal):
    if not member.startswith('__'):
        print(member)


#6th program
#  Find  outputs
print(dir())#['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'c1', 'disp', 'x']
print()
import  cal
print()
print(dir())#members are  not imported becoz we imported module

#7th program
#  Find  outputs
print(dir())#['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'c1', 'disp', 'x']
print()
from  cal  import  *
print()
print(dir())#All the members of cal module

#8th program
#  Find  outputs
print(dir())#['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'c1', 'disp', 'x']
print()
from  cal  import  add , mul , x
print()
print(dir())#add ,mul,x members of imported of cal  module


#9th program
# sys . path  demo   program
import  sys
print('Original  sys.path')#Original  sys.path
for  x  in   sys . path:
	print(x)#iterates throw all the members of sys module
print(len(sys . path))#6
#import  cal

#10th program
from  random  import  *
print(random())
print(randint(1 , 100))#selects some random integer b/w the range of 1,100
print(uniform(1 , 100))#selects some random number in the given range
print(randrange(10))#selects some random range
print(randrange(1 , 11))#selects some random range
print(randrange(1 , 11 , 2))
list = [10 , 20 , 15 , 12 , 18]
print(choice(list))#selects any element from the given list
print(choice('RAJESH'))#Selects any random letter from the string 
set  =  {10 , 20 , 30 , 40}
#print(choice(set))


#11th program(Write  a  program  to  print  random  character  of  the  string  10  times (Home  work))
from random import choice

s = input("Enter any string: ")
for _ in range(10):
    print(choice(s))

#12th program(# Generate 10 passwords)
import random
import string
for _ in range(10):
    password = ""
    for i in range(6):
        if i % 2 == 0:   
            password += random.choice(string.ascii_letters)
        else:         
            password += random.choice(string.digits)
    print(password)


#13th program(random element from the list)
import random
list=input('enter any list:')
for _ in range(10):
    print(random.choice(list))'''


#14th program(rock paper scissor game)
import random
choices=['rock','paper','scissor']
user_choice=input('what do you want to choose')
computer_choice=random.choice(choices)
print("computer choice:",computer_choice)
if computer_choice==user_choice:
       print('draw')
cont=input('do you want to continue')
y='yes'
n='no'
for ch in cont:
    if ch==y:
        print('what do you want to choose')
    if ch==n:
        print('ok quit the game')
if (user_choice=='rock' and computer_choice=='scissor') or (user_choice=='paper' and computer_choice=='rock') or (user_choice=='scissor' and computer_choice=='paper'):
        print('you win')
else:
     print('computer win ')



