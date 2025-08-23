# add() method demo program
a = set()

a.add(True)       # Adds boolean True
a.add(25)         # Adds integer 25
a.add(10.8)       # Adds float 10.8
a.add(1)          # Adds integer 1 but True is same as 1, so won't add new element)
a.add('Hyd')      # Adds string "Hyd"
a.add(25)         # Duplicate (ignored)
a.add(None)       # Adds None
a.add('Hyd')      # Duplicate (ignored)
a.add(1.0)        # 1.0 is equal to 1 -> won't add new element

print(a)

a.add(10, 20, 30)     # Error -> add() takes exactly one argument
a.add([10, 20, 30])   # Error -> list is mutable, cannot be added to set






# Find  outputs  (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
tpl = (10 , 20 , 30){25, 'Hyd', 10.8, True}
print(a) # {25, 'Hyd', 10.8, True}
print(id(a)) # 135969459491488
a . add(tpl)
a . add('Sec')
print(a) # {'Sec', True, 10.8, (10, 20, 30), 'Hyd', 25}
print(id(a)) # 135969459491488
print(len(a)) # 6
a . add([100 , 200 , 300]) # Error
a . add(set()) # Error
a . add({ }) # Error






# Find  outputs (Home  work)
s = set()
tpl = (10 , 20 , 15 , 18)
s . add(tpl)
print(s) # {(10, 20, 15, 18)}
print(len(s)) # 1






# update()  method  demo program  (Home  work)
tpl = (10 , 20 , 15, 18 , 10 , 20)
s = set()
s . update(tpl)
print(len(s)) # 4
print(s) # {10, 18, 20, 15}
s . update(25) # Error





# Find  outputs  (Home  work)
a = [10 , 20 , 30]
b = {30 , 40,50 }
c = (50 , 60 , 70)
s = set()
s . update(a , b , c)
print(s)  # {50, 20, 70, 40, 10, 60, 30}
print(len(s)) # 7
s . add(a , b , c) # Error add() takes exactly one argument




# Find  outputs  (Home  work)
a = set()
a . update('Rama Rao')
print(a) #  {'R', 'a', ' ', 'm', 'o'}
print(len(a)) # 5
a . update(3 + 4j , 10.8 , True) # Error 'complex' object is not iterable





# copy()  method  demo  program  (Home  work)
a = {10 , 20 , 15 , 18}
print(a) # {10, 18, 20, 15}
b = a . copy()
print(b) # {10, 18, 20, 15}
print(a  is  b) # False
print(a  ==  b) # True
c = a
print(a  is  c) # True





# pop()  method  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
print(a) # {25, 10.8, 'Hyd', True}
print(a . pop()) # 25
print(a . pop()) # 10.8
print(a . pop()) # True
print(a . pop()) # Hyd
print(a . pop()) # Error 'pop from an empty set'
print(a) # set()
b = {10 , 20 , 30 , 40}
print(b . pop(2)) # pop() takes no arguments





# remove()  method  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
print(a) # {25, 10.8, 'Hyd', True}
a . remove('Hyd'){25, 10.8, True}
print(a) # {25, 10.8, True}
a . remove('Sec') # Error no Sec





# discard()  method  demo  program (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
print(a) # {25, 10.8, 'Hyd', True}
a . discard('Hyd')
print(a) # {25, 10.8, True}
a . discard('Sec')
print(a) # {25, 10.8, True}
a . remove('Sec') # Error no Sec





# clear()  method  demo  program (Home  work)
a = {10 , 20 , 15 , 18}
print(a) # {10, 18, 20, 15}
a . clear()
print(a) # set()
print(len(a))  # 0 






# Find  outputs  (Home work)
a = {10 , 20 , 30 , 40}
b = [30 , 40 , 50 , 60]
print(a . union(b)) # {40, 10, 50, 20, 60, 30}
print(a | b) # Error
print(b . union(a)) # Error 'list' object has no attribute 'union'
print(a + b) # Error 