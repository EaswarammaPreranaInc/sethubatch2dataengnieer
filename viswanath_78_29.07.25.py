# Write  a  program  to  test  year  is  leap  year  or  not
try:
    a = int(input('Enter the input : ')) 
    if a%4==0 and a%100!=0 or a%400 == 0:
        print('Its a leap year')
    else :
        print('Not a leap year')
except: 
    print('enter only years')

# Write  a  program  to  determine  largest  of  three  numbers  with  if  and  else
try:
    a = float(input('Enter the first input : ')) 
    b = float(input('Enter the second input : ')) 
    c = float(input('Enter the third input : ')) 
    print(a if a>b and a>c else b if b>c else c)
except: 
    print('enter only int or float values')

# Write  a  program  to  convert  celsius  temperature  to  farenheit  and  vice-versa
try:
    a = int(input('Enter the number 1 or 2 : ')) 
    if(a==1):
      print('Enter the value to convert into Farenheit ')
      c = float(input('Enter temperature in Celsius: '))
      f = (c * 9/5) + 32
      print('Temperature in Fahrenheit:', f)
    elif(a==2):
        print('Enter the value to convert into Celsius ')
        f = float(input('Enter temperature in Fahrenheit: '))
        c = (f - 32) * 5/9
        print('Temperature in Celsius:', c)
    else:
        print('Invalid input. Input must be 1 or 2 ')
except: 
    print('enter only int values')

# Write  a  program  to  test  a  point  (x , y)  lies  in  1st  quadrant , 2nd  quadrant , 3rd  quadrant ,
4th  quadrant , x - axis , y - axis   or  origin
try:
    x = float(input('Enter the value of x coordinate : ')) 
    y = float(input('Enter the value of y coordinate : ')) 
    if(x>0 and y>0):
        print('x,y lie in first quadrant')
    elif(x>0 and y<0):
        print('x,y lie in fourth quadrant')
    elif(x<0 and y>0):
        print('x,y lie in second quadrant') 
    elif(x<0 and y<0):
        print('x,y lie in third quadrant') 
    elif(x==0 and y!=0):
        print('x,y lie on y axis') 
    elif(x!=0 and y==0):
        print('x,y lie on x axis') 
    elif(x==0 and y==0):
        print('x,y lie on origin')
    else:
        print('Invalid Input.')
except: 
    print('enter only int or float values')

# Write  a  program  to  determine  largest , smallest  and  middle  of  three  numbers
try:
    a = float(input('Enter the first input : ')) 
    b = float(input('Enter the second input : ')) 
    c = float(input('Enter the third input : ')) 
    max = a
    if b > max:
        max = b
    if c > max:
        max = c
        min = a
    if b < min:
        min = b
    if c < min:
        min = c
    mid = ((a+b+c)-(max+min))
    print('Maximum value is:', max)
    print('Middle value is:', mid)
    print('Minimum value is:', min)
except:
    print('Invalid input. Enter int or float values')

#Write  a  program  to  determine  three  sides  form  a  triangle  or  not
import math
a = float(input('Enter the first input : ')) 
b = float(input('Enter the second input : ')) 
c = float(input('Enter the third input : ')) 
s = ('Given sides form triangle')
t = ('Given sides do not form triangle')
try:
    print(s if (a+b>c) and (b+c>a) and (c+a>b) else t)
    if(a==b and b==c):
           print('it is a equilateral triangle')
           x = math.sqrt(3)/4*a**2 or b**2 or c**2
           print(f'area of equilateral triangle = {x:.2f}')
    else:
            if(a==b and b!=c):        
               print('it is a isoscles triangle')
               y = (a+b+c)
               print('perimeter of isoscles triangle= ',y)
            else:
                if(a!=b and b!=c):        
                   print('it is a scalene triangle')
                   s = (a+b+c)/2
                   z = math.sqrt(s*(s-a)*(s-b)*(s-c))
                   p = a+b+c
                   print(f'area of scalene triangle = {z:.2f}')
                   print('perimeter of isoscles triangle = ',p)
                else:
                    print('Invalid input')
except:
 print('input invalid. sum of 2 sides should be greater than 3 side')

# Write  a  program  to  determine  roots  of  a  quadtratic  equation  a * x ^ 2 + b * x + c = 0  where  a  ! = 0
import math
try:
    a = float(input("Enter the value of a (a ≠ 0): "))
    b = float(input("Enter the value of b: "))
    c = float(input("Enter the value of c: "))
    if a == 0:
        print("Invalid input. 'a' should not be zero.")
    else:
        d = b**2 - 4*a*c
        print("Discriminant value is:", d)
        if d > 0:
            print("Roots are real and distinct")
            r1 = (-b + math.sqrt(d)) / (2*a)
            r2 = (-b - math.sqrt(d)) / (2*a)
            print("Root 1 =", r1)
            print("Root 2 =", r2)
        elif d == 0:
            print("Roots are real and same")
            r = -b / (2*a)
            print("Root =", r)
        else:
            print("Roots are imaginary or complex")
            real = -b / (2*a)
            imag = math.sqrt(-d) / (2*a)
            print("Root 1 =", real, "+", imag, "j")
            print("Root 2 =", real, "-", imag, "j")
