

'''
Write  a  program  to  print  all  the  members  of  cal  module  without  environment  variables

1) What  is  the  result  of  'name' . startswith('')  ?  ---> True

2) What  is  the  result  of  'spec' . endswith('')  ?  --->  True

3) What  is  the  result  of  'spec_' . startswith('_')  ?  ---> False

4) a = []
    Append  all  the  elements  of  list  returned  by  dir()  function  to  list  'a'  except  environment  variables
'''
import calendar


a = []

for item in dir(calendar):
    if not item.isupper():
        a.append(item)

# Print the filtered list
print("Filtered members of calendar module:")
for member in a:
    print(member)


----------------------------------------------------------------------------------------------

# Write  a  program  to  print  random  character  of  the  string  10  times (Home  work)

import random

# Define your string
my_string = "HomeworkIsFun"


for _ in range(10):
    random_char = random.choice(my_string)
    print(random_char)

---------------------------------------------------------------------------------


# Write  a  program to  generate  10  passwords  each  of  6 character  length  where
# 1st , 3rd , 5th  characters  are  alphabets  and  2nd , 4th , 6th  characters   are  digits
import random
import string

# Generate 10 passwords
for _ in range(10):
    password = ""
    for i in range(6):
        if i % 2 == 0:  # Even index → 0, 2, 4 → Alphabet
            password += random.choice(string.ascii_letters)
        else:           # Odd index → 1, 3, 5 → Digit
            password += random.choice(string.digits)
    print(password)


---------------------------------------------------------------------------------------
# Write  a  program  to  print  random  element  of  the  list  ten  times   (Home  work)
import random

# Define your list
my_list = [25,10.8,'Hyd',True,3+4j,None]


for _ in range(10):
    print(random.choice(my_list))
----------------------------------------------------------------------------------------
# Write  a  program  to  generate  ten  six-digit  OTP's  (Home  work)

import random

# Generate 10 OTPs
for _ in range(10):
    otp = random.randint(100000, 999999)
    print(otp)


-----------------------------------------------------------------------------------------
''' Write  a  program to  open  any  website  from  gmail ,  google ,  rediff ,  ...   with  a  time  gap  of  5  to  20   sec
- What  does  open('http://google.com')  do ?  ---> Opens  google.com  website
- Where  is  open()  function  defined  ?  ---> In  webbrowser  module
- list = ['google.com' , 'rediff.com' , 'gmail.com' , 'amazon.com' , 'netflix.com']
- Provide  a  time  gap  of  5  to  20 sec  between  the  websites '''
import webbrowser
import time
import random

# List of websites
websites = ['google.com', 'rediff.com', 'gmail.com', 'amazon.com', 'netflix.com']

# Open each website with a random delay
for site in websites:  
    webbrowser.open(f'http://{site}')
    delay = random.randint(5, 10)
    print(f"Opened {site}, waiting {delay} seconds before next...")
    time.sleep(delay)


---------------------------------------------------------------------------------------------------
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


import random

# Choices available
choices = ['rock', 'paper', 'scissors']

# Get user input
user_choice = input("Enter your choice (rock, paper, scissors): ").lower()

# Get computer's random choice
computer_choice = random.choice(choices)

print(f"Computer chose: {computer_choice}")

# Determine the result
if user_choice == computer_choice:
    print("Result: Draw")
elif (computer_choice == 'paper' and user_choice == 'rock') or \
     (computer_choice == 'scissors' and user_choice == 'paper') or \
     (computer_choice == 'rock' and user_choice == 'scissors'):
    print("Result: Computer wins because", computer_choice, "dominates", user_choice)
elif user_choice in choices:
    print("Result: You win!")
else:
    print("Invalid input. Please choose rock, paper, or scissors.")



                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       