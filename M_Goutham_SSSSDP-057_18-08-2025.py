 #  len()  function demo   program  (Home  work)
a = [ 25, 10.8, 'Hyd', True] #Here reference a points to list of elements
print(len(a)) #Returns the length of list i.e 4
b = [] #Reference b points to an empty list
print(len(b)) #Returns 0 as the list is empty
c = [[10 , 20] , 30 , 40] #Reference c points to list of elements and a list inside the list is their 
print(len(c)) #Returns the length of list i.e 3

'''
What  does  len(list)  do ?  --->  Returns  number  of  elements  in  the  list
'''



# sum()  function  demo  program  (Home  work)
a = [25 , 10.8 , True] #Reference a points to list of elements
print(sum(a)) #Returns the sum of elements in the list i.e 36.8
b= [3 + 4j , 5 + 6j] #Reference b points to list of elements i.e complex elements
print(sum(b)) #Returns the sum of complex numbers i.e 8+10j
c = [25 , 10.8 , True , 3 + 4j , False] #Reference c points to list of elements
print(sum(c)) #Returns the sum of elements in the list i.e 25 + 10.8 + True = 1 + 3 + 4j + False i.e 
d = [10 , 20 , 15 , 18] #Reference d points to list of elements 
print(sum(d)) #Returns the sum of elements in the list i.e 10+20+15+18 i.e 63
e = [25 , 10.8 , 'Hyd' , True] #Reference e points to list of elements
print(sum(e)) #Error #Because str 'Hyd' is a unsupported operand

'''
What  does  sum(list)  do ?  ---> Returns  sum  of  list  elements
'''


#  Find  outputs
a = [[10 , 20 , 15 , 18]] #Reference a points to list of elements
print(sum(a)) #Error 
print(sum(a[0])) #We can add the sum of elements by indexes i.e 63
#print(How  to  determine  sum  of  inner  list  elements  in  another)
#We can add the list of elements using for loop
for i in a:
	print(sum(i))
'''Output:
63
'''


# max()  and  min()  functions  demo  program  (Home  work)
a = [10 , 20 , 15 , 18 , 30, 5 , 12] #Reference a points to list of elements
print(max(a)) #Returns the largest element in the list i.e 30
print(min(a)) #Returns the smallest element in the list i.e 5
b = ['Rama' , 'Sita' , 'Rajesh' , 'Kiran' , 'Amar' , 'Vamsi' , 'Manohar'] #Reference b points to list of str elements
print(max(b)) #Returns the str where it compares the 1st letter of the str and which has the highest asci value that will be the max i.e 'Vamsi'
print(min(b)) #Returns the str where it compares the 1st letter of the str and which has the lowest asci value that will be the min i.e 'Amar'
c = [25 , 10.8 ,  3 + 4j , True] #Reference c points to list of elements
print(max(c)) #Error #Because we cannot compare complex and int
d = [25 , '35'] 
print(max(d)) #Error #We cannot compare str and int
print(max([])) #Error #Because argument is empty
print(min([])) #Error #Because argument is empty


'''
1) What  does  max(list)  do ?  --->  Returns  largest  element  of  the  list

2) What  does  min(list)  do ?  --->  Returns  smallest  element  of  the  list
'''



# list()  function  demo  program
a = (10 , 20 , 15, 18) #Reference a points to tuple of elements
b = list(a) #Here we are converting the tuple to list using list() 
print(b) #Returns the converted list i.e [10, 20, 15, 18]
print(type(b)) #Returns the type i.e <class 'list'>
print(a  is  b) #False #a points to tuple and b points to list
print(a == b) #False #Because one is tuple and one is list



#  Find  outputs (Home  work)
a = range(4 , 10 , 2)
b = list(a) #Here range object is converted to list of 3 elements i.e [4,6,8]
print(b) #[4, 6, 8]
print(type(b)) #<Class 'list'>
a = list('Vamsi') #Here str is converted to list by each character as each element in the list 
print(a) #['V','a','m','s','i']
a = list() 
print(a) #Empty list
print(list(25)) #Error #as int cannot be a list 
print(list(10.8)) #Error #as float cannot be a list
print(list(True)) #Error #as bool cannot be a list
print(list(None)) #Error #as none cannot be a list


'''
1) What  does  list(sequence)  do ?  --->  Converts  sequence  to  list  and  returns  list

2) What  does  list(no-args)  do ?  ---> Returns  an  empty  list

3) What  does  list(non-sequence)  do ?  --->  Throws  error
'''


