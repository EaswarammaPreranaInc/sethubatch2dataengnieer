# add() method
a = set()
a.add(True)
a.add(25)
a.add(10.8)
a.add(1)
a.add('Hyd')
a.add(25)
a.add(None)
a.add('Hyd')
a.add(1.0)
print(a)              # {True, 25, 10.8, 'Hyd', None}   order may be
# a.add(10,20,30)     #Error
# a.add([10,20,30])   #Error


# add() with tuple
a = {25 , 10.8 , 'Hyd' , True}
tpl = (10 , 20 , 30)
print(a)                               # {25, 10.8, 'Hyd', True}      
print(id(a))                           #address of a
a.add(tpl)
a.add('Sec')
print(a)                               #{25, 10.8, 'Hyd', True, (10, 20, 30), 'Sec'}      
print(id(a))                           #address of a
print(len(a))                          # 6
# a.add([100,200,300])                 #Error
# a.add(set())                         #Error
# a.add({})                            #Error


# add() with tuple inside set
s = set()
tpl = (10 , 20 , 15 , 18)
s.add(tpl)
print(s)                                # {(10, 20, 15, 18)}      
print(len(s))                           #1


# update() method
tpl = (10 , 20 , 15 , 18 , 10 , 20)
s = set()
s.update(tpl)
print(len(s))                          #4
print(s)                               # {10, 20, 15, 18}

# s.update(25)                         #Error


# update() with multiple collections
a = [10 , 20 , 30]
b = {30 , 40 , 50}
c = (50 , 60 , 70)
s = set()
s.update(a , b , c)
print(s)                                  # {10, 20, 30, 40, 50, 60, 70} 

print(len(s))                             #7
# s.add(a , b , c)                        #Error


# update() with string
a = set()
a.update('Rama Rao')
print(a)                                    # {'o', 'a', 'R', 'm', ' ', 'A'}     
print(len(a))                               #6
# a.update(3+4j , 10.8 , True)              #Error


# copy() method
a = {10 , 20 , 15 , 18}
print(a)                                     # {10, 20, 15, 18}      
b = a.copy()
print(b)                                     # {10, 20, 15, 18}   
print(a is b)                                # False  
print(a == b)                                #True
c = a
print(a is c)                                 #True


#  pop() method
a = {25 , 10.8 , 'Hyd' , True}
print(a)                                    # {25, 10.8, 'Hyd', True}  (unordered)
print(a.pop())                              # removes & prints random element   

print(a.pop())      
print(a.pop())      
print(a.pop())      
# print(a.pop())                           #Error
print(a)                                   # set()
b = {10 , 20 , 30 , 40}
# print(b.pop(2))                          #Error


# remove() method
a = {25 , 10.8 , 'Hyd' , True}
print(a)                                  # {25, 10.8, 'Hyd', True}
a.remove('Hyd')
print(a)                                  # {25, 10.8, True}

# a.remove('Sec')                         # Error


# discard() method
a = {25 , 10.8 , 'Hyd' , True}
print(a)                                  # {25, 10.8, 'Hyd', True}
a.discard('Hyd')
print(a)                                  # {25, 10.8, True}
a.discard('Sec')
print(a)                                  # {25, 10.8, True}  

# a.remove('Sec')                         # Error


# clear() method
a = {10 , 20 , 15 , 18}
print(a)                                  # {10, 20, 15, 18}
a.clear()
print(a)                                  # set()
print(len(a))                             # 0


#  union() method
a = {10 , 20 , 30 , 40}
b = [30 , 40 , 50 , 60]
print(a.union(b))                        # {10, 20, 30, 40, 50, 60}





# print(a | b)                           # Error
# print(b.union(a))                      # Error
# print(a + b)                           # Error
