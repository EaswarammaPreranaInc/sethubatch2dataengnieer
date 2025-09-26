 # cal.py
def add(a , b):
 return a + b
def sub(a , b):
 return a - b
def mul(a , b):
 return a * b
def div(a , b):
 return a / b
class c1:
 def m1(self):
  pass
#End of the class
x = 100
y = 200
if __name__ == '__main__':
 print('Hyd')
 print('Sec')
 print('Cyb')


'''
1) What is the module name ? ---> cal

2) py cal.py
    What is the value of __name__ ? ---> '__main__'
    What are the outputs ? ---> Hyd , Sec and Cyb becoz if condition is True

3) import cal
    What is the value of __name__ ? ---> The imported module name i.e. 'cal'
 What are the outputs ? ---> Nothing becoz if condition is False
'''
 cal.py is not a home work
 
 
#1
#Find outputs (Home work)
import sys , time , math
print(dir(sys))
print()
print()
print(dir(time))
print()
print(dir(math))

o/p
"""
['__breakpointhook__', '__displayhook__', '__doc__', '__excepthook__',
 '__interactivehook__', '__loader__', '__name__', '__package__',
 '__spec__', '__stderr__', '__stdin__', '__stdout__', '__unraisablehook__',
 '_base_executable', '_clear_type_cache', '_current_exceptions',
 '_current_frames', '_debugmallocstats', '_framework', '_getframe',
 ...]
 
 ['CLOCK_BOOTTIME', 'CLOCK_MONOTONIC', 'CLOCK_MONOTONIC_RAW',
 'CLOCK_PROCESS_CPUTIME_ID', 'CLOCK_REALTIME', 'CLOCK_TAI',
 'CLOCK_THREAD_CPUTIME_ID', '_STRUCT_TM_ITEMS', '__doc__',
 '__loader__', '__name__', '__package__', '__spec__', 'altzone',
 'asctime', 'clock_getres', 'clock_gettime', 'clock_gettime_ns',
 'clock_settime', 'clock_settime_ns', 'ctime', 'daylight',
 'get_clock_info', 'gmtime', 'localtime', 'mktime', 'monotonic',
 'monotonic_ns', 'perf_counter', 'perf_counter_ns', 'process_time',
 ...]
 
 ['__doc__', '__file__', '__loader__', '__name__', '__package__',
 '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2',
 'atanh', 'cbrt', 'ceil', 'comb', 'copysign', 'cos', 'cosh',
 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'exp2', 'expm1',
 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma',
 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', ...]


#2
# Find outputs (Home work)
import cal
print(dir(cal))
"""
['__doc__', '__loader__', '__name__', '__package__', '__spec__',
 'add', 'c1', 'div', 'mul', 'sub', 'x', 'y']

#3
# Find outputs (Home work)
x = 25
def disp():
 print('Hello')
class c1:
        def m1(self):
                pass
print(dir())
print(type(dir()))
print(type(dir))


"""
['__annotations__', '__builtins__', '__doc__', '__loader__',
 '__name__', '__package__', '__spec__',
 'c1', 'disp', 'x']

<class 'list'>
<class 'builtin_function_or_method'>
"""

'''
Write a program to print all the members of cal module without environment variables

1) What is the result of '__name__' . startswith('__') ? ---> True

2) What is the result of '__spec__' . endswith('__') ? ---> True

3) What is the result of 'spec__' . startswith('__') ? ---> False

4) a = []
    Append all the elements of list returned by dir() function to list 'a' except environment variables
'''


#4
# Find outputs
print(dir())
print()
import cal
print()
print(dir())
"""
['__annotations__', '__builtins__', '__doc__',
 '__loader__', '__name__', '__package__', '__spec__']

['__annotations__', '__builtins__', '__doc__',
 '__loader__', '__name__', '__package__', '__spec__', 'cal']
 """


#5
# Find outputs
print(dir())
print()
from cal import *
print()
print(dir())
"""
['__annotations__', '__builtins__', '__doc__',
 '__loader__', '__name__', '__package__', '__spec__']

['__annotations__', '__builtins__', '__doc__',
 '__loader__', '__name__', '__package__', '__spec__',
 'add', 'c1', 'div', 'mul', 'sub', 'x', 'y']

"""

#6
# Find outputs
print(dir())
print()
from cal import add , mul , x
print()
print(dir())

"""
['__annotations__', '__builtins__', '__doc__',
 '__loader__', '__name__', '__package__', '__spec__']

['__annotations__', '__builtins__', '__doc__',
 '__loader__', '__name__', '__package__', '__spec__',
 'add', 'mul', 'x']
 """


#7
# sys . path demo program
import sys
print('Original sys.path')
for x in sys . path:
 print(x)
print(len(sys . path))
#import cal

#8
# Store sample.py module in c:\\sairam folder before the program is executed (Home work)
How to print number of directories (or) folders in sys.path
How to append c:\sairam folder to sys.path
How to print number of directories (or) folders in sys.path
How to print object 'x' of sample module which is in c:\sairam folder
How to call function f1() of sample module which is in c:\sairam folder
How to call method m1() of class c1 of sample module which is in c:\sairam folder
import sys

# 1. Print number of directories in sys.path
print("Before appending:", len(sys.path))

# 2. Append "C:\\sairam" folder to sys.path
sys.path.append("C:\\sairam")

