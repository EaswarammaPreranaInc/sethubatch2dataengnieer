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
print(a) # {True , 25 , 10.8 , 'Hyd' , None} can be any order
a . add(10 , 20 , 30) # {True , 25 , 10.8 , 'Hyd' , None , (10 , 20 , 30)} can be any order
a . add([10,20,30]) # error as set cannot hold mutable elements

# Find  outputs  (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
tpl = (10 , 20 , 30)
print(a) # {25 , 10.8 , 'Hyd' , True} can be any order
print(id(a)) # address of set a
a . add(tpl) 
a . add('Sec')
print(a) # {25 , 10.8 , 'Hyd' , True , (10 , 20 , 30) , 'Sec'}
print(id(a)) # address of set a
print(len(a)) # 6
a . add([100 , 200 , 300]) # error as set cannot hold mutable elements
a . add(set()) # error as set cannot hold mutable elements
a . add({ }) # error as set cannot hold mutable elements


# Find  outputs (Home  work)
s = set()
tpl = (10 , 20 , 15 , 18)
s . add(tpl)
print(s) # {(10 , 20 , 15 , 18)}
print(len(s)) # 1


# update()  method  demo program  (Home  work)
tpl = (10 , 20 , 15, 18 , 10 , 20)
s = set()
s . update(tpl)
print(len(s)) # 4
print(s) # {10 , 20 , 15 , 18}
s . update(25) # error agument  should  be  sequence  only

# Find  outputs  (Home  work)
a = [10 , 20 , 30]
b = {30 , 40,50 }
c = (50 , 60 , 70)
s = set()
s . update(a , b , c)
print(s) # {10 , 20 , 30 , 40 , 50 , 60 , 70} can be any order
print(len(s)) # 7
s . add(a , b , c) # error as add method argument should be only 1

# Find  outputs  (Home  work)
a = set()
a . update('Rama Rao')
print(a) # {'R' , 'a' , 'm' , 'o' , ' '}
print(len(a)) # 5
a . update(3 + 4j , 10.8 , True) # error as argument should be sequence only


# copy()  method  demo  program  (Home  work)
a = {10 , 20 , 15 , 18}
print(a) # {10 , 20 , 15 , 18}
b = a . copy()
print(b) # {10 , 20 , 15 , 18}
print(a  is  b) # False
print(a  ==  b) # True
c = a
print(a  is  c) # True



# pop()  method  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
print(a) # {25 , 10.8 , 'Hyd' , True}
print(a . pop()) # 25
print(a . pop()) # 10.8
print(a . pop()) # 'Hyd'
print(a . pop()) # True
print(a . pop()) # error as there are no elements to delete
print(a) # set()
b = {10 , 20 , 30 , 40}
print(b . pop(2)) # error as set does not have indexes


# remove()  method  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
print(a) # {25 , 10.8 , 'Hyd' , True}
a . remove('Hyd') 
print(a) # {25 , 10.8 , True}
a . remove('Sec') # error as there is no Sec in the set


# discard()  method  demo  program (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
print(a) # {25 , 10.8 , 'Hyd' , True}
a . discard('Hyd')
print(a) # {25 , 10.8 , True}
a . discard('Sec')
print(a) #  {25 , 10.8 , True}
a . remove('Sec') # error as Sec is not in the list

# clear()  method  demo  program (Home  work)
a = {10 , 20 , 15 , 18}
print(a) # {10 , 20 , 15 , 18}
a . clear()
print(a) # set()
print(len(a)) # 0


# Find  outputs  (Home work)
a = {10 , 20 , 30 , 40}
b = [30 , 40 , 50 , 60]
print(a . union(b)) # {10 , 20 , 30 , 40 , 50 , 60} can be any order
print(a | b) # error concatenation cannot be between set and list with pipe operator
print(b . union(a)) # error list does not have union method
print(a + b)  # error concatenation cannot be between set and list with + operator



