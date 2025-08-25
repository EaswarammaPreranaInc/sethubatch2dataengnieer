#  intersection()   method  demo  program (Home  work)
a = {10 , 20 , 30 , 40} # Ref 'a' points to set
b = {30 , 40 , 50 , 60} # Ref 'b' points to set
c = a . intersection(b) # gives common elements of a and b and assigned to 'c'
print(c) # prints 'c' i.e., {30, 40}
print(type(c)) # prints type of 'c' i.e., <class 'set'>
d = a & b # gives common elements of a and b and assigned to 'd'        
print(d) # prints 'd' i.e., {30, 40}
print(type(d)) # prints type of 'd' i.e., <class 'set'>
print(c  is  d) # False because c and d points to different sets
print(c  ==  d) # True because c and d contain same elements
















# difference()   method  demo  program  (Home  work)
a = {10 , 20 , 30 , 40} # Ref 'a' points to set
b = {30 , 40 , 50 , 60} # Ref 'b' points to set
c = a . difference(b) # gives set with elements of set 'a' those are not in set 'b' and assigned to 'c'
print(c) # prints 'c' i.e., {10, 20}
print(type(c)) # prints type of 'c' i.e., <class 'set'>
d = a - b # gives set with elements of set 'a' those are not in set 'b' and assigned to 'd'
print(d) # prints 'd' i.e., {10, 20}
print(type(d)) # prints type of 'd' i.e., <class 'set'>
print(c  is  d) # False beccause 'c' and 'd' points to different sets
print(c  ==  d) # True because elements of 'c' and 'd' are same
















# symmetric_difference()   method  demo  program  (Home  work)
a = {10 , 20 , 30 , 40} # Ref 'a' points to set
b = {30 , 40 , 50 , 60} # Ref 'b' points to set
c = a . symmetric_difference(b) # gives set with all elements of sets 'a' and 'b' without common elements and assigned to 'c'
print(c) # prints 'c' i.e., {10, 20, 50, 60}
print(type(c)) # prints type of 'c' i.e., <class 'set'>
d = a ^ b # gives set with all elements of sets 'a' and 'b' without common elements and assigned to 'c'
print(d) # prints 'd' i.e., {10, 20, 50, 60}
print(type(d)) # prints type of 'd' i.e., <class 'set'>
print(c  is  d) # False beccause 'c' and 'd' points to different sets
print(c  ==   d) # True because elements of 'c' and 'd' are same
















# Find  outputs  (Home  work)
a = {x * x  for   x   in   range(10)}
print(a)
print(type(a))

'''
{0, 1, 4, 9, 16, 25, 36, 49, 64, 81} in any order
prints type of 'a' i.e., <class 'set'>
'''








'''
(Home  work)
Write  a  program  to  remove  duplicate  characters  of  the  string  using  set

1) Let  input  be   Rama  Rao
    What  is  the  output  ? --->  Ram<space>o

2) Both  input  and  output  are  strings

3) How  to  convert  string  to  set  ?  --->  set(string)
    How  to  convert  set  to  string ?  --->  '' . join(set)

4) What  is  the  result  of  str({'H' , 'y' , 'd'})  ? --->  "{'H' , 'y' , 'd'}"  but not 'Hyd'
Enter  input  string :  Rama Rao
String  without  duplicates : ao mR
'''
a = input("Enter any string:")
b = set(a)
print(b)
c = '' . join(b)
print(c)

'''
Outputs:

Enter any string:Rama Rao
{' ', 'a', 'o', 'R', 'm'}
 aoRm
'''













'''
Write  a  program  to  remove  duplicate  elements  of   list  using  set

1) Let  input  be  [False , 25 , 10.8 , 1  , 25 , 0 , 'Hyd' ,  10.8 , 1.0 , None , 'Sec' , 'Hyd' , True  ]
    What  is  the  output ?  ---> [False , 25 , 10.8 , 1 , 'Hyd' , None , 'Sec']

2) Both  input  and  output are lists
Enter  list  with  duplicates :  [False , 25 , 10.8 , 1  , 25 , 0 , 'Hyd' ,  10.8 , 1.0 , None , 'Sec' , 'Hyd' , True  ]
List  without  duplicates :   [False, 1, None, 'Sec', 10.8, 25, 'Hyd']
'''
a = eval(input("Enter list with duplicates :"))
b = set(a)
print(b)
c = list(b)
print(c)

