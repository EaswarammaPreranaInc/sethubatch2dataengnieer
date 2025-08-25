#  intersection()   method  demo  program (Home  work)
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . intersection(b)      # set of common elements of 'a' and 'b'
print(c)                     # {40,30}
print(type(c))               # <class 'set'> 
d = a & b                    # to obtain common elements
print(d)                     # <40,30}
print(type(d))               # <class 'set'>
print(c  is  d)              # False
print(c  ==  d)              # True



# difference()   method  demo  program  (Home  work)
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . difference(b)       # elements of set 'a' which are not in 'b'
print(c)                    # {10,20}
print(type(c))              # <class 'set'>
d = a - b                   # to obtain elements of set 'a' which are not in 'b
print(d)                    # {10,20}
print(type(d))              # <class 'set'>
print(c  is  d)             # False
print(c  ==  d)             # True



# symmetric_difference()   method  demo  program  (Home  work)
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . symmetric_difference(b)         # returns all the elements of set 'a' and 'b' without common elements
print(c)                                # {10,60,50,20}
print(type(c))                          # <class 'set'>
d = a ^ b                               # to obtain elements of set 'a' and 'b' without common elements
print(d)                                # {10,50,60,20}
print(type(d))                          # <class 'set'>
print(c   is   d)                       # False
print(c  ==   d)                        # True



# Find  outputs  (Home  work)
a = {x * x  for   x   in   range(10)}
print(a)
print(type(a))

#output
'''
{0, 1, 4, 9, 16, 25, 36, 49, 64, 72, 81}
<class 'set'>
'''

#  How  to  access  values  of  dictionary (Home  work)
a  =  {'Empno'  :  25 ,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a['Empno'])           #print(How  to  print  value  25  in  dict  'a')
print(a['Ename'])           #print(How  to  print  'Rama Rao'  in  dict  'a')
print(a['Sal'])             #print(How  to  print  value  1000.65   in  dict  'a')


# How  to  modify  values  of  dictionary  (Home  work)
a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a)                # {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(id(a))            # address of same dictionary
a['sal'] = 2000         #How  to  modify  1000.65  to  2000
a['Ename'] = 'Sita'     #How  to  modify  'Rama  Rao'  to  'Sita'
a['Empno'] = 35         #How  to  modify  25   to  35
print(a)                # {'Empno'  :  35,  'Ename'  :  'Sita'  ,  'Sal'  :  2000  }
print(id(a))            # address of same dictionary

#  How  to  append  key : value  pairs  to dictionary  (Home  work)
a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a)                 # {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
a['Gender'] = 'M'        # How  to  append  'Gender' : 'M'  to  dictionary  'a'
a['Married'] = True      # How  to  append  'Married' :  True  to  dictionary  'a'
print(a)                 # {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  , 'Gender' : 'M' , 'Married' : True}

# Find  outputs (Home  work)
a = { }
a[10] = 'Rama'          # How  to  append  10 : 'Rama'  to  dictionary  'a'
a[20] = 'Sita'          # How  to  append  20 : 'Sita'  to  dictionary  'a'
a[15] = 'Rajesh'        # How  to  append  15 : 'Rajesh'  to  dictionary  'a'
a[18] = 'Kiran'         # How  to  append  18 : 'Kiran'  to  dictionary  'a'
print(a)                # {10: 'Rama', 20: 'Sita', 15: 'Rajesh', 18: 'Kiran'}

#  How  to  remove  key : value  pairs  of  dictionary  (Home  work)
a =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a)                # {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
del a['Sal']            # How  to  remove  'Sal' : 1000.65  from  dictionary  'a'
print(a)                # {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  }

#  in  and  not  in  operators  (Home  work)
a =  {10 : 20 , 30 : 40 , 50 : 60 , 70 : 80}
print(30  in  a . keys())                       # True
print(60  in  a . keys())                       # False
print(60  in  a . values())                     # True
print(30  in  a . values())                     # False
print(50  in  a)                                # True
print(20  in  a)                                # False
print(70  not  in  a . keys())                  # False
print(40  not  in  a . values())                # False
print(25  not  in  a)                           # True


