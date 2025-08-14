#Write  a  program  to  add ,  subtract , multiply  and  divide  two  complex  numbers

a = eval(input("Enter 1st complex number: "))
b = eval(input("Enter 2nd complex number: "))
print(F'{a} + {b} = {a+b}')
print(F'{a} - {b} = {a-b}')
print(F'{a} * {b} = {a*b}')
print(F'{a} / {b} = {a/b}')




# Identify  error

else:			# we cannot use else without if
	print('else  suite')
print('Outside')




# Identify  error

if  9 > 5 		#Here the ':' is missing
	print('Hello') 
print('Bye')




# Identify  error

if  9 > 12:
	print('Hyd')
else                   #Here the ':' is missing
	print('Sec')




# Identify  error

if  (10,20,15):
print('Hyd')          #Indentation Error 
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
if  []:     # Indentation error
	print('Four')
	print('Five')
	print('Six')
else:
if  {}:    # Indentation error
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



 # Find outputs  (Home  work)
if():                  
        print('Hyd')
        print('Sec')
        print('Cyb')
else:                   
        print('One')    #One
        print('Two')	#Two
        print('Three')	#Three
print('Bye')          	#Bye





# Find  outputs  (Home  work)
if{10 : 20 , 30 : 40}:     
        print('Hyd')		#Hyd
        print('Sec')		#sec
        print('Cyb')		#Cyb
print('Bye')                    #Bye




# Find outputs  (Home  work)
if { }:                         #Here the condition is False because the dictionary is empty
	print('Hyd')
	print('Sec')
	print('Cyb')
print('Bye')                    #Bye




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
# Enter a number between 0 to 10: 3
# Three