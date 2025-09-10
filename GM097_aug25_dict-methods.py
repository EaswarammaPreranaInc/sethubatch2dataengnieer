# 1) intersection()   method  demo  program (Home  work)

a = {10, 20, 30, 40}
b = {30, 40, 50, 60}
c = a.intersection(b) # Returns common elements
print(c) # {40, 30}
print(type(c)) # <class 'set'>
d = a & b
print(d) # {40, 30}
print(type(d)) # <class 'set'>
print(c is d) # False 
print(c == d) # True (same elements)




# 2) difference()   method  demo  program  (Home  work)

a = {10, 20, 30, 40}
b = {30, 40, 50, 60}
c = a.difference(b) # elements in set 'a' but not in set 'b'
print(c) # {10, 20}
print(type(c)) # <class 'set'>
d = a - b # alternative way
print(d) # {10, 20}
print(type(d)) # <class 'set'>
print(c is d) # False
print(c == d) # True 




# 3) symmetric_difference()   method  demo  program  (Home  work)

a = {10, 20, 30, 40}
b = {30, 40, 50, 60}
c = a.symmetric_difference(b) # elements from both sets excluding common
print(c) # {10, 20, 50, 60}
print(type(c)) # <class 'set'>
d = a ^ b # alternative way
print(d) # {10, 20, 50, 60}
print(type(d)) # <class 'set'>
print(c is d) # False
print(c == d) # True



''' 4) Write  a  program  to  remove  duplicate  characters  of  the  string  using  set

1) Let  input  be   Rama  Rao
    What  is  the  output  ? --->  Ram<space>o

2) Both  input  and  output  are  strings

3) How  to  convert  string  to  set  ?  --->  set(string)
    How  to  convert  set  to  string ?  --->  '' . join(set)

4) What  is  the  result  of  str({'H' , 'y' , 'd'})  ? --->  "{'H' , 'y' , 'd'}"  but  not  'Hyd'
'''

s = input("Enter input string: ") 
result = ''.join(set(s))
print("String without duplicates:", result)
'''
#Output:
Enter  input  string :  Rama Rao
String  without  duplicates  : amo R
'''



''' 5) Write  a  program  to  remove  duplicate  elements  of   list  using  set

1) Let  input  be  [False , 25 , 10.8 , 1  , 25 , 0 , 'Hyd' ,  10.8 , 1.0 , None , 'Sec' , 'Hyd' , True  ]
    What  is  the  output ?  ---> [False , 25 , 10.8 , 1 , 'Hyd' , None , 'Sec']

2) Both  input  and  output  are  lists
'''
l = eval(input("Enter list with duplicates: "))
new = list(set(l))
print("List without duplicates:", new)

'''
#Output:
Enter  list  with  duplicates :  [False , 25 , 10.8 , 1  , 25 , 0 , 'Hyd' ,  10.8 , 1.0 , None , 'Sec' , 'Hyd' , True  ]
List  without  duplicates :   [False, 1, None, 'Sec', 10.8, 25, 'Hyd']
'''


''' 6) Write  a  program  to   obtain  common  elements  between  two  lists  using  sets

1) Let  1st  list  be  [10 , 20 , 30 , 40 , 50 , 60]  and  2nd  list  be  [30 , 40 , 70 , 80 , 20]
    What  is  the  output ?  --->  [20 , 30 , 40]

2) Both  input  and  output  are  lists
'''
a = eval(input("Enter 1st list: "))
b = eval(input("Enter 2nd list: "))
common = list(set(a) & set(b))
print("Common elements between the 2 lists:", common)

'''
#Output:
Enter  1st  list  :  [10,20,30,40,50,60]
Enter  2nd  list  :  [30,40,70,80,20]
Common  elements  between  the  2  lists :   [40, 20, 30]
'''



# 7) How  to  access  values  of  dictionary (Home  work)

a  =  {'Empno'  :  25 ,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a['Empno']) #Output: 25 # How  to  print  value  25  in  dict  'a'
print(a['Ename']) #Output: Rama Rao # How  to  print  'Rama Rao'  in  dict  'a'
print(a['Sal']) #Output: 1000.65 # How  to  print  value  1000.65 in  dict  'a'



# 8) How  to  modify  values  of  dictionary  (Home  work)

