
# len()  function demo   program  (Home  work)

a = [ 25, 10.8, 'Hyd', True]
print(len(a))# output: 4
b = []
print(len(b))# output: 0
c = [[10 , 20] , 30 , 40]
print(len(c))# output: 3




# sum()  function  demo  program  (Home  work)

a = [25 , 10.8 , True]
print(sum(a))# output: 36.8
b= [3 + 4j , 5 + 6j]
print(sum(b))# output: (8+10j)
c = [25 , 10.8 , True , 3 + 4j , False]
print(sum(c))# output: (39.8+4j)
d = [10 , 20 , 15 , 18]
print(sum(d))# output: 63
e = [25 , 10.8 , 'Hyd' , True]
print(sum(e))# Error as we cannot add string element to non sequence elements



# Find  outputs

a = [[10 , 20 , 15 , 18]]
print(sum(a))# error we cannot add list with empty list
print((How  to  determine  sum  of  inner  list  elements))
print(sum(a[0]))# output: 63
print(How  to  determine  sum  of  inner  list  elements  in  another  way)



# max()  and  min()  functions  demo  program  (Home  work)

a = [10 , 20 , 15 , 18 , 30, 5 , 12]
print(max(a))# output: 30
print(min(a))# output: 5
b = ['Rama' , 'Sita' , 'Rajesh' , 'Kiran' , 'Amar' , 'Vamsi' , 'Manohar']
print(max(b))# output: Vamshi
print(min(b))# output: Amar
c = [ 3 + 4j , 4+5j]
print(max(c))# Error as '>' not supported for complex numbers
d = [25 , '35']
print(max(d))# Error as '>' not supported between string and integer
print(max([]))# Error as max() argument cannot be empty
print(min([]))# Error as min() argument cannot be empty



# list()  function  demo  program

a = (10 , 20 , 15, 18)
b = list(a)
print(b)# output: [10 , 20 , 15, 18]
print(type(b))# output: <class 'list'>
print(a  is  b)# output: False
print(a == b)# output: False



#  Find  outputs (Home  work)

a = range(4 , 10 , 2)
b = list(a)
print(b)# output: [4,6,8]
print(type(b))# output: <class 'list'>
a = list('Vamsi')
print(a)# output: ['V','a','m','s','i']
a = list()
print(a)# output: empty list [] 
print(list(25)) # list(non-sequence) throws error
print(list(10.8))# list(non-sequence) throws error
print(list(True))# list(non-sequence) throws error
print(list(None))# list(non-sequence) throws error



# Find  outputs (Home  work)

a = ((10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90))
print(list(a))# output: [(10, 20), (30, 40, 50), (60, 70, 80, 90)]
b = { (10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90)}
print(list(b))# output: [(30, 40, 50), (60, 70, 80, 90), (10, 20)]
c = ([10 , 20] , (30 , 40) , {50 , 60})
print(list(c))# output: [[10, 20], (30, 40), {50, 60}]



# sorted()  function   demo  program

a = [10 , 20 , 15 , 5 , 12]
b = sorted(a)
print(b)# output: [5, 10, 12, 15, 20]
print(type(b))# output: <class 'list'>
c = sorted(a , reverse = True)
print(c)# output: [20, 15, 12, 10, 5]
print(a)# output: [10, 20, 15, 5, 12]



#  Find  outputs  (Home  work)

a = ['Rama',  'Rajesh',  'Amar',  'Sita',  'Vamsi'  ,  'Kiran'  , 'Rama  Rao']
b = sorted(a)
print(b)# output: ['Amar', 'Kiran', 'Rajesh', 'Rama', 'Rama  Rao', 'Sita', 'Vamsi']
c = sorted(a , reverse = True)
print(c)# output: ['Vamsi', 'Sita', 'Rama  Rao', 'Rama', 'Rajesh', 'Kiran', 'Amar']
print(a)# output: ['Rama', 'Rajesh', 'Amar', 'Sita', 'Vamsi', 'Kiran', 'Rama  Rao']



# all()  function demo  program  (Home  work)

a = [12 > 10 , 5 < 20 , 30 == 30]
print(all(a))# output: True
b = [9 >= 6 , 12 <= 9 , 6 == 6]
print(all(b))# output: False
c = [25 , 10.8 , '' , True , 3+4j , 'Hyd']
print(all(c))# output: False
d = [10 , 0 , 20]
print(all(d))# output: False
e = []
print(all(e))# output: True



#  any()  function demo program  (Home  work)

a  = [12 > 18 , 5 < 20 , 35 == 30]
print(any(a))# output: True
b = [12 > 18 , 25 < 20 , 35 == 30]
print(any(b))# output: False
c = [0 , 0.0 , '' , 25 , 0 + 0j , False]
print(any(c))# output: True
d = [0 , 0.0 , '' , 0 + 0j , False]
print(any(d))# output: False
e = []
print(any(e))# output: False



#  del  operator  demo  program (Home  work)

a = [10 , 20 , 15 , 18]
print(a)# output: [10 , 20 , 15 , 18]
del    a[2]
print(a)# output: [10,20,18]
del  a[3]# Error as index out of range
del  a # deletes object 'a'
print(a)# Error as there is no object of 'a'




# append()  method  demo  program (Home  work)

list = [10 , 20 , 15 , 18]
print(list)# output: [10,20,15,18]
list . append(19)
print(list)# output: [10,20,15,18,19]



