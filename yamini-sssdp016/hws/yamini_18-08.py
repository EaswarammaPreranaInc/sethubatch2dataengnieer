#  len()  function demo   program  (Home  work)
a = [ 25, 10.8, 'Hyd', True]
print(len(a)) # returns the number of elements in list a i.e 4
b = []
print(len(b)) # number of elements in list b is 0 so len is 0
c = [[10 , 20] , 30 , 40]
print(len(c)) # we have 3 objects in c so len is 3


# sum()  function  demo  program  (Home  work)
a = [25 , 10.8 , True]
print(sum(a)) # sum of 3 elements 25+10.8+1=36.8
b= [3 + 4j , 5 + 6j]
print(sum(b)) # adding 2 complex numbers 8+10j
c = [25 , 10.8 , True , 3 + 4j , False]
print(sum(c)) # 25+10.8+1+3+4j+0=39.8+4j
d = [10 , 20 , 15 , 18]
print(sum(d)) # 10+20+15+18=53
e = [25 , 10.8 , 'Hyd' , True]
print(sum(e)) # error as we cant add integers to string

#  Find  outputs
a = [[10 , 20 , 15 , 18]]
print(sum(a)) # error as a has only one element it is a list
print(sum(a[0])) # How  to  determine  sum  of  inner  list  elements)
#How  to  determine  sum  of  inner  list  elements  in  another  way
[b,c,d,e]=a[0]
f=[b,c,d,e]
print(sum(f))

# max()  and  min()  functions  demo  program  (Home  work)
a = [10 , 20 , 15 , 18 , 30, 5 , 12]
print(max(a)) # prints the max element of the list i.e 30
print(min(a)) # prints the min element of the list i.e 5
b = ['Rama' , 'Sita' , 'Rajesh' , 'Kiran' , 'Amar' , 'Vamsi' , 'Manohar']
print(max(b))  # 1st non matching character is compared vamsi
print(min(b))  # amar
c = [25 , 10.8 ,  3 + 4j , True]
print(max(c)) # error because we cant compare complex wit int
d = [25 , '35']
print(max(d)) # error because we cant compare string with int
print(max([])) # error as there are no elements in the empty list to compare
print(min([])) # error as there are no elements in the empty list to compare

# list()  function  demo  program
a = (10 , 20 , 15, 18)
b = list(a) # converts the tuple to list
print(b) # [10,20,15,18]
print(type(b)) # class list
print(a  is  b) # false because both a and b are not pointing to same object
print(a == b) # false

a = range(4 , 10 , 2)
b = list(a)  # converts the range object to list 
print(b) # [4,6,8]
print(type(b)) # class list
a = list('Vamsi') # converts the string to list of characters 
print(a) #['v','a','m','s','i']
a = list() # empty list
print(a) #[]
print(list(25))# error as the argument of list function should be sequence
print(list(10.8)) # error as the argument of list function should be sequence
print(list(True))# error as the argument of list function should be sequence
print(list(None)) # error as the argument of list function should be sequence

a = ((10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90))
print(list(a)) # converts the outer tuple to list [(10, 20), (30, 40, 50), (60, 70, 80, 90)]
b = { (10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90)}
print(list(b)) # converts the outer set to list [(30, 40, 50), (60, 70, 80, 90), (10, 20)]
c = ([10 , 20] , (30 , 40) , {50 , 60})
print(list(c)) # converts the outer list to list [[10, 20], (30, 40), {50, 60}]

# sorted()  function   demo  program
a = [10 , 20 , 15 , 5 , 12]
b = sorted(a) #  sorts the list to ascending order
print(b) # [5,10,12,15,20]
print(type(b)) # class list
c = sorted(a , reverse = True) #  sorts the list to descending order
print(c) # [20,15,12,10,5]
print(a) # [10,20,15,5,12]


a = ['Rama',  'Rajesh',  'Amar',  'Sita',  'Vamsi'  ,  'Kiran'  , 'Rama  Rao']
b = sorted(a) 
print(b) #['Amar', 'Kiran', 'Rajesh', 'Rama', 'Rama  Rao', 'Sita', 'Vamsi']
c = sorted(a , reverse = True)
print(c) # ['Vamsi', 'Sita', 'Rama  Rao', 'Rama', 'Rajesh', 'Kiran', 'Amar']
print(a) # ['Rama', 'Rajesh', 'Amar', 'Sita', 'Vamsi', 'Kiran', 'Rama  Rao']

# all()  function demo  program  (Home  work)
a = [12 > 10 , 5 < 20 , 30 == 30]
print(all(a)) # true
b = [9 >= 6 , 12 <= 9 , 6 == 6]
print(all(b)) # false
c = [25 , 10.8 , '' , True , 3+4j , 'Hyd']
print(all(c))  # false becuase all should be non 0's
d = [10 , 0 , 20]
print(all(d)) # false becuase all should be non 0's
e = []
print(all(e)) # true


a  = [12 > 18 , 5 < 20 , 35 == 30]
print(any(a))# true because one condition is true 5<20
b = [12 > 18 , 25 < 20 , 35 == 30]
print(any(b)) # false as no condition is true
c = [0 , 0.0 , '' , 25 , 0 + 0j , False]
print(any(c)) # true as one condition is true
d = [0 , 0.0 , '' , 0 + 0j , False]
print(any(d)) # false as no condition is true
e = []
print(any(e)) # false as no condition is true

