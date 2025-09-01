#  intersection()   method  demo  program (Home  work)
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a.intersection(b)
print(c) # {40, 50}
print(type(c)) # <class 'set'>
d = a & b
print(d) # {40, 50}
print(type(d)) # <class 'set'>
print(c  is  d) # False
print(c == d) # True

# difference()   method  demo  program  (Home  work)
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a.difference(b)
print(c) # {10, 20}
print(type(c)) # <class 'set'>
d = a - b
print(d) # {10, 20}
print(type(d)) # <class 'set'>
print(c  is  d) # False 
print(c==d) # True

# symmetric_difference()   method  demo  program  (Home  work)
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a.symmetric_difference(b)
print(c) # {10, 50, 20, 60}
print(type(c)) # <class 'set'>
d = a ^ b
print(d) # {10, 50, 20, 60}
print(type(d)) # <class 'set'>
print(c   is   d) # False
print(c == d)# True

# Find  outputs  (Home  work)
a = {x * x  for   x   in   range(10)}
print(a) # {0, 1, 64, 4, 36, 9, 16, 49, 81, 25}
print(type(a)) # <class 'set'>

'''
Write  a  program  to  remove  duplicate  characters  of  the  string  without  using  set

1) Let  input  be   RAMA  RAO
   What  is  the  output ? ---> RAM<space>O

2) out = '' + 'R' = 'R' + 'A' = 'RA' + 'M' = 'RAM' + ' ' = 'RAM ' + 'O' = 'RAM O'

3) What  action  to  be  made  if  the  character  is  not  in  out  object ?  --->
																	Concatenate  the  character  to  out  object

4) What  action  to  be  made  if  the  character  is  already  in  out  object ?  --->
																							Ignore  the  character

5) Hint:  Use  not  in   operator
'''
a = input('Enter  any  string  :  ')
b = ''
for  ch  in   a:  #  ch  is  each  char  of  the  string
	if   ch   not  in   b:
		b  += ch #   Concatenates  each  char  to  object  'b'  if   it  is not  in  object  'b'
print('String  without  duplicates  :   ' , b)
'''Output:
Enter  input  string :  Rama Rao
String  without  duplicates: ao mR
'''
# Write  a  program  to  remove  duplicate  elements  of   list  using  set
a = eval(input('Enter  list  with  duplicates :  '))  #  Reads  a  list
b = set(a)  #  Converts   list  to  set  so  that duplicate  elements  are  removed
c = list(b)  #   Converts  set  to  list
print('List  without  duplicates :  ' ,  c) # Prints  list
'''Output:
Enter  list  with  duplicates : [False , 25 , 10.8 , 1  , 25 , 0 , 'Hyd' ,  10.8 , 1.0 , None , 'Sec' , 'Hyd' , True  ]
Enter  list  without  duplicates : [False , 25 , 10.8 , 1 , 'Hyd' , None , 'Sec']'''

#Write  a  program  to   obtain  common  elements  between  two  lists  using  sets
list1 = eval(input("Enter 1st list: "))
list2 = eval(input("Enter 2nd list: "))
a = set(list1)
b = set(list2)
c=a.intersection(b)
print(list(c))
'''Output:
Enter 1st list: [10 , 20 , 30 , 40 , 50 , 60]    
Enter 2nd list: [30 , 40 , 70 , 80 , 20]
[20 , 30 , 40]'''

