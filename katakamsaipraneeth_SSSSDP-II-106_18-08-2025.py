#  len()  function demo   program  (Home  work)
a = [ 25, 10.8, 'Hyd', True] # list obj
print(len(a)) # 4
b = [] # empty list obj
print(len(b)) # 0
c = [[10 , 20] , 30 , 40] # nested list
print(len(c)) # 3


'''
What  does  len(list)  do ?  --->  Returns  number  of  elements  in  the  list
'''

# sum()  function  demo  program  (Home  work)
a = [25 , 10.8 , True] # list obj
print(sum(a)) # 36.8
b= [3 + 4j , 5 + 6j] # list obj
print(sum(b)) # 8 + 10j
c = [25 , 10.8 , True , 3 + 4j , False] # list obj
print(sum(c)) # 39.8 + 4j
d = [10 , 20 , 15 , 18] # list obj
print(sum(d)) # 
e = [25 , 10.8 , 'Hyd' , True]
print(sum(e))


'''
What  does  sum(list)  do ?  ---> Returns  sum  of  list  elements
'''

#  Find  outputs
a = [[10 , 20 , 15 , 18]] # list obj
print(sum(a)) # error
print(sum(a[0]) # How  to  determine  sum  of  inner  list  elements
total = 0
for i in a[0]:
    total += i
print(total) # How  to  determine  sum  of  inner  list  elements  in  another  way


# max()  and  min()  functions  demo  program  (Home  work)
a = [10 , 20 , 15 , 18 , 30, 5 , 12] # list obj
print(max(a)) # 30
print(min(a)) # 5
b = ['Rama' , 'Sita' , 'Rajesh' , 'Kiran' , 'Amar' , 'Vamsi' , 'Manohar']
print(max(b)) # Vamsi
print(min(b)) # Amar
c = [25 , 10.8 ,  3 + 4j , True] # list obj
print(max(c)) # error
d = [25 , '35'] # list obj
print(max(d)) # error
print(max([])) # error
print(min([])) # error


'''
1) What  does  max(list)  do ?  --->  Returns  largest  element  of  the  list

2) What  does  min(list)  do ?  --->  Returns  smallest  element  of  the  list
'''


# list()  function  demo  program
a = (10 , 20 , 15, 18) # tuple obj
b = list(a) # tuple is converted to list
print(b) # [10 , 20 , 15, 18]
print(type(b)) # <class 'list'>
print(a  is  b) # False
print(a == b) # False


#  Find  outputs (Home  work)
a = range(4 , 10 , 2) # range obj
b = list(a) # converted to list
print(b) # [4,6,8]
print(type(b)) # <class 'list'>
a = list('Vamsi') # converted to list
print(a) # ['Vamsi']
a = list() # empty list 
print(a) # []
print(list(25)) # error
print(list(10.8)) # error
print(list(True)) # error
print(list(None)) # error


'''
1) What  does  list(sequence)  do ?  --->  Converts  sequence  to  list  and  returns  list

2) What  does  list(no-args)  do ?  ---> Returns  an  empty  list

3) What  does  list(non-sequence)  do ?  --->  Throws  error
'''

# Find  outputs (Home  work)
a = ((10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90)) # tuple obj
print(list(a)) # [(10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90)]
b = { (10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90)} # tuple obj
print(list(b)) # [(10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90)]
c = ([10 , 20] , (30 , 40) , {50 , 60}) # tuple obj
print(list(c)) # [[10 , 20] , (30 , 40) , {50 , 60}]


# sorted()  function   demo  program
a = [10 , 20 , 15 , 5 , 12] # list obj
b = sorted(a) # [5,10,12,15,20]
print(b) # [5,10,12,15,20]
print(type(b)) # <class 'list'>
c = sorted(a , reverse = True) # [20,15,12,10,5]
print(c) # [20,15,12,10,5]
print(a) # [10 , 20 , 15 , 5 , 12]


'''
sorted()  function
----------------------
1) What  does  sorted(list)  do  ?  ---> Returns  another  sorted  list

2) Is  argument  list  modified ?  --->  No  and  it  remains  unchanged

3) How  to  sort  list  in  descending  order ?  --->  sorted(list , reverse = True)

4) What  are  the  two  arguments  of  sorted()  function ?  --->  List  to  be  sorted and reverse = True  which  is  an  optional  argument
'''

# Find  outputs  (Home  work)
a = ['Rama',  'Rajesh',  'Amar',  'Sita',  'Vamsi'  ,  'Kiran'  , 'Rama  Rao'] # list obj
b = sorted(a) # ['Amar', 'Kiran', 'Rajesh','Rama', 'Rama  Rao', 'Sita', 'Vamsi']
print(b) # ['Amar', 'Kiran', 'Rajesh','Rama', 'Rama  Rao', 'Sita', 'Vamsi']
c = sorted(a , reverse = True) # ['Vamsi', 'Sita', 'Rama  Rao', 'Rama', 'Rajesh', 'Kiran', 'Amar']
print(c) # ['Vamsi', 'Sita', 'Rama  Rao', 'Rama', 'Rajesh', 'Kiran', 'Amar']
print(a) # ['Rama',  'Rajesh',  'Amar',  'Sita',  'Vamsi'  ,  'Kiran'  , 'Rama  Rao']


# all()  function demo  program  (Home  work)
a = [12 > 10 , 5 < 20 , 30 == 30] # list obj
print(all(a)) # True
b = [9 >= 6 , 12 <= 9 , 6 == 6] # list obj
print(all(b)) # False
c = [25 , 10.8 , '' , True , 3+4j , 'Hyd'] # list obj
print(all(c)) # False
d = [10 , 0 , 20] # list obj
print(all(d)) # False
e = [] # list obj
print(all(e)) # False


'''
all()  function
-----------------
1) What  does  all(list)  do ?  --->  Returns  True  when  every  element of  the  list  is  True  and  False  otherwise

2) When  does  it  return  False ?  --->  When  at  least  one  element  of  the  list  is  False

3) if  cond1  and  cond2  and  cond3  and  cond4:
    How  to  reduce  the  four  conditions  to  a  single  condition ?  --->  if  all([cond1 , cond2 , cond3 , cond4]):
'''

# any()  function demo program  (Home  work)
a  = [12 > 18 , 5 < 20 , 35 == 30] # list obj
print(any(a)) # True
b = [12 > 18 , 25 < 20 , 35 == 30] # list obj
print(any(b)) # False
c = [0 , 0.0 , '' , 25 , 0 + 0j , False] # list obj
print(any(c)) # True
d = [0 , 0.0 , '' , 0 + 0j , False] # list obj
print(any(d)) # False
e = [] # empty list
print(any(e)) # False


'''
any()   function
-------------------
1) What  does  any(list)  do ?  ---> Returns  True  when  at  least  one  element  of  the  list  is  True  and  False  otherwise

2) When  does  it  return  False ?  ---> When  every  element  of  the  list  is  false

3) if  cond1  or  cond2  or  cond3  or  cond4:
     How  to  reduce  the  four  conditions  to  a  single  condition ?  ---> if  any([cond1 , cond2 , cond3 , cond4]):

4) all()  and  any()  functions  are  used  as  an  alternative  when  there  are  too  many  conditions  in  if  and  while
'''


# del  operator  demo  program (Home  work)
a = [10 , 20 , 15 , 18] # list obj
print(a) # [10 , 20 , 15 , 18]
del    a[2] # deletes element 15 at index 2
print(a) # [10, 20, 18]
del  a[3] # error no index 3
del  a # deletes list obj 'a'
print(a) # error


#  append()  method  demo  program (Home  work)
list = [10 , 20 , 15 , 18] # list obj
print(list) # [10 , 20 , 15 , 18]
list . append(19) # [10 , 20 , 15 , 18, 19]
print(list) # [10 , 20 , 15 , 18, 19]


#  Find  outputs (Home  work)
list = [] # empty list 
print(list) # []
list . append(25) # it appends 25 into list
list . append(10.8) # it appends 10.8 into list
list . append('Hyd') # it appends 'Hyd' into list
list . append(True) # it appends True into list
print(list) # [25, 10.8 ,'Hyd', True]


# Find  outputs  (Home  work)
list = [] # list obj
for  x  in   range(0 , 50 , 10): # for loop in range of 0 to 49 in steps of 10
	list . append(x) # appends element with step 10
print(list) # [10,20,30,40]


#  Find  outputs  (Home  work)
a = [10 , 20 , 30] # list obj
a . append('Hyd') # appends 'Hyd' to list a 
print(a) # [10 , 20 , 30, 'Hyd']
print(len(a)) # 4
print(a[3]) # How  to  print  4th  element  of  list  'a'
print(a[3][0]) # How  to  print  'H'
print(a[3][1]) # How  to  print  'y'
print(a[3][2]) # How  to  print  'd'


# remove()  method  demo  program  (Home  work)
try:
	list = [10 , 20 , 15 , 18 , 15 , 12 , 15 , 19] # list obj
	list . remove(15) # removes first occurence of list
	print(list)
	list . remove(25)
except:
	print('25  is   not  in  the  list')



'''
remove()   method
---------------------
1) What  does  remove(x)  do ?  --->  Removes   first  occurance  of  'x'  from  the  list

2) What  does  remove()  method  do  if  'x'  is  not   in  the  list ?  --->  Throws  ValueError

3) How  to  remove  all  ocurances  of  'x'  from  the  list ?  --->   Call  remove()  method  in  a  loop
'''

'''
Write  a  program  to  delete  'all'  occurences  of  'x'  from  the  list

Let  1st  input  be   [10 , 20 , 15 , 18 , 19 , 15 , 17 , 20 , 15 , 14]  and
2nd  input  be  15
What  is  the  output ?  ---> [10 , 20 ,  18 , 19 , 17 , 20 , 14]
'''
############### program #####################33
list = eval(input("Enter list:"))
li = eval(input("Enter  element  to  be  deleted :")) # list obj
for i in list:
    if i == li:
        list.remove(i)
print(F"List  without   {li}'s : {list}")

Enter List  :  [10 , 20 , 15 , 18 , 19 , 15 , 17 , 20 , 15 , 14]
Enter  element  to  be  deleted : 15
List  without   15's :  [10, 20, 18, 19, 17, 20, 14]


# clear() method  demo program  (Home  work)
list = [10 , 20 , 15 , 18] # list obj
print(list) # [10 , 20 , 15 , 18]
list . clear() # removes all elements in list
print(list) # []


'''
clear()  method
------------------
1) What  does  clear()  method  do ?  --->  Removes  all  the  elements  of  the  list  and  list  becomes  empty

2) What  about  remove()  and  pop()  methods  ?  ---> They  remove  single  element  of  the  list
'''

# reverse()  method  demo  program (Home  work)
a = [10 , 20 , 15 , 18] # list obj
print(a) # [10 , 20 , 15 , 18]
a . reverse() # reverses all the elements in list
print(a) # [18,15,20,10]


'''
reverse()  method
---------------------
1) What  does  reverse()  method  do ?  --->  Reverses  all  the  elements  of  list

2) Where  are  the  results  stored ?  --->  In  the  same  list  replacing  existing  elements (List  is  mutable)
'''


#  sort()  method  demo  program (Home  work)
list = [10 , 20 , 15 , 18 , 5] # list obj
print(list) # [10 , 20 , 15 , 18 , 5]
list . sort() # [5, 10, 15, 18, 20]
print(list) # [5, 10, 15, 18, 20]
list . sort(reverse = True) # [20, 18, 15, 10, 5]
print(list) # [20, 18, 15, 10, 5]


# Find  outputs (Home  work)
a = ['Rama' , 'Rajesh' , 'Amar' ,  'Sita' ,  'Vamsi' , 'Kiran' , 'Rama  Rao']
print(a) # ['Rama' , 'Rajesh' , 'Amar' ,  'Sita' ,  'Vamsi' , 'Kiran' , 'Rama  Rao']
a . sort() # ['Amar', 'Kiran', 'Rajesh','Rama', 'Rama  Rao', 'Sita', 'Vamsi']
print(a) # ['Amar', 'Kiran', 'Rajesh','Rama', 'Rama  Rao', 'Sita', 'Vamsi']
a . sort(reverse = True) # reversed list
print(a) # ['Vamsi', 'Sita', 'Rama  Rao', 'Rama', 'Rajesh', 'Kiran', 'Amar']

# Identify  error (Home  work)
a = [25 , 10.8 ,  'Hyd' ,  True] # list obj
a . sort() # error


#  count()  method  demo    program (Home  work)
a = [10 , 20 , 15 , 18 , 15 , 12 , 14 , 15 , 19]
print(a . count(15)) # 3
print(a . count(25)) # error
print(len(a)) # 9


'''
What  does  list . count(x)  do ?  ---> Returns  number  of  times  'x'  is  in  the  list
'''

'''
Tricky  program
Write  a  program  to  remove  all  duplicate  elements  of  the  list  (Not  even  single  occurance)
Let  input  be  [10 , 20 , 15 , 10 , 14 , 10 , 18 , 20 , 19]
What  is  the  output ?  ---> [15 , 14 , 18 , 19]

Hint:  Use  count()  and  append()  methods
'''
####################### program ################3333
a = [10 , 20 , 15 , 10 , 14 , 10 , 18 , 20 , 19]
for i in a[:]:
    if a.count(i) > 1:
        a.remove(i)
print("Output:", a)  # Output: [15, 14, 18, 19]


'''
Write  a  program  to  determine  all  the  list  elements  are  identical  or  not

1) Let  input  be  [25 , 25 , 25 , 25]
    What  is  the  output ?  ---> All  the  elements  are  identical
    How  many  elements  are  in  the  list ?  --->  4
    How  many  times  is  first  element  repeated ?  ---> 4

2) Let  input  be  [10 , 10 , 20 ,  10]
    What  is  the  output ?  --->All  the  elements  are  not  identical
    How  many  elements  are  in  the  list ?  ---> 4
    How  many  times  is  first  element  repeated ? --->  3

3) Hint: Use  len()  and  count()
'''
################# program ##################33
a = eval(input("Enter  any  list  :"))

if a.count(a[0]) == len(a):
    print("All  the  list  elements  are  identical")
else:
    print("All  the  list  elements  are  not  identical")

Enter  any  list  :  [25,25,25,25]
All  the  list  elements  are  identical


Enter  any  list  :  [10,10,20,10]
List   elements  are  not  identical


# index()  method  demo  program  (Home  work)
a = [10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25]
#    0     1    2    3    4    5    6    7    8    9    10
try:
	i = a . index(15)
	while  True:
		print(i)
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









