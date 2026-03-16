# intersection()   method  demo  program (Home  work)
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . intersection(b) #Here a new set is created and it consists of common elements which are in both a and b sets
print(c) #It returns the set of elements which are common in both a and b i.e {40, 30} in any order
print(type(c)) #<class 'set'>
d = a & b #We can use '&' also for intersection but it only works for sets not set and another sequence
print(d) #Returns the set of common elements in both a and b sets i.e {40, 30} in any order
print(type(d)) #<class 'set'>
print(c  is  d) #Returns False #Here references are compared both c and d points to two sets
print(c  ==  d) #Returns True #here elements are compared 


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
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . difference(b) #Returns  a  set  with  those  elements  of  set  'a'  which  are  not  in  'b' 
print(c) #Returns a set with i.e {10 , 20} in any order
print(type(c)) #<class 'set'>
d = a - b #Alternate for difference method we can use '-' but it only works for two sets not set and another sequence
print(d) #Returns the set with 10 and 20 i.e {10, 20} in any order
print(type(d)) #<class 'set'>
print(c  is  d) #Returns False
print(c  ==  d) #Returns True


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
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . symmetric_difference(b) #Here it creates a set of elements of both set sets without common elements
print(c) #Returns the set c i.e {10, 20, 50, 60} in any order
print(type(c)) #<class 'set'>
d = a ^ b #Atlernate "^" is used for symmetric_difference and only works for sets not set and another sequence
print(d) #Returns the elements of set a and b without common elements i.e {10, 20, 50, 60} in any order
print(type(d)) #<class 'set'>
print(c   is   d) #False 
print(c  ==   d) #True


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
a = {x * x  for   x   in   range(10)} #Here set comprehension is used we are iterating the loop from 0 to 9 by multiplying the each element with itself i.e x*x
print(a) #Returns the set of elements i.e{0, 1, 4, 9, 16, 25 ,36, 49, 64, 81} in any order
print(type(a)) #<class 'set'>



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
'''
Enter  input  string :  Rama Rao
String  without  duplicates  :   ao mR
'''
n = input("Enter the input string: ")
b = set(n)
c = ''.join(b)
print(c)

'''output
Enter the input string: Rama Rao
 Ramo
'''




'''
Write  a  program  to  remove  duplicate  elements  of   list  using  set

1) Let  input  be  [False , 25 , 10.8 , 1  , 25 , 0 , 'Hyd' ,  10.8 , 1.0 , None , 'Sec' , 'Hyd' , True  ]
    What  is  the  output ?  ---> [False , 25 , 10.8 , 1 , 'Hyd' , None , 'Sec']

2) Both  input  and  output  are  lists
'''
'''Enter  list  with  duplicates :  [False , 25 , 10.8 , 1  , 25 , 0 , 'Hyd' ,  10.8 , 1.0 , None , 'Sec' , 'Hyd' , True  ]
List  without  duplicates :   [False, 1, None, 'Sec', 10.8, 25, 'Hyd']
'''

n = eval(input("Enter list with duplicates: "))
b = set(n)
c = list(b)
print(f"List without duplicate elements {c}")

'''
output:
Enter list with duplicates: [False , 25 , 10.8 , 1  , 25 , 0 , 'Hyd' ,  10.8 , 1.0 , None , 'Sec' , 'Hyd' , True  ]
List without duplicate elements [False, 1, None, 10.8, 'Hyd', 'Sec', 25]
'''


'''
Write  a  program  to   obtain  common  elements  between  two  lists  using  sets

1) Let  1st  list  be  [10 , 20 , 30 , 40 , 50 , 60]  and  2nd  list  be  [30 , 40 , 70 , 80 , 20]
    What  is  the  output ?  --->  [20 , 30 , 40]

2) Both  input  and  output  are  lists
'''
list1 = eval(input("Enter list 1 :")) 
list2 = eval(input("Enter list 2 :"))
b = set(list1)
c = b.intersection(list2)
d = list(c)
print(f"Common  elements  between  the  2  lists :{d}")

