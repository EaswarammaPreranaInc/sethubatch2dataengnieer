                                  NAME:M.SAICHARAN               HOMEWORK
                                  DATE:10-11-2025

1.# Most  tricky  program
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

#Output:
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


2.# Find  outputs
import  time
class   c3:
	def  __iter__(self):
		print('__iter__  method ')
		return  reversed([10 , 20 , 15 , 18])
# End  of  the  class
itr = c3()
for  x  in   itr:
	print(x)
	time . sleep(1)
print(next(itr))#Type C3 is not a iterator

#Output:
__iter__  method 
18
15
20
10


3.# Identify  Error  (Home  work)
class   c4:
	def  _iter_(self):
		print('_iter_  method ')
		return   self
# End  of  the  class
itr = c4()
for  x  in   itr:
	print(x)

output:
TypeError: 'c4' object is not iterable


4.# Identify  Error
class   c5:
	def  _iter_(self):
		print('_iter_  method ')
# End  of  the  class
itr = c5()
for  x  in   itr:
	print(x)

output:
TypeError: 'c5' object is not iterable


5.# Identify  Error
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

output:
TypeError: 'c6' object is not iterable



6.# Find  outputs(Home  work)
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

output:
Elements  of  iterator  with  for  loop
TypeError: 'c1' object is not iterable


7.# Find  outputs (Home  work)
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

output:
TypeError: 'Remote' object is not iterable

'''

8.#Write  an  iterator  which  yields  10 , 11 , 12 , 13 , ...... 20

Hint: Use  for  loop
'''
#Program:
class TenToTwenty:
    def __iter__(self):
        self.num = 10
        return self
    def __next__(self):
        if self.num > 20:
            raise StopIteration
        value = self.num
        self.num += 1
        return value
obj = TenToTwenty()
for x in obj:
    print(x)

'''


9.#Design  an  iterator  which  yields  powers  of  two   i.e.  2 ^ 0 , 2 ^ 1 , 2 ^ 2 , ........ 2 ^ 7

Hint :  Use  for  loop
'''
#Program:
class PowerOfTwo:
    def __iter__(self):
        self.n = 0
        return self
    def __next__(self):
        if self.n > 7:
            raise StopIteration
        value = 2 ** self.n
        self.n += 1
        return value
p = PowerOfTwo()
for x in p:
    print(x)