except:
    print("Invalid input. Please enter only numbers.")
   
# Write  a  program   to  determine  a  point (x , y)  lies  inside , outside  or  on  the  circle.
Center  is  origin  and  radius  is  'r'
import math
try:
    x = float(input("Enter x-coordinate of the point: "))
    y = float(input("Enter y-coordinate of the point: "))
    r = float(input("Enter radius of the circle: "))
    distance = math.sqrt(x**2 + y**2)
    print("Distance from origin =", distance)
    if distance > r:
        print("The point lies outside the circle.")
    elif distance < r:
        print("The point lies inside the circle.")
    else:
        print("The point lies on the circle.")
except:
    print("Invalid input. Please enter numeric values.")

m = 4
match  m:
	case  1:
		print('One')
	case  2:
		print('Two')
	case  3:
		print('Three')
print('Bye')
# Output: # Bye(case 4 does not match)

i = 2
match  i:
	case  1:
		print('One')
	case  _:
		print('None of   the  above')
	case  2:
		print('Two')
print('Bye')
# Error: wildcard case '_' must be last, no cases allowed after it

m = 2
match  m:
	case  1:
		print('One')
	case  _:
		print('Hello')
	case  _:
		print('Bye')
print('End')
# Error: duplicate wildcard case '_', only one allowed

m = 1
match m:
	case 1:
		print('Hyd')
	case 1:
		print('Sec')
	case 1:
		print('Cyb')
print('Bye')
outputs: # Hyd
#Bye

ch = 'B'
match ch:
	case 'A':
		print('Apple')
	case 'B':
		print('Book')
	case 'C':
		print('Cafe')
	case _:
		print('None of  the  above')
print('Bye')

ouputs:# Book
#Bye


# 1) What are the outputs if input is -6 ?
# Input: -6
# x matches case 7 | -6 | 0 → matched
# Output:
# Hyd
# Sec
# Cyb
# Bye
# 2) What are the outputs if input is 15 ?
# Input: 15
# x matches case -10 | 15 → matched
# Output:
# One
# Two
# Three
# Bye
# 3) What are the outputs if input is 10.8 ?
# Input: 10.8
# x does not match any explicit case → default case _
# Output:
# India
# China
# Usa
# Bye
# 4) What are the outputs if input is 0 ?
# Input: 0
# x matches case 7 | -6 | 0 → matched
# Output:
# Hyd
# Sec
# Cyb
# Bye
# 5) What are the outputs if input is -10 ?
# Input: -10
# x matches case -10 | 15 → matched
# Output:
# One
# Two
# Three
# Bye

# 6) What are the outputs if input is 7 ?
# Input: 7
# x matches case 7 | -6 | 0 → matched
# Output:
# Hyd
# Sec
# Cyb
# Bye

# 1) Input: (-10, -20)
# Matches case (x, y) → prints 'Quadrant'
# Output:
# Quadrant
# 2) Input: (10, 0)
# Matches case (x, 0) → prints 'x - axis'
# Output:
# x - axis
# 3) Input: (0, -20)
# Matches case (0, y) → prints 'y - axis'
# Output:
# y - axis
# 4) Input: (0, 0)
# Matches case (0, 0) → prints 'Origin'
# Output:
# Origin
# 5) Input: (10, 20, 30)
# Tuple with 3 elements → no case matches → default _
# Output:
# Not  a  point
# 6) Input: [10, 20]
# List type, not tuple → no match → default _
# Output:
# Not  a  point
# 7) Input: [0, -25]
# List type, not tuple → no match → default _
# Output:
# Not  a  point
# 8) Input: ()
# Empty tuple → no match → default _
# Output:
# Not  a  point
# 9) Input: {10, 20}
# Set type, not tuple → no match → default _
# Output:
# Not  a  point
# 10) Input: (25,)
# Tuple with one element → no match → default _
# Output:
# Not  a  point
# 11) Input: {10: 20}
# Dictionary type → no match → default _
# Output:
# Not  a  point

# Write  a  program  to  determine  bill  amount  and  input  is  units
try:
	units = int(input('Enter units: '))
	if units < 0:
		print('Invalid input: Units cannot be negative')
	else:
		amt = 0
		match units // 100:
			case 0:
				amt = units * 3.00
			case 1:
				amt = 100 * 3.00 + (units - 100) * 3.50
			case 2 | 3:
				amt = 100 * 3.00 + 100 * 3.50 + (units - 200) * 4.00
			case 4 | 5 | 6:
				amt = 100 * 3.00 + 100 * 3.50 + 200 * 4.00 + (units - 400) * 4.50
			case _:
				amt = 100 * 3.00 + 100 * 3.50 + 200 * 4.00 + 300 * 4.50 + (units - 700) * 5.00
		print('Bill Amount =', amt)
