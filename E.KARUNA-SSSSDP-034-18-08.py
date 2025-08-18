 #  len()  function demo   program  (Home  work)
a = [ 25, 10.8, 'Hyd', True]
print(len(a)) #4
b = []
print(len(b)) #0
c = [[10 , 20] , 30 , 40]
print(len(c)) #3
# sum()  function  demo  program  (Home  work)
a = [25 , 10.8 , True]
print(sum(a))#36.8
b= [3 + 4j , 5 + 6j]#(8+10j)
print(sum(b)) 
c = [25 , 10.8 , True , 3 + 4j , False]
print(sum(c)) #(39.8+4j)
d = [10 , 20 , 15 , 18]
print(sum(d)) #63
e = [25 , 10.8 , 'Hyd' , True]
#print(sum(e)) #error unsupported operand
#  Find  outputs
a = [[10 , 20 , 15 , 18]]
#print(sum(a))
print(sum(a[0]))
#print(sum(for x in a[0]))
# max()  and  min()  functions  demo  program  (Home  work)
a = [10 , 20 , 15 , 18 , 30, 5 , 12]
print(max(a))#30
print(min(a))#5
b = ['Rama' , 'Sita' , 'Rajesh' , 'Kiran' , 'Amar' , 'Vamsi' , 'Manohar']
print(max(b))#vamsi
print(min(b))#amar
c = [25 , 10.8 ,  3 + 4j , True]
print(max(c)) #error
d = [25 , '35']
print(max(d)) #error
print(max([])) #error due to max()iterable arugument is empty
print(min([]))#error due to min()iterable arugument is empty 
#  Find  outputs (Home  work)
a = range(4 , 10 , 2)
b = list(a)
print(b) #[4,6,8]
print(type(b))#<class 'list'>
a = list('Vamsi')
print(a)#[v,a,m,s,i]
a = list()
print(a) #[]
print(list(25)) #error
print(list(10.8))#error
print(list(True))#error
print(list(None))#error
# Find  outputs (Home  work)
a = ((10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90))
print(list(a)) #[(10,20),(30,40,50),(60,70,80,90)]
b = { (10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90)}
print(list(b))#[(30,40,50),(60,70,80,90),(10,20)]
c = ([10 , 20] , (30 , 40) , {50 , 60})
print(list(c))#[[10.20],(30,40),{50,60}]
# Find  outputs  (Home  work)
a = ['Rama',  'Rajesh',  'Amar',  'Sita',  'Vamsi'  ,  'Kiran'  , 'Rama  Rao']
b = sorted(a)
print(b)#['Amar','kiran','rajesh','rama','rama rao','sita','vamsi]]
c = sorted(a , reverse = True)
print(c)#['vamsi','sita','rama rao','rajesh','kiran','amar']
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
print(a) #[10,20,15,18]
del  a[2] # 15 is deleted from the list
print(a)#[10,20,18]
del  a[3] #18 is deleted from list
del  a #list is deleted
print(a) #error due to no object
#  append()  method  demo  program (Home  work)
list = [10 , 20 , 15 , 18]
print(list)#[10,20,15,18]
list . append(19)
print(list)#[10,20,15,18,19]
#  Find  outputs (Home  work)
list = []
print(list)#empty list
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
print(a)#[10,20,30]
print(len(a))#3
print(How  to  print  4th  element  of  list  'a')#print(a[3])
print(How  to  print  'H')#print(a[3][0])
print(How  to  print  'y')#print(a[3][1])
print(How  to  print  'd')#print(a[3][2])
# remove()  method  demo  program  (Home  work)
try:
	list = [10 , 20 , 15 , 18 , 15 , 12 , 15 , 19]
	list . remove(15)
	print(list)#[10,20,18,15,12,15,19]
	list . remove(25)#error and except suite is executed due 25 is not found in the list
except:
	print('25  is   not  in  the  list')
	'''
Write  a  program  to  delete  'all'  occurences  of  'x'  from  the  list

Let  1st  input  be   [10 , 20 , 15 , 18 , 19 , 15 , 17 , 20 , 15 , 14]  and
2nd  input  be  15
What  is  the  output ?  ---> [10 , 20 ,  18 , 19 , 17 , 20 , 14]
'''
a=eval(input('enter a list:'))
x=eval(input('enter element to be deleted:'))
for i  in a:
	if i==x:
		a.remove(x)
		print(a)
# clear() method  demo program  (Home  work)
list = [10 , 20 , 15 , 18]
print(list)#[10,20,15,18]
list . clear()
print(list)#[]
# reverse()  method  demo  program (Home  work)
a = [10 , 20 , 15 , 18]
print(a)#[10,20,15,18]
a . reverse()
print(a)#[18,15,20,10]
#  sort()  method  demo  program (Home  work)
list = [10 , 20 , 15 , 18 , 5]
print(list)#[10,20,15,18,5]
list . sort()
print(list)#[5,10,15,18,20]
list . sort(reverse = True)
print(list)#[20,18,,15,10,5]
#  count()  method  demo    program (Home  work)
a = [10 , 20 , 15 , 18 , 15 , 12 , 14 , 15 , 19]
print(a . count(15))#3
print(a . count(25))#0
print(len(a))#9
# index()  method  demo  program  (Home  work)
a = [10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25]
#     0     1     2    3    4     5    6    7     8    9    10
try:
	i = a . index(15)# find first occurrence of 15
	while  True:
		print(i)#print index where 15 is found
		i = a . index(15 , i + 1)# find next occurrence after index
except:
	print(F'15  is  found  {a . count(15)}  times ')
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

3) Hint: Use  len()  and  count()
'''
a = eval(input('Enter any list: '))

total_elements = len(a)
count_first = a.count(a[0])

if count_first == total_elements:
    print('All elements are identical')
else:
    print('All elements are not identical')

