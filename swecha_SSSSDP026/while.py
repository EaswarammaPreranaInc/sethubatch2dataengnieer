
for  i   in   range(1 , 8):
	print(i)
	if   i % 3 == 0:
		pass
		print('Hyd')
	else:
		print('Sec')
	print('Hello')
print('Outside loop')

numbers = [10, 20 , 15, 12, 18]
x = int(input("enter the element to search:"))
found = False
for i in range(len(numbers)):
    if numbers[i] == x:
        print(f"found at index {i}")
        found = True
        break
    if not found:
        print("not found")       


num = [10 , 20 ,15 , 12 , 18 , 15 , 19 , 14 , 15 , 14]
search = int(input('enter number to search'))
count = num.count(search)
indexes = [i for i, x in enumerate(num) if x == search]
if count > 0:
   print(f"{search} found {count} times")
   print("at positions {indexes}:",indexes)
else:
   print(f"{search} not found ") 

num = [10 , 20 , 15 ,12 , 18 , 19 , 20]
search = int(input('enter number to search'))
count = num . count(search)
indexes = [i for i, x in enumerate(num) if x == search]
if count > 0:
    print(f"{search} found{count} times")
    print("at positions{indexes}:",indexes)
else:
    print(f"{search} not found")   
num = [10 , 20 , 15 ,12 , 18]
search = int(input('enter number to search'))
found = False
for i in range(len(num)):
 if num[i] == search:
   print(f"found at indexes{i}")
   found = True
   break
 if not found:
   print("not found") 

total = 0
count = 0
try:
    while True:
        num = int(input("enter value (cntrl + z to stop): "))
        total += float(num)
        count += 1
except EOFError:
    if count > 0:
        print(f"/naverage is [total/count]")
    else:
        print("no input is given")
        items = [1, 2, 3, 4, 5, 6] 
frequency = {} 
for item in items:
    if item in frequency:
        frequency[item] += 1
    else:
        frequency[item] = 1
for key in frequency:
    print(f"{key} appears {frequency[key]} times")


colour = ['yellow', 'orange', 'white', 'pink'] 
search = input('enter colour to search') 
count = 0
for i in range(len(colour)):
    if colour[i] == search:
        print(f"{search} found at indexes{i}") 
        count += 1
        if count > 0:
            print(f"{search} found {count} times")
        else:
            print("not found")  


num = [1, 2, 3, 4, 5, 6, 7,8] 
count = 0
for i in range(len(num)):
    if num[i] % 2 == 0:
        print(f"{num} is even and found at indexes{i}")
        count += 1
print(f"Total even numbers: {count}") 



num = [10, 11, 12, 13, 20, 15]
threeshold = 14
count = 0
for i in range(len(num)):
    if num[i] > threeshold == 0:
        print(f"{num[i]} is greater than {threeshold} at index {i}")  


try:
    sum = ctr = 0

    while True:
        if (x := eval(input('Enter input (ctrl + z to stop): '))):
            sum += x
            ctr += 1
except EOFError:
    try:
        print(f'Average : {sum / ctr}')
    except ZeroDivisionError:
        print('Enter at least one input')
except (NameError, TypeError):
    print('Input can not be string')

try:
	sum =  ctr = 0
	while  True:
		x = eval(input('Enter input  (ctrl + z  to  stop)  :  '))
		sum += x
		ctr +=1
except  EOFError:
	try:
		print(F'Average :   {sum / ctr}')
	except  ZeroDivisionError:
		print('Enter  at  least  one  input')
except  (NameError , TypeError):
	print('Input  can  not  be  string')
     

n = int(input('enter how many lines?:'))
s = n-1
for i in range(1, n+1):
    print(' '*s,end='')
    s -= 1
    print('*'* (2 * i - 1))

x = [1,2,3,4]
y = [1,2,4,3]
print(x==y)
a = (1,2,3,4)
b = (1,2,4,3)
print(a==b)
p = {1,2,3,4}
q = {1,2,4,3}
print (p==q)
m = range(5)
n = range(4)
print(m==n)

a = 10
b = 20
c = 7
max =  20
min =  7
mid =  (10 + 20 + 7) - (20 + 7) = 10

a = [25 , 10.8 , 'Hyd' , True]
b = []
for i in range(len(a) -1, -1, -1):
  b.append (a[i])
print('reverse order:', b)
a = [25 , 10.8 , 'Hyd' , True]
b = []
for x in a[i]:
    b.append

a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Sec']
b = []
print('indexed for loop')
for i in range(2 , 5):
    print(a[i])

a = eval(input('enter 1st list:',))
b = eval(input('enter 2nd list:',))
c = []
for x , y in range([a] + [b]):
    c.append(a + b)
    print('c')

lines = int(input('how many lines'))
for i in range(lines):
    print(' ' * (n - i - 1, end =''))