'''output:
Enter list 1 :[10 , 20 , 30 , 40 , 50 , 60]
Enter list 2 :[30 , 40 , 70 , 80 , 20]
Common  elements  between  the  2  lists :   [40, 20, 30]
'''




#  How  to  access  values  of  dictionary (Home  work)
a  =  {'Empno'  :  25 ,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a['Empno'])  #(How  to  print  value  25  in  dict  'a')
print(a['Ename'])  #(How  to  print  'Rama Rao'  in  dict  'a')
print(a['Sal'])    #(How  to  print  value  1000.65   in  dict  'a')




# How  to  modify  values  of  dictionary  (Home  work)
a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a) #Returns the key-value pairs in dict a 
print(id(a)) #Returns the address of dict a i.e {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
a['Sal'] = 2000         #How  to  modify  1000.65  to  2000
a['Ename'] = 'Sita'     #How  to  modify  'Rama  Rao'  to  'Sita'
a['Empno'] = 35         #How  to  modify  25   to  35 
print(a) #Returns the modified dict i.e {'Empno': 35, 'Ename': 'Sita', 'Sal': 2000}
print(id(a)) #Returns the same address as we made modifications in same dict




#How  to  append  key : value  pairs  to dictionary  (Home  work)
a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a) #Returns the key-value pairs of dict a i.e {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
a['Gender'] = 'M'    #How  to  append  'Gender' : 'M'  to  dictionary  'a'
a['Married'] = True  #How  to  append  'Married' :  True  to  dictionary  'a'
print(a) #Returns the dict with appended key-value pairs i.e {'Empno': 25, 'Ename': 'Rama  Rao', 'Sal': 1000.65, 'Gender': 'M', 'Married': True}




# Find  outputs (Home  work)
a = { } #Reference a points to an empty dict
a[10] = 'Rama'        #How  to  append  10 : 'Rama'  to  dictionary  'a'
a[20] = 'Sita'        #How  to  append  20 : 'Sita'  to  dictionary  'a'
a[15] = 'Rajesh'      #How  to  append  15 : 'Rajesh'  to  dictionary  'a'
a[18] = 'Kiran'       #How  to  append  18 : 'Kiran'  to  dictionary  'a'
print(a) #Returns the dict a with appended key-value pairs i.e {10: 'Rama', 20: 'Sita', 15: 'Rajesh', 18: 'Kiran'}




#How  to  remove  key : value  pairs  of  dictionary  (Home  work)
a =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65}
print(a) #Returns the key-value pairs of dict a i.e {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65}
del a['Sal']    #How  to  remove  'Sal' : 1000.65  from  dictionary  'a'
print(a) #Returns the dict with 2 key-value pairs i.e {'Empno'  :  25,  'Ename'  :  'Rama  Rao'}




#  in  and  not  in  operators  (Home  work)
a =  {10 : 20 , 30 : 40 , 50 : 60 , 70 : 80}
print(30  in  a . keys()) #Returns True if the key 30 is existed in the dict a #i.e True
print(60  in  a . keys()) #Returns True if the key 60 is existed in the dict a orelse False #i.e False
print(60  in  a . values()) #Returns True if the value 60 is existed in the dict a i.e True
print(30  in  a . values()) #Returns True if the Value 30 is existed in the dict a or else False #i.e False
print(50  in  a) #By default it checks the key so here if key 50 is existed then returns true else False i.e #True
print(20  in  a) #By default it checks the key so here if key 20 is existed then returns true else False i.e #False
print(70  not  in  a . keys()) #Returns False #Here we are checking 70 not in a.keys() but it is their so it returns False
print(40  not  in  a . values()) #Returns False #Here we are checking 40 not in a.values() but it is their so it returns False
print(25  not  in  a) #Returns True #key 25 is not their in dict a



