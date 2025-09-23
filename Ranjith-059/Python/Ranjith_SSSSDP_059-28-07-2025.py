(28-07-2025)

#Write  a  program  to  add ,  subtract , multiply  and  divide  two  complex  numbers

#Program

a = eval(input("Enter 1st complex number: "))
b = eval(input("Enter 2nd complex number: "))
print(F'{a} + {b} = {a+b}')
print(F'{a} - {b} = {a-b}')
print(F'{a} * {b} = {a*b}')
print(F'{a} / {b} = {a/b}')

#Output

Enter 1st complex number: 3+4j
Enter 2nd complex number: 5+6j
(3+4j) + (5+6j) = (8+10j)
(3+4j) - (5+6j) = (-2-2j)
(3+4j) * (5+6j) = (-9+38j)
(3+4j) / (5+6j) = (0.6393442622950819+0.03278688524590165j)


# Identify  error

else:			# we cannot use else without if
	print('else  suite')
print('Outside')


# Identify  error

if  9 > 5 		#Here the ':' is missing as it is mandatory
	print('Hello') 
print('Bye')


# Identify  error

if  9 > 12:
	print('Hyd')
else                   #Here the ':' is missing as for else also it is 				mandatory  
	print('Sec')


# Identify  error

if  (10,20,15):
print('Hyd')          #Indentation Error #We should follow python indentation
else:
print('Sec')


# Identify  error     

if  ():			#Here if and else should be in same indentation
			print('Hyd')
	else:		
					print('Sec')
print('Bye')


# Identify  error  
			
if  { }:  
{		   			#Here {} are not allowed so it give error
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


# Identify  error
if  ():
	print('One')
	print('Two')
	print('Three')
else:
if  []:     # The Error is indentation error here
	print('Four')
	print('Five')
	print('Six')
else:
if  {}:    # The Error is indentation error here
	print('Seven')
	print('Eight')
	print('Nine')
else:
	print('Hyd')
	print('Sec')
	print('Cyb')
print('Bye')


#This is the correct program without any indentation error
if  ():  				#Empty Tuple as it returns false so it goes to else
	print('One')
	print('Two')
	print('Three')
else:
	if  []: 			#Empty List it returns the False where condition becomes false
		print('Four')
		print('Five')
		print('Six')
	else: 
		if  {}: 		#Dict cannot be empty as it returns False where condition becomes false
			print('Seven')
			print('Eight')
			print('Nine')
		else:			#Else block is executed as above condition becomes false
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

#Output
'''
Enter the input value: 56
The number is even
Enter the input value: 45
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
'''
print('One')
print('Two')
print('Three')
print('Bye')
'''

# Find  outputs  (Home  work)
if{10 : 20 , 30 : 40}:          #Here the condition is True because the dictionary is not empty
        print('Hyd')
        print('Sec')
        print('Cyb')
print('Bye')                    #Here this will always execute

#Output 
'''
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
print('Bye')                    #Here this will always execute

#Output
#Bye

try:
    n = int(input("Enter month number (1-12): "))
    
    if n == 1:
        print("January")
    elif n == 2:
        print("February")
    elif n == 3:
        print("March")
    elif n == 4:
        print("April")
    elif n == 5:
        print("May")
    elif n == 6:
        print("June")
    elif n == 7:
        print("July")
    elif n == 8:
        print("August")
    elif n == 9:
        print("September")
    elif n == 10:
        print("October")
    elif n == 11:
        print("November")
    elif n == 12:
        print("December")
    else:
        print("Please choose a number between 1 and 12")
except ValueError:
    print("Please enter a valid integer.")


#Output

Enter month number (1-12): 3
March
Enter month number (1-12): 13
Please choose a number between 1 and 12
Enter month number (1-12): 10.8
Please enter a valid integer.

'''
Write  a  program  to  print  digit  in  words  with  else  and  if  (do  not  use  elif)
0 - Zero
1 - One
2 - Two
....
9 - Nine
10 - Invalid
'''
n = int(input("Enter a number between 0 to 10: "))
if n == 0 or n == 1 or n == 2 or n == 3 or n == 4 or n == 5 or n == 6 or n == 7 or n == 8 or n == 9:
    if n == 0:
        print("Zero")
    if n == 1:
        print("One")
    if n == 2:
        print("Two")
    if n == 3:
        print("Three")
    if n == 4:
        print("Four")
    if n == 5:
        print("Five")
    if n == 6:
        print("six")
    if n == 7:
        print("Seven")
    if n == 8:
        print("Eight")
    if n == 9:
        print("Nine")
else:
    print("Invalid")

# Output:
# Enter a number between 0 to 10: 5
# Five
# Enter a number between 0 to 10: 10
# Invalid
# Enter a number between 0 to 10: 3
# Three
