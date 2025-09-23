# cal.py
def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    return a / b
class c1:
    def m1(self):
        pass
# End of the class
x = 100
y = 200
if __name__ == '__main__':
    print('Hyd')
    print('Sec')
    print('Cyb')


'''
1) What is the module name ?  ---> cal

2) py cal.py
    What is the value of __name__ ?  ---> '__main__'
    What are the outputs ?  ---> Hyd , Sec and Cyb because if condition is True

3) import cal
    What is the value of __name__ ?  ---> The imported module name i.e. 'cal'
    What are the outputs ?  ---> Nothing because if condition is False
'''


# ---------------------------------------------------------
# Find outputs (Home work)
import sys, time, math
print(dir(sys))                #Lists all names (functions, variables, classes, constants) inside the sys module.
print()
print()
print(dir(time))               #Lists all members of the time module
print()
print(dir(math))              #Lists all members of the math module


# ---------------------------------------------------------
# Find outputs (Home work)
import cal
print(dir(cal))         #path of file where it is stored 


# ---------------------------------------------------------
# Find outputs (Home work)
x = 25
def disp():
    print('Hello')
class c1:
    def m1(self):
        pass
print(dir())                  #Lists all members of the dir module
print(type(dir()))            #<class 'list'>
print(type(dir))              #<class 'builtin_function_or_method'>


# ---------------------------------------------------------
'''
Write a program to print all the members of cal module without environment variables

1) What is the result of '_name'.startswith('_') ?  ---> True

2) What is the result of '_spec'.endswith('_') ?  ---> True

3) What is the result of 'spec_'.startswith('_') ?  ---> False

4) a = []
   Append all the elements of list returned by dir() function to list 'a' except environment variables
'''


import cal

a = []
for name in dir(cal):
    if not name.startswith("_"):   
        a.append(name)

print(a)



# ---------------------------------------------------------
# Find outputs
print(dir())               #error
print()
import cal
print()
print(dir())              #Lists all members of the dir module


# ---------------------------------------------------------
# Find outputs
print(dir())                  #shows only environment variables.
print()
from cal import *
print()
print(dir())                 #all functions, class, and variables from cal.py


# ---------------------------------------------------------
# Find outputs
print(dir())                 #shows only environment variables.
print()
from cal import add, mul, x
print()
print(dir())                 #sows only specifc like add ,mul,x.


# ---------------------------------------------------------
# sys.path demo program
import sys
print('Original sys.path')
for x in sys.path:
    print(x)
print(len(sys.path))
# import cal


# ---------------------------------------------------------
# Store sample.py module in c:\sairam folder before the program is executed (Home work)
# c:\sairam\sample.py

# sample.py
x = 100

def f1():
    print("Hello from f1() in sample module")

class c1:
    def m1(self):
        print("Hello from m1() of class c1 in sample module")





#program

import sys

# 1) Print number of directories in sys.path
print("Before appending:")
print("Number of directories in sys.path =", len(sys.path))

# 2) Append c:\sairam to sys.path
sys.path.append(r"c:\sairam")

# 3) Print number of directories in sys.path again
print("\nAfter appending:")
print("Number of directories in sys.path =", len(sys.path))

# 4) Import sample module
import sample

# 5) Print object 'x' from sample module
print("\nValue of x from sample module:", sample.x)
# Output: 100

# 6) Call function f1() from sample module
sample.f1()
# Output: Hello from f1() in sample module

# 7) Call method m1() of class c1 of sample module
obj = sample.c1()
obj.m1()
# Output: Hello from m1() of class c1 in sample module


# ---------------------------------------------------------
from random import *

print(random())      # Output: A random float between 0.0 and 1.0 (e.g., 0.374829184)

print(randint(1, 100))   # Output: A random integer between 1 and 100 inclusive (e.g., 57)

print(uniform(1, 100))   # Output: A random float between 1 and 100 (e.g., 82.145732)

print(randrange(10))      # Output: Random integer from 0 to 9 (e.g., 6)