except:
	print('Invalid input: Please enter an integer value only')

# Write  a  program  to  print  fibonacci  series  upto  x using while loop
try:
    x = int(input('Enter the limit: '))  # 10
    a, b = 0, 1
    while a <= x:
        print(a, end=' , ')
        a, b = b, a + b
except ValueError:
    print('Please enter a valid integer')

while True:
    print('Hello')
print('Bye')
# Output:
# Hello
# Hello
# ... (infinite loop, 'Bye' is never printed)

while False:
    print('Hello')
print('Bye')
# Output:
# Bye, The condition `while False` is never true. Only `print('Bye')` is executed.

# Printing each element of list [10, 20, 15, 18]
for i in [10, 20, 15, 18]:    print(i)
# Printing each character of string 'Hyd'
for ch in 'Hyd':    print(ch)
# Printing each element of range(5)
for n in range(5):    print(n)

for x in {10: 20, 30: 40, 50: 60}.keys():
	print(x)
# 10
# 30
# 50
print()
for x in {10: 20, 30: 40, 50: 60}.values():
	print(x)
# 20
# 40
# 60
print()
for x in {10: 20, 30: 40, 50: 60}.items():
	print(x)
# (10, 20)
# (30, 40)
# (50, 60)
print()
for x in {10: 20, 30: 40, 50: 60}:
	print(x)
# 10
# 30
# 50
a = {10: 20, 30: 40, 50: 60}
for x, y in a.items():
	print(x, y, sep='...')
# 10...20
# 30...40
# 50...60
for x, y in a:
  print(x, y)# Error: cannot unpack a dictionary directly; use .items() to get key-value pairs
for x, y in {10: 20, 30: 40, 50: 60}:
  print(x, y, sep='...')# Error: same reason as above – must use .items() for unpacking key-value pairs

for x in 123:
     print(x)# Error: int object is not iterable

for x in ():  
        print(x)# No output (empty tuple)
for x in []:  
        print(x)# No output (empty list)
for x in {}:  
        print(x)# No output (empty dict)
for x in set():  
        print(x)# No output (empty set)
for x in '':  
        print(x)# No output (empty string)
for x in range(10, 10):  
	print(x)# No output (range is empty)
for x in range():  
	print(x) # Error: range expected at least 1 argument
for x in (25):  
	print(x)# Error: int object is not iterable

for i in range(1, 4):
	for j in range(1, 5):
		print(i, j)  # (i,j) pairs: (1,1) to (1,4), then (2,1) to (2,4), then (3,1) to (3,4)
	print('Hello')  # Printed after inner loop of each i
print('Bye')  # Printed once after outer loop
# Output:
# 1 1
# 1 2
# 1 3
# 1 4
# Hello
# 2 1
# 2 2
# 2 3
# 2 4
# Hello
# 3 1
# 3 2
# 3 3
# 3 4
# Hello
# Bye

a = [25, 10.8, 'Hyd', True]
print('Indexed based for loop')
for i in range(len(a)):
	print(i, a[i])  # prints index and corresponding element
print('For each loop')
for x in a:
	print(a.index(x), x)  # prints index using index() method
# Note: a.index(x) gives first occurrence index. If list has duplicates, this gives wrong index for repeated elements

a = [25, 10.8, 'Hyd', True]
print('Indexed for loop')
for i in range(len(a)-1, -1, -1):
	print(i, a[i])  # prints index and element in reverse order
print('For each loop')
for x in reversed(a):
	print(x)  # prints element only using reversed() without slice.

# Write  a  program  to  add  two  lists  and  store  results  in  3rd  list
try:
	a = eval(input('Enter 1st list : '))       # [10, 20, 15, 18]
	b = eval(input('Enter 2nd list : '))       # [30, 40, 35, 12, 100, 200, 300]
	c = []
	# Indexed based for loop
	for i in range(min(len(a), len(b))):
		c.append(a[i] + b[i])
	print('3rd list (index-based):', c)  # [40, 60, 50, 30]
	# For each loop (without second variable)
	c = []
	for x in zip(a, b):
		c.append(sum(x))
	print('3rd list (for-each):', c)  # [40, 60, 50, 30]
except Exception as e:
	print('Error:', e)  # Error: <error message in simple terms>
a = [25, 10.8, 'Hyd', True, 3 + 4j, None, 'Sec']
print('Indexed for loop')
for i in range(2, 5):
	print(a[i])
# Hyd# True# (3+4j)
print('For each loop')
for i, x in enumerate(a):
	if i >= 2 and i <= 4:
		print(x)
# Hyd# True# (3+4j)
print('For each loop without second variable')
i = 0
for x in a:
	if i >= 2 and i <= 4:
		print(x)
	i += 1
# Hyd# True# (3+4j)

a = [10, 20, 15, 18]
for i in range(len(a)):
	a[i] += 1
print('a :  ', a)  # a :  [11, 21, 16, 19]

b = [10, 20, 15, 18]
for x in b:
	x += 1
print('b :  ', b)  # b :  [10, 20, 15, 18]
