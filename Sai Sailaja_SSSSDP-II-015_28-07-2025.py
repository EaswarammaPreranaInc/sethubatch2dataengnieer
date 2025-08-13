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
a = eval(input("Enter first complex number : "))
b = eval(input("Enter second complex number: "))
print(F'Sum = {a + b}')
print(F'Difference = {a - b}')
print(F'Product = {a * b}')
print(F'Division = {a / b}')








# Identify  error
else:  # else should not be there without if
    print('else  suite')
print('Outside')






# Identify  error
if  9 > 5 # if statement must be end with colon ':' 
	print('Hello')
print('Bye')






# Identify  error
if  9 > 5 # if statement must be end with colon ':' 
	print('Hello')
print('Bye')





# Identify  error
if  (10,20,15):
print('Hyd') # beginning of print statement there should be space or tab space, so indentation error
else:
print('Sec')  # beginning of print statement there should be space or tab space, so indentation error






# Identify  error
if  ():
			print('Hyd')
	else:  # indentation error, else should be indented with if or in same column with if
					print('Sec')
print('Bye')






# Identify  error
if  { }:
{
	print('One')
	print('Two')
	print('Three') # statements or suite cannot be in braces
}
else:
{
	print('Four')
	print('Five')
	print('Six') # statements or suite cannot be in braces
}
print('Bye')







# Identify  error
if  ():
	print('One')
	print('Two')
	print('Three')
else:
if  []:  # if should be followed by a tab space after colon
	print('Four')
	print('Five')
	print('Six')
else:
if  {}: # if should be followed by a tab space after colon
	print('Seven')
	print('Eight')
	print('Nine')
else:
	print('Hyd')
	print('Sec')
	print('Cyb')
print('Bye')







# Write  a  program  to  determine  a  number  is  even  or  odd  with   if  statement

a = int(input("Enter input:"))
if a % 2 == 0:
    print("Even number")
else:
    print("Odd number")
	






# Find outputs  (Home  work)
if():   
        print('Hyd')
        print('Sec')
        print('Cyb') # if condition is False because of empty tuple
else:
        print('One')
        print('Two')
        print('Three') # print else block statements i.e., One<nextline>Two<nextline>Three
print('Bye') # prints Bye







# Find  outputs  (Home  work)
if{10 : 20 , 30 : 40}:
        print('Hyd') # prints Hyd
        print('Sec') # prints Sec
        print('Cyb') # prints Cyb
print('Bye') # prints Bye







# Find outputs  (Home  work)
if { }:
	print('Hyd')
	print('Sec')
	print('Cyb') # if condtion is False so prints nothing
print('Bye') # prints Bye







# Write   a  program  to  print  month  name  for  input  month  number  by  using  if  and  elif  (Home  work)
try:
    a = int(input("Enter month number(1 - 12):"))
    if a == 1:
        print("January")
    elif a == 2:
        print("February")
    elif a == 3:
        print("March")
    elif a == 4:
        print("April")
    elif a == 5:
        print("May")
    elif a == 6:
        print("June")
    elif a == 7:
        print("July")
    elif a == 8:
        print("August")
    elif a == 9:
        print("September")
    elif a == 10:
        print("October")
    elif a == 11:
        print("November")
    elif a == 12:
        print("December")
    else:
        print("Input should be between 1 and 12")
except ValueError:
    print("Input should be an integer")







'''
Write  a  program  to  print  digit  in  words  with  else  and  if  (do  not  use  elif)
0 - Zero
1 - One
2 - Two
....
9 - Nine
10 - Invalid
'''
a = int(input("Enter a digit:"))
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