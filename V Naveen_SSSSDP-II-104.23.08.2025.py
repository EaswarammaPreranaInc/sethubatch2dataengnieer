#1. add() method demo program (Home work)
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
print(a) # {True, 25, 10.8, 'Hyd', None}
#a . add(10 , 20 , 30) # Error
#a . add([10,20,30]) # Error



#2. Find outputs (Home work)
a = {25 , 10.8 , 'Hyd' , True}
tpl = (10 , 20 , 30)
print(a) # {25 , 10.8 , 'Hyd' , True}
print(id(a)) # Address of tuple
a . add(tpl) # tuple is added to set
a . add('Sec') 
print(a) # {True, 'Sec', 10.8, 'Hyd', (10, 20, 30), 25}
print(id(a)) # Address of set {True, 'Sec', 10.8, 'Hyd', (10, 20, 30), 25}
print(len(a)) # 6
#a . add([100 , 200 , 300]) # Error
#a . add(set()) # Error
#a . add({ }) # Error






#3. Find outputs (Home work)
s = set()
tpl = (10 , 20 , 15 , 18)
s . add(tpl)
print(s) # {(10, 20, 15, 18)}
print(len(s)) # 1







#4. update() method demo program (Home work)
tpl = (10 , 20 , 15, 18 , 10 , 20)
s = set()
s . update(tpl)
print(len(s)) # 4
print(s) # {10, 20, 15, 18}
#s . update(25) # Error due to update method can take only sequences







#5. Find outputs (Home work)
a = [10 , 20 , 30]
b = {30 , 40,50 }
c = (50 , 60 , 70)
s = set()
s . update(a , b , c) 
print(s) # {50, 20, 70, 40, 10, 60, 30}
print(len(s)) # 7
#s . add(a , b , c) # Error due add method can take only one argument




#6. Find outputs (Home work)
a = set()
a . update('Rama Rao')
print(a) # { 'R', 'a', 'm', 'o', ' '}
print(len(a)) # 5
#a . update(3 + 4j , 10.8 , True) # Error due to update method can take only sequences





#7. copy() method demo program (Home work)
a = {10 , 20 , 15 , 18}
print(a) # {10 , 20 , 15 , 18}
b = a . copy()
print(b) # {10 , 20 , 15 , 18}
print(a is b) # Flase
print(a == b) # True
c = a 
print(a is c) # True








#8. pop() method demo program (Home work)
a = {25 , 10.8 , 'Hyd' , True}
print(a) # {25 , 10.8 , 'Hyd' , True}
print(a . pop()) # 25
print(a . pop()) # 10.8
print(a . pop()) # Hyd
print(a . pop()) # True
#print(a . pop()) # Error due to no elements in set a
print(a) # Set()
b = {10 , 20 , 30 , 40}
#print(b . pop(2)) # Error






#9. remove() method demo program (Home work)
a = {25 , 10.8 , 'Hyd' , True}
print(a) # {25 , 10.8 , 'Hyd' , True}
a . remove('Hyd')
print(a) # # {25 , 10.8 , True}
#a . remove('Sec') # Error due to there is 'sec' in set 'a'








#10. discard() method demo program (Home work)
a = {25 , 10.8 , 'Hyd' , True}
print(a) # {25 , 10.8 , 'Hyd' , True}
a . discard('Hyd')
print(a) # {25 , 10.8 , True}
a . discard('Sec')
print(a) # {25 , 10.8 , True}
#a . remove('Sec') # Error







#11. clear() method demo program (Home work)
a = {10 , 20 , 15 , 18}
print(a) # {10 , 20 , 15 , 18}
a . clear()
print(a) # set()
print(len(a)) # 0






#12. Find outputs (Home work)
a = {10 , 20 , 30 , 40}
b = [30 , 40 , 50 , 60]
print(a . union(b)) # { 10,20,30,40,50,60}
#print(a | b) # Error due to | unsupported between set and other sequences
#print(b . union(a)) # Error due to list does not have union method
#print(a + b) # Error due to set and other sequences are not concatented with '+' operator