a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a) # Output: {'Empno': 25, 'Ename': 'Rama  Rao', 'Sal': 1000.65}
print(id(a)) # address of set 'a'
a['Sal'] = 2000 # How  to  modify  1000.65  to  2000
a['Ename'] = 'Sita' # How  to  modify  'Rama  Rao'  to  'Sita'
a['Empno'] = 35 # How  to  modify  25   to  35
print(a) # Output: {'Empno': 35, 'Ename': 'Sita', 'Sal': 2000}
print(id(a)) # address of same set 'a'



# 9) How  to  append  key : value  pairs  to dictionary  (Home  work)

a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a) # Output: {'Empno': 25, 'Ename': 'Rama  Rao', 'Sal': 1000.65}
a['Gender']= 'M' # How  to  append  'Gender' : 'M'  to  dictionary  'a'
a['married']: True # How  to  append  'Married' :  True  to  dictionary  'a'
print(a) # Output: {'Empno': 25, 'Ename': 'Rama  Rao', 'Sal': 1000.65, 'Gender': 'M'}



# 10) Find  outputs (Home  work)

a = { }
a[10]= 'Rama' # How  to  append  10 : 'Rama'  to  dictionary  'a'
a[20]= 'Sita' # How  to  append  20 : 'Sita'  to  dictionary  'a'
a[15]= 'Rajesh' # How  to  append  15 : 'Rajesh'  to  dictionary  'a'
a[18]= 'Kiran' # How  to  append  18 : 'Kiran'  to  dictionary  'a'
print(a) # Output: {10: 'Rama', 20: 'Sita', 15: 'Rajesh', 18: 'Kiran'}



# 11) How  to  remove  key : value  pairs  of  dictionary  (Home  work)

a =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a) # Output: {'Empno': 25, 'Ename': 'Rama  Rao', 'Sal': 1000.65}
del a['Sal'] # How  to  remove  'Sal' : 1000.65  from  dictionary  'a'
print(a) # Output: {'Empno': 25, 'Ename': 'Rama  Rao'}



# 12) in  and  not  in  operators  (Home  work)

a =  {10 : 20 , 30 : 40 , 50 : 60 , 70 : 80}
print(30  in  a . keys()) # Output: True
print(60  in  a . keys()) # Output: False
print(60  in  a . values()) # Output: True
print(30  in  a . values()) # Output: False
print(50  in  a) # Output: True
print(20  in  a) # Output: False
print(70  not  in  a . keys()) # Output: False
print(40  not  in  a . values()) # Output: False
print(25  not  in  a) # Output: True


# 13) What  are  the  outputs  if  input  is  {10: 'A', 20: 'B', 15: 'C' , 20 : 'D'}

a = input('Enter  dictionary  :  ')
print(a) # Output: {10: 'A', 20: 'B', 15: 'C' , 20 : 'D'}
print(type(a)) # Output: <class 'str'>
b = eval(a)
print(b) # Output: {10: 'A', 20: 'D', 15: 'C'}
print(type(b)) # Output: <class 'dict'>



# 14) Find  outputs  (Home  work)

a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh' , 18 : 'Kiran'}
b = {**a}
print(b) # Output: {10: 'Rama', 20: 'Sita', 15: 'Rajesh', 18: 'Kiran'}
print(a  is  b) # Output: False
print(a  ==  b) # Output: True
c = a
print(a  is   c) # Output: True
print(a  ==  c) # Output: True



# 15) Find  outputs  (Home  work)

a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh'}
b = {18 : 'Kiran' , 14 : 'Amar' , 20  : 'Manohar'}
c = {25 : 'Ramesh' , 19 : 'Krishna' , 15 : 'Radha' , 14 : 'Srinivas'}
d = {*a , *b , *c} # unpacks the keys only gives keys in set
print(d) # Output: {10, 14, 15, 18, 19, 20, 25}
print(type(d)) # Output: <class 'set'>
e = {**a , **b , **c} # unpacks the item to give new dict
print(e) # Output: {10: 'Rama', 20: 'Manohar', 15: 'Radha', 18: 'Kiran', 14: 'Srinivas', 25: 'Ramesh', 19: 'Krishna'}
print(type(e)) # Output: <class 'dict'>



# 16) Find  outputs  (Home  work)

a = {10 : 20 , 30 : 40}
b = {30 : 50 , 10 : 60}
#print(a + b) # Error as '+' is invalid for dict
c = {**a , **b}
print(c) # Output: {10: 60, 30: 50}
d = a | b
print(d) # Output: {10: 60, 30: 50}



