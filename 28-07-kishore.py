"""Write  a  program  to  add ,  subtract , multiply  and  divide  two  complex  numbers

First  complex  number   --->  3 + 4j
2nd   complex  number   --->  5 + 6j
What  is  the  sum ? ---> (3 + 4j) + (5 + 6j) = 8 + 10j
What  is  the  difference ?  ---> (3 + 4j) - (5 + 6j) =  -2 - 2j
What  is  the  product ?  ---> (3 + 4j) * (5 + 6j) =  15 + 18j + 20j - 24 =  -9 + 38j


What  is  the  division ?  ---> (3 + 4j) / (5 + 6j) = (3 + 4j) * (5 - 6j) / (5 + 6j) * (5 -6j)
                                                                       =   (15 - 18j + 20j + 24) / (25 + 36)
																		 = 39 / 61 + 2j / 61	"""
x = complex(input("Enter 1st complex number : "))
y = complex(input("Enter 2nd conplex number : "))
print("sum:",x+y)  # sum: (8+10j)
print("difference:",x-y)  # difference: (-2-2j)
print("product:",x*y)  # product: (-9+38j)
print("division:",x/y)   # division: (39/61+2j/61)




# Identify  error
#else:
#		print('else  suite')
#print('Outside')

 # There is no if condition


# Identify  error
#if  9 > 5
#	print('Hello')
#print('Bye')
# Error due to : is missing in if condition




# Identify  error
if  9 > 12:
	print('Hyd')
#else
#	print('Sec')
# Error due to : is missing in else block




# Identify  error
#if  (10,20,15):
#print('Hyd')
#else:
#print('Sec')
# there is no correct  indentation format




# Identify  error
if  ():
			print('Hyd')
#	else:
#					print('Sec')
print('Bye')

# there is no correct  indentation format of else





# Identify  error
"""if  { }:
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
print('Bye')"""

# {} are not use in the if and else statements.



# Identify  error
if  ():
	print('One')
	print('Two')
	print('Three')
else:
#if  []:
	print('Four')
	print('Five')
	print('Six')
#else:
#if  {}:
	print('Seven')
	print('Eight')
	print('Nine')
#else:
	print('Hyd')
	print('Sec')
	print('Cyb')
print('Bye')

# # there is no correct  indentation format




# Write  a  program  to  determine  a  number  is  even  or  odd  with   if  statement
a = int(input("enter a number : "))
if a %2 == 0 :
    print('Even number')
else:
	print('Odd number')
"""o/p:
23
Odd number
"""


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
"""o/p:
One
Two
Three
Bye"""

# Find  outputs  (Home  work)
if{10 : 20 , 30 : 40}:
        print('Hyd')
        print('Sec')
        print('Cyb')
print('Bye')
"""o/p:
Hyd
Sec
Cyb
Bye"""




# Find outputs  (Home  work)
if { }:
	print('Hyd')
	print('Sec')
	print('Cyb')
print('Bye')
#o/p:
#Bye




# Write   a  program  to  print  month  name  for  input  month  number  by  using  if  and  elif  (Home  work)
x=input("enter month number(1-12): ")
if x.isdigit():
    month = int(x)
    if month == 1:
        print("Jan")
    elif month == 2:
        print("Feb")
    elif month ==3:
        print("Mar")
    elif month ==4:
        print("Apr")
    elif month ==5:
        print("May")
    elif month == 6:
        print("Jun")
    elif month == 7:
        print("july")
    elif month ==8:
        print("aug")
    elif month == 9:
        print("Sep")
    elif month == 10:
        print("Oct")
    elif month ==11:
        print("Nov")
    elif month ==12:
        print("Dec")
    else:
        print("Input should be between 1 and 12")
else:
    print("input should be an integer")
"""o/p:
enter month number(1-12): 13
Input should be between 1 and 12"""



"""Write  a  program  to  print  digit  in  words  with  else  and  if  (do  not  use  elif)
0 - Zero
1 - One
2 - Two
....
9 - Nine
10 – Invalid"""

a = input("Enter a digit (0 - 9): ")
if a.isdigit():
    digit = int(a)
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
                                            print("Invalid")
else:
    print("Invalid")
"""o/p:
Enter a digit (0 - 9): 10
Invalid
"""
