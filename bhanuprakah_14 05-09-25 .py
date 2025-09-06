# Find  outputs  (Home  work)
def  change(b):
	b  = [50 , 60 , 70 , 80]
	print(b)
# End  of  the  function
a = [10 , 20 , 30 , 40]
print(a)
change(a)
print(a)
 the out is
[10, 20, 30, 40]
[50, 60, 70, 80]
[10, 20, 30, 40]

#  Find  outputs  (Home  work)
def   f1(x):
	x = 20
	print(x)
# End  of   the   function
x = 10
print(x)
f1(x)
print(x)
the output is
10
20
10
#  Find  outputs  (Home  work)
def  f1(b):
	b[2] = 25
#end  of  the  function
a = (10 , 20 , 15 , 18)
print(a)
f1(a)
print(a)
the output is
(10, 20, 15, 18)
# Find  outputs (Home  work)
square = lambda  x = 10  :   x * x
print(square(5))
print(square())
the output is
25
100

# Find  output (Home  work)
How  to  define  lambda  function   to  return  sum   of  two  arguments
print(type(add))
print(add(10 , 20)) 30
print(add(10.6 , 20.8)) 31.24
print(add('Hyder' , 'abad')) hyderabad
print(add(True , False)) true
print(add(25 , 10.8)) 35.8
print(add(3 + 4j , 5 + 6j))
print(add(10 , '20'))
print(add())
print(add) error

#  Find  outputs (Home  work)
add = lambda  a = 1 , b = 2 :  a + b
print(add(10 , 20))
the final output
30
3
# Find  outputs
all = lambda  a , b :  (a + b ,  a - b , a * b , a / b)
x = all(10 , 7)
print(type(x))
print(x)
p , q , r , s = all(9 , 2)
print(p)
print(q)
print(r)
print(s)
<class 'tuple'>
(17, 3, 70, 1.4285714285714286)
11
7
18
4.5
#  Find  outputs
a  =  lambda  :  'Hyd'
print(a())
print(a)
the ouput is...
Hyd
<function <lambda> at 0x7f1234567890>
#  Find  outputs  (Home  work)
s = 'Hyd'
print(lambda  s  :  print(s))
print(lambda  x  :  print(x) (s))
print((lambda  x  :  print(x)) (s))
(lambda  x  :  print(x)) (s)
the final output is
<function <lambda> at 0x7f1234567890>
<function <lambda> at 0x7f1234567890>
Hyd
None
Hyd
#  Find  outputs
def   f1():
	print('Hyd')
def   f2():
	print('Sec')
a = [f1 , f2]
for  x  in  a:
	     x()
a = [def   f1():  print('Hyd') ,  def   f2():  print('Sec')]
print(a)
the output  is
Hyd
Sec


