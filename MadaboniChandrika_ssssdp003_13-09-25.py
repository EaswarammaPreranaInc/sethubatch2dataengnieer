#1st program
#  How  to  iterate  generator  with  for  loop
import  time
def   f1():
	print('One')#one
	yield  25#25
	print('Two')#Two
	yield  10.8#10.8
	print('Three')#Three
	yield  'Hyd'#Hyd
	print('Four')#Four
# End  of  generator
g = f1()# 
for   x   in   g:
	print(x)
	time . sleep(1)
	print('Hello')#Hello
# End  of  for  loop
print('End')
print(g)#<class 'generator'> and some address 
#print(next(g))#Error  
g = f1()
print(next(g))


#2nd program
# Most  tricky  program
# Find  outputs(Home  work)
import  time
def   f1():
	yield  25
	yield  10.8
	yield  'Hyd'
# End  of  generator
g = f1()#Ref g points to f1() object
print(next(g))
for  x  in   g:
	print(x)#25 10.8 Hyd
print()
for  x  in   f1():
	print(x)#25 10.8 Hyd
print()
gen = f1()
print(next(gen))#25
for  x  in   f1():
	print(x)#25 10.8 Hyd 
print(next(gen))#10.8


#3rd program
#Find  outputs (Home  work)
import  time
g = (x * x   for    x    in    range(5))
for  y  in   g:
	print(y) #0 1 4 9 16 
	time . sleep(2)
	print('Hello')#Hello
for  y  in   g:
	print(y)
    time.sleep(2)
 

#4th program
# Find  outputs(Home  work)
import  time
g1 = (x * x   for  x  in  range(5))
g2 = g1#Ref g2 points to g1
for  y  in  g1:
	print(y)#0 1 4 9 16 
	time . sleep(2)
for  y  in  g2:
	print(y)
print(g1  is  g2)#True
 

#5th program
#  Find  outputs (Home  work)
l = [x * x   for   x   in   range(5)]
print(l)#[0, 1, 4, 9, 16]
print(type(l))#<class 'list'>

s = {x * x   for   x   in   range(5)}
print(s)#{0, 1, 4, 9, 16}
print(type(s))#<class 'list'>

d = {x : x * x    for   x   in   range(5)}
print(d)#{0:0, 1:1, 2:4, 3:9, 4:16}
print(type(d))#<class 'dict'>

g = (x * x   for   x   in   range(5))
print(g)#<class 'generator'> and some address
print(type(g))#<class 'function'>
  

#6th program
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
print(f1())#10
print(f1())#10
print(f1())#10
print()
g = f2()#Ref g points to f1()
print(next(g))#10
print(next(g))#20
print(next(g))#30
#print(next(g))#Error


#7th program
def op_gen(a,b):
    yield a+b
    yield a-b
    yield a*b
    if b!=0:
        yield a/b
    else:
        yield "Division by zero Error "

a=float(input("Enter first number:"))
b=float(input("Enter second number:"))

for res in op_gen(a,b):
  

#8th program
def nums_gen(x, y):
	n = x
	while n<=y:
		yield n
		n+=1
x = int(input("Enter start value: "))
y = int(input("Enter end value: "))

for num in nums_gen(x, y):
    print(num)
    print('result',res)
  


