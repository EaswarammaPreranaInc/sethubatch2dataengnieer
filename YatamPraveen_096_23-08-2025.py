# add()  method  demo  program  (Home  work)
a = set()
a . add(True)			#Adds True into empty set
a . add(25)			#Adds 25 to set
a . add(10.8)			#Adds 10.8 into set
a . add(1)			#Doesn't add 1 as True is already present
a . add('Hyd')			#Adds 'Hyd' into set
a . add(25)			#Doesn't add 25 as it is already present
a . add(None)			#Adds None to set
a . add('Hyd')			#Doesn't add 'Hyd' as it is already present
a . add(1.0)			#Doesn't add 1.0 as True is already present
print(a)			#{True, 25, 10.8, 'Hyd', None}
a . add(10 , 20 , 30)		#Throws error as add can only take one argument
a . add([10,20,30])		#Throws error as list can't be added as an element to set





# Find  outputs  (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
tpl = (10 , 20 , 30)
print(a)                    #{25 , 10.8 , 'Hyd' , True}
print(id(a))                #Address of set a
a . add(tpl)
a . add('Sec')
print(a)                    #{25, 10.8, 'Hyd', True, (10, 20, 30), 'Sec'}
print(id(a))                #Same address as previous
print(len(a))               #6
a . add([100 , 200 , 300])  #List, which is a mutable, can't be added to a set. So throws error
a . add(set())              #Set, which is a mutable, can't be added to a set. So throws error
a . add({ })                #Dictionary, which is a mutable, can't be added to a set. So throws error





# Find  outputs (Home  work)
s = set()
tpl = (10 , 20 , 15 , 18)
s . add(tpl)
print(s)                #{(10,20,15,18)}
print(len(s))           #1





# update()  method  demo program  (Home  work)
tpl = (10 , 20 , 15, 18 , 10 , 20)
s = set()
s . update(tpl)
print(len(s))           #4
print(s)                #{10, 18, 20, 15}
s . update(25)          #Throws error as update can't have non sequence as argument





# Find  outputs  (Home  work)
a = [10 , 20 , 30]
b = {30 , 40,50 }
c = (50 , 60 , 70)
s = set()
s . update(a , b , c)
print(s)                    #{10, 20, 30, 40, 50, 60, 70}
print(len(s))               #7
s . add(a , b , c)          #Throws error as add takes only one argument





# Find  outputs  (Home  work)
a = set()
a . update('Rama Rao')
print(a)                                #{'R', 'a', 'm', ' ', 'o'}
print(len(a))                           #5
a . update(3 + 4j , 10.8 , True)        #Throws error as update can't have non sequence as argument





# copy()  method  demo  program  (Home  work)
a = {10 , 20 , 15 , 18}
print(a)                #{10 , 20 , 15 , 18}
b = a . copy()
print(b)                #{10 , 20 , 15 , 18}
print(a  is  b)         #False
print(a  ==  b)         #True
c = a
print(a  is  c)         #True





# pop()  method  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
print(a)                        #{25, 10.8, 'Hyd', True}
print(a . pop())                #25
print(a . pop())                #10.8
print(a . pop())                #Hyd
print(a . pop())                #True
print(a . pop())                #Throws error as set now doesn't have any elements left
print(a)                        #set()
b = {10 , 20 , 30 , 40}
print(b . pop(2))               #pop can't take any arguments wrt set as set is not indexed. So this throws error





# remove()  method  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
print(a)                    #{25 , 10.8 , 'Hyd' , True}
a . remove('Hyd')
print(a)                    #{25 , 10.8 , True}
a . remove('Sec')           #Throws error as set doesn't have 'Sec'





# discard()  method  demo  program (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
print(a)                #{25 , 10.8 , 'Hyd' , True}
a . discard('Hyd')
print(a)                #{25 , 10.8 , True}
a . discard('Sec')
print(a)                #{25 , 10.8 , True}
a . remove('Sec')       #Throws error as set doesn't have 'Sec'





# clear()  method  demo  program (Home  work)
a = {10 , 20 , 15 , 18}
print(a)                #{10 , 20 , 15 , 18}
a . clear()
print(a)                #set()
print(len(a))           #0





# Find  outputs  (Home work)
a = {10 , 20 , 30 , 40}
b = [30 , 40 , 50 , 60]
print(a . union(b))         #{10, 20, 30, 40, 50, 60}
print(a | b)                #Throws error as | can only be used with sets not with any other
print(b . union(a))         #Throws error as list doesn't have union method
print(a + b)                #Throws error as + can't be used with sets
