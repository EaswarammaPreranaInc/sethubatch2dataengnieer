# Write  a  program  to  determine  largest  of  three  numbers  with  if  and  else

num1 = int(input("enter 1st number"))
num2 = int(input("enter 2nd number"))
num3 = int(input("enter 3rd number"))

if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

print(f"The largest number is: {largest}")

--------------------------------

# Write  a  program  to  test  year  is  leap  year  or  not

x=int(input("enter year :"))

if  (x % 4 ==0 and x % 100 !=0) or (x % 400==0):
	
	print(" It is a leap year")
else :
	print("It is not a leap year")

-----------------------------------

#  Write  a  program  to  test  a  point  (x , y)  lies  in  1st  quadrant , 2nd  quadrant , 3rd  quadrant ,
     4th  quadrant , x - axis , y - axis   or  origin


x=int(input("Enter 1st value :"))
y=int(input("Enter 2nd  value :")


if  x>0 and y>0:
	print("1st quadrant")
elif x<0 and y>0:
	print("2nd qudrant")
elif x<0 and y<0:
	print("3rd quadrant")
elif x>0 and y<0:
	print("4th qudrant")
elif x==0 and y!=0:
	print("Y-axis")
elif x!=0 and y==0:
	print("X-axis")
elif:
	print("Point lies in Origin")

--------------------------------------

#  Find  outputs
while  True:
	print('Hello')
print('Bye') # infinite loop Hello

-----------------------

#  Find  outputs
while  False:
	print('Hello')
print('Bye')    # Bye

--------------------------------------------

# Find  outputs  (Home  work)

for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . keys():
	print(x)
#  10
    30
    50
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . values():
	print(x)
# 20
   40
   60

for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . items():
	print(x)
 # (10,20)
     (30,40)
     (50,60)

for  x  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x)
# 10
   30
   50

----------------------------

# Find  outputs  (Home  work)

How  to  print  each  element  of  list  [10 , 20 , 15 , 18]  with  for  loop
#  list = [10, 20, 15, 18]
for item in list:
    print(item)

How  to  print  each  character  of   string  'Hyd'  with  for  loop
#  s = 'Hyd'
for char in s:
    print(char)

How  to  print  each  element  of   range(5)  with  for  loop
# for i in range(5):
    print(i)

-----------------------------------------

# Find outputs  (Home  work)

a = {10 : 20 , 30 : 40 , 50 : 60}

for  x , y  in   a . items():
	print(x , y , sep = '...') #  10...20
					       30...40
					       50...60
for  x ,  y  in   a:
	print(x , y)  # Error

for  x , y  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x , y , sep = '...') #  Error

----------------------------------------

# Identify  error  (Home  work)
for  x  in   123:
        print(x)  # 123 is an integer which is not iterable

-----------------------------------

# Find  outputs  (Home  work)
for  x   in   ():
        print(x) # empty tuple
for  x   in  []:
        print(x) # empty list
for  x   in   {}:
        print(x) # empty Dict
for  x   in   set():
        print(x) # empty set
for  x   in   '':
        print(x) # empty String
for  x  in  range(10 , 10):
	print(x) # empty
for  x  in   range():
	print(x) # error
for  x  in   (25):
	print(x) # error
------------------------------------------

#  Nested  Loop  demo  program
for  i  in  range(1 , 4):
	for  j  in  range(1 , 5):
			print(i ,  j)  #
	print('Hello')
print('Bye')

output:-
--------
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
Bye
------------------------
# How  to  print  each  element  and  the  corresponding  index

a = [25 , 10.8 , 'Hyd' , True]
print('Indexed  based  for loop')
How  to  print  each  element  and  the  corresponding  index  with  index  based  for  loop
output:-
------------
a = [25, 10.8, 'Hyd', True]
for i in range(len(a)):
    print('Index:', i, 'Element:', a[i])

print('For each loop')
How  to  print  each  element  and  the  corresponding  index  with  for  ...  each  loop (Do  not  use  2nd  variable)
output:-
----------
print('For each loop')
for x in a:
    print('Index:', a.index(x), 'Element:', x)

------------------------------------------------
#  How  to  print  list  elements  in  reverse  order   without  slice

a = [25 , 10.8 , 'Hyd' , True]

1)How   to  print  each  element  of  list  in  reverse  order  with  indexed  based  for  loop 
#  print('Indexed for loop')
for i in range(len(a) - 1, -1, -1):   # from last index to 0
    print(a[i])

2)How   to  print  each  element  of  list  in  reverse  order  with  for  each  loop  (Do  not  use  2nd  variable  and  slice)
      # print('For each loop')
      a.reverse()  # modifies the original list
      for x in a:
   	 print(x)
----------------------------

# Write  a  program  to  add  two  lists  and  store  results  in  3rd  list

a = [10, 20, 30, 40]
b = [1, 2, 3, 4]
c = []

for i in range(len(a)):
    c.append(a[i] + b[i])

print('3rd list:', c)

for each loop:-
------------------
a = [10, 20, 30, 40]
b = [1, 2, 3, 4]
c = []

for x in a:
    c.append(x + b[a.index(x)])

print('3rd list:', c)

----------------------------------
# Tricky program

a = [10, 20, 15, 18]
for i in range(len(a)):
    a[i] += 1
print('a :  ', a)

b = [10, 20, 15, 18]
for x in b:
    x += 1
print('b :  ', b)
   
outputs:-
----------
a :   [11, 21, 16, 19]
b :   [10, 20, 15, 18]
-----------------------------------

# Write  a  program  to  determine  bill  amount  and  input  is  units
Units                                                                      Cost
---------------------------------------------------------------------------------------
First  100  units(0 - 99)					Rs. 3.00 / unit #(say case 1)

Next  100  units(100 - 199)				Rs. 3.50 / unit #(case2)

Next  200  units(200 - 399)		         	Rs. 4.00 / unit # (case3 & 4)

Next  300  units(400 - 699)				Rs. 4.50 / unit #(casec 5 & 6)

Above  700  units(>= 700)				Rs. 5.00 / unit

Code : -
--------
units = int(input("Enter total units consumed: "))
bill = 0

match units:
    case 1 if u < 100:
        bill = u * 3.00
    case 2 if u < 200:
        bill = 100 * 3.00 + (u - 100) * 3.50
    case 3 if u < 400:
        bill = 100 * 3.00 + 100 * 3.50 + (u - 200) * 4.00
    case  if u < 700:
        bill = 100 * 3.00 + 100 * 3.50 + 200 * 4.00 + (u - 400) * 4.50
    case _:
        bill = 100 * 3.00 + 100 * 3.50 + 200 * 4.00 + 300 * 4.50 + (units - 700) * 5.00

print("Total Bill Amount: Rs.", bill)





























































