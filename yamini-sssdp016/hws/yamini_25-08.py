#  intersection()   method  demo  program (Home  work)
a = {10 , 20 , 30 , 40} # assign set  to a
b = {30 , 40 , 50 , 60} # assign set to b
c = a . intersection(b)  # new set with common elements 
print(c) # {40, 30}
print(type(c)) # classs set
d = a & b # returns common elements of 2 sets
print(d) # {40, 30}
print(type(d)) # class set
print(c  is  d) # false both are not pointing to same set
print(c  ==  d) # true as elements of both sets are same


'''
intersection()  method
---------------------------
1) What  does  a . intersection(b)  do ?  --->  Returns  a  set  with  common  elements  of  sets   'a'  and  'b'

2) Is  set . intersection(list)  valid  ?  --->
								Yes  becoz  argument  of  intersection()  method  can  be  any  sequence  but  not  necessarily  set

3) What  is  another  way  to  obtain  common  elements ?  --->  a & b

4) Is  set & list  valid ?  --->  No  becoz  operands  of  &  operator  should  be  sets  only

5) Is  list . intersection(set)  valid ?  --->  No  becoz  there  is  no  intersection()  method  in  list  class
'''

# difference()   method  demo  program  (Home  work)
a = {10 , 20 , 30 , 40} # set is assigned to a
b = {30 , 40 , 50 , 60} # set is assigned to b
c = a . difference(b) # returns new set with elements which are in a and not in b
print(c) # {10, 20}
print(type(c)) # class set
d = a - b 
print(d)#  {10, 20}
print(type(d))  # class set
print(c  is  d)# false as both are pointing to same set
print(c  ==  d) # true as elements are same


'''
difference()  method
------------------------
1) What  does  a . difference(b)  do ? --->  Returns  a  set  with  those  elements  of  set  'a'  which  are  not  in  'b'

2) Is  set . difference(list)  valid  ?  --->
							Yes  becoz  argument  of  difference()  method  can  be  any  sequence  but  not  necessarily  set

3) What  is  the  alternative  to  a . difference(b) ?  --->  a - b

4) Is  set - list  valid ?  --->  No  becoz  operands  of  -  operator  should  be  sets  only
'''


# symmetric_difference()   method  demo  program  (Home  work)
a = {10 , 20 , 30 , 40} # assigns set to a
b = {30 , 40 , 50 , 60} # assigns set to b
c = a . symmetric_difference(b) # returns a new set without common elements
print(c) #{10, 50, 20, 60}
print(type(c)) # class set
d = a ^ b  # returns a new set without common elements
print(d) #{10, 50, 20, 60}
print(type(d)) # class set
print(c   is   d) # false both are not pointing to same object
print(c  ==   d) # true as elements of sets are same


'''
symmetric_difference()  method
---------------------------------------
1) What  does  a . symmetric_difference(b)  do ? --->  Returns  a  set  with  all  the  elements  of  sets   'a'  and  'b'  but
						                                                              without  common  elements
																					  i.e.  Union  -  Intersection

2) Is  set . symmetric_difference(list)  valid  ?  --->  Yes  becoz  argument  can  be  any  sequence  but  not  necessarily  set

3) What  is  the  alternative  to  a . symmetric_difference(b) ?  --->  a ^ b

4) Is  set ^ list  valid ?  --->  No  becoz  operands  of  ^  operator  should  be  sets  only
'''

# Find  outputs  (Home  work)
a = {x * x  for   x   in   range(10)} #  prints the squares of o to 9 in any order as it is set
print(a) # {0, 1, 64, 4, 36, 9, 16, 49, 81, 25}
print(type(a)) # class set

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

s= input('enter a string: ')
p=set(s)
k=''.join(p)
print(k)

'''
Write  a  program  to  remove  duplicate  elements  of   list  using  set

1) Let  input  be  [False , 25 , 10.8 , 1  , 25 , 0 , 'Hyd' ,  10.8 , 1.0 , None , 'Sec' , 'Hyd' , True  ]
    What  is  the  output ?  ---> [False , 25 , 10.8 , 1 , 'Hyd' , None , 'Sec']

2) Both  input  and  output  are  lists
'''

s=eval(input())
p=list(set(s))
print(p)

'''
Write  a  program  to   obtain  common  elements  between  two  lists  using  sets

1) Let  1st  list  be  [10 , 20 , 30 , 40 , 50 , 60]  and  2nd  list  be  [30 , 40 , 70 , 80 , 20]
    What  is  the  output ?  --->  [20 , 30 , 40]

2) Both  input  and  output  are  lists
'''


a=eval(input())
b=eval(input())
c=set(a).intersection(set(b))
print(list(c))

