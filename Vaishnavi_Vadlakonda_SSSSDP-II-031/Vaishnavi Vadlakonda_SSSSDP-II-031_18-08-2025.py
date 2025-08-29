#  len()  function demo   program  (Home  work)
a = [25, 10.8, 'Hyd', True]  # Ref 'a' points to list of 4 elements
print(len(a)) # prints number of elements in the list i.e., 4
b = [] # Ref 'b' points to empty list
print(len(b)) # prints number of elements in list i.e., 0
c = [[10 , 20] , 30 , 40] # Ref 'c' points to list of 3 elements
print(len(c)) # prints number of elements in list i.e., 3








# sum()  function  demo  program  (Home  work)
a = [25 , 10.8 , True] # # Ref 'a' points to list of 3 elements
print(sum(a)) # prints 36.8
b= [3 + 4j , 5 + 6j] # Ref 'b' points to list of 2 elements
print(sum(b)) # prints (8 + 10j)
c = [25 , 10.8 , True , 3 + 4j , False] # Ref 'c' points to list of 5 elements
print(sum(c))  # prints (39.8 + 4j)
d = [10 , 20 , 15 , 18] # Ref 'd' points to list of 4 elements
print(sum(d)) # prints 63
e = [25 , 10.8 , 'Hyd' , True] # Ref 'e' points to list of 4 elements
print(sum(e)) # Error because string cannot be added










#  Find  outputs
a = [[10 , 20 , 15 , 18]] # Ref 'a' points to list of 1 element
print(sum(a)) # Error because because there is only one element in list 
print(a) #How  to  determine  sum  of  inner  list  elements
print(sum(a[0])) #How  to  determine  sum  of  inner  list  elements  in  another  way
      








# max()  and  min()  functions  demo  program  (Home  work)
a = [10 , 20 , 15 , 18 , 30, 5 , 12] # Ref 'a' points to list of 7 elements
print(max(a)) # prints largest number in list 'a' i.e., 30
print(min(a)) # prints smallest number in list 'a' i.e., 5
b = ['Rama' , 'Sita' , 'Rajesh' , 'Kiran' , 'Amar' , 'Vamsi' , 'Manohar'] # Ref 'b' points to list of 7 elements
print(max(b)) # prints largest element in list 'b' by first non matching character of string i.e., Vamsi
print(min(b)) # prints smallest element in list 'b' by first non matching character of string i.e., Amar
c = [25 , 10.8 ,  3 + 4j , True] # Ref 'c' points to list of 4 elements
#print(max(c)) # Error because int and complex cannot be compared
d = [25 , '35'] # Ref 'd' points to list of 2 elements
#print(max(d)) # Error because int and string cannot be compared
print(max([])) # Error because max function cannot be empty,it should contain argument
print(min([])) # Error because min function cannot be empty,it should contain argument











# list()  function  demo  program
a = (10 , 20 , 15, 18) # Ref 'a' points tuple of 4 elements
b = list(a) # tuple 'a' converts to list and assigned reference 'b'
print(b) # prints list of 4 elements i.e., [10, 20, 30, 40]
print(type(b)) # prints type of 'b' i.e., <class str>
print(a  is  b) # prints False
print(a == b) # prints False
      








#  Find  outputs (Home  work)
a = range(4 , 10 , 2) # Ref 'a' points to range object
b = list(a) # range object is converted to list and assigned to reference 'b' i.e., [4, 6, 8]
print(b) # prints list i.e., [4, 6, 8]
print(type(b)) # prints type of 'a' i.e., <class list>
a = list('Vamsi') # Converts string object Vamsi to list and assigned to reference 'a'
print(a) # prints list i.e., ['V', 'a', 'm', 's', 'i']
a = list() # converts empty tuple to list and assign to reference 'a'
print(a) # prints empty list i.e., []
print(list(25)) # Error because int object cannot be convertted to list
print(list(10.8)) # Error because float object cannot be convertted to list
print(list(True)) # Error because boolen object cannot be convertted to list
print(list(None)) # Error because Nonetype object cannot be convertted to list





 





# Find  outputs (Home  work)
a = ((10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90)) # Ref 'a' points to tuple of tuples
print(list(a)) # converts tuple of tuples into list of tuples and prints [(10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90)]
b = { (10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90)} # Ref 'b' points to set of tuples
print(list(b)) # converts set of tuples into list of tuples and prints [(10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90)] in any order
c = ([10 , 20] , (30 , 40) , {50 , 60}) # Ref 'c' points to tuple of sequences
print(list(c)) # converts tuple of sequences to list of sequences and prints [[10 , 20] , (30 , 40) , {50 , 60}]









# sorted()  function   demo  program
a = [10 , 20 , 15 , 5 , 12] # Ref 'a' points to list of 5 elements
b = sorted(a) # list 'a' is sorted and assigned to 'b'
print(b) # prints 'b' i.e., [5, 10, 12, 15, 20]
print(type(b)) # prints type of 'b' i.e., <class list>
c = sorted(a , reverse = True) # list 'a' is sorted in descending order and assigned to reference 'c'
print(c) # prints 'c' i.e., [20, 15, 12, 10, 5]
print(a) # prints 'a' i.e., [10, 20, 15, 5, 12]









