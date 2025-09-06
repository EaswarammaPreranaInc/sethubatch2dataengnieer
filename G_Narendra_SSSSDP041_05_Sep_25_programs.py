'''
There  are  21  matchsticks.
User  can  pick  1 , 2 , 3  or  4  matchsticks.
Computer  picks  after  user  and  whoever  picks  the  last  matchstick, they  lose  the  game.
Write  a  program  such  that  computer  wins

Logic:  Total  should  be  5

Hint: Use while  loop

						n = 21
   Iteration     user         computer             n
-------------------------------------------------------------
         1               2                 3               n = 21 - 5 = 16

		 2              3                 2               n = 16 - 5 = 11

		 3              1                 4               n = 11 - 5 = 6

		 4              4                 1               n =6 - 5 = 1
---------------------------------------------------------------
'''
n = 21
while n > 1:
    user = int(input('Enter 1, 2, 3 or 4 matchsticks: '))
    if user < 1 or user > 4:
        print('Invalid input, try again')
        continue
    computer = 5 - user
    n -= (user + computer)
    print(f'Computer picked {computer} matchsticks, remaining matchsticks: {n}')
print('Computer wins')
# End of the game

'''
Write  a  program  to  convert  roman number to  arabic  number

1) What is the output  if input is  III ? --->  3

2) What is the output if input is  IV --->  4

3) What is the output if input is  IX --->  9

4) What is the output if input is  LVIII --->  58

5) What is the output if input is MCMXCIV ---> 1994

6) What is the output  if  input  is  MMMCDXXIV --->  3424

7) Reverse  the  string

8) {'I' : 1  , 'V' : 5 , 'X' : 10 , 'L' : 50 , 'C' : 100 ,  'D' : 500 , 'M' : 1000}
    What  action  to   be  made  if  the  char  is  >=  prev ?  --->  Add  the  corresponding  value  to  sum
																							       and  assign  prev  = correponding  value

9) What  action  to   be  made  if  the  char  is  <  prev ?  --->  Subtract  the  corresponding  value  from  sum
																							      and  assign  prev  = correponding  value
'''
s = input('Enter roman number: ')
roman_to_int = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
sum = 0     
prev = 0
for char in reversed(s):
    if roman_to_int[char] >= prev:
        sum += roman_to_int[char]
        prev = roman_to_int[char]
    else:
        sum -= roman_to_int[char]
        prev = roman_to_int[char]   
print(f'The arabic number is: {sum}')       
# End of the program