#  What  are  the  outputs  if  input  is  {10: 'A', 20: 'B', 15: 'C' , 20 : 'D'}
a = input('Enter  dictionary  :  ') #  {10: 'A', 20: 'B', 15: 'C' , 20 : 'D'} takes input as str dict obj
print(a) #Returns the str dict i.e {10: 'A', 20: 'B', 15: 'C' , 20 : 'D'} 
print(type(a)) #<class 'str'>
b = eval(a) #Here str dict obj is converted to dict 
print(b) #Returns the dict i.e {10: 'A', 20: 'B', 15: 'C' , 20 : 'D'}
print(type(b)) #Returns the Type i.e <class 'dict'>




#  Find  outputs  (Home  work)
a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh' , 18 : 'Kiran'}
b = {**a} #Reference b points to copy of dict obj
print(type(b))
print(b) #Returns the dict obj i.e {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh' , 18 : 'Kiran'}
print(a  is  b) #Returns False #as a and b points to two different dicts with same key-value pairs
print(a  ==  b) #Returns the True #as a and b are having same key-value pairs
c = a #Reference c points to same dict obj where a points to 
print(a  is   c) #Returns True #as a and c are pointing to the same dict obj
print(a  ==  c) #Returns True #as the key-value pairs of both a and c are same



#Find  outputs  (Home  work)
a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh'}
b = {18 : 'Kiran' , 14 : 'Amar' , 20  : 'Manohar'}
c = {25 : 'Ramesh' , 19 : 'Krishna' , 15 : 'Radha' , 14 : 'Srinivas'}
d = {*a , *b , *c} #Here a,b,c dict keys unpacked into a new set b i.e {10, 14, 15, 18, 19, 20, 25} 
print(d) #Returns the unpacked keys without duplicates i.e {10, 14, 15, 18, 19, 20, 25}
print(type(d)) #Returns the type i.e <class 'set'>
e = {**a , **b , **c} #Here concatinate all the a, b, c dict obj into c and if any duplicate keys are their the values of those keys are replaced with last one and it is a set obj not dict obj
print(e) #Returns the concatinated dict i.e {10: 'Rama', 20: 'Manohar', 15: 'Radha', 18: 'Kiran', 14: 'Srinivas', 25: 'Ramesh', 19: 'Krishna'}
print(type(e)) #Returns type i.e <class 'set'>




#  Find  outputs  (Home  work)
a = {10 : 20 , 30 : 40} 
b = {30 : 50 , 10 : 60}
print(a + b) #Error #We cannot use '+' operator to concatinate two dict
c = {**a , **b} #Here a and b are concatinated into set c and duplicates will be replaced with last one
print(c) #Returns the set c i.e {10: 60, 30: 50}
d = a | b #Here we are using pipe('|') operator to concatinate two dicts into a new dict d
print(d) #Returns the dict with concatinated key-value pairs i.e {10: 60, 30: 50}




'''
(Home  work)
Write  a  program  to  create  a  dictionary  with  emp  names  and  salaries

Hint:  Append  each  emp  name  and  salary  to  dictionary  'a'
'''


'''
How many Employees ? : 4
Enter Emp Name : AAA
Enter Salary : 100000
Enter Emp Name : BBB
Enter Salary : 200000
Enter Emp Name : CCC
Enter Salary : 150000
Enter Emp Name : DDD
Enter Salary : 175000
{'AAA': 100000.0, 'BBB': 200000.0, 'CCC': 150000.0, 'DDD': 175000.0}
'''

n = eval(input("How many Employees ? : "))
d = {}
while n > 0:
    name = input("Enter Emp Name: ")
    salary = float(input("Enter Emp Salary: "))
    d[name] = salary
    n -= 1
print(d)

