# Most  tricky  program
#  Find  outputs (Home  work)
from   itertools    import    count
cnt = count()
list = [10 , 20 , 15 , 18]
z1 = zip(cnt , list)
print('while  loop')
while   True:
        try:
                print(next(z1)) #(0,10) (1,20) (2,15) (3,18)
        except:
                break
z2 = zip(list , cnt)
print('for  loop')
for  x   in    z2: 
        print(x) #(5,10) (6,20) (7,15) (8,18)
z3 = zip(cnt , list)
print(next(z3)) #(10,10)
print(*z3) #(11,20) (12,15) (13,18)
z4 = zip(list , cnt)
print(next(z4)) #(20,10)

# Find  outputs
import  time
class   c3:
	def  __iter__(self):
		print('__iter__  method ')
		return  reversed([10 , 20 , 15 , 18])
# End  of  the  class
itr = c3()
for  x  in   itr:
	print(x) #18 15 20 10
	time . sleep(1)
print(next(itr)) #error does not have __next__() method

# Identify  Error  (Home  work)
class   c4:
	def  __iter__(self):
		print('__iter__  method ')
		return   self
# End  of  the  class
itr = c4()
for  x  in   itr:
	print(x)
#__iter__ should return a iterator 

# Identify  Error
class   c5:
	def  __iter__(self):
		print('__iter__  method ')
# End  of  the  class
itr = c5()
for  x  in   itr:
	print(x)
#__iter__ should return a iterator 

# Identify  Error
class   c6:  
        def   iter(self):
                return   reversed([10 , 20 , 15 , 18])
        def  next(self):
                print('next  method')
# End  of  the  class
a  =  c6()
print(dir(c6))
for  x  in  a: 
        print(x) #error, not a iterable
while  True:
	print(next(a)) #error, not a iterator
a . next() #next method

# Find  outputs(Home  work)
class   c1:
	def   __init__(self):
		self . x =  1
	def   __iter__(self):
		print('__iter__    method')
		return  self
	def   __next__(self):
		value =  self . x
		self . x  +=  1
		return  value
# End  of  the  class
a = c1()
print('Elements  of  iterator  with  for  loop')
for   element   in   a:
	print(element) #1 2 3 4 5 
	if  element  ==  5:
               break
print('Elements  of  iterator  with  next()  function')
while    True:
	element = next(a) 
	print(element) #6 7 8 9 10
	if  element  ==  10:
		break
#end  of  while  loop
print('Elements  of  iterator  with  for  loop')
for   element   in    a:
	print(element) #11 12 13 14 15
	if  element  ==  15:
		break


#  object   'a'  --->

# Find  outputs (Home  work)
import   time
class  Remote:
	def    __init__(self):
		self . list = ['Tv 9' , 'Espn' , 'Zee Tv' , 'ETV']
		self . index = -1
	def   __iter__(self):
		return  self
	def   __next__(self):
		self . index += 1
		if   self . index  ==  len(self . list): #4
			raise  StopIteration
		return    self . list[self . index]
# End  of  the  class
r = Remote()
for  x   in    r: 
	print(x) #Tv9 Espn Zee Tv ETv
	time . sleep(1)

#  object  'r'  --->

'''
Write  an  iterator  which  yields  10 , 11 , 12 , 13 , ...... 20

Hint: Use  for  loop
'''
class c1:
	def __init__(self):
		self.x=1
	def __iter__(self):
		return self
	def __next__(self):
		val=self.x
		if val==21:
			raise StopIteration
		self.x+=1
		return val
a=c1()
while True:
	try:
		print(next(a))
	except:
		break
a=c1()
for x in a:
	print(x)
'''
Design  an  iterator  which  yields  powers  of  two   i.e.  2 ^ 0 , 2 ^ 1 , 2 ^ 2 , ........ 2 ^ 7

Hint :  Use  for  loop
'''
class c1:
	def __init__(self):
		self.x=0
	def __iter__(self):
		return self
	def __next__(self):
		val=self.x
		if val==8:
			raise StopIteration
		self.x+=1
		return pow(2,val)
a=c1()
while True:
	try:
		print(next(a))
	except:
		break
a=c1()
for x in a:
	print(x)