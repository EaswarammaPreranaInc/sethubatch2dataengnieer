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
																	and  assign  prev  = correponding value
'''


def roman(s):
    d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    s = s.upper()[::-1]  
    total = 0
    prev = 0
    for ch in s:
        val = d[ch]
        if val >= prev:      
            total += val
        else:                
            total -= val
        prev = val
    return total
s = input("Enter any roman number : ")
print(roman(s))


'''
Enter  any  roman  number :  MMMCDXXIV
3424
'''
