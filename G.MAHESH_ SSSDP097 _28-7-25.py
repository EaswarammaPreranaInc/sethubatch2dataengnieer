# 1) Write  a  program  to  add ,  subtract , multiply  and  divide  two  complex  numbers

a = eval(input("Enter 1st complex number: "))
b = eval(input("Enter 2nd complex number: "))
print(F'{a} + {b} = {a+b}')
print(F'{a} - {b} = {a-b}')
print(F'{a} * {b} = {a*b}')
print(F'{a} / {b} = {a/b}')

'''
# Output:

Enter 1st complex number: 3+4j
Enter 2nd complex number: 5+6j
(3+4j) + (5+6j) = (8+10j)
(3+4j) - (5+6j) = (-2-2j)
(3+4j) * (5+6j) = (-9+38j)
(3+4j) / (5+6j) = (0.6393442622950819+0.03278688524590165j)
'''


# 2) Identify  error

else:			# we cannot use else without if
	print('else  suite')
print('Outside')



# 3) Identify  error

if  9 > 5 		#Here the ':' is missing as it is mandatory
	print('Hello') 
print('Bye')



# 4) Identify  error

if  9 > 12:
	print('Hyd')
else                   # Here the ':' is missing for else as it is mandatory  
	print('Sec')



# 5) Identify  error

if  (10,20,15):
print('Hyd')          # Indentation Error we it should have indentation
else:
print('Sec')



# 6) Identify  error
     
if  ():			# Here if and else should be in same indentation
			print('Hyd')
	else:		
					print('Sec')
print('Bye')



# 7) Identify  error  	
	
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




# 8) Identify  error
if  ():
	print('One')
	print('Two')
	print('Three')
else:
if  []:				#here the inner if and else statement should have indentation  
	print('Four')
	print('Five')
	print('Six')
else:
if  {}:				#here the inner if and else statement should have indentation
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



# 9) Write  a  program  to  determine  a  number  is  even  or  odd  with   if  statement

n = int(input("Enter the input value: "))
if n % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

'''
# Output:

Enter the input value: 36
The number is even

Enter the input value: 41
The number is odd
'''


# 10) Find outputs  (Home  work)

if():                   #Here the condition is empty, which is always false
        print('Hyd')
        print('Sec')
        print('Cyb')
else:                   # The else block will execute since the if condition is false
        print('One')
        print('Two')
        print('Three')
print('Bye')            # This will always execute since it's outside the if-else structure

'''
# Output:

print('One')
print('Two')
print('Three')
print('Bye')

'''


# 11) Find  outputs  (Home  work)
if{10 : 20 , 30 : 40}:          #Here the condition is True because the dictionary is not empty
        print('Hyd')
        print('Sec')
        print('Cyb')
print('Bye')                    

'''
# Output:

Hyd
Sec
Cyb
Bye
'''


# 12) Find outputs  (Home  work)
if { }:                         #Here the condition is False because the dictionary is empty
	print('Hyd')
	print('Sec')
	print('Cyb')
print('Bye')                   

#Output: Bye



# 13) Write   a  program  to  print  month  name  for  input  month  number  by  using  if  and  elif  (Home  work)

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
# Output:

Enter month number (1-12): 5
May

Enter month number (1-12): 15
Input  should  be  between  1  and   12

Enter month number (1-12): 12.8
Input  should  be  an  integer
'''


# 14) Write  a  program  to  print  digit  in  words  with  else  and  if  (do  not  use  elif)

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
# Output:

Enter a number from 0 to 9: 6
Six

Enter a number from 0 to 9: 11
Invalid input please enter a single digit (0–9)
'''

			#(OR)

n = int(input("Enter a number from 0 to 9: "))
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


'''
# Output:

Enter a number from 0 to 9: 6
Six

Enter a number from 0 to 9: 11
Invalid 

'''



