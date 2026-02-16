

import sys
print(dir(sys))
# Output (partial):
# ['__breakpointhook__', '__displayhook__', '__doc__', '__excepthook__', '__interactivehook__',
#  '__loader__', '__name__', '__package__', '__spec__', '__stderr__', '__stdin__', '__stdout__',
#  'argv', 'exit', 'path', 'version', 'warnoptions']







import time
print(dir(time))
# Output (partial):
# ['CLOCK_BOOTTIME', 'CLOCK_MONOTONIC', 'CLOCK_MONOTONIC_RAW', 'CLOCK_PROCESS_CPUTIME_ID', 
#  'CLOCK_REALTIME', 'CLOCK_TAI', 'CLOCK_THREAD_CPUTIME_ID', '__doc__', 'altzone', 'asctime',
#  'ctime', 'gmtime', 'sleep', 'time', 'timezone', 'tzname', 'tzset']








import math
print(dir(math))
# Output (partial):
# ['__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'asin',
#  'atan', 'ceil', 'cos', 'degrees', 'e', 'exp', 'factorial', 'floor', 'fmod', 'frexp', 'gamma',
#  'gcd', 'hypot', 'inf', 'isfinite', 'isnan', 'log', 'log10', 'pi', 'pow', 'radians', 'sin',
#  'sqrt', 'tan', 'tau', 'trunc']







x = 25
def disp():
    print('Hello')
class c1:
    def m1(self):
        pass

print(dir())
# Output example:
# ['Any', 'BaseFormatter', 'E2BChartFormatter', 'E2BDataFormatter', 'E2BEnviron', 'Figure',
#  'IPython', 'Image', ..., 'c1', 'disp', 'math', 'sys', 'time', 'x']

print(type(dir()))
# Output:
# <class 'list'>

print(type(dir))
# Output:
# <class 'builtin_function_or_method'>








print('_name'.startswith('_'))
# Output: True

print('_spec'.endswith('_'))
# Output: True

print('spec_'.startswith('_'))
# Output: False







from random import random, randint, uniform, randrange, choice

print(random())        # Example Output: 0.6143126520586247
print(randint(1, 100)) # Example Output: 19
print(uniform(1, 100)) # Example Output: 38.313350624237174
print(randrange(10))   # Example Output: 5
print(randrange(1, 11))# Example Output: 2
print(randrange(1, 11, 2)) # Example Output: 1

lst = [10, 20, 15, 12, 18]
print(choice(lst))     # Example Output: 15
print(choice('RAJESH'))# Example Output: 'E'
print(choice(list({10, 20, 30, 40}))) # Example Output: 40








# 1. Print all members of a module (e.g., `cal`) excluding environment variables (starting with '_')


import cal  # Assuming cal module present

a = []
for item in dir(cal):
    if not item.startswith('_'):
        a.append(item)

print(a)

'''
Output :

['add', 'mul', 'sub', 'x', 'f1', 'c1']
'''








# 2. sys.path manipulation and sample module usage (assuming sample.py in c:\sairam)

import sys
print('Number of directories in sys.path:', len(sys.path))

sys.path.append(r'c:\sairam')
print('Number of directories in sys.path after append:', len(sys.path))

import sample  # sample.py must be in c:\sairam

print(sample.x)    # Prints variable x from sample module
sample.f1()        # Calls function f1 from sample module
obj = sample.c1()  # Creates instance of class c1
obj.m1()           # Calls method m1 of class c1
'''

Output (example):

Number of directories in sys.path: 10
Number of directories in sys.path after append: 11
25
Function f1 executed
Method m1 executed
'''






# 3. Print random character from string 10 times

from random import choice

s = input("Enter any string : ")
for _ in range(10):
    print(choice(s))
'''

Input:

Rama Rao

Output (sample):

R
a
R
R
a
R
R
m
a
o
'''








# 4. Generate 10 passwords each of 6 characters: 1st, 3rd, 5th alphabets; 2nd, 4th, 6th digits


from random import choice, randint
import string

for _ in range(10):
    pwd = []
    for i in range(6):
        if i % 2 == 0:
            pwd.append(choice(string.ascii_uppercase))
        else:
            pwd.append(str(randint(0, 9)))
    print(''.join(pwd))
'''

Output (example):

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





# 5. Print random element from a list 10 times

from random import choice

lst = eval(input("Enter a List : "))
for _ in range(10):
    print(choice(lst))
'''

Input:

[25, 10.8, 'Hyd', True, 3+4j, None]

Output (sample):

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






# 6. Generate ten six-digit OTPs

from random import randint

for _ in range(10):
    print(randint(100000, 999999))
'''

Output (example):

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






# 7. Open websites with 5 to 20 seconds delay between each

import webbrowser
import time
import random

websites = ['http://google.com', 'http://rediff.com', 'http://gmail.com', 'http://amazon.com', 'http://netflix.com']
for site in websites:
    webbrowser.open(site)
    time_gap = random.randint(5, 20)
    time.sleep(time_gap)







# 8. Rock-Paper-Scissors game between user and computer


import random

choices = {0: 'Rock', 1: 'Paper', 2: 'Scissors'}

while True:
    user_input = int(input("What do you want to select (0 - Rock, 1 - Paper, 2 - Scissors): "))
    computer_choice = random.randint(0, 2)
    print("User  : ", choices[user_input])
    print("Computer  : ", choices[computer_choice])

    if user_input == computer_choice:
        print("Draw")
    elif (computer_choice == 1 and user_input == 0) or \
         (computer_choice == 2 and user_input == 1) or \
         (computer_choice == 0 and user_input == 2):
        print("Computer wins")
    else:
        print("User wins")

    cont = input("Continue (y/n)? ")
    if cont.lower() != 'y':
        print("End of the game")
        break
'''

output:

What do you want to select (0 - Rock, 1 - Paper, 2 - Scissors) : 1
User  :  Paper
Computer  :  Rock
User wins
Continue (y/n)? y
What do you want to select (0 - Rock, 1 - Paper, 2 - Scissors) : 2
User  :  Scissors
Computer  :  Scissors
Draw
Continue (y/n)? y
What do you want to select (0 - Rock, 1 - Paper, 2 - Scissors) : 0
User  :  Rock
Computer  :  Rock
Draw
Continue (y/n)? y
What do you want to select (0 - Rock, 1 - Paper, 2 - Scissors) : 1
User  :  Paper
Computer  :  Scissors
Computer wins
Continue (y/n)? n
End of the game
'''



