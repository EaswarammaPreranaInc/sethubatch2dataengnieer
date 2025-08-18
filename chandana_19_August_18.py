# len()function

a=[25,10.8,'Hyd',True]
print(len(a)) # 4
b =[]
print(len(b))  # 0
c=[[10,20],30,40]
print(len(c))  #  3

# sum()  function
a = [25 , 10.8 , True]
print(sum(a))   # 36.8
b= [3 + 4j , 5 + 6j]
print(sum(b))  # (8+10j)
c = [25 , 10.8 , True , 3 + 4j , False]
print(sum(c))  # (39.8+4j)
d = [10 , 20 , 15 , 18]
print(sum(d))  # 63
e = [25 , 10.8 , 'Hyd' , True] 
#print(sum(e))  # TypeError: str and float cannot be added

# Find outputs
a= [[10,20,15,18]]
#print(sum(a)) # Error : list 'a' has only one element
print(sum(a[0])) # 63 : determine sum of inner list elements
print(sum(x for x in a[0])) # 63


# max()  and  min()  functions  
a = [10 , 20 , 15 , 18 , 30, 5 , 12]
print(max(a))  # 30
print(min(a))  # 5
b = ['Rama' , 'Sita' , 'Rajesh' , 'Kiran' , 'Amar' , 'Vamsi' , 'Manohar']
print(max(b))  # Vamsi
print(min(b)) # Amar
c = [25 , 10.8 ,  3 + 4j , True]
#print(max(c)) # TypeError: cannot compare int and complex
d = [25 , '35']
#print(max(d)) # TypeError: cannot compare int and string
#print(max([])) # ValueError
#print(min([])) # valueError

# list()  function  
a = (10 , 20 , 15, 18)
b = list(a) 
print(b) # [10,20,15,18]
print(type(b)) # <class 'list'>
print(a  is  b) # False
print(a == b)  # False


#  Find  outputs 
a = range(4 , 10 , 2)
b = list(a)
print(b) # [4,10,2]
print(type(b)) # <class 'list'>
a = list('Vamsi')
print(a) # ['vamsi']
a = list()
print(a) # [] : Empty list
#print(list(25)) # Error : int is not iterable
#print(list(10.8)) # TypeError : float object is not iterable
#print(list(True)) # TypeError : bool object is not iterable
#print(list(None)) # TypeError : NoneType object is not iterable

# Find  outputs 
a = ((10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90))
print(list(a)) # [(10, 20), (30, 40, 50), (60, 70, 80, 90)]
b = { (10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90)}
print(list(b))  #  [(30, 40, 50), (60, 70, 80, 90), (10, 20)]
c = ([10 , 20] , (30 , 40) , {50 , 60})
print(list(c))  #  [[10, 20], (30, 40), {50, 60}]

# sorted() function
a=[10,20,15,5,12]
b=sorted(a) # arrange the elements of the list in ascending order
print(b)  # [5, 10, 12, 15, 20]
print(type(b)) # <class 'list'>
c=sorted(a,reverse=True)
print(c) # [20, 15, 12, 10, 5]
print(a) # [10, 20, 15, 5, 12]

# Find  outputs  
a = ['Rama',  'Rajesh',  'Amar',  'Sita',  'Vamsi'  ,  'Kiran'  , 'Rama  Rao']
b = sorted(a)
print(b) # ['Amar', 'Kiran', 'Rajesh', 'Rama', 'Rama  Rao', 'Sita', 'Vamsi']
c = sorted(a , reverse = True)
print(c) # ['Vamsi', 'Sita', 'Rama  Rao', 'Rama', 'Rajesh', 'Kiran', 'Amar']
print(a)  #  ['Rama', 'Rajesh', 'Amar', 'Sita', 'Vamsi', 'Kiran', 'Rama  Rao']


# all()  function 
a = [12 > 10 , 5 < 20 , 30 == 30]
print(all(a))  # True : Returns True when every element of the list is True
b = [9 >= 6 , 12 <= 9 , 6 == 6]
print(all(b))  # False : return False when at least one element of the list is False
c = [25 , 10.8 , '' , True , 3+4j , 'Hyd']
print(all(c)) # False
d = [10 , 0 , 20]
print(all(d)) # False
e = [] 
print(all(e))  # True


# any()  function 
a  = [12 > 18 , 5 < 20 , 35 == 30]
print(any(a))  # True : returns True when atleast one element of the list is True
b = [12 > 18 , 25 < 20 , 35 == 30]
print(any(b)) # False : returns False when every element of the list is False
c = [0 , 0.0 , '' , 25 , 0 + 0j , False]
print(any(c)) # True
d = [0 , 0.0 , '' , 0 + 0j , False]
print(any(d)) # False
e = []
print(any(e)) # False


