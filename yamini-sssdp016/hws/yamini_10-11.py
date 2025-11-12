# Most  tricky  program
#  Find  outputs (Home  work)
from   itertools    import    count
cnt = count()
list = [10 , 20 , 15 , 18]
z1 = zip(cnt , list)    # empty object
print('while  loop')
while   True:
        try:
                print(next(z1))     #(0,10)(1,20)(2,15)(3,18)
        except:
                break
z2 = zip(list , cnt)    #empty object
print('for  loop')
for  x   in    z2:
        print(x)    #(10,5)(20,6)(15,7)(18,8)
z3 = zip(cnt , list)
print(next(z3)) #(9,10)
print(*z3)  #(10,20)(11,15)(12,18)
z4 = zip(list , cnt)
print(next(z4)) #(10,14)

# Find  outputs
import  time
class   c3:
	def  __iter__(self):
		print('_iter_  method ')
		return  reversed([10 , 20 , 15 , 18])   # returns reversed object
# End  of  the  class
itr = c3()  # c3 class object is created
for  x  in   itr:   # calls __iter__ method and itr is replaced with reversed object
	print(x)    # 18,15,20,10
	time . sleep(1)
print(next(itr))    # error as there is no__next__ method

# Identify  Error  (Home  work)
class   c4:
	def  __iter__(self):
		print('_iter_  method ')
		return   self
# End  of  the  class
itr = c4()  # c4 class object
for  x  in   itr:   # calling __iter__ method so it is replaced with itr
	print(x)    # error for subsequent calls there is __next__


# Identify  Error
class   c5:
	def  __iter__(self):
		print('_iter_  method ')
# End  of  the  class
itr = c5()
for  x  in   itr:   # calls __iter__ method of c5 and none is returned by default 
	print(x)    # as none is not an iterator error

# Identify  Error
class   c6:  
        def   iter(self):
                return   reversed([10 , 20 , 15 , 18])
        def  next(self):
                print('next  method')
# End  of  the  class
a  =  c6()
print(dir(c6))  # prints all methods of c6 with environment variables
for  x  in  a:  # error as there is no __iter__ method in class c6
        print(x)
while  True:
	print(next(a))  # error as there is no __next__ method
a . next()  # next is a function not a method

# Find  outputs(Home  work)
class   c1:
	def   __init__(self):
		self . x =  1
	def   __iter__(self):
		print('_iter_    method')
		return  self
	def   __next__(self):
		value =  self . x
		self . x  +=  1
		return  value
# End  of  the  class
a = c1()
print('Elements  of  iterator  with  for  loop')
for   element   in   a:
	print(element)  #1,2,3,4,5
	if  element  ==  5:
               break
print('Elements  of  iterator  with  next()  function')
while    True:
	element = next(a)
	print(element)  # 6,7,8,9,10
	if  element  ==  10:
		break
#end  of  while  loop
print('Elements  of  iterator  with  for  loop')
for   element   in    a:
	print(element)  # 11,12,13,14,15
	if  element  ==  15:
		break


#  object   'a'  ---> x=15


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
		if   self . index  ==  len(self . list):
			raise  StopIteration
		return    self . list[self . index]
# End  of  the  class
r = Remote()
for  x   in    r:
	print(x)    # tv 9,espn,zee tv,etv
	time . sleep(1)

#  object  'r'  --->    list = ['Tv 9' , 'Espn' , 'Zee Tv' , 'ETV']
                        #index=4
# Find  outputs (Home  work)
import   time
from itertools import	*
class  a:
	def   __iter__(self):
		return  count(start=10)
		return    
# End  of  the  class
r = a()
for  x   in    r:
	print(x)    
	time . sleep(1)
	if x==20:
		break

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
        p=2**self.x
        if self.x==8:
              raise StopIteration
        self.x+=1
        return p
a=c1()
for x in a:
	print(x)