'''
Outputs:

Enter list with duplicates :[False , 25 , 10.8 , 1  , 25 , 0 , 'Hyd' ,  10.8 , 1.0 , None , 'Sec' , 'Hyd' , True  ]
{False, 1, None, 'Hyd', 10.8, 'Sec', 25}
[False, 1, None, 'Hyd', 10.8, 'Sec', 25]
'''









'''
Write  a  program  to   obtain  common  elements  between  two  lists  using  sets

1) Let  1st  list  be  [10 , 20 , 30 , 40 , 50 , 60]  and  2nd  list  be  [30 , 40 , 70 , 80 , 20]
    What  is  the  output ?  --->  [20 , 30 , 40]

2) Both  input  and  output are lists
Enter  1st  list  :  [10,20,30,40,50,60]
Enter  2nd  list  :  [30,40,70,80,20]
Common  elements  between  the  2  lists : [40, 20, 30]
'''

a = eval(input("Enter 1st list:"))
b = eval(input("Enter 2nd list:"))
c = set(a)
d = set(b)
e = list(c.intersection(d))
print("Common elements between the 2 lists :", e)


'''
Outputs:

Enter 1st list:[10,20,30,40,50,60]
Enter 2nd list:[30,40,70,80,20]
Common elements between the 2 lists : [40, 20, 30]
'''











#  How  to  access  values  of  dictionary (Home  work)
a  =  {'Empno'  :  25 ,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  } # Ref 'a' points to dictionary of 3 key value pairs
print(a['Empno']) # How  to  print  value  25  in  dict  'a'
print(a['Ename']) # How  to  print  'Rama Rao'  in  dict  'a'
print(a['Sal']) # How  to  print  value  1000.65 in dict 'a'
      











# How  to  modify  values  of  dictionary  (Home  work)
a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a)
print(id(a))
a['Sal'] = 2000 # How to modify 1000.65 to 2000
a['Ename'] = 'Sita' # How to modify 'Rama Rao' to 'Sita'
a['Empno'] = 35 # How  to  modify  25   to  35
print(a)
print(id(a))
















#  How  to  append  key : value  pairs  to dictionary  (Home  work)
a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a) # {'Empno': 25, 'Ename': 'Rama  Rao', 'Sal': 1000.65}
a['Gender'] = ' M' # How  to  append  'Gender' : 'M'  to  dictionary  'a'
a['Married'] = True # How  to  append  'Married' :  True  to  dictionary  'a'
print(a) # {'Empno': 25, 'Ename': 'Rama  Rao', 'Sal': 1000.65, 'Gender': ' M', 'Married': True}
















# Find  outputs (Home  work)
a = { }
a[10] = 'Rama' # How to append 10 : 'Rama' to dictionary 'a'
a[20] = 'Sita' # How to append 20 : 'Sita'  to dictionary 'a'
a[15] = 'Rajesh' # How to append 15 : 'Rajesh'  to dictionary 'a'
a[18] = 'Kiran' # How to append 18 : 'Kiran'  to dictionary 'a'
print(a) #  {10: 'Rama', 20: 'Sita', 15: 'Rajesh', 18: 'Kiran'}











#  How  to  remove  key : value  pairs  of  dictionary  (Home  work)
a =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a)
a.pop('Sal') # How to remove 'Sal' : 1000.65 from dictionary 'a'
print(a)

'''
Outputs:

{'Empno': 25, 'Ename': 'Rama  Rao', 'Sal': 1000.65}
{'Empno': 25, 'Ename': 'Rama  Rao'}
'''












