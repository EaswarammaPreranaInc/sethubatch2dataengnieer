Write  a  program  to  add ,  subtract , multiply  and  divide  two  complex  numbers
 
num1 = complex(input("Enter 1st complex number: "))
num2 = complex(input("Enter 2nd complex number : "))

sum_result = num1 + num2

print("Sum:", sum_result)

Substract:-
--------------
num1 = input("Enter 1st  number : ")
num2 = input("Enter 2nd  number : ")

result = num1 - num2

print("Diff:", result)

Multiply:-
-----------
num1 = input("Enter 1st  number : ")
num2 = input("Enter 2nd number : ")

result = num1 * num2

print("product:", result)

Divide:-
---------
num1 = input("Enter 1st  number : ")
num2 = input("Enter 2nd number : ")

result = num1 / num2

print("Division:", result)

-------------------------------------

# Identify  error
else:
		print('else  suite')
print('Outside')  # error due to no if condition

-------------------------------------

# Identify  error
if  9 > 5
	print('Hello')
print('Bye')   # error missing colon

----------------------------------

# Identify  error
if  9 > 12:
	print('Hyd')
else
	print('Sec')   # error missing colon for else

--------------------------------

# Identify  error
if  (10,20,15):
print('Hyd')
else:
print('Sec') # indentation error

---------------------------------

# Identify  error
if  ():
			print('Hyd')
	else:
					print('Sec')
print('Bye')

# Error due to empty if condition

----------------------------------

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
print('Bye') # syntax error

------------------------

# Identify  error
if  ():
	print('One')
	print('Two')
	print('Three')
else:
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
 
# indentation error at 2nd if
------------------------------

# Write  a  program  to  determine  a  number  is  even  or  odd  with   if  statement

Number=int(input("Enter Number : ")

if   Number/2:
	print("Even")
else:
	print("Odd")
---------------------------------------
# Find outputs  (Home  work)

if():
        print('Hyd')
        print('Sec')
        print('Cyb')
else:
        print('One')
        print('Two')
        print('Three')
print('Bye')	# One
			    Two
			    Three
			    Bye

-----------------------
# Find  outputs  (Home  work)

if{10 : 20 , 30 : 40}:
        print('Hyd')
        print('Sec')
        print('Cyb')
print('Bye')	# Hyd
			   Sec
			   Cyb
			   Bye
-------------------------------

# Write   a  program  to  print  month  name  for  input  month  number  by  using  if  and  elif  (Home  work)

user_input = input("Enter month number (1 - 12): ")

try:
    num = int(user_input)

    if num == 1:
        print("Jan")
    elif num == 2:
        print("Feb")
    elif num == 3:
        print("Mar")
    elif num == 4:
        print("Apr")
    elif num == 5:
        print("May")
    elif num == 6:
        print("June")
    elif num == 7:
        print("July")
    elif num == 8:
        print("Aug")
    elif num == 9:
        print("Sep")
    elif num == 10:
        print("Oct")
    elif num == 11:
        print("Nov")
    elif num == 12:
        print("Dec")
    else:
        print("Enter number between 1 and 12 only.")

except ValueError:
    print("Input should be an integer.")

---------------------------------

Write  a  program  to  print  digit  in  words  with  else  and  if  (do  not  use  elif)

digit = input("Enter a digit (0-9): ")

if digit == "0":
    print("Zero")
else:
    if digit == "1":
        print("One")
    else:
        if digit == "2":
            print("Two")
        else:
            if digit == "3":
                print("Three")
            else:
                if digit == "4":
                    print("Four")
                else:
                    if digit == "5":
                        print("Five")
                    else:
                        if digit == "6":
                            print("Six")
                        else:
                            if digit == "7":
                                print("Seven")
                            else:
                                if digit == "8":
                                    print("Eight")
                                else:
                                    if digit == "9":
                                        print("Nine")
                                    else:
                                        print("Invalid input! Enter a single digit (0–9).")





















































