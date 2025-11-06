'''
Modify  following  porgram  such  that
1) Use  regular  function  instead  of  lambda  function
2) Use  for  loop  instead  of  while  loop
'''
import  time
list = [10,20,15,18,5]
def f1(x):
	return x*x
m = map(f1 , list)
print(type(m)) # <class 'map'>
print(m) # type and address of m
for a in m:
	print(a)
	time.sleep(0.5)
	

# Find  outputs 
import  time
a = [ ('A',10) , ('B',20),('C', 15) , ('D', 5) , ('E',18) ]
m = map(lambda x : x[1] , a)
while   True:
	try:
		print(next(m))
		time.sleep(1)
	except StopIteration:
		break
'''
o/p:
10
20
15
5
18
'''


# Find  outputs 
import   time
def  disp(m):
	while   True:
		try:
			print(next(m))
			time.sleep(0.5)
		except  StopIteration:
			break
list = [ {'country' : 'India' , 'sale' : 150.5} ,
        {'country' : 'China' , 'sale' : 200.2} ,
        {'country' : 'USA' , 'sale' : 300.3} ,
        {'country' : 'UK' , 'sale' : 210.4} ]
m1 = map(lambda  x : x['country'] , list)
print('Map m1')
disp(m1)
m2 = map(lambda x : x['sale'] , list)
print('Map m2')
disp(m2)
'''
o/p:
Map m1
India
China
USA
UK
Map m2
150.5
200.2
300.3
210.4
'''


'''
Write  a  program  to  convert  each  celsius  temperature  of  the  list  to  farenheit  temperature
1) What is the formula to convert celsius temperature  to  farenheit ?  --->  1.8 * celsius-temp + 32
2) Let input be list of celsius temperatures such  as  [30 , 40 , 50 , 25]
    What  is  the  output ?  --->  1.8 * 30 + 32
							                      1.8 * 40 +32
								                  1.8 * 50 + 32
								                  1.8 * 25 + 32
'''
a=eval(input('enter a list :'))
def f1(x):
    return 1.8*x+32
m = list(map(f1, a))
print("Celsius Temperatures:", a)
print("Fahrenheit Temperatures:", m)
'''
o/p:
enter a list :[30, 40, 50, 25]
Celsius Temperatures: [30, 40, 50, 25]
Fahrenheit Temperatures: [86.0, 104.0, 122.0, 77.0]
'''


# Write  a  program  to  print  2 ^ 0 , 2 ^ 1 , 2 ^ 2 , ....... 2 ^ 9  using  map   iterator 
def power(x):
    return 2 ** x
m=list(map(power,range(10)))
for x in m:
    print(x)
'''
o/p:
1
2
4
8
16
32
64
128
256
512
'''


'''
Write  a  program  to  determine  area  of  circle  for  each  radius  in  the  list

1) What  is  area  of  circle ?  --->  3.14159 * r * r

2) Let  input  be  [3.5 , 2.8 , 4.2 ,1.9]
    What  are  the  outputs ?  --->   Area  of  radius  3.5
						                              Area  of  radius  2.8
						                              Area  of  radius  4.2
						                              Area  of  radius  1.9
'''
def area(r):
    return  3.14159 * r * r

a=eval(input('enter list of radii :'))
print('Area of each radius in the list')
m=list(map(area , a))
for x in m:
    print(f'{x:0.2f}')
'''
o/p:
enter list of radii :[3.5 , 2.8 , 4.2  , 1.9]
Area of each radius in the list
38.48
24.63
55.42
11.34
'''



'''
Write  a  program  to  add  two  tuples  of  difierent  sizes  and  store  the  results  in  3rd  tuple

Let  1st  tuple  be  (10,20,30,40)  and  2nd  tuple  be  (1,2,3,4,5,6)
What  is  the  3rd  tuple ?  --->  (10 + 1 , 20 + 2 , 30 + 3 , 40 + 4)   and  5  and 6  are  ignored
'''
a=eval(input('enter first tuple :'))
b=eval(input('enter second tuple :'))
def f1(x,y):
    return x+y
m=tuple(map(f1,a,b))
print('Addition tuple',m)
'''
o/p:
enter first tuple :(10,20,30,40)
enter second tuple :(1,2,3,4,5,6)
Addition tuple (11, 22, 33, 44)
'''



'''
Write  a  program  to  multiply  two  lists  and  store  results  in  3rd  list

Let  1st  list  be  [10 , 20 , 15 , 18 , 19 , 17]  and  2nd  list  be  [1 , 5 , 3 , 2]
What  is  the  3rd  list ?  --->  [10 * 1 , 20 * 5 , 15 * 3 , 18 * 2]  and  ignores  19  and  17
'''
a=eval(input('enter first list :'))
b=eval(input('enter second list :'))
def f1(x,y):
    return x*y
m=list(map(f1,a,b))
print('Multiplication list',m)
'''
o/p:
enter first list :[10,20,15,18,19,17]
enter second list :[1,5,3,2]
Multiplication list [10, 100, 45, 36]
'''


# map  inside  filter 
import   time
a = [10,20,15,12,18,5,14,25,17]
f = filter(lambda y : y % 2 == 0 , map(lambda  x : x ** 2 , a)) # filters only even numbers from the squared values
while   True:
	try:
		print(next(f))
		time.sleep(1)
	except:
		break
'''
o/p:
100
400
144
324
196
'''


# filter  inside  map
import  time
a = [10 , 20 , 15 , 12 , 18 , 5 , 14 , 25 , 17]
m = map(lambda  y : y + y ,  filter(lambda  x  :  x >= 15 , a)) # doubles each number which is greater than or equal to 15
while   True:
	try:
		print(next(m))
		time.sleep(1)
	except:
		break
'''
o/p:
40
30
36
50
34
'''



'''
Write  a  program  to  determine  largest  element  of  the  list  with  reduce()  function
Let  list   be  [10 , 20 , 15 , 30 , 25 , 40 , 35]
What  is   the  largest  element  of  list ?  --->  40
Hint:  Use  reduce()  function
'''

from functools import reduce
a = [10,20,15,30,25,40,35]
largest = reduce(lambda x, y: x if x > y else y, a)
print("Largest element of list:", largest) # Largest element of list: 40


#Find  outputs  
from functools import reduce
a = [ 10,20,15,5,12,18,25,14]
ans = reduce(lambda  x , y: x + y ,map(lambda  y :  y ** 2 ,filter(lambda x : x >= 15, a)))
print(ans) # 1574