# Find  outputs (Home  work)
a = ((10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90))
print(list(a)) #Returns the list and inside list tuples i.e [(10, 20), (30, 40, 50), (60, 70, 80, 90)]
b = { (10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90)}
print(list(b)) #[(30, 40, 50), (60, 70, 80, 90), (10, 20)]
c = ([10 , 20] , (30 , 40) , {50 , 60})
print(list(c)) #[[10, 20], (30, 40), {50, 60}]



# sorted()  function   demo  program
a = [10 , 20 , 15 , 5 , 12]
b = sorted(a) #Here elements of list a will be arranged in ascending order and listed them in reference b
print(b) #[5, 10, 12, 15, 20]
print(type(b)) #<class 'list'>
c = sorted(a , reverse = True)
print(c) #Returns the elements of c which are sorted in reverse order of list b i.e [20, 15, 12, 10, 5]
print(a) #Returns the same list i.e [10 , 20 , 15 , 5 , 12]


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
b = sorted(a) #Here reference b points to sorted list(ascending ordered elements of a) according to the 1st letters asci values
print(b) # Returns the sorted list i.e ['Amar', 'Kiran', 'Rajesh', 'Rama', 'Rama  Rao', 'Sita', 'Vamsi']
c = sorted(a , reverse = True) #Reverse the sorted list i.e b
print(c) # ['Vamsi', 'Sita', 'Rama  Rao', 'Rama', 'Rajesh', 'Kiran', 'Amar']
print(a) # Returns the list a i.e ['Rama',  'Rajesh',  'Amar',  'Sita',  'Vamsi'  ,  'Kiran'  , 'Rama  Rao']



# all()  function demo  program  (Home  work)
a = [12 > 10 , 5 < 20 , 30 == 30]
print(all(a)) #all() returns the if all the conditions are True i.e True
b = [9 >= 6 , 12 <= 9 , 6 == 6]
print(all(b)) #Returns False 
c = [25 , 10.8 , '' , True , 3+4j , 'Hyd']
print(all(c)) #False #Because there is an empty str in the list
d = [10 , 0 , 20]
print(all(d)) #As the list has 0 so it returns False
e = []
print(all(e)) #False #as there is an empty list


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
print(any(a)) #Returns true as any() will return true when atleast one condition becomes True
b = [12 > 18 , 25 < 20 , 35 == 30]
print(any(b)) #Returns False
c = [0 , 0.0 , '' , 25 , 0 + 0j , False]
print(any(c)) #True
d = [0 , 0.0 , '' , 0 + 0j , False]
print(any(d)) #False
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
print(a) #Returns the list of elements i.e [10 , 20 , 15 , 18]
del    a[2] #Deletes the element at index 2 and returns nothing i.e a[2] = 15
print(a) #Returns the list after deletion of the element 15 i.e [10, 20, 18]
del  a[3] #Error as there is no index 3
del  a  #deletes the entire list which is referencing a 
print(a) #Error #as we have deleted the list a and we cannot print the a



#  append()  method  demo  program (Home  work)
list = [10 , 20 , 15 , 18]
print(list) #Returns the list i.e [10, 20, 15, 18]
list . append(19) #Adds the element 19 at the end of the list
print(list) #Returns the updated list where we have already appended the element i.e [10, 20, 15, 18, 19]


#  Find  outputs (Home  work)
list = []
print(list) #Returns the empty list 
list . append(25) #Here the int element 25 is added to the list 
list . append(10.8) #Here the float element 10.8 is added after 25 in the list
list . append('Hyd') #Here the str element 'Hyd' is added after 10.8 in the list
list . append(True) #Here the bool element True is added after 'Hyd' in the list
print(list) #[25, 10.8, 'Hyd', True]


# Find  outputs  (Home  work)
list = []
for  x  in   range(0 , 50 , 10): #By using for loop we are appending elements to the list from range 0 to 49 in steps of 10  
	list . append(x) #0 10 20 30 40 
print(list) #Returns the list with appended elements i.e [0, 10, 20, 30, 40]


#  Find  outputs  (Home  work)
a = [10 , 20 , 30]
a . append('Hyd') #Here str 'Hyd' is appended to the list at end of the list 
print(a) #Returns the list with updated elements i.e [10, 20, 30, 'Hyd']
print(len(a)) #Returns the length of list i.e 4
print(a[3]) #print(How  to  print  4th  element  of  list  'a')
print(a[3][0]) #print(How  to  print  'H')
print(a[3][1]) #print(How  to  print  'y')
print(a[3][2]) #print(How  to  print  'd')