# Find  outputs  (Home  work)
a = ['Rama',  'Rajesh',  'Amar',  'Sita',  'Vamsi'  ,  'Kiran'  , 'Rama  Rao'] # Ref 'a' points to list of strings
b = sorted(a) # list 'a' is sorted and assigned to 'b'
print(b) # prints sorted list i.e., ['Amar', 'Kiran', 'Rajesh', 'Rama', 'Rama Rao', 'Sita', 'Vamsi' ]
c = sorted(a , reverse = True) # list 'a' is sorted in descending order and assigned to reference 'c'
print(c) # prints sorted list 'c' i.e., ['Vamsi', 'Sita', 'Rama Rao', 'Rama', 'Rajesh', 'Kiran', 'Amar']
print(a) # prints list 'a' i.e., ['Rama',  'Rajesh',  'Amar',  'Sita',  'Vamsi'  ,  'Kiran'  , 'Rama  Rao']









# all()  function demo  program  (Home  work)
a = [12 > 10 , 5 < 20 , 30 == 30] # Ref 'a' points to list of conditions
print(all(a)) # prints True because all conditions are True
b = [9 >= 6 , 12 <= 9 , 6 == 6] # Ref 'b' points to list of conditions
print(all(b)) # prints False because if atleast one condition is False then it returns False
c = [25 , 10.8 , '' , True , 3+4j , 'Hyd'] # Ref 'c' points to list of 6 elements
print(all(c)) # prints False because '' is False
d = [10 , 0 , 20] # Ref 'd' points to list of 3 elements
print(all(d)) # prints False because 0 is False
e = [] # Ref 'e' points to empty list
print(all(e)) # prints True 











# any()  function demo program  (Home  work)
a  = [12 > 18 , 5 < 20 , 35 == 30] # Ref 'a' points to list of conditions
print(any(a)) # prints True
b = [12 > 18 , 25 < 20 , 35 == 30] # Ref 'b' points to list of conditions
print(any(b)) # prints False
c = [0 , 0.0 , '' , 25 , 0 + 0j , False] # Ref 'c' points to list 
print(any(c)) # prints True 
d = [0 , 0.0 , '' , 0 + 0j , False] # Ref 'd' points to list
print(any(d)) # prints False
e = []  # Ref 'e' points to list
print(any(e)) #  prints True









# del  operator  demo  program (Home  work)
a = [10 , 20 , 15 , 18] # Ref 'a' points to list 
print(a) # prints [10, 20, 15, 18]
del  a[2]  # deletes element at index 2 in list 'a'
print(a) # prints list i.e., [10, 20, 18]
del  a[3] # Error because there is no index 3
del a # deletes object 'a'
print(a) # Error because 'a' is not defined and already deleted










#  append()  method  demo  program (Home  work)
list = [10 , 20 , 15 , 18] # list points to list of 4 elements
print(list) # prints list i.e., [10, 20, 15, 18]
list . append(19) # element 19 is inserted at the end of the list 
print(list) # prints list i.e., [10, 20, 15, 18, 19]











#  Find  outputs (Home  work)
list = [] # list points to empty list
print(list)  # prints list i.e., []
list . append(25) # inserts element 25 at the end of list 
list . append(10.8) # inserts element 10.8 at the end of list 
list . append('Hyd') # inserts element 'Hyd' at the end of list 
list . append(True) # inserts element True at the end of list 
print(list) # prints list i.e., [25, 10.8, 'Hyd', True]











# Find  outputs  (Home  work)
list = [] # list points empty list i.e., []
for x in range(0 , 50 , 10): # for loop from indexes from 0 to 49 in steps of 10
	list . append(x) 
print(list) # prints list i.e., [0, 10, 20, 30, 40]










#  Find  outputs  (Home  work)
a = [10 , 20 , 30] # Ref 'a' points to list of 3 elements
a . append('Hyd') # inserts 'Hyd' at the end of list 'a'
print(a) # prints 'a' i.e., [10, 20, 30, 'Hyd']
print(len(a)) # prints number of elements in the list 'a' i.e., 4
print(a[3]) # How to print 4th element of list 'a'
print(a[3][0]) # How to print 'H'
print(a[3][1]) # How to print 'y'
print(a[3][2]) # How to print 'd'
      









# remove()  method  demo  program  (Home  work)
try:
	list = [10 , 20 , 15 , 18 , 15 , 12 , 15 , 19] # Ref 'list' points to list of 8 elements
	list . remove(15) # removes first occurence of element 15 from list 
	print(list) # prints modified list i.e., [10, 20, 18, 15, 12, 15, 19]
	list . remove(25) # Error because element 25 is not present in list
except:
	print('25  is   not  in  the  list') # prints this statement when given element is not present in the list













