#  len()  function demo   program  (Home  work)
a = [ 25, 10.8, 'Hyd', True] 
print(len(a)) #4
b = [] #empty list
print(len(b)) #0
c = [[10 , 20] , 30 , 40] 
print(len(c)) #len 3


'''
What  does  len(list)  do ?  --->  Returns  number  of  elements  in  the  list
'''
# sum()  function  demo  program  (Home  work)
a = [25 , 10.8 , True]
print(sum(a)) #36.8
b= [3 + 4j , 5 + 6j] 
print(sum(b)) #(8+10j) tuple
c = [25 , 10.8 , True , 3 + 4j , False]
print(sum(c)) #(39.8+4j)tuple
d = [10 , 20 , 15 , 18]
print(sum(d)) #63
e = [25 , 10.8 , 'Hyd' , True]
#print(sum(e)) #string cannot be added error


'''
What  does  sum(list)  do ?  ---> Returns  sum  of  list  elements
'''
#  Find  outputs
a = [[10 , 20 , 15 , 18]]
#print(sum(a))  #63 #type error
print(sum(a[0])) #using direct sum on list #63
total=0
for num in a[0]:
	total+= num
print(total) #63
# max()  and  min()  functions  demo  program  (Home  work)
a = [10 , 20 , 15 , 18 , 30, 5 , 12]
print(max(a)) #30
print(min(a)) #5
b = ['Rama' , 'Sita' , 'Rajesh' , 'Kiran' , 'Amar' , 'Vamsi' , 'Manohar']
print(max(b)) #Vamsi
print(min(b)) #Amar
c = [25 , 10.8 ,  3 + 4j , True]
#print(max(c)) #error complex cannot  be compared
d = [25 , '35']
#print(max(d)) #error string cannot be compared
#print(max([])) #error 
#print(min([])) #error


'''
1) What  does  max(list)  do ?  --->  Returns  largest  element  of  the  list

2) What  does  min(list)  do ?  --->  Returns  smallest  element  of  the  list
'''
# list()  function  demo  program
a = (10 , 20 , 15, 18)
b = list(a) #typecasting converting tupule to List
print(b) #prints list 
print(type(b)) #<class 'list' >
print(a  is  b) #False
print(a == b) #False
#  Find  outputs (Home  work)
a = range(4 , 10 , 2)
b = list(a) #[4,6,8]
print(b) #[4,6,8]
print(type(b)) #<class 'list' >
a = list('Vamsi')
print(a) #['V','a','m','s','i']
a = list()  #empty list []
print(a) #empty list []
#print(list(25)) #error int
#print(list(10.8)) #error float
#print(list(True)) #error bool
#print(list(None)) #error nonetype


'''
1) What  does  list(sequence)  do ?  --->  Converts  sequence  to  list  and  returns  list

2) What  does  list(no-args)  do ?  ---> Returns  an  empty  list

3) What  does  list(non-sequence)  do ?  --->  Throws  error
'''
# Find  outputs (Home  work)
a = ((10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90))
print(list(a)) #[(10,20),(30,40,50),(60,70,80,90)]
b = { (10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90)}
print(list(b))  #[(10,20),(30,40,50),(60,70,80,90)]
c = ([10 , 20] , (30 , 40) , {50 , 60})
print(list(c)) #[(10,20),(30,40),{50,60}]

# sorted()  function   demo  program
a = [10 , 20 , 15 , 5 , 12]
b = sorted(a) #[5,10,12,15,20]
print(b) #[5,10,12,15,20]
print(type(b)) #<class 'list'>
c = sorted(a , reverse = True)
print(c) #[20,15,12,10,5]
print(a) #[10 , 20 , 15 , 5 , 12]


'''
sorted()  function
----------------------
1) What  does  sorted(list)  do  ?  ---> Returns  another  sorted  list

2) Is  argument  list  modified ?  --->  No  and  it  remains  unchanged

3) How  to  sort  list  in  descending  order ?  --->  sorted(list , reverse = True)

4) What  are  the  two  arguments  of  sorted()  function ?  --->  List  to  be  sorted
																												and
																					                  reverse = True  which  is  an  optional  argument
'''
# Find  outputs  (Home  work)
a = ['Rama',  'Rajesh',  'Amar',  'Sita',  'Vamsi'  ,  'Kiran'  , 'Rama  Rao']
b = sorted(a) 
print(b) #['Amar','Kiran','Sita','Rajesh','Rama','Rama Rao','Vamsi']
c = sorted(a , reverse = True)
print(c) #['Vamsi','Rama Rao,'Rama','Rajesh','Sita','Kiran','Amar']
print(a) #['Rama',  'Rajesh',  'Amar',  'Sita',  'Vamsi'  ,  'Kiran'  , 'Rama  Rao']