#  in  and  not  in  operators  (Home  work)
a =  {10 : 20 , 30 : 40 , 50 : 60 , 70 : 80} # Ref 'a' points to dictionary of key value pairs
print(30  in  a . keys()) # prints True
print(60  in  a . keys()) # prints False
print(60  in  a . values()) # prints True
print(30  in  a . values()) # prints False
print(50  in  a) # prints True
print(20  in  a) # prints False
print(70  not  in  a . keys()) # prints False
print(40  not  in  a . values()) # prints False
print(25 not in a) # prints True
      












#  What  are  the  outputs  if  input  is  {10: 'A', 20: 'B', 15: 'C' , 20 : 'D'}
a = input('Enter  dictionary  :  ') # reads string dictionary from keyboard or user
print(a) # prints sring dictionary 'a' i.e., '{10 : 'A', 20 : 'B', 15 : 'C', 20 : 'D}'
print(type(a)) # prints type of 'a' i.e., <class 'str'>
b = eval(a) # converts string dictionary to dictionary and assigned to ref 'b'
print(b) # prints 'b' i.e., {10 : 'A', 20 : 'D', 15 : 'C'}
print(type(b)) # prints type of 'b' i.e., <class 'dict'>












#  Find  outputs  (Home  work)
a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh' , 18 : 'Kiran'} # Ref 'a' points to dictionary of 4 key value pairs
b = {**a} # unpacks key value pairs of dictionary 'a' and assigned to ref 'b'
print(b) # prints 'b' i.e., {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh' , 18 : 'Kiran'}
print(a is b) # prints False because 'a' and 'b' points to different dictionaries
print(a == b) # prints True because key value pairs of 'a' and 'b' are same
c = a # Ref 'c' points to where ref 'b' points
print(a is c) # prints True because 'a' and 'b' points to same dictionary
print(a == c) # prints True because key value pairs of 'a' and 'b' are same
      














#Find  outputs  (Home  work)
a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh'} # Ref 'a' points to dictionary of 3 key value pairs
b = {18 : 'Kiran' , 14 : 'Amar' , 20  : 'Manohar'} # Ref 'b' points to dictionary of 3 key value pairs
c = {25 : 'Ramesh' , 19 : 'Krishna' , 15 : 'Radha' , 14 : 'Srinivas'} # Ref 'c' points to dictionary of 4 key value pairs
d = {*a , *b , *c} # unpacks key value pairs of dictionaries a, b and c to 'd'
print(d) # prints set of keys i.e., {10, 20, 15, 18, 14, 25, 19}
print(type(d)) # prints type of 'd' i.e., <class 'set'>
e = {**a , **b , **c} # unpacks key value pairs of dictionaries a, b and c to 'e'
print(e) # prints 'd' i.e., {10 : 'Rama', 20 : 'Manohar', 15 : 'Radha', 18 : 'Kiran', 14 : 'Srinivas', 25 : 'Ramesh', 19 : 'Krishna'}
print(type(e)) # prints type of 'd' i.e., <class 'dict'>














#  Find  outputs  (Home  work)
a = {10 : 20 , 30 : 40} # Ref 'a' points to dictionary of 2 key value pairs
b = {30 : 50 , 10 : 60} # Ref 'b' points to dictionary of 2 key value pairs
print(a + b) # Error because dictionaries cannot be concatenated with '+' operator
c = {**a , **b} # unpacks key value pairs of dictonary 'a' and 'b' and creates another dictionary
print(c) # prints 'c' i.e., {10 : 60, 30 : 50}
d = a|b # dictionaries 'a' and 'b' concatenated using pipe operator
print(d) # prints 'd' i.e., {10 : 60, 30 : 50}














'''
(Home  work)
Write  a  program  to  create  a  dictionary  with  emp  names  and  salaries

Hint:  Append  each  emp  name  and  salary  to  dictionary 'a'
How many Employees ? : 4
Enter Emp Name : AAA
Enter Salary : 100000
Enter Emp Name : BBB
Enter Salary : 200000
Enter Emp Name : CCC
Enter Salary : 150000
Enter Emp Name : DDD
Enter Salary : 175000
{'AAA': 100000.0, 'BBB': 200000.0, 'CCC': 150000.0, 'DDD': 175000.0}
'''

