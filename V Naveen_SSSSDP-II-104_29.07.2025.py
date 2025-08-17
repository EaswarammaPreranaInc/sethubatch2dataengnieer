#1. write a program to test leap year
try:
    a = int(input("Enter year :"))
    if((a % 4 == 0 and a %100 != 0) or a % 400 == 0):
        print("It is a leap year")
    else:
        print("It is not a leap year")
except:
    print("Input should be an integer")



#2. Largest number among three numbers
try:
    a = eval(input("Enter 1st number :"))
    b = eval(input("Enter 2nd number :"))
    c = eval(input("Enter 3rd number :"))
    if(a > b and a > c):
        print("a is greater")
    else:
        if(b > a and b > c):
            print("b is greater")
        else:
            print("c is greater")
except:
    print("Input should be an integer and float")



#3. conversion 
try:
    a = int(input("Enter a number(1 or 2) :"))
    if(a == 1):
        temp = eval(input("Enter celcius temperature :"))
        fah = 1.8 * temp + 32 
        print("Fahrenheit Equivalent :", fah)
    else:
        if(a == 2):
            temp = eval(input("Enter fahrenheit temperature :"))
            cel = (temp - 32) / 1.8 
            print("Celsius Equivalent :", cel)
        else:
            print("Invalid input, input should be 1 or 2")
except:
    print("Input should be an integer or float")



#4. write a program to test quandrant
try:
    a = eval(input("Enter a number :"))
    b = eval(input("Enter a number :"))
    if(a > 0 and b > 0):
        print("point(a, b) lies in 1st quadrant")
    elif(a < 0 and b > 0):
        print("point(a, b) lies in 2st quadrant")
    elif(a < 0 and b < 0):
        print("point(a, b) lies in 3st quadrant")
    elif(a > 0 and b < 0):
        print("point(a, b) lies in 4st quadrant")
    elif(a != 0 and b == 0):
        print("point(a, b) lies x-axis")
    elif(a == 0 and b != 0):
        print("point(a, b) lies in y-axis")
    else:
        print("Invalid input")
except:
    print("Input should be an integer or float")



#5. program to find lagest , middle , smallest number
try:
    a = float(input("Enter 1st number :"))
    b = float(input("Enter 2nd number :"))
    c = float(input("Enter 3rd number :"))
    max = a
    if ( max < b ):
        max = b
    if ( c > max ):
        max = c
    min = a
    if ( min > b ):
        min = b
    if ( min > c ):
        min = c
    mid = (a + b + c) - (max + min)
    print("Largest number :" , max)
    print("Smallest number :" , min)
    print("Middle number :" , mid)
except:
    print("Input should be an integer or float")



#6. program to find original,x and y axis, Quadrant
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
		print('Not  a  point')



#7. using case
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



#8. Find  outputs  (Home  work)
ch = 'B'
match  ch:
	case   'A':
		print('Apple')
	case  'B':
		print('Book') # Book
	case  'C':
		print('Cafe')
	case  _:
		print('None of  the  above')
print('Bye') # Bye



#9.  Find  outputs  (Home  work)
m = 1
match  m:
	case  1:
		print('Hyd') # Hyd
	case  1:
		print('Sec')
	case  1:
		print('Cyb')
print('Bye') # Bye



#10. Find  outputs  (Home  work)
m = 2
match  m:
	case  1:
		print('One')
	case  _:
		print('Hello')
	case  _:
		print('Bye')
print('End')
# Error due to using multiple nameless objects



#11. Identify  Error
i = 2
match  i:
	case  1:
		print('One')
	case  _: # Error because of usinf nameless object in the middle
		print('None of   the  above')
	case  2:
		print('Two')
print('Bye')



#12. Find  outputs  (Home  work)
m = 4
match  m:
	case  1:
		print('One')
	case  2:
		print('Two')
	case  3:
		print('Three')
print('Bye') # bye
# because of there is no case 4 , it executes outer match i.e. Bye



#13. program to find bill amount
units = eval(input("Enter units :"))
match units//100:
    case 0:
        cost = units * 3.00
    case 1:
        cost = (100 * 3.00) +(units - 100) * 3.50
    case 2:
        cost = (100 * 3.00) +(100 * 3.50) + ( units - 200) * 4.00
    case 3:
        cost = (100 * 3.00) +(100 * 3.50) + (200  * 4.00) + (units - 400) * 4.5
    case _:
        cost = (100 * 3.00) +(100 * 3.50) + (200  * 4.00) + (300 * 4.5) + (units - 700) * 5.00