# all()  function demo  program  (Home  work)
a = [12 > 10 , 5 < 20 , 30 == 30]
print(all(a)) #True
b = [9 >= 6 , 12 <= 9 , 6 == 6]
print(all(b)) #False
c = [25 , 10.8 , '' , True , 3+4j , 'Hyd']
print(all(c)) #False
d = [10 , 0 , 20]
print(all(d)) #False
e = []
print(all(e)) #False


'''
all()  function
-----------------
1) What  does  all(list)  do ?  --->  Returns  True  when  every  element of  the  list  is  True  and  False  otherwise

2) When  does  it  return  False ?  --->  When  at  least  one  element  of  the  list  is  False

3) if  cond1  and  cond2  and  cond3  and  cond4:
    How  to  reduce  the  four  conditions  to  a  single  condition ?  --->  if  all([cond1 , cond2 , cond3 , cond4]):
'''
# any()  function demo program  (Home  work)
a  = [12 > 18 , 5 < 20 , 35 == 30]
print(any(a)) #True
b = [12 > 18 , 25 < 20 , 35 == 30]
print(any(b)) #False
c = [0 , 0.0 , '' , 25 , 0 + 0j , False]
print(any(c)) #True
d = [0 , 0.0 , '' , 0 + 0j , False]
print(any(d))  #False
e = []
print(any(e)) #False


'''
any()   function
-------------------
1) What  does  any(list)  do ?  ---> Returns  True  when  at  least  one  element  of  the  list  is  True  and  False  otherwise

2) When  does  it  return  False ?  ---> When  every  element  of  the  list  is  false

3) if  cond1  or  cond2  or  cond3  or  cond4:
     How  to  reduce  the  four  conditions  to  a  single  condition ?  ---> if  any([cond1 , cond2 , cond3 , cond4]):

4) all()  and  any()  functions  are  used  as  an  alternative  when  there  are  too  many  conditions  in  if  and  while
'''
# del  operator  demo  program (Home  work)
a = [10 , 20 , 15 , 18]
print(a) #[10 , 20 , 15 , 18]
del    a[2] 
print(a) #[10,20,18]
#del  a[3] #error theere is not index 3 in list index out of range
del  a #deletes the whole list
#print(a) #no list to print
#  append()  method  demo  program (Home  work)
list = [10 , 20 , 15 , 18]
print(list) #[10 , 20 , 15 , 18]
list . append(19) 
print(list)  #[10 , 20 , 15 , 18,19]
#  Find  outputs (Home  work)
list = []
print(list)
list . append(25)
list . append(10.8)
list . append('Hyd')
list . append(True)
print(list) #[25,10.8,'Hyd',True]
# Find  outputs  (Home  work)
list = []
for  x  in   range(0 , 50 , 10):
	list . append(x)
print(list) #[0,10,20,30,40]
#  Find  outputs  (Home  work)
a = [10 , 20 , 30]
a . append('Hyd')
print(a) #[10,20,30,'Hyd']
print(len(a)) #4
print(a[2]) #30 
print(a[3]) #Hyd
#print(a[4]) #index error out of range 
#print(a[5]) #index out of range
#  # remove()  method  demo  program  (Home  work)
try:
	list = [10 , 20 , 15 , 18 , 15 , 12 , 15 , 19]
	list . remove(15)
	print(list) #[10 , 20 , 18 , 15 , 12 , 15 , 19]
	list . remove(25) #throws error that 25 is not present in the list
except:
	print('25  is   not  in  the  list')



'''
remove()   method
---------------------
1) What  does  remove(x)  do ?  --->  Removes   first  occurance  of  'x'  from  the  list

2) What  does  remove()  method  do  if  'x'  is  not   in  the  list ?  --->  Throws  ValueError

3) How  to  remove  all  ocurances  of  'x'  from  the  list ?  --->   Call  remove()  method  in  a  loop
'''
'''
Write  a  program  to  delete  'all'  occurences  of  'x'  from  the  list

Let  1st  input  be   [10 , 20 , 15 , 18 , 19 , 15 , 17 , 20 , 15 , 14]  and
2nd  input  be  15
What  is  the  output ?  ---> [10 , 20 ,  18 , 19 , 17 , 20 , 14]
'''
list_n = [10 , 20 , 15 , 18 , 19 , 15 , 17 , 20 , 15 , 14]
print("Enter list :",list_n)
x = int(input("Enter the element to be deleted: "))
while x in list_n:
	list_n.remove(x)
