
#1st program
#  intersection()   method  demo  program (Home  work)
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . intersection(b) #common elements from sets a,b are stored in c
print(c) #{30,40} in any order
print(type(c))#<class'set'>
d = a & b #other way of intersection 
print(d)#{30,40} in any order
print(type(d))#<class'set'>
print(c  is  d)#False
print(c  ==  d)#True

#2nd program
# difference()   method  demo  program  (Home  work)
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . difference(b) #the elements which are present exclusively in set 'a' are stored in c 
print(c) #{10,20}
print(type(c))#<class'set'>
d = a - b #alternate way of finding difference
print(d)#{10,20}
print(type(d))#<class'set'>
print(c  is  d)#False
print(c  ==  d)#True

#3rd program
# symmetric_difference()   method  demo  program  (Home  work)
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . symmetric_difference(b) #all elements of sets a,b except common elements gets stored in c
print(c)#{10,20,50,60} in any order
print(type(c))#<class'set'>
d = a ^ b #alternate way for finding symmetric differnce between sets
print(d)#{10,20,50,60} in any order
print(type(d))#<class'set'>
print(c   is   d)#False
print(c  ==   d)#True

#4th program
# Find  outputs  (Home  work)
a = {x * x  for   x   in   range(10)}
print(a) #{0,1,4,9,16,25,36,49,64,81} in any order
print(type(a))#<class'set'>


#5th program
a=input("Enter any string: ")
b=set(a)
c=''.join(b)
print(f"String without duplicates {c}")


#6th program
'''
Write  a  program  to  remove  duplicate  elements  of   list  using  set

1) Let  input  be  [False , 25 , 10.8 , 1  , 25 , 0 , 'Hyd' ,  10.8 , 1.0 , None , 'Sec' , 'Hyd' , True  ]
    What  is  the  output ?  ---> [False , 25 , 10.8 , 1 , 'Hyd' , None , 'Sec']

2) Both  input  and  output  are  lists
'''
a=eval(input("Enter list with duplicates: "))
b=set(a)
c=list(b)
print(f'List without duplicates: {c}')


#7th program
'''
Write  a  program  to   obtain  common  elements  between  two  lists  using  sets

1) Let  1st  list  be  [10 , 20 , 30 , 40 , 50 , 60]  and  2nd  list  be  [30 , 40 , 70 , 80 , 20]
    What  is  the  output ?  --->  [20 , 30 , 40]

2) Both  input  and  output  are  lists
'''
a=eval(input("Enter 1st list: "))
b=eval(input("Enter 2nd list: "))
c=set(a)
d=set(b)
i=c.intersection(d)
res=list(i)
print("common elements between the 2 lists: ",res)

#8th program
#  How  to  access  values  of  dictionary (Home  work)
a  =  {'Empno'  :  25 ,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a['Empno'])#How  to  print  value  25  in  dict  'a'
print(a['Ename'])#How  to  print  'Rama Rao'  in  dict  'a'
print(a['Sal'])#How  to  print  value  1000.65   in  dict  'a'


#9th program
# How  to  modify  values  of  dictionary  (Home  work)
a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a) #{'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(id(a)) #address of dict a
a['Sal']=2000#How  to  modify  1000.65  to  2000
a['Ename']='Sita'#How  to  modify  'Rama  Rao'  to  'Sita'
a['Empno']=35#How  to  modify  25   to  35
print(a)#{'Empno'  :  35,  'Ename'  :  'Sita'  ,  'Sal'  :  2000 }
print(id(a))#Same address as previous a


#10th program
#  How  to  append  key : value  pairs  to dictionary  (Home  work)
a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a)#{'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
a['Gender']='M'#How  to  append  'Gender' : 'M'  to  dictionary  'a'
a['Married']=True#How  to  append  'Married' :  True  to  dictionary  'a'
print(a)#{'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65 , 'Gender': 'M' , 'Married: True'}


#11th program
# Find  outputs (Home  work)
a = { }
a[10]='Rama'#How  to  append  10 : 'Rama'  to  dictionary  'a'
a[20]='Sita'#How  to  append  20 : 'Sita'  to  dictionary  'a'
a[15]='Rajesh'#How  to  append  15 : 'Rajesh'  to  dictionary  'a'
a[18]='Kiran'#How  to  append  18 : 'Kiran'  to  dictionary  'a'
print(a)#{10 : 'Rama' , 20 : 'Sita' , 15 :' Rajesh', 18 : 'Kiran' }


#12th program
#  How  to  remove  key : value  pairs  of  dictionary  (Home  work)
a =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a)#{'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
del a['Sal']#How  to  remove  'Sal' : 1000.65  from  dictionary  'a'
print(a)#{'Empno'  :  25,  'Ename'  :  'Rama  Rao'  }


