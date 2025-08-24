# 1) add()  method  demo  program  (Home  work)

a = set()
a . add(True) # add method inserts the element in the set
a . add(25)
a . add(10.8)
a . add(1)
a . add('Hyd')
a . add(25)
a . add(None)
a . add('Hyd')
a . add(1.0)
print(a) # Output: {None, True, 10.8, 25, 'Hyd'} 
a . add(10 , 20 , 30) # Error as add method take only one argument
a . add([10,20,30]) # Error as we can't add list to set  because set take only immutable object 



# 2) Find  outputs  (Home  work)

a = {25 , 10.8 , 'Hyd' , True}
tpl = (10 , 20 , 30)
print(a) # Output: {25, 10.8, 'Hyd', True}
print(id(a)) # Output: address of the set {25, 10.8, 'Hyd', True}
a . add(tpl)
a . add('Sec')
print(a) # Output: {True, 'Sec', 10.8, (10, 20, 30), 25, 'Hyd'}
print(id(a)) # Output: same address of the set 
print(len(a)) # Output: 6
a . add([100 , 200 , 300]) # Error as we can't add list to set  because set take only immutable object 
a . add(set()) # Error as we can't add list to set  because set take only immutable object 
a . add({ }) # Error as we can't add list to set  because set take only immutable object 



# 3) Find  outputs (Home  work)

s = set()
tpl = (10 , 20 , 15 , 18)
s . add(tpl)
print(s) # Output: {(10, 20, 15, 18)}
print(len(s)) # Output: 1





# 4) update()  method  demo program  (Home  work)

tpl = (10 , 20 , 15, 18 , 10 , 20)
s = set()
s . update(tpl) # update method inserts sequence anywhere in the set 
print(len(s)) # Output: 4
print(s) # Output: {10, 18, 20, 15}
s . update(25) # Error as update method argument should be sequence only



# 5) Find  outputs  (Home  work)

a = [10 , 20 , 30]
b = {30 , 40,50 }
c = (50 , 60 , 70)
s = set()
s . update(a , b , c) # update method inserts sequence anywhere in the set 
print(s) # Output: {50, 20, 70, 40, 10, 60, 30}
print(len(s)) # Output: 7
s . add(a , b , c) # Error as add method take only one argument



# 6) Find  outputs  (Home  work)

a = set()
a . update('Rama Rao')
print(a) # Output: {' ', 'o', 'a', 'm', 'R'}
print(len(a)) # Output: 5
a . update(3 + 4j , 10.8 , True) # Error as complex argument is not valid in update method



# 7) copy()  method  demo  program  (Home  work)

a = {10 , 20 , 15 , 18}
print(a) # Output: {10, 18, 20, 15}
b = a . copy() # copy method returns a new set with same elements
print(b) # Output: {10, 18, 20, 15}
print(a  is  b) # Output: False
print(a  ==  b) # Output: True
c = a
print(a  is  c) # Output: True



# 8) pop()  method  demo  program  (Home  work)

a = {25 , 10.8 , 'Hyd' , True} # pop method removes first element of the set and returns the deleted element
print(a) # Output: {25, 10.8, 'Hyd', True}
print(a . pop()) # Output: 25
print(a . pop()) # Output: 10.8
print(a . pop()) # Output: 'Hyd'
print(a . pop()) # Output: True
print(a . pop()) # Error as pop method returns error when set is empty
print(a) # Output: set()
b = {10 , 20 , 30 , 40}
print(b . pop(2)) # Error as we cannot use pop(index) because set is not indexed 



# 9) remove()  method  demo  program  (Home  work)

a = {25 , 10.8 , 'Hyd' , True} # remove method removes element in the set and return error wheen element not found
print(a) # Output: {25, 10.8, True, 'Hyd'}
a . remove('Hyd')
print(a) # Output: {25, 10.8, True}
a . remove('Sec') # Error as 'sec' is not found in the set remove method returns error



# 10) discard()  method  demo  program (Home  work)

a = {25 , 10.8 , 'Hyd' , True} # discard method is same as remove method but it doesn't return error wheen element not found
print(a) # Output: {25, 10.8, True, 'Hyd'}
a . discard('Hyd')
print(a) # Output: {25, 10.8, True}
a . discard('Sec')
print(a) # Output: {25, 10.8, True}
#a . remove('Sec') # Error as 'sec' is not found in the set remove method returns error



# 11) clear()  method  demo  program (Home  work)

a = {10 , 20 , 15 , 18} # clear method removes all the elements of set and set becomes empty
print(a) # Output: {10, 18, 20, 15}
a . clear()
print(a) # Output: set()
print(len(a)) # Output: 0



# 12) Find  outputs  (Home work)

a = {10 , 20 , 30 , 40} # Union method concatenate the elements and it gives new set
b = [30 , 40 , 50 , 60]
print(a . union(b)) # Output: {40, 10, 50, 20, 60, 30}
print(a | b) # Error as '|' operator doesn't concatenate set and list
print(b . union(a)) # Error as list doesn't has union method
print(a + b) # Error as '+' operator doesn't concatenate set and list