#  How  to  access  values  of  dictionary (Home  work)
a  =  {'Empno'  :  25 ,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a[Empno])#How  to  print  value  25  in  dict  'a')
print(a[Ename])#How  to  print  'Rama Rao'  in  dict  'a')
print(a[sal])#How  to  print  value  1000.65   in  dict  'a')

#  How  to  append  key : value  pairs  to dictionary  (Home  work)
a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a) #{'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
a['Gender']='M' #How  to  append  'Gender' : 'M'  to  dictionary  'a'
a['Married']=True#How  to  append  'Married' :  True  to  dictionary  'a'
print(a)

# Find  outputs (Home  work)
a = { }
a[10]='Rama' # How  to  append  10 : 'Rama'  to  dictionary  'a'
a[20]='Sita' #How  to  append  20 : 'Sita'  to  dictionary  'a'
a[15]='Rajesh'#How  to  append  15 : 'Rajesh'  to  dictionary  'a'
a[18]='Kiran' #How  to  append  18 : 'Kiran'  to  dictionary  'a'
print(a)

#  How  to  remove  key : value  pairs  of  dictionary  (Home  work)
a =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a)
del a['Sal'] #How  to  remove  'Sal' : 1000.65  from  dictionary  'a'
print(a)

#  in  and  not  in  operators  (Home  work)
a =  {10 : 20 , 30 : 40 , 50 : 60 , 70 : 80}
print(30  in  a . keys()) # returs true as 30 key is there in dict a
print(60  in  a . keys()) # returs false as 60 key is not there in dict a
print(60  in  a . values()) # returs true as 60 value is there in dict a
print(30  in  a . values()) # returs false as 30 key is not there in dict a
print(50  in  a) #returs true as 50 key is there in dict a
print(20  in  a) # returs false as 20 key is there in dict a
print(70  not  in  a . keys()) # returs false as 70 key is there in dict a but not in method is used
print(40  not  in  a . values()) # returs false as 40 key is there in dict a but not in method is used
print(25  not  in  a)  # returs true as 25 key is not there in dict a but not in method is used

#  What  are  the  outputs  if  input  is  {10: 'A', 20: 'B', 15: 'C' , 20 : 'D'}
a = input('Enter  dictionary  :  ')
print(a) # '{10: 'A', 20: 'B', 15: 'C' , 20 : 'D'}'
print(type(a)) # class string
b = eval(a) # string dict is converted to dict
print(b) # {10: 'A', 20: 'B', 15: 'C' , 20 : 'D'}
print(type(b)) # class dict

#  Find  outputs  (Home  work)
a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh' , 18 : 'Kiran'}
b = {**a} # deep copy of dict is created
print(b) # {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh' , 18 : 'Kiran'}
print(a  is  b)  # false as both are pointing to different objects
print(a  ==  b) # true as both have same elements
c = a # c points to same object 
print(a  is   c) # true
print(a  ==  c) # true

#Find  outputs  (Home  work)
a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh'}
b = {18 : 'Kiran' , 14 : 'Amar' , 20  : 'Manohar'}
c = {25 : 'Ramesh' , 19 : 'Krishna' , 15 : 'Radha' , 14 : 'Srinivas'}
d = {*a , *b , *c} # dicts are unpacked to set of keys
print(d) # {10, 14, 15, 18, 19, 20, 25}
print(type(d)) # class set
e = {**a , **b , **c} # deep copy of 3 dicts 
print(e) # combination of 3 dicts after removing duplicates
print(type(e)) # class dict

#  Find  outputs  (Home  work)
a = {10 : 20 , 30 : 40} 
b = {30 : 50 , 10 : 60}
print(a + b) # error as sets are concatenated with + operator
c = {**a , **b}  # deep copy of lists a and b
print(c) # combination of a and b
d = a | b # concatenated a and b
print(d) # prints d

'''
(Home  work)
Write  a  program  to  create  a  dictionary  with  emp  names  and  salaries

Hint:  Append  each  emp  name  and  salary  to  dictionary  'a'
'''
n=int(input())
a={}
for i in range(n):
    k=(input())
    s = int(input())  # convert salary to integer
    a[k] = s
print(a)

''' (Home  work)
Write  a  program  to  convert  a  string  to  dictionary

Let  input  be   "Emp no = 25 , Emp name = Rama  Rao , sal = 10000.0 , gender = m"

What  is  the  output ?  --->  {Emp no : 25 , Emp name  :  Rama Rao , sal : 10000.0 , gender : m}

Hint :  Use  split()  method  twice
'''
n=input().split(',')
b={}
for i in n:
    a=i.split('=')
    b[a[0]]=a[1]
print(b)



# len()  function  demo  program  (Home  work)
a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(len(a)) # no of  key : value  pairs  in  the  dictionary i.e  3
b = {} # empty  dictionary
print(len(b)) # 0  as  there  are  no  key : value  pairs  in  the  dictionary


