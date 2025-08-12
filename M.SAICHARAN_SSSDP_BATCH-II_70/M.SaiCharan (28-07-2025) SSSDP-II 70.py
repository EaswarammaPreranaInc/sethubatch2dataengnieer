          Name: M.SaiCharan                        HOMEWORK
          Date: 28-07-2025.                   


1.'''
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
sample output:
Enter first complex number : 3+4j
Enter second complex number: 5+6j
Sum :  (8+10j)
Difference :  (-2-2j)
Product:  (-9+38j)
Division :  (0.6393442622950819+0.03278688524590165j)

program:
a = complex(input("Enter first complex number : "))
b = complex(input("Enter second complex number: "))
print("Sum       :", a + b)
print("Difference:", a - b)
print("Product   :", a * b)
print("Division  :", a / b)





2.# Identify  error
else:
	print('else  suite')				# Error
print('Outside')




3.# Identify  error
if  9 > 5
	print('Hello')					# error 
print('Bye')




4.# Identify  error
if  9 > 12:
	print('Hyd')
else
	print('Sec')					# error




5.# Identify  error
if  (10,20,15):
print('Hyd')
else:
print('Sec')						# Error because of indentation.




6.# Identify  error
if  ():
			print('Hyd')
	else:
					print('Sec')
print('Bye')						# error because of Indentation.





7.# Identify  error
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
print('Bye')						# Error because of braces





8.# Identify  error
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
if  {}:							# Error because of Indentation
	print('Seven')
	print('Eight')
	print('Nine')
else:
	print('Hyd')
	print('Sec')
	print('Cyb')
print('Bye')





9.# Write  a  program  to  determine  a  number  is  even  or  odd  with   if  statement

program:
a= int(input("Enter the Number :"))
if a % 2 ==0:
	print("even number")
else: 
        print("odd number")



10.# Find outputs  (Home  work)
if():
        print('Hyd')
        print('Sec')
        print('Cyb')
else:
        print('One')				# one
        print('Two')				# Two
        print('Three')				# Three
print('Bye')					# Bye





11.# Find  outputs  (Home  work)
if{10 : 20 , 30 : 40}:
        print('Hyd')				# Hyd
        print('Sec')				# sec
        print('Cyb')				# cyb
print('Bye')					# Bye





12.# Find outputs  (Home  work)
if { }:
	print('Hyd')
	print('Sec')
	print('Cyb')
print('Bye')					# Bye





13.# Write   a  program  to  print  month  name  for  input  month  number  by  using  if  and  elif  (Home  work)
sample outputs:
Enter month number (1 - 12): 6
June

Enter month number (1 - 12): 13
Input  should  be  between  1  and   12

Enter month number (1 - 12): 10.8
Input  should  be  an  integer

program:

month_input = input("Enter month number (1 - 12): ")
if month_input.isdigit():
    month = int(month_input)
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
        print("Input should be between 1 and 12")
else:
    print("Input should be an integer")









'''



14.Write  a  program  to  print  digit  in  words  with  else  and  if  (do  not  use  elif)
0 - Zero
1 - One
2 - Two
....
9 - Nine
10 - Invalid
'''
program:

a = int(input("Enter a digit (0 to 9): "))
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