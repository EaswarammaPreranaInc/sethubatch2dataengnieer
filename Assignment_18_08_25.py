'''#  len()  function demo   program  (Home  work)
a = [ 25, 10.8, 'Hyd', True]
print(len(a))#4
b = []
print(len(b))#0
c = [[10 , 20] , 30 , 40]
print(len(c))#3

# sum()  function  demo  program  (Home  work)
a = [25 , 10.8 , True]
print(sum(a))#36.8
b= [3 + 4j , 5 + 6j]
print(sum(b))#(8+10j)
c = [25 , 10.8 , True , 3 + 4j , False]
print(sum(c))#(39.8+4j)
d = [10 , 20 , 15 , 18]
print(sum(d))#63
e = [25 , 10.8 , 'Hyd' , True]
print(sum(e))#error

#  Find  outputs
a = [[10 , 20 , 15 , 18]]
#print(sum(a))#Error
print(sum(a[0]))#63
print(sum([x for x in a[0]]))   # Output: 63

# max()  and  min()  functions  demo  program  (Home  work)
a = [10 , 20 , 15 , 18 , 30, 5 , 12]
print(max(a))#30
print(min(a))#5
b = ['Rama' , 'Sita' , 'Rajesh' , 'Kiran' , 'Amar' , 'Vamsi' , 'Manohar']
print(max(b))#Vamsi
print(min(b))#Amar
c = [25 , 10.8 ,  3 + 4j , True]
print(max(c))#error
d = [25 , '35']
print(max(d))#error
print(max([]))#error
print(min([]))#error

# list()  function  demo  program
a = (10 , 20 , 15, 18)
b = list(a)
print(b)#[10,20,15,18]
print(type(b))#<class list>
print(a  is  b)#False
print(a == b)#False

#  Find  outputs (Home  work)
a = range(4 , 10 , 2)
b = list(a)
print(b)#[4,6,8]
print(type(b))#<class list>
a = list('Vamsi')
print(a)#['V','a','m','s','i,]
a = list()
print(a)#[]
print(list(25))#error
print(list(10.8))#error
print(list(True))#error
print(list(None))#error

# Find  outputs (Home  work)
a = ((10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90))
print(list(a))#[(10,20),(30,40,50),(60,70,80,90)]
b = { (10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90)}
print(list(b))#[(10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90)]
c = ([10 , 20] , (30 , 40) , {50 , 60})
print(list(c))#[[10 , 20] , (30 , 40) , {50 , 60}]

# sorted()  function   demo  program
a = [10 , 20 , 15 , 5 , 12]
b = sorted(a)
print(b)#[5,10,12,15,20]
print(type(b))#<class list>
c = sorted(a , reverse = True)
print(c)#[20,15,12,10,5]
print(a)#[10 , 20 , 15 , 5 , 12]

# Find  outputs  (Home  work)
a = ['Rama',  'Rajesh',  'Amar',  'Sita',  'Vamsi'  ,  'Kiran'  , 'Rama  Rao']
b = sorted(a)
print(b)##['Amar','Kiran','Rajesh', 'Rama','Rama Rao','Sita','Vamsi']
c = sorted(a , reverse = True)
print(c)#['Vamsi', 'Sita', 'Rama  Rao', 'Rama', 'Rajesh', 'Kiran', 'Amar']
print(a)#['Rama',  'Rajesh',  'Amar',  'Sita',  'Vamsi'  ,  'Kiran'  , 'Rama  Rao']


# all()  function demo  program  (Home  work)
a = [12 > 10 , 5 < 20 , 30 == 30]
print(all(a))#True
b = [9 >= 6 , 12 <= 9 , 6 == 6]
print(all(b))#False
c = [25 , 10.8 , '' , True , 3+4j , 'Hyd']
print(all(c))#False
d = [10 , 0 , 20]
print(all(d))#False
e = []
print(all(e))#True

# any()  function demo program  (Home  work)
a  = [12 > 18 , 5 < 20 , 35 == 30]
print(any(a))#True
b = [12 > 18 , 25 < 20 , 35 == 30]
print(any(b))#False
c = [0 , 0.0 , '' , 25 , 0 + 0j , False]
print(any(c))#True
d = [0 , 0.0 , '' , 0 + 0j , False]
print(any(d))#False
e = []
print(any(e))#False

# del  operator  demo  program (Home  work)
a = [10 , 20 , 15 , 18]
print(a)#[10 , 20 , 15 , 18]
del    a[2]
print(a)#[10 , 20 , 18]
#del  a[3]#error
del  a
print(a)#error

#  append()  method  demo  program (Home  work)
list = [10 , 20 , 15 , 18]
print(list)#[10 , 20 , 15 , 18]
list . append(19)
print(list)#[10 , 20 , 15 , 18,19]

#  Find  outputs (Home  work)
list = []
print(list)#[]
list . append(25)
list . append(10.8)
list . append('Hyd')
list . append(True)
print(list)#[25,10.8,'Hyd',True]

# Find  outputs  (Home  work)
list = []
for  x  in   range(0 , 50 , 10):
	list . append(x)
print(list)#[0,10,20,30,40]

#  Find  outputs  (Home  work)
a = [10 , 20 , 30]
a . append('Hyd')
print(a)#[10,20,30,'Hyd']
print(len(a))#4
print(a[3][0])#H
print(a[3][1])#y
print(a[3][2])#d

# remove()  method  demo  program  (Home  work)
try:
	list = [10 , 20 , 15 , 18 , 15 , 12 , 15 , 19]
	list . remove(15)
	print(list)#[10 , 20, 18 , 15 , 12 , 15 , 19]
	list . remove(25)#'25  is   not  in  the  list'
except:
	print('25  is   not  in  the  list')'''