#13th program
#  in  and  not  in  operators  (Home  work)
a =  {10 : 20 , 30 : 40 , 50 : 60 , 70 : 80}
print(30  in  a . keys()) #True
print(60  in  a . keys())#False
print(60  in  a . values())#True
print(30  in  a . values())#False
print(50  in  a)#True
print(20  in  a)#False
print(70  not  in  a . keys())#False
print(40  not  in  a . values())#False
print(25  not  in  a)#True


#14th program
#  What  are  the  outputs  if  input  is  {10: 'A', 20: 'B', 15: 'C' , 20 : 'D'}
a = input('Enter  dictionary  :  ')#{10: 'A', 20: 'B', 15: 'C' , 20 : 'D'}
print(a)#{10: 'A', 20: 'B', 15: 'C' , 20 : 'D'}
print(type(a))#<class'str'>
b = eval(a)
print(b)#{10: 'A', 20: 'D', 15: 'C' }
print(type(b))#<class'dict'>


#15th program
#  Find  outputs  (Home  work)
a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh' , 18 : 'Kiran'}
b = {**a}
print(b)#{10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh' , 18 : 'Kiran'}
print(a  is  b)#False
print(a  ==  b)#True
c = a #ref copy
print(a  is   c)#True
print(a  ==  c)#True

#16th program
#Find  outputs  (Home  work)
a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh'}
b = {18 : 'Kiran' , 14 : 'Amar' , 20  : 'Manohar'}
c = {25 : 'Ramesh' , 19 : 'Krishna' , 15 : 'Radha' , 14 : 'Srinivas'}
d = {*a , *b , *c}
print(d)#{10,20,15,18,14,25,19,} in any order
print(type(d))#<class'set'>
e = {**a , **b , **c}
print(e)#{10 : 'Rama' , 20 : 'Manohar' , 15 : 'Radha' ,18 : 'Kiran' , 14 : 'Srinivas' , 25 : 'Ramesh' , 19 : 'Krishna' }
print(type(e))#<class'dict'>


#17th program
#  Find  outputs  (Home  work)
a = {10 : 20 , 30 : 40}
b = {30 : 50 , 10 : 60}
#print(a + b)#Error dict cannot be concatenated with + operator
c = {**a , **b}
print(c) #{10:60,30:50}
d = a | b #concate dict a and b
print(d) #{10:60,30:50}


#18th program
'''
(Home  work)
Write  a  program  to  create  a  dictionary  with  emp  names  and  salaries

Hint:  Append  each  emp  name  and  salary  to  dictionary  'a'
'''

n=int(input("How many employees: "))
res={}
for i in range(n):
    a=input("Enter Emp Name : ")
    b=eval(input("Enter Salary : "))
    res[a]=b
print(res)



#19th program
''' (Home  work)
Write  a  program  to  convert  a  string  to  dictionary

Let  input  be   "Emp no = 25 , Emp name = Rama  Rao , sal = 10000.0 , gender = m"

What  is  the  output ?  --->  {Emp no : 25 , Emp name  :  Rama Rao , sal : 10000.0 , gender : m}

Hint :  Use  split()  method  twice
'''

a=input("Enter string:")
b=a.split(",")
c={}
for x in b:
    y=x.split('=')
    c[y[0]]=y[1]
print(c)

#20th program
# len()  function  demo  program  (Home  work)
a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(len(a))#3
b = {}
print(len(b))#0

#21st program
#  sum()  function demo  program  (Home  work)
a = {10 : 20 , 30 : 40 , 50 : 60}
print(sum(a . keys()))#90
print(sum(a . values()))#120
print(sum(a))#90
#print(sum(a . items()))#error,tuple and int cannot be added

#22nd program
# max()  and  min()   functions  demo  program  (Home  work)
a = {10 : 20 , 30 : 25 , 40 : 5 , 7 : 28 , 9 : 50}
print(max(a . keys()))#40
print(min(a . keys()))#7
print(max(a . values()))#50
print(min(a . values()))#5
print(max(a . items()))#(40,5)
print(min(a . items()))#(7,28)
print(max(a))#40
print(min(a))#7


#23rd program
#  dict()  function  demo program (Home  work))
a = [ (10 , 'Hyd') , (20 , 'Sec') , (15 , 'Cyb') , (20 , 'Pune')]
b = dict(a)
print(b)#{10:'hyd',20:'pune',15:'cyb'}
c = ( ['R' , 'Red'] , ['G' , 'Green'] , ['B' , 'Blue'] , ['G' , 'Gray'])
d = dict(c)
print(d)#{'R':Red','G':'Gray,'B':'Blue'}
e = [[10 , 20 , 30] , [40 , 50 , 60] , [70 , 80 , 90]]
#print(dict(e))#Error
f = [[10] , [20] , [30]]
#print(dict(f))#Error
#print(dict([10 , 20]))#Error
g = [[10 , [20 , 30]] , [40 , [50 , 60]] , [70 , [80 , 90]]]
print(dict(g))#{10:[20,30],40:[50,60],70:[80,90]}
h = [[[10 , 20] , 30] , [[40 , 50] , 60] , [[70 , 80] , 90]]
#print(dict(h))#Error
i = [[(10 , 20) , 30] , [(40 , 50) , 60] , [(70 , 80) , 90]]
print(dict(i))#{(10,20):30,(40,50):60,(70,80):90}


