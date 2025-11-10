: # Most  tricky  program
#  Find  outputs (Home  work)
from   itertools    import    count
cnt = count()
list = [10 , 20 , 15 , 18]
z1 = zip(cnt , list)
print('while  loop')
while   True:
        try:
                print(next(z1))
        except:
                break
z2 = zip(list , cnt)
print('for  loop')
for  x   in    z2:
        print(x)
z3 = zip(cnt , list)
print(next(z3))
print(*z3)
z4 = zip(list , cnt)
print(next(z4))
#############################
while loop
(0, 10)
(1, 20)
(2, 15)
(3, 18)
for loop
(10, 4)
(20, 5)
(15, 6)
(18, 7)
(8, 10)
(9, 20) (10, 15) (11, 18)
(10, 12)








: # Find  outputs
import  time
class   c3:
	def  _iter_(self):
		print('_iter_  method ')
		return  reversed([10 , 20 , 15 , 18])
# End  of  the  class
itr = c3()
for  x  in   itr:
	print(x)
	time . sleep(1)
print(next(itr))
#########################
__iter__ method
18
15
20
10
next(itr) → causes TypeError: 'c3' object is not an iterator
(because __iter__ returns a reversed object, not self).




: # Identify  Error  (Home  work)
class   c4:
	def  _iter_(self):
		print('_iter_  method ')
		return   self
# End  of  the  class
itr = c4()
for  x  in   itr:
	print(x)

########################
TypeError: iter() returned non-iterator of type 'c4'
(Reason: no __next__() defined.)





: # Identify  Error
class   c5:
	def  _iter_(self):
		print('_iter_  method ')
# End  of  the  class
itr = c5()
for  x  in   itr:
	print(x)

###########################
TypeError: iter() returned non-iterator of type 'NoneType'

(__iter__ doesn’t return anything.)




: # Identify  Error
class   c6:  
        def   iter(self):
                return   reversed([10 , 20 , 15 , 18])
        def  next(self):
                print('next  method')
# End  of  the  class
a  =  c6()
print(dir(c6))
for  x  in  a: 
        print(x)
while  True:
	print(next(a)) 
a . next()
######################
TypeError: 'c6' object is not iterable








: # Find  outputs(Home  work)
class   c1:
	def   _init_(self):
		self . x =  1
	def   _iter_(self):
		print('_iter_    method')
		return  self
	def   _next_(self):
		value =  self . x
		self . x  +=  1
		return  value
# End  of  the  class
a = c1()
print('Elements  of  iterator  with  for  loop')
for   element   in   a:
	print(element)
	if  element  ==  5:
               break
print('Elements  of  iterator  with  next()  function')
while    True:
	element = next(a)
	print(element)
	if  element  ==  10:
		break
#end  of  while  loop
print('Elements  of  iterator  with  for  loop')
for   element   in    a:
	print(element)
	if  element  ==  15:
		break


#  object   'a'  --->
###############################
Elements of iterator with for loop
__iter__ method
1
2
3
4
5
Elements of iterator with next() function
6
7
8
9
10
Elements of iterator with for loop
__iter__ method
11
12
13
14
15




: # Find  outputs (Home  work)
import   time
class  Remote:
	def    _init_(self):
		self . list = ['Tv 9' , 'Espn' , 'Zee Tv' , 'ETV']
		self . index = -1
	def   _iter_(self):
		return  self
	def   _next_(self):
		self . index += 1
		if   self . index  ==  len(self . list):
			raise  StopIteration
		return    self . list[self . index]
# End  of  the  class
r = Remote()
for  x   in    r:
	print(x)
	time . sleep(1)

#  object  'r'  --->
###############################
Tv 9
Espn
Zee Tv
ETV






: '''
Write  an  iterator  which  yields  10 , 11 , 12 , 13 , ...... 20

Hint: Use  for  loop
'class MyIterator:
    def __iter__(self):
        for i in range(10, 21):
            yield i

for x in MyIterator():
    print(x)

#######################################
10
11
12
13
14
15
16
17
18
19
20




: '''
Design  an  iterator  which  yields  powers  of  two   i.e.  2 ^ 0 , 2 ^ 1 , 2 ^ 2 , ........ 2 ^ 7

Hint :  Use  for  loop
'''
##############################
class PowerOfTwo:
    def __iter__(self):
        for i in range(8):
            yield 2 ** i

for x in PowerOfTwo():
    print(x)
##################################
1
2
4
8
16
32
64
128

