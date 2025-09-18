#  Find  outputs  (Home  work)
import  sys , time , math
print(dir(sys))
print()
print()
print(dir(time))
print()
print(dir(math))




#  Find  outputs  (Home  work)
import  cal
print(dir(cal))                 # ['__builtins__', '__cached__', '__doc__', '__file__','__loader__', '__name__', '__package__', '__spec__', 'add', 'sub']



#  Find  outputs  (Home  work)
x = 25
def  disp():
	print('Hello')
class  c1:
        def  m1(self):
                pass
print(dir())                 # ['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'c1', 'disp', 'x']
print(type(dir()))           # <class 'list'>
print(type(dir))             # <class 'builtin_function_or_method'>




'''
Write  a  program  to  print  all  the  members  of  cal  module  without  environment  variables

1) What  is  the  result  of  '_name' . startswith('_')  ?  ---> True

2) What  is  the  result  of  '_spec' . endswith('_')  ?  --->  True

3) What  is  the  result  of  'spec_' . startswith('_')  ?  ---> False

4) a = []
    Append  all  the  elements  of  list  returned  by  dir()  function  to  list  'a'  except  environment  variables
'''



import cal   

a = []

for name in dir(cal):
    
    if not (name.startswith('__') and name.endswith('__')):
        print(name)      
        a.append(name)   

print()
print("Filtered list:", a)



#  Find  outputs
print(dir())            # ['__annotations__', '__builtins__', '__doc__',  '__loader__', '__name__', '__package__', '__spec__',  'cal']
print()
import  cal
print()
print(dir())            # ['__annotations__', '__builtins__', '__doc__',  '__loader__', '__name__', '__package__', '__spec__',  'cal']




#  Find  outputs
print(dir())            # ['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__']
print()
from  cal  import  *
print()
print(dir())            # ['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__','add','sub','x']



#  Find  outputs
print(dir())                # ['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__']
print()
from  cal  import  add , mul , x
print()
print(dir())                # ['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'add', 'mul', 'x']




# sys . path  demo   program
import  sys
print('Original  sys.path')             # original sys.path
for  x  in   sys . path:
	print(x)
print(len(sys . path))                  # 5
#import  cal


# sys . path  demo   program
import  sys
print('Original  sys.path')
for  x  in   sys . path:
	print(x)
print(len(sys . path)) 



from  random  import  *
print(random())                     # 0.37482
print(randint(1 , 100))             # 57
print(uniform(1 , 100))             # 23.891233
print(randrange(10))                # 6
print(randrange(1 , 11))            # 4
print(randrange(1 , 11 , 2))        # 7
list = [10 , 20 , 15 , 12 , 18]
print(choice(list))                 # maybe 20
print(choice('RAJESH'))             # 'A'
set  =  {10 , 20 , 30 , 40}
print(choice(set))                  # Error




# Write  a  program  to  print  random  character  of  the  string  10  times (Home  work)
import random
Str = input("Enter a string : ") 
for i in range(10):
    print(random.choice(Str)) 



#Write  a  program to  generate  10  passwords  each  of  6 character  length  where
#1st , 3rd , 5th  characters  are  alphabets  and  2nd , 4th , 6th  characters   are  digits

import random
import string

for _ in range(10):  
    password = ""
    for i in range(6):
        if i % 2 == 0:   
            password += random.choice(string.ascii_letters)  
        else:            
            password += ** random.choice(string.digits)         
    print(password)



# Write  a  program  to  print  random  element  of  the  list  ten  times   (Home  work)

import random 
list = eval(input("Enter a list : ")) 
for i in range(10):
    print(random.choice(list))





#Write  a  program  to  generate  ten  six-digit  OTP's  (Home  work)

import random 
for i in range(10):
    s = ''
    for j in range(6):
        s += str(random.randint(0,9))
    print(s)




# Write  a  program to  open  any  website  from  gmail ,  google ,  rediff ,  ...   with  a  time  gap  of  5  to  20   sec

import random ,time, webbrowser
list = ['google.com' , 'rediff.com' , 'gmail.com' , 'amazon.com' , 'netflix.com']
for i in range(len(list)):
    webbrowser.open(list[i])
    time.sleep(random.randint(5,20))




#Write  a  program  to  implement  Rock , paper  and  scissors  game  between  user  and  computer

import random 
dict = {0 : 'Rock' , 1 : 'Paper' , 2 : 'Scissors'}
continuee = 'Y'
while continuee == 'Y':
    user = int(input("What  do  you  want  to  select  (0 - Rock , 1 - Paper , 2 - Scissors)  : "))
    print(f'User : {dict[user]}')
    computer = random.choice(dict)
    print(f'Computer : {computer}')
    if (user == 0 and computer == dict[0]) or (user == 1 and computer == dict[1]) or (user == 2 and computer == dict[2]):
        print("Draw")
    elif (user == 0 and computer == dict[1]) or (user == 1 and computer == dict[2]) or (user == 2 and computer == dict[0]):
        print("Computer wins")
    else:
        print("User wins")
    continuee = input("Continue  (  y / n)  ? ").upper()
print("End of the game")