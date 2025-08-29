#Write  a  program  to  add ,  subtract , multiply  and  divide  two  complex  numbers

a = eval(input("Enter 1st complex number: "))
b = eval(input("Enter 2nd complex number: "))
print(F'{a} + {b} = {a+b}')
print(F'{a} - {b} = {a-b}')
print(F'{a} * {b} = {a*b}')
print(F'{a} / {b} = {a/b}')

'''
Output:

Enter 1st complex number: 3+4j
Enter 2nd complex number: 5+6j
(3+4j) + (5+6j) = (8+10j)
(3+4j) - (5+6j) = (-2-2j)
(3+4j) * (5+6j) = (-9+38j)
(3+4j) / (5+6j) = (0.6393442622950819+0.03278688524590165j)
'''

# Identify  error
'''
else:			# we cannot use else without if
	print('else  suite')
print('Outside')
'''

# Identify  error

if  9 > 5: #Here the ':' is missing as it is mandatory
	print('Hello') 
print('Bye')



# Identify  error

if  9 > 12:
	print('Hyd')
else:                   # Here the ':' is missing for else as it is mandatory  
	print('Sec')



# Identify  error
if  (10,20,15):
#print('Hyd')          # Indentation Error we it should have indentation
#else:
#print('Sec')



# Identify  error     
#if  ():			# Here if and else should be in same indentation
			print('Hyd')
	#else:		
					#print('Sec')
print('Bye')



# Identify  error  
'''		
if  { }:  
{		   			# Here {} are not allowed so it give error
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
'''



# Identify  error
if  ():
	print('One')
	print('Two')
	print('Three')
else:
#if  []:				#here the inner if and else statement should have indentation  
	print('Four')
	print('Five')
	print('Six')
#else:
if  {}:				#here the inner if and else statement should have indentation
	print('Seven')
	print('Eight')
	print('Nine')
else:
	print('Hyd')
	print('Sec')
	print('Cyb')
print('Bye')



# Write  a  program  to  determine  a  number  is  even  or  odd  with   if  statement

n = int(input("Enter the input value: "))
if n % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

'''
Output:
Enter the input value: 36
The number is even

Enter the input value: 41
The number is odd
'''


# Find outputs  (Home  work)

if():                   #Here the condition is empty, which is always false
        print('Hyd')
        print('Sec')
        print('Cyb')
else:                   # The else block will execute since the if condition is false
        print('One')
        print('Two')
        print('Three')
print('Bye')            # This will always execute since it's outside the if-else structure

# Output:

print('One')
print('Two')
print('Three')
print('Bye')



# Find  outputs  (Home  work)
if{10 : 20 , 30 : 40}:          #Here the condition is True because the dictionary is not empty
        print('Hyd')
        print('Sec')
        print('Cyb')
print('Bye')                    

'''
Output:
Hyd
Sec
Cyb
Bye
'''


# Find outputs  (Home  work)
if { }:                         #Here the condition is False because the dictionary is empty
	print('Hyd')
	print('Sec')
	print('Cyb')
print('Bye')

'''
Output:
Bye
'''


# Write   a  program  to  print  month  name  for  input  month  number  by  using  if  and  elif  (Home  work)

try:
    month = int(input("Enter month number (1-12): "))
    
    if month == 1:
       print("January")
    elif month == 2:
       print("February")
    elif month == 3:
       print("March")
    elif month == 4:
       print("April")
    elif month == 5:
       print("May")
    elif month == 6:
       print("June")
    elif month == 7:
       print("July")
    elif month == 8:
       print("August")
    elif month == 9:
       print("September")
    elif month == 10:
       print("October")
    elif month == 11:
       print("November")
    elif month == 12:
       print("December")
    else:
       print("Input  should  be  between  1  and   12")
except ValueError:
    print("Input  should  be  an  integer")

'''
Output:
Enter month number (1-12): 5
May

Enter month number (1-12): 15
Input  should  be  between  1  and   12

Enter month number (1-12): 12.8
Input  should  be  an  integer
'''


# Write  a  program  to  print  digit  in  words  with  else  and  if  (do  not  use  elif)

digit = int(input("Enter a digit (0 to 9): "))

if digit == 0:
    print("Zero")
else:
    if digit == 1:
        print("One")
    else:
        if digit == 2:
            print("Two")
        else:
            if digit == 3:
                print("Three")
            else:
                if digit == 4:
                    print("Four")
                else:
                    if digit == 5:
                        print("Five")
                    else:
                        if digit == 6:
                            print("Six")
                        else:
                            if digit == 7:
                                print("Seven")
                            else:
                                if digit == 8:
                                    print("Eight")
                                else:
                                    if digit == 9:
                                        print("Nine")
                                    else:
                                        print("Invalid input please enter a single digit (0–9)")
'''
Output:
Enter a number from 0 to 9: 6
Six

Enter a number from 0 to 9: 11
Invalid input please enter a single digit (0–9)
'''