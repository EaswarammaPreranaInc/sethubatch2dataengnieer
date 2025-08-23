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

Enter first complex number : 3+4j
Enter second complex number: 5+6j
Sum :  (8+10j)
Difference :  (-2-2j)
Product:  (-9+38j)
Division :  (0.6393442622950819+0.03278688524590165j)										   

'''
try:
	a = complex(input('Enter a complex number : '))
	b = complex(input('Enter a complex number : '))
	print(f'Sum : {a + b}')
	print(f'Difference : {a - b}')
	print(f'Product : {a * b}')
	print(f'Division : {a / b}')
except ValueError:
	print('Input should be complex number')


  # Identify  error
else: # error without if else cannot be written
		print('else  suite')
print('Outside')

# Identify  error
if  9 > 5 # error as there is no :
	print('Hello')
print('Bye')

# Identify  error
if  9 > 12:
	print('Hyd')
else # error as there is no : 
	print('Sec')
  
# Identify  error
if  (10,20,15):
print('Hyd') # error as there is no indentation
else:
print('Sec')


# Identify  error
if  ():
			print('Hyd')
	else: # error becoz else is not indented with if
					print('Sec')
print('Bye')

 Identify  error
if  { }:
{  # error becoz braces are for set and dict not for suite
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
if  []: # error becoz if is not indented with the above else
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


# Write a program to determine a number is even or odd with if statement
try:
	a = int(input('Enter a Number  : '))
	if a % 2 == 0:
		print(f'{a} is Even Number')
	else:
		print(f'{a} is Odd Number')
except ValueError:
	print('Enter Only Integer Value')


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

'''
One
Two
Three
Bye
'''


# Find  outputs  (Home  work)
if{10 : 20 , 30 : 40}:
        print('Hyd')
        print('Sec')
        print('Cyb')
print('Bye')

'''
Hyd
Sec
Cyb
Bye
'''


# Find outputs  (Home  work)
if { }:
	print('Hyd')
	print('Sec')
	print('Cyb')
print('Bye') # Bye



# Write a program to print month name for input month number by using if and elif (Home work)
'''
Enter month number (1 - 12): 6
June
Enter month number (1 - 12): 13
Input should be between 1 and 12
Enter month number (1 - 12): 10.8
Input should be an integer

'''
try:
	a = int(input('Enter month number (1 - 12): '))
	if a == 1:
		print('January')
	elif a == 2:
		print('February')
	elif a == 3:
		print('March')
	elif a == 4:
		print('April')
	elif a == 5:
		print('May')
	elif a == 6:
		print('June')
	elif a == 7:
		print('July')
	elif a == 8:
		print('August')
	elif a == 9:
		print('September')
	elif a == 10:
		print('October')
	elif a == 11:
		print('November')
	elif a == 12:
		print('December')
	else:
		print('Input should be between 1 and 12')
except ValueError:
	print('Input should be Integer Value')


'''
Write a program to print digit in words with else and if (do not use elif)
0 - Zero
1 - One
2 - Two
....
9 - Nine
10 - Invalid
'''
a = int(input("Enter a digit: "))
if a == 0:
    print("Zero")
else:
    if a == 1:
        print("One")
    else:
        if a == 2:
            print("Two")
        else:
            if a == 3:
                print("Three")
            else:
                if a == 4:
                    print("Four")
                else:
                    if a == 5:
                        print("Five")
                    else:
                        if a == 6:
                            print("Six")
                        else:
                            if a == 7:
                                print("Seven")
                            else:
                                if a == 8:
                                    print("Eight")
                                else:
                                    if a == 9:
                                        print("Nine")
                                    else:
                                        print("Invalid")