a = [10 , 20 , 15 , 18]
print(a) # [10 , 20 , 15 , 18]
del    a[2] # 15 is deleted
print(a) # [10 , 20 , 18]
del  a[3] #error  3 rd index is present
del  a # object a is deleted 
print(a) # error as a is deleted

list = [10 , 20 , 15 , 18]
print(list) # [10 , 20 , 15 , 18]
list . append(19) # 19 is added at end
print(list) # [10 , 20 , 15 , 18, 19]

list = []
print(list) # empty list
list . append(25) # 25 is added at end
list . append(10.8) # 10.8 is added at end
list . append('Hyd') # 'Hyd' is added at end
list . append(True) # True is added at end
print(list) # [25,10.8,'Hyd',True]

list = []
for  x  in   range(0 , 50 , 10):
	list . append(x) # 0,10,20,30,40
print(list) #[0,10,20,30,40]

a = [10 , 20 , 30]
a . append('Hyd') # adds hyd at end
print(a) # [10 , 20 , 30, 'Hyd']
print(len(a)) # 4
print(a[3])# How  to  print  4th  element  of  list  'a')
print(a[3][0]) # How  to  print  'H') 
print(a[3][1]) # How  to  print  'y')
print(a[3][2]) # How  to  print  'd')

# remove()  method  demo  program  (Home  work)
try:
	list = [10 , 20 , 15 , 18 , 15 , 12 , 15 , 19]
	list . remove(15) # removes the 1st occurance of 15
	print(list) # [10 , 20 , 18 , 15 , 12 , 15 , 19]
	list . remove(25) # error as there is no 25 in list so goes to except suite
except:
	print('25  is   not  in  the  list') # this statement is printed

'''
Write  a  program  to  delete  'all'  occurences  of  'x'  from  the  list

Let  1st  input  be   [10 , 20 , 15 , 18 , 19 , 15 , 17 , 20 , 15 , 14]  and
2nd  input  be  15
What  is  the  output ?  ---> [10 , 20 ,  18 , 19 , 17 , 20 , 14]
'''

a=eval(input('enter a list : '))
x=int(input('enter element to be deleted : '))
try:
    for y in a:
            a.remove(x)
except:
    print(F'List without {x} s: ',a)

# clear() method  demo program  (Home  work)
list = [10 , 20 , 15 , 18]
print(list) # [10 , 20 , 15 , 18]
list . clear()# removes all the elements of the list
print(list) # empty list]

# reverse()  method  demo  program (Home  work)
a = [10 , 20 , 15 , 18]
print(a) # [10 , 20 , 15 , 18]
a . reverse() # reverses the list
print(a) # [18,15,20,10]

#  sort()  method  demo  program (Home  work)
list = [10 , 20 , 15 , 18 , 5]
print(list)  # [10 , 20 , 15 , 18 , 5]
list . sort() # sorts the list in ascending order
print(list) # [5,10,15,18,20]
list . sort(reverse = True) # sorts the list in descending order
print(list) # [20,18,15,10,5]

# Find  outputs (Home  work)
a = ['Rama' , 'Rajesh' , 'Amar' ,  'Sita' ,  'Vamsi' , 'Kiran' , 'Rama  Rao']
print(a)
a . sort()  # ascending order
print(a) # ['Amar', 'Kiran', 'Rajesh', 'Rama', 'Rama  Rao', 'Sita', 'Vamsi']
a . sort(reverse = True) # descending order
print(a) ['Vamsi', 'Sita', 'Rama  Rao', 'Rama', 'Rajesh', 'Kiran', 'Amar']

# Identify  error (Home  work)
a = [25 , 10.8 ,  'Hyd' ,  True]  
a . sort() # cant compare string with other

#  count()  method  demo    program (Home  work)
a = [10 , 20 , 15 , 18 , 15 , 12 , 14 , 15 , 19]
print(a . count(15)) # returns 3 as 15 is repeated 3 times
print(a . count(25)) # returns 0 as it 25 not fond in the list
print(len(a)) # returns 9 as there are 9 elements

'''
Tricky  program
Write  a  program  to  remove  all  duplicate  elements  of  the  list  (Not  even  single  occurance)
Let  input  be  [10 , 20 , 15 , 10 , 14 , 10 , 18 , 20 , 19]
What  is  the  output ?  ---> [15 , 14 , 18 , 19]

Hint:  Use  count()  and  append()  methods
'''
a=eval(input('enter a list: '))
b=[]
for x in a:
    if a.count(x)==1:
        b.append(x)
print(b)
    
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

3) Hint: Use  len()  and  count()
'''

a=eval(input('enter a list: '))
if(len(a)==a.count(a[0])):
    print('All  the  list  elements are identical')
else:
    print('List  elements are not identical')

 
# index()  method  demo  program  (Home  work)
a = [10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25]
#     0     1     2    3    4     5    6    7     8    9    10
try:
	i = a . index(15) # initial occurance of 15 is at 2
	while  True:
		print(i)
		i = a . index(15 , i + 1) # 8,15
except:
	print(F'15  is  found  {a . count(15)}  times ') # 3 times


