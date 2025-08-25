#  intersection()   method 
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . intersection(b) # Returns  a  set  with  common  elements  of  sets   'a'  and  'b'
print(c) # {40, 30} in any order
print(type(c)) # <class 'set'>
d = a & b # returns a set with common elements of set 'a' and 'b'
print(d) # {40, 30} in any order
print(type(d)) # <class 'set'>
print(c  is  d) # False : both of them points to two different sets
print(c  ==  d) # True : because they contain same elements


# difference()   method  
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . difference(b) # returns a set with those elements of set 'a' which are not in 'b'
print(c) # {10,20}
print(type(c)) # <class 'set'>
d = a - b # returns a set with those elements of set 'a' which are not in 'b'
print(d) # {10,20}
print(type(d)) # <class 'set'>
print(c  is  d) # False :  c and d points to two diff sets
print(c  ==  d) # True : c and d has same elements


# symmetric_difference()   method  
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . symmetric_difference(b) # Returns a set with  all  the  elements  of  sets 'a' and 'b' but without  common  elements i.e.Union - Intersection
print(c) # {10,50,20,60} in any order
print(type(c)) # <class 'set'>
d = a ^ b 
print(d) # {10,50,20,60} in any order
print(type(d)) # <class 'set'>
print(c   is   d) # False
print(c  ==   d) # True


# Find  outputs  
a = {x * x  for   x   in   range(10)} # squares fron 0 to 9
print(a) # {0, 1, 64, 4, 36, 9, 16, 49, 81, 25} in any order
print(type(a)) # <class 'set'>


'''
Write  a  program  to  remove  duplicate  characters  of  the  string  using  set

1) Let  input  be   Rama  Rao
    What  is  the  output  ? --->  Ram<space>o

2) Both  input  and  output  are  strings

3) How  to  convert  string  to  set  ?  --->  set(string)
    How  to  convert  set  to  string ?  --->  '' . join(set)

4) What  is  the  result  of  str({'H' , 'y' , 'd'})  ? --->  "{'H' , 'y' , 'd'}"  but  not  'Hyd'
'''

x=input("Enter a string :")
y=set(x)
z=''.join(y)
print("string without duplicates: " ,z)
'''
Enter a string :Rama Rao
string without duplicates:  Ram o
'''


'''
Write  a  program  to  remove  duplicate  elements  of   list  using  set

1) Let  input  be  [False , 25 , 10.8 , 1  , 25 , 0 , 'Hyd' ,  10.8 , 1.0 , None , 'Sec' , 'Hyd' , True  ]
    What  is  the  output ?  ---> [False , 25 , 10.8 , 1 , 'Hyd' , None , 'Sec']

2) Both  input  and  output  are  lists
'''

x=eval(input("Enter list with duplicates: "))
y=set(x)
z=list(y)
print("List without duplicates: ",z)

'''
Enter list with duplicates: [False,25,10.8,1,25,0,'Hyd',10.8,1.0,None,'Sec','Hyd',True]
List without duplicates:  [False, 1, 'Sec', 10.8, None, 'Hyd', 25]'''



'''
Write  a  program  to   obtain  common  elements  between  two  lists  using  sets

1) Let  1st  list  be  [10 , 20 , 30 , 40 , 50 , 60]  and  2nd  list  be  [30 , 40 , 70 , 80 , 20]
    What  is  the  output ?  --->  [20 , 30 , 40]

2) Both  input  and  output  are  lists
'''

x=eval(input("Enter 1st list: "))
y=eval(input("Enter 2nd list: "))
a=set(x)
b=set(y)
c=a.intersection(b)
print(sorted(list(c)))


'''
Enter 1st list: [10,20,30,40,50,60]
Enter 2nd list: [30,40,70,80,20]
[20, 30, 40]
'''


#  access  values  of  dictionary 
a  =  {'Empno'  :  25 ,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a['Empno'])# print  value  25  in  dict  'a'
print(a['Ename'])#  print  'Rama Rao'  in  dict  'a'
print(a['sal'])# print  value  1000.65   in  dict  'a'



