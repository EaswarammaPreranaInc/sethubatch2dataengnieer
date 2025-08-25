#1.  intersection()   method  demo  program (Home  work)
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . intersection(b)
print(c) # {10,20,50,60}
print(type(c)) # <class 'set'>
d = a & b
print(d) # {10,20,50,60}
print(type(d)) # <class 'set'>
print(c  is  d) # False
print(c  ==  d) # True






#2. difference()   method  demo  program  (Home  work)
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . difference(b)
print(c) # {10,20}
print(type(c)) # <class 'set'>
d = a - b
print(d) # {10,20}
print(type(d)) # <class 'set'>
print(c  is  d) # False
print(c  ==  d) # True






#3. symmetric_difference()   method  demo  program  (Home  work)
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . symmetric_difference(b)
print(c) # {10,20,50,60}
print(type(c)) # <class 'set'>
d = a ^ b
print(d) # {10,20,50,60}
print(type(d)) # <class 'set'>
print(c   is   d) # False
print(c  ==   d) # True






#4. Find  outputs  (Home  work)
a = {x * x  for   x   in   range(10)}
print(a) # {0,1,4,9,16,25,36,49,64,81}
print(type(a)) # <class 'set'>





#5.  How  to  access  values  of  dictionary (Home  work)
a  =  {'Empno'  :  25 ,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a['Empno']) # How  to  print  value  25  in  dict  'a'
print(a['Ename']) # How  to  print  'Rama Rao'  in  dict  'a'
print(a['Sal']) # How  to  print  value  1000.65   in  dict  'a'





#6. How  to  modify  values  of  dictionary  (Home  work)
a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a) # {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(id(a)) # Address of 'a'
a['Sal'] = 2000 # How  to  modify  1000.65  to  2000
a['Ename'] = 'Sita' # How  to  modify  'Rama  Rao'  to  'Sita'
a['Empno'] = 35 # How  to  modify  25   to  35
print(a) # {'Empno'  :  35,  'Ename'  :  'Sita'  ,  'Sal'  :  2000  }
print(id(a)) # same address





#7.  How  to  append  key : value  pairs  to dictionary  (Home  work)
a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a) # {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
a['Gender'] = 'M' # How  to  append  'Gender' : 'M'  to  dictionary  'a'
a['Married'] = True # How  to  append  'Married' :  True  to  dictionary  'a'
print(a) # {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65 ,'Gender'  :  'M' , 'Married'  :  True }






8.# Find  outputs (Home  work)
a = { }
a[10] = 'Rama' # How  to  append  10 : 'Rama'  to  dictionary  'a'
a[20] = 'Sita' # How  to  append  20 : 'Sita'  to  dictionary  'a'
a[15] = 'Rajesh' # How  to  append  15 : 'Rajesh'  to  dictionary  'a'
a[18] = 'Kiran' # How  to  append  18 : 'Kiran'  to  dictionary  'a'
print(a) # {10: 'Rama', 20: 'Sita', 15: 'Rajesh', 18: 'Kiran'}







#9.  How  to  remove  key : value  pairs  of  dictionary  (Home  work)
a =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a) # {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
del a['Sal'] # How  to  remove  'Sal' : 1000.65  from  dictionary  'a'
print(a) # {'Empno': 25, 'Ename': 'Rama  Rao'}







#10.  in  and  not  in  operators  (Home  work)
a =  {10 : 20 , 30 : 40 , 50 : 60 , 70 : 80}
print(30  in  a . keys()) # True
print(60  in  a . keys()) # False
print(60  in  a . values()) # True
print(30  in  a . values()) # False
print(50  in  a) # True
print(20  in  a) # False
print(70  not  in  a . keys()) # False
print(40  not  in  a . values()) # False
print(25  not  in  a) # True






#11.  What  are  the  outputs  if  input  is  {10: 'A', 20: 'B', 15: 'C' , 20 : 'D'}
a = input('Enter  dictionary  :  ')
print(a) # '{10: 'A', 20: 'B', 15: 'C' , 20 : 'D'}'
print(type(a)) # <class 'str'>
b = eval(a)
print(b) # {10: 'A', 20: 'D', 15: 'C'}
print(type(b)) # <class 'dict'>







#12.  Find  outputs  (Home  work)
a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh' , 18 : 'Kiran'}
b = {**a}
print(b) # {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh' , 18 : 'Kiran'}
print(a  is  b) # Flase
print(a  ==  b) # True
c = a
print(a  is   c) # True
print(a  ==  c) # True






