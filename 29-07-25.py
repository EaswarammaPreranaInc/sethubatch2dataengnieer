#1st
year=int(input("enter the year:"))
if  year % 100!=0 and year % 4==0 or year % 400==0:
    print("it is a leap year")
else:
    print("it is not a leap year")

#2nd
a=int(input("enter first number:"))
b=int(input("enter second number:"))
c=int(input("enter third number:"))
if a>b and a>c:
    print("largest number=",a)
else:
     if b>c:
        print("largest number=",b)
     else:
        print("largest number=",c)

#3rd
m=int(input("enter 1 to convert celsius to farenheit and 2 to convert farenheit to celsius "))
match m:
    case 1:
        d=float(input("enter celsius temperature"))
        f=1.8*d+32
        print("farenheit eqvalent",f)
    case 2:
        d=float(input("enter farenheit temperature"))
        c=(d-32)/1.8
        print("celsius eqvalent:",c)
    case _:
        print("invalid input")


#4th
x = float(input("Enter x-coordinate: "))
y = float(input("Enter y-coordinate: "))
if x > 0 and y > 0:
    print("The point lies in the 1st quadrant.")
elif x < 0 and y > 0:
    print("The point lies in the 2nd quadrant.")
elif x < 0 and y < 0:
    print("The point lies in the 3rd quadrant.")
elif x > 0 and y < 0:
    print("The point lies in the 4th quadrant.")
elif x != 0 and y == 0:
    print("The point lies on the x-axis.")
elif x == 0 and y != 0:
    print("The point lies on the y-axis.")
elif x == 0 and y == 0:
    print("The point is at the origin.")

#5th
a = float(input("Enter first input: "))
b = float(input("Enter second input: "))
c = float(input("Enter third input: "))
max_val = a
min_val = a
if b > max_val:
    max_val = b
if c > max_val:
    max_val = c
if b < min_val:
    min_val = b
if c < min_val:
    min_val = c
mid_val = (a + b + c) - (max_val + min_val)
print("Largest number: ", max_val)
print("Smallest number: ", min_val)
print("Middle number: ", mid_val)

#6th
import math
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))
if (a + b > c) and (a + c > b) and (b + c > a):
    print("The sides form a triangle.")
    if a == b and b == c:
        print("It is an Equilateral Triangle.")
        area = (math.sqrt(3) / 4) * (a ** 2)
        print("Area =", area)
    elif a == b or b == c or a == c:
        print("It is an Isosceles Triangle.")
        perimeter = a + b + c
        print("Perimeter =", perimeter)
    else:
        print("It is a Scalene Triangle.")
        perimeter = a + b + c
        s = perimeter / 2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        print("Perimeter =", perimeter)
        print("Area =", area)

#7th
import math
a = float(input("Enter coefficient a (not zero): "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))
if a != 0:
    disc = b**2 - 4 * a * c
    print("Discriminant =", disc)
    if disc > 0:
        root1 = (-b + math.sqrt(disc)) / (2 * a)
        root2 = (-b - math.sqrt(disc)) / (2 * a)
        print("Roots are Real and Distinct")
        print("Root 1 =", root1)
        print("Root 2 =", root2)
    elif disc == 0:
        root = -b / (2 * a)
        print("Roots are Real and Same")
        print("Root =", root)
    else:
        real_part = -b / (2 * a)
        imag_part = math.sqrt(-disc) / (2 * a)
        root1 = complex(real_part, imag_part)
        root2 = complex(real_part, -imag_part)
        print("Roots are Complex or Imaginary")
        print("Root 1 =", root1)
        print("Root 2 =", root2)

else:
    print("Invalid input. Coefficient 'a' must not be zero.")


#8th
import math
x = float(input("Enter x-coordinate of point: "))
y = float(input("Enter y-coordinate of point: "))
r = float(input("Enter radius of the circle: "))
distance = math.sqrt(x*2 + y*2)
if distance < r:
    print("The point lies inside the circle.")
elif distance > r:
    print("The point lies outside the circle.")
elif distance == r:
    print("The point lies on the circle.")


#9th
m = 4
match  m:
	case  1:
		print('One')
	case  2:
		print('Two')
	case  3:
		print('Three')
print('Bye')#Bye

#10th
# Identify  Error
i = 2
match  i:
	case  1:
		print('One')
	#case  _:
		print('None of   the  above')
	case  2:
		print('Two')
print('Bye')