'''output:
How many Employees ? : 4
Enter Emp Name: goutham
Enter Emp Salary: 400000
Enter Emp Name: chotu
Enter Emp Salary: 200000
Enter Emp Name: sai
Enter Emp Salary: 600000
Enter Emp Name: santhosh 
Enter Emp Salary: 1000000
{'goutham': 400000.0, 'chotu': 200000.0, 'sai': 600000.0, 'santhosh': 1000000.0}
'''



'''Write  a  program  to  convert  a  string  to  dictionary
Let  input  be   "Emp no = 25 , Emp name = Rama  Rao , sal = 10000.0 , gender = m"
What  is  the  output ?  --->  {Emp no : 25 , Emp name  :  Rama Rao , sal : 10000.0 , gender : m}
Hint :  Use  split()  method  twice
'''

n = input("Enter a String: ")
b = n.split(',')
d = {}
for i in b:
    key,value = i.split('=')
    d[key] = value
print(d)

'''
# Output:
Enter Emp details: Emp no = 25 , Emp name = Rama  Rao , sal = 10000.0 , gender = m
{'Emp no ': ' 25 ', ' Emp name ': ' Rama  Rao ', ' sal ': ' 10000.0 ', ' gender ': ' m'}
'''


# len()  function  demo  program  (Home  work)
a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(len(a)) #Returns the length of a i.e 3
b = {} #Reference b points to an empty dict
print(len(b)) #Returns the length as 0 as there are no elements in the dict b


'''
What  does  len(dict)  do ?  --->  Returns  number  of  key : value  pairs  in  the  dictionary
'''




#  sum()  function demo  program  (Home  work)
a = {10 : 20 , 30 : 40 , 50 : 60}
print(sum(a . keys())) #Returns the sum of all keys in the dict a i.e 90
print(sum(a . values())) #Returns the sum of all values in the dict a i.e 120
print(sum(a)) #Returns the sum of all keys in the dict a #By default keys() is executed i.e 90
print(sum(a . items())) #Error #Because in item() there is list inside list there are tuples so sum is not possible



# max()  and  min()   functions  demo  program  (Home  work)
a = {10 : 20 , 30 : 25 , 40 : 5 , 7 : 28 , 9 : 50}
print(max(a . keys())) #Returns the max key in the dict a i.e 40
print(min(a . keys())) #Returns the min key in the dict a i.e 7
print(max(a . values())) #Returns the max value in the dict a i.e 50
print(min(a . values())) #Returns the min value in the dict a i.e 5
print(max(a . items())) #Returns the max key-value pair #compares the keys in the dict a and returns the tuple i.e (40 ,5)
print(min(a . items())) #Returns the min key-value pair #compares the keys in the dict a and returns the tuple i.e (7 ,28)
print(max(a)) #By default keys() are comapared i.e 40
print(min(a)) #By default keys() are compared i.e 7