#13. Find  outputs  (Home  work)
a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh'}
b = {18 : 'Kiran' , 14 : 'Amar' , 20  : 'Manohar'}
c = {25 : 'Ramesh' , 19 : 'Krishna' , 15 : 'Radha' , 14 : 'Srinivas'}
d = {*a , *b , *c}
print(d) #  {10,20,15,18,14,25,19}
print(type(d)) # <class 'set'>
e = {**a , **b , **c}
print(e) # {10: 'Rama', 20: 'Manohar', 15: 'Radha', 18: 'Kiran', 14: 'Srinivas', 25: 'Ramesh', 19: 'Krishna'}
print(type(e)) # class 'dict'>






#14.  Find  outputs  (Home  work)
a = {10 : 20 , 30 : 40}
b = {30 : 50 , 10 : 60}
#print(a + b) # Error due to '+'is unsupported
c = {**a , **b}
print(c) # {10:60 . 30:50}
d = a | b
print(d) # {10:60 . 30:50}








#15. len()  function  demo  program  (Home  work)
a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(len(a)) # 3
b = {}
print(len(b)) # 0









#16.  sum()  function demo  program  (Home  work)
a = {10 : 20 , 30 : 40 , 50 : 60}
print(sum(a . keys())) # 90
print(sum(a . values())) # 120
print(sum(a)) # 90
#print(sum(a . items())) #  Error






#17. max()  and  min()   functions  demo  program  (Home  work)
a = {10 : 20 , 30 : 25 , 40 : 5 , 7 : 28 , 9 : 50}
print(max(a . keys())) # 40
print(min(a . keys())) # 7
print(max(a . values())) # 50
print(min(a . values())) # 5
print(max(a . items())) # (40,5)
print(min(a . items())) # (7,28)
print(max(a)) # 40
print(min(a)) # 7






#18.  dict()  function  demo program (Home  work))
a = [ (10 , 'Hyd') , (20 , 'Sec') , (15 , 'Cyb') , (20 , 'Pune')]
b = dict(a)  
print(b) # {10 : 'Hyd' , 20 : 'Pune' , 15 : 'Cyb' }
c = ( ['R' , 'Red'] , ['G' , 'Green'] , ['B' , 'Blue'] , ['G' , 'Gray'])
d = dict(c)
print(d) # {'R' : 'Red' , 'G' : 'Gray' , 'B' : 'Blue' }
e = [[10 , 20 , 30] , [40 , 50 , 60] , [70 , 80 , 90]]
#print(dict(e)) # Error
f = [[10] , [20] , [30]]
#print(dict(f)) # Error
#print(dict([10 , 20])) # Error
g = [[10 , [20 , 30]] , [40 , [50 , 60]] , [70 , [80 , 90]]]
print(dict(g)) # {10 ; [20 , 30],[40 : [50 , 60] , 70 : [80 , 90]}
h = [[[10 , 20] , 30] , [[40 , 50] , 60] , [[70 , 80] , 90]]
#print(dict(h)) # Error
i = [[(10 , 20) , 30] , [(40 , 50) , 60] , [(70 , 80) , 90]]
print(dict(i)) # {(10 , 20) : 30 , (40 , 50) : 60 , (70 , 80) : 90}









#19. sorted()  function  (Home  work)
a = {10 : 'Red' , 20 : 'Green' , 15 : 'Blue' , 18 : 'Yellow' , 5 : 'White'}
b = sorted(a . keys())
print(b) # [5, 10, 15, 18, 20]
c = sorted(a . values())
print(c) # ['Blue', 'Green', 'Red', 'White', 'Yellow']
d = sorted(a . items())
print(d) # [(5, 'White'), (10, 'Red'), (15, 'Blue'), (18, 'Yellow'), (20, 'Green')]
f  = sorted(a  , reverse = True)
print(f) # [20, 18, 15, 10, 5]
print(a) # {10: 'Red', 20: 'Green', 15: 'Blue', 18: 'Yellow', 5: 'White'}






#20. clear()  method  demo  program (Home  work)
a = {10 : 20 , 30 : 40 , 50 : 60}
print(a) # {10 : 20 , 30 : 40 , 50 : 60}
a . clear()
print(a) # set()
del  a
#print(a) # Error due to 'a' is already deleted