a = int(input("How many employees? :"))
d = {}
for i in range(a):
    b = input("Enter Emp Name :")
    c = eval(input("Enter Salary :"))
    d[b] = c
print(d)

'''
Outputs:      

How many employees? :4
Enter Emp Name :AAA
Enter Salary :100000
Enter Emp Name :BBB
Enter Salary :200000
Enter Emp Name :CCC
Enter Salary :150000
Enter Emp Name :DDD
Enter Salary :175000
{'AAA': 100000, 'BBB': 200000, 'CCC': 150000, 'DDD': 175000} 
'''













''' (Home  work)
Write  a  program  to  convert  a  string  to  dictionary

Let  input  be   "Emp no = 25 , Emp name = Rama  Rao , sal = 10000.0 , gender = m"

What  is  the  output ?  --->  {Emp no : 25 , Emp name  :  Rama Rao , sal : 10000.0 , gender : m}

Hint :  Use  split()  method twice
'''

a=input("Enter String  :").split(',')
d={}
for i in a:
    b,c=i.split('=')
    d[b]=eval('c')
print(d)

'''
Outputs:

Enter String  :Emp no = 25 , Emp name = Rama  Rao , sal = 10000.0 , gender = m
{'Emp no ': ' 25 ', ' Emp name ': ' Rama  Rao ', ' sal ': ' 10000.0 ', ' gender ': ' m'}
'''










# len()  function  demo  program  (Home  work)
a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }  # Ref 'a' points to dictionary of 3 key value pairs
print(len(a)) # prints number of key value pairs in dictionary 'a' i.e., 3
b = {}  # Ref 'a' points to empty dictionary 
print(len(b)) # prints number of elements in the dictionary 'b' i.e., 0
















#  sum()  function demo  program  (Home  work)
a = {10 : 20 , 30 : 40 , 50 : 60} # Ref 'a' points to dictionary of 3 key value pairs
print(sum(a . keys())) # prints sum of keys in dictionary 'a' i.e., 90
print(sum(a . values())) # prints sum of values in dictionary 'a' i.e., 120
print(sum(a)) # prints sum of keys in dictionary 'a' i.e., 90
print(sum(a.items())) # Error because keys and values in tuples cannoy be sum up
     












# max()  and  min()   functions  demo  program  (Home  work)
a = {10 : 20 , 30 : 25 , 40 : 5 , 7 : 28 , 9 : 50}  # Ref 'a' points to dictionary of 5 key value pairs
print(max(a . keys())) # prints largest of keys in dictionary 'a' i.e., 40
print(min(a . keys())) # prints smallest of keys in dictionary 'a' i.e., 7
print(max(a . values())) # prints largest of values in dictionary 'a' i.e., 50
print(min(a . values())) # prints smallest of values in dictionary ;a; i.e., 5
print(max(a . items())) # prints largest of items in dictionary (40, 5)
print(min(a . items())) # prints smallest of items in dictionary (7, 28)
print(max(a)) # prints largest of keys in dictionary 'a' i.e., 40
print(min(a)) # prints smallest of keys in dictionary 'a' i.e., 7















#  dict()  function  demo program (Home  work))
a = [ (10 , 'Hyd') , (20 , 'Sec') , (15 , 'Cyb') , (20 , 'Pune')] # Ref 'a' points to list of tuples
b = dict(a) # converts list of tuples 'a' to dictionary
print(b) # prints 'b' i.e., {10 : 'Hyd', 20 : 'Pune', 15 : 'Cyb']
c = ( ['R' , 'Red'] , ['G' , 'Green'] , ['B' , 'Blue'] , ['G' , 'Gray']) # Ref 'c' points to tuple of lists
d = dict(c) # converts tuple of lists 'b' to dictionary
print(d) # prints 'd' i.e., {'R' : 'Red', 'G' : 'Gray', 'B' : 'Blue'}
e = [[10 , 20 , 30] , [40 , 50 , 60] , [70 , 80 , 90]] # Ref 'e' points to nested  lists
print(dict(e)) # Error because 'e' is three dimensional but dictionary is only two dimensional
f = [[10] , [20] , [30]] # Ref 'f' points to nested  lists
print(dict(f)) # Error because 'f' is only one dimension but dictionary is two dimensional
print(dict([10 , 20])) # converts list to dictionary and prints dictionary i.e., {10 : 20}
g = [[10 , [20 , 30]] , [40 , [50 , 60]] , [70 , [80 , 90]]] # Ref 'g' points to nested  lists
print(dict(g)) # converts nested list to dictionary and prints {10 : [20, 30], 40 : [50, 60], 70 : [80 , 90]}
h = [[[10 , 20] , 30] , [[40 , 50] , 60] , [[70 , 80] , 90]] # Ref 'h' points to nested  lists
print(dict(h)) # Error because values can be one or more values but key should be only one
i = [[(10 , 20) , 30] , [(40 , 50) , 60] , [(70 , 80) , 90]] # Ref 'i' points to nested  lists
print(dict(i)) # Error because values can be one or more values but key should be only one

