'''
Write  a  program  to  delete  'all'  occurences  of  'x'  from  the  list

Let  1st  input  be   [10 , 20 , 15 , 18 , 19 , 15 , 17 , 20 , 15 , 14]  and
2nd  input  be  15
What  is  the  output ?  ---> [10, 20,  18, 19, 17, 20, 14]

Enter List  :  [10 , 20 , 15 , 18 , 19 , 15 , 17 , 20 , 15 , 14]
Enter  element  to  be  deleted : 15
List  without   15's :  [10, 20, 18, 19, 17, 20, 14]
'''

a = eval(input("Enter any list:"))
b = eval(input("Enter element to be deleted:"))
while b in a:
	a.remove(b)
print(a)

'''
Outputs:

Enter any list:[10 , 20 , 15 , 18 , 19 , 15 , 17 , 20 , 15 , 14]
Enter element to be deleted:15
[10, 20, 18, 19, 17, 20, 14]
'''








# clear() method  demo program  (Home  work)
list = [10 , 20 , 15 , 18] # list points to list of 4 elements 
print(list) # prints list i.e., [10, 20, 15, 18]
list . clear() # deletes all elements of the list and becomes empty list
print(list) # prints empty list i.e., []










# reverse()  method  demo  program (Home  work)
a = [10 , 20 , 15 , 18] # Ref 'a' points list of 4 elements
print(a) # prints list 'a' i.e., [10, 20, 15, 18]
a . reverse() # replaces the elements in reverse
print(a) # prints reversed list i.e., [18, 15, 20, 10]









#  sort()  method  demo  program (Home  work)
list = [10 , 20 , 15 , 18 , 5] # list points to list of 5 elements
print(list) # prints list i.e., [10, 20, 15, 18, 5]
list . sort() # list is sorted
print(list) # prints sorted list i.e., [5, 10, 15, 18, 20]
list . sort(reverse = True) # list is sorted in descending order 
print(list) # prints sorted in descending order i.e., [20, 18, 15, 10, 5]










# Find  outputs (Home  work)
a = ['Rama' , 'Rajesh' , 'Amar' ,  'Sita' ,  'Vamsi' , 'Kiran' , 'Rama  Rao'] # Ref 'a' points to list of 7 elements
print(a) # prints 'a' ['Rama' , 'Rajesh' , 'Amar' ,  'Sita' ,  'Vamsi' , 'Kiran' , 'Rama  Rao']
a . sort() # list 'a' is sorted in ascending order
print(a) # prints sorted list 'a' i.e., ['Amar', 'Kiran', 'Rajesh', 'Rama', 'Rama Rao', 'Sita', 'Vamsi']
a . sort(reverse = True) # list 'a' is sorted in descending order
print(a) # prints sorted list 'a' i.e., ['Vamsi', 'Sita', 'Rama Rao', 'Rama', 'Rajesh', 'Kiran', 'Amar']












# Identify  error (Home  work)
a = [25 , 10.8 ,  'Hyd' ,  True] # Ref 'a' points to list
a . sort() # list with sequences and string cannot be sorted










#  count()  method  demo    program (Home  work)
a = [10 , 20 , 15 , 18 , 15 , 12 , 14 , 15 , 19] # Ref 'a' points to list of 9 elements
print(a . count(15)) # prints number of times 15 occured in list i.e., 3
print(a . count(25)) # prints 0
print(len(a)) # prints number of elements in the list 'a' i.e., 9












'''
Tricky  program
Write  a  program  to  remove  all  duplicate  elements  of  the  list  (Not  even  single  occurance)
Let  input  be  [10 , 20 , 15 , 10 , 14 , 10 , 18 , 20 , 19]
What  is  the  output ?  ---> [15 , 14 , 18 , 19]

Hint:  Use  count()  and  append() methods
'''

a = eval(input("Enter any list:"))
b = []
for i in a:
    c = a.count(i)
    if c == 1:
        b.append(i)
print(b)

'''
Outputs:  

Enter any list:[10 , 20 , 15 , 10 , 14 , 10 , 18 , 20 , 19]
[15, 14, 18, 19]
'''

    







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

3) Hint: Use len() and count()

Enter any list : [25,25,25,25]
All the list elements are identical

Enter any list : [10,10,20,10]
List elements are not identical
'''

a = eval(input("Enter any list:"))
for i in a:
    if a.count(i) != len(a):
        print("List elements are not identical")
        break   
else:
    print("All the list elements are identical")

'''
Outputs:

Enter any list:[25, 25, 25, 25]
All the list elements are identical

Enter any list:[25, 10, 25, 25]
List elements are not identical
'''








# index()  method  demo  program  (Home  work)
a = [10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25]
#    0    1    2    3    4    5    6    7    8    9    10
try:
	i = a . index(15) 
	while  True:
		print(i)
		i = a . index(15 , i + 1)
except:
	print(F'15  is  found  {a . count(15)}  times ')
	
'''
Outputs:
2
5
8
15  is  found  3  times
'''
