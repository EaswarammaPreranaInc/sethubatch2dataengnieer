#  Find  outputs  (Home  work)
a = [10 , 20 , 30]
a . append('Hyd')
print(a) # [10 , 20 , 30,'Hyd']
print(len(a))#4
print(How  to  print  4th  element  of  list  'a')#print(a[3])
print(How  to  print  'H')#print(a[3][0])
print(How  to  print  'y')#print(a[3][1])
print(How  to  print  'd')#print(a[3][2])

# remove()  method  demo  program  (Home  work)
try:
    list = eval("enter list of integer val:" )
    x=int(input("enter a number to remove in list))
    while x in list:
        list.remove(x)
    print(list)
except:
	print('x  is   not  in  the  list')
'''
remove()   method
---------------------
1) What  does  remove(x)  do ?  --->  Removes   first  occurance  of  'x'  from  the  list

2) What  does  remove()  method  do  if  'x'  is  not   in  the  list ?  --->  Throws  ValueError

3) How  to  remove  all  ocurances  of  'x'  from  the  list ?  --->   Call  remove()  method  in  a  loop
'''

# clear() method  demo program  (Home  work)
list = [10 , 20 , 15 , 18]
print(list) #[10 , 20 , 15 , 18]
list . clear()
print(list) #[]


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
print(a) #[18,15,20,10] same id


'''
reverse()  method
---------------------
1) What  does  reverse()  method  do ?  --->  Reverses  all  the  elements  of  list

2) Where  are  the  results  stored ?  --->  In  the  same  list  replacing  existing  elements (List  is  mutable)
'''

#  sort()  method  demo  program (Home  work)

list = [10 , 20 , 15 , 18 , 5]
print(list) #[10 , 20 , 15 , 18 , 5]
list . sort()
print(list) #[5,10,15,18,20]
list . sort(reverse = True)
print(list) #[20,18,15,10,5]
# Find  outputs (Home  work)
a = ['Rama' , 'Rajesh' , 'Amar' ,  'Sita' ,  'Vamsi' , 'Kiran' , 'Rama  Rao']
print(a) #['Rama' , 'Rajesh' , 'Amar' ,  'Sita' ,  'Vamsi' , 'Kiran' , 'Rama  Rao']
a . sort()
print(a)#['Amar' , 'Kiran' , 'Rajesh' , 'Rama' ,  'Rama  Rao', 'Sita' ,  'Vamsi' ,]
a . sort(reverse = True)
print(a) # ['Vamsi', 'Sita', 'Rama  Rao', 'Rama', 'Rajesh', 'Kiran', 'Amar']
# Identify  error (Home  work)
a = [25 , 10.8 ,  'Hyd' ,  True]
a . sort() # not possible multiple classes
#  count()  method  demo    program (Home  work)
a = [10 , 20 , 15 , 18 , 15 , 12 , 14 , 15 , 19]
print(a . count(15)) #3
print(a . count(25))#0
print(len(a)) #9


'''
What  does  list . count(x)  do ?  ---> Returns  number  of  times  'x'  is  in  the  list

Tricky  program
Write  a  program  to  remove  all  duplicate  elements  of  the  list  (Not  even  single  occurance)
Let  input  be  [10 , 20 , 15 , 10 , 14 , 10 , 18 , 20 , 19]
What  is  the  output ?  ---> [15 , 14 , 18 , 19]

Hint:  Use  count()  and  append()  methods
'''
x= [10 , 20 , 15 , 10 , 14 , 10 , 18 , 20 , 19]
y=[]
for i in x:
    cnt=x.count(i)
    if(cnt==1):
        y.append(i)
print(y)
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
x=eval(input("enter list:"))
a=len(x)
b=x.count(x[0])
if(a==b):
    print("All  the  elements  are  identical")
else:
    print("List   elements  are  not  identical")
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
