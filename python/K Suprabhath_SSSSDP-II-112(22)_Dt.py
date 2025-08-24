# add()  method  demo  program  (Home  work)
a = set()
a . add(True)# True  is  equal  to  1
a . add(25)# int  value
a . add(10.8)# float  value
a . add(1)# 1  is  equal  to  True
a . add('Hyd')# duplicate  value
a . add(25)# duplicate  value
a . add(None)# None  is  allowed
a . add('Hyd')# duplicate  value
a . add(1.0)# 1.0  is  equal  to  1
print(a)# {None, True, 10.8, 25, 'Hyd'}
a . add(10 , 20 , 30)# TypeError
a . add([10,20,30])# TypeError

# Find  outputs  (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
tpl = (10 , 20 , 30)
print(a)# {True, 10.8, 25, 'Hyd'}
print(id(a))# address of set
a . add(tpl)
a . add('Sec')
print(a)# {True, 10.8, 25, (10, 20, 30), 'Hyd', 'Sec'}
print(id(a))#address  of  set
print(len(a))# 6
a . add([100 , 200 , 300])# TypeError
a . add(set())#empty  set  is  not  allowed
a . add({ })# TypeError

# Find  outputs (Home  work)
s = set()
tpl = (10 , 20 , 15 , 18)
s . add(tpl)# adding  tuple
print(s)# {(10, 20, 15, 18)}
print(len(s))# 1

# update()  method  demo program  (Home  work)
tpl = (10 , 20 , 15, 18 , 10 , 20)
s = set()
s . update(tpl)
print(len(s))# 4
print(s)# {10, 18, 20, 15}
s . update(25)# TypeError

# Find  outputs  (Home  work)
a = [10 , 20 , 30]
b = {30 , 40,50 }
c = (50 , 60 , 70)
s = set()
s . update(a , b , c)
print(s)# {70, 10, 40, 50, 20, 60, 30}
print(len(s))# 7
s . add(a , b , c)# TypeError

# Find  outputs  (Home  work)
a = set()
a . update('Rama Rao')
print(a)# {' ', 'R', 'a', 'm', 'o'}
print(len(a))# 8
a . update(3 + 4j , 10.8 , True)# TypeError
           
# copy()  method  demo  program  (Home  work)
a = {10 , 20 , 15 , 18}
print(a)# {10, 18, 20, 15}
b = a . copy()
print(b)# {10, 18, 20, 15}
print(a  is  b)# False
print(a  ==  b)# True
c = a
print(a  is  c)# True

# pop()  method  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
print(a)# {True, 10.8, 25, 'Hyd'}
print(a . pop())# True
print(a . pop())# 10.8
print(a . pop())# 25
print(a . pop())# 'Hyd'
print(a . pop())# KeyError
print(a)# set()
b = {10 , 20 , 30 , 40}
print(b . pop(2))# TypeError

# remove()  method  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
print(a)# {True, 10.8, 25, 'Hyd'}
a . remove('Hyd')
print(a)# {True, 10.8, 25}
a . remove('Sec')

# discard()  method  demo  program (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
print(a)# {True, 10.8, 25, 'Hyd'}
a . discard('Hyd')
print(a)# {True, 10.8, 25}
a . discard('Sec')
print(a)# {True, 10.8, 25}
a . remove('Sec')

# clear()  method  demo  program (Home  work)
a = {10 , 20 , 15 , 18}
print(a)# {10, 18, 20, 15}
a . clear()
print(a)# set()
print(len(a))# 0

# Find  outputs  (Home work)
a = {10 , 20 , 30 , 40}
b = [30 , 40 , 50 , 60]
print(a . union(b))# {10, 20, 30, 40, 50, 60}
print(a | b)# TypeError
print(b . union(a))# {10, 20, 30, 40, 50, 60}
print(a + b)# TypeError