lines = int(input('how many lines?:'))
for i in range(lines):
    print(' ' * (1 , n ), end= '')
    for j in range( 1 , i + 1):
     print('j',end = '')
     for j in range( i - 1 , -1 , -1):
        print('j', end = '')

import math
print(math . degrees(math . pi/2))
print(math . radians(90))
print(math . degrees(math . pi))
print(math . radians(180))
print(math . pi)
import math
print(math . fabs(0))
print(math . fabs(3+4j))
print(math . fabs(True))
import math
print(math . degrees(math . pi/-2))
print(math . radians(-180))

a = 25
b = 10.9274
c = 'Hyd'
print('%d    %f    %s'  %(a , b , c))
print('%i    %g    %s'    %(a , b , c))
print('%s    %s    %s'  %(a , b , c))
print('%d    %g    %s'  ,a , b , c)
# print('%d    %g      %s'   a , b , c)
print('%d    %g    %s'  ,  %(a , b , c))
print('%d    %g    %s'    %a%b%c)
print('%d'    %a  ,  '%f'     %b  ,  '%s'   %c)
a = 25
b = 35
c = 'word'
print('%i, %f, %s', (a, b, c))
print('%d, %s, %g', (a, c, b))

print(eval('25'))
print(eval('10.8'))
print(eval('False'))
print(eval('3+4j'))
print(eval('Hyd'))
print(eval("    'Hyd'   "))
print(eval('3 + 4 * 5'))
print(eval('[10 , 20 , 15 , 18]'))
print(eval('{10,20,15,18,20,12,18}'))
print(eval('(10 , 20 , 30)'))
print(eval("{10 : 'Hyd' , 10 : 'Sec'}"))
print(eval(4 + 5))

print(eval("    'hyd'   "))
hyd = 'Sec'
print(eval('hyd'))
sec = '25'
print(eval('sec'))
print(eval(sec))
cyb = 10.8
print(eval('cyb'))
print(eval(cyb))

print(eval('print("Hyd")'))
a = input('Enter  any  string  :  ') # 'Hyd'
print(len(a)) #3
print(a) # Hyd
b = eval(input('Enter   any  string  : '))# '25'
print(len(b)) #2
print(b) # 25
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c , sep = ',')   #   25 , 10.8 , Hyd 
print(a , b , c , sep = '\t') #25 10.8 Hyd
print(a , b , c , sep = '---')
print(a , b , c , sep = '\n')
print(a , b , c) 
print(a , b , c , separator = ':') 





a =  'A'
print(a[1])


a = range(10 , 50 , 5)

print(type(a)) # <class 'range'>

print(a) # range(10, 50, 5)

print(*a)

print(id(a)) # address of object a

print(len(a)) # 8

print(*a[2 : 7] , sep = ' , ') # 20 , 25 , 30 , 35 , 40 , 45

print(*a[ : : -1]) # 45 , 40 , 35 , 30 , 25 , 20 , 15 , 10

# a[4] = 32 

print(a * 2)

a = range(10 , 20)
print(*a , sep = ',') # 10,11,12,13,14,15,16,17,18,19
b = range(5) # 0,1,2,3,4
print(*b) # 0 1 2 3 4
c = range(10 , 1 , -1)
print(*c , sep = '...')
d = range(-10 , 0)
print(*d)
e = range(-10)
print(*e)
f = range(2 , 2)
print(*f)
g = range(10 , 11 , 0.1)
h = range('A' , 'F')

a , b , c = r
print(a , b , c) # 10 13 16
r = range(3)
x , y = r
p , q  , r , s = r
a , b , c = *r

x = 25
print(F'{x}')  #  25
print(F'{{x}}')   #  {x}
print(F'{{{x}}}')  #   {25}
print(F'{{{{x}}}}')
print(F'{{{{{x}}}}}')
print(F'{{{{{{x}}}}}}')
print(F'{{{{{{{x}}}}}}}')
print(F'{{{{{{{{x}}}}}}}}')

a = 20
b = 30
print(a is b)
print(a is not b)

set = {1, 2, 3, 4}
print(1 in set)
a = 'hyd'

a = 2
import math
print(math . pow(2 , 3))
print(math . pow(-2 , -3))
print(math .pow(2 , -1))
print(math . pow(4 , 0.5))
import math
print(math . pow(0.2 , 0.2))
print(math .pow(4 , math . pow(-2 , -3)))
import math
print(math . pow(-2 , -3))
print(math. pow(-3 , -2))
print(math . pow(2 , math . pow(2 , 3)))
print(math . pow(2 , 3 ))
import math
print(math . sqrt(4))
print(math . sqrt(0))
print(math . sqrt(255))
print(math . sqrt(math . pow(2 , 3)))
import math
print(math . fabs(-2))
def fabs(x):
    