#11th
# Find  outputs  (Home  work)
m = 2
match  m:
	case  1:
		print('One')
	#case  _:
		print('Hello')
	case  _:
		print('Bye')
print('End')

#12th
m = 1
match  m:
	case  1:
		print('Hyd')#Hyd
	case  1:
		print('Sec')#not executed
	case  1:
		print('Cyb')#not executed
print('Bye')#Bye

#13th
# Find  outputs  (Home  work)
ch = 'B'
match  ch:
	case   'A':
		print('Apple')
	case  'B':
		print('Book')#Book
	case  'C':
		print('Cafe')
	case  _:
		print('None of  the  above')
print('Bye')#Bye

#14th
x = eval(input('Enter any  number :  '))
match  x:
	case  7 |  -6  |  0:
		print('Hyd')
		print('Sec')
		print('Cyb')
	case  -10 | 15:
		print('One')
		print('Two')
		print('Three')
	case  _:
		print('India')
		print('China')
		print('Usa')
# End  of  match
print('Bye')


#15th
tpl = eval(input('Enter  any  point  in  the  form  of  (x , y) :  '))
match  tpl:
	case  (0 , 0):
		print('Origin')
	case   (0 , y):
		print('y - axis')
	case   (x , 0):
		print('x - axis')
	case   (x , y):
		print('Quadrant')
	case  _:
		print('Not  a  point')

#16th
units = int(input("Enter units: "))
cost = 0
match units // 100:
    case 0:
        cost = units * 3.00
    case 1:
        cost = 100 * 3.00 + (units - 100) * 3.50
    case 2 | 3:
        cost = 100 * 3.00 + 100 * 3.50 + (units - 200) * 4.00
    case 4 | 5 | 6:
        cost = 100 * 3.00 + 100 * 3.50 + 200 * 4.00 + (units - 400) * 4.50
    case _:
        cost = 100 * 3.00 + 100 * 3.50 + 200 * 4.00 + 300 * 4.50 + (units - 700) * 5.00

print("Bill amount: Rs.", cost)


#17th
x = int(input("Enter the value of x: "))
a = 0
b = 1
print("Fibonacci series ")
while a <= x:
    print(a)
    c = a + b
    a = b
    b = c

#18th
while True:#infinite loop
      print('Hello')
print('Bye')

#19th
while False:
      print('Hello')
print('Bye')#Bye

#20th
for x in [10,20,15,18]:
      print(x)
print()
for y in 'Hyd':
      print(y)
print()
for z in range(5):
      print(z)

#21th
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . keys():
	print(x)
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . values():
	print(x)
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . items():
	print(x)
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x)
      
#22nd
# Find outputs  (Home  work)
a = {10 : 20 , 30 : 40 , 50 : 60}
for  x , y  in   a . items():
	print(x , y , sep = '...')
for  x ,  y  in   a:
	print(x , y)#error
for  x , y  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x , y , sep = '...')#error
      
#23rd
# Identify  error  (Home  work)
for  x  in   123:#error
        print(x)


#24th
for  x   in   ():
        print(x)
for  x   in  []:
        print(x)
for  x   in   {}:
        print(x)
for  x   in   set():
        print(x)
for  x   in   '':
        print(x)
for  x  in  range(10 , 10):
	print(x)
for  x  in   range():#error
	print(x)
for  x  in   (25):#error
	print(x)

#25th
#  Nested  Loop  demo  program
for  i  in  range(1 , 4):
	for  j  in  range(1 , 5):
			print(i ,  j)  #
	print('Hello')
print('Bye')

#26th
# How  to  print  each  element  and  the  corresponding  index
a = [25 , 10.8 , 'Hyd' , True]
print('Indexed  based  for loop')
for x in range(len(a)):
      print(x,a[x])
for x in a:
      print(x,a.index(x))

#27th
for x in range(1):
      print(a[-i])


#28TH
a = eval(input('Enter 1st list: '))
b = eval(input('Enter 2nd list: '))
c = []
for i in range(min(len(a), len(b))):
    c.append(a[i] + b[i])
print('3rd list:', c)

#29th
for i in range(2,5):
      print(a[i])

#30th
a = [10 , 20 , 15 , 18]
for  i  in  range(len(a)):
	a[i] +=  1
print('a :  ' , a)
b = [10 , 20 , 15 , 18]
for  x  in   b:
	x += 1
print('b :  ' ,  b)

