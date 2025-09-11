'''
1) There  are  21  matchsticks.
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

How  many  matchsticks  would  you  like  to  pick (1 , 2 ,  3 or  4) ?  :  3
Computer  picks  2 matchsticks
How  many  matchsticks  would  you  like  to  pick (1 , 2 ,  3 or  4) ?  :  0
Input  can  not  be >  4  nor  <  1,  Reenter  :  1
Computer  picks  4 matchsticks
How  many  matchsticks  would  you  like  to  pick (1 , 2 ,  3 or  4) ?  :  2
Computer  picks  3 matchsticks
How  many  matchsticks  would  you  like  to  pick (1 , 2 ,  3 or  4) ?  :  5
Input  can  not  be >  4  nor  <  1,  Reenter  :  6
Input  can  not  be >  4  nor  <  1,  Reenter  :  7
Input  can  not  be >  4  nor  <  1,  Reenter  :  8
Input  can  not  be >  4  nor  <  1,  Reenter  :  4
Computer  picks  1 matchsticks
You  have  lost  the  game  and  Computer  wins

# Program
total=21
print("There are 21 matchsticks.")
print("Pick 1,2,3 or 4 matchsticks. whoever picks the last matchstick")
while total>1:
    user=int(input("Your Turn (1-4) :"))
    if user<1 or user > 4 or user>total:
        print("Invalid move. Try again.")
        continue
    total -=user
    print("Matchsticks Left :",total)
    
    comp=5-user
    if comp>total:
        comp=total-1
    print(F'Computer picks {comp}')
    total-=comp
    print("matchsticks left :",total)
    if total==1:
        print("You Left the last matchstick. you lose!")
        break
    

'''
2) Write  a  program  to  convert  roman number to  arabic  number

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
# Program
def roman_to_int(s):
    roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    total = 0
    i = 0
    while i < len(s):
        if i+1 < len(s) and roman[s[i]] < roman[s[i+1]]:
            total += roman[s[i+1]] - roman[s[i]]
            i += 2
        else:
            total += roman[s[i]]
            i += 1
    return total
s=input("Enter Roman Number :").upper()
print(roman_to_int(s))  # Output: 3878

Enter  any  roman  number :  MMMCDXXIV
3424
3)write a program to print number in words.
let input :123456789
output: Twelve crore thirty four lakhs fifty six thousand seven hundred eighty nine.

# Program
a=['','One','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Eleven','Twleve','Thirteen','Fourteen','Fifteen','Sixteen','Seventeen','Eighteen','Nineteen']
b=['','','Twenty','Thirty','Fourty','Fifty','Sixty','Seventy','Eighty','Ninety']
def words(n,units):
    if n>=20:
        print(b[n//10],a[n%10],end='')
    else:
        print(a[n],end='')
    if n>0:
        print(units,end='')
n=int(input("Enter Any Number :"))
if n==0:
    print("Zero")
else:
    words(n//10000000,'Crores')
    words(n//100000%100,'Lakhs')
    words(n//1000%100,'Thousand')
    words(n//100%10,'Hundred')
    words(n%100,'')
4) write a program to test a string is palindrome or not without using any pre-defined function or method such as reverse or reversed
hint : Reverse a string and input should be same.
# Program
s=input("Enter a String :").upper()
n=len(s)
is_palindrome=True
for i in range(n//2):
    if s[i]!=s[n-i-1]:
        is_palindrome=False
        break
if is_palindrome:
    print("Palindrome")
else:
    print("Not Palindrome")
5) Write a program to test a number is armstrong or not 

# Program
num=int(input("Enter a Number :"))
temp=num
n=len(str(num))
sum=0
while temp>0:
    digit=temp%10
    sum += digit ** n
    temp//=10
if sum==num:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")
6) Write a program to print following pyramid
     1
    123
   12345
  1234567
 123456789

# Program
n = int(input("Enter input: "))
for i in range(1, n + 1):
    print(' ' * (n-i-1),end=" ")
    for j in range(1,2*i):
        print(j, end=" ")
    print()
