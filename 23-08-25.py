
# add()  method  demo  program  (Home  work)
a = set()
a . add(True)#{True}
a . add(25)#{25,True} in any order
a . add(10.8)#{True,25,10.8} in any order
a . add(1)#{True,25,10.8} in any order
a . add('Hyd')#{True,25,'Hyd',10.8} in any order
a . add(25)#duplicate elements are not permitted
a . add(None)#{True,25,'Hyd',None,10.8} in any order
a . add('Hyd')
a . add(1.0)#{True,25,'Hyd',None,10.8} in any order
print(a)#{True,25,'Hyd',None,10.8} in any order
#a . add(10 , 20 , 30)#Error set takes one arguement only
#a . add([10,20,30])#Error set cannot contain mutable elemnts

#2nd program
# Find  outputs  (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
tpl = (10 , 20 , 30)
print(a)#{25 , 10.8 , 'Hyd' , True}
print(id(a))#address of the set {25 , 10.8 , 'Hyd' , True}
a . add(tpl)#{25 , 10.8 ,(10 , 20 , 30), 'Hyd' , True} in any oreder
a . add('Sec')#{25 , 10.8, 'sec',(10 , 20 , 30), 'Hyd' , True} in any oreder
print(a)#{25 , 10.8, 'sec',(10 , 20 , 30), 'Hyd' , True} in any oreder
print(id(a))#Address of the set{25 , 10.8, 'sec',(10 , 20 , 30), 'Hyd' , True} 
#a . add(set())#Error
#a.add({})#Error 


#3rd program# Find  outputs (Home  work)
s = set()
tpl = (10 , 20 , 15 , 18)
s . add(tpl)
print(s)#{(10 , 20 , 15 , 18)}
print(len(s))#1


#4th program
# update()  method  demo program  (Home  work)
tpl = (10 , 20 , 15, 18 , 10 , 20)
s = set()
s . update(tpl)#{10 , 20 , 15, 18 }
print(len(s))#4
print(s)#{10 , 20 , 15, 18 , 10 , 20}
#s . update(25)#Error non sequence connot be added

#5th program
# Find  outputs  (Home  work)
a = [10 , 20 , 30]
b = {30 , 40,50 }
c = (50 , 60 , 70)
s = set()#{10 , 20 , 30, 40, 50, 60 , 70}
s . update(a , b , c)#{10 , a, 20 , 30, b, 40, 50, 60 , c, 70}
print(s)#{10 , a, 20 , 30, b, 40, 50, 60 , c, 70}
print(len(s))#10
#s . add(a , b , c)#Error takes one arguement only


#6th program
# Find  outputs  (Home  work)
a = set()
a . update('Rama Rao')#{'R', 'a', 'm', ' ', 'o'} in any order
print(a)#{'R', 'a', 'm', ' ', 'o'} 
print(len(a))#5
a . update(3 + 4j , 10.8 , True)#Error non sequence connot be added

#7th program
# copy()  method  demo  program  (Home  work)
a = {10 , 20 , 15 , 18}
print(a)#{10 , 20 , 15 , 18}
b = a . copy()
print(b)#{10 , 20 , 15 , 18}
print(a  is  b)#False
print(a  ==  b)#True
c = a
print(a  is  c)#True


#8th program
# pop()  method  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
print(a)#{25 , 10.8 , 'Hyd' , True} in any order
print(a . pop())#25
print(a . pop())#10.8
print(a . pop())#'Hyd'
print(a . pop())#True
print(a . pop())#Error
print(a)#set()
b = {10 , 20 , 30 , 40}
print(b . pop(2))#Error set does not support indexing


#9th program
# remove()  method  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
print(a)#{25 , 10.8 , 'Hyd' , True} in any order
a . remove('Hyd')
print(a)#{25 , 10.8 , True}
a . remove('Sec')#Error


#10th program
# discard()  method  demo  program (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
print(a)#{25 , 10.8 , 'Hyd' , True} in any order
a . discard('Hyd')
print(a)#{25 , 10.8 , True}
a . discard('Sec')#nothing
print(a)#{25 , 10.8 , True}
a . remove('Sec')#Error


#11th program
# clear()  method  demo  program (Home  work)
a = {10 , 20 , 15 , 18}
print(a)#{10 , 20 , 15 , 18}
a . clear()#set()
print(a)#set()
print(len(a))#0


#12th program
# Find  outputs  (Home work)
a = {10 , 20 , 30 , 40}
b = [30 , 40 , 50 , 60]
print(a . union(b))#{10 , 20 , 30 , 40 , 50 , 60}
print(a | b)#{10 , 20 , 30 , 40 , 50 , 60}
print(b . union(a))#{10 , 20 , 30 , 40 , 50 , 60}
print(a+b)#Error set does not support concatenation