'''
What  does  len(dict)  do ?  --->  Returns  number  of  key : value  pairs  in  the  dictionary
'''

#  sum()  function demo  program  (Home  work)
a = {10 : 20 , 30 : 40 , 50 : 60}
print(sum(a . keys())) # sum of the keys i.e. 10+30+50=90
print(sum(a . values())) # sum of the values i.e. 20+40+60=120
print(sum(a)) # sum of the keys i.e. 10+30+50=90
print(sum(a . items())) # as a.items() is a list of tuples, it gives an error

# max()  and  min()   functions  demo  program  (Home  work)
a = {10 : 20 , 30 : 25 , 40 : 5 , 7 : 28 , 9 : 50}
print(max(a . keys())) # macimum  key i.e. 40
print(min(a . keys())) # minimum  key i.e. 7
print(max(a . values())) # maximum  value i.e. 50
print(min(a . values())) # minimum  value i.e. 5
print(max(a . items())) # maximum  (key , value)  pair i.e. (40 , 5)
print(min(a . items())) # minimum  (key , value)  pair i.e. (7 , 28)
print(max(a)) # maximum  key i.e. 40
print(min(a)) # minimum  key i.e. 7

#  dict()  function  demo program (Home  work))
a = [ (10 , 'Hyd') , (20 , 'Sec') , (15 , 'Cyb') , (20 , 'Pune')]
b = dict(a) #  Converts  list  of  tuples  to  dictionary
print(b) #  {10: 'Hyd', 20: 'Pune', 15: 'Cyb'}  (20  is  duplicate  key  so  last  value  is  considered)
c = ( ['R' , 'Red'] , ['G' , 'Green'] , ['B' , 'Blue'] , ['G' , 'Gray'])
d = dict(c) #  Converts  tuple  of  lists  to  dictionary
print(d) #  {'R': 'Red', 'G': 'Gray', 'B': 'Blue'}  (G  is  duplicate  key  so  last  value  is  considered)
e = [[10 , 20 , 30] , [40 , 50 , 60] , [70 , 80 , 90]]
print(dict(e)) #  Error  becoz  each  inner  sequence  should  have  exactly  two  elements
f = [[10] , [20] , [30]] #  Each  inner  sequence  has  only  one  element
print(dict(f)) #  Error  becoz  each  inner  sequence  should  have  exactly  two  elements
print(dict([10 , 20])) #  Error  becoz  argument  is  not  a  nested  sequence
g = [[10 , [20 , 30]] , [40 , [50 , 60]] , [70 , [80 , 90]]] # assigns nested sequence to g
print(dict(g)) #  {10: [20, 30], 40: [50, 60], 70: [80, 90]}  
h = [[[10 , 20] , 30] , [[40 , 50] , 60] , [[70 , 80] , 90]] # assigns nested sequence to h 
print(dict(h)) #  {[10, 20]: 30, [40, 50]: 60, [70, 80]: 90}  (list  should not be there as element  so  error)
i = [[(10 , 20) , 30] , [(40 , 50) , 60] , [(70 , 80) , 90]] # assigns nested sequence to i
print(dict(i)) #  {(10, 20): 30, (40, 50): 60, (70, 80): 90}  (tuple  can  be  there  as  element)



'''
dict()  function
------------------
1) What  is  the  argument  of  dict()  function ?  --->
											Nested  sequence  such  as  list  of  tuples , list  of  lists , tuple  of  tuples , tuple  of  lists,
											set  of  tuples  and  so  on

2) What  does  dict(nested-sequence)  do ?  --->  Converts  nested  sequence  to  dictionary

3) How  many  elements  can  be  in  each  inner  sequence ?  --->  Exactly  two  elements
    What  are  the  two  elements  of   each  inner  sequence ?  ---> key  and   value

4) Is  dict(sequence)  valid ?  --->  No  becoz  argument  is  not  a  nested  sequence
'''

# sorted()  function  (Home  work)
a = {10 : 'Red' , 20 : 'Green' , 15 : 'Blue' , 18 : 'Yellow' , 5 : 'White'}
b = sorted(a . keys()) # keys  in  sorted  order
print(b) # [print  the  sorted  keys] [5, 10, 15, 18, 20]
c = sorted(a . values()) # values  in  sorted  order
print(c) # [print  the  sorted  values] ['Blue', 'Green', 'Red', 'White', 'Yellow']
d = sorted(a . items()) # items  in  sorted  order
print(d) # [print  the  sorted  items] [(5, 'White'), (10, 'Red'), (15, 'Blue'), (18, 'Yellow'), (20, 'Green')]
f  = sorted(a  , reverse = True) # keys  in  reverse  sorted  order
print(f) # [print  the  reverse  sorted  keys] [20, 18, 15, 10, 5]
print(a) # [print  the  original  dictionary] {10: 'Red', 20: 'Green', 15: 'Blue', 18: 'Yellow', 5: 'White'}