#  What  are  the  outputs  if  input  is  {10: 'A', 20: 'B', 15: 'C' , 20 : 'D'}
a = input('Enter  dictionary  :  ')
print(a)                # {10: 'A', 20: 'B', 15: 'C' , 20 : 'D'}
print(type(a))          # <class 'str'>
b = eval(a)             
print(b)                # {10: 'A', 20: 'D', 15: 'C' }
print(type(b))          # <class 'dict'>


#  Find  outputs  (Home  work)
a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh' , 18 : 'Kiran'}
b = {**a}               # shallow copy
print(b)                # {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh' , 18 : 'Kiran'}
print(a  is  b)         # False
print(a  ==  b)         # True
c = a                   # reference is copied
print(a  is   c)        # True
print(a  ==  c)         # False


#Find  outputs  (Home  work)
a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh'}
b = {18 : 'Kiran' , 14 : 'Amar' , 20  : 'Manohar'}
c = {25 : 'Ramesh' , 19 : 'Krishna' , 15 : 'Radha' , 14 : 'Srinivas'}
d = {*a , *b , *c}      # unpacks only keys
print(d)                # {10,19,25,14,15,18,}
print(type(d))          # <class 'dict'>
e = {**a , **b , **c}   # merges all the dictionaries
print(e)                # {10 : 'Rama' , 20 : 'Manohar' , 15 : 'Radha' , 18 : 'Kiran' , 14 : 'Srinivas' , 25 : 'Ramesh' , 19 : 'Krishna' }
print(type(e))          # <class 'dict'>


#  Find  outputs  (Home  work)
a = {10 : 20 , 30 : 40}
b = {30 : 50 , 10 : 60}
#print(a + b)           # unsupported + operand in dictionaries
c = {**a , **b}         # unpacking dictionaries
print(c)                # { 10:60 , 30:50}
d = a | b               # union operator combine two sets
print(d)                # {10:60,30:50}


# len()  function  demo  program  (Home  work)
a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(len(a))           # 3
b = {}
print(len(b))           # 0


#  sum()  function demo  program  (Home  work)
a = {10 : 20 , 30 : 40 , 50 : 60}
print(sum(a . keys()))          # 10+30+50=90
print(sum(a . values()))        # 20+40+60=120
print(sum(a))                   # 90
#print(sum(a . items()))        # error key value pairs cannot be summed directly


# max()  and  min()   functions  demo  program  (Home  work)
a = {10 : 20 , 30 : 25 , 40 : 5 , 7 : 28 , 9 : 50}
print(max(a . keys()))          # max key    40
print(min(a . keys()))          # min key     7
print(max(a . values()))        # max value  50
print(min(a . values()))        # min value   5
print(max(a . items()))         # max item   (40:5)
print(min(a . items()))         # min item   (7:28)
print(max(a))                   # max same as key 40
print(min(a))                   # min same as key 7



#  dict()  function  demo program (Home  work))
a = [ (10 , 'Hyd') , (20 , 'Sec') , (15 , 'Cyb') , (20 , 'Pune')]
b = dict(a)         # shallow copy
print(b)
c = ( ['R' , 'Red'] , ['G' , 'Green'] , ['B' , 'Blue'] , ['G' , 'Gray'])
d = dict(c)         # shallow copy
print(d)
e = [[10 , 20 , 30] , [40 , 50 , 60] , [70 , 80 , 90]]
#print(dict(e))          # error elements should have 2 elements
f = [[10] , [20] , [30]]
#print(dict(f))          # error elements should have 2 elements
#print(dict([10 , 20]))  # error
g = [[10 , [20 , 30]] , [40 , [50 , 60]] , [70 , [80 , 90]]]
print(dict(g))
h = [[[10 , 20] , 30] , [[40 , 50] , 60] , [[70 , 80] , 90]]
#print(dict(h))         # error 
i = [[(10 , 20) , 30] , [(40 , 50) , 60] , [(70 , 80) , 90]]
print(dict(i))