# del  operator  
a = [10 , 20 , 15 , 18]
print(a)  # [10,20,15,18]
del    a[2]
print(a) # [10,20,18]
#del  a[3] # Error : There is no index 3
del  a # deletes entire list
#print(a) # NameError: No ref 'a'

#  append()  method  
list = [10 , 20 , 15 , 18]
print(list) # [10,20,15,18]
list . append(19) # append 19 at the end of the list
print(list) # [10, 20, 15, 18, 19]


#  Find  outputs 
list = []
print(list) # []
list . append(25) # append 25 to the list
list . append(10.8) # append 10.8 at the end of the list
list . append('Hyd')
list . append(True)
print(list) #  [25, 10.8, 'Hyd', True]

# Find  outputs  
list = []
for  x  in   range(0 , 50 , 10):
	list . append(x)
print(list)   #  [0, 10, 20, 30, 40]


# find outputs
a=[10,20,30]
a.append('Hyd')
print(a) # [10,20,30,'Hyd']
print(a[3]) # Hyd
print(a[3][0]) # H
print(a[3][1]) # y
print(a[3][2]) # d

# remove()  method  
try:
	list = [10 , 20 , 15 , 18 , 15 , 12 , 15 , 19]
	list . remove(15)
	print(list) # [10 , 20 , 18 , 15 , 12 , 15 , 19]
	list . remove(25) # Error and except suite is executed because their is no element 25 in the list
except:
	print('25  is   not  in  the  list') 

#program to delete 'all' occurences of 'x' from the list
a=eval(input("Enter list :"))
x=eval(input("Enter element to be deleted :"))
for i in a :
	if i==x:
		a.remove(x)
print(a)
	
'''
output:
Enter list :[10, 20, 18, 15, 12, 15, 19]
Enter element to be deleted :15
[10, 20, 18, 12, 19]
'''

# clear() method
list=[10,20,15,18]
print(list) # [10,20,15,18]
list.clear() # Removes all the elements of the list and list becomes emoty
print(list) # []
		
# reverse() method
a=[10,20,15,18]
print(a)  #  [10, 20, 15, 18]
a.reverse()  # reverse all the elements of list
print(a)  #  [18, 15, 20, 10]

#  sort()  method  
list = [10 , 20 , 15 , 18 , 5]
print(list)  # [10, 20, 15, 18, 5]
list . sort()
print(list)  #  [5, 10, 15, 18, 20]
list . sort(reverse = True)
print(list)  #  [20, 18, 15, 10, 5]


# Find  outputs 
a = ['Rama' , 'Rajesh' , 'Amar' ,  'Sita' ,  'Vamsi' , 'Kiran' , 'Rama  Rao']
print(a) # ['Rama', 'Rajesh', 'Amar', 'Sita', 'Vamsi', 'Kiran', 'Rama  Rao']
a . sort()
print(a)  # ['Amar', 'Kiran', 'Rajesh', 'Rama', 'Rama  Rao', 'Sita', 'Vamsi']
a . sort(reverse = True)
print(a) # ['Vamsi', 'Sita', 'Rama  Rao', 'Rama', 'Rajesh', 'Kiran', 'Amar']

# Identify  error (Home  work)
a = [25 , 10.8 ,  'Hyd' ,  True]
#a . sort() # TypeError: cannot compare str and float

#  count()  method  
a = [10 , 20 , 15 , 18 , 15 , 12 , 14 , 15 , 19]
print(a . count(15))  # 3
print(a . count(25))  # 0
print(len(a))  # 9

#program to remove all duplicate elements of the list(Not even a single occurance)
x=eval(input("enter list :"))
a=[]
for i in x:
	if x.count(i)==1:
		a.append(i)
print(a)
'''
output:
enter list :[10,20,30,10,20]
[30]
'''

#program to determine all the list elements are identical or not
x=eval(input("enter list :"))
if x.count(x[0])==len(x):
	print("All the elements are identical")
else:
	print("List elements are not identical")

'''
output:
enter list :[10,10,10]
All the elements are identical

enter list :[10,20,10]
List elements are not identical
'''

# index()  method  
a = [10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25]
#     0     1     2    3    4     5    6    7     8    9    10
try:
	i = a . index(15)
	while  True:
		print(i) 
		i = a . index(15 , i + 1)
except:
	print(F'15  is  found  {a . count(15)}  times ') 
'''
output:
2
5
8
15  is  found  3  times
'''