# add()  method  
a = set()
a . add(True) # insert True to set 'a' in any order
a . add(25) # insert 25 to set 'a' in any order
a . add(10.8)
a . add(1) # Duplicates are not allowed in set . True and 1 are treated as one element.
a . add('Hyd') 
a . add(25)
a . add(None)
a . add('Hyd')
a . add(1.0) # Duplicates are not allowed in set . True and 1 and 1.0 are treated as one element.
print(a) # {True, 10.8, None, 25, 'Hyd'}
#a . add(10 , 20 , 30) # error:add() can take only one argument
#a . add([10,20,30]) # error: cannot add mutable objects to set.

# Find  outputs  
a = {25 , 10.8 , 'Hyd' , True}
tpl = (10 , 20 , 30)
print(a) # {25, 10.8, 'Hyd', True}
print(id(a)) # address of object '{25, 10.8, 'Hyd', True}'
a . add(tpl) # adds the tuple to the set. set allows immutable objects.
a . add('Sec') # adds the string 'sec' to the set
print(a) # {True, 10.8, (10, 20, 30), 'Sec', 25, 'Hyd'}
print(id(a)) # address is same as before
print(len(a)) # 6
#a . add([100 , 200 , 300])
#a . add(set()) # cannot add set to set. set is mutable object
#a . add({ }) # error: dict are mutable.


# Find  outputs 
s = set()
tpl = (10 , 20 , 15 , 18)
s . add(tpl)
print(s) # {(10, 20, 15, 18)}
print(len(s)) # 1


# update()  method  
tpl = (10 , 20 , 15, 18 , 10 , 20)
s = set()
s . update(tpl) 
print(len(s)) # 4 : set doesn't allow duplicates
print(s) # {10, 18, 20, 15}
#s . update(25) # error update argument should be sequence only



# Find  outputs  
a = [10 , 20 , 30]
b = {30 , 40,  50}
c = (50 , 60 , 70)
s = set()
s . update(a , b , c)
print(s) # {50, 20, 70, 40, 10, 60, 30}
print(len(s)) # 7
#s . add(a , b , c) # error : set.add() takes exactly one argument 


# Find  outputs 
a = set()
a . update('Rama Rao')
print(a) # {'o', 'R', 'm', 'a', ' '}
print(len(a)) # 5
#a . update(3 + 4j , 10.8 , True) # update() argument should not be non sequence


# copy()  method  
a = {10 , 20 , 15 , 18}
print(a) # {10, 18, 20, 15}
b = a . copy() # returns a new set 'b' with same elements as 'a'
print(b) # {10, 18, 20, 15}
print(a  is  b) # False
print(a  ==  b) # True
c = a
print(a  is  c) # True


# pop()  method  
a = {25 , 10.8 , 'Hyd' , True}
print(a) # {25, 10.8, 'Hyd', True}
print(a . pop()) # 25 : pop() removes first element of the set and returns the deleted element
print(a . pop()) # 10.8
print(a . pop()) # Hyd
print(a . pop()) # True
#print(a . pop()) # error : because set is empty
print(a) # set()
b = {10 , 20 , 30 , 40}
#print(b . pop(2)) # error: set.pop() has no arguments



# remove()  method  
a = {25 , 10.8 , 'Hyd' , True}
print(a) # {25, 10.8, 'Hyd', True}
a . remove('Hyd') # removes 'hyd' from set 'a'
print(a) # {25, 10.8, True}
#a . remove('Sec') # error : no element 'sec' in set 'a'


# discard()  method 
a = {25 , 10.8 , 'Hyd' , True}
print(a) # {25, 10.8, 'Hyd', True}
a . discard('Hyd') # removes 'Hyd' from set 'a'
print(a) # {25, 10.8, True}
a . discard('Sec') # discard(invalid element) does not raise error nor deletion
print(a) # {25, 10.8, True}
#a . remove('Sec') # Error : remove(invalid element) raises error


# clear()  method  
a = {10 , 20 , 15 , 18}
print(a) # {10, 18, 20, 15}
a . clear() # Removes  all  the  elements  of  set  and  set  becomes  empty
print(a) # set()
print(len(a)) # 0



# Find  outputs  
a = {10 , 20 , 30 , 40}
b = [30 , 40 , 50 , 60]
print(a . union(b)) # {40, 10, 50, 20, 60, 30}
#print(a | b) # error :pipe operator can not concatenate set and list
#print(b . union(a)) # error :There is no union method in list
#print(a + b) # error :cannot add set and list by + operator