# modify  values  of  dictionary  
a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a) # {'Empno': 25, 'Ename': 'Rama  Rao', 'Sal': 1000.65}
print(id(a)) # address of 'a'
a['Sal']=2000# modify  1000.65  to  2000
a['Ename']='sita'# modify  'Rama  Rao'  to  'Sita'
a['Empno']=35# modify  25   to  35
print(a) # {'Empno': 35, 'Ename': 'sita', 'Sal': 2000}
print(id(a)) # same address as before


#  append  key : value  pairs  to dictionary  
a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a) # {'Empno': 25, 'Ename': 'Rama  Rao', 'Sal': 1000.65}
a['Gender']='M'# append  'Gender' : 'M'  to  dictionary  'a'
a['Married']='True'# append  'Married' :  True  to  dictionary  'a'
print(a) # {'Empno': 25, 'Ename': 'Rama  Rao', 'Sal': 1000.65, 'Gender': 'M', 'Married': 'True'}


# Find  outputs 
a = { }
a[10]='Rama'# append  10 : 'Rama'  to  dictionary  'a'
a[20]='Sita'# append  20 : 'Sita'  to  dictionary  'a'
a[15]='Rajesh'# append  15 : 'Rajesh'  to  dictionary  'a'
a[18]='Kiran'# append  18 : 'Kiran'  to  dictionary  'a'
print(a) # {10: 'Rama', 20: 'Sita', 15: 'Rajesh', 18: 'Kiran'}


# remove  key : value  pairs  of  dictionary 
a =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a) # {'Empno': 25, 'Ename': 'Rama  Rao', 'Sal': 1000.65}
a.pop('Sal')# remove  'Sal' : 1000.65  from  dictionary  'a'
print(a) # {'Empno': 25, 'Ename': 'Rama  Rao'}


#  in  and  not  in  operators  
a =  {10 : 20 , 30 : 40 , 50 : 60 , 70 : 80}
print(30  in  a . keys()) # True
print(60  in  a . keys()) # False
print(60  in  a . values()) # True
print(30  in  a . values()) # False
print(50  in  a)  # True
print(20  in  a) # False
print(70  not  in  a . keys()) # False
print(40  not  in  a . values()) # False
print(25  not  in  a) # True


#  What  are  the  outputs  if  input  is  {10: 'A', 20: 'B', 15: 'C' , 20 : 'D'}
a = input('Enter  dictionary  :  ')
print(a) # {10: 'A', 20: 'B', 15: 'C' , 20 : 'D'}
print(type(a)) # <class 'str'>
b = eval(a)
print(b) # {10: 'A', 20: 'D', 15: 'C'}
print(type(b)) # <class 'dict'>


#Find  outputs  
a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh'}
b = {18 : 'Kiran' , 14 : 'Amar' , 20  : 'Manohar'}
c = {25 : 'Ramesh' , 19 : 'Krishna' , 15 : 'Radha' , 14 : 'Srinivas'}
d = {*a , *b , *c} 
print(d) # {10, 14, 15, 18, 19, 20, 25}
print(type(d)) # <class 'set'>
e = {**a , **b , **c}
print(e) # {10: 'Rama', 20: 'Manohar', 15: 'Radha', 18: 'Kiran', 14: 'Srinivas', 25: 'Ramesh', 19: 'Krishna'}
print(type(e)) # <class 'dict'>


#  Find  outputs  
a = {10 : 20 , 30 : 40}
b = {30 : 50 , 10 : 60}
#print(a + b) # Error
c = {**a , **b}
print(c) # {10: 60, 30: 50}
d = a | b
print(d) # {10: 60, 30: 50}


'''
Write  a  program  to  create  a  dictionary  with  emp  names  and  salaries
Hint:  Append  each  emp  name  and  salary  to  dictionary  'a'
'''