# remove()  method  demo  program  (Home  work)
try:
	list = [10 , 20 , 15 , 18 , 15 , 12 , 15 , 19]
	list . remove(15)
	print(list)
	list . remove(25)
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

n = eval(input("Enter any list: "))
b = eval(input("Enter the element to be deleted: "))
while b in n:
    n.remove(b) #Modifies the existing list by removing the 1st occurance of the desired element
print(f"List without {b}'s: {n}")

'''
output:
Enter List  :  [10 , 20 , 15 , 18 , 19 , 15 , 17 , 20 , 15 , 14]
Enter  element  to  be  deleted : 15
List  without   15's :  [10, 20, 18, 19, 17, 20, 14]
'''



# clear() method  demo program  (Home  work)
list = [10 , 20 , 15 , 18]
print(list) #Rteurns the list i.e [10 , 20 , 15 , 18]
list . clear() #Clear all the elements in the list 
print(list) #Returns the empty list


'''
clear()  method
------------------
1) What  does  clear()  method  do ?  --->  Removes  all  the  elements  of  the  list  and  list  becomes  empty

2) What  about  remove()  and  pop()  methods  ?  ---> They  remove  single  element  of  the  list
'''



# reverse()  method  demo  program (Home  work)
a = [10 , 20 , 15 , 18]
print(a) #Returns the list elements of a i.e [10 , 20 , 15 , 18]
a . reverse() #Reverse the list a 
print(a) #Returns the reversed list i.e [18, 15, 20, 10] 


'''
reverse()  method
---------------------
1) What  does  reverse()  method  do ?  --->  Reverses  all  the  elements  of  list

2) Where  are  the  results  stored ?  --->  In  the  same  list  replacing  existing  elements (List  is  mutable)
'''


#  sort()  method  demo  program (Home  work)
list = [10 , 20 , 15 , 18 , 5]
print(list) #Returns the list [10 , 20 , 15 , 18 , 5]
list . sort() #Sort the elements in the list in ascending order
print(list) #Returns the sorted elements i.e [5, 10, 15, 18, 20]
list . sort(reverse = True) #Here sort the list and reverse that list i.e 
print(list) # [20, 18, 15, 10, 5]


# Find  outputs (Home  work)
a = ['Rama' , 'Rajesh' , 'Amar' ,  'Sita' ,  'Vamsi' , 'Kiran' , 'Rama  Rao']
print(a) #Returns the list a i.e ['Rama' , 'Rajesh' , 'Amar' ,  'Sita' ,  'Vamsi' , 'Kiran' , 'Rama  Rao']
a . sort() #Sort the elements in the list with their 1st character according to the asci value small to big
print(a) #Returns the sorted list i.e ['Amar', 'Kiran', 'Rajesh', 'Rama', 'Rama  Rao', 'Sita', 'Vamsi']
a . sort(reverse = True) #sort the list and reverse the sorted list 
print(a) #['Vamsi', 'Sita', 'Rama  Rao', 'Rama', 'Rajesh', 'Kiran', 'Amar']


# Identify  error (Home  work)
a = [25 , 10.8 ,  'Hyd' ,  True]
a . sort() #Here the error is we cannot compare and sort these elements as their are of different types



#  count()  method  demo    program (Home  work)
a = [10 , 20 , 15 , 18 , 15 , 12 , 14 , 15 , 19]
print(a . count(15)) #Returns the number of times 15 is repeated in the list i.e 3
print(a . count(25)) #Returns 0 as there is no element 25 in the list
print(len(a)) #Returns the length of list a i.e 9

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
n = eval(input("Enter any list: "))
if n.count(n[0]) == len(n):
    print("All  the  list  elements  are  identical")
else:
    print("List   elements  are  not  identical")

'''
Enter  any  list  :  [25,25,25,25]
All  the  list  elements  are  identical
 Enter  any  list  :  [10,10,20,10]
List   elements  are  not  identical
'''




# index()  method  demo  program  (Home  work)
a = [10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25]
#     0    1    2    3    4    5    6    7    8    9   10
try:
	i = a . index(15)
	while  True:
		print(i)
		i = a . index(15 , i + 1)
except:
	print(F'15  is  found  {a . count(15)}  times ')



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