# sorted()  function  (Home  work)
a = {10 : 'Red' , 20 : 'Green' , 15 : 'Blue' , 18 : 'Yellow' , 5 : 'White'} # Ref 'a' points to dictionary of 5 key value pairs
b = sorted(a . keys()) # keys of dictionary 'a' is sorted and assigned to ref 'b'
print(b) # prints 'b' i.e., [5, 10, 15, 18, 20]
c = sorted(a . values()) # values of dictionary 'a' is sorted and assigned to ref 'b'
print(c) # prints 'c' i.e., ['Blue', 'Green', 'Red', 'White', 'Yellow']
d = sorted(a . items()) # dictionary 'a' is sorted based on keys and assigned to ref 'd'
print(d) # prints 'd' i.e., [(5, 'White'), (10, 'Red'), (15, 'Blue'), (18, 'Yellow'), (20, 'Green')]
f  = sorted(a  , reverse = True) # keys of dictionary 'a' is sorted in descending order and assigned to ref 'f'
print(f) # prints 'f' i.e., [20, 18, 15, 10, 5]
print(a) # prints 'a' i.e., {10 : 'Red' , 20 : 'Green' , 15 : 'Blue' , 18 : 'Yellow' , 5 : 'White'}
















'''
Tricky  program
Write  a  program  to  sort  dictionary  wrt  keys  (Home  work)

1) Let  input  be   {10 : 'A' , 20 : 'B' , 15 : 'C' , 5 : 'D' , 12 : 'E'}
    What  is  the  output ?  ---> {5 : 'D' , 10 : 'A' ,  12 : 'E' ,  15 : 'C' , 20 : 'B'}

2) Both  input  and  output  are  dictionaries

3) Hint:  Use  sorted() function
Enter  dictionary  :  {10 : 'A' , 20 : 'B' , 15 : 'C' , 5 : 'D' , 12 : 'E'}
{5: 'D', 10: 'A', 12: 'E', 15: 'C',20: 'B'}
'''

a = eval(input("Enter any dictionary:"))
b = sorted(a.items())
c = dict(b)
print(c)

'''
Outputs:

Enter any dictionary:{10 : 'A' , 20 : 'B' , 15 : 'C' , 5 : 'D' , 12 : 'E'}
{5: 'D', 10: 'A', 12: 'E', 15: 'C', 20: 'B'}
'''














# clear()  method  demo  program (Home  work)
a = {10 : 20 , 30 : 40 , 50 : 60} # Ref a' points dictionary of 3 key value pairs
print(a) # prints 'a' i.e., {10 : 20 , 30 : 40 , 50 : 60}
a . clear() # deletes all key value pairs of dictionary 'a' and dictionary becomes empty
print(a) # prints 'a' i.e., {}
del  a # deletes 'a' 
print(a) # Error because 'a' is already deleted