print(cost)


#14. Fibonacci
x = int(input("Enter a number :"))
a = 0
b = 1
print(a)
print(b)
c = a + b
while c <= x:
    print(c)
    a = b
    b = c
    c = a + b




#15. Find  outputs  (Home  work)
a = [10 , 20 , 15 , 18] # How  to  print  each  element  of  list  [10 , 20 , 15 , 18]  with  for  loop
for x in a:
    print(x) # How  to  print  each  character  of   string  'Hyd'  with  for  loop
for i in range(len(a)):
    print(a[i]) # How  to  print  each  element  of   range(5)  with  for  loop



#16.  Find  outputs
while  False:
	print('Hello')
print('Bye') # Bye



#17.  Find  outputs
while  True:
	print('Hello') # prints Hello infinite times
print('Bye') # Bye



#18.  Tricky  program
#  Find  outputs  (Home  work)
a = [10 , 20 , 15 , 18]
for  i  in  range(len(a)):
	a[i] +=  1
print('a :  ' , a) # a :   [11, 21, 16, 19]
b = [10 , 20 , 15 , 18]
for  x  in   b:
	x += 1
print('b :  ' ,  b) # b :   [10, 20, 15, 18]




#19. Find  outputs  (Home  work)
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . keys():
	print(x) # 10<nextline>30<nextline>50<nextline>
print() # nothing
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . values():
	print(x) # 20V=<nextline>40<nextline>60<nextline>
print() # nothing
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . items():
	print(x) # (10, 20)<nextline>(30, 40)<nextline>(50, 60)<nextline>
print() # nothing
for  x  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x) # 10<nextline>30<nextline>50<nextline>



#20. Find outputs  (Home  work)
a = {10 : 20 , 30 : 40 , 50 : 60}
for  x , y  in   a . items():
	print(x , y , sep = '...') # 10...20
                               # 30...40
                               # 50...60
for  x ,  y  in   a: # error because we cannot print items without using functions such as items()
	print(x , y)
for  x , y  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x , y , sep = '...')# error because we cannot print items without using functions such as items()



#21. Identify  error  (Home  work)
for  x  in   123: # non-sequences are not iterable
        print(x)

#22. Find  outputs  (Home  work)
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
#for  x  in   range(): # error due to atleast one arg should be there
	print(x)
#for  x  in   (25): # int object is illiterable



#23.  Nested  Loop  demo  program
for  i  in  range(1 , 4):
	for  j  in  range(1 , 5):
			print(i ,  j)  #
	print('Hello')
print('Bye')
'''
1 1
1 2
1 3
1 4
Hello
2 1
2 2
2 3
2 4
Hello
3 1
3 2
3 3
3 4
Hello
Bye '''




#24. How  to  print  each  element  and  the  corresponding  index
a = [25 , 10.8 , 'Hyd' , True]
for i in range(len(a)):
    print(a[i], i , sep = " is element and index is ") # How  to  print  each  element  and  the  corresponding  index  with  index  based  for  loop
for x in a:
    print(x) # How  to  print  each  element  and  the  corresponding  index  with  for  ...  each  loop (Do  not  use  2nd  variable)




#25.  How  to  print  list  elements  in  reverse  order   without  slice
a = [25 , 10.8 , 'Hyd' , True]
for i in range(len(a) - 1,-1,-1):
    print(a[i]) # How   to  print  each  element  of  list  in  reverse  order  with  indexed  based  for  loop
for x in reversed(a):
    print(x) # How   to  print  each  element  of  list  in  reverse  order  with  for  each  loop  (Do  not  use  2nd  variable  and  slice)



#26.add two lists
a = eval(input("Enter 1st list :"))  # [10, 20, 15, 18]
b = eval(input("Enter 2st list :")) # [30, 40, 35, 12, 100, 200, 300]
c =[]
d = []
for i in range(len(a)):
    c.append(a[i] + b[i])
print('3rd list :' ,c)
for x, y in zip(a, b):
    d.append(x + y)
print('3rd list :' ,d)




#27.  How  to  print  list  elements  from  indexes  2  to  4  without  slice
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Sec']
print('Indexed for loop')
for i in range(2, 5):
    print(a[i]) # How  to  print  elements  from  indexes  2  to  4  of  list  'a'  with  indexed  based  for  loop
c = 0
for x in a:
    if 2 <= c <= 4:
        print(x)
    c = c+1 # How  to  print  elements  from  indexes  2  to  4  of  list  'a'  with  for  each  loop   without  using  2nd  variable  and  slice