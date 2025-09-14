
#  len()  function demo   program  (Home  work)
a = [ 25, 10.8, 'Hyd', True]
print(len(a)) # 4
b = []
print(len(b)) # 0
c = [[10 , 20] , 30 , 40]
print(len(c)) # 3

# sum()  function  demo  program  (Home  work)
a = [25 , 10.8 , True]
print(sum(a)) # 36.8
b= [3 + 4j , 5 + 6j]
print(sum(b)) #  8 + 10j
c = [25 , 10.8 , True , 3 + 4j , False]
print(sum(c)) # 39 + 4j
d = [10 , 20 , 15 , 18]
print(sum(d)) # 63
e = [25 , 10.8 , 'Hyd' , True]
print(sum(e)) # error as float and string cannot be added

#  Find  outputs
a = [[10 , 20 , 15 , 18]]
print(sum(a)) # error 
print(sum(a[0])) # How  to  determine  sum  of  inner  list  elements)
print(sum(a[-1])) # How  to  determine  sum  of  inner  list  elements  in  another  way)

# max()  and  min()  functions  demo  program  (Home  work)
a = [10 , 20 , 15 , 18 , 30, 5 , 12]
print(max(a)) # 30
print(min(a)) # 5
b = ['Rama' , 'Sita' , 'Rajesh' , 'Kiran' , 'Amar' , 'Vamsi' , 'Manohar']
print(max(b)) # Vamsi
print(min(b)) # Amar
c = [25 , 10.8 ,  3 + 4j , True]
print(max(c)) # error 
d = [25 , '35']
print(max(d)) # error as int and string cannot be compared
print(max([])) # error
print(min([])) # error

# list()  function  demo  program
a = (10 , 20 , 15, 18)
b = list(a)
print(b) # [10 , 20 , 15 , 18]
print(type(b)) # <class 'list'>
print(a  is  b) # False
print(a == b) # False

#  Find  outputs (Home  work)
a = range(4 , 10 , 2)
b = list(a)
print(b) # [4 , 8]
print(type(b)) # <class 'list'>
a = list('Vamsi')
print(a) # ['Vamsi']
a = list()
print(a) # []
print(list(25)) # error becoz arg is non-sequence
print(list(10.8)) # error becoz arg is non-sequence
print(list(True)) # error becoz arg is non-sequence
print(list(None)) # error becoz arg is non-sequence

# Find  outputs (Home  work)
a = ((10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90))
print(list(a)) # [(10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90)]
b = { (10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90)}
print(list(b)) # [(10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90)] can be any order
c = ([10 , 20] , (30 , 40) , {50 , 60})
print(list(c)) # [[10 , 20] , (30 , 40) , {50 , 60}]

# sorted()  function   demo  program
a = [10 , 20 , 15 , 5 , 12]
b = sorted(a)
print(b) # [5 , 10 , 12 , 15 , 20]
print(type(b)) # <class 'list'>
c = sorted(a , reverse = True)
print(c) # [20 , 15 , 12 ,10 , 5]
print(a) # [10 , 20 , 15 , 5 , 12]

# Find  outputs  (Home  work)
a = ['Rama',  'Rajesh',  'Amar',  'Sita',  'Vamsi'  ,  'Kiran'  , 'Rama  Rao']
b = sorted(a)
print(b) # ['Amar', 'Kiran', 'Rajesh', 'Rama', 'Rama  Rao', 'Sita', 'Vamsi']
c = sorted(a , reverse = True)
print(c) # ['Vamsi', 'Sita', 'Rama  Rao', 'Rama', 'Rajesh', 'Kiran', 'Amar']
print(a) # ['Rama', 'Rajesh', 'Amar', 'Sita', 'Vamsi', 'Kiran', 'Rama  Rao']


# all()  function demo  program  (Home  work)
a = [12 > 10 , 5 < 20 , 30 == 30]
print(all(a)) # True
b = [9 >= 6 , 12 <= 9 , 6 == 6]
print(all(b)) # False
c = [25 , 10.8 , '' , True , 3+4j , 'Hyd']
print(all(c)) # False
d = [10 , 0 , 20]
print(all(d)) # False
e = []
print(all(e)) # True

# any()  function demo program  (Home  work)
a  = [12 > 18 , 5 < 20 , 35 == 30]
print(any(a)) # True
b = [12 > 18 , 25 < 20 , 35 == 30]
print(any(b)) # False
c = [0 , 0.0 , '' , 25 , 0 + 0j , False]
print(any(c)) # False
d = [0 , 0.0 , '' , 0 + 0j , False]
print(any(d)) # False
e = []
print(any(e)) # True

# del  operator  demo  program (Home  work)
a = [10 , 20 , 15 , 18]
print(a) # [10 , 20 , 15 , 18]
del    a[2] # delete element at index 2
print(a) # [10 , 20 , 18]
del  a[3] # error as there is no element at index 3
del  a
print(a) # error as object a is deleted

#  append()  method  demo  program (Home  work)
list = [10 , 20 , 15 , 18]
print(list) # [10 , 20 , 15 , 18]
list . append(19) # appends 19 to the list
print(list) # [10 , 20 , 15 , 18 , 19]

#  Find  outputs (Home  work)
list = []
print(list) # []
list . append(25) # appends 25 to the list
list . append(10.8) # appends 10.8 to the list
list . append('Hyd') # appends Hyd to the list
list . append(True) # appends True to the list
print(list) # [25 , 10.8 , 'Hyd' , True]

# Find  outputs  (Home  work)
list = []
for  x  in   range(0 , 50 , 10):
	list . append(x)
print(list) # [0 , 10 , 20 , 30 , 40]

