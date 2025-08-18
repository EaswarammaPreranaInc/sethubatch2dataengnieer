# 1) len()  function demo   program  
a = [ 25, 10.8, 'Hyd', True]
print(len(a))#4
b = []
print(len(b))#0
c = [[10 , 20] , 30 , 40]
print(len(c))#3


# 2)sum()  function  demo  program  
a = [25 , 10.8 , True]
print(sum(a))#36.8
b= [3 + 4j , 5 + 6j]
print(sum(b))#(8+10j)
c = [25 , 10.8 , True , 3 + 4j , False]
print(sum(c))#(39.8+4j)
d = [10 , 20 , 15 , 18]
print(sum(d))#63
e = [25 , 10.8 , 'Hyd' , True]
#print(sum(e))#Error



# 3) Find  outputs
a = [[10 , 20 , 15 , 18]]
#print(sum(a))#Error
print(sum(a[0]))# 63 , determine  sum  of  inner  list  elements
print(sum(x for x in a[0]))# 63 ,determine  sum  of  inner  list  elements  in another way


# 4) max()  and  min()  functions  demo  program  
a = [10 , 20 , 15 , 18 , 30, 5 , 12]
print(max(a))#30
print(min(a))#5
b = ['Rama' , 'Sita' , 'Rajesh' , 'Kiran' , 'Amar' , 'Vamsi' , 'Manohar']
print(max(b))#vamsi
print(min(b))#Amar
c = [25 , 10.8 ,  3 + 4j , True]
#print(max(c))#Error because 'complex' and 'int'
d = [25 , '35']
#print(max(d))#Error because 'complex' and 'int'
#print(max([]))#Error max() arg is an empty sequence
#print(min([]))#Error min() arg is an empty sequence



# 5) list()  function  
a = (10 , 20 , 15, 18)
b = list(a)
print(b)#[10, 20, 15, 18]
print(type(b))#<class 'list'>
print(a  is  b)#False
print(a==b)#False



# 6)  Find  outputs 
a = range(4 , 10 , 2)
b = list(a)
print(b)#[4, 6, 8]
print(type(b))#<class 'list'>
a = list('Vamsi')
print(a)#['V', 'a', 'm', 's', 'i']
a = list()
print(a)#[]
#print(list(25))#Error because 'int' object is not iterable
#print(list(10.8))#Error because 'float' object is not iterable
#print(list(True))#Error because 'bool' object is not iterable
#print(list(None))#Error because 'NoneType' object is not iterable



# 7) Find  outputs 
a = ((10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90))
print(list(a))#[(10, 20), (30, 40, 50), (60, 70, 80, 90)]
b = { (10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90)}
print(list(b))#[(30, 40, 50), (60, 70, 80, 90), (10, 20)]
c = ([10 , 20] , (30 , 40) , {50 , 60})
print(list(c))#[[10, 20], (30, 40), {50, 60}]


# 8) sorted()  function   demo  program
a = [10 , 20 , 15 , 5 , 12]
b = sorted(a)
print(b)#[5, 10, 12, 15, 20]
print(type(b))#<class 'list'>
c = sorted(a , reverse = True)
print(c)#[20, 15, 12, 10, 5]
print(a)#[10, 20, 15, 5, 12]


# 9) Find  outputs  
a = ['Rama',  'Rajesh',  'Amar',  'Sita',  'Vamsi'  ,  'Kiran'  , 'Rama  Rao']
b = sorted(a)
print(b)#['Amar', 'Kiran', 'Rajesh', 'Rama', 'Rama  Rao', 'Sita', 'Vamsi']
c = sorted(a , reverse = True)
print(c)#['Vamsi', 'Sita', 'Rama  Rao', 'Rama', 'Rajesh', 'Kiran', 'Amar']
print(a)#['Rama', 'Rajesh', 'Amar', 'Sita', 'Vamsi', 'Kiran', 'Rama  Rao']


# 10) all()  function demo  program  
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


#11) any()  function demo program  
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


# 12) del  operator  demo  program 
a = [10 , 20 , 15 , 18]
print(a)#[10, 20, 15, 18]
del    a[2]
print(a)#[10, 20, 18]
#del  a[3]#Error because index 3 is out of range
#del a#Error
print(a)#[10, 20, 18]


# 13) append()  method  demo  program 
list = [10 , 20 , 15 , 18]
print(list)#[10, 20, 15, 18]
list . append(19)
print(list)#[10, 20, 15, 18, 19]


#  14) Find  outputs 
list = []
print(list)#[]
list . append(25)
list . append(10.8)
list . append('Hyd')
list . append(True)
print(list)#[25, 10.8, 'Hyd', True]


# 15) Find  outputs  
list = []
for  x  in   range(0 , 50 , 10):
	list . append(x)