print(randrange(1, 11))    # Output: Random integer from 1 to 10 inclusive (e.g., 3)

print(randrange(1, 11, 2))  # Output: Random odd number from {1, 3, 5, 7, 9} (e.g., 7)

list = [10, 20, 15, 12, 18]
print(choice(list))         # Output: Random element from list (e.g., 15)

print(choice('RAJESH'))    # Output: Random character from the string (e.g., 'J')

set = {10, 20, 30, 40}
#print(choice(set))         #Error


# ---------------------------------------------------------
# Write a program to print random character of the string 10 times (Home work)


from random import choice

# Input string from user
s = input("Enter any string: ")

print("\nRandom characters:")
for _ in range(10):
    print(choice(s))


# ---------------------------------------------------------
# Write a program to generate 10 passwords each of 6 character length
# where 1st, 3rd, 5th characters are alphabets and 2nd, 4th, 6th characters are digits

import random
import string

print("Generated Passwords:")
for _ in range(10):     # Generate 10 passwords
    password = ""
    for i in range(6):
        if i % 2 == 0:  # 1st, 3rd, 5th positions (0,2,4) → alphabets
            password += random.choice(string.ascii_letters)   # a-z, A-Z
        else:           # 2nd, 4th, 6th positions (1,3,5) → digits
            password += random.choice(string.digits)          # 0-9
    print(password)

# ---------------------------------------------------------

# Write a program to print random element of the list ten times (Home work)
from random import choice

# Input a list from user
lst = eval(input("Enter a List: "))

print("\nRandom elements from the list:")
for i in range(10):
    print(choice(lst))



# ---------------------------------------------------------
# Write a program to generate ten six-digit OTP's (Home work)

from random import randint

print("Ten 6-digit OTPs:")

for i in range(10):
    print(randint(100000, 999999))

# ---------------------------------------------------------
'''
Write a program to open any website from gmail, google, rediff, ... with a time gap of 5 to 20 sec

1) What does open('http://google.com') do ?  ---> Opens google.com website

2) Where is open() function defined ?  ---> In webbrowser module

3) list = ['google.com', 'rediff.com', 'gmail.com', 'amazon.com', 'netflix.com']

4) Provide a time gap of 5 to 20 sec between the websites
'''
import webbrowser
import time
from random import randint

# List of websites
sites = ['google.com', 'rediff.com', 'gmail.com', 'amazon.com', 'netflix.com']

print("Opening websites with random delay between 5 to 20 seconds...")

for site in sites:
    webbrowser.open("http://" + site)   # Opens the website in default browser
    wait_time = randint(5, 20)          # Random delay between 5 to 20 seconds
    print(f"Waiting for {wait_time} seconds before opening next site...")
    time.sleep(wait_time)


# ---------------------------------------------------------
'''
(Home work)
Write a program to implement Rock, Paper and Scissors game between user and computer

1) What is the result if user input and computer random number are same ?  ---> Draw

2) What is the result if computer selects paper and user input is rock ?  
    ---> Computer wins because paper dominates rock

3) What is the result if computer selects scissors and user input is paper ?  
    ---> Computer wins because scissors dominates paper

4) What is the result if computer selects rock and user input is scissors ?  
    ---> Computer wins because rock dominates scissors

5) What is the result in all other cases ?  ---> User wins
'''
from random import randint

options = ["Rock", "Paper", "Scissors"]

print("Welcome to Rock, Paper, Scissors Game!")

while True:
    
    user = int(input("What do you want to select (0 - Rock, 1 - Paper, 2 - Scissors) : "))
    
    
    comp = randint(0, 2)
    
    print("User   :", options[user])
    print("Computer:", options[comp])
    
    
    if user == comp:
        print("Draw")
    elif (comp == 1 and user == 0) or (comp == 2 and user == 1) or (comp == 0 and user == 2):
        print("Computer wins")
    else:
        print("User wins")
    
    
    ch = input("Continue (y/n)? ")
    if ch.lower() != 'y':
        break

print("End of the game")
