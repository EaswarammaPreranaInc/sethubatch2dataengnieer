'''
Write  a  generator  to  divide  a  string  into  words

Hint1:  Use  generator  function  and  for   loop

Hint2:  Use  split()  method  of  str  class
'''

def gen(ip):
    for i in ip.split():
        yield(i)
      
ip = input('Enter any string : ')
for i in gen(ip):
    print(i)        





# Find  outputs
def   f1():
        yield  [10 , 20]
        yield  {30 , 40 , 50}
        yield  60  , 70 , 80 , 90
        yield  100
# End  of  generator
g = f1()
for   x   in   g:
	print(x)
	print(type(x))              #[10, 20]<next_line><class 'list'><<next_line>{40, 50, 30}<<next_line><class 'set'><<next_line>
				     (60, 70, 80, 90)<<next_line><class 'tuple'><<next_line>100<<next_line><class 'int'>





#  Find  outputs
def   f1():
	x = 1
	while  x <= 100000000000000000000:
		yield  x
		x +=  1
# End of  generator
g = f1()
print('Begin')          #Begin
print(*g)               #1 2 3 4 5 6 7 8..... there may also be possibility of memory error incase of generator containing huge number of elements 
print('End')            #End





#  Find  outputs
g = (x * x  for  x  in  range(500000000000000000))
print(*g)               #Due to large number of elements, after a long waiting time, we will be getting memory error





# Find  outputs  (Home  work)
def   f1(begin , end):
	while  begin  <=  end:
			print('Hello')
			yield  begin
			begin += 1
	print('End  of  generator')
#end of the genrator  function
g = f1(10 , 20)
print('Before')                 #Before
print(list(g))                  #Hello(11 times)<next_line>[10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20] 
print('After')                  #After
print(next(g))                  #Error as g has already been iterated completely





#  Find    outputs (Home  work)
def      f1():
	print('One')
	yield    1
	print('Two')
	yield    2
	print('Three')
	yield    3
	print('End')
# End  of  generator
g = f1() 
for   m   in   g:
	print(m)                #One<next_line>1<next_line>Two<next_line>2<next_line>Three<next_line>3<next_line>End
x ,  y ,  z  =  f1()        #One<next_line>Two<next_line>Three
print(x)                    #1
print(y)                    #2
print(z)                    #3





# Identify  error (Home  work)
def  f1():
        yield  10
        yield  20
        yield  30
        yield  40
a , b , c = f1()                    #Throws error as there are values on the right more than the number of variables on the left
p , q , r , s , m = f1()





#  Find  outputs (Home  work)
def   f1():
	yield    1
	yield    2
	yield    3
# End  of  generator
g =  f1()
print(len(g))               #Throws error as len function expects only sequences not generators
print(g * 3)                #Throws error as generators can't be repeted or multiplied as they are empty
print(g[0])                 #Throws error as generators aren't indexed
print(g[1 : 3])             #Throws error as slicing indexes isn't possible
print(*g)                   #1 2 3