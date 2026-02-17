#Tarun Banala         05-09-2025

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


def roman_to_arabic(roman):
    # Dictionary mapping Roman numerals to their values
    roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 
                   'C': 100, 'D': 500, 'M': 1000}
    
    # Reverse the string to process from right to left
    reversed_roman = roman[::-1]
    
    total = 0
    prev_value = 0
    
    for char in reversed_roman:
        current_value = roman_values[char]
        
        if current_value >= prev_value:
            total += current_value
        else:
            total -= current_value
        
        prev_value = current_value
    
    return total

# Test cases
test_cases = ["III", "IV", "IX", "LVIII", "MCMXCIV", "MMMCDXXIV"]

for roman in test_cases:
    arabic = roman_to_arabic(roman)
    print(f"{roman} -> {arabic}")


#example:
'''
Enter any roman number: MMMCDXXIV
o/p: 3424
'''
#exlanation:
'''  
Original: MMMCDXXIV
Reversed: V I X X D C M M M

V: 5 → total = 5, prev = 5

I: 1 (< 5) → total = 5 - 1 = 4, prev = 1

X: 10 (≥ 1) → total = 4 + 10 = 14, prev = 10

X: 10 (≥ 10) → total = 14 + 10 = 24, prev = 10

D: 500 (≥ 10) → total = 24 + 500 = 524, prev = 500

C: 100 (< 500) → total = 524 - 100 = 424, prev = 100

M: 1000 (≥ 100) → total = 424 + 1000 = 1424, prev = 1000

M: 1000 (≥ 1000) → total = 1424 + 1000 = 2424, prev = 1000

M: 1000 (≥ 1000) → total = 2424 + 1000 = 3424, prev = 1000

Now it correctly calculates to 3424 '''