''' 17) 
Write  a  program  to  create  a  dictionary  with  emp  names  and  salaries

Hint:  Append  each  emp  name  and  salary  to  dictionary  'a'
'''
n = int(input("How many Employees? : "))
employees = {}
for i in range(n):
    name = input("Enter Emp Name : ")
    salary = float(input("Enter Salary : "))
    employees[name] = salary
print(employees)

'''
# Output:
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


''' 17) Write  a  program  to  convert  a  string  to  dictionary

Let  input  be   "Emp no = 25 , Emp name = Rama  Rao , sal = 10000.0 , gender = m"

What  is  the  output ?  --->  {Emp no : 25 , Emp name  :  Rama Rao , sal : 10000.0 , gender : m}

Hint :  Use  split()  method  twice
'''

s = input("Enter Emp details:")
b = s.split(',')  
emp_dict = {}
for pair in b:
    key, value = pair.split('=')  
    emp_dict[key] = value  
print(emp_dict)

'''
# Output:
Enter Emp details: Emp no = 25 , Emp name = Rama  Rao , sal = 10000.0 , gender = m
{'Emp no ': ' 25 ', ' Emp name ': ' Rama  Rao ', ' sal ': ' 10000.0 ', ' gender ': ' m'}
'''


# 18) len()  function  demo  program  (Home  work)
a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(len(a)) # Output: 3
b = {}
print(len(b)) # Output: 0




# 19) sum()  function demo  program  (Home  work)

a = {10 : 20 , 30 : 40 , 50 : 60}
print(sum(a . keys())) # Output: 90
print(sum(a . values())) # Output: 120
print(sum(a)) # Output: 90
print(sum(a . items())) # Error as sum is not supported for dict.items





# 20) max()  and  min()   functions  demo  program  (Home  work)

a = {10 : 20 , 30 : 25 , 40 : 5 , 7 : 28 , 9 : 50}
print(max(a . keys())) # Output: 40
print(min(a . keys())) # Output: 7
print(max(a . values())) # Output:50 
print(min(a . values())) # Output: 5
print(max(a . items())) # Output: (40, 5)
print(min(a . items())) # Output: (7, 28)
print(max(a)) # Output: 40
print(min(a)) # Output: 7




# 21) dict()  function  demo program (Home  work))

a = [ (10 , 'Hyd') , (20 , 'Sec') , (15 , 'Cyb') , (20 , 'Pune')]
b = dict(a)
print(b) # Output: {10: 'Hyd', 20: 'Pune', 15: 'Cyb'}
c = ( ['R' , 'Red'] , ['G' , 'Green'] , ['B' , 'Blue'] , ['G' , 'Gray'])
d = dict(c)
print(d) # Output: {'R': 'Red', 'G': 'Gray', 'B': 'Blue'}
e = [[10 , 20 , 30] , [40 , 50 , 60] , [70 , 80 , 90]]
print(dict(e)) # Output: # Error there should only two elemnts in list to convert it into dict
f = [[10] , [20] , [30]]
print(dict(f)) # Error there should only two elemnts to convert it into dict
print(dict([10 , 20])) # Error
g = [[10 , [20 , 30]] , [40 , [50 , 60]] , [70 , [80 , 90]]]
print(dict(g)) # Output: {10: [20, 30], 40: [50, 60], 70: [80, 90]}
h = [[[10 , 20] , 30] , [[40 , 50] , 60] , [[70 , 80] , 90]]
print(dict(h)) # Error
i = [[(10 , 20) , 30] , [(40 , 50) , 60] , [(70 , 80) , 90]]
print(dict(i)) # {(10, 20): 30, (40, 50): 60, (70, 80): 90}



# 22) sorted()  function  (Home  work)

a = {10 : 'Red' , 20 : 'Green' , 15 : 'Blue' , 18 : 'Yellow' , 5 : 'White'}
b = sorted(a . keys())
print(b) # Output: [5, 10, 15, 18, 20]
c = sorted(a . values())
print(c) # Output: ['Blue', 'Green', 'Red', 'White', 'Yellow']
d = sorted(a . items())
print(d) # Output: [(5, 'White'), (10, 'Red'), (15, 'Blue'), (18, 'Yellow'), (20, 'Green')]
f  = sorted(a  , reverse = True)
print(f) # Output: [20, 18, 15, 10, 5]
print(a) # Output: {10: 'Red', 20: 'Green', 15: 'Blue', 18: 'Yellow', 5: 'White'}



''' 23) Tricky  program
Write  a  program  to  sort  dictionary  wrt  keys  (Home  work)

