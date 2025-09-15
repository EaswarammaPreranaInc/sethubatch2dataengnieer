def word_gen(s):
    for word in s.split():
        yield word

s = input("Enter a string: ")
for w in word_gen(s):
    print(w)

#2nd program
# Find  outputs
def   f1():
        yield   [10 , 20]#[10, 20]  <class 'list'>
        yield  {30 , 40 , 50}#{30 , 40 , 50}  <class 'set'>  
        yield  60  , 70 , 80 , 90#(60, 70, 80, 90)  <class 'tuple'>
        yield  100#100   <class 'int'>
# End  of  generator
g = f1()
for   x   in   g:
	print(x)
	print(type(x))


#3rd program
#  Find  outputs
def   f1():
	x = 1
	while  x <=  100000000000000000000:
		yield  x
		x +=  1
# End of  generator
g = f1()
print('Begin')#Begin
print(*g)
print('End')


#4th program
#  Find  outputs
g = (x * x  for  x  in  range(500000000000000000))
print(*g)

#5th program
# Find  outputs  (Home  work)
def   f1(begin , end):
	while  begin  <=  end:
			print('Hello')
			yield  begin
			begin += 1
	print('End  of  generator')
#end of the genrator  function
g = f1(10 , 20)
print('Before')
print(list(g))
print('After')
#print(next(g))#Error

'''#op
Before
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
End  of  generator
[10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
After'''

#6th program
#  Find    outputs (Home  work)
def      f1():
	print('One')#one
	yield    1#1
	print('Two')#Two
	yield    2#2
	print('Three')#Three
	yield    3 #3
	print('End')#End
# End  of  generator
g = f1() 
for   m   in   g:
	print(m)
x ,  y ,  z  =  f1()  
print(x)
print(y)
print(z)x

#7th program
# Identify  error (Home  work)
def  f1():
        yield  10
        yield  20
        yield  30
        yield  40
#a , b , c = f1()#too many values to unpack (expected 3)
#p , q , r , s , m = f1()#not enough values to unpack (expected 5, got 4)


#8th program
#  Find  outputs (Home  work)
def   f1():
	yield    1
	yield    2
	yield    3
# End  of  generator
g =  f1()
#print(len(g))#Error generator has no len()
#print(g * 3)#Error due to generator cannot be repeated 
#print(g[0])#Error due to generator has no index as it empty
#print(g[1 : 3])#Error due to slicing is not possible as there is no indexing
print(*g)# 1 2 3