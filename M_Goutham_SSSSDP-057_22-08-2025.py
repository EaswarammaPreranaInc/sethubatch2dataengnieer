#index()  and  count()  methods  demo  program   (Home  work)
a = (10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25)
#     0    1      2     3    4     5     6    7     8    9    10
try:
	i = a . index(15)
	while  True:
		print('15 is found at index : ' , i)
		i = a . index(15 , i + 1)
except:
		print(F'15  is  found  {a . count(15)}  times')

'''output:
15 is found at index : 2
15 is found at index : 5
15 is found at index : 2
15 is found 3 times
'''


#  How  to  modify  an  element  of  tuple ?    (Home  work)
a  =  10 ,  20 ,  30 ,   40 ,  50
#     0      1       2       3      4
#a[2] = 35 #Error #Tuple cannot be modified because tuple is immuatble
print(a) #Returns the tuple of elements
print(id(a)) #Returns the address of tuple
#How  to  modify  30  in  tuple  to  35
a = a[:2]+(35,)+a[3:]
print(a) #Returns the modified tuple in place of 30 , 35 is added
print(id(a)) #Returns the address of new tuple



# How  to  delete  an  element  of  tuple ?   (Home  work)
a  = 10 , 20 , 30 , 40 , 50
#    0     1      2     3      4
a . remove(30) #Error #There is no remove method in tuple
del  a[2] #Error #we cannot delete the element in the tuple
a . pop(2) #Error #There is no pop method in tuple
print(a) #Returns the tuple a i.e (10 , 20 , 30 , 40 , 50)
print(id(a)) #Returns the address of tuple a
#How  to  remove  30  from  tuple  'a'
#We can remove element from tuple using slicing 
a = a[:2]+a[3:] #Here we are concatinating the two tuple elements
print(a) #Returns the modified tuple
print(id(a)) #Returns the address of tuple a




#  Nested   tuple  (Home  work)
a = ( (10 , 20)  ,  (30 , 40 , 50)  ,  (60 , 70 , 80 , 90) ) #Reference a points to a nested tuple 
print(a) #Returns the nested tuple i.e ((10 , 20),  (30 , 40 , 50),  (60 , 70 , 80 , 90))
print(type(a)) #Returns the type i.e <class 'tuple'>
print(len(a)) #Returns the length of tuple i.e 3 
#How  to  print  1st  inner  tuple
print(a[0])
#How  to  print  2nd  inner  tuple
print(a[1])
#How  to  print  3rd  inner  tuple
print(a[2])
#How  to  print  20
print(a[0][1])
#How  to  print  50
print(a[1][2])
#How  to  print  90
print(a[2][3]) 



# Find  outputs  (Home  work)
a = ((10 , 20 , 30),) #Reference a points to tuple object
#(How  to   print  inner  tuple)
print(a[0])
#(How  to   print  inner  tuple  in  another  way)
print(*a)
#(How   to  print   10)
print(a[0][0])
#(How   to  print   20)
print(a[0][1])
#(How   to  print   30)
print(a[0][2])
b = ((),) #Reference b points to empty nested tuple 
#(How  to   print  inner  tuple  of  tuple  'b')
print(b[0])
#(How  to   print  inner  tuple  of  tuple  'b'  in  another  way)
print(*b)


#  Find  outputs (Home  work)
a = ((10 , 20 , 30)) #Reference a points to tuple a
print(a) #Returns the tuple i.e (10 , 20 , 30)
print(*a) #Returns the elements which are inside the tuple
b = (()) #Reference b points to an empty tuple
print(b) #Returns the empty tuple i.e ()
print(*b) #Returns the nothing as there is nothing in the tuple 


# What  are  the  outputs  if  input  is  {10 , 20 , 15 , 18 , 20 , 12 , 18}
a = input('Enter  Set  :  ') #Input function takes string as default 
print(a) #Returns the string set i.e {10 , 20 , 15 , 18 , 20 , 12 , 18}
print(type(a)) #Returns the type i.e <class 'str'>
b = eval(a) #Here string set is converted to set
print(b) #Returns the set of elements without duplicates i.e {18, 20, 10, 12, 15}
print(type(b)) #Returns the type i.e <class 'set'>