#24th program
# sorted()  function  (Home  work)
a = {10 : 'Red' , 20 : 'Green' , 15 : 'Blue' , 18 : 'Yellow' , 5 : 'White'}
b = sorted(a . keys())
print(b)#[5,10,15,18,20]
c = sorted(a . values())
print(c)#['Blue','Green','Red','White','Yellow' ]
d = sorted(a . items())
print(d)#[(5,'White'),(10,'Red'),(15,'Blue'),(18,'Yellow'),(20,'Green')]
f  = sorted(a  , reverse = True)
print(f)#[20, 18, 15, 10, 5]
print(a)#{10 : 'Red' , 20 : 'Green' , 15 : 'Blue' , 18 : 'Yellow' , 5 : 'White'}

#25th program
'''
Tricky  program
Write  a  program  to  sort  dictionary  wrt  keys  (Home  work)

1) Let  input  be   {10 : 'A' , 20 : 'B' , 15 : 'C' , 5 : 'D' , 12 : 'E'}
    What  is  the  output ?  ---> {5 : 'D' , 10 : 'A' ,  12 : 'E' ,  15 : 'C' , 20 : 'B'}

2) Both  input  and  output  are  dictionaries

3) Hint:  Use  sorted()  function
'''

a=eval(input("Enter dictionary: "))
b=a.items()
c=sorted(b)
print(dict(c))


#26th program
# clear()  method  demo  program (Home  work)
a = {10 : 20 , 30 : 40 , 50 : 60}
print(a)#{10 : 20 , 30 : 40 , 50 : 60}
a . clear()
print(a)#{}
del  a
#print(a)#Error


#27th program
# copy()  method demo  program  (Home  work)
a = {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue'}
b = a . copy()
print(b)#{'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue'}
print(a  is  b)#false
print(a  ==  b)#true


#28th program
#  keys()  method  demo  program
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
b = a . keys()
print(b)#dict_keys([10,20,15,18])
print(type(b))#<class'dict_keys'>
for  x  in   b:
        print(x)#10 \n 20\n 15\n 18\n


#29th program
# values()  method  demo  program
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
b = a . values()
print(b)#dict_values(['Hyd' ,'Sec' ,'Cyb' ,'Pune'])
print(type(b))#<class'dict_values'>
for  x   in   b:
	print(x)#Hyd \n Sec\n Cyb\n Pune


#30th program
#  items()  method  demo  program
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
b = a . items()
print(b)#dict_items([(10,'Hyd'),(20,'Sec'),(15,'Cyb'),(18,Pune)])
print(type(b))#<class'dict_items'>
for  x   in   b:
        print(x)#(10,'Hyd')\n (20,'Sec')\n (15,'Cyb')\n (18,'Pune')
for  x , y   in  b:
        print(x , y , sep = ' ... ')#10...Hyd \n 20...Sec \n 15...Cyb \n 18...Pune


#31st program
# Find  outputs (Home  work)
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
for  x , y   in  a . items():
       print(x , y , sep = ' ... ')#10 ... Hyd \n 20 ... Sec \n 15 ... Cyb \n 18 ... Pune
#for  x , y   in  a . keys():
      # print(x , y , sep = ' ... ')#error
#for  x , y   in  a . values():
      # print(x , y , sep = ' ... ')#error
#for  x , y   in  a:
 #      print(x , y , sep = ' ... ')#error


#32nd program
#  Find  outputs  (Home  work)
a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh'}
x , y , z = a . keys()
print(x)#10
print(y)#20
print(z)#15
print()#blank line
x , y , z = a . values()
print(x)#Rama
print(y)#Sita
print(z)#Rajesh
print()#blank line
x , y ,  z = a . items()
print(x)#(10, 'Rama')
print(y)#(20, 'Sita')
print(z)#(15, 'Rajesh')
print()#blank line
(rno1 , sname1) , (rno2 , sname2) , (rno3 , sname3) = a . items()
print(rno1 , sname1)#10 Rama
print(rno2 , sname2)#20 Sita
print(rno3 , sname3)#15 Rajesh

#33rd program
'''
Tricky  program
(Home  work)
Write  a program  to  determine  frequency  of  each  alphabet  in  the  string   in   alphabetical  order
(ignoring  the  case)

'''

a=input("Enter mixed case string: ")
b=a.upper()
c=sorted(b)
d={}
for x in c:
    if x.isalpha():
        d[x]=d.get(x,0)+1
print(d)    