#  How  to  access  values  of  dictionary (Home  work)
a  =  {'Empno'  :  25 ,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
#print(How  to  print  value  25  in  dict  'a')
print(a['Empno']) 
#print(How  to  print  'Rama Rao'  in  dict  'a')
print(a['Ename'])
#print(How  to  print  value  1000.65   in  dict  'a')
print(a['Sal'])
      
# How  to  modify  values  of  dictionary  (Home  work)
a  =  {'Empno' : 25, 'Ename' : 'Rama  Rao'  , 'Sal'  : 1000.65 }
print(a) # {'Empno': 25, 'Ename': 'Rama  Rao', 'Sal': 1000.65}
print(id(a)) # 136585771817344
#How  to  modify  1000.65  to  2000
a['Sal'] = 2000
#How  to  modify  'Rama  Rao'  to  'Sita'
a['Ename'] = 'Sita'
#How  to  modify  25   to  35
a['Empno'] = 35
print(a) # {'Empno': 35, 'Ename': 'Sita', 'Sal': 2000}
print(id(a)) # 136585771817344 

#  How  to  append  key : value  pairs  to dictionary (Home  work)
a  = {'Empno' : 25,  'Ename'  :  'Rama  Rao' , 'Sal'  : 1000.65 }
print(a) # {'Empno': 25, 'Ename': 'Rama  Rao', 'Sal': 1000.65}
#How  to  append  'Gender' : 'M'  to  dictionary  'a'
a['Gender'] = 'M'
#How  to  append  'Married' :  True  to  dictionary  'a'
a['Married'] ='True'
print(a)

# Find  outputs (Home  work)
a = {}
#How  to  append  10 : 'Rama'  to  dictionary  'a'
a[10] = 'Rama'
#How  to  append  20 : 'Sita'  to  dictionary  'a'
a[20] = 'Sita'
#How  to  append  15 : 'Rajesh'  to  dictionary  'a'
a[15] = 'Rajesh'
#How  to  append  18 : 'Kiran'  to  dictionary  'a'
a[18] = 'Kiran'
print(a)

#How  to  remove  key : value  pairs  of  dictionary  (Home  work)
a =  {'Empno' : 25,  'Ename' : 'Rama  Rao'  , 'Sal'  :  1000.65  }
print(a) # {'Empno': 25, 'Ename': 'Rama  Rao', 'Sal': 1000.65}
#How  to  remove  'Sal' : 1000.65  from  dictionary  'a'
a.pop('Sal')
print(a) # {'Empno': 25, 'Ename': 'Rama  Rao'}

#  in  and  not  in  operators  (Home  work)
a =  {10 : 20 , 30 : 40 , 50 : 60 , 70 : 80}
print(30  in  a . keys()) # True
print(60  in  a . keys()) # False
print(60  in  a . values()) # True
print(30  in  a . values()) # False
print(50  in  a) # True
print(20  in  a) # False
print(70  not  in  a . keys()) # False
print(40  not  in  a . values()) # False
print(25 not in a)# True
      
#  What  are  the  outputs  if  input  is  {10: 'A', 20: 'B', 15: 'C' , 20 : 'D'}
a = input('Enter  dictionary  :  ')
print(a) # {10: 'A', 20: 'B', 15: 'C' , 20 : 'D'}
print(type(a)) # <class 'str'>
b = eval(a) 
print(b) # {10: 'A', 20: 'D', 15: 'C'}
print(type(b)) # <class 'dict'>

#  Find  outputs  (Home  work)
a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh' , 18 : 'Kiran'}
b = {**a}
print(b) # {10: 'Rama', 20: 'Sita', 15: 'Rajesh', 18: 'Kiran'}
print(a  is  b) # False
print(a  ==  b) # True
c = a
print(a  is  c) # True
print(a == c) # True
      
#Find  outputs  (Home  work)
a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh'}
b = {18 : 'Kiran' , 14 : 'Amar' , 20  : 'Manohar'}
c = {25 : 'Ramesh' , 19 : 'Krishna' , 15 : 'Radha' , 14 : 'Srinivas'}
d = {*a , *b , *c}
print(d) # {10, 14, 15, 18, 19, 20, 25}
print(type(d)) # <class 'set'>
e = {**a , **b , **c}
print(e) # {10: 'Rama', 20: 'Manohar', 15: 'Radha', 18: 'Kiran', 14: 'Srinivas', 25: 'Ramesh', 19: 'Krishna'}
print(type(e)) # <class 'dict'>

#  Find  outputs  (Home  work)
a = {10 : 20 , 30 : 40}
b = {30 : 50 , 10 : 60}
print(a + b) # Error
c = {**a , **b}
print(c) # {10: 60, 30: 50}
d =a|b
print(d) # {10: 60, 30: 50}

# Write  a  program  to  create  a  dictionary  with  emp  names  and  salaries
# Hint:  Append  each  emp  name  and  salary  to  dictionary  'a'
n = int(input("How many Employees ? : "))  #  Reads number  of  employees
a = { }  #  Empty  dictionary
for  i  in  range(n):  #  Execute  loop  'n'  times
	ename = input('Enter Emp Name : ') #  Reads  emp  name
	sal = float(input('Enter Salary : '))  #   Reads  salary
	a[ename] = sal  #   Appends  ename :  sal  to  dict  'a'
# End  of  for  loop
print(a)
'''Output:
How many Employees ? : 4
Enter Emp Name : AAA
Enter Salary : 100000
Enter Emp Name : BBB
Enter Salary : 200000
Enter Emp Name : CCC
Enter Salary : 150000
Enter Emp Name : DDD
Enter Salary : 175000
{'AAA': 100000.0, 'BBB': 200000.0, 'CCC': 150000.0, 'DDD': 175000.0}'''

''' 
Write  a  program  to  convert  a  string  to  dictionary
Let  input  be   "Emp no = 25 , Emp name = Rama  Rao , sal = 10000.0 , gender = m"
What  is  the  output ?  --->  {Emp no : 25 , Emp name  :  Rama Rao , sal : 10000.0 , gender : m}
Hint :  Use  split()  method  twice
'''
a = input('Enter  string  with  arg1 = value1 , arg2 = value2 , arg3 = value3 , ....  :  ')  #  Reads  a string
b = a . split(',')  #  Divides  string  into  list  of  strings  based  on  ','
c = {}  #  Empty dictionary
for  x  in  b:   #    x  is   element   of   list  'b'
	y = x . split('=')  #   Divides  'x'  into  list  of  2  strings  based  on   '='
	c[y[0]] = y[1] #  Appends  y[0] : y[1]  to  dict  'c'
# End  of  for  loop
print(c)

# len()  function  demo  program  (Home  work)
a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(len(a)) # 3
b = {}
print(len(b)) # 0

#  sum()  function demo  program  (Home  work)
a = {10 : 20 , 30 : 40 , 50 : 60}
print(sum(a . keys())) # 90
print(sum(a . values())) # 120
print(sum(a))  # 90
print(sum(a.items())) # Error

# max()  and  min()   functions  demo  program  (Home  work)
a = {10 : 20 , 30 : 25 , 40 : 5 , 7 : 28 , 9 : 50}
print(max(a . keys())) # 40
print(min(a . keys())) # 7
print(max(a . values())) # 50
print(min(a . values())) # 5
print(max(a . items())) # (40,5)
print(min(a . items())) # (7, 28)
print(max(a)) # 40
print(min(a)) # 7

#  dict()  function  demo program (Home  work))
a = [ (10 , 'Hyd') ,(20 , 'Sec') , (15 , 'Cyb') , (20 , 'Pune')]
b = dict(a)
print(b) # {10: 'Hyd', 20: 'Pune', 15: 'Cyb'}
c = ( ['R' , 'Red'] , ['G' , 'Green'] , ['B' , 'Blue'] , ['G' , 'Gray'])
d = dict(c)
print(d) # {'R': 'Red', 'G': 'Gray', 'B': 'Blue'}
e = [[10 , 20 , 30] , [40 , 50 , 60] , [70 , 80 , 90]]
print(dict(e)) # Error
f = [[10] , [20] , [30]]
print(dict(f)) # Error
print(dict([10 , 20])) # Error
g = [[10 , [20 , 30]] , [40 , [50 , 60]] , [70 , [80 , 90]]]
print(dict(g)) # {10: [20, 30], 40: [50, 60], 70: [80, 90]}
h = [[[10 , 20] , 30] , [[40 , 50] , 60] , [[70 , 80] , 90]]
print(dict(h)) # Error
i = [[(10 , 20) , 30] , [(40 , 50) , 60] , [(70 , 80) , 90]]
print(dict(i)) # {(10, 20): 30, (40, 50): 60, (70, 80): 90}

# sorted()  function  (Home  work)
a = {10 : 'Red' , 20 : 'Green' , 15 : 'Blue' , 18 : 'Yellow' , 5 : 'White'}
b = sorted(a . keys())
print(b) # [5, 10, 15, 18, 20]
c = sorted(a . values())
print(c) # ['Blue', 'Green', 'Red', 'White', 'Yellow']
d = sorted(a . items())
print(d) # [(5, 'White'), (10, 'Red'), (15, 'Blue'), (18, 'Yellow'), (20, 'Green')]
f  = sorted(a  , reverse = True)
print(f) # [20, 18, 15, 10, 5]
print(a) # {10: 'Red', 20: 'Green', 15: 'Blue', 18: 'Yellow', 5: 'White'}

#Tricky  program
'''
Write  a  program  to  sort  dictionary  wrt  keys  (Home  work)
1) Let  input  be   {10 : 'A' , 20 : 'B' , 15 : 'C' , 5 : 'D' , 12 : 'E'}
    What  is  the  output ?  ---> {5 : 'D' , 10 : 'A' ,  12 : 'E' ,  15 : 'C' , 20 : 'B'}
2) Both  input  and  output  are  dictionaries
3) Hint:  Use  sorted()  function
'''
a = eval(input('Enter  dictionary  :  '))  #   Reads  a  dictionary
b = a . items()   #  Converts  dictionary  to   dict_items  object
c = sorted(b)  #  Sorts  the  tuples  in  the  list  of  dict_items  object
print(dict(c))   #  Converts  list  of  tuples  to  dictionary
'''
b = a . items()
c = sorted(b)
print(dict(c))
How  to  reduce  the  above  three  statements  to  a  single  statement ?  --->  print(dict(sorted(a . items())))
'''
# clear()  method  demo  program (Home  work)
a = {10 : 20 , 30 : 40 , 50 : 60}
print(a) # {10: 20, 30: 40, 50: 60}
a . clear()
print(a) # {}
del a # Error
print(a) # {}

# copy()  method demo  program  (Home  work)
a = {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue'}
b = a . copy()
print(b) # {'R': 'Red', 'G': 'Green', 'B': 'Blue'}
print(a  is  b) # False
print(a==b) # True

#  keys()  method  demo  program
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
b = a . keys()
print(b) # dict_keys([10, 20, 15, 18])
print(type(b)) # <class 'dict_keys'>
for  x  in   b:
        print(x)
'''10
   20
   15
   18'''

# values()  method  demo  program
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
b = a . values()
print(b) # dict_values(['Hyd', 'Sec', 'Cyb', 'Pune'])
print(type(b)) # <class 'dict_values'>
for  x   in   b:
	print(x)
''' Hyd
    Sec
    Cyb
    Pune'''

#  items()  method  demo  program
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
b = a . items()
print(b) # dict_items([(10, 'Hyd'), (20, 'Sec'), (15, 'Cyb'), (18, 'Pune')])
print(type(b)) # <class 'dict_items'>
for  x   in   b:
        print(x)
for  x , y   in  b:
        print(x , y , sep = ' ... ')
'''     (10, 'Hyd')
        (20, 'Sec')
        (15, 'Cyb')
        (18, 'Pune')
        10 ... Hyd
        20 ... Sec
        15 ... Cyb
        18 ... Pune'''

# Find  outputs (Home  work)
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
for  x , y   in  a . items():
       print(x , y , sep = ' ... ')
for  x , y   in  a . keys(): # Error
       print(x , y , sep = ' ... ')
for  x , y   in  a . values(): # Error
       print(x , y , sep = ' ... ')
for  x , y   in  a: # Error
       print(x , y ,sep='... ')

'''         10 ... Hyd
            10 ... Hyd
            10 ... Hyd
            10... Hyd
            20 ... Sec
            20 ... Sec
            20 ... Sec
            20... Sec
            15 ... Cyb
            15 ... Cyb
            15 ... Cyb
            15... Cyb
            18 ... Pune
            18 ... Pune
            18 ... Pune
            18... Pune'''
       
#  Find  outputs  (Home  work)
a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh'}
x , y , z = a . keys()
print(x) # 10
print(y) # 20
print(z) # 25
print() # empty
x , y , z = a . values()
print(x) # Rama
print(y) # Sita
print(z) # Rajesh
print() # nothing
x , y ,  z = a . items()
print(x) # (10, 'Rama')
print(y) # (20, 'Sita')
print(z) # (15, 'Rajesh')
print()
(rno1 , sname1) , (rno2 , sname2) , (rno3 , sname3) = a . items()
print(rno1 , sname1) # 10 Rama
print(rno2 , sname2) # 20 Sita
print(rno3 , sname3) # 15 Rajesh

'''
Tricky  program
(Home  work)
Write  a program  to  determine  frequency  of  each  alphabet  in  the  string   in   alphabetical  order
(ignoring  the  case)

Let  input  be   RamA raO
What  is  the  output ?  ---> {'A' : 3 , 'M' : 1 , 'O' : 1 , 'R' : 2}  in  alphabetical  order

1) What  is  the  string  after  it  is  converted  to  uppercase ?  --->  'RAMA RAO'

2) What  is  the  result  of  sorted('RAMA RAO') ?  --->  [' ' , 'A' , 'A' , 'A' , 'M' , 'O' , 'R' , 'R']

3) What  is  dictionary  'a'  initially ?  --->  { }

4) What  is  the  first  element  in  list ?  --->  ' '
    What  action  to  be  made  for  ' ' ?  --->  Ignore  becoz  it  is  not  an  alphabet

5) What  is  the  2nd  element  in  list ?  ---> 'A'
    What  is  a['A']  ?  --->  a . get('A' , 0) + 1 = 0 + 1 = 1
    What  does  a['A']  =  1  do ?  --->  Appends  'A' : 1  to  dict  'a'
    What  is  dictionary  'a' ?  --->  {'A' : 1}

6) What  is  the  3rd  element  in  list ?  --->  'A'
    What  is  a['A']  ?  --->  a . get('A' , 0) + 1 =  1 + 1 = 2
    What  does  a['A']  =  2  do ?  --->  Modifies  value  of  'A'  to  2  in dict  'a'
    What  is  dictionary  'a' ?  --->  {'A' : 2}

7) What  is  the  4th  element  in  list ?  --->  'A'
    What  is  a['A']  ?  --->  a . get('A' , 0) + 1 =  2 + 1 = 3
    What  does  a['A'] = 3  do ?  --->  Modifies  value  of  'A'  to  3  in dict  'a'
    What  is  dictionary  'a' ?  ---> {'A' : 3}

8) What  is  the  5th  element  in  list ?  --->  'M'
     What  is  a['M']  ?  --->  	 a . get('M' , 0) + 1 =  0 + 1 = 1
    What  does  a['M'] = 1  do ?  --->  Appends  'M' : 1  to  dict  'a'
    What  is  dictionary  'a' ?  ---> {'A' : 3 , 'M' : 1}

9) What  is  the  6th  element  in  list ?  ---> 'O'
     What  is  a['O']  ?  --->  a . get('O' , 0) + 1 =  0 + 1 = 1
     What  does  a['O'] = 1  do ?  ---> Appends  'O' : 1  to  dict  'a'
     What  is  dictionary  'a' ?  --->  {'A' : 3 , 'M' : 1 , 'O' : 1}

10) What  is  the  7th  element  in  list ?  ---> 'R'
      What  is  a['R']  ?  --->  a . get('R' , 0) + 1 =  0 + 1 = 1
       What  does  a['R'] = 1  do ?  --->  Appends  'R' : 1  to  dict  'a'
	  What  is  dictionary  'a' ?  ---> {'A' : 3 , 'M' : 1 , 'O' : 1 , 'R' : 1}

11) What  is  the  last  element  in  list ?  --->  'R'
      What  is  a['R']  ?  --->  a . get('R' , 0) + 1 =  1 + 1 = 2
      What  does  a['R'] = 2  do ?  ---> Modifies  value  of  'R'  to  2  in dict  'a'
      What  is  dictionary  'a' ?  --->  	{'A' : 3 , 'M' : 1 , 'O' : 1 , 'R' : 2}

11) Finally  what   is  dict  'a' ?  ---> {'R' : 2 , 'A' : 3 , 'M' : 1 , 'O' : 1}
'''
a = input('Enter  mixed  case  string : ')  #   Reads  a  string
a = a . upper()  #  Converts string  to  uppercase
b = sorted(a)  #  Sorts  characters  of  the  uppercase  string   to  form  a  list
c = { }  # Empty  dictionary
for  ch  in   b:  # ch  is   each  char  of  the  list
	if  ch . isalpha():  #  Is  ch  an  alphabet
		c[ch] = c . get(ch , 0) + 1
# End  of  for  loop
print(c)