# 3. Print number of directories in sys.path again
print("After appending:", len(sys.path))

# 4. Import sample module from C:\sairam
import sample

# 5. Print object 'x'
print("Value of x:", sample.x)

# 6. Call function f1()
sample.f1()

# 7. Call method m1() of class c1
obj = sample.c1()
obj.m1()



#9
from random import *
print(random())                           #0.374820146984
print(randint(1 , 100))                   #45
print(uniform(1 , 100))                   #4.5
print(randrange(10))                      #5
print(randrange(1 , 11))                  #6
print(randrange(1 , 11 , 2))              #9
list = [10 , 20 , 15 , 12 , 18]
print(choice(list))                       #12
print(choice('RAJESH'))                   #R
set = {10 , 20 , 30 , 40}
print(choice(set))                        #20


#10
# Write a program to print random character of the string 10 times (Home work)

n=input("Enter the string:")
import random as r
for i in range(10):
    print(r.choice(n))

 Enter any string : Rama Rao
R

a
R
R
a
R
R
m


#11.# Write a program to generate 10 passwords each of 6 character length where
1st , 3rd , 5th characters are alphabets and 2nd , 4th , 6th characters are digits

import random
import string


# alphabets (both upper and lower case)
letters = string.ascii_letters.upper()
#print(letters)
digits = string.digits
#print(digits)
for i in range(10):
    st=''
    for i in range(2,8):
        if i%2==0:
            st=st+random.choice(digits)   # 2nd digit
        else:
            st=st+random.choice(letters)   # 1st alphabet
    print(st)

: U7U2X8
V9I6X8
G4M8S2
M4U3C3
I7K2B8
F0E9Q1
Y8H8L7
K1U5S0
W7G0J3
Y9B9J6


#12# Write a program to print random element of the list ten times (Home work)
lst=eval(input("enter the string:"))
import random as r
for i in range(10):
    print(r.choice(lst)) 

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


#13
# Write a program to generate ten six-digit OTP's (Home work)
import random


for i in range(10):
    otp = random.randint(100000, 999999)  # ensures 6-digit number
    print(otp)

: 700690
664735
472299
820818
886311
912752
323114
971162
930848
404338


#14 '''
Write a program to open any website from gmail , google , rediff , ... with a time gap of 5 to 20 sec

1) What does open('http://google.com') do ? ---> Opens google.com website

2) Where is open() function defined ? ---> In webbrowser module

3) list = ['google.com' , 'rediff.com' , 'gmail.com' , 'amazon.com' , 'netflix.com']

4) Provide a time gap of 5 to 20 sec between the websites
'''
import webbrowser
import time
import random

sites = [
    "http://google.com",
    "http://rediff.com",
    "http://gmail.com",
    "http://amazon.com",
    "http://netflix.com"
]

print("Starting to open sites...")

for site in sites:
    print(f"Opening: {site}")
    webbrowser.open(site)  # open URL in default browser
    # choose a random integer delay between 5 and 20 seconds (inclusive)
    delay = random.randint(5, 10)
    print(f"Sleeping for {delay} seconds...\n")
    time.sleep(delay)

print("Done.")


#15
'''
(Home work)
Write a program to implement Rock , paper and scissors game between user and computer

1) What is the result if user input and computer random number are same ? ---> Draw

2) What is the result if computer selects paper and user input is rock ? --->
                            Computer wins becoz parer dominates rock

3) What is the result if computer selects scissors and user input is paper ? --->
                          Computer wins becoz scissors dominates paper

4) What is the result if computer selects rock and user input is scissors ? --->
                          Computer wins becoz rock dominates scissors

5) What is the result in all other cases ? ---> User wins
'''


What do you want to select (0 - Rock , 1 - Paper , 2 - Scissors) : 1
User : Paper
Computer : Rock
User wins
Continue ( y / n) ? y
What do you want to select (0 - Rock , 1 - Paper , 2 - Scissors) : 2
User : Scissors
Computer : Scissors
Draw
Continue ( y / n) ? y
What do you want to select (0 - Rock , 1 - Paper , 2 - Scissors) : 0
User : Rock
Computer : Rock
Draw
Continue ( y / n) ? y
What do you want to select (0 - Rock , 1 - Paper , 2 - Scissors) : 1
User : Paper
Computer : Scissors
Computer wins
Continue ( y / n) ? n
End of the game

import random

# mapping numbers to choices
choices = ["Rock", "Paper", "Scissors"]

while True:
    # user input
    user_input = int(input("What do you want to select (0 - Rock , 1 - Paper , 2 - Scissors) : "))
    user_choice = choices[user_input]

    # computer random choice
    comp_input = random.randint(0, 2)
    comp_choice = choices[comp_input]

    # show selections
    print(f"User : {user_choice}")
    print(f"Computer : {comp_choice}")

    # decide result
    if user_input == comp_input:
        print("Draw")
    elif (comp_input == 1 and user_input == 0):   # Paper vs Rock
        print("Computer wins")
    elif (comp_input == 2 and user_input == 1):   # Scissors vs Paper
        print("Computer wins")
    elif (comp_input == 0 and user_input == 2):   # Rock vs Scissors
        print("Computer wins")
    else:
        print("User wins")

    # continue or not
    ch = input("Continue ( y / n) ? ")
    if ch.lower() != 'y':
        print("End of the game")
        break