'''
Tricky  program
Write  a  program  to  sort  dictionary  wrt  keys  (Home  work)

1) Let  input  be   {10 : 'A' , 20 : 'B' , 15 : 'C' , 5 : 'D' , 12 : 'E'}
    What  is  the  output ?  ---> {5 : 'D' , 10 : 'A' ,  12 : 'E' ,  15 : 'C' , 20 : 'B'}

2) Both  input  and  output  are  dictionaries

3) Hint:  Use  sorted()  function
'''
a=eval(input())
b=sorted(a)
c={}
for i in b:
    c[i]=a[i]
print(c)

# clear()  method  demo  program (Home  work)
a = {10 : 20 , 30 : 40 , 50 : 60}
print(a) # prints a with 3 key-value pairs
a . clear() # removes all key-value pairs
print(a) # prints empty dictionary
del  a # deletes the dictionary
print(a) # raises an error since a no longer exists

# copy()  method demo  program  (Home  work)
a = {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue'}
b = a . copy() # b is created as a copy of a
print(b) # prints  {'R': 'Red', 'G': 'Green', 'B': 'Blue'}
print(a  is  b) # prints  False as both are different objects
print(a  ==  b) # prints  True as both have same content

#  keys()  method  demo  program
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
b = a . keys() # list of  all  the  keys
print(b) # dict_keys  object
print(type(b)) # <class 'dict_keys'>
for  x  in   b:
        print(x) # prints the keys in the dict_keys object for each iteration 10<next line>20<next line>15<next line>18


'''
What  does  keys()  method  do  --->  Returns  dict_keys  object  which  has  list  of  all  the  dictionary  keys
'''

# values()  method  demo  program
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
b = a . values() # list of  all  the  values
print(b) # dict_values  object
print(type(b)) # <class 'dict_values'>
for  x   in   b:
	print(x) # prints the values in the dict_values object for each iteration Hyd<next line>Sec<next line>Cyb<next line>Pune


'''
What  does  values()  method  do  --->  Returns  dict_values  object  which  has  list  of  all  the  dictionary  values
'''

#  items()  method  demo  program
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
b = a . items() # list of  all  the  (key , value)  tuples
print(b) # dict_items  object
print(type(b)) # <class 'dict_items'>
for  x   in   b: 
        print(x) # prints the (key , value) tuples in the dict_items object for each iteration (10, 'Hyd')<next line>(20, 'Sec')<next line>(15, 'Cyb')<next line>(18, 'Pune')
for  x , y   in  b:
        print(x , y , sep = ' ... ') # prints the key and value in the dict_items object for each iteration 10 ... Hyd<next line>20 ... Sec<next line>15 ... Cyb<next line>18 ... Pune


'''
1) What  does  items()  method  do  --->  Returns  dict_items  object  which  has  list  of  tuples

2) What  are  the  two  elements  of  each  tuple ?  ---> (key , value)
'''


# Find  outputs (Home  work)
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
for  x , y   in  a . items(): # iterates  over  the  dict_items  object
       print(x , y , sep = ' ... ') # 10 ... Hyd<next line>20 ... Sec<next line>15 ... Cyb<next line>18 ... Pune
for  x ,y   in  a . keys(): # iterates  over  the  dict_keys  object
       print(x ,y, sep = ' ... ') # Error as dict_keys object is 1d so only one variable can be used in the for loop
for  x , y   in  a . values(): # iterates  over  the  dict_values  object
       print(x , y , sep = ' ... ')  # Error as dict_keys object is 1d so only one variable can be used in the for loop
for  x , y   in  a: # iterates  over  the  dictionary  object
       print(x , y , sep = ' ... ') # Error as default method used is keys it is 1d so only one variable can be used in the for loop

       #  Find  outputs  (Home  work)
a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh'}
x , y , z = a . keys() # unpacking  the  dict_keys  object
print(x) # 10
print(y) # 20
print(z) # 15
print() # empty  line
x , y , z = a . values() # unpacking  the  dict_values  object
print(x)  # Rama
print(y) # Sita
print(z) # Rajesh
print() # empty  line
x , y ,  z = a . items() # unpacking  the  dict_items  object
print(x) # (10, 'Rama')
print(y) # (20, 'Sita')
print(z) # (15, 'Rajesh')
print() # empty  line
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

s=input().upper()
l=sorted(s)
a={}
for i in l:
    if i.isalpha():
        a[i]=a.get(i,0)+1
print(a)