'''
15) Write  a  program  to  determine  three  sides  form  a  triangle  or  not

1) Find  area  if  it  is  an  equilateral  triangle
    What  is  an  equilateral  triangle ?  ---> All  the  three  sides  should  be  same
    What  is  the  area  of  equilateral  triangle ?  --->  sqrt(3) / 4 * a ^ 2

2) Find  perimeter  if  it  is  an  isosceles  triangle
    What  is  an  isoscles  triangle ?  ---> Any  two  sides  are  same
    What   is  the  perimeter  of  isoscles  triangle ?  ---> a + b + c

3) Find  both  if  it  is  scalene  triangle
    What  is  a  scalene  triangle ?  ---> All  the  three  sides  are  different
    What  is  the  area  of  scalene  triangle ?  ---> sqrt(s * (s - a) * (s - b) * (s - c))
	What  is  the  value  of  's'  ? 
'''

import math

a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))

if a + b > c and a + c > b and b + c > a:
    print("The sides form a triangle.")

    if a == b == c:
        print("It is an Equilateral Triangle.")
        area = (math.sqrt(3) / 4) * a ** 2
        print(f"Area of equilateral triangle = {area:.2f}")

    elif a == b or b == c or a == c:
        print("It is an Isosceles Triangle.")
        perimeter = a + b + c
        print(f"Perimeter of isosceles triangle = {perimeter:.2f}")

    else:
        print("It is a Scalene Triangle.")
        s = (a + b + c) / 2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        perimeter = a + b + c
        print(f"Area = {area:.2f}")
        print(f"Perimeter = {perimeter:.2f}")
else:
    print("The given sides do NOT form a triangle.")





'''
16) Write  a  program  to  determine  roots  of  a  quadtratic  equation  a * x ^ 2 + b * x + c = 0  where  a  ! = 0

1) What  is  the  value  of  discriminant ?  --->  b ^ 2 - 4ac

2) What  are  the  roots  called  if  disc > 0 ?  --->  Real  and  distinct
     What  is  the  formula  for  root1  ?  ---> (-b + sqrt(disc)) / 2a
     What  is  the  formula  for  root2 ?  ---> (-b - sqrt(disc)) / 2a

3) What  are  the  roots  called  if  disc  is  0 ?  --->  Real  and  same
     What  is  the  formula  for  root  ?  --->  -b / 2a

4) What  are  the  roots  called  if  disc < 0 ?  --->  Complex  (or)  Imaginary  roots
     What  is  the  formula  for  real  part ?  --->  -b / 2a
	 What  is  the  formula  for  imag  part ?  --->  sqrt(-disc) / 2a
	 What  is  roo…
'''

import math

a = float(input("Enter coefficient a (≠0): "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

disc = b**2 - 4*a*c

print(f"Discriminant = {disc}")

if disc > 0:
    print("Roots are real and distinct.")
    root1 = (-b + math.sqrt(disc)) / (2*a)
    root2 = (-b - math.sqrt(disc)) / (2*a)
    print(f"Root 1 = {root1:.2f}")
    print(f"Root 2 = {root2:.2f}")

elif disc == 0:
    print("Roots are real and equal.")
    root = -b / (2*a)
    print(f"Root = {root:.2f}")

else:
    print("Roots are complex.")
    real = -b / (2*a)
    imag = math.sqrt(-disc) / (2*a)
    print(f"Root 1 = {real:.2f} + {imag:.2f}i")
    print(f"Root 2 = {real:.2f} - {imag:.2f}i")



'''
17) Write  a  program   to  determine  a  point (x , y)  lies  inside , outside  or  on  the  circle.
Center  is  origin  and  radius  is  'r'

1) What  is  the  distance  between  origin  and  point (x , y) ?  --->  sqrt(x ^ 2 + y ^ 2)

2) Where  is  the  point  if  distance >  raidus ?  --->  Outside  the  circle

3) Where  is  the  point  if  distance < raidus ?  --->  Inside  the  circle

4) Where  is  the  point  if  distance  and  raidus   are  same ?  ---> On  the  circle
'''

import math

# Input coordinates and radius
x = float(input("Enter x-coordinate: "))
y = float(input("Enter y-coordinate: "))
r = float(input("Enter radius of the circle: "))

# Calculate distance from origin
distance = math.sqrt(x**2 + y**2)

print(f"Distance from origin = {distance:.2f}")

if distance < r:
    print("The point lies INSIDE the circle.")
elif distance == r:
    print("The point lies ON the circle.")
else:
    print("The point lies OUTSIDE the circle.")