#  dict()  function  demo program (Home  work))
a = [ (10 , 'Hyd') , (20 , 'Sec') , (15 , 'Cyb') , (20 , 'Pune')] #Reference a points to the list of tuples 
b = dict(a) #Here list is converted to dict and tuple of elements are converted to key-value pairs 
print(b) #Returns the dict with key-value pairs and repeated will be allowed if one appears again then it is overide it with present one i.e {10: 'Hyd', 20: 'Pune', 15: 'Cyb'}
c = ( ['R' , 'Red'] , ['G' , 'Green'] , ['B' , 'Blue'] , ['G' , 'Gray']) #Reference c points to tuple and inside tuple there are lists 
d = dict(c) #Here tuple of lists are converted to dict and each list in tuple is converted to key-value pairs and duplicates are not allowed they are replaced with new occurance
print(d) #Returns the converted dict i.e {'R : 'Red','G' : 'Gray', 'B' : 'Blue',}
e = [[10 , 20 , 30] , [40 , 50 , 60] , [70 , 80 , 90]] #Reference e points to nested list
print(dict(e)) #Error #Because there are 3 elements in each inner list but dict takes onlu two one is key and another is value
f = [[10] , [20] , [30]] #Reference f points to nested list 
print(dict(f)) #Error #Because each inner list is having only one element but dict() takes two
print(dict([10 , 20])) #Error here sequence should be a nested sequence
g = [[10 , [20 , 30]] , [40 , [50 , 60]] , [70 , [80 , 90]]]
print(dict(g)) #Here nested list is converted to dict with in inner list is key and inner(inner list) will be list of values i.e {10: [20, 30], 40: [50, 60], 70: [80, 90]}
h = [[[10 , 20] , 30] , [[40 , 50] , 60] , [[70 , 80] , 90]]
print(dict(h)) #Here Error #List cannot be converted to dict as here list of elements not tuple of elements
i = [[(10 , 20) , 30] , [(40 , 50) , 60] , [(70 , 80) , 90]]
print(dict(i)) #Here nested list is converted to dict as inner tuple is converted to key and element in inner list in value i.e {(10, 20): 30, (40, 50): 60, (70, 80): 90}



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
b = sorted(a . keys()) #Here all keys in the dict a is sorted in ascending order and returns list i.e [5, 10,15, 18,20]
print(b) #Returns the sorted list i.e [5, 10, 15, 18, 20]
c = sorted(a . values()) #Here all the values of dict is sorted in alphabetical order 
print(c) #Returns the sorted values i.e ['Blue', 'Green', 'Red', 'White', 'Yellow']
d = sorted(a . items()) #Here all the key-value pairs are sorted based on the keys in ascending order in list and inside list tuple of key and value
print(d) #Returns the sorted key-value pairs in list and inside list tuple of key and values i.e [(5, 'White'), (10, 'Red'), (15, 'Blue'), (18, 'Yellow'), (20, 'Green')] 
f  = sorted(a  , reverse = True) #Here sorting is done in reverse order and only keys are sorted i.e decending order
print(f) #Returns the reversed sorted keys i.e [20, 18, 15, 10, 5]
print(a) #Returns the original dict i.e {10 : 'Red' , 20 : 'Green' , 15 : 'Blue' , 18 : 'Yellow' , 5 : 'White'}



'''
Tricky  program
Write  a  program  to  sort  dictionary  wrt  keys  (Home  work)

1) Let  input  be   {10 : 'A' , 20 : 'B' , 15 : 'C' , 5 : 'D' , 12 : 'E'}
    What  is  the  output ?  ---> {5 : 'D' , 10 : 'A' ,  12 : 'E' ,  15 : 'C' , 20 : 'B'}

2) Both  input  and  output  are  dictionaries

3) Hint:  Use  sorted()  function
'''

n = eval(input("Enter input: "))
b = sorted(n.items())
c = dict(b)
print(c)

'''output:
Enter input: {10 : 'A' , 20 : 'B' , 15 : 'C' , 5 : 'D' , 12 : 'E'}
{5: 'D', 10: 'A', 12: 'E', 15: 'C', 20: 'B'}
'''



# clear()  method  demo  program (Home  work)
a = {10 : 20 , 30 : 40 , 50 : 60} #Reference a points to dict obj
print(a) #Returns the dict a i.e {10 : 20 , 30 : 40 , 50 : 60}
a . clear() #Here clear() removes all the key-value pairs and dict becomes empty
print(a) #Here empty dict is returned 
del  a #Here reference a is deleted
print(a) #Error there is no a as it is deleted using 'del' operator 