print(list)#[0, 10, 20, 30, 40]


# 16) Find  outputs  
a = [10 , 20 , 30]
a . append('Hyd')
print(a)#[10, 20, 30, 'Hyd']
print(len(a))#4
print(a[3])# Hyd,    How  to  print  4th  element  of  list  'a'
print(a[3][0])# H ,How  to  print  'H'
print(a[3][1])# y  ,How  to  print  'y'
print(a[3][2])# d ,  to  print  'd'


# 17) remove()  method  demo  program  
try:
	list = [10 , 20 , 15 , 18 , 15 , 12 , 15 , 19]
	list . remove(15)
	print(list)#[10, 20, 18, 15, 12, 15, 19]
	list . remove(25)# except is executed
except:
	print('25  is   not  in  the  list')
	


#18) Write  a  program  to  delete  'all'  occurences  of  'x'  from  the  list

list=eval(input('enter list:'))# [10 , 20 , 15 , 18 , 19 , 15 , 17 , 20 , 15 , 14]        
x=eval(input( 'Enter element to be deleted:'))#15
for r in list:
	if r==x:
		list.remove(x)
print(list)#[10, 20, 18, 19, 17, 20, 14]


# 19) clear() method  demo program  
list = [10 , 20 , 15 , 18]
print(list)#[10, 20, 15, 18]
list . clear()
print(list)#[]


# 20) reverse()  method  demo  program
a = [10 , 20 , 15 , 18]
print(a)#[10, 20, 15, 18]
a . reverse()
print(a)#[18, 15, 20, 10]


# 21)  sort()  method  demo  program 
list = [10 , 20 , 15 , 18 , 5]
print(list)#[10, 20, 15, 18, 5]
list . sort()
print(list)#[5, 10, 15, 18, 20]
list . sort(reverse = True)
print(list)#[20, 18, 15, 10, 5]


# 22) Find  outputs 
a = ['Rama' , 'Rajesh' , 'Amar' ,  'Sita' ,  'Vamsi' , 'Kiran' , 'Rama  Rao']
print(a)#['Rama', 'Rajesh', 'Amar', 'Sita', 'Vamsi', 'Kiran', 'Rama  Rao']
a . sort()
print(a)#['Amar', 'Kiran', 'Rajesh', 'Rama', 'Rama  Rao', 'Sita', 'Vamsi']
a . sort(reverse =True)
print(a)#['Vamsi', 'Sita', 'Rama  Rao', 'Rama', 'Rajesh', 'Kiran', 'Amar']


# 23)Identify  error 
a = [25 , 10.8 ,  'Hyd' ,  True]
#a.sort()#Error because string and folat can't be compered


# 24) count()  method  demo    program 
a = [10 , 20 , 15 , 18 , 15 , 12 , 14 , 15 , 19]
print(a . count(15))#3
print(a . count(25))#0
print(len(a))#9




'''
25) Tricky  program
Write  a  program  to  remove  all  duplicate  elements  of  the  list  (Not  even  single  occurance)
Let  input  be  [10 , 20 , 15 , 10 , 14 , 10 , 18 , 20 , 19]
What  is  the  output ?  ---> [15 , 14 , 18 , 19]

Hint:  Use  count()  and  append()methods
'''
list = [10, 20, 15, 10, 14, 10, 18, 20, 19]
result = []
for x in list:
    if list.count(x) == 1:
        result.append(x)
print("Output=",result)#[15, 14, 18, 19]




'''
26) Write  a  program  to  determine  all  the  list  elements  are  identical  or  not

1) Let  input  be  [25 , 25 , 25 , 25]
    What  is  the  output ?  ---> All  the  elements  are  identical
    How  many  elements  are  in  the  list ?  --->  4
    How  many  times  is  first  element  repeated ?  ---> 4

2) Let  input  be  [10 , 10 , 20 ,  10]
    What  is  the  output ?  --->All  the  elements  are  not  identical
    How  many  elements  are  in  the  list ?  ---> 4
    How  many  times  is  first  element  repeated ? --->  3

3) Hint: Use  len()  and count()
'''

list = eval(input("Enter any list : "))
n = len(list)
count_first = list.count(list[0])
if n == count_first:
    print("All the list elements are identical")
else:
    print("List elements are not identical")
print("How many elements are in the list? --->", n)
print("How many times is first element repeated? --->",count_first)




# 27) index()  method  demo  program  (Home  work)
a = [10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25]
#     0     1     2    3    4     5    6    7     8    9    10
try:
	i = a . index(15)
	while  True:
		print(i)#2, 5 ,8
		i = a . index(15 , i + 1)
except:
	print(F'15  is  found  {a . count(15)}  times ')# 15 is found 3 times