#output
'''
{10: 'Hyd', 20: 'Pune', 15: 'Cyb'}
{'R': 'Red', 'G': 'Gray', 'B': 'Blue'}
{10: [20, 30], 40: [50, 60], 70: [80, 90]}
{(10, 20): 30, (40, 50): 60, (70, 80): 90}
'''

# sorted()  function  (Home  work)
a = {10 : 'Red' , 20 : 'Green' , 15 : 'Blue' , 18 : 'Yellow' , 5 : 'White'}
b = sorted(a . keys())              
print(b)                    # [5,10,15,18,20]
c = sorted(a . values())
print(c)                    # ['Blue','Green','Red','White','Yellow']
d = sorted(a . items())
print(d)                    # [(5,'White'),(10,'Red'),(15,'Blue'),(18,'Yellow'),(20,'Green')]
f  = sorted(a  , reverse = True)
print(f)                    # [20,18,15,10,5]
print(a)                    # {10 : 'Red' , 20 : 'Green' , 15 : 'Blue' , 18 : 'Yellow' , 5 : 'White'}


# clear()  method  demo  program (Home  work)
a = {10 : 20 , 30 : 40 , 50 : 60}
print(a)            # {10 : 20 , 30 : 40 , 50 : 60}
a . clear()         # clears all the key-value pairs
print(a)            # {}
del  a              # deletes 'a'
#print(a)            # error