# copy()  method demo  program  (Home  work)
a = {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue'} # Ref 'a' points to dictionary of 3 key value pairs
b = a . copy() # key value pairs of dictionary 'a' are copied to ref 'b'
print(b) # prints 'b' i.e., {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue'}
print(a  is  b) # prints False because 'a' and 'b' points to different dictionaries
print(a == b) # prints True because key value pairs of both 'a' and 'b' are same
      














#  keys()  method  demo  program
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'} # Ref 'a' points to dictionary of 4 key value pairs
b = a . keys() # keys of dictionary 'a' are assigned to 'b'
print(b) # prints 'b' i.e., dict_keys([10, 20, 15, 18])
print(type(b)) # prints type of 'b' i.e., <class 'dict_keys'>
for  x  in   b:
        print(x) # 10<nextline>20<nextline>15<nextline>18














# values()  method  demo  program
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'} # Ref 'a' points to dictionary of 4 key value pairs
b = a . values() # values of dictionary 'a' are assigned to 'b'
print(b) # prints 'b' i.e., dict_values(['Hyd', 'Sec', 'Cyb', 'Pune'])
print(type(b)) # prints type of 'b' i.e., <class 'dict_values'>
for  x   in   b:
	print(x) # Hyd<nextline>Sec<nextline>Cyb<nextline>Pune















#  items()  method  demo  program
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'} # Ref 'a' points to dictionary of 4 key value pairs
b = a . items() # keys and values of dictionary 'a' are assigned to 'b'
print(b) # prints 'b' i.e., [(10, 'Hyd'), (20, 'Sec'), (15, 'Cyb'), (18, 'Pune')]
print(type(b)) # prints type of 'b' i.e., <class 'dict_items'>
for  x   in   b:
        print(x) # (10, 'Hyd')<nextline>(20, 'Sec')<nextline>(15, 'Cyb')<nextline>(18, 'Pune')
for  x , y   in  b:
        print(x , y , sep = ' ... ') # 10...Hyd<nextline>20...Sec<nextline>15...Cyb<nextline>18...Pune



















# Find  outputs (Home  work)
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'} #  Ref 'a' points to dictionary of 4 key value pairs
for  x , y   in  a . items():
       print(x , y , sep = ' ... ') # 10...'Hyd'<nextline>20...'Sec'<nextline>15...'Cyb'<nextline>18...'Pune'
for  x , y   in  a . keys():
       print(x , y , sep = ' ... ') # Error because only keys are present but not values
for  x , y   in  a . values():
       print(x , y , sep = ' ... ') # Error because only values are present but not keys
for  x , y   in  a:
       print(x , y , sep = ' ... ') # Error because only keys are present but not values
             













#  Find  outputs  (Home  work)
a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh'} #  Ref 'a' points to dictionary of 3 key value pairs
x , y , z = a . keys() 
print(x) # prints 10
print(y) # prints 20
print(z) # prints 15
print() # prints nothing
x , y , z = a . values()
print(x) # prints 'Rama'
print(y) # prints 'Sita'
print(z) # prints 'Rajesh'
print() # prints nothing
x , y ,  z = a . items()
print(x) # prints (10, Rama')
print(y) # prints (20, 'Sita')
print(z) # prints (15, 'Rajesh')
print() # prints nothing
(rno1 , sname1) , (rno2 , sname2) , (rno3 , sname3) = a . items()
print(rno1 , sname1) # prints 10 Rama
print(rno2 , sname2) # prints 20 Sita
print(rno3 , sname3) # prints 15 Rajesh
      
'''
Outputs:

10
20
15

Rama
Sita
Rajesh

(10, 'Rama')
(20, 'Sita')
(15, 'Rajesh')

10 Rama
20 Sita
15 Rajesh
'''










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

11) Finally  what   is  dict  'a' ?  ---> {'R' : 2 , 'A' : 3 , 'M' : 1 , 'O' : 1}
Enter  mixed  case  string : RamA raO
{'A': 3, 'M': 1, 'O':  1,'R': 2}
'''

a = input("Enter any string:").upper()
b = sorted(a)
print(b)
c = {}
for i in range(1,len(b)):
    c[b[i]] = c.get(b[i] , 0) + 1
print(c)

'''
Outputs:

Enter any string:amA raO
[' ', 'A', 'A', 'A', 'M', 'O', 'R']
{'A': 3, 'M': 1, 'O': 1, 'R': 1}
'''