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
print(a)             	#{True, 25,10.8,'Hyd',None}
a . add(10 , 20 , 30)   # error bcz it takes only 1 argument
a . add([10,20,30])     # error

#2
# Find  outputs  (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
tpl = (10 , 20 , 30)
print(a)                    # {25 , 10.8 , 'Hyd' , True}
print(id(a))                # address of tuple a
a . add(tpl)  
a . add('Sec')  
print(a)      			    # {25 , 10.8 , 'Hyd' , True, (10 , 20 , 30), 'sec}
print(id(a))    	        # same address
print(len(a))  			    #6
a . add([100 , 200 , 300])  # error
a . add(set())              # error
a . add({ })                # error

#3
# Find  outputs (Home  work)
s = set()
tpl = (10 , 20 , 15 , 18)
s . add(tpl)    
print(s)         #{(10 , 20 , 15 , 18)}
print(len(s))    # 1

#4
# update()  method  demo program  (Home  work)
tpl = (10 , 20 , 15, 18 , 10 , 20)
s = set()
s . update(tpl)
print(len(s))	    # 4
print(s)	        # {10,20,15,18}
s . update(25)  	# error

#5
# Find  outputs  (Home  work)
a = [10 , 20 , 30]
b = {30 , 40,50 }
c = (50 , 60 , 70)
s = set()
s . update(a , b , c)
print(s)            #{ 10 , 20 ,30 , 40,50 , 60 , 70} in any order
print(len(s))       # 7
s . add(a , b , c)  # error


#6
# Find  outputs  (Home  work)
a = set()
a . update('Rama Rao')
print(a)                            # {'R','a','m', ' ' , 'o'}
print(len(a))                       # 5
a . update(3 + 4j , 10.8 , True)    # error

#7
# copy()  method  demo  program  (Home  work)
a = {10 , 20 , 15 , 18}
print(a)                                      # {10 , 20 , 15 , 18} in any order
b = a . copy() 
print(b)  #  {10 , 20 , 15 , 18} same as a
print(a  is  b)                               # False
print(a  ==  b)                               # True
c = a   
print(a  is  c)                               # True

#8
# pop()  method  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
print(a)                               # {25 , 10.8 , 'Hyd' , True} in any order
print(a . pop())                       #25
print(a . pop())                       # 10.8
print(a . pop())                       # Hyd
print(a . pop())                       # True
print(a . pop())                       # error
print(a)                               # set()
b = {10 , 20 , 30 , 40}
print(b . pop(2))                      # error bcz it takes only 1 argument


#9.
# remove()  method  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
print(a)                             # {25 , 10.8 , 'Hyd' , True} in any order
a . remove('Hyd')
print(a)                             # {25 , 10.8 , True}
a . remove('Sec')                    # error 

#10
# discard()  method  demo  program (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
print(a)                                  #  {25 , 10.8 , 'Hyd' , True} in any order
a . discard('Hyd')  
print(a)                                  #  {25 , 10.8 ,True}
a . discard('Sec')
print(a)                                  #  {25 , 10.8 ,True} bcz it not throws any error if the element is not found
a . remove('Sec')                         # error


#11
# clear()  method  demo  program (Home  work)
a = {10 , 20 , 15 , 18}
print(a)                         # {10 , 20 , 15 , 18} in any order
a . clear()
print(a)                         # set()
print(len(a))                    # 0

#12
# Find  outputs  (Home work)
a = {10 , 20 , 30 , 40}
b = [30 , 40 , 50 , 60]
print(a . union(b))                        # {10 , 20 , 30 , 40, 50 , 60} in any order
print(a | b)                               # error 
print(b . union(a))                        # error 
print(a + b)                               # error 
