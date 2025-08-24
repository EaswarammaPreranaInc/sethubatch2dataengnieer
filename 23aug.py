1. 
# add()  method  demo  program  (Home  work)
a = set()
a . add(True) #(True,)
a . add(25)
a . add(10.8)
a . add(1)
a . add('Hyd')
a . add(25)
a . add(None)
a . add('Hyd')
a . add(1.0)
print(a)   #{True, 10.8, 25, 'Hyd', None}we get set of elements in unordered, set removes duplicates
a . add(10 , 20 , 30) #error, add cannot add multiple elemts at a time 
a . add([10,20,30]) #error, list is mutable hence it will not fit in set


2.
# Find  outputs  (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
tpl = (10 , 20 , 30)
print(a)  #{25 , 10.8 , 'Hyd' , True}
print(id(a))  #address of set
a . add(tpl)  #{True, 'Hyd', 10.8, (10, 20, 30), 25}
a . add('Sec') #{True, 'Hyd', 'Sec', 10.8, (10, 20, 30), 25}
print(a)  #{True, 'Hyd', 'Sec', 10.8, (10, 20, 30), 25}
print(id(a))  #address of set
print(len(a)) #6
a . add([100 , 200 , 300])  #error, list is mutable and cannot fit in set
a . add(set()) #error set
a . add({ }) #error dict


3.
# Find  outputs (Home  work)
s = set()
tpl = (10 , 20 , 15 , 18)
s . add(tpl)
print(s)   #{(10 , 20 , 15 , 18)}
print(len(s))  #1


4.
# update()  method  demo program  (Home  work)
tpl = (10 , 20 , 15, 18 , 10 , 20)
s = set()
s . update(tpl)  #s.update((10 , 20 , 15, 18 , 10 , 20))= set(10 , 20 , 15, 18 , 10 , 20)={10 , 20 , 15, 18}
print(len(s))   #4
print(s) # {10 , 20 , 15, 18}
s . update(25)   #{10 , 20 ,25, 15, 18}


5.
# Find  outputs  (Home  work)
a = [10 , 20 , 30]
b = {30 , 40,50 }
c = (50 , 60 , 70)
s = set()   
s . update(a , b , c)#s=set([10 , 20 , 30],{30 , 40,50 },(50 , 60 , 70) )
print(s)  #{10,20,30,40,50,60,70}  order may not be same, in any order
print(len(s)) #7
s . add(a , b , c)   #error, set.add takes only 1 element, here it has taken 3 elements


6.
# Find  outputs  (Home work)
a = {10 , 20 , 30 , 40}   #set
b = [30 , 40 , 50 , 60]   #list
print(a . union(b))   #{10,20,30,40,50,60} in any order
print(a | b)  #error:unsupported
print(b . union(a))  #error: b is list and list do not have union method, 
print(a + b)  #error: set does not support concatenation


7.
# Find  outputs  (Home  work)
a = set()
a . update('Rama Rao')
print(a) #set('Rama Rao')={'R','a','m',' ','o'} in any order
print(len(a))  #5
a . update(3 + 4j , 10.8 , True) #{'R','a','m',' ','o', 3+4j, 10.8, True} in any order


8.
a = {10 , 20 , 15 , 18}  #set
print(a)   #{10 , 20 , 15 , 18} in any order
b = a . copy()  #{20,10,18,15}  in any order shallow copy
print(b)   #{20,10,18,15}  in any order shallow copy
print(a  is  b)   #False  #
print(a  ==  b)   #True   #both sets contains same elements
c = a  #  c={10 , 20 , 15 , 18}
print(a  is  c)  #True




9.
a = {25 , 10.8 , 'Hyd' , True}
print(a)   #{25 , 10.8 , 'Hyd' , True}       #in any order
print(a . pop())  #1st element will be deleted and returns 1st element in o/p i.e. 25
print(a . pop())  #  "
print(a . pop())  #  "
print(a . pop())  @  "
print(a . pop())  #error as there are no elemts left, all 4 elements deleted in set and it is an empty set i.e. set()
print(a)  #set()
b = {10 , 20 , 30 , 40}
print(b . pop(2))   #error: if we mention 2 it doesn't delete 2nd argument, pop doesn't take arguments, it directly deleted 1 st element of set
print(b) # {10 , 20 , 30 , 40}



10.

a = {25 , 10.8 , 'Hyd' , True}
print(a)   #{25 , 10.8 , 'Hyd' , True} in any order
a . remove('Hyd')  #{25 , 10.8 , True}
print(a)   ##{25 , 10.8 , True}
a . remove('Sec')  #error, there is no elemnt names Sec in the set


11.
a = {25 , 10.8 , 'Hyd' , True}
print(a)   #{25 , 10.8 , 'Hyd' , True} in any order
a . discard('Hyd')  #{25 , 10.8, True}
print(a)  ##{25 , 10.8, True}
a . discard('Sec')  #there is no element names Sec in the set, discard doesn't give error for it, it remains calm
print(a) #{25 , 10.8, True}
a . remove('Sec') #error, unlike discard, remove doesn't sit calm even if there is no Sec. It raises error.

12.

a = {10 , 20 , 15 , 18}
print(a)   #{10 , 20 , 15 , 18} in any order
a . clear()   #clears all elements in set makes it empty set
print(a)  #set()
print(len(a))  #0






