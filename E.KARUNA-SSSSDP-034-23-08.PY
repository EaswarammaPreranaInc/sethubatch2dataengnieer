# add()  method  demo  program  (Home  work)
a = set()
a . add(True)
a . add(25)
a . add(10.8)
a . add(1)
a . add('Hyd')
a . add(25)
a . add(None)
a . add('Hyd')
a . add(1.0)
print(a)#{True,25,10.8,'hyd'}:any order
#a . add(10 , 20 , 30)#Errorset.add()take single argument
#a . add([10,20,30])#error:list is mutable 


# Find  outputs  (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
tpl = (10 , 20 , 30)
print(a)#{25 , 10.8 , 'Hyd' , True}any order
print(id(a))#address of the 'a'
a . add(tpl)#{25 , 10.8 , 'Hyd' , True,(10 , 20 , 30)}
a . add('Sec')
print(a)#{25 , 10.8 , 'Hyd' , True,(10 , 20 , 30),'sec'}
print(id(a))#address of the 'a'
print(len(a))#6
#a . add([100 , 200 , 300])#error list is mutable
#a . add(set())#error set mutable
#a . add({ })#dict is mutable

# Find  outputs (Home  work)
s = set()
tpl = (10 , 20 , 15 , 18)
s . add(tpl)
print(s)#{(10 , 20 , 15 , 18)}
print(len(s))#1

# update()  method  demo program  (Home  work)
tpl = (10 , 20 , 15, 18 , 10 , 20)
s = set()
s . update(tpl)
print(len(s))#4
print(s)#{10 , 20 , 15, 18 } update elements of sequence
#s . update(25)#25 is int i.e non sequence


# Find  outputs  (Home  work)
a = set()
a . update('Rama Rao')
print(a)#{'r','a','m','o',' '}any order
print(len(a))#5
#a . update(3 + 4j , 10.8 , True)#error non sequence


# copy()  method  demo  program  (Home  work)
a = {10 , 20 , 15 , 18}
print(a)#{10 , 20 , 15 , 18} any order
b = a . copy()
print(b)#{10 , 20 , 15 , 18}any order
print(a  is  b)#False
print(a  ==  b)#True
c = a
print(a  is  c)#True

# pop()  method  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
print(a)#{25 , 10.8 , 'Hyd' , True} any order
print(a . pop())#25
print(a . pop())#10.8
print(a . pop())#'Hyd'
print(a . pop())#True
#print(a . pop())#error: empty set.pop()
print(a)#set()
b = {10 , 20 , 30 , 40}
#print(b . pop(2))#error :due to set does not have indexs

# remove()  method  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
print(a)#{25 , 10.8 , 'Hyd' , True} 
a . remove('Hyd')#'hyd' is removed
print(a)#{True,25 , 10.8 }
#a . remove('Sec')#error: invalid element


# discard()  method  demo  program (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
print(a)#{25 , 10.8 , 'Hyd' , True
a . discard('Hyd')#discard 'hyd'
print(a)#{25,10.8,True}
a . discard('Sec')#nothing
print(a)#{25,10.8,True}
#a . remove('Sec')#error


# clear()  method  demo  program (Home  work)
a = {10 , 20 , 15 , 18}
print(a)#{10 , 20 , 15 , 18}
a . clear()#removes the all the elementsof set and set becomes empty
print(a)#empty set i.e set()
print(len(a))#0


# Find  outputs  (Home work)
a = {10 , 20 , 30 , 40}
b = [30 , 40 , 50 , 60]
print(a . union(b))#concanate 'b' and'a'
#print(a | b)
#print(b . union(a))#error list does not have union method
#print(a + b)#error :'+' opertor not supported

