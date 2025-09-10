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
print(a)			# {True, 10.8, None, 'Hyd', 25}
a . add(10 , 20 , 30)		# Error
a . add([10,20,30])		# Error





# Find  outputs  (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
tpl = (10 , 20 , 30)
print(a)			# {True, 10.8, 'Hyd', 25}
print(id(a))			# Address of a may be 2000
a . add(tpl)
a . add('Sec')
print(a)			# {True, 'Hyd', 10.8, (10, 20, 30), 'Sec', 25}
print(id(a))			# Same Address
print(len(a))			# 3
a . add([100 , 200 , 300])	# Error
a . add(set())			# Error
a . add({ })			# Error




# Find  outputs (Home  work)
s = set()
tpl = (10 , 20 , 15 , 18)
s . add(tpl)
print(s)			# {(10, 20, 15, 18)}
print(len(s))			# 1




# update()  method  demo program  (Home  work)
tpl = (10 , 20 , 15, 18 , 10 , 20)
s = set()
s . update(tpl)
print(len(s))			# 4
print(s)			# {10, 18, 20, 15}
s . update(25)





# Find  outputs  (Home  work)
a = [10 , 20 , 30]
b = {30 , 40,50 }
c = (50 , 60 , 70)
s = set()
s . update(a , b , c)
print(s)			# {50, 20, 70, 40, 10, 60, 30}
print(len(s))			# 7
s . add(a , b , c)		# Error




# Find  outputs  (Home  work)
a = set()
a . update('Rama Rao')
print(a)				# {'o', ' ', 'a', 'R', 'm'}
print(len(a))				# 5
a . update(3 + 4j , 10.8 , True)	# Error





# copy()  method  demo  program  (Home  work)
a = {10 , 20 , 15 , 18}
print(a)			# {10, 18, 20, 15}
b = a . copy()
print(b)			# {10, 18, 20, 15}
print(a  is  b)			# False
print(a  ==  b)			# True
c = a
print(a  is  c)			# True





# pop()  method  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
print(a)			# {'Hyd', True, 10.8, 25}
print(a . pop())		# Hyd
print(a . pop())		# True
print(a . pop())		# 10.8
print(a . pop())		# 25
print(a . pop())		# set()
print(a)			# Error
b = {10 , 20 , 30 , 40}
print(b . pop(2))		# Error





# remove()  method  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
print(a)			# {True, 10.8, 'Hyd', 25}
a . remove('Hyd')
print(a)			# {True, 10.8, 25}
a . remove('Sec')		# Error






# discard()  method  demo  program (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
print(a)			# {True, 10.8, 25, 'Hyd'}
a . discard('Hyd')
print(a)			# {True, 10.8, 25}
a . discard('Sec')
print(a)			# {True, 10.8, 25}
a . remove('Sec')		# Error





# clear()  method  demo  program (Home  work)
a = {10 , 20 , 15 , 18}
print(a)			# {10 , 20 , 15 , 18}
a . clear()
print(a)			# set()
print(len(a))			# 0





# Find  outputs  (Home work)
a = {10 , 20 , 30 , 40}
b = [30 , 40 , 50 , 60]
print(a . union(b))		# {40, 10, 50, 20, 60, 30}
print(a | b)			# Error
print(b . union(a))		# Error
print(a + b)			# Error