#  How  to  iterate  generator  with  for  loop
import  time
def   f1():
	print('One')
	yield 25
	print('Two')
	yield 10.8
	print('Three')
	yield 'Hyd'
	print('Four')
# End  of  generator
g = f1()
for   x   in   g:
	print(x)                #One<next_line>25<next_line>Hello<next_line>Two<next_line>10.8<next_line>Hello<next_line>
	time.sleep(1)		#                      Three<next_line>Hyd<next_line>Hello<next_line>Four
	print('Hello')
# End  of  for  loop
print('End')                    #End
print(g)                        #<generator at <address at which generator g is stored>>
print(next(g))                  #Throws error as generator is already exhausted
g = f1()
print(next(g))                  #One<next_line>25





# Most  tricky  program
# Find  outputs(Home  work)
import  time
def   f1():
	yield  25
	yield  10.8
	yield  'Hyd'
# End  of  generator
g = f1()
print(next(g))              	#25
for  x  in   g:
	print(x)                #10.8<next_line>Hyd
print()
for  x  in  f1():
	print(x)                #25<next_line>10.8<next_line>Hyd
print()
gen = f1()
print(next(gen))            	#25
for  x  in   f1():
	print(x)                #25<next_line>10.8<next_line>Hyd
print(next(gen))            	#10.8





#Find  outputs (Home  work)
import  time
g = (x * x   for  x  in  range(5))
for  y  in   g:
	print(y)                    #0<>Hello<>1<>Hello<>4<>Hello<>9<>Hello<>16<>Hello
	time.sleep(2)
	print('Hello')
for  y  in   g:
	print(y)                    #No output as the generator has been exhausted in previous for loop





# Find  outputs (Home  work)
import  time
for y in (x*x for x in range(5)):
	print(y)                        #0<next_line>1<next_line>4<next_line>9<next_line>16                   
	time . sleep(2)
for  y  in   (x*x for x in range(5)):
	print(y)                        #0<next_line>1<next_line>4<next_line>9<next_line>16
	time . sleep(2)





# Find  outputs(Home  work)
import  time
g1 = (x * x   for  x  in  range(5))
g2 = g1
for  y  in  g1:
	print(y)                    #0<next_line>1<next_line>4<next_line>9<next_line>16
	time . sleep(2)
for  y  in  g2:
	print(y)                    #No output as g2 points to same generator which has already been exhausted
print(g1  is  g2)                   #True





#  Find  outputs (Home  work)
l = [x * x  for  x  in  range(5)]
print(l)                            #[0, 1, 4, 9, 16]
print(type(l))                      #<class 'list'>

s = {x * x  for  x  in  range(5)}
print(s)                            #{0, 1, 4, 9, 16}   <in any order>
print(type(s))                      #<class 'set'>

d = {x : x*x for x in range(5)}
print(d)                            #{0:0, 1:1, 2:4, 3:9, 4:16}
print(type(d))                      #<class 'dict'>

g = (x * x for x in range(5))
print(g)                            #<generator at  <address of generator g>
print(type(g))                      #<class 'generator'>





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
print(f1())                     #10
print(f1())                     #10
print(f1())                     #10
print()
g = f2()
print(next(g))                  #10
print(next(g))                  #20
print(next(g))                  #30
print(next(g))                  #Throws error as generator has already been exhausted





'''
Write  a  generator  to  yield  sum , difference , product  and  division  of  2  numbers

Hint:  Use  generator  function  and  for  loop  to  iterate  elements
'''

def gen(a, b):
    yield f'Sum : {a+b}'
    yield f'Difference : {a-b}'
    yield f'Product : {a*b}'
    try:
        yield f'Division : {a/b}'
    except:
        yield 'Division by zero is not permitted'

ip1 = int(input('Enter 1st number : '))
ip2 = int(input('Enter 2nd number : '))
g = gen(ip1, ip2)    
for i in g:
    print(i)





'''
Design  a  generator  to  yield  from  x (may  be  10)  to   y (may  be  20)
Hint:  Use  generator  function  and  for  loop
Hint:  Do  not  use  range  object
'''

def gen(x, y):
    while x <= y:
        yield x
        x += 1
        
ip1 = int(input('Enter start value : '))   
ip2 = int(input('Enter end value : '))  
g = gen(ip1, ip2)
for i in g:
    print(i)





'''
Write  a   generator  to  generate  fibonacci  series
1) What is fibonacci series ? ---> 0, 1, 1, 2, 3, 5, 8, .....
2) What is the formula for 10th term ? ---> 9th term + 8th term
   What is the formula for 3rd  term ? ---> 2nd term + 1st term
3) What  are  the  first  two  terms ?  --->  0  and  1
4) Use  generator  function  and  for  loop
'''

def gen(x):
    a, b = 0, 1
    while a < x:
        yield a
        a, b = b, a+b
        
ip1 = int(input('Enter the last value of fibonacci series : '))
g = gen(ip1)
for i in g:
    print(i)