
1
'''
Write  a  generator  to  divide  a  string  into  words

Hint1:  Use  generator  function  and  for   loop

Hint2:  Use  split()  method  of  str  class
'''
#output:
"""
Enter  any   string  :  Hyd is green city
Words  of  the  string
Hyd
is
green
city"""

#program
def f1():
    b=a.split(' ')
    for i in b:
        yield i


a=input("enter any string: ")
g=f1()
for x in g:
    print(x)



2

# Find  outputs
def   f1():	# function header
        yield   [10 , 20]	#returns the [10,20] to the x 
        yield  {30 , 40 , 50}	#returns the {30,40,50} to the x
        yield  60  , 70 , 80 , 90	#retuns the (60,70,80,90) to the x
        yield  100	#returns the 100 to the x of gen object
# End  of  generator
g = f1()	#creates the empty generator object
for   x   in   g:	#execute the genertor
	print(x)	#prints the returns value of yield stmt i.e [10,20]
	print(type(x)) 	#<class list>---->  <class set>----------<class tuple>------<class int>
      


3

#  Find  outputs
def   f1():# generator function header
	x = 1
	while  x <=  100000000000000000000: # unitl codition false it executes
		yield  x	# yield   the value to generator obj
		x +=  1	#x=1+1=2
# End of  generator
g = f1()	# creates the empty generator object
print('Begin')	#Begin
print(*g)		#it executes from begening to end  and ouput is 1 2 3 4 5 6 ........................ (may be memory error due * )
print('End')	#if memory error not raised then 'End' returns


4
 #  Find  outputs
g = (x * x  for  x  in  range(500000000000000000))  #empty generator creates here 
print(*g)   #Here *  it need  to store the all element in generator object so may be we get memory error ---- or print the 0^0 1^2 2^2 ..................500000000000000000^2


5
# Find  outputs  (Home  work)
def   f1(begin , end):
	while  begin  <=  end:  #while condition false
			print('Hello')  #Hello
			yield  begin    #10
			begin += 1  #10+1=11.........19+1=20
	print('End  of  generator')#End of generator
#end of the generator  function
g = f1(10 , 20)	# creates an empty generator
print('Before')	# Before
print(list(g))	# waiting time for store the  all the so many values in generator
print('After')  #After
print(next(g))#stop iteration due to already execute the generator


6

def      f1():
	print('One')	#One
	yield    1		#1 is yield to the generator object m
	print('Two')	#Two
	yield    2		#2 is yield to the generator obje m
	print('Three')	#Three
	yield    3		#3 is yield to the generator object m
	print('End')	#End
# End  of  generator
g = f1() 	#creates the empty generator
for   m   in   g:	# execute the generator
	print(m)		#One<nextline>Two<nextline>Three
x ,  y ,  z  =  f1()  #x,y,z=1,2,3
print(x)	#1
print(y)	#2
print(z)	#3

7

 # Identify  error (Home  work)
'''def  f1():
        yield  10
        yield  20
        yield  30
        yield  40
a , b , c = f1()	# too many values are in generator
p , q , r , s , m = f1()	#few elements in generators'''

8

 #  Find  outputs (Home  work)
def   f1():
    yield    1  #1 is yield to the generator object
    yield    2  #2 is yield to the generator object
    yield    3  #3 is yield to the generator object
# End  of  generator
g =  f1()	#creates an empty generator
#print(len(g))	#Error due len() arg should be sequence
#print(g * 3)    #repetition is not permitted
#print(g[0])    #no index
#print(g[1 : 3])    #slicing is not possible
print(*g)   #stores the values in generator object 1 2 3