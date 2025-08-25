a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a.intersection(b) # {40, 30}
print(type(c))   # <class 'set'>
d = a & b    # {40, 30}
print(type(d))    # <class 'set'>
print(c is d)     # False
print(c == d)      # True


difference() Method Demo
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a.difference(b)  # {10, 20}
print(type(c))  <class 'set'>
d = a - b  # {10, 20}
print(type(d   # <class 'set'>
print(c is d)    # False
print(c == d) # True

symmetric_difference() Method Demo
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a.symmetric_difference(b)   # {10, 20, 50, 60}
print(type(c))# <class 'set'>
d = a ^ b # {10, 20, 50, 60}
print(type(d) # <class 'set'>
print(c is d)    # False
print(c == d)      # True
Set Comprehension Demoa = {x * x for x in range(10)}  # {0, 1, 4, 9, 16, 25, 36, 49, 64, 81}
print(type(a))# <class 'set'>

How to append items to a dictionarya = {}                            # Empty dictionary
a[10] = 'Rama' # {10: 'Rama'}
a[20] = 'Sita'  # {10: 'Rama', 20: 'Sita'}
a[15] = 'Rajesh' # {10: 'Rama', 20: 'Sita', 15: 'Rajesh'}
a[18] = 'Kiran' # {10: 'Rama', 20: 'Sita', 15: 'Rajesh', 18: 'Kiran'}
print(a) # {10: 'Rama', 20: 'Sita', 15: 'Rajesh', 18: 'Kiran'}

in and not in operators (Home work)a = {10 : 20, 30 : 40, 50 : 60, 70 : 80}
print(30 in a.keys())   # True
print(60 in a.keys() # False
print(60 in a.values())  # True
print(30 in a.values()) # False
print(50 in a) # True
print(20 in a)  False
print(70 not in a.keys())  # False
print(40 not in a.values()# False
print(25 not in a)   # True

a = input('Enter  dictionary  :  ')   # {10: 'A', 20: 'B', 15: 'C', 20: 'D'}
print(a)  # {10: 'A', 20: 'B', 15: 'C', 20: 'D'}
print(type(a)) # class 'str'
b = eval(a) # {10: 'A', 20: 'D', 15: 'C'}
print(b) # {10: 'A', 20: 'D', 15: 'C'}
print(type(b))   # class 'dict'

Find outputs
a = {10: 'Rama', 20: 'Sita', 15: 'Rajesh', 18: 'Kiran'}
b = {**a}
print(b)   {10: 'Rama', 20: 'Sita', 15: 'Rajesh', 18: 'Kiran'}
print(a is b)  # False
print(a == b) # True
c = a
print(a is c)# True
print(a == c)  # True

a = {10: 'Rama', 20: 'Sita', 15: 'Rajesh'}
b = {18: 'Kiran', 14: 'Amar', 20: 'Manohar'}
c = {25: 'Ramesh', 19: 'Krishna', 15: 'Radha', 14: 'Srinivas'}
d = {*a, *b, *c}
print(d) # {10, 14, 15, 18, 19, 20, 25}
print(type(d)) # class 'set'
e = {**a, **b, **c}
print(e)  # {10: 'Rama', 20: 'Manohar', 15: 'Radha', 18: 'Kiran', 14: 'Srinivas', 25: 'Ramesh', 19: 'Krishna'}
print(type(e)) # class 'dict'

a = {10: 20, 30: 40}
b = {30: 50, 10: 60}
# print(a + b) # error
c = {**a, **b}
print(c)# {10: 60, 30: 50}
d = a | b
print(d)   # {10: 60, 30: 50}

#  sum()  function demo  program  (Home  work)
a = {10 : 20 , 30 : 40 , 50 : 60}
print(sum(a . keys()))#90
print(sum(a . values()))#120
print(sum(a))#90
print(sum(a . items()))#error can't add items


max()  and  min()   functions  demo  program  (Home  work)
a = {10 : 20 , 30 : 25 , 40 : 5 , 7 : 28 , 9 : 50}
print(max(a . keys()))#40
print(min(a . keys()))#9
print(max(a . values()))#50
print(min(a . values()))#5
print(max(a . items()))40,5
print(min(a . items()))#7,28
print(max(a))#40
print(min(a))#7

# dict() function demo program (Homework)
a = [(10, 'Hyd'), (20, 'Sec'), (15, 'Cyb'), (20, 'Pune')]
b = dict(a)
print(b)  #{10: 'Hyd', 20: 'Pune', 15: 'Cyb'}
c = (['R', 'Red'], ['G', 'Green'], ['B', 'Blue'], ['G', 'Gray'])
d = dict(c)
print(d)#: {'R': 'Red', 'G': 'Gray', 'B': 'Blue'}
e = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
# print(dict(e))  # error
f = [[10], [20], [30]]
# print(dict(f))  # error
# print(dict([10, 20]))  # error
g = [[10, [20, 30]], [40, [50, 60]], [70, [80, 90]]]
print(dict(g))#{10: [20, 30], 40: [50, 60], 70: [80, 90]}
h = [[[10, 20], 30], [[40, 50], 60], [[70, 80], 90]]
# print(dict(h))  # error



# sorted()  function  (Home  work)
a = {10: 'Red', 20: 'Green', 15: 'Blue', 18: 'Yellow', 5: 'White'}
b = sorted(a.keys())
print(b) #[5, 10, 15, 18, 20]
c = sorted(a.values())
print(c) #['Blue', 'Green', 'Red', 'White', 'Yellow']
d = sorted(a.items())
print(d)#[(5, 'White'), (10, 'Red'), (15, 'Blue'), (18, 'Yellow'), (20, 'Green')]
f = sorted(a, reverse=True)
print(f) # [20, 18, 15, 10, 5]

print(a)#{10: 'Red', 20: 'Green', 15: 'Blue', 18: 'Yellow', 5: 'White'}

# clear()  method  demo  program (Home  work)
a = {10 : 20 , 30 : 40 , 50 : 60}
print(a)# {10 : 20 , 30 : 40 , 50 : 60}
a . clear()
print(a){}
del  a#
print(a)#error


# copy()  method demo  program  (Home  work)
a = {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue'}
b = a . copy()
print(b)#{'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue'}
print(a  is  b)#false
print(a  ==  b)#true

#  keys()  method  demo  program
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
b = a . keys()
print(b)#[10,20,15,18]
print(type(b))# class 'list'
for  x  in   b:
        print(x)
#10
20
30
40


# values()  method  demo  program
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
b = a . values()
print(b)#[hyd,sec,cyb,pune]
print(type(b))#class list
for  x   in   b:
	print(x)#hyd
Sec
Cyd
Pune



#  items()  method  demo  program
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
b = a . items()
print(b)#{10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
print(type(b))
for  x   in   b:
        print(x)#hyd
Sec
Cyd
Pune


for  x , y   in  b:
        print(x , y , sep = ' ... ')
#10 :'Hyd' ... 20 : 'Sec'... , 15 : 'Cyb'..., 18 : 'Pune'...}

#  Find  outputs  (Home  work)
a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh'}
x , y , z = a . keys()10
print(x)#10
print(y)#20
print(z)#15
print()# empty line
x , y , z = a . values()
print(x)#rama
print(y)#sita
print(z)#rajesh
print()# empty line
x , y ,  z = a . items()
print(x)#10 : 'Rama
print(y)#20 : 'Sita'
print(z)#15 : 'Rajesh
print()#empty line
(rno1 , sname1) , (rno2 , sname2) , (rno3 , sname3) = a . items()
print(rno1 , sname1)#10,rama
print(rno2 , sname2)#20,sita
print(rno3 , sname3)#15,rajesh

'''
(Home  work)
Write  a  program  to  remove  duplicate  characters  of  the  string  using  set

1) Let  input  be   Rama  Rao
    What  is  the  output  ? --->  Ram<space>o

2) Both  input  and  output  are  strings

s = input("enter a string:")
a= "".join(set(s))
print("After Removing Duplicates:",a)
enter a string: rama rao
After removing duplicates :
 rm ao

'''
Write  a  program  to  remove  duplicate  elements  of   list  using  set

1) Let  input  be  [False , 25 , 10.8 , 1  , 25 , 0 , 'Hyd' ,  10.8 , 1.0 , None , 'Sec' , 'Hyd' , True  ]
    What  is  the  output ?  ---> [False , 25 , 10.8 , 1 , 'Hyd' , None , 'Sec']

2) Both  input  and  output  are  lists
'''
a = eval(input("enter a list: "))
result = list(set(a))
print("list after removing duplicates:", result)
enter a list:  [False , 25 , 10.8 , 1  , 25 , 0 , 'Hyd' ,  10.8 , 1.0 , None , 'Sec' , 'Hyd' , True  ]
list after removing duplicates: [False, 1, None, 10.8, 25, 'Sec', 'Hyd']

#obtaining common elements between 2 lists
a=eval(input("enter list: "))
b=eval(input("enter 2Nd list:"))
c=set(a).intersection(set(b))
print(list(c))                                                                                                                                   enter list: [10,20,30,40,50,60]
enter 2Nd list:[30,40,70,80,20]
[40, 20, 30]

#Write  a  program  to  create  a  dictionary  with  emp  names  and  salaries

a=int(input("how many employees: "))
s={}
i=0
for i in range(a):
     key=input("enter emp name:")
     value=input("enter salary :")
     s[key]=value
print(s)                                                                                                                                                    how many employees: 4
enter emp name:sravani
enter salary :1000000
enter emp name:padma
enter salary :200000
enter emp name:nagu
enter salary :300000
enter emp name:mahesh
enter salary :500000
{'sravani': '1000000', 'padma': '200000', 'nagu': '300000', 'mahesh': '500000'}

'''
Tricky  program
Write  a  program  to  sort  dictionary  wrt  keys  (Home  work)

1) Let  input  be   {10 : 'A' , 20 : 'B' , 15 : 'C' , 5 : 'D' , 12 : 'E'}
    What  is  the  output ?  ---> {5 : 'D' , 10 : 'A' ,  12 : 'E' ,  15 : 'C' , 20 : 'B'}

2) Both  input  and  output  are  dictionaries

3) Hint:  Use  sorted()  function
'''

#Write  a  program  to sort dictionary wrt keys
 
data = eval(input("Enter dictionary: "))
sorted_dict = {}
for k in sorted(data):
    sorted_dict[k] = data[k]

print("Input  :", data)
print("Output :", sorted_dict)                                                                                            Enter dictionary: {10:'A',20:'B',15:'C',5:'D',12:'E'}
Input  : {10: 'A', 20: 'B', 15: 'C', 5: 'D', 12: 'E'}
Output : {5: 'D', 10: 'A', 12: 'E', 15: 'C', 20: 'B'}

s=input("enter a string:")
s=s.upper()
b=sorted(s)
a={}
for i in b:
   if i.isalpha():
      a[i]=a.get(i,0)+1
print(a)                                                                                                                                                    enter a string:rAma raO
{'A': 3, 'M': 1, 'O': 1, 'R': 2}

#  How  to  access  values  of  dictionary (Home  work)
a  =  {'Empno'  :  25 ,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(How  to  print  value  25  in  dict  'a')#a.values()
print(How  to  print  'Rama Rao'  in  dict  'a')#a[ename]
print(How  to  print  value  1000.65   in  dict  'a')#a[sal]


# How  to  modify  values  of  dictionary  (Home  work)
a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a)#{'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(id(a))#address of object a
How  to  modify  1000.65  to  2000#a[sal]=2000
How  to  modify  'Rama  Rao'  to  'Sita'#a[ename]=sita
How  to  modify  25   to  35#a[empno]=35
print(a)#{'Empno'  :  35,  'Ename'  :  'sita'  ,  'Sal'  :  2000  }
print(id(a))# address of a will be changed 


 #  How  to  append  key : value  pairs  to dictionary  (Home  work)
a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a)#{'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
How  to  append  'Gender' : 'M'  to  dictionary  'a'
How  to  append  'Married' : a['Gender'] = 'M'
a['Married'] = True
 True  to  dictionary  'a'
print(a)#{'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65 ,'gender'='M','married'='true' }