#Find  outputs  (Home  work)
print({(10 , 20 , 30)}) #Returns the set and inside the set tuple i.e  {(10 , 20 , 30)}
print({[10 , 20 , 30]}) #Error #We cannot use list in the set
print({{10 , 20 , 30}}) #Error #We cannot use set in set 
print({{}}) #Error #We cannot use dict inside a set



# How  to  print  set  in  differ net ways  (Home  work)
a = {25 , True , 'Hyd' , 10.8} #Reference a points to set of elements
print('set  with  print  function') 
print(a) #Returns the set i.e {25, 'Hyd', 10.8, True}
print('Iterate  elements  of  set  with  for  loop')
#How  to  iterate  set  with  for  loop
for i in a:
	print(i,end =' ')
	
'''output:
25 10.8 True Hyd
'''


# Find  outputs  (Home  work)
a = 'Hyd' #Reference a points to str 'Hyd'
b = True #Reference b points to bool True
c = 25 #Reference c points int object 25
d = 1 #Reference d points to int object 1
e = 'Hyd' #Reference e points to str 'Hyd' and a is deleted by PVM 
s = {a , b , c , d , e} #Reference s points to set of elements i,e set packing 
print(s) #Returns the packed set i.e { 'Hyd', True, 25} as set don't allow duplicates so it returns only 3 elements
print(len(s)) #Returns the length of set i.e 3
print(type(s)) #Returns the type i.e <class 'set'>



# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 } #Reference s points to set of elements
print(s) #Returns the set i.e {'Hyd',  25,  True,  10.8 }
a , b , c , d = s #Here set unpacking is done
print(a) #a = 'Hyd'
print(b) #a = 25
print(c) #a = True
print(d) #a = 10.8



# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 } #Reference s points to set of elements
print(s) #Returns the set i.e {'Hyd',  25,  True,  10.8 }  #order of elements may vary
a , *b = s #set unpacking i.e a = anything in the set  and b = list of 3 elements
print(a) #Anything in the set 
print(b) #Remaining elements i.e 3 elements other than a 
print(type(b)) #Returns the type i.e <class 'list'>



# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }  #Reference s points to set of elements
print(s) #Returns the set i.e {'Hyd',  25,  True,  10.8 }  #order of elements may vary
a , *b , c = s #set unpacking i.e a = an element from the set and c = an element from the set and b = list of remaining elements 
print(a) #an element from the set
print(b) #list of remaining elements
print(c) #An element from the set



# Find  outputs  (Home  work)
s = {20 , 10 , 20 , 10} #Reference s points to set of elements without duplicates
print(s) #Returns the set s in any order i.e {20 , 10}
x , y = s #Here x and y are two elements in the set which they have assigned
print(x) #one element in set
print(y) #remaining element in the set 



# set()  function  demo  program  (Home  work)
a = range(100 , 151 , 10) #Reference a points to range of elements from 100 to 150
b = set(a) #Range of elements are converted to set 
print(b) #Returns the set of elements in any order i.e {130, 100, 140, 110, 150, 120}
c = [10 , 20 , 15 , 18 , 10 , 50 , 20 , 12 , 18] #Reference c points to list of elements
d = set(c) #Reference d points to set c which is converted
print(d) #Returns the set of elements in any order
e = set('Rama  rAo') #String 'Rama  rAo' is converted to set where duplicates are removed and lower and upper case are not treated as same
print(e) #Returns the set of strings which are converted i.e {'o', 'r', 'A', 'R', 'a', 'm', ' '}
print(set(25)) #Error #int object cannot converted to set
print(set()) #Returns the empty set i.e set()


'''
set()  function
-----------------
1) What  does  set(sequence)  do ?  ---> Converts  sequence  to  set

2) What  does  set(No-args)  do ?  --->  Returns  an  empty  set

3) How  many  arguments  can  set()  function  take ?  ---> Zero  (or) One  but  not  more  than  one

4) Is  set(non-sequence)  valid ?  --->  No  becoz  argument  should  be  sequence
'''