#21. copy()  method demo  program  (Home  work)
a = {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue'}
b = a . copy()
print(b) # {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue'}
print(a  is  b) # False
print(a  ==  b) # True






#22.  keys()  method  demo  program
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
b = a . keys()
print(b) # dict_keys([10,20,15,18])
print(type(b)) # <class 'dict_keys'>
for  x  in   b:
        print(x) # 10<nextline>20<nextline>15<nextline>18








#23. values()  method  demo  program
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
b = a . values()
print(b) # dict_values(['Hyd','Sec', 'Cyb','Pune'])
print(type(b)) # <class 'dict_values'>
for  x   in   b:
	print(x) # 'Hyd'<nextline>'Sec'<nextline>'Cyb'<nextline>'Pune'







#24.  items()  method  demo  program
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
b = a . items()
print(b) # dict_values([(10,'Hyd'),(20,'Sec'),(15,'Cyb'),(18,'Pune')])
print(type(b)) # <class 'dict_items'>
for  x   in   b:
        print(x) # (10, 'Hyd')<nextline>(20, 'Sec')<nextline>(15, 'Cyb')<nextline>(18, 'Pune')
for  x , y   in  b:
        print(x , y , sep = ' ... ') # 10...Hyd<nextline>20...Sec<nextline>15...Cyb<nextline>18...Pune







#25. Find  outputs (Home  work)
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
for  x , y   in  a . items():
       print(x , y , sep = ' ... ') # 10...Hyd<nextline>20...Sec<nextline>15...Cyb<nextline>18...Pune
#for  x , y   in  a . keys():
#       print(x , y , sep = ' ... ') # Error
#for  x , y   in  a . values():
#       print(x , y , sep = ' ... ') # Error
#for  x , y   in  a:
#       print(x , y , sep = ' ... ') # Error







#26.  Find  outputs  (Home  work)
a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh'}
x , y , z = a . keys()
print(x) # 10
print(y) # 20
print(z) # 15
print() # Nothing will be printed
x , y , z = a . values()
print(x) # 'Rama'
print(y) # 'Sita'
print(z) # 'Rajesh'
print() # Nothing
x , y ,  z = a . items()
print(x) # (10,'Rama')
print(y) # (20,'sita')
print(z) # (15,'Rajesh')
print() # Nothing
(rno1 , sname1) , (rno2 , sname2) , (rno3 , sname3) = a . items()
print(rno1 , sname1) # 10 'Rama'
print(rno2 , sname2) # 20 'sita'
print(rno3 , sname3)# 15 'Rajesh'




#27. Write  a  program  to  remove  duplicate  characters  of  the  string  using  set
a = input("Enter  input  string :  ")
b = set(a)
print("String  without  duplicates : ",''.join(b)) # oR ma



#28. Write  a  program  to  remove  duplicate  elements  of   list  using  set
a = eval(input("Enter  list  with  duplicates : "))
b = set(a)
print("List  without  duplicates :   ",list(b)) # [False, 1, None, 'Hyd', 10.8, 'Sec', 25]



#29. Write  a  program  to   obtain  common  elements  between  two  lists  using  sets
a = eval(input("Enter  1st  list  :  ")) # [10,20,30,40,50]
b = set(a)
c = eval(input("Enter  2st  list  :  ")) # [10,20,60,70,80]
d = set(c)
e = b.intersection(d)
print("Common  elements  between  the  2  lists : ",list(e)) # [10,20]






#30. Write  a  program  to  create  a  dictionary  with  emp  names  and  salaries
a = int(input("How many Employees ? : "))
d ={}
for i in range(a):
    b = input("Enter Emp Name : ")
    c = float(input("Enter Salary : "))
    d[b] = c
print(d)

'''How many Employees ? : 5
Enter Emp Name : naveen
Enter Salary : 10000
Enter Emp Name : banny
Enter Salary : 2000
Enter Emp Name : kiran
Enter Salary : 40000
Enter Emp Name : jack
Enter Salary : 400000
Enter Emp Name : ill
Enter Salary : 500
{'naveen': 10000.0, 'banny': 2000.0, 'kiran': 40000.0, 'jack': 400000.0, 'ill': 500.0}'''





#31. Write  a  program  to  convert  a  string  to  dictionary
a = input("Enter a string : ").split(",")
b ={}
for i in a:
    j = i.split("=")
    b[j[0]]=(j[1])
print(b) # {'Emp no ': ' 25 ', ' Emp name ': ' Rama  Rao ', ' sal ': ' 10000.0 ', ' gender ': ' m'}




#32. Write  a  program  to  sort  dictionary  wrt  keys  (Home  work)
a = eval(input("Enter  dictionary  :  ")) # {10 : 'A' , 20 : 'B' , 15 : 'C' , 5 : 'D' , 12 : 'E'}
b = (sorted(a.items()))
print(dict(b)) # {5 : 'D' , 10 : 'A' ,  12 : 'E' ,  15 : 'C' , 20 : 'B'}





#33.Write  a program  to  determine  frequency  of  each  alphabet  in  the  string   in   alphabetical  order(ignoring  the  case)
a = (input("Enter a string  :  ")).upper() # 'Rama Rao'
b = sorted(a)
c ={}
for i in b:
    if i.isspace():
        continue
    c[i] = c . get(i , 0) + 1
print(c) # {'A': 3, 'M': 1, 'O': 1, 'R': 2}

