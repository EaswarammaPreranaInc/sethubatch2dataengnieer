'''
Write  a  program  to  add ,  subtract , multiply  and  divide  two  complex  numbers
First  complex  number   --->  3 + 4j
2nd   complex  number   --->  5 + 6j
What  is  the  sum ? ---> (3 + 4j) + (5 + 6j) = 8 + 10j
What  is  the  difference ?  ---> (3 + 4j) - (5 + 6j) =  -2 - 2j
What  is  the  product ?  ---> (3 + 4j) * (5 + 6j) =  15 + 18j + 20j - 24 =  -9 + 38j
What  is  the  division ?  ---> (3 + 4j) / (5 + 6j) = (3 + 4j) * (5 - 6j) / (5 + 6j) * (5 -6j)
                                                                         =   (15 - 18j + 20j + 24) / (25 + 36)
																 = 39 / 61 + 2j / 61							   
'''
# Identify  error
else:
		print('else  suite')
print('Outside')   
	Without  ‘ if ‘  statement ‘else ‘  which is not executed 

# Identify  error
if  9 > 5
	print('Hello')
print('Bye')  
	 After   ‘if’   statement  “ : “ is mandatory 
# Identify  error
if  9 > 12:
	print('Hyd')
else
	print('Sec')
	After ‘else’ statement  “:” is mandatory 

# Identify  error
if  (10,20,15):
print('Hyd')
else:
print('Sec')
	After condition decleration , new line or block of code must be after space weather its ‘if’ or ‘else ‘  after

# Identify  error
if  ():
			print('Hyd')
	else:
					print('Sec')
print('Bye')
	After ‘if’  statement else part decleration also be in same line as per if () block whih doesn’t exceed line then if  

# Identify  error
if  { }:
{
	print('One')
	print('Two')
	print('Three')
}
else:
{
	print('Four')
	print('Five')
	print('Six')
}
print('Bye')
	Condition between ‘if’ and else blocks always follows or not followed by only “  ( ) “ or not with “ ( )” condition doesn’t defines by  “  {   }   “

# Identify  error
if  ():
	print('One')
	print('Two')
	print('Three')
else:
#error 
# after else statement “if” statement which starts from after space on next line , doesn’t on sameline 
if  []:        
	print('Four')
	print('Five')
	print('Six')
else:
if  {}:
	print('Seven')
	print('Eight')
	print('Nine')
else:
	print('Hyd')
	print('Sec')
	print('Cyb')
print('Bye')
#error 
	Hyd  Sec Cyb Bye //all conditions are non empty strings which returns false 
	# after else statement “if” statement which starts from after space on next line , doesn’t on sameline

# Write  a  program  to  determine  a  number  is  even  or  odd  with   if  statement

#even or odd 
n=eval(input("enter any number "))
if n%2==0:
    print(f"{n} is an Even Number")
else:
    print(f"{n} is an Odd Number ")

output:
enter any number 11
11 is an Odd Number 
PS F:\>
# Find outputs  (Home  work)
if():
        print('Hyd')
        print('Sec')
        print('Cyb')
else:
        print('One')
        print('Two')
        print('Three')
print('Bye')

output:   One Two Three Bye   // because its an non empty string with no arguments 

# Find  outputs  (Home  work)
if{10 : 20 , 30 : 40}:
        print('Hyd')
        print('Sec')
        print('Cyb')
print('Bye')   

output  :   Hyd  Sec Cyb Bye 

# Find outputs  (Home  work)
if { }:
	print('Hyd')
	print('Sec')
	print('Cyb')
print('Bye')  
output :
	Bye // its non empty string and always Bye executed weather  condition is  true or false 

# Write   a  program  to  print  month  name  for  input  month  number  by  using  if  and  elif  (Home  work)
#month
import calendar
m = int(input("Enter month number: "))
if m>=1 and m<=12:
    name = calendar.month_name[m]
    print(f"Month name: {name}")
else:
    print("Enter month number within 12 months")

:output : Enter month number: 8
Month name: August
Write  a  program  to  print  digit  in  words  with  else  and  if  (do  not  use  elif)
0 - Zero
1 - One
2 - Two
....
9 - Nine
10 – Invalid

import math
n=int(input("enter any digit : ")) 

# if n>=0 and n<=9 :
#      if n==0:
#          print("ZERO")
#      if n==1:
#          print("ONE")
#      if n==2:
#          print("TWO")
#      if n==3:
#          print("THREE")
#      if n==4:
#          print("FOUR")
#      if n==5:
#          print("FIVE")
#      if n==6:
#          print("SIX")
#      if n==7:
#          print("SEVEN")
#      if n==8:
#          print("EIGHT")
#      if n==9:
#          print("NINE")
# else:
#     print(" enter valid digit below 9 ")
try:
    if n==0:
         print("ZERO")
    else:    
     if n==1:
         print("ONE")
     else:
          if n==2:
             
           print("TWO")
          else:
           if n==3:
            print("THREE")
           else:
    
             if n==4:
              print("FOUR")
             else:
    
              if n==5:
               print("FIVE")
     
              if n==6:
                print("SIX")
              else:
         
               if n==7:
                print("SEVEN")
               else:
     
                if n==8:
                  print("EIGHT")
                else:
    
                 if n==9:
                   print("NINE")
except:
   print("enter valid input ")
     
     