'''
Write  a  program  to  delete  'all'  occurences  of  'x'  from  the  list

Let  1st  input  be   [10 , 20 , 15 , 18 , 19 , 15 , 17 , 20 , 15 , 14]  and
2nd  input  be  15
What  is  the  output ?  ---> [10 , 20 ,  18 , 19 , 17 , 20 , 14]

list1=eval(input("Enter the elemenst of list:"))
e=eval(input("Enter the element to be removed:"))
for i in list1:
    if i==e:
      (list1.remove(i))
print(list1)
output:
Enter the elements of list: [10,20,15,14,16,17,15,18,19,15,22,25]
Enter the element to be removed: 15
[10, 20, 14, 16, 17, 18, 19, 22, 25]

# clear() method  demo program  (Home  work)
list = [10 , 20 , 15 , 18]
print(list)# [10 , 20 , 15 , 18]
list . clear()
print(list)#[]

# reverse()  method  demo  program (Home  work)
a = [10 , 20 , 15 , 18]
print(a)#[10,20,15,18]
a . reverse()
print(a)#[18,15,20,10]

#  sort()  method  demo  program (Home  work)
list = [10 , 20 , 15 , 18 , 5]
print(list)#[10 , 20 , 15 , 18 , 5]
list . sort()
print(list)#[5,10,15,18,20]
list . sort(reverse = True)
print(list)#[20,18,15,10,5]


# Find  outputs (Home  work)
a = ['Rama' , 'Rajesh' , 'Amar' ,  'Sita' ,  'Vamsi' , 'Kiran' , 'Rama  Rao']
print(a)#['Rama' , 'Rajesh' , 'Amar' ,  'Sita' ,  'Vamsi' , 'Kiran' , 'Rama  Rao']
a . sort()
print(a)#['Amar','Kiran','Rajesh','Rama','Rama Rao','Sita','Vamsi']
a . sort(reverse = True)
print(a)#['Vamsi','Sita','Rama Rao','Rama','Rajesh','Kiran','Amar']

# Identify  error (Home  work)
a = [25 , 10.8 ,  'Hyd' ,  True]
a . sort()#error

#  count()  method  demo    program (Home  work)
a = [10 , 20 , 15 , 18 , 15 , 12 , 14 , 15 , 19]
print(a . count(15))#3
print(a . count(25))#0
print(len(a))#9


Tricky  program
Write  a  program  to  remove  all  duplicate  elements  of  the  list  (Not  even  single  occurance)
Let  input  be  [10 , 20 , 15 , 10 , 14 , 10 , 18 , 20 , 19]
What  is  the  output ?  ---> [15 , 14 , 18 , 19]

Hint:  Use  count()  and  append()  methods


# Program to remove all duplicate elements (not even single occurrence)

lst = eval(input("Enter list of Elements:"))
result = []

for item in lst:
    if lst.count(item) == 1:   # keep only if it occurs once
        result.append(item)

print("Output list:", result)
output:
Enter list of Elements:[10, 20, 15, 10, 14, 10, 18, 20, 19]
Output list: [15, 14, 18, 19]

# Program to check if all elements in a list are identical
lst = eval(input("Enter the elements:"))
t = len(lst)
cf = lst.count(lst[0])
if cf == t:
    print("All the elements are identical")
else:
    print("All the elements are not identical")

print("How many elements are in the list ? --->", t)
print("How many times is first element repeated ? --->", cf)

output:
Enter the elements:[25,25,25,25]
All the elements are identical
How many elements are in the list ? ---> 4
How many times is first element repeated ? ---> 4

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



output:
2
5
8
15  is  found  3  times '''
    


