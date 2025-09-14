# add()  method  demo  program  (Home  work)
a = set()
a . add(True)#{True}
a . add(25)#{25,True}
a . add(10.8)#{25,True,10.8}
a . add(1)# already true are there {25,True,10.8}
a . add('Hyd')#{25,True,Hyd,10.8}
a . add(25)#{25,True,Hyd,10.8}
a . add(None)#{25,True,Hyd,None,10.8}
a . add('Hyd')#{25,True,Hyd,None,10.8}
a . add(1.0)#{25,True,Hyd,None,10.8}
print(a)##{25,True,Hyd,None,10.8}
a . add(10 , 20 , 30)#Error
a . add([10,20,30])#Error


# Find  outputs  (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
tpl = (10 , 20 , 30)
print(a)#{25 , 10.8 , 'Hyd' , True}
print(id(a))#class set
a . add(tpl)#{25 , 10.8 , 'Hyd' , (10 , 20 , 30),True}
a . add('Sec')#{25 , 10.8 , 'Hyd' , (10 , 20 , 30),True,sec}
print(a)#{25 , 10.8 , 'Hyd' , (10 , 20 , 30),True,sec}
print(id(a))# class set
print(len(a))#6
a . add([100 , 200 , 300])#Error
a . add(set())#Error
a . add({ })#Error

# Find  outputs (Home  work)
s = set()
tpl = (10 , 20 , 15 , 18)
s . add(tpl)
print(s)#{ (10 , 20 , 15 , 18)}
print(len(s))#4

# update()  method  demo program  (Home  work)
tpl = (10 , 20 , 15, 18 , 10 , 20)
s = set()
s . update(tpl)#{10 , 20 , 15, 18}
print(len(s))#4
print(s)#{10 , 20 , 15, 18}
s . update(25)#Error

# Find  outputs  (Home  work)
a = [10 , 20 , 30]
b = {30 , 40,50 }
c = (50 , 60 , 70)
s = set()
s . update(a , b , c)
print(s)# {10, 20, 30, 40, 50, 60, 70}
print(len(s))#7
s . add(a , b , c)#Error

# Find  outputs  (Home  work)
a = set()
a . update('Rama Rao')
print(a)# {R,a,m,' ',o}
print(len(a))#5
a . update(3 + 4j , 10.8 , True)#Error

# copy()  method  demo  program  (Home  work)
a = {10 , 20 , 15 , 18}
print(a)# {10 , 20 , 15 , 18}
b = a . copy()
print(b)#= {10 , 20 , 15 , 18}
print(a  is  b)#False
print(a  ==  b)#True
c = a
print(a  is  c)# True


# pop()  method  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
print(a)#{25 , 10.8 , 'Hyd' , True}
print(a . pop())#25
print(a . pop())#10.8
print(a . pop())#hyd
print(a . pop())#True
print(a . pop())#Error
print(a)
b = {10 , 20 , 30 , 40}
print(b . pop(2))#Error


# remove()  method  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
print(a)#{25 , 10.8 , 'Hyd' , True}
a . remove('Hyd')#{25 , 10.8, True}
print(a)#{10.8 ,25, True}
a . remove('Sec')#Error

# discard()  method  demo  program (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
print(a)#{25 , 10.8 , 'Hyd' , True}
a . discard('Hyd')
print(a)#{25 , 10.8, True}
a . discard('Sec')
print(a)#{25, 10.8, True}
a . remove('Sec')# Error

# clear()  method  demo  program (Home  work)
a = {10 , 20 , 15 , 18}
print(a)#{10 , 20 , 15 , 18}
a . clear()
print(a)#set()
print(len(a))#0

# Find  outputs  (Home work)
a = {10 , 20 , 30 , 40}
b = [30 , 40 , 50 , 60]
print(a . union(b))#{10, 20, 30, 40, 50, 60}
print(a | b)#TypeError
print(b . union(a))#AttributeError
print(a + b)#TypeError