# Find  outputs (Home  work)

list = []
print(list)# output: []
list . append(25) #[25]
list . append(10.8)#[25, 10.8]
list . append('Hyd')#[25, 10.8, 'Hyd']
list . append(True)#[25, 10.8, 'Hyd', True]
print(list)# output: [25, 10.8, 'Hyd', True]



# Find  outputs  (Home  work)

list = []
for  x  in   range(0 , 50 , 10):
	list . append(x)
print(list)# output: [0, 10, 20, 30, 40]



# Find  outputs  (Home  work)

a = [10 , 20 , 30]
a . append('Hyd')
print(a)# output: [10,20,30,'Hyd']
print(len(a))# output: 4
print(a[3])# output: Hyd   #How  to  print  4th  element  of  list  'a'
print(a[3][0])# output: H  #How  to  print  'H'
print(a[3][1])# output: y  #How  to  print  'y'
print(a[3][2])# output: d  #How  to  print  'd'



#  remove()  method  demo  program  (Home  work)

try:
	list = [10 , 20 , 15 , 18 , 15 , 12 , 15 , 19]
	list . remove(15)
	print(list)
	list . remove(25)
except:
	print('25  is   not  in  the  list')

'''
# output:
[10,20,18,15,12,15,19]
25  is   not  in  the  list
'''



'''Write  a  program  to  delete  'all'  occurences  of  'x'  from  the  list
Let  1st  input  be   [10 , 20 , 15 , 18 , 19 , 15 , 17 , 20 , 15 , 14]  and
2nd  input  be  15
What  is  the  output ?  ---> [10 , 20 ,  18 , 19 , 17 , 20 , 14]
'''

n = eval(input("Enter any list: "))
b = eval(input("Enter the element to be deleted: "))
while b in n:
    n.remove(b) # Modifies the existing list by removing the 1st occurance of the desired element
print(f"List without {b}'s: {n}")

'''
output:
Enter List  :  [10 , 20 , 15 , 18 , 19 , 15 , 17 , 20 , 15 , 14]
Enter  element  to  be  deleted : 15
List  without   15's :  [10, 20, 18, 19, 17, 20, 14]
'''



# clear() method  demo program  (Home  work)

list = [10 , 20 , 15 , 18]
print(list)# output: [10 , 20 , 15 , 18]
list . clear()
print(list)# output: []




# reverse()  method  demo  program (Home  work)

a = [10 , 20 , 15 , 18]
print(a)# output: [10, 20, 15, 18]
a . reverse()
print(a)# output: [18, 15, 20, 10]



# sort()  method  demo  program (Home  work)

list = [10 , 20 , 15 , 18 , 5]
print(list)# output: [10 , 20 , 15 , 18 , 5]
list . sort()
print(list)# output: [5, 10, 15, 18, 20]
list . sort(reverse = True)
print(list)# output: [20, 18, 15, 10, 5]



# Find  outputs (Home  work)

a = ['Rama' , 'Rajesh' , 'Amar' ,  'Sita' ,  'Vamsi' , 'Kiran' , 'Rama  Rao']
print(a)# output: ['Rama', 'Rajesh', 'Amar', 'Sita', 'Vamsi', 'Kiran', 'Rama  Rao']
a . sort()
print(a)# output: ['Amar', 'Kiran', 'Rajesh', 'Rama', 'Rama  Rao', 'Sita', 'Vamsi']
a . sort(reverse = True)
print(a)# output: ['Vamsi', 'Sita', 'Rama  Rao', 'Rama', 'Rajesh', 'Kiran', 'Amar']




#  Identify  error (Home  work)
a = [25 , 10.8 ,  'Hyd' ,  True]
a . sort()# output: sort() is not supported between sequence and non-sequence




#  count()  method  demo    program (Home  work)
a = [10 , 20 , 15 , 18 , 15 , 12 , 14 , 15 , 19]
print(a . count(15))# output: 3
print(a . count(25))# output: 0
print(len(a))# output: 9



''' Tricky  program
Write  a  program  to  remove  all  duplicate  elements  of  the  list  (Not  even  single  occurance)
Let  input  be  [10 , 20 , 15 , 10 , 14 , 10 , 18 , 20 , 19]
What  is  the  output ?  ---> [15 , 14 , 18 , 19]

Hint:  Use  count()  and  append()  methods
'''
n = eval(input("Enter any list: "))
b =[]
for i in range(len(n)):
    if n.count(n[i]) == 1:
        b.append(n[i])
print(b)

'''output
Enter any list: [10 , 20 , 15 , 10 , 14 , 10 , 18 , 20 , 19]
[15, 14, 18, 19]
'''




'''  Write  a  program  to  determine  all  the  list  elements  are  identical  or  not

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
n = eval(input("Enter any list: "))
if n.count(n[0]) == len(n):
    print("All  the  list  elements  are  identical")
else:
    print("List  elements  are  not  identical")

'''
Enter  any  list  :  [25,25,25,25]
All  the  list  elements  are  identical
 Enter  any  list  :  [10,10,20,10]
List   elements  are  not  identical
'''




#  index()  method  demo  program  (Home  work)
a = [10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25]
#     0   1    2    3    4    5    6    7    8    9   10
try:
	i = a . index(15)
	while  True:
		print(i)
		i = a . index(15 , i + 1)
except:
	print(F'15 is found {a . count(15)} times ')

'''
# output:
2
5
8
15  is  found  3 times 
'''