# copy()  method demo  program  (Home  work)
a = {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue'} #Reference a points to dict obj
b = a . copy() #Here copy() will make a deep copy i.e make a copy of dict a 
print(b) #Returns the copied dict i.e {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue'}
print(a  is  b) #Returns False
print(a  ==  b) #Returns True



#  keys()  method  demo  program
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'} #Reference a points to dict obj
b = a . keys() #Reference b points to set of keys without duplicates in any order
print(b) #Returns the keys of the dict a 
print(type(b)) #Returns the type() i.e <class 'dict_keys'>
for  x  in   b:
        print(x) #10 20 15 18


'''
What  does  keys()  method  do  --->  Returns  dict_keys  object  which  has  list  of  all  the  dictionary  keys
'''



# values()  method  demo  program
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'} #Reference a points to dict obj
b = a . values() #Reference b points to dict_values() obj
print(b) #Returns the dict_values(['Hyd', 'Sec', 'Cyb', 'Pune'])
print(type(b)) #Returns the type i.e <class 'dict_values'>
for  x   in   b:
	print(x) #Hyd Sec Cyb Pune


'''
What  does  values()  method  do  --->  Returns  dict_values  object  which  has  list  of  all  the  dictionary  values
'''



#  items()  method  demo  program
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'} #Reference a points to dict obj
b = a . items() #Reference b points to dict_items([()])
print(b) #Returns the obj dict_items([(10, 'Hyd'), (20, 'Sec'), (15, 'Cyb'), (18, 'Pune')])
print(type(b)) #Returns the type i.e <class 'dict_items'>
for  x   in   b:
        print(x) 
        '''#Returns the tuple of key-value pairs i.e  (10, 'Hyd')
                                                            (20, 'Sec')
                                                            (15, 'Cyb')
                                                            (18, 'Pune')'''
for  x , y   in  b:
        print(x , y , sep = ' ... ') #Returns the key (x) and value(y) with ... sep
'''10 ... Hyd
20 ... Sec
15 ... Cyb
18 ... Pune
'''

'''
1) What  does  items()  method  do  --->  Returns  dict_items  object  which  has  list  of  tuples

2) What  are  the  two  elements  of  each  tuple ?  ---> (key , value)
'''



# Find  outputs (Home  work)
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'} #Reference a points to dict obj
for  x , y   in  a . items(): 
       print(x , y , sep = ' ... ')
#The above for loop returns the key and value with ... separator
'''10...Hyd
20...Sec
15...Cyb
18...Pune'''
for  x , y   in  a . keys():
       print(x , y , sep = ' ... ')
#Error #As we should iterate the loop with 1 variable(Reference)
for  x , y   in  a . values():
       print(x , y , sep = ' ... ')
#Error #As we should iterate the loop with 1 variable(Reference)
for  x , y   in  a:
       print(x , y , sep = ' ... ')
#Error #As we should iterate the loop with 1 variable(Reference)



#  Find  outputs  (Home  work)
a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh'} #Reference a points to dict obj 
x , y , z = a . keys() #Here for dict obj keys are unpacked to 3 references i.e x , y , z
print(x) #10
print(y) #20
print(z) #15
print() #Prints nothing returns none and goes to next line
x , y , z = a . values() #Here for dict obj values are unpacked to 3 references i.e x,y,z
print(x) #Rama
print(y) #Sita
print(z) #Rajesh
print() #Prints nothing returns none and goes to next line
x , y ,  z = a . items() #Here for dict obj key-value pairs in tuple are unpacked to 3 references i.e x,y,z
print(x) #Tuple ()
print(y) #(10, 'Rama')
print(z) # (20, 'Sita')
print() #(15, 'Rajesh')
(rno1 , sname1) , (rno2 , sname2) , (rno3 , sname3) = a . items() #Here dict is unpacked to tuple (rno and sname) rno is key and sname is value
print(rno1 , sname1) #10 Rama
print(rno2 , sname2) #20 Sita
print(rno3 , sname3) #15 Rajesh





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

'''output:
Enter  mixed  case  string : RamA raO
{'A': 3, 'M': 1, 'O': 1, 'R': 2}
'''

n = input("Enter a mixed case string: ").upper()
b = sorted(n)
a = {}
for i in range(len(b)):
    if b[i] != ' ':
        a[b[i]] = b.count(b[i])
print(a)

'''output:
Enter a mixed case string: rama rao
{'A': 3, 'M': 1, 'O': 1, 'R': 2}
'''