1) Let  input  be   {10 : 'A' , 20 : 'B' , 15 : 'C' , 5 : 'D' , 12 : 'E'}
    What  is  the  output ?  ---> {5 : 'D' , 10 : 'A' ,  12 : 'E' ,  15 : 'C' , 20 : 'B'}

2) Both  input  and  output  are  dictionaries

3) Hint:  Use  sorted()  function
'''
my_dict = eval(input("Enter dictionary: "))
sorted_dict = dict(sorted(my_dict.items()))
print(sorted_dict)

'''
# Output:
Enter  dictionary  :  {10 : 'A' , 20 : 'B' , 15 : 'C' , 5 : 'D' , 12 : 'E'}
{5: 'D', 10: 'A', 12: 'E', 15: 'C', 20: 'B'}
'''


# 24) clear()  method  demo  program (Home  work)

a = {10 : 20 , 30 : 40 , 50 : 60}
print(a) # Output: {10: 20, 30: 40, 50: 60}
a . clear()
print(a) # Output: {}
del  a
#print(a) # error as there is object 'a'



# 25) copy()  method demo  program  (Home  work)

a = {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue'}
b = a . copy()
print(b) # Output: {'R': 'Red', 'G': 'Green', 'B': 'Blue'}
print(a  is  b) # Output: False
print(a  ==  b) # Output: True



# 26) keys()  method  demo  program

a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
b = a . keys()
print(b) # Output: dict_keys([10, 20, 15, 18])
print(type(b)) # Output: <class 'dict_keys'>
for  x  in   b:
        print(x)
''' 
# Output: 
10
20
15
18
'''    


# 27) values()  method  demo  program

a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
b = a . values()
print(b) # Output: dict_values(['Hyd', 'Sec', 'Cyb', 'Pune'])
print(type(b)) # Output: <class 'dict_values'>
for  x   in   b:
	print(x)
''' 
# Output: 
Hyd
Sec
Cyb
Pune
'''   




# 28) items()  method  demo  program

a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
b = a . items()
print(b) # Output: dict_items([(10, 'Hyd'), (20, 'Sec'), (15, 'Cyb'), (18, 'Pune')])
print(type(b)) # Output: <class 'dict_items'>
for  x   in   b:
        print(x)
''' 
# Output: 
(10, 'Hyd')
(20, 'Sec')
(15, 'Cyb')
(18, 'Pune')
'''    
for  x , y   in  b:
        print(x , y , sep = ' ... ')
''' 
# Output: 
10 ... Hyd
20 ... Sec
15 ... Cyb
18 ... Pune
'''    
print()
# Find  outputs (Home  work)
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
for  x , y   in  a . items():
       print(x , y , sep = ' ... ')
''' 
# Output: 
10 ... Hyd
20 ... Sec
15 ... Cyb
18 ... Pune
'''      
for  x , y   in  a . keys():
       print(x , y , sep = ' ... ') # error as cannot unpack non-iterable int
for  x , y   in  a . values():
       print(x , y , sep = ' ... ') # error as too many values to unpack
for  x , y   in  a:
       print(x , y , sep = ' ... ') # error as cannot unpack non-iterable int 



# 29) Find  outputs  (Home  work)

a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh'}
x , y , z = a . keys()
print(x) # Output: 10
print(y) # Output: 20
print(z) # Output: 15
print()
x , y , z = a . values()
print(x) # Output: Rama
print(y) # Output: Sita
print(z) # Output: Rajesh
print()
x , y ,  z = a . items()
print(x) # Output: (10, 'Rama')
print(y) # Output: (20, 'Sita')
print(z) # Output: (15, 'Rajesh')
print()
(rno1 , sname1) , (rno2 , sname2) , (rno3 , sname3) = a . items()
print(rno1 , sname1) # Output: 10 Rama
print(rno2 , sname2) # Output: 20 Sita
print(rno3 , sname3) # Output: 15 Rajesh



''' 30) Tricky  program
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
s = input("Enter mixed case string: ")
s = s.upper()
sorted_list = sorted(s)
freq = {}
for ch in sorted_list:
    if ch.isalpha():  
        freq[ch] = freq.get(ch, 0) + 1
sorted_freq = dict(sorted(freq.items()))
print(sorted_freq)

'''
# Output: 
Enter  mixed  case  string : RamA raO
{'A': 3, 'M': 1, 'O': 1, 'R': 2}'''








