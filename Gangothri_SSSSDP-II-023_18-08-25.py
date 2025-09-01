#  len()  function demo   program  (Home  work)
a = [ 25, 10.8, 'Hyd', True]
print(len(a)) # 4
b = []
print(len(b)) # 0
c = [[10 , 20] , 30 , 40]
print(len(c))# 3

# sum()  function  demo  program  (Home  work)
a = [25 , 10.8 , True]
print(sum(a)) # 36.8
b= [3 + 4j , 5 + 6j]
print(sum(b)) # (8+10j)
c = [25 , 10.8 , True , 3 + 4j , False]
print(sum(c)) # (39.8+4j)
d = [10 , 20 , 15 , 18]
print(sum(d)) # 63
e = [25 , 10.8 , 'Hyd' , True]
print(sum(e)) # Error cannot add float and string

#  Find  outputs
a = [[10 , 20 , 15 , 18]]
print(sum(a)) # Error Python tries to add the inner lists together, not their numbers
#print(How  to  determine  sum  of  inner  list  elements)
a = [[10, 20, 15, 18]]
print(sum(a[0]))
#print(How  to  determine  sum  of  inner  list  elements in another way)
print(sum(*a))

# max()  and  min()  functions  demo  program  (Home  work)
a = [10 , 20 , 15 , 18 , 30, 5 , 12]
print(max(a)) # 30
print(min(a)) # 5
b = ['Rama' , 'Sita' , 'Rajesh' , 'Kiran' , 'Amar' , 'Vamsi' , 'Manohar']
print(max(b)) # Vamsi
print(min(b)) # Amar
c = [25 , 10.8 ,  3 + 4j , True]
print(max(c)) # Error
d = [25 , '35']
print(max(d)) # error
print(max([])) # ValueError
print(min([])) # ValueError

# list()  function  demo  program
a = (10 , 20 , 15, 18)
b = list(a)
print(b) # [10,20,15,18]
print(type(b)) #<class 'list'>
print(a  is  b) # False
print(a == b) # False

#  Find  outputs (Home  work)
a = range(4 , 10 , 2)
b = list(a)
print(b) # [4,8]
print(type(b)) # <class 'list'>
a = list('Vamsi')
print(a) # ['V', 'a', 'm', 's', 'i']
a = list()
print(a) # empty []
print(list(25)) # Error
print(list(10.8)) # Error
print(list(True)) # Error
print(list(None)) # Error

# Find  outputs (Home  work)
a = ((10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90))
print(list(a)) # [(10, 20), (30, 40, 50), (60, 70, 80, 90)]
b = { (10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90)}
print(list(b)) # [(30, 40, 50), (60, 70, 80, 90), (10, 20)]
c = ([10 , 20] , (30 , 40) , {50 , 60})
print(list(c)) # [[10, 20], (30, 40), {50, 60}]

# sorted()  function   demo  program
a = [10 , 20 , 15 , 5 , 12]
b = sorted(a)
print(b) # [5, 10, 12, 15, 20]
print(type(b)) # <class 'list'>
c = sorted(a , reverse = True)
print(c) # [20, 15, 12, 10, 5]
print(a) # [10 , 20 , 15 , 5 , 12]

# Find  outputs  (Home  work)
a = ['Rama',  'Rajesh',  'Amar',  'Sita',  'Vamsi'  ,  'Kiran'  , 'Rama  Rao']
b = sorted(a)
print(b) # ['Amar','Kiran', 'Rajesh', 'Rama', 'Rama Rao', 'Sita', 'Vamsi']
c = sorted(a , reverse = True)
print(c) # reverse order ['Vamsi', 'Sita', 'Rama  Rao', 'Rama', 'Rajesh', 'Kiran', 'Amar']
print(a) # ['Rama',  'Rajesh',  'Amar',  'Sita',  'Vamsi'  ,  'Kiran'  , 'Rama  Rao']

# all()  function demo  program  (Home  work)
a = [12 > 10 , 5 < 20 , 30 == 30]
print(all(a)) # True
b = [9 >= 6 , 12 <= 9 , 6 == 6]
print(all(b)) # False
c = [25 , 10.8 , '' , True , 3+4j , 'Hyd']
print(all(c)) # False
d = [10 , 0 , 20]
print(all(d)) # False
e = [] # True
print(all(e))

# any()  function demo program  (Home  work)
a  = [12 > 18 , 5 < 20 , 35 == 30]
print(any(a)) # True
b = [12 > 18 , 25 < 20 , 35 == 30]
print(any(b)) # False 
c = [0 , 0.0 , '' , 25 , 0 + 0j , False]
print(any(c)) # True
d = [0 , 0.0 , '' , 0 + 0j , False]
print(any(d)) # False
e = []
print(any(e)) # False

# del  operator  demo  program (Home  work)
a = [10 , 20 , 15 , 18]
print(a) # [10, 20, 15, 18]
del    a[2] 
print(a) # [10, 20, 18]
del  a[3] # error
del a # error
print(a) # Error