#  Find  outputs  (Home  work)
a = [10 , 20 , 30]
a . append('Hyd')
print(a) # [10 , 20 , 30 , 'Hyd']
print(len(a)) # 4
print(a[3]) # How  to  print  4th  element  of  list  'a')
print(a[3][0]) # How  to  print  'H')
print(a[3][1]) # How  to  print  'y')
print(a[3][2]) # How  to  print  'd')

# remove()  method  demo  program  (Home  work)
try:
	list = [10 , 20 , 15 , 18 , 15 , 12 , 15 , 19]
	list . remove(15)
	print(list) # [10 , 20 , 18 , 15 , 12 , 15 , 19]
	list . remove(25) # Error as 25 is not there in the list and a user friendly message is printed
except:
	print('25  is   not  in  the  list')

'''
Write  a  program  to  delete  'all'  occurences  of  'x'  from  the  list

Let  1st  input  be   [10 , 20 , 15 , 18 , 19 , 15 , 17 , 20 , 15 , 14]  and
2nd  input  be  15
What  is  the  output ?  ---> [10 , 20 ,  18 , 19 , 17 , 20 , 14]

Enter List  :  [10 , 20 , 15 , 18 , 19 , 15 , 17 , 20 , 15 , 14]
Enter  element  to  be  deleted : 15
List  without   15's :  [10, 20, 18, 19, 17, 20, 14]
'''
try:
	a = eval(input('Enter List of numbers : '))
	b = eval(input('Enter a element to be removed : '))
	while True:
		a . remove(b)
except:
	print(f'List without {b} : {a}')

# clear() method  demo program  (Home  work)
list = [10 , 20 , 15 , 18]
print(list) # [10 , 20 , 15 , 18]
list . clear() # removes all the elements from the list
print(list) # []

# reverse()  method  demo  program (Home  work)
a = [10 , 20 , 15 , 18]
print(a) # [10 , 20 , 15 , 18]
a . reverse() # reverses all the elements of the list
print(a) # [18 , 15 , 20 , 10]

#  sort()  method  demo  program (Home  work)
list = [10 , 20 , 15 , 18 , 5]
print(list) # [10 , 20 , 15 , 18 , 5]
list . sort()
print(list) # [5 , 10 , 15 , 18 , 20]
list . sort(reverse = True)
print(list) # [20 , 18 , 15 , 10 , 3]

# Find  outputs (Home  work)
a = ['Rama' , 'Rajesh' , 'Amar' ,  'Sita' ,  'Vamsi' , 'Kiran' , 'Rama  Rao']
print(a) # ['Rama', 'Rajesh', 'Amar', 'Sita', 'Vamsi', 'Kiran', 'Rama  Rao']
a . sort()
print(a) # ['Amar', 'Kiran', 'Rajesh', 'Rama', 'Rama  Rao', 'Sita', 'Vamsi']
a . sort(reverse = True)
print(a) # ['Vamsi', 'Sita', 'Rama  Rao', 'Rama', 'Rajesh', 'Kiran', 'Amar']

# Identify  error (Home  work)
a = [25 , 10.8 ,  'Hyd' ,  True]
a . sort() # error as we cannot compare with string

#  count()  method  demo    program (Home  work)
a = [10 , 20 , 15 , 18 , 15 , 12 , 14 , 15 , 19]
print(a . count(15)) # 3
print(a . count(25)) # 0
print(len(a)) # 9

'''
Tricky  program
Write  a  program  to  remove  all  duplicate  elements  of  the  list  (Not  even  single  occurance)
Let  input  be  [10 , 20 , 15 , 10 , 14 , 10 , 18 , 20 , 19]
What  is  the  output ?  ---> [15 , 14 , 18 , 19]

Hint:  Use  count()  and  append()  methods
'''
a = eval(input('Enter  List :  '))
b = []
for  x  in  a:
	if a . count(x) == 1:
		b . append(x)
print(b)

'''
Write  a  program  to  determine  all  the  list  elements  are  identical  or  not

1) Let  input  be  [25 , 25 , 25 , 25]
    What  is  the  output ?  ---> All  the  elements  are  identical
    How  many  elements  are  in  the  list ?  --->  4
    How  many  times  is  first  element  repeated ?  ---> 4

2) Let  input  be  [10 , 10 , 20 ,  10]
    What  is  the  output ?  ---> All  the  elements  are  not  identical
    How  many  elements  are  in  the  list ?  ---> 4
    How  many  times  is  first  element  repeated ? --->  3

3) Hint: Use  len()  and  count()

Enter  any  list  :  [25,25,25,25]
All  the  list  elements  are  identical

Enter  any  list  :  [10,10,20,10]
List   elements  are  not  identica
'''
a = eval(input('Enter a List : '))
if a.count(a[0]) == len(a):
	print('All the elements are identical')
else:
	print('All  the  elements  are  not  identical')
# index()  method  demo  program  (Home  work)
a = [10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25]
#     0     1     2    3    4     5    6    7     8    9    10
try:
	i = a . index(15)
	while  True:
		print(i) # 2 <next line> 5 <next line> 7
		i = a . index(15 , i + 1)
except:
	print(F'15  is  found  {a . count(15)}  times ')


'''
index()  method
-------------------
1) What  does  index(x)  do ?  --->  Returns  index  of  first  'x'  in  the  list

2) What  does  index(invalid-element)  do  ?  --->  Throws  error

3) list . index(x , i)
    list . index(x)
    What  is  the  difference  between  the  two  statements ?  --->
										list . index(x , i)  searches  for  'x'  from   index  'i'  of  the  list  but
										list . index(x)   searches  for  for  'x'  from   index  0  of  the  list

Note:
1) What  are  the  four  search  methods  in  str  class  --->  find() , rfind() , index() , rindex()

2) What  is  the  only  search  method  in  list  class  ---> index()
'''
