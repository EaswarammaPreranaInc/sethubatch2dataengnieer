 #  How  to  iterate  generator  with  for  loop
import  time
def   f1():
	print('One')					
	yield  25
	print('Two')
	yield  10.8
	print('Three')
	yield  'Hyd'
	print('Four')
# End  of  generator
g = f1()
for   x   in   g:
	print(x)
	time . sleep(1)				# each yeild stop 1 second then continoue print same 
	print('Hello')
# End  of  for  loop
print('End')
print(g)
print(next(g))					# error stop itreation
g = f1()
print(next(g))

	# output
	  # One
	  # 25
	  # Hello
	  # Two
	  # 10.8
	  # Hello
	  # Three
	  # Hyd
	  # Hello
	  # Four
	  # End
	  # address of generator object
	  # one 
	  # 25
	  

 # Most  tricky  program
# Find  outputs(Home  work)
import  time
def   f1():
	yield  25
	yield  10.8
	yield  'Hyd'
# End  of  generator
g = f1()
print(next(g))
for  x  in   g:
	print(x)
print()
for  x  in   f1():
	print(x)
print()
gen = f1()
print(next(gen))
for  x  in   f1():
	print(x)
print(next(gen))
	#output
	  # 25
	  # 10.8
	  # Hyd
	  # <space>
	  # 25
	  # 10.8
	  # Hyd
	  # <space>
	  # 25
	  # 25
	  # 10.8
	  # Hyd
	  # 10.8
	 


 #Find  outputs (Home  work)
import  time
g = (x * x   for    x    in    range(5))		
for  y  in   g:
	print(y)
	time . sleep(2)						# after print 1 TO stop the 2 seconds of loop then print the next steps code 
	print('Hello')
for  y  in   g:
	print(y) 
	
	# output
	  # 0
	  # Hello
	  # 1
	  # Hello
	  # 4
	  # Hello
	  # 9
	  # Hello
	  # 16
	  # Hello
 	   
 	# next loop prints
	  # 0
	  # 1
	  # 4
	  # 9
	  # 16



 # Find  outputs (Home  work)
import  time
for  y  in   (x * x   for    x    in    range(5)):
	print(y)
	time . sleep(2)					# it hold 2 seconds when it printing of each number 
for  y  in   (x * x   for    x    in    range(5)):
	print(y)
	time . sleep(2)					# it hold 2 seconds when it printing of each number 
	
	#output
	 # 0
	 # 1
	 # 4
	 # 9
	 # 16
	 # 0
	 # 1
	 # 4
	 # 9
	 # 16
	 


 # Find  outputs(Home  work)
import  time
g1 = (x * x   for  x  in  range(5))
g2 = g1
for  y  in  g1:
	print(y)
	time . sleep(2)						 # it hold 2 seconds when it printing of each number
for  y  in  g2:
	print(y)						# all elements print there is not hold any time 
print(g1  is  g2)						# true

    # output
	# 0
	# 1
	# 4
	# 9
	# 16
	
	# 0
	# 1
	# 4
	# 9
	# 16
	# True


 #  Find  outputs (Home  work)
l = [x * x   for   x   in   range(5)]
print(l)							# [0, 1, 4, 9, 16]
print(type(l))							# <class list>

s = {x * x   for   x   in   range(5)}
print(s)							# {0, 1, 4, 9, 16}
print(type(s))							# <class set>

d = {x : x * x    for   x   in   range(5)}
print(d)							# {0:0, 1:1, 2:4, 3:9, 4:16}
print(type(d))							# <class dict>

g = (x * x   for   x   in   range(5))
print(g)							# (0, 1, 4, 9, 16)
print(type(g))							# <class tuple>


 #  Find  outputs (Home  work)
def  f1():
	return  10
	return  20
	return  30
def  f2():
	yield  10
	yield  20
	yield  30
# End  of  the  function
print(f1())							# 10
print(f1())							# 10
print(f1())							# 10
print()								# empty
g = f2()							
print(next(g))							# 10
print(next(g))							# 20
print(next(g))							# 30
print(next(g))							# stop iteration


 #  Prove  that  there  is  no  waiting  time  for  generator
from  timeit  import   timeit
print(timeit('[x * x   for  x  in  range(500) ]'))		# 22.425...
print(timeit('( x * x   for  x  in  range(500) )'))		# 0.32..


 # Prove  that  there  is  no  memory  error  for  generator
import  sys
list = [x * x   for   x   in    range(10000)]
gen = (x * x   for   x   in    range(100000000000000000000000000000000000000000000000))
print(sys . getsizeof(list))					 
print(sys . getsizeof(gen))

	#output
	 # f1
	 # End
	 # 85176
	 # 200


 '''
Write  a  generator  to  yield  sum , difference , product  and  division  of  2  numbers

Hint:  Use  generator  function  and  for  loop  to  iterate  elements
'''
	
 Enter   first  number  :   10
Enter   second  number  :   7
Sum : 17
Differnece :  3
Product :  70
Division : 1.4285714285714286


 Enter   first  number  :   10
Enter   second  number  :   0
Sum : 10
Differnece :  10
Product :  0
Division  by zero  is  not  permitted

	#output
   def add(a,b):
     yield f"sum: {a+b}"
     yield f"Product: {a*b}"
     yield f"diff: {a-b}"
     if b!=0:
        yield f"div: {a/b}"
     else:
        yield f"divide by zero is not permisible"
   x=int(input('enter 1st num: '))
   y=int(input('enter 2nd num: '))
   for i in add(x,y):
   	   print(i)



 '''
Design  a  generator  to  yield  from  x (may  be  10)  to   y (may  be  20)

Hint:  Use  generator  function  and  for  loop

Hint:  Do  not  use  range  object
'''
	#output
  def gen(x, y):
	for _ in iter(lambda: x<=y, False):
		yield x
		x=x+1
  x=int(input('enter start num: '))
  y=int(input('enter end num: '))
  for i in gen(x, y):
	print(i)
  

 Enter  start  value :  10
 Enter  end  value :  20
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


 '''
Write  a   generator  to  generate  fibonacci  series

1) What  is  fibonacci  series ?  --->  0 , 1 , 1 , 2 , 3 , 5 , 8 , .....

2) What  is  the  formula  for  10th  term ?  --->  9th  term + 8th  term
    What  is  the  formula  for  3rd  term ?  ---> 2nd  term + 1st  term

3) What  are  the  first  two  terms ?  --->  0  and  1

4) Use  generator  function  and  for  loop

'''
	#output
	  def fib(n):
		a=0
		b=1
		for i in range(a,n):
			yield a
			a,b=b,a+b
	n=int(input('enter a num: '))
	for num in fib(n):
		print(num)
	 

Enter the last value of fibonacci series:10
0
1
1
2
3
5
8
End