#  append()  method  demo  program (Home  work)
list = [10 , 20 , 15 , 18]
print(list) # [10, 20, 15, 18]
list.append(19)
print(list) # [10,20,15,18,19]

#  Find  outputs (Home  work)
list = []
print(list) # [] empty list
list.append(25)
list.append(10.8)
list.append('Hyd')
list.append(True)
print(list) # [25, 10.8, 'Hyd', True]

# Find  outputs  (Home  work)
list = []
for  x  in   range(0 , 50 , 10):
	list.append(x)
print(list) # [0, 10, 20, 30, 40]

#  Find  outputs  (Home  work)
a = [10 , 20 , 30]
a.append('Hyd')
print(a) # [10,20,30,'Hyd']
print(len(a)) # 4
print(a[3]) #print(How  to  print  4th  element  of  list  'a') 
#print(How  to  print  'H') 
print(a[3][0])
#print(How  to  print  'y')
print(a[3][1])
#print(How to print 'd')
print(a[3][2])

'''
Write  a  program  to  delete  'all'  occurences  of  'x'  from  the  list

Let  1st  input  be   [10 , 20 , 15 , 18 , 19 , 15 , 17 , 20 , 15 , 14]  and
2nd  input  be  15
What  is  the  output ?  ---> [10 , 20 ,  18 , 19 , 17 , 20 , 14]
'''
try:
	list = [10 , 20 , 15 , 18 , 15 , 12 , 15 , 19]
	list.remove(15)
	print(list) # first 15 is removed [10, 20, 18, 15, 12, 15, 19]
	list.remove(25) # Here except suite is executed
except:
	print('25 is not in the list')
# clear() method  demo program  (Home  work)
list = [10 , 20 , 15 , 18]
print(list) # [10, 20, 15, 18]
list . clear()
print(list) # []
x = eval(input("Enter the list: "))
element = eval(input("Enter the element: "))
for i in x:
    if i==element:
        x.remove(i)
print(x)                                                                                                                                                                                    Output: Enter the list: [10 , 20 , 15 , 18 , 19 , 15 , 17 , 20 , 15 , 14]
'''Enter the element: 15
[10, 20, 18, 19,17,20,14]'''
# reverse()  method  demo  program (Home  work)
a = [10 , 20 , 15 , 18]
print(a)  # [10 , 20 , 15 , 18]
a.reverse() 
print(a) # # [18, 15, 20, 10]
#  sort()  method  demo  program (Home  work)
list = [10 , 20 , 15 , 18 , 5]
print(list) # [10 , 20 , 15 , 18 , 5]
list.sort()
print(list) # [5, 10, 15, 18, 20]
list . sort(reverse = True)
print(list) # [20, 18, 15, 10, 5]
# Find  outputs (Home  work)
a = ['Rama' , 'Rajesh' , 'Amar' ,  'Sita' ,  'Vamsi' , 'Kiran' , 'Rama  Rao']
print(a) # ['Rama', 'Rajesh', 'Amar', 'Sita', 'Vamsi', 'Kiran', 'Rama  Rao']
a.sort()
print(a) # ['Amar', 'Kiran', 'Rajesh', 'Rama', 'Rama  Rao', 'Sita', 'Vamsi']
a.sort(reverse = True)
print(a) # ['Amar', 'Kiran', 'Rajesh', 'Rama', 'Rama  Rao', 'Sita', 'Vamsi']
# Identify  error (Home  work)
a = [25 , 10.8 ,  'Hyd' ,  True]
a.sort()# error
#  count()  method  demo    program (Home  work)
a = [10 , 20 , 15 , 18 , 15 , 12 , 14 , 15 , 19]
print(a . count(15)) # 3
print(a . count(25)) # 0
print(len(a)) # 9
x = [10, 20, 15, 10, 14, 10, 18, 20, 19]
result = []
for i in x:
    if x.count(i) == 1:   # keep only elements that occur once
        result.append(i)
print(result)
x = eval(input("Enter any list : "))
n = len(x)                  
count_first = x.count(x[0]) 
if count_first == n:
    print("All the list elements are identical")
else:
    print("List elements are not identical")
print("How many elements are in the list? --->", n)
print("How many times is first element repeated? --->", count_first)                                                                    Output:
'''Enter any list : [25,25,25,25]
All the list elements are identical
How many elements are in the list? ---> 4
How many times is first element repeated? ---> 4                                                                                          Enter any list : [10,10,20,10]
List elements are not identical
How many elements are in the list? ---> 4
How many times is first element repeated? ---> 3'''
# index()  method  demo  program  (Home  work)
a = [10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25]
#     0     1     2    3    4     5    6    7     8    9    10
try:
	i = a . index(15)
	while  True:
		print(i)
		i = a . index(15 , i + 1)
except:
	print(F'15  is  found  {a . count(15)}  times ')
'''Output:
2
5
8
15  is found 3 times'''