print("List without {}'s:".format(x),list_n)

'''
Enter List  :  [10 , 20 , 15 , 18 , 19 , 15 , 17 , 20 , 15 , 14]
Enter  element  to  be  deleted : 15
List  without   15's :  [10, 20, 18, 19, 17, 20, 14]
'''
# clear() method  demo program  (Home  work)
list = [10 , 20 , 15 , 18]
print(list) #[10 , 20 , 15 , 18]
list . clear()
print(list) #empty list


'''
clear()  method
------------------
1) What  does  clear()  method  do ?  --->  Removes  all  the  elements  of  the  list  and  list  becomes  empty

2) What  about  remove()  and  pop()  methods  ?  ---> They  remove  single  element  of  the  list
'''
# reverse()  method  demo  program (Home  work)
a = [10 , 20 , 15 , 18]
print(a) #[10 , 20 , 15 , 18]
a . reverse()
print(a) #[18,15,20,10]


'''
reverse()  method
---------------------
1) What  does  reverse()  method  do ?  --->  Reverses  all  the  elements  of  list

2) Where  are  the  results  stored ?  --->  In  the  same  list  replacing  existing  elements (List  is  mutable)
'''
#  sort()  method  demo  program (Home  work)
list = [10 , 20 , 15 , 18 , 5]
print(list)  #[10 , 20 , 15 , 18 , 5]
list . sort() 
print(list) #[5,10,12,15,20]
list . sort(reverse = True)
print(list) #[20,15,12,10,5]

# Find  outputs (Home  work)
a = ['Rama' , 'Rajesh' , 'Amar' ,  'Sita' ,  'Vamsi' , 'Kiran' , 'Rama  Rao']
print(a)
a . sort()
print(a)
a . sort(reverse = True)
print(a)
# Identify  error (Home  work)
a = [25 , 10.8 ,  'Hyd' ,  True]
#a . sort() #error for non sequences
#  count()  method  demo    program (Home  work)
a = [10 , 20 , 15 , 18 , 15 , 12 , 14 , 15 , 19]
print(a . count(15))
print(a . count(25))
print(len(a))


'''
What  does  list . count(x)  do ?  ---> Returns  number  of  times  'x'  is  in  the  list
'''
'''
Tricky  program
Write  a  program  to  remove  all  duplicate  elements  of  the  list  (Not  even  single  occurance)
Let  input  be  [10 , 20 , 15 , 10 , 14 , 10 , 18 , 20 , 19]
What  is  the  output ?  ---> [15 , 14 , 18 , 19]

Hint:  Use  count()  and  append()  methods
'''
a =  [10 , 20 , 15 , 10 , 14 , 10 , 18 , 20 , 19]
result =[]

for num in a:
	if a.count(num) == 1:
		result.append(num)

print(result)
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
'''
Enter  any  list  :  [25,25,25,25]
All  the  list  elements  are  identical
Enter  any  list  :  [10,10,20,10]
List   elements  are  not  identical
'''
a = eval(input("Enter any list: "))

if len(a) == a.count(a[0]):
	print("All the elements are identical")
else:
	print("All the elements are not identical")

print("How many elemennts are in the list ? --->", len(a))
print("How many times is the first elements repeated ? -->",a.count(a[0]))


# index()  method  demo  program  (Home  work)
a = [10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25]
#     0    1    2    3    4    5    6    7    8    9   10
try:
	i = a . index(15)
	while  True:
		print(i)  
		i = a . index(15 , i + 1)
except:
	print(F'15  is  found  {a . count(15)}  times ') #15 is found 3 times


'''
index()  method
-------------------
1) What  does  index(x)  do ?  --->  Returns  index  of  first  'x'  in  the  list

2) What  does  index(invalid-element)  do  ?  --->  Throws  error

3) list . index(x , i)
    list . index(x)
    What  is  the  difference  between  the  two  statements ?  --->
										list . index(x , i)  searches  for  'x'  from   index  'i'  of  the  list  but
										list . index(x)   searches  for  for  'x'  from   index  0  of  the  list

Note:
1) What  are  the  four  search  methods  in  str  class  --->  find() , rfind() , index() , rindex()

2) What  is  the  only  search  method  in  list  class  ---> index()
'''