x=eval(input("How many Employees? :"))
a={}
while x!=0:
    y=input("Enter Emp Name: ")
    z=float(input("Enter Salary :"))
    a[y]=z
    x-=1
print(a)

'''
How many Employees? :4
Enter Emp Name: AAA
Enter Salary :100000
Enter Emp Name: BBB
Enter Salary :200000
Enter Emp Name: CCC
Enter Salary :150000
Enter Emp Name: DDD
Enter Salary :175000 
{'AAA': 100000.0, 'BBB': 200000.0, 'CCC': 150000.0, 'DDD': 175000.0}'''


''' 
Write  a  program  to  convert  a  string  to  dictionary

Let  input  be   "Emp no = 25 , Emp name = Rama  Rao , sal = 10000.0 , gender = m"

What  is  the  output ?  --->  {Emp no : 25 , Emp name  :  Rama Rao , sal : 10000.0 , gender : m}

Hint :  Use  split()  method  twice
'''


x="Emp no = 25 , Emp name = Rama  Rao , sal = 10000.0 , gender = m"
d={}
for item in x.split(','):
    key,value=item.split('=')
    d[key.strip()]=value.strip()
print(d)

'''
{'Emp no': '25', 'Emp name': 'Rama  Rao', 'sal': '10000.0', 'gender': 'm'}
'''



# len()  function  
a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(len(a)) # 3 : Returns number of key: value pairs in the dictionary
b = {}
print(len(b)) # 0


#  sum()  function 
a = {10 : 20 , 30 : 40 , 50 : 60}
print(sum(a . keys())) # 90
print(sum(a . values())) # 120
print(sum(a)) # 90
#print(sum(a . items())) # Error


# max()  and  min()   functions  
a = {10 : 20 , 30 : 25 , 40 : 5 , 7 : 28 , 9 : 50}
print(max(a . keys())) # 40
print(min(a . keys())) # 7
print(max(a . values())) # 50
print(min(a . values())) # 5
print(max(a . items())) # (40,5)
print(min(a . items())) # (7,28)
print(max(a)) # 40
print(min(a)) # 7

#  dict()  function  
a = [ (10 , 'Hyd') , (20 , 'Sec') , (15 , 'Cyb') , (20 , 'Pune')]
b = dict(a)
print(b) # {10: 'Hyd', 20: 'Pune', 15: 'Cyb'}
c = ( ['R' , 'Red'] , ['G' , 'Green'] , ['B' , 'Blue'] , ['G' , 'Gray'])
d = dict(c)
print(d) # {'R': 'Red', 'G': 'Gray', 'B': 'Blue'}
e = [[10 , 20 , 30] , [40 , 50 , 60] , [70 , 80 , 90]]
#print(dict(e)) # inner sequence should have exactly 2 elements
f = [[10] , [20] , [30]]
#print(dict(f)) # inner sequence should have exactly 2 elements
#print(dict([10 , 20])) # error : int object is not iterable
g = [[10 , [20 , 30]] , [40 , [50 , 60]] , [70 , [80 , 90]]]
print(dict(g))  # {10: [20, 30], 40: [50, 60], 70: [80, 90]}
h = [[[10 , 20] , 30] , [[40 , 50] , 60] , [[70 , 80] , 90]]
#print(dict(h)) # error: The keys in a dictionary must be immutable but list is mutable
i = [[(10 , 20) , 30] , [(40 , 50) , 60] , [(70 , 80) , 90]]
print(dict(i)) # {(10, 20): 30, (40, 50): 60, (70, 80): 90}


# sorted()  function  
a = {10 : 'Red' , 20 : 'Green' , 15 : 'Blue' , 18 : 'Yellow' , 5 : 'White'}
b = sorted(a . keys())
print(b) # [5, 10, 15, 18, 20]
c = sorted(a . values())
print(c) # ['Blue', 'Green', 'Red', 'White', 'Yellow']
d = sorted(a . items())
print(d) # [(5, 'White'), (10, 'Red'), (15, 'Blue'), (18, 'Yellow'), (20, 'Green')]
f  = sorted(a  , reverse = True)
print(f) # [20, 18, 15, 10, 5]
print(a) # {10: 'Red', 20: 'Green', 15: 'Blue', 18: 'Yellow', 5: 'White'}