# copy()  method demo  program  (Home  work)
a = {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue'}
b = a . copy()        # shallow copy
print(b)              # {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue'}
print(a  is  b)       # False
print(a  ==  b)       # True


#  keys()  method  demo  program
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
b = a . keys()          # retrievs all the keys
print(b)                # [10,20,15,18]
print(type(b))          # <class 'dict_keys'>
for  x  in   b:
        print(x)


#output
'''
[10,20,15,18]
<class 'dict_keys'>
10
20
15
18
'''

# values()  method  demo  program
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
b = a . values()            # retrievs all the dict values
print(b)                    # ['Hyd','Sec','Cyb','Pune']
print(type(b))              # <class 'dict_values'>
for  x   in   b:
	print(x)


#output
'''
['Hyd','Sec','Cyb','Pune']
<class 'dict_values'>
Hyd
Sec
Cyb
Pune
'''

#  items()  method  demo  program
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
b = a . items()         # retrievs all the dict items
print(b)                # [(10,'Hyd'),(20,'Sec'),(15,'Cyb'),(18,'Pune')]
print(type(b))          # <class 'dict_items'>
for  x   in   b:
        print(x)
for  x , y   in  b:
        print(x , y , sep = ' ... ')


'''
[(10,'Hyd'),(20,'Sec'),(15,'Cyb'),(18,'Pune')]
<class 'dict_items'>
(10,'Hyd')
(20,'Sec')
(15,'Cyb')
(18,'Pune')
10...Hyd
20...Sec
15...Cyb
18...Pune
'''


# Find  outputs (Home  work)
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
for  x , y   in  a . items():
       print(x , y , sep = ' ... ')
'''for  x , y   in  a . keys():
       print(x , y , sep = ' ... ')          # error 
for  x , y   in  a . values():
       print(x , y , sep = ' ... ')          # error
for  x , y   in  a:
       print(x , y , sep = ' ... ')          # error
'''

#output
'''
10...Hyd
20...Sec
15...Cyb
18...Pune
'''

#  Find  outputs  (Home  work)
a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh'}
x , y , z = a . keys()
print(x)                    # 10
print(y)                    # 20
print(z)                    # 15
print()
x , y , z = a . values()
print(x)                    # Rama
print(y)                    # Sita
print(z)                    # Rajesh
print()
x , y ,  z = a . items()
print(x)                    # (10,'Rama')
print(y)                    # (20,'Sita')
print(z)                    # (15,'Rajesh')
print()
(rno1 , sname1) , (rno2 , sname2) , (rno3 , sname3) = a . items()
print(rno1 , sname1)        # 10 Rama
print(rno2 , sname2)        # 20 Sita
print(rno3 , sname3)        # 15 Rajesh


'''
(Home  work)
Write  a  program  to  remove  duplicate  characters  of  the  string  using  set

1) Let  input  be   Rama  Rao
    What  is  the  output  ? --->  Ram<space>o

2) Both  input  and  output  are  strings

3) How  to  convert  string  to  set  ?  --->  set(string)
    How  to  convert  set  to  string ?  --->  '' . join(set)

4) What  is  the  result  of  str({'H' , 'y' , 'd'})  ? --->  "{'H' , 'y' , 'd'}"  but  not  'Hyd'
'''


string=input('Enter a string:')
new_string=''.join(set(string))
print("string after removal:",new_string)

'''
Write  a  program  to  remove  duplicate  elements  of   list  using  set

1) Let  input  be  [False , 25 , 10.8 , 1  , 25 , 0 , 'Hyd' ,  10.8 , 1.0 , None , 'Sec' , 'Hyd' , True  ]
    What  is  the  output ?  ---> [False , 25 , 10.8 , 1 , 'Hyd' , None , 'Sec']

2) Both  input  and  output  are  lists
'''

l = eval(input('Enter any list:  '))
print(list(set(l)))


'''
Write  a  program  to   obtain  common  elements  between  two  lists  using  sets

1) Let  1st  list  be  [10 , 20 , 30 , 40 , 50 , 60]  and  2nd  list  be  [30 , 40 , 70 , 80 , 20]
    What  is  the  output ?  --->  [20 , 30 , 40]

2) Both  input  and  output  are  lists
'''

list1 = eval(input('Enter 1st list:  '))
list2 = eval(input('Enter 2nd list:  '))
print(f'Common elements between the 2 lists: {list(set(list1) & set(list2))}')


'''
(Home  work)
Write  a  program  to  create  a  dictionary  with  emp  names  and  salaries

Hint:  Append  each  emp  name  and  salary  to  dictionary  'a'
'''

a = {}
n = int(input("How many Employees ? : "))
for i in range(n):
    name = input("Enter Emp Name : ")
    salary = float(input("Enter Salary : "))
    a[name] = salary
print(a)


''' (Home  work)
Write  a  program  to  convert  a  string  to  dictionary

Let  input  be   "Emp no = 25 , Emp name = Rama  Rao , sal = 10000.0 , gender = m"

What  is  the  output ?  --->  {Emp no : 25 , Emp name  :  Rama Rao , sal : 10000.0 , gender : m}

Hint :  Use  split()  method  twice
'''

string = input('Enter the string with = and comma  :  ')
a = {}
for s in string.split(','):
    t = s.split('=')
    a[t[0]] = t[1]
print(a)


'''
Tricky  program
Write  a  program  to  sort  dictionary  wrt  keys  (Home  work)

1) Let  input  be   {10 : 'A' , 20 : 'B' , 15 : 'C' , 5 : 'D' , 12 : 'E'}
    What  is  the  output ?  ---> {5 : 'D' , 10 : 'A' ,  12 : 'E' ,  15 : 'C' , 20 : 'B'}

2) Both  input  and  output  are  dictionaries

3) Hint:  Use  sorted()  function
'''


a = eval(input('Enter dictionary:  '))
sorted_dict = {k: a[k] for k in sorted(a)}
print(sorted_dict)



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

string = input('Enter any string:  ')
string = sorted(string.upper())
counted = {}
for c in string: 
    if 65 <= ord(c) <= 90:
        counted[c] = counted.get(c, 0) + 1
print(counted)