'''
Write  a  program  to  sort  dictionary  wrt  keys  

1) Let  input  be   {10 : 'A' , 20 : 'B' , 15 : 'C' , 5 : 'D' , 12 : 'E'}
    What  is  the  output ?  ---> {5 : 'D' , 10 : 'A' ,  12 : 'E' ,  15 : 'C' , 20 : 'B'}

2) Both  input  and  output  are  dictionaries

3) Hint:  Use  sorted()  function
'''

x=eval(input("Enter dictionary: "))
d={}
for i in sorted(x):
    d[i]=x[i]
print(d)

'''
Enter dictionary:  {10 : 'A' , 20 : 'B' , 15 : 'C' , 5 : 'D' , 12 : 'E'}
{5: 'D', 10: 'A', 12: 'E', 15: 'C', 20: 'B'}
'''

# clear()  method  
a = {10 : 20 , 30 : 40 , 50 : 60}
print(a) # {10: 20, 30: 40, 50: 60}
a . clear()
print(a) # {}
del  a # deletes 'a'
#print(a) # error : there is no obj 'a'
   

# copy()  method 
a = {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue'}
b = a . copy()
print(b) # {'R': 'Red', 'G': 'Green', 'B': 'Blue'}
print(a  is  b) # False
print(a  ==  b) # True


#  keys()  method 
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
b = a . keys() # Returns  dict_keys  object  which  has  list  of  all  the  dictionary  keys
print(b) # dict_keys([10, 20, 15, 18])
print(type(b)) # <class 'dict_Keys>
for  x  in   b:
        print(x)
'''
10
20
15
18
'''


# values()  method  
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
b = a . values() # Returns  dict_values object which has list of all the dictionary values
print(b) # dict_values(['Hyd', 'Sec', 'Cyb', 'Pune'])
print(type(b)) # <class 'dict_values'>
for  x   in   b:
	print(x)
'''
Hyd
Sec
Cyb
Pune
'''

#  items()  method  
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
b = a . items() # Returns  dict_items  object  which  has  list  of  tuples
print(b) # dict_items([(10, 'Hyd'), (20, 'Sec'), (15, 'Cyb'), (18, 'Pune')])
print(type(b)) #  <class 'dict_items'>
for  x   in   b:
        print(x)
'''
(10, 'Hyd')
(20, 'Sec')
(15, 'Cyb')
(18, 'Pune')'''
for  x , y   in  b:
        print(x , y , sep = ' ... ')
'''
10 ... Hyd
20 ... Sec
15 ... Cyb
18 ... Pune'''



# Find  outputs 
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
for  x , y   in  a . items():
       print(x , y , sep = ' ... ')
'''
10 ... Hyd
20 ... Sec
15 ... Cyb
18 ... Pune'''
#for  x , y   in  a . keys():
#       print(x , y , sep = ' ... ') # Error
#for  x , y   in  a . values():
#      print(x , y , sep = ' ... ') # Error
#for  x , y   in  a:
#       print(x , y , sep = ' ... ') # error

#  Find  outputs 
a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh'}
x , y , z = a . keys()
print(x) # 10
print(y) # 20
print(z) # 15
print()
x , y , z = a . values()
print(x) # Rama
print(y) # Sita
print(z) # Rajesh
print()
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
program  to  determine  frequency  of  each  alphabet  in  the  string   in   alphabetical  order
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

x=input("Enter mixed case string :").upper()
y=sorted(x) # [' ', 'A', 'A', 'A', 'M', 'O', 'R', 'R']
z={}
for i in y:
       if i.isalpha():
              z[i]=z.get(i,0)+1
print(z)

'''
Enter mixed case string :rama rao
{'A': 3, 'M': 1, 'O': 1